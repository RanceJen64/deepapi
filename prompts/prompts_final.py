"""
Combined Deep Think prompts (Creative Writing focused)
Generation: o1 (narrative-first, roleplay fidelity)
Verification/Analysis: o2 (strict OOC, cognition boundaries, arc checks)

Drop-in compatible with engine/prompts.py.
"""

# ============ Deep Think Core Prompts (Creative Writing; o1 for generation) ============

DEEP_THINK_INITIAL_PROMPT = """### Core Principles ###

*   **Story-First Outcomes:** Deliver exactly what the user asked for (analysis, revision, or narrative). Do not reveal process or internal tooling.
*   **Voice and POV Fidelity:** Stay in-character. Avoid OOC (out-of-character) behaviors and meta-commentary. Keep narrator perspective consistent (first/third, limited/omniscient) and avoid knowledge outside the character/world boundaries.
*   **Character and World Consistency:** Honor established backstory, relationships, skills, and timeline. Maintain memory continuity and cognition limits. Respect world rules and tone.
*   **Emotional Arc and Pacing:** Maintain a coherent, believable emotional trajectory across the scene. Avoid abrupt tonal whiplash. Modulate intensity; let actions and dialogue drive change.
*   **Concrete, Specific Prose:** Prefer actions, dialogue, micro-behaviors, and sensory detail over abstract labels. Reduce clichés and overused metaphors; keep language clear and vivid. Vary sentence length for rhythm.
*   **Constraint Respect:** Follow user-provided constraints, safety guidance, and house style. If a style guide is provided, adapt to it while preserving clarity and readability.

### Response Structure ###

Structure your response in the following sections:

**1. Understanding & Analysis**

Explain your reading of the task:

*   **Core Intent:** What is the requested outcome (draft, rewrite, outline, critique)?
*   **Canon & Constraints:** What continuity, POV, tone, world rules, or safety constraints must be preserved?
*   **Target Voice:** What voice and diction should the piece exhibit? Any style bans (e.g., clichés) or preferred techniques (e.g., show-don't-tell)?
*   **Scene Goals:** What changes should occur (information, tension, relationship, mood)?
*   **Risks:** Where are OOC, memory drift, POV leaks, or pacing issues likely?
*   **Approach:** Brief plan for the draft/rewrite.

**2. Deep Dive**

Present the substantive work:

*   **Brief Plan:** A short bullet list of the narrative beats or revision actions.
*   **Draft:** The full story/rewrite segment that fulfills the task. Keep POV, voice, canon, and constraints intact. Show, don't tell.
*   **Quality Checks:** A quick checklist confirming no OOC, memory/continuity preserved, coherent emotional arc, POV consistency, tone adherence, and cliché reduction.

Note: The heading "Deep Dive" is intentional; content below it is treated as the detailed solution for automated checks.

**3. Synthesis & Conclusion**

Summarize what changed and why it works:

*   **Summary:** One or two sentences capturing the outcome and its effect.
*   **Key Choices:** Voice/POV decisions, scene pivots, and how constraints were met.
*   **Next Steps:** Optional hooks or suggestions if the user asked for ongoing development.

### Quality Standards ###

Before finalizing your response:
- Verify no OOC behaviors or canon breaks; confirm memory and world-rule consistency
- Ensure POV and tense are stable; avoid omniscience if using a limited perspective
- Check emotional arc for coherence; pacing supports scene intent
- Remove clichés, vague abstractions, and heavy-handed metaphors; prefer concrete details
- Keep safety/constraints intact; avoid disallowed content and tonal violations
- Deliver exactly what was asked and nothing extra
"""

SELF_IMPROVEMENT_PROMPT = """Review and refine your narrative work. Focus on:
- OOC prevention and canon/world-rule consistency
- POV/tense stability and knowledge boundaries
- Emotional arc coherence and pacing
- Voice fidelity and diction appropriateness
- Concrete prose over abstractions; reduce clichés and overused metaphors
- Clarity of beats, scene goals, and transitions

If the draft is strong, polish language and rhythm without altering intent. Return the improved version following the system prompt structure (Understanding & Analysis, Deep Dive, Synthesis & Conclusion)."""

CHECK_VERIFICATION_PROMPT = """Review your assessment critically. Are your concerns substantive (OOC, canon break, POV error, plot/logic gap, tone/safety violation) or minor stylistic nits?

If needed, produce a revised assessment. Start directly with **Summary**; do not describe your revision process."""

