---
name: context-engineering-advisor
description: Diagnose context stuffing vs. context engineering. Use when an AI workflow feels bloated, brittle, or hard to steer reliably.
intent: >-
  Guide product managers through diagnosing whether they're doing **context stuffing** (jamming volume without intent) or **context engineering** (shaping structure for attention). Use this to identify context boundaries, fix "Context Hoarding Disorder," and implement tactical practices like bounded domains, episodic retrieval, and the Research→Plan→Reset→Implement cycle.
type: interactive
theme: ai-agents
best_for:
  - "Diagnosing context stuffing vs. context engineering in your AI workflows"
  - "Building better memory and retrieval architecture for AI agents"
  - "Improving AI output quality through structured context design"
scenarios:
  - "My AI outputs are mediocre even though I'm giving it lots of information — diagnose what's wrong"
  - "I want to architect context properly for a multi-step AI workflow in my product team"
estimated_time: "15-20 min"
---

## Purpose

Guide product managers through diagnosing whether they're doing **context stuffing** (jamming volume without intent) or **context engineering** (shaping structure for attention). Use this to identify context boundaries, fix "Context Hoarding Disorder," and implement tactical practices like bounded domains, episodic retrieval, and the Research→Plan→Reset→Implement cycle.

**Key Distinction:** Context stuffing assumes volume = quality ("paste the entire PRD"). Context engineering treats AI attention as a scarce resource and allocates it deliberately.

This is not about prompt writing—it's about **designing the information architecture** that grounds AI in reality without overwhelming it with noise.

## Outputs

**Artifact:** Context-stuffing diagnosis (symptom count + 5-question assessment) plus a phased action plan; optionally a Context Manifest and memory-architecture blueprint
**Format:** Markdown
**Location:** Delivered in conversation; saved to a file only if the user asks
**Audience:** The PM or team designing/steering AI workflows

## Key Concepts

### The Paradigm Shift: Parametric → Contextual Intelligence

- LLMs have **parametric knowledge** (encoded during training) = static, outdated, non-attributable
- When asked about proprietary data, real-time info, or user preferences → forced to hallucinate or admit ignorance
- **Context engineering** bridges the gap between static training and dynamic reality
- **PM's role shift:** from feature builder → **architect of informational ecosystems** that ground AI in reality

### Context Stuffing vs. Context Engineering

| Dimension | Context Stuffing | Context Engineering |
|-----------|------------------|---------------------|
| **Mindset** | Volume = quality | Structure = quality |
| **Approach** | "Add everything just in case" | "What decision am I making?" |
| **Persistence** | Persist all context | Retrieve with intent |
| **Agent Chains** | Share everything between agents | Bounded context per agent |
| **Failure Response** | Retry until it works | Fix the structure |
| **Economic Model** | Context as storage | Context as attention (scarce resource) |

**Critical Metaphor:** Context stuffing is like bringing your entire file cabinet to a meeting. Context engineering is bringing only the 3 documents relevant to today's decision.

### The Anti-Pattern: Context Stuffing

**Five markers:** reflexively expanding context windows; persisting everything "just in case"; chaining agents without boundaries; adding evaluations to mask inconsistency; normalized retries ("it works if you run it 3 times").

**Why it fails:**
- **Reasoning Noise:** Thousands of irrelevant files compete for attention, degrading multi-hop logic
- **Context Rot:** Dead ends, past errors, irrelevant data accumulate → goal drift
- **Lost in the Middle:** Models prioritize beginning (primacy) and end (recency), ignore middle
- **Economic Waste:** Every query becomes expensive without accuracy gains; accuracy drops below 20% when context exceeds ~32k tokens

### Real Context Engineering: Core Principles

1. **Context without shape becomes noise**
2. **Structure > Volume**
3. **Retrieve with intent, not completeness**
4. **Small working contexts** (like short-term memory)
5. **Context Compaction:** Maximize density of relevant information per token

**Quantitative Framework:** `Efficiency = (Accuracy × Coherence) / (Tokens × Latency)`

**Key Finding:** Using RAG with 25% of available tokens preserves 95% accuracy while significantly reducing latency and cost.

### The 5 Diagnostic Questions (Detect Context Hoarding Disorder)

1. **What specific decision does this support?** — If you can't answer, you don't need it
2. **Can retrieval replace persistence?** — Just-in-time beats always-available
3. **Who owns the context boundary?** — If no one, it'll grow forever
4. **What fails if we exclude this?** — If nothing breaks, delete it
5. **Are we fixing structure or avoiding it?** — Stuffing context often masks bad information architecture

### Memory Architecture: Two-Layer System

- **Short-term (conversational):** Immediate interaction history for follow-ups; single-session lifespan; manage space by summarizing/truncating older parts
- **Long-term (persistent):** User preferences and key facts across sessions, typically via vector database (semantic retrieval). Two types: **Declarative Memory** (facts — "I'm vegan") and **Procedural Memory** (behavioral patterns — "I debug by checking logs first")
- **LLM-Powered ETL:** Models generate their own memories by identifying signals, consolidating with existing data, updating the database automatically

### The Research → Plan → Reset → Implement Cycle

The context rot solution:
1. **Research:** Agent gathers data → large, chaotic context window (noise + dead ends allowed)
2. **Plan:** Agent synthesizes into a high-density SPEC.md or PLAN.md (Source of Truth): decision made, supporting evidence, constraints applied, sequenced next steps
3. **Reset:** **Clear the entire context window** — delete research artifacts, dead ends, errors
4. **Implement:** Fresh session using **only** the high-density plan as context

**Why this works:** Context rot is eliminated; the agent starts clean with compressed, high-signal context.

### Anti-Patterns (What This Is NOT)

- **Not about choosing AI tools** — Claude vs. ChatGPT doesn't matter; architecture matters
- **Not about writing better prompts** — This is systems design, not copywriting
- **Not about adding more tokens** — "Infinite context" narratives are marketing, not engineering reality
- **Not about replacing human judgment** — Context engineering amplifies judgment, doesn't eliminate it

### When to Use This Skill

✅ **Use this when:**
- You're pasting entire PRDs/codebases into AI and getting vague responses
- AI outputs are inconsistent ("works sometimes, not others")
- You're burning tokens without seeing accuracy improvements
- You suspect you're "context stuffing" but don't know how to fix it
- You need to design context architecture for an AI product feature

❌ **Don't use this when:**
- You're just getting started with AI (start with basic prompts first)
- You're looking for tool recommendations (this is about architecture, not tooling)
- Your AI usage is working well (if it ain't broke, don't fix it)

### Facilitation Source of Truth

Use `workshop-facilitation` as the default interaction protocol: session heads-up + entry modes (Guided, Context dump, Best guess), one-question turns in plain language, progress labels, interruption/pause handling, and numbered quick-select options (include `Other (specify)` when useful). This file defines the domain-specific assessment content; if there is a conflict, follow this file's domain logic.

## Application

This interactive skill uses **adaptive questioning** to diagnose context stuffing, identify boundaries, and provide tactical implementation guidance.

---

### Step 0: Gather Context

**Agent asks about:**

- **Current AI usage:** tools/systems (ChatGPT, Claude, custom agents), PM tasks (PRD writing, research synthesis, discovery), how context is provided (paste docs, reference files, projects/memory)
- **Symptoms:** inconsistent outputs? repeated retries? vague/hedged responses despite "all the context"? escalating token costs without accuracy gains?
- **System architecture (if applicable):** custom agents or workflows? how is context shared between agents? RAG, vector databases, memory systems?

The user can describe briefly or paste examples.

---

### Step 1: Diagnose Context Stuffing Symptoms

**Agent asks:** "Which of these symptoms do you recognize? Select all that apply:"

1. **"I paste entire documents into AI"** — full PRDs, complete transcripts, entire codebases
2. **"AI gives vague, hedged responses despite having 'all the context'"** — "it depends," non-committal
3. **"I have to retry prompts 3+ times to get usable output"** — inconsistency is normalized
4. **"Token costs are escalating but accuracy isn't improving"**
5. **"I keep adding more context hoping it'll help"** — reflexive expansion without strategy
6. **"My agents pass everything to each other"** — full context chain A → B → C
7. **"I don't have clear criteria for what to include/exclude"** — no boundary definitions
8. **"None of these—my AI usage is working well"** — skip to advanced optimization

**Agent analyzes:**
- **0-1 symptoms:** Healthy context practices; proceed to optimization
- **2-3 symptoms:** Early context stuffing; address before it scales
- **4+ symptoms:** Active Context Hoarding Disorder; immediate intervention needed

Then walk the 5 diagnostic questions (Steps 2-6), one per turn.

---

### Step 2: Q1 — What Specific Decision Does This Support?

