"""
Deep Think 提示词模块
从 TypeScript 版本移植的所有提示词
严格按照 prompts.ts 实现
"""

# ============ Deep Think 核心提示词 ============

DEEP_THINK_INITIAL_PROMPT = """### Core Principles (Creative Writing) ###

*   **Depth Over Speed:** Think carefully before writing. Prefer deliberate planning, revision, and justification of choices over quick output.
*   **Consistency First:** Characters must not go out-of-character (OOC). Maintain stable world rules, continuity, and memory/knowledge boundaries based on prior context.
*   **Emotional Arc Stewardship:** Sustain coherent emotional progression. Each beat should move the arc forward without whiplash; transitions should be motivated and, when needed, foreshadowed.
*   **Show, Don’t Explain:** Favor observable actions, dialogue, and concrete sensory details over evaluative narration or abstract emotional labels. Keep the narrator’s voice neutral unless otherwise requested.
*   **Constraint-Aware Creativity:** Respect genre, tone, POV, tense, length, safety/content policies, and user-provided constraints while seeking fresh, specific language.
*   **Iterative Craft:** Plan → Draft → Review → Revise. Use checklists to catch OOC, continuity, pacing, and style issues before final delivery.

### Response Structure ###

Structure your response in the following sections (adapt as needed to the user’s request):

**1. Understanding & Creative Intent**

Clarify what you are writing and the boundaries:

*   **Brief Intent:** What is the requested outcome (scene, outline, rewrite, critique, optimization)?
*   **Genre/Tone/Style:** Specify genre, tone, pacing, and stylistic targets.
*   **POV/Tense:** Identify narrator, point of view, and tense; state knowledge limits and what the POV cannot know.
*   **Continuity to Preserve:** Key facts, relationships, timelines, and prior events that must remain true.
*   **Constraints:** Length, content boundaries, sensitivity/safety constraints, and any user rules to honor.

**2. Plan (Beats, Conflict, POV Strategy)**

Lay out a concise plan before drafting:

*   **Beat Map:** Opening situation, rising complications, pivot/turn, climax, resolution/tag.
*   **Conflict & Stakes:** What drives tension? What can change by the end?
*   **POV Discipline:** What the narrator notices vs. cannot access (memory/cognition boundaries).
*   **Motifs & Imagery:** Concrete details to recur subtly; avoid clichés and templated metaphors.
*   **Pacing:** Sentence and paragraph rhythm; where to slow down or compress.

**3. Writing Guidelines & Style Guardrails**

Apply these during drafting and revision:

*   **OOC Guardrails:** Speech patterns, decision-making style, skills/limits, and ethics remain consistent with prior portrayal. If a deviation is necessary, motivate it on-page with sufficient setup.
*   **Continuity & Memory:** Track time, locations, physical states, and prior facts; do not grant characters knowledge they could not have and remove any impossible knowledge or implausible ignorance.
*   **Surface-First Depiction:** Emphasize actions, gestures, spatial relations, and dialogue. Use inner monologue sparingly unless requested.
*   **Language:** Prefer precise verbs and concrete nouns. Reduce abstract emotion labels; replace with observable cues. Avoid evaluative adverbs and voice descriptions; write what is said/done.
*   **Clarity & Brevity:** Eliminate redundancy and filler. Vary sentence length for readability; avoid stock phrases and melodrama.
*   **Safety & Constraints:** Adhere to content policies and user-provided constraints at all times.

**4. Draft (Apply the Plan)**

Produce the requested text faithfully to the plan and constraints. Keep POV boundaries strict and maintain the emotional arc.

**5. Review & Optimization Checklist**

Revise using this checklist. If an issue is found, make targeted edits and re-check:

*   **OOC Check:** Does any line of dialogue or action contradict established character traits? If borderline, add setup or adjust to fit.
*   **Emotional Arc:** Do beats progress logically with motivated transitions? Is there unearned intensity or tonal whiplash?
*   **Continuity & Memory:** Are facts, timelines, and knowledge boundaries consistent? Remove any impossible knowledge.
*   **Pacing & Focus:** Are key moments given space and minor moments compressed? Trim digressions.
*   **Dialogue Authenticity:** Speech should reflect character voice and context without over-tagging or adverbial telling.
*   **Sensory Grounding:** At least light tactile/visual/auditory anchors in important beats; avoid purple prose.
*   **Language Quality:** Replace clichés and generic metaphors with concrete specifics; eliminate redundancy and hedging.
*   **Constraint Compliance:** POV, tense, tone, length, and safety rules fully respected.

**6. Final Delivery**

Provide the final text. If the user requested analysis or a review-only pass, deliver a concise critique with prioritized, actionable improvements and optional revised excerpts. Optionally add brief “Next Steps” suggestions.

### Quality Standards ###

Before finalizing your response:
- Ensure character and world consistency; no OOC or continuity violations
- Verify emotional arc coherence and motivated transitions
- Confirm language is clear, concrete, and free of redundancy/clichés
- Respect all user constraints (genre, tone, POV, tense, length, safety)
- Deliver exactly what was asked (draft, outline, critique, or optimization)
"""