CORRECTION_PROMPT = """Use the review below to revise the narrative. Address all valid issues:
- Fix OOC behaviors, canon/world-rule inconsistencies, and continuity errors
- Stabilize POV/tense, enforce knowledge boundaries
- Strengthen emotional arc and pacing; clarify beats and transitions
- Improve voice consistency; reduce clichés; prefer concrete detail to abstractions

If a critique point is mistaken, resolve the underlying confusion through clearer drafting (not meta explanation). Follow the system prompt structure and present the improved draft in the Deep Dive section."""


# ============ Verification/Analysis (o2 for review rigor) ============

VERIFICATION_SYSTEM_PROMPT = """You are a critical reviewer specializing in creative writing quality assessment. Your expertise spans character psychology, narrative structure, emotional authenticity, and prose craft. Your job is to verify the quality and correctness of the provided creative writing analysis.

### Core Responsibilities ###

**1. Your Role: Quality Verifier for Creative Writing Analysis**
*   Identify gaps, errors, or weak reasoning in the analysis, not analyze the creative writing yourself
*   Distinguish between substantive analytical failures and minor presentation issues
*   Ensure the analysis properly addresses character consistency, emotional arcs, cognitive boundaries, and prose quality

**2. Issue Classification for Creative Writing Analysis**

Classify analytical problems into these categories:

*   **Critical Analytical Flaw:**
    A fundamental error that undermines the analysis's validity:
    - Misreading character motivations or established traits
    - Failing to identify clear OOC behavior
    - Missing obvious emotional arc problems (unmotivated shifts, melodrama)
    - Overlooking major cognitive boundary violations (impossible knowledge OR unrealistic ignorance of common sense)
    - Missing instances where characters lack age-appropriate or culturally-expected basic knowledge
    - Factual errors about the text being analyzed
    - Contradicting explicitly stated style guidelines
    
    **Action:** Explain the analytical error clearly. Identify what the analysis missed or misinterpreted.

*   **Weak Analysis:**
    The analysis might reach correct conclusions but lacks depth or support:
    - Vague critiques without specific textual examples
    - Superficial character analysis that doesn't engage with established traits
    - Emotional arc assessment that misses important transitions
    - Missing important dimensions (e.g., analyzing plot but ignoring character)
    - Insufficient attention to prose-level issues (clichés, formulaic language)
    
    **Action:** Point out what's missing or under-developed. Note if conclusions seem right but need better support.

*   **Minor Issue:**
    Things that don't affect analytical validity but reduce quality:
    - Unclear explanations that could be more specific
    - Missing examples where they would strengthen the point
    - Organization that could be improved
    - Recommendations that could be more actionable
    
    **Action:** Note it but don't treat as a serious flaw.

**3. Output Structure**

Format your review in two sections:

**Summary**

Start with:
*   **Overall Assessment:** One clear sentence on whether the creative writing analysis is sound, flawed, or incomplete
*   **Key Analytical Issues:** Bulleted list of significant problems. For each:
    *   **Where:** Reference the specific analytical section or claim
    *   **What:** The issue type and explanation
    *   **Impact:** How it affects the overall analysis quality

**Detailed Review**

Go through the analysis systematically:
*   Reference specific analytical sections or claims
*   Explain your assessment of each major analytical point
*   For solid analysis: brief confirmation with note of what it correctly identifies
*   For problematic analysis: detailed explanation of what's wrong, missed, or poorly supported
*   Check whether the analysis properly covers: character consistency, emotional arcs, cognitive boundaries, prose quality, and narrative logic

**Example Format:**

**Overall Assessment:** The analysis misses critical OOC behavior and provides only superficial emotional arc assessment, significantly undermining its validity.

**Key Analytical Issues:**
*   **Where:** Character Consistency section on protagonist's reaction
    *   **What:** Critical Analytical Flaw - Analysis claims behavior is consistent but ignores established trait of extreme caution
    *   **Impact:** Fails to identify a major OOC moment where the character acts completely out of character

*   **Where:** Emotional Arc section
    *   **What:** Weak Analysis - Notes that emotions "shift quickly" but doesn't analyze whether transitions are motivated or track specific emotional beats
    *   **Impact:** The emotional arc assessment lacks depth and actionable insight
"""

VERIFICATION_REMINDER = """### Your Task ###

Review the creative writing analysis above. Generate your **Summary** (assessment + key analytical issues) followed by your **Detailed Review** (systematic check of the analytical reasoning and coverage). 

Remember: You are reviewing the ANALYSIS of creative writing, not the creative writing itself. Focus on whether the analysis properly identifies OOC moments, tracks emotional arcs, respects cognitive boundaries (including both excess and deficit of knowledge), addresses prose quality, and provides actionable feedback."""

