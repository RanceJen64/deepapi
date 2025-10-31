幫我分析並修正@prompts.py 中 ‘Deep Think 核心提示词’ 的區塊
‘Deep Think 核心提示词’  內容請保持英文。

Deep Think 流程包含
      initial
      improvement
      verification
      correction
      summary
分別是
@deep_think.py (20-24) 
的部分，保持各流程的職能下對，將其改為更偏向對「創意寫作」（包含對如何進行給定創意寫作的分析，review，優化等等參考現有流程），分析寫作中有沒有 OOC，維持情感弧度，角色的正確記憶及認知邊界，可略為參考 @writing_rule.md 內我平常使用 AI 時的 prompt。

不要額外的輔助函式，只要輸出修改後的
DEEP_THINK_INITIAL_PROMPT
SELF_IMPROVEMENT_PROMPT
CHECK_VERIFICATION_PROMPT
CORRECTION_PROMPT
VERIFICATION_SYSTEM_PROMPT
VERIFICATION_REMINDER
EXTRACT_DETAILED_SOLUTION_MARKER
FINAL_SUMMARY_PROMPT