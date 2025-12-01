"""
OpenAI 客户端包装器
用于调用后端 LLM 提供商
"""
from typing import Optional, Dict, Any, List, AsyncIterator
from openai import AsyncOpenAI
import json
import logging
import httpx
import asyncio

logger = logging.getLogger(__name__)


class EmptyResponseError(Exception):
    """Raised when the backend returns an empty choices response twice."""
    pass


class OpenAIClient:
    """OpenAI 客户端包装器"""
    
    def __init__(self, base_url: str, api_key: str, rpm: Optional[int] = None, max_retry: int = 3, use_response_api: bool = False):
        # OpenAI客户端自己会管理连接，不需要我们操心
        self.client = AsyncOpenAI(
            base_url=base_url,
            api_key=api_key,
            max_retries=max_retry,
        )
        self.rpm = rpm
        self.rate_limiter = None
        self.use_response_api = use_response_api
        
        # 统计信息
        self.api_calls = 0
        self.total_tokens = 0
        
        # 如果设置了RPM限制，导入限流器
        if rpm:
            from utils.rate_limiter import rate_limiter
            self.rate_limiter = rate_limiter
    
    def _prepare_temperature(self, temperature: Optional[float], kwargs: Dict[str, Any]) -> (Optional[float], Dict[str, Any]):
        """
        规范化 temperature：
        - 若 kwargs 中包含 temperature，则以其为准并移除避免重复
        - 将数值限制在 [0.0, 1.0] 区间，兼容部分提供商（如 Moonshot）
        """
        local_kwargs = dict(kwargs) if kwargs is not None else {}
        if "temperature" in local_kwargs and local_kwargs["temperature"] is not None:
            temperature = local_kwargs.pop("temperature")
        if temperature is None:
            return None, local_kwargs
        try:
            t = float(temperature)
        except Exception:
            logger.warning(f"收到非法 temperature 值: {temperature}，将回退为 0.6")
            t = 0.6
        if t < 0.0:
            logger.warning(f"temperature {t} < 0，已夹紧到 0.0")
            t = 0.0
        if t > 1.0:
            logger.warning(f"temperature {t} > 1.0，已夹紧到 0.6 以兼容部分提供商限制")
            t = 0.6
        return t, local_kwargs
    
    def get_statistics(self) -> Dict[str, int]:
        """获取统计信息"""
        return {
            "api_calls": self.api_calls,
            "total_tokens": self.total_tokens
        }
    
    async def generate_text(
        self,
        model: str,
        prompt: str = None,
        messages: List[Dict[str, Any]] = None,
        system: str = None,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> str:
        """
        生成文本
        支持多模态内容（文本和图片）
        
        Args:
            model: 模型名称
            prompt: 提示词(如果不使用messages，可以是字符串或多模态内容)
            messages: 消息列表（支持多模态content）
            system: 系统提示词
            temperature: 温度参数
            max_tokens: 最大token数
        
        Returns:
            生成的文本
        """
        # RPM限制 - 在调用后端API之前等待
        if self.rate_limiter and self.rpm:
            await self.rate_limiter.wait_for_rate_limit(
                f"backend_api_{model}",
                self.rpm,
                60
            )
        
        # 构建消息列表
        if messages is None:
            messages = []
            if system:
                messages.append({"role": "system", "content": system})
            if prompt:
                # prompt 可以是字符串或多模态内容
                messages.append({"role": "user", "content": prompt})
        else:
            # 如果提供了system,插入到消息列表开头
            if system:
                messages = [{"role": "system", "content": system}] + messages
        
        # 统一规范化温度，避免提供商返回 400
        temperature, kwargs = self._prepare_temperature(temperature, kwargs)
        
        # 当启用 response_api 时，使用流式接口并在本地聚合，向后兼容返回完整文本
        if self.use_response_api:
            stream = await self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True,
                **kwargs
            )
            self.api_calls += 1
            chunks: List[str] = []
            async for chunk in stream:
                if not chunk.choices or len(chunk.choices) == 0:
                    continue
                if chunk.choices[0].delta and chunk.choices[0].delta.content:
                    chunks.append(chunk.choices[0].delta.content)
            return "".join(chunks)
        
        response = await self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )
        
        # 统计 API 调用
        self.api_calls += 1
        if hasattr(response, 'usage') and response.usage:
            self.total_tokens += response.usage.total_tokens
        
        # 检查响应是否包含 choices
        if not response.choices or len(response.choices) == 0:
            logger.error(f"API 返回空响应，自动重试一次: model={model}")
            # 重试一次
            await asyncio.sleep(2)
            retry_response = await self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs
            )
            # 统计 API 调用
            self.api_calls += 1
            if hasattr(retry_response, 'usage') and retry_response.usage:
                self.total_tokens += retry_response.usage.total_tokens
            # 再次检查
            if not retry_response.choices or len(retry_response.choices) == 0:
                logger.error(f"API 两次返回空响应: model={model}")
                raise EmptyResponseError(f"API 返回空响应两次，模型: {model}")
            return retry_response.choices[0].message.content
        
        return response.choices[0].message.content
    
    async def generate_object(
        self,
        model: str,
        prompt: str,
        response_format: Dict[str, Any],
        temperature: float = 0.7,
        **kwargs
    ) -> Dict[str, Any]:
        """
        生成结构化对象(JSON)
        
        Args:
            model: 模型名称
            prompt: 提示词
            response_format: 响应格式定义
            temperature: 温度参数
        
        Returns:
            解析后的JSON对象
        """
        # RPM限制 - 在调用后端API之前等待
        if self.rate_limiter and self.rpm:
            await self.rate_limiter.wait_for_rate_limit(
                f"backend_api_{model}",
                self.rpm,
                60
            )
        
        # 统一规范化温度，避免提供商返回 400
        temperature, kwargs = self._prepare_temperature(temperature, kwargs)
        
        # 当启用 response_api 时，使用流式接口并在本地聚合文本后再解析 JSON
        if self.use_response_api:
            stream = await self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                response_format={"type": "json_object"},
                stream=True,
                **kwargs
            )
            self.api_calls += 1
            chunks: List[str] = []
            async for chunk in stream:
                if not chunk.choices or len(chunk.choices) == 0:
                    continue
                if chunk.choices[0].delta and chunk.choices[0].delta.content:
                    chunks.append(chunk.choices[0].delta.content)
            text = "".join(chunks)
            try:
                return json.loads(text)
            except json.JSONDecodeError:
                # 尝试从代码块中提取JSON
                if "```json" in text:
                    json_text = text.split("```json")[1].split("```")[0].strip()
                elif "```" in text:
                    json_text = text.split("```")[1].split("```")[0].strip()
                else:
                    json_text = text.strip()
                return json.loads(json_text)
        
        response = await self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            response_format={"type": "json_object"},
            **kwargs
        )
        
        # 统计 API 调用
        self.api_calls += 1
        if hasattr(response, 'usage') and response.usage:
            self.total_tokens += response.usage.total_tokens
        
        # 检查响应是否包含 choices
        if not response.choices or len(response.choices) == 0:
            logger.error(f"API 返回空响应，自动重试一次: model={model}")
            # 重试一次
            await asyncio.sleep(2)
            retry_response = await self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                response_format={"type": "json_object"},
                **kwargs
            )
            # 统计 API 调用
            self.api_calls += 1
            if hasattr(retry_response, 'usage') and retry_response.usage:
                self.total_tokens += retry_response.usage.total_tokens
            if not retry_response.choices or len(retry_response.choices) == 0:
                logger.error(f"API 两次返回空响应: model={model}")
                raise EmptyResponseError(f"API 返回空响应两次，模型: {model}")
            text = retry_response.choices[0].message.content
        else:
            text = response.choices[0].message.content
        
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            # 尝试从代码块中提取JSON
            if "```json" in text:
                json_text = text.split("```json")[1].split("```")[0].strip()
            elif "```" in text:
                json_text = text.split("```")[1].split("```")[0].strip()
            else:
                json_text = text.strip()
            
            return json.loads(json_text)
    
    async def stream_text(
        self,
        model: str,
        messages: List[Dict[str, Any]],
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> AsyncIterator[str]:
        """
        流式生成文本
        支持多模态内容（文本和图片）
        
        Args:
            model: 模型名称
            messages: 消息列表（支持多模态content）
            temperature: 温度参数
            max_tokens: 最大token数
        
        Yields:
            文本块
        """
        # RPM限制 - 在调用后端API之前等待
        if self.rate_limiter and self.rpm:
            await self.rate_limiter.wait_for_rate_limit(
                f"backend_api_{model}",
                self.rpm,
                60
            )
        
        # 统一规范化温度，避免提供商返回 400
        temperature, kwargs = self._prepare_temperature(temperature, kwargs)
        
        stream = await self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
            **kwargs
        )
        
        # 统计 API 调用
        self.api_calls += 1
        
        async for chunk in stream:
            # 检查 chunk 是否包含 choices
            if not chunk.choices or len(chunk.choices) == 0:
                logger.warning(f"流式响应中收到空 chunk: model={model}")
                continue
            
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content


def create_client(base_url: str, api_key: str, rpm: Optional[int] = None, max_retry: int = 3, use_response_api: bool = False) -> OpenAIClient:
    """创建OpenAI客户端"""
    return OpenAIClient(base_url, api_key, rpm, max_retry, use_response_api)