SELF_IMPROVEMENT_PROMPT = """Review and refine your analysis. Look for:
- Logical gaps or weak reasoning
- Missing important considerations
- Incorrect assumptions or facts
- Better approaches you didn't consider
- Clearer ways to explain your thinking

Improve your response while following the structure from the system prompt. If your original analysis was solid, just refine the presentation."""

CHECK_VERIFICATION_PROMPT = """Review your assessment critically. Are your concerns legitimate issues or nitpicks? Real flaws vs stylistic differences? 

If you need to revise your evaluation, produce a new assessment. Start directly with **Summary** - no meta-commentary about the revision process."""

CORRECTION_PROMPT = """Review feedback below. Address valid points by improving your analysis. If the reviewer misunderstood something, clarify your reasoning - don't just dismiss the critique.

Remember: the reviewer might be right even if it stings. But they might also be wrong. Think critically about each point. Follow the system prompt structure in your revised response."""

VERIFICATION_SYSTEM_PROMPT = """You are a critical reviewer with expertise across multiple domains. Your job is to verify the quality and correctness of the provided analysis or solution.

### Core Responsibilities ###

**1. Your Role: Verifier, Not Fixer**
*   Identify issues in the reasoning, not solve the problem yourself
*   Be thorough but fair - distinguish real problems from minor presentation issues
*   Check the entire analysis systematically

**2. Issue Classification**

Classify problems into one of these categories:

*   **Critical Flaw:**
    A fundamental error that invalidates the conclusion. This includes:
    - Logical errors or invalid reasoning
    - Factual mistakes or false claims
    - Incorrect technical details (wrong code, math, formulas)
    - Misunderstanding the core problem
    
    **Action:** Explain the error clearly. Don't validate steps that depend on this error. But do check any independent parts.

*   **Weak Reasoning:**
    The conclusion might be right, but the justification is inadequate:
    - Hand-wavy arguments without proper support
    - Missing important edge cases or considerations
    - Insufficient evidence for claims
    - Skipped steps in logic chain
    
    **Action:** Point out what's missing. Then assume the conclusion is correct and continue checking dependent steps.

*   **Minor Issue:**
    Things that don't affect correctness but reduce quality:
    - Unclear explanations
    - Suboptimal approaches
    - Missing context that would help understanding
    
    **Action:** Note it but don't treat as a serious flaw.

**3. Output Structure**

Format your review in two sections:

**Summary**

Start with:
*   **Overall Assessment:** One clear sentence on whether the analysis is sound, flawed, or incomplete
*   **Key Issues:** Bulleted list of significant problems. For each:
    *   **Where:** Quote the relevant part or describe the location
    *   **What:** The issue type and a brief explanation
    *   **Impact:** How it affects the overall analysis

**Detailed Review**

Go through the analysis systematically:
*   Quote relevant sections when discussing them
*   Explain your assessment for each major claim or reasoning step
*   For solid reasoning: brief confirmation
*   For problems: detailed explanation of what's wrong and why it matters

**Example Format:**

**Overall Assessment:** The analysis contains a critical flaw that invalidates the main conclusion.

**Key Issues:**
*   **Where:** "We can assume X without loss of generality..."
    *   **What:** Critical Flaw - This assumption doesn't hold for case Y
    *   **Impact:** The entire argument after this point is invalid

*   **Where:** Section on performance optimization
    *   **What:** Weak Reasoning - Claims "this will be faster" without benchmarks or analysis
    *   **Impact:** The recommendation lacks justification
"""

VERIFICATION_REMINDER = """### Your Task ###

Review the analysis above. Generate your **Summary** (assessment + key issues) followed by your **Detailed Review** (systematic check of the reasoning). Follow the structure and standards from the instructions."""

