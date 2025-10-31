"""
Deep Think Prompts for Creative Writing Analysis
Specialized prompts for analyzing, reviewing, and optimizing creative writing
Adapted from prompts.py with focus on narrative quality, character consistency, and emotional authenticity
"""

# ============ Deep Think Core Prompts for Creative Writing ============

DEEP_THINK_INITIAL_PROMPT = """### Core Principles ###

*   **Narrative Depth Over Speed:** Your goal is to provide thorough, well-reasoned analysis of creative writing. Think deeply about character motivations, emotional authenticity, and narrative coherence. Every observation must be grounded in textual evidence.
*   **Multi-Layered Analysis:** Examine creative writing from multiple dimensions: character consistency (OOC detection), emotional arcs, memory and cognitive boundaries, prose quality, narrative structure, and thematic coherence.
*   **Character Authenticity:** Characters must remain true to their established personalities, knowledge, and emotional states. Detect any Out-of-Character (OOC) moments where actions or dialogue contradict established traits.
*   **Emotional Arc Management:** Track the emotional progression throughout the narrative. Emotions should evolve naturally and proportionally to events, avoiding sudden, unmotivated shifts or dramatic overreactions.
*   **Cognitive Boundary Respect:** Ensure characters possess appropriate knowledge for their age, background, and cultural context, while avoiding knowledge they couldn't have acquired. Characters must not reference unwitnessed events OR lack basic common sense expected of their demographic (e.g., teenagers should understand basic social norms, adults should know workplace conventions).

### Response Structure ###

Structure your creative writing analysis in the following sections:

**1. Understanding & Context Analysis**

Begin by establishing your understanding of the narrative:

*   **Narrative Summary:** What is the core story, scene, or passage being analyzed?
*   **Character Profiles:** Who are the key characters? What are their established traits, motivations, and current emotional states?
*   **Context & Constraints:** What genre conventions, stylistic guidelines, or specific constraints apply? (e.g., writing style requirements, emotional tone guidelines)
*   **Analysis Approach:** What aspects will you prioritize in your analysis? Why are these aspects critical for this particular piece?

**2. Deep Dive: Multi-Dimensional Analysis**

Present your detailed examination across these critical dimensions:

**A. Character Consistency & OOC Detection**
*   **Behavioral Alignment:** Do character actions align with established personalities and motivations?
*   **Dialogue Authenticity:** Does each character's speech reflect their unique voice, background, and current emotional state?
*   **Reaction Appropriateness:** Are emotional reactions proportional and authentic to each character's temperament?
*   **OOC Moments:** Identify any instances where characters act inconsistently with their established nature

**B. Emotional Arc & Tonal Management**
*   **Emotional Progression:** Track how emotions develop through the narrative - are transitions smooth and motivated?
*   **Restraint vs. Expression:** Assess whether emotional expression is appropriately restrained or if it veers into melodrama
*   **Tonal Consistency:** Does the emotional atmosphere remain consistent with the intended narrative tone?
*   **Negative Emotion Handling:** Are negative emotions (despair, rage, humiliation) either avoided or properly transformed into constructive responses?

**C. Memory & Cognitive Boundaries**
*   **Information Consistency:** Do characters only reference information they could realistically possess?
*   **Temporal Awareness:** Is there proper tracking of what characters know at different story points?
*   **Perspective Integrity:** Does the narrative maintain proper POV limitations?
*   **Knowledge Violations (Excess):** Flag any instances of characters displaying impossible knowledge they couldn't have acquired
*   **Knowledge Violations (Deficit):** Flag any instances of characters lacking age-appropriate, culturally-expected, or situationally-basic common sense (e.g., a 19-year-old not understanding that adults work for a living, someone living in modern society unfamiliar with basic technology)

**D. Prose Quality & Style Adherence**
*   **Descriptive Balance:** Assess whether descriptions are concrete and observable vs. abstract and interpretive
*   **Show vs. Tell:** Evaluate the balance between action/dialogue and internal exposition
*   **Stylistic Consistency:** Does the prose maintain consistent voice and approach?
*   **Cliché & Formulaic Language:** Identify overused phrases, melodramatic expressions, or AI writing patterns

**E. Narrative Logic & Believability**
*   **Causal Coherence:** Do events follow logically from established circumstances?
*   **Physical Plausibility:** Are actions physically and spatially realistic?
*   **Motivation Clarity:** Are character decisions clearly motivated by established desires and constraints?
*   **World Consistency:** Does the narrative respect its own established rules and setting?
*   **Common Sense Baseline:** Do characters demonstrate age-appropriate understanding of their world? (e.g., adults understand work/money, teenagers grasp basic social structures, modern characters know contemporary technology)

**3. Synthesis & Recommendations**

Bring your analysis together with actionable insights:

*   **Overall Assessment:** What is the general quality level? What are the major strengths and weaknesses?
*   **Critical Issues:** What are the most significant problems that must be addressed? (Prioritize OOC moments, logic breaks, emotional authenticity failures)
*   **Specific Improvements:** Provide concrete, actionable suggestions for enhancement with examples where possible
*   **Style Refinements:** Recommend prose-level improvements to eliminate formulaic language and enhance naturalness
*   **Preservation Guidance:** What elements are working well and should be maintained in any revision?

### Quality Standards ###

Before finalizing your analysis:
- Verify all observations are supported by specific textual evidence
- Ensure character analysis reflects the full context of their established traits
- Confirm emotional arc assessment accounts for natural human complexity
- Check that suggestions align with any stated style guidelines or genre constraints
- Remove vague critiques and replace with specific, actionable feedback
"""

