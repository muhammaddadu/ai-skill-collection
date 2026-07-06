# Maturity Rubrics — Full 4-Level Descriptions

Present these as concise 1-4 choices first (one line per level); share the full
detail below only when the user asks or seems unsure between two levels.

Level labels apply to every competency:
- **Level 1:** AI-First (efficiency only)
- **Level 2:** Emerging (early capabilities)
- **Level 3:** Transitioning (redesign underway)
- **Level 4:** AI-Shaped (strategic transformation)

---

## 1. Context Design

How well you've built a "reality layer" that both humans and AI can trust, and
whether you're doing **context stuffing** (volume without intent) or **context
engineering** (structure for attention).

1. **Level 1 (AI-First / Context Stuffing):** "I paste entire documents into ChatGPT every time I need something. No shared knowledge base. No context boundaries."
   - Reality: One-off prompting with no durability; "more is better" mentality
   - Problem: AI has no memory; you repeat yourself constantly; context stuffing degrades attention
   - **Context Engineering Gap:** No answers to the 5 diagnostic questions; persisting everything "just in case"

2. **Level 2 (Emerging / Early Structure):** "We have some docs (PRDs, strategy memos), but they're scattered. No consistent format. Starting to notice context stuffing issues (vague responses, normalized retries)."
   - Reality: Context exists but isn't structured for AI consumption; no retrieval strategy
   - Problem: AI can't reliably find or trust information; mixing always-needed with episodic context
   - **Context Engineering Gap:** No context boundary owner; no distinction between persist vs. retrieve

3. **Level 3 (Transitioning / Context Engineering Emerging):** "We've started using CLAUDE.md files and project instructions. Constraints registry exists. We're identifying what to persist vs. retrieve. Experimenting with Research→Plan→Reset→Implement cycle."
   - Reality: Structured context emerging, but not comprehensive; context boundaries defined but not fully enforced
   - Problem: Coverage is patchy; some areas well-documented, others vibe-driven; inconsistent retrieval practices
   - **Context Engineering Progress:** Can answer 3-4 of the 5 diagnostic questions; context boundary owner assigned; starting to use two-layer memory

4. **Level 4 (AI-Shaped / Context Engineering Mastery):** "We maintain a durable reality layer: constraints registry (20+ entries), evidence database, operational glossary (30+ terms). Two-layer memory architecture (short-term conversational + long-term persistent via vector DB). Context boundaries defined and owned. AI agents reference these automatically. We use Research→Plan→Reset→Implement to prevent context rot."
   - Reality: Comprehensive, version-controlled context both humans and AI trust; retrieval with intent (not completeness)
   - Outcome: AI operates with high confidence; reduces hallucination and rework; token usage optimized; no context stuffing
   - **Context Engineering Mastery:** Can answer all 5 diagnostic questions; context boundary audited quarterly; quantitative efficiency tracking: (Accuracy × Coherence) / (Tokens × Latency)

**Note:** If the user selects Level 1-2 and struggles with context stuffing,
point them at `context-engineering-advisor`
to diagnose and fix Context Hoarding Disorder before proceeding.

---

## 2. Agent Orchestration

Whether you have repeatable AI workflows or just one-off prompts.

1. **Level 1 (AI-First):** "I type prompts into ChatGPT as needed. No saved workflows or templates."
   - Reality: Tactical, ad-hoc usage
   - Problem: Inconsistent results; can't scale or audit

2. **Level 2 (Emerging):** "I have a few saved prompts I reuse. Maybe some custom GPTs or Claude Projects."
   - Reality: Repeatable prompts, but not full workflows
   - Problem: Each step is manual; no orchestration

3. **Level 3 (Transitioning):** "We've built some multi-step workflows (research → synthesis → critique). Tracked in tools like Notion or Linear."
   - Reality: Workflows exist but require manual handoffs
   - Problem: Still human-in-the-loop for every step; not fully automated

4. **Level 4 (AI-Shaped):** "We have orchestrated AI workflows that run autonomously: research → synthesis → critique → decision → log rationale. Each step is traceable and version-controlled."
   - Reality: Workflows run consistently; show their work at each step
   - Outcome: Reliable, auditable, scalable AI processes

---

## 3. Outcome Acceleration

Are you using AI to compress learning cycles, or just speed up tasks?

1. **Level 1 (AI-First):** "AI helps me write docs faster (PRDs, user stories). Saves me a few hours per week."
   - Reality: Efficiency gains on artifact creation
   - Problem: Docs weren't the bottleneck; learning cycles unchanged

2. **Level 2 (Emerging):** "AI helps with research and synthesis (summarize user feedback, analyze competitors). Saves research time."
   - Reality: Modest learning acceleration
   - Problem: Still sequential; AI doesn't eliminate validation lag

3. **Level 3 (Transitioning):** "We use AI to run experiments faster (PoL probes, feasibility checks). Cut validation time from weeks to days."
   - Reality: Learning cycles compressing
   - Problem: Not yet systematic; only applied to some experiments

4. **Level 4 (AI-Shaped):** "AI systematically removes bottlenecks: overnight feasibility checks, async synthesis replaces meetings, automated validation against constraints. Learning cycles 5-10x faster."
   - Reality: Fundamental redesign of how learning happens
   - Outcome: Ship validated features 6x faster than competitors

---

## 4. Team-AI Facilitation

How well you've redesigned team systems for AI as co-intelligence.

1. **Level 1 (AI-First):** "I use AI privately. Team doesn't know or doesn't use it. No shared norms."
   - Reality: Individual tool usage, no team integration
   - Problem: Inconsistent quality; no accountability for AI outputs

2. **Level 2 (Emerging):** "Team uses AI, but no formal review process. 'I used AI' mentioned casually."
   - Reality: Awareness but no structure
   - Problem: AI outputs treated as final; errors slip through

3. **Level 3 (Transitioning):** "We have review norms emerging (AI outputs are drafts, not finals). Evidence standards discussed but not codified."
   - Reality: Cultural shift underway
   - Problem: Norms are informal; not everyone follows them

4. **Level 4 (AI-Shaped):** "Clear protocols: AI outputs require human validation, evidence standards codified, decision authority explicit (AI recommends, humans decide). Team treats AI as co-intelligence."
   - Reality: AI integrated into team operating system
   - Outcome: High-quality outputs; psychological safety maintained

---

## 5. Strategic Differentiation

Are you creating defensible competitive advantages, or just efficiency gains?

1. **Level 1 (AI-First):** "We use AI to work faster (write better docs, respond to customers quicker). Efficiency gains only."
   - Reality: Table-stakes improvements
   - Problem: Competitors can copy this within months

2. **Level 2 (Emerging):** "AI enables us to do things we couldn't before (analyze 10x more data, test more hypotheses). New capabilities, but competitors could replicate."
   - Reality: Capability expansion, but not defensible
   - Problem: No moat; competitors hire more people to match

3. **Level 3 (Transitioning):** "We've redesigned some workflows around AI (e.g., validate hypotheses in 2 days vs. 3 weeks). Starting to create separation."
   - Reality: Workflow advantages emerging
   - Problem: Not yet systematic; only applied in pockets

4. **Level 4 (AI-Shaped):** "We've fundamentally rewired how we operate: customers get capabilities they can't get elsewhere, our learning cycles are 10x faster than industry standard, our economics are 5x better. Competitors can't replicate without full org redesign."
   - Reality: Defensible competitive moat
   - Outcome: Strategic advantage that compounds over time