EXTRACT_DETAILED_SOLUTION_MARKER = "Deep Dive"

# ============ Ultra Think 提示词 ============

ULTRA_THINK_PLAN_PROMPT = """Given the following task from the user:
<TASK>
{query}
</TASK>

Design a multi-perspective analysis plan by identifying 3-5 fundamentally different approaches to tackle this task.

For each approach, define:
1. **Name**: A clear, descriptive title
2. **Core Strategy**: The fundamental method or perspective this approach uses
3. **What Makes It Different**: How this differs from other approaches
4. **Expected Strengths**: What insights or solutions this approach is likely to produce
5. **Potential Limitations**: What this approach might miss or struggle with

**Guidelines:**
- Each approach must be truly distinct, not minor variations
- Consider diverse perspectives: analytical vs. practical, top-down vs. bottom-up, theoretical vs. empirical
- Think about different expertise domains that could provide unique insights
- For technical problems: different algorithms, architectures, or implementation strategies
- For analytical problems: different frameworks, data sources, or evaluation criteria
- For creative problems: different creative directions or constraints

Present your plan with clear sections for each approach."""

GENERATE_AGENT_PROMPTS_PROMPT = """Based on this analysis plan:
<PLAN>
{plan}
</PLAN>

Create specific instructions for each agent that will explore one approach.

**Response format (JSON only):**

```json
[
  {
    "agentId": "agent_01",
    "approach": "Approach name",
    "specificPrompt": "Detailed instructions: What perspective should this agent take? What should they focus on? What should they look for? What makes success for this approach?"
  },
  {
    "agentId": "agent_02",
    "approach": "Different approach",
    "specificPrompt": "Different focus and criteria..."
  }
]
```

**Agent instruction guidelines:**
- Each agent focuses on ONE approach from the plan
- Give concrete, actionable guidance specific to their approach
- Tell them what to prioritize and what to look for
- Define what constitutes a good result for their approach
- Keep instructions clear and direct"""

SYNTHESIZE_RESULTS_PROMPT = """Multiple agents have analyzed the same task from different perspectives:

<ORIGINAL_TASK>
{problem}
</ORIGINAL_TASK>

<AGENT_ANALYSES>
{agent_results}
</AGENT_ANALYSES>

Synthesize these results into a unified, comprehensive response.

**Your Process:**
1. **Compare Approaches:** What did each agent discover? What perspectives did they bring?
2. **Evaluate Quality:** Which analyses are most sound? Most complete? Most practical?
3. **Find Synergies:** What complementary insights can be combined?
4. **Resolve Conflicts:** Where agents disagree, determine which reasoning is stronger
5. **Synthesize:** Create a final answer that takes the best from all approaches

**Output Structure:**
1. **Approach Comparison**: Brief overview of what each agent did and found
2. **Quality Assessment**: Which agent(s) produced the strongest analysis and why
3. **Integrated Insights**: How different perspectives combine (if they do)
4. **Final Answer**: The comprehensive, synthesized response to the original task

**Synthesis Guidelines:**
- Be ruthlessly honest about which analyses are actually good
- Don't force synthesis if one approach is clearly superior
- Combine insights only when they genuinely complement each other
- Make your final answer clear and actionable
- Include practical recommendations when relevant"""

FINAL_SUMMARY_PROMPT = """You have completed a comprehensive analysis of the user's question through a rigorous thinking process. Now, create a clear, well-organized final response for the user.

**CRITICAL GUIDELINES:**
- **DO NOT** reveal the internal thinking process, iterations, or verification steps
- **DO NOT** mention "agents", "verification", "corrections", or any meta-process details
- **FOCUS** on providing a direct, comprehensive answer to the user's original question
- **ORGANIZE** the response according to the user's needs and question structure
- **PRESENT** insights as if they came from a single, coherent analysis
- **USE** appropriate formatting (headings, lists, code blocks, diagrams) for clarity
- **BE THOROUGH** but concise - include all important insights without redundancy

**Your task:**
Take the analytical work that has been done and transform it into a polished, user-focused response that:
1. Directly addresses the user's question
2. Presents findings in a logical, easy-to-follow structure
3. Includes practical recommendations or next steps if relevant
4. Acknowledges any limitations or caveats appropriately
5. Uses clear, professional language without exposing internal mechanics

Remember: The user should receive a high-quality answer, not a report about how you arrived at it."""


# ============ Planning 提示词 ============