Ask the user what decision they're making *right now*, and audit their context against it. Example: for "help with discovery planning" a user might supply a 20-page PRD, 50 full transcripts, a 15-page competitive analysis, and 3 months of meeting notes — but:

1. **"Deciding which user segment to interview first"** needs only the PRD's segment paragraphs + a 1-page synthesis of prior interview themes — not full transcripts, meeting notes, or the competitive analysis
2. **"Deciding which discovery questions to ask"** needs research objectives + past interview insights + a JTBD frame
3. **"Not sure — I just want AI to 'understand my product'"** — no specific decision = the context stuffing trap. Define the decision first, then select context.

**Best Practice:** Before adding context, complete this sentence:
> "I need this context because I'm deciding [specific decision], and without [specific information], I can't make that decision."

If the sentence can't be completed, the context isn't needed. **Agent validates** the user's decision + context pairing and recommends trimming anything that doesn't directly support it.

---

### Step 3: Q2 — Can Retrieval Replace Persistence?

Ask whether each piece of context is **always-needed (persist)** or **episodic (retrieve on-demand)**:

- **Persist:** core product constraints, user preferences that apply to every interaction, critical definitions (operational glossary), non-negotiable rules
- **Retrieve:** project-specific details, historical data (past PRDs, old transcripts), contextual facts (competitive analysis, market research), temporary decisions

**Typical user positions and responses:**
1. **"Most is always-needed"** — good instinct; verify with the Q4 falsification test; build a constraints registry + glossary for what survives
2. **"Most is episodic"** — perfect candidate for RAG; implement semantic search, retrieve only relevant chunks per query
3. **"Not sure — I persist everything to be safe"** — classic Context Hoarding Disorder; apply the Q4 test to each piece

**Rule of Thumb:** Persist what's referenced in 80%+ of interactions; retrieve what's referenced in <20%; the gray zone (20-80%) depends on retrieval latency vs. context window cost.

---

### Step 4: Q3 — Who Owns the Context Boundary?

If **no one** owns the context boundary, it grows indefinitely — every PM adds "just one more thing," and six months later every query stuffs 100k tokens.

**Ownership models and responses:**
1. **"I own it" (solo PM/small team)** — good, fast decisions; document the boundary criteria (use Questions 1-5 as the framework)
2. **"Team shares ownership"** — works if formalized; create a **Context Manifest**: what's always included, what's retrieved, what's excluded (and why)
3. **"No one — it's ad-hoc/implicit"** — critical risk; assign explicit ownership and schedule quarterly context audits

**For the Context Manifest template (sections, example entries, review cadence), read `references/context-manifest-template.md`.**

---

### Step 5: Q4 — What Fails if We Exclude This?

The **falsification test**: for each context element, complete
> "If I exclude [context element], then [specific failure] will occur in [specific scenario]."

- ✅ Good: "If I exclude GDPR constraints, AI will recommend features that violate EU privacy law." → valid reason to persist
- ⚠️ Vague: "If I exclude historical PRDs, AI won't understand our product evolution." → hypothetical; retrieve PRDs only when explicitly referencing past decisions
- ❌ None: "I'm not sure anything would break — I include it to be thorough." → context stuffing; delete immediately

**Agent provides:** a list of the user's context elements to delete (no concrete failure identified).

---

### Step 6: Q5 — Are We Fixing Structure or Avoiding It?

Context stuffing often hides bad information architecture: instead of fixing messy, ambiguous documents, teams add more documents hoping AI will "figure it out."

**The Structural Health Test** — if the user is adding context to compensate for:
- **Ambiguous documentation** → fix the docs (e.g., reconcile 5 conflicting PRDs into 1 Source of Truth), don't add more
- **Undefined terms** → build an operational glossary (20-30 key terms: "active user," "churn," "engagement" defined unambiguously)
- **Undocumented constraints** → create a constraints registry (technical, regulatory, strategic — "We won't build mobile apps" documented once, not re-explained per prompt)

**Agent provides:** a prioritized list of structural fixes to do before adding any more context.

---

### Step 7: Define Memory Architecture

Summarize the user's context profile from Steps 2-6 (always-needed vs. episodic, boundary owner, validated essentials, structural fixes), then design their **two-layer memory architecture** per the Key Concepts section: short-term conversational memory (with summarize/truncate management), long-term persistent memory (constraints registry + glossary, vector DB with Declarative vs. Procedural entries), and a retrieval strategy for episodic context (semantic search triggered by query intent; consider Contextual Retrieval — prepend explanatory context to each chunk before embedding).