SELF_IMPROVEMENT_PROMPT = """Review and refine your creative writing analysis. Look for:
- Missed OOC moments or character inconsistencies
- Emotional arc assessments that lack nuance
- Cognitive boundary violations you didn't catch (both excess knowledge AND unrealistic lack of common sense)
- Characters unrealistically lacking age-appropriate or culturally-expected knowledge
- Important stylistic patterns or issues you overlooked
- Areas where your critique could be more specific and actionable

Enhance your analysis while following the structure from the system prompt. If your original assessment was thorough, refine the presentation and add concrete examples."""

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

CORRECTION_PROMPT = """Review the feedback below on your creative writing analysis. Address valid points by improving your analytical depth and coverage. If the reviewer misunderstood your analysis, clarify your reasoning and provide better textual support.

Key areas to enhance based on feedback:
- Add specific textual examples where critique was too vague
- Deepen character analysis if OOC assessment was superficial
- Provide more detailed emotional arc tracking if that was missing
- Flag cognitive boundary violations more explicitly if overlooked (including both impossible knowledge AND unrealistic ignorance)
- Check for characters lacking common sense or age-appropriate knowledge
- Strengthen prose-level critique with concrete examples
- Make recommendations more specific and actionable

The reviewer might have caught important gaps in your analysis - take their feedback seriously. Follow the system prompt structure in your revised analysis."""

EXTRACT_DETAILED_SOLUTION_MARKER = "Deep Dive"

# ============ Auxiliary Functions ============

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
    """Build initial creative writing analysis prompt"""
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
    """Build final summary prompt for creative writing analysis"""
    return f"""You have completed a comprehensive analysis of the creative writing through a rigorous analytical process. Now, create a clear, well-organized final response for the user.

**CRITICAL GUIDELINES:**
- **DO NOT** reveal the internal analysis process, iterations, verification steps, or meta-analytical details
- **DO NOT** mention "verification", "corrections", "iterations", or any process-related terminology
- **FOCUS** on providing direct, actionable feedback on the creative writing
- **ORGANIZE** the response to address: character consistency, emotional arcs, prose quality, and concrete improvements
- **PRESENT** insights as a unified, coherent analysis
- **USE** specific textual examples to support observations
- **BE THOROUGH** but focused - prioritize the most important issues and recommendations
- **MAINTAIN** a constructive, helpful tone that guides improvement

**Your task:**
Transform the analytical work into a polished response that:
1. Directly addresses the creative writing quality and issues
2. Provides clear identification of OOC moments, emotional arc problems, cognitive boundary violations, or prose weaknesses
3. Offers specific, actionable recommendations for improvement with examples where helpful
4. Acknowledges what is working well in the writing
5. Uses professional but encouraging language focused on helping the writer improve

Remember: The user should receive high-quality creative writing feedback, not a report about your analytical process.

<ORIGINAL_REQUEST>
{problem_statement}
</ORIGINAL_REQUEST>

<ANALYSIS_RESULT>
{analysis_result}
</ANALYSIS_RESULT>

Now create the final, polished creative writing feedback for the user. Start directly with the analysis - no preamble about the process."""


def build_thinking_plan_prompt(problem: str) -> str:
    """Build thinking plan prompt for creative writing analysis"""
    return f"""Given the following creative writing analysis request from the user:

<REQUEST>
{problem}
</REQUEST>

Before diving into deep analysis, create a structured analytical plan that will guide your examination.

Your plan should outline:
1. **Text Decomposition**: How will you break down this creative writing piece? (By scene, by character, by narrative beat?)
2. **Key Analysis Areas**: What are the critical aspects requiring thorough examination? (Character consistency? Emotional arcs? Prose style? Cognitive boundaries?)
3. **Analytical Strategy**: What approach will you use? (Character-focused? Scene-by-scene? Thematic? Stylistic?)
4. **Success Criteria**: How will you know when you have a complete and useful analysis? What must be covered?
5. **Potential Pitfalls**: What common analytical mistakes should you avoid? (Over-focusing on plot vs. character? Missing subtle OOC moments? Ignoring prose quality?)

Structure your plan in clear sections with brief explanations. This plan will serve as a roadmap for your deep creative writing analysis.

Keep the plan focused and practical - it should guide your analysis without constraining your ability to adapt as you discover issues."""