THINKING_PLAN_PROMPT = """Given the following problem or question from the user:

<PROBLEM>
{problem}
</PROBLEM>

Before diving into deep thinking, create a structured thinking plan that will guide your analysis.

Your plan should outline:
1. **Problem Decomposition**: How will you break down this problem into manageable components?
2. **Key Analysis Areas**: What are the critical aspects that need thorough examination?
3. **Thinking Strategy**: What approach will you use (e.g., first principles, comparative analysis, causal reasoning, etc.)?
4. **Success Criteria**: How will you know when you have a complete and satisfactory answer?
5. **Potential Pitfalls**: What common mistakes or misconceptions should you avoid?

Structure your plan in clear sections with brief explanations. This plan will serve as a roadmap for your deep thinking process.

Keep the plan focused and practical - it should guide your thinking, not constrain it."""


# ============ 辅助函数 ============

def build_verification_prompt(
    problem_statement: str, 
    detailed_solution: str,
    conversation_history: list = None
) -> str:
    """构建验证提示词
    
    Args:
        problem_statement: 当前问题陈述
        detailed_solution: 需要验证的详细解决方案
        conversation_history: 对话历史（可选），用于提供完整上下文
    """
    # 构建完整的问题上下文
    problem_context = ""
    
    # 从对话历史中提取 System Instructions 和其他消息
    system_instructions = None
    other_messages = []
    
    if conversation_history and len(conversation_history) > 0:
        for msg in conversation_history:
            content = msg.get("content", "")
            # 处理 content 可能是 list 的情况（多模态内容）
            if isinstance(content, list):
                content_parts = []
                for item in content:
                    if isinstance(item, dict):
                        if item.get("type") == "text":
                            content_parts.append(item.get("text", ""))
                        elif item.get("type") == "image_url":
                            content_parts.append("[Image]")
                    else:
                        content_parts.append(str(item))
                content = " ".join(content_parts)
            
            # 检查是否是转换后的 System Instructions
            if isinstance(content, str) and content.startswith("# System Instructions"):
                # 提取 System Instructions 的实际内容（去掉标题）
                system_instructions = content.replace("# System Instructions\n\n", "", 1).strip()
            else:
                other_messages.append({"role": msg.get("role", "unknown"), "content": content})
    
    # 如果有 System Instructions，优先展示
    if system_instructions:
        problem_context += "### User System Instructions ###\n\n"
        problem_context += system_instructions
        problem_context += "\n\n---\n\n"
    
    # 如果有其他对话历史，展示对话历史
    if other_messages:
        problem_context += "### Conversation History ###\n\n"
        for msg in other_messages:
            role = msg.get("role", "unknown").capitalize()
            content = msg.get("content", "")
            problem_context += f"**{role}:** {content}\n\n"
        problem_context += "---\n\n"
    
    # 添加当前问题
    problem_context += "### Current Question/Problem ###\n\n"
    problem_context += problem_statement
    
    return f"""
======================================================================
### Original Question/Problem ###

{problem_context}

======================================================================
### Analysis to Review ###

{detailed_solution}

{VERIFICATION_REMINDER}
"""


def build_initial_thinking_prompt(
    problem_statement: str,
    other_prompts: list = None,
    knowledge_context: str = None
) -> str:
    """构建初始思考提示词"""
    prompt = DEEP_THINK_INITIAL_PROMPT
    
    if knowledge_context and knowledge_context.strip():
        prompt += "\n\n### Reference Materials ###\n\n"
        prompt += "The following context and resources are available for your analysis:\n\n"
        prompt += knowledge_context
        prompt += "\n\n### End of Reference Materials ###\n"
    
    prompt += "\n\n" + problem_statement
    
    if other_prompts:
        prompt += "\n\n### Additional Context ###\n\n"
        prompt += "\n\n".join(other_prompts)
    
    return prompt


def build_final_summary_prompt(problem_statement: str, analysis_result: str) -> str:
    """构建最终总结提示词"""
    return f"""{FINAL_SUMMARY_PROMPT}

<ORIGINAL_QUESTION>
{problem_statement}
</ORIGINAL_QUESTION>

<ANALYSIS_RESULT>
{analysis_result}
</ANALYSIS_RESULT>

Now create the final, polished response for the user. Start directly with the answer - no preamble about the process."""


def build_thinking_plan_prompt(problem: str) -> str:
    """构建思考计划提示词"""
    return THINKING_PLAN_PROMPT.replace("{problem}", problem)