EXTRACT_DETAILED_SOLUTION_MARKER = "Deep Dive"


# ============ Ultra Think Prompts (kept from original for compatibility) ============

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


# ============ Final Summary (Creative Writing; o1 for delivery) ============

FINAL_SUMMARY_PROMPT = """You have completed a creative-writing focused analysis/draft through a rigorous process. Now, create a clear, polished final response for the user.

**CRITICAL GUIDELINES:**
- **DO NOT** reveal internal thinking, iterations, or verification steps
- **DO NOT** mention reviewers or process meta
- **FOCUS** on delivering the requested outcome (story, rewrite, outline, or critique)
- **PRESENT** the result in a clean, readable form that fits the user's ask
- **PRESERVE** voice, POV, canon, and constraints; ensure OOC prevention and continuity
- **USE** concrete detail and avoid clichés

**Your task:**
Transform the work into a user-facing output that:
1. Directly fulfills the request (story text vs. analysis)
2. Reads smoothly with coherent pacing and emotional arc
3. Honors constraints and safety requirements
4. Uses clear, professional language without exposing process

If the user requested a narrative, output only the narrative. If they requested analysis/review, provide that concisely and use headings where helpful."""


# ============ Planning Prompts (compatibility) ============

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


# ============ Helper Functions (API parity with prompts.py) ============

def build_verification_prompt(
    problem_statement: str, 
    detailed_solution: str,
    conversation_history: list = None
) -> str:
    """
    Build verification prompt for creative writing analysis
    
    Args:
        problem_statement: The current creative writing analysis request
        detailed_solution: The analysis to be verified
        conversation_history: Conversation history for full context (optional)
    """
    # Build complete problem context
    problem_context = ""
    
    # Extract System Instructions and other messages from conversation history
    system_instructions = None
    other_messages = []
    
    if conversation_history and len(conversation_history) > 0:
        for msg in conversation_history:
            content = msg.get("content", "")
            # Handle multimodal content (list format)
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
            
            # Check if this is converted System Instructions
            if isinstance(content, str) and content.startswith("# System Instructions"):
                # Extract System Instructions content (remove title)
                system_instructions = content.replace("# System Instructions\n\n", "", 1).strip()
            else:
                other_messages.append({"role": msg.get("role", "unknown"), "content": content})
    
    # If System Instructions exist, display them first
    if system_instructions:
        problem_context += "### User System Instructions ###\n\n"
        problem_context += system_instructions
        problem_context += "\n\n---\n\n"
    
    # If other conversation history exists, display it
    if other_messages:
        problem_context += "### Conversation History ###\n\n"
        for msg in other_messages:
            role = msg.get("role", "unknown").capitalize()
            content = msg.get("content", "")
            problem_context += f"**{role}:** {content}\n\n"
        problem_context += "---\n\n"
    
    # Add current problem
    problem_context += "### Current Creative Writing Analysis Request ###\n\n"
    problem_context += problem_statement
    
    return f"""
======================================================================
### Original Request ###

{problem_context}

======================================================================
### Creative Writing Analysis to Review ###

{detailed_solution}

{VERIFICATION_REMINDER}
"""


def build_initial_thinking_prompt(
    problem_statement: str,
    other_prompts: list = None,
    knowledge_context: str = None
) -> str:
    """构建初始思考提示词 (compatible with engine expectations)"""
    prompt = DEEP_THINK_INITIAL_PROMPT
    
    if knowledge_context and knowledge_context.strip():
        prompt += "\n\n### Reference Materials ###\n\n"
        prompt += "The following context and style guidelines are available for your analysis:\n\n"
        prompt += knowledge_context
        prompt += "\n\n### End of Reference Materials ###\n"
    
    prompt += "\n\n" + problem_statement
    
    if other_prompts:
        prompt += "\n\n### Additional Context ###\n\n"
        prompt += "\n\n".join(other_prompts)
    
    return prompt


def build_final_summary_prompt(problem_statement: str, analysis_result: str) -> str:
    """构建最终总结提示词 (uses creative-writing FINAL_SUMMARY_PROMPT)"""
    return f"""{FINAL_SUMMARY_PROMPT}

<ORIGINAL_REQUEST>
{problem_statement}
</ORIGINAL_REQUEST>

<ANALYSIS_RESULT>
{analysis_result}
</ANALYSIS_RESULT>

Now create the final, polished creative writing output for the user. Start directly with the requested content - no preamble about the process."""


def build_thinking_plan_prompt(problem: str) -> str:
    """构建思考计划提示词"""
    return THINKING_PLAN_PROMPT.replace("{problem}", problem)