**Agent offers:**
1. **Generate a Context Architecture Blueprint** for their specific use case
2. **Provide implementation guidance** (tools, techniques, best practices)
3. **Design a retrieval strategy** for their episodic context

---

### Step 8: Implement Research → Plan → Reset → Implement

Walk the user through applying the four-phase cycle (defined in Key Concepts) to their workflow, stressing that **Reset is the critical, non-optional step** — clearing the context window after Plan is what prevents research-phase rot from poisoning implementation.

**Agent offers:**
1. **A template for the PLAN.md format** (decision, evidence, constraints, sequenced next steps)
2. **A worked example of the cycle** on a concrete PM use case (e.g., discovery planning)
3. **A step-by-step guide** to adopting it in their workflow

---

### Step 9: Action Plan & Next Steps

**Agent synthesizes:**

**Immediate Fixes (This Week):**
1. Delete context with no falsifiable failure mode (from Q4)
2. Apply Research→Plan→Reset→Implement to the next AI task
3. Document the context boundary in a Context Manifest

**Foundation Building (Next 2 Weeks):**
1. Build constraints registry with 20+ entries
2. Create operational glossary with 20-30 key terms
3. Implement two-layer memory architecture

**Long-Term Optimization (Next Month):**
1. Set up semantic retrieval for episodic context
2. Assign context boundary owner + quarterly audit schedule
3. Implement Contextual Retrieval (Anthropic) for RAG

**Success Metrics:** token usage down 50%+ · output consistency up (fewer retries) · response quality up (sharper, less hedged) · context window stable (no unbounded growth)

**Agent offers:** generate implementation docs (Context Manifest, PLAN.md template) · advanced techniques (Contextual Retrieval, LLM-powered ETL) · review of the user's current prompts/workflows.

---

## Examples

For three worked end-to-end diagnoses (solo PM stuffing → engineering; growth-stage team with unbounded agent chains; enterprise RAG retrieving without intent — each with symptoms, per-question assessment, intervention, and measured outcome), read `references/worked-examples.md`.

---

## Common Pitfalls

1. **"Infinite Context" Marketing vs. Engineering Reality** — believing 1M-token windows mean you should use them → Reasoning Noise; accuracy drops below 20% past ~32k tokens. Fix: tokens are scarce; optimize for density, not volume.
2. **Retrying Instead of Restructuring** — "it works if I run it 3 times" → wastes time and money; masks context rot. Fix: common retries mean broken structure; apply Q5.
3. **No Context Boundary Owner** — ad-hoc, implicit context decisions → unbounded growth; 100k-token queries within six months. Fix: assign ownership, create a Context Manifest, audit quarterly.
4. **Mixing Always-Needed with Episodic** — persisting historical data that should be retrieved → crowded window, diluted attention. Fix: apply the Q2 80%/20% rule.
5. **Skipping the Reset Phase** — never clearing the window between Plan and Implement → context rot accumulates; goal drift; dead ends poison implementation. Fix: Reset is mandatory; implement with only the high-density plan.

---

## References

### Related Skills
- **`ai-shaped-readiness-advisor`** (Interactive) — Context Design is Competency #1 of AI-shaped work
- **`problem-statement`** (Component) — Evidence-based framing requires context engineering
- **`epic-hypothesis`** (Component) — Testable hypotheses depend on clear constraints (part of context)
- **`pol-probe-advisor`** (Interactive) — Validation experiments benefit from context engineering (define what AI needs to know)

### External Frameworks
- **Dean Peters** — [*Context Stuffing Is Not Context Engineering*](https://deanpeters.substack.com/p/context-stuffing-is-not-context-engineering) (Dean Peters' Substack, 2026)
- **Teresa Torres** — *Continuous Discovery Habits* (Context Engineering as one of 5 new AI PM disciplines)
- **Marty Cagan** — *Empowered* (Feasibility risk in AI era includes understanding "physics of AI")
- **Anthropic** — [Contextual Retrieval whitepaper](https://www.anthropic.com/news/contextual-retrieval) (35% failure rate reduction)
- **Google** — Context engineering whitepaper on LLM-powered memory systems

### Technical References
- **RAG (Retrieval-Augmented Generation)** — Standard technique for episodic context retrieval
- **Vector Databases** — Semantic search for long-term memory (Pinecone, Weaviate, Chroma)
- **Contextual Retrieval (Anthropic)** — Prepend explanatory context to chunks before embedding
- **LLM-as-Judge** — Automated evaluation of context quality
