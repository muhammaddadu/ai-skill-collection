---
name: ai-shaped-readiness-advisor
description: Assess whether your product work is AI-first or AI-shaped. Use when evaluating AI maturity and choosing the next team capability to build.
intent: >-
  Assess whether your product work is **"AI-first"** (using AI to automate existing tasks faster) or **"AI-shaped"** (fundamentally redesigning how product teams operate around AI capabilities). Use this to evaluate your readiness across **5 essential PM competencies for 2026**, identify gaps, and get concrete recommendations on which capability to build first.
type: interactive
theme: ai-agents
best_for:
  - "Assessing whether your team is AI-first or genuinely AI-shaped"
  - "Identifying which of the 5 AI competencies to build next"
  - "Understanding your product org's AI maturity honestly"
scenarios:
  - "My team uses AI tools but I'm not sure if we're working differently or just automating the same tasks"
  - "I want to assess my product org's AI maturity and prioritize where to invest next quarter"
estimated_time: "15-20 min"
---

## Purpose

Assess whether your product work is **"AI-first"** (using AI to automate existing tasks faster) or **"AI-shaped"** (fundamentally redesigning how product teams operate around AI capabilities). Use this to evaluate your readiness across **5 essential PM competencies for 2026**, identify gaps, and get concrete recommendations on which capability to build first.

**Key Distinction:** AI-first is cute (using Copilot to write PRDs faster). AI-shaped is survival (building a durable "reality layer" that both humans and AI trust, orchestrating AI workflows, compressing learning cycles).

This is not about AI tools—it's about **organizational redesign around AI as co-intelligence**. The interactive skill guides you through a maturity assessment, then recommends your next move.

## Outputs

**Artifact:** AI-Shaped Readiness Profile (5-competency maturity table + overall assessment) with a prioritized 4-week action plan; optional progress tracker
**Format:** Markdown (table, recommendations, checklist)
**Location:** Delivered in conversation; saved to a file only if the user asks
**Audience:** The PM or product leader being assessed; shareable with their team/leadership

## Key Concepts

### AI-First vs. AI-Shaped

| Dimension | AI-First (Cute) | AI-Shaped (Survival) |
|-----------|-----------------|----------------------|
| **Mindset** | Automate existing tasks | Redesign how work gets done |
| **Goal** | Speed up artifact creation | Compress learning cycles |
| **AI Role** | Task assistant | Strategic co-intelligence |
| **Advantage** | Temporary efficiency gains | Defensible competitive moat |
| **Example** | "Copilot writes PRDs 2x faster" | "AI agent validates hypotheses in 48 hours instead of 3 weeks" |

**Critical Insight:** If a competitor can replicate your AI usage by throwing bodies at it, it's not differentiation—it's just efficiency (which becomes table stakes within months).

### The 5 Essential PM Competencies (2026)

These competencies define AI-shaped product work. You'll assess maturity on each.

#### 1. **Context Design**
Building a durable **"reality layer"** that both humans and AI can trust—treating AI attention as a scarce resource and allocating it deliberately. Includes: documenting what's true vs. assumed, immutable constraints, an operational glossary, evidence standards, context boundaries (persist vs. retrieve), and memory architecture.

**Key Principle:** *"If you can't point to evidence, constraints, and definitions, you don't have context. You have vibes."* The critical distinction is **context stuffing** (jamming volume without intent) vs. **context engineering** (shaping structure for attention).

**AI-first version:** Pasting PRDs into ChatGPT; no context boundaries; "more is better"
**AI-shaped version:** CLAUDE.md files, evidence databases, constraint registries AI agents reference; two-layer memory; Research→Plan→Reset→Implement cycle

**Deep Dive:** For the stuffing-vs-engineering diagnosis, the 5 diagnostic questions, and memory architecture, use [`context-engineering-advisor`](../context-engineering-advisor/SKILL.md).

#### 2. **Agent Orchestration**
Creating repeatable, traceable AI workflows (not one-off prompts): defined loops (research → synthesis → critique → decision → log rationale), each step shows its work, workflows run consistently, prompts version-controlled.

**Key Principle:** One-off prompts are tactical. Orchestrated workflows are strategic.

**AI-first version:** "Ask ChatGPT to analyze this user feedback"
**AI-shaped version:** Automated workflow that ingests feedback, tags themes, generates hypotheses, flags contradictions, logs decisions

#### 3. **Outcome Acceleration**
Using AI to compress **learning cycles** (not just speed up tasks): eliminate validation lag (PoL probes in days, not weeks), remove approval delays (AI pre-validates against constraints), cut meeting overhead (async AI synthesis).

**Key Principle:** Do less, purposefully. AI removes bottlenecks, not generates more work.

**AI-first version:** "AI writes user stories faster"
**AI-shaped version:** "AI runs feasibility checks overnight, eliminating 2 weeks of technical discovery"

#### 4. **Team-AI Facilitation**
Redesigning team systems so AI operates as **co-intelligence**, not an accountability shield: review norms (who checks AI outputs, when, how), evidence standards (AI must cite sources), decision authority (AI recommends, humans decide), psychological safety (team can challenge AI).

**Key Principle:** AI amplifies judgment, doesn't replace accountability.

**AI-first version:** "I used AI" as excuse for bad outputs
**AI-shaped version:** Clear review protocols; AI outputs treated as drafts requiring human validation

#### 5. **Strategic Differentiation**
Moving beyond efficiency to create **defensible competitive advantages**: new customer capabilities, workflow rewiring competitors can't replicate without full redesign, economics competitors can't match.

**Key Principle:** *"If a competitor can copy it by throwing bodies at it, it's not differentiation."*

**AI-first version:** "We use AI to write better docs"
**AI-shaped version:** "We validate product hypotheses in 2 days vs. industry standard 3 weeks—ship 6x more validated features per quarter"

### Anti-Patterns (What This Is NOT)

- **Not about AI tools:** Using Claude vs. ChatGPT doesn't matter. Redesigning workflows matters.
- **Not about speed:** Writing PRDs 2x faster isn't strategic if PRDs weren't the bottleneck.
- **Not about automation:** Automating bad processes just scales the bad.
- **Not about replacing humans:** AI-shaped orgs augment judgment, not eliminate it.

### When to Use This Skill

✅ **Use this when:**
- You're using AI tools but not seeing strategic advantage
- You suspect you're "AI-first" (efficiency) but want to be "AI-shaped" (transformation)
- You need to prioritize which AI capability to build next
- Leadership asks "How are we using AI?" and you're not sure how to answer strategically
- You want to assess team readiness for AI-powered product work

❌ **Don't use this when:**
- You haven't started using AI at all (start with basic tools first)
- You're looking for tool recommendations (this is about organizational design, not tooling)
- You need tactical "how to write a prompt" guidance (use skills for that)

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the default interaction protocol: session heads-up + entry modes (Guided, Context dump, Best guess), one-question turns in plain language, progress labels, interruption/pause handling, and numbered quick-select options (include `Other (specify)` when useful). This file defines the domain-specific assessment content; if there is a conflict, follow this file's domain logic.

## Application

This interactive skill uses **adaptive questioning** to assess maturity across the 5 competencies, then recommends which to prioritize.

**Domain-specific protocol notes** (on top of `workshop-facilitation`):
- Up to 13 questions total: 8 context + 5 scoring. Labels: `Context Qx/8`, `Scoring Qx/5`; include "questions remaining" when practical.
- For scoring questions, present concise 1-4 choices first; share full rubric details only on request.
- Numbered recommendations **only at decision points**: after the context summary, after the 5-dimension maturity profile, and during priority/action-plan selection. Accept selections like `#1`, `1`, `1 and 3`, `1,3`, or custom text; synthesize combined paths for multi-selects; map custom text to the closest valid path without forcing re-entry.

---

### Session Start: Heads-Up + Entry Mode (Mandatory)

**Agent opening prompt (use this first):**

"Quick heads-up before we start: this usually takes about 7-10 minutes and up to 13 questions total (8 context + 5 scoring).

How do you want to do this?
1. Guided mode: I’ll ask one question at a time.
2. Context dump: you paste what you already know, and I’ll skip anything redundant.
3. Best guess mode: I’ll make reasonable assumptions where details are missing, label them, and keep moving."

**Mode behavior:**
- **Guided:** Run Step 0 as written, then scoring.
- **Context dump:** Ask for pasted context once, summarize, identify gaps, skip answered questions, ask at most 0-2 clarifying questions, then move to scoring.
- **Best guess:** Ask for the smallest viable input (role/team + primary goal), infer the rest with labelled `Assumption` items and confidence tags (`High`/`Medium`/`Low`), and continue without blocking.

At the final summary, include an **Assumptions to Validate** section when context dump or best guess mode was used.

---

### Step 0: Gather Context

Collect context using this exact sequence, one question at a time:

1. "Which AI tools are you using today?"
2. "How does your team usually use AI today: one-off prompts, reusable templates, or multi-step workflows?"
3. "Who uses AI consistently today: just you, PMs, or cross-functional teams?"
4. "About how many PMs, engineers, and designers are on your team?"
5. "What stage are you in: startup, growth, or enterprise?"
6. "How are decisions made: centralized, distributed, or consensus-driven?"
7. "What competitive advantage are you trying to build with AI?"
8. "What's the biggest bottleneck slowing learning and iteration today?"

After question 8, summarize back in 4 lines: current AI usage pattern, team context, strategic intent, primary bottleneck.

---

### Steps 1-5: Score the 5 Competencies (Scoring Q1-5)

Score one competency per turn, in this order:

1. **Context Design** — the "reality layer"; stuffing vs. engineering
2. **Agent Orchestration** — repeatable workflows vs. one-off prompts
3. **Outcome Acceleration** — compressed learning cycles vs. faster tasks
4. **Team-AI Facilitation** — team norms for AI as co-intelligence
5. **Strategic Differentiation** — defensible advantage vs. efficiency

For each, ask "Which statement best describes your current state?" and present the four levels as concise one-line choices. **For the full 4-level rubric text per competency (reality, problem, outcome details), read `references/maturity-rubrics.md`** — expand a level's detail when the user asks or hesitates between two levels.

If the user selects Level 1-2 on Context Design with context-stuffing symptoms, suggest [`context-engineering-advisor`](../context-engineering-advisor/SKILL.md) as a follow-up.

Record each response: `[Competency] maturity = Level X`.

---

### Step 6: Assess Maturity Profile

**Agent synthesizes:**

```
┌─────────────────────────────┬───────┬──────────┐
│ Competency                  │ Level │ Maturity │
├─────────────────────────────┼───────┼──────────┤
│ 1. Context Design           │   X   │ [Label]  │
│ 2. Agent Orchestration      │   X   │ [Label]  │
│ 3. Outcome Acceleration     │   X   │ [Label]  │
│ 4. Team-AI Facilitation     │   X   │ [Label]  │
│ 5. Strategic Differentiation│   X   │ [Label]  │
└─────────────────────────────┴───────┴──────────┘

Overall Assessment: [AI-First / Emerging / Transitioning / AI-Shaped]
```

**Maturity Labels:** Level 1 = AI-First (efficiency only) · Level 2 = Emerging (early capabilities) · Level 3 = Transitioning (redesign underway) · Level 4 = AI-Shaped (strategic transformation)

**Overall Assessment Logic (by average level):** 1-1.5 → AI-First · 2-2.5 → Emerging · 3-3.5 → Transitioning · 3.5-4 → AI-Shaped

---

### Step 7: Identify Priority Gap

**Dependency Logic:**
1. **Context Design is foundational** — if Level 1-2, it must be priority #1 (Agent Orchestration and Outcome Acceleration depend on it)
2. **Agent Orchestration enables Outcome Acceleration** — if Context Design is 3+ but Orchestration is 1-2, prioritize orchestration
3. **Team-AI Facilitation is parallel** — can develop alongside others, but required for scale (and first priority when usage is individual, not team-wide, across a distributed org)
4. **Strategic Differentiation requires Level 3+ on the others** — don't focus here until the foundations are built

**Agent recommends** the priority competency with a one-line "why" and "impact":

1. **Context Design** — without durable context, AI operates on vibes; unlocks Orchestration and Acceleration
2. **Agent Orchestration** — turn one-off prompts into reliable, traceable workflows
3. **Outcome Acceleration** — infrastructure exists; now compress learning cycles for strategic advantage
4. **Team-AI Facilitation** — can't scale if only you're AI-shaped; shared norms > individual productivity
5. **Strategic Differentiation** — foundation is in place; build the moat

**Then offer:**
1. **Accept recommendation** — provide detailed action plan (Step 8)
2. **Choose different priority** — warn about dependencies but allow override
3. **Focus on multiple simultaneously** — suggest parallel tracks if feasible

---

### Step 8: Generate Action Plan

**For the full week-by-week action plan for the selected priority (phases, success criteria, related skills), read `references/action-plans.md`** and deliver the matching plan, tailored to the user's context from Step 0. One plan exists per competency:

- **Context Design** — constraints registry → glossary → evidence standards + boundaries → memory architecture (4 weeks)
- **Agent Orchestration** — map workflows → design orchestrated loop → build/test → document/scale (4 weeks)
- **Outcome Acceleration** — find bottleneck → design AI intervention → pilot → scale (4 weeks)
- **Team-AI Facilitation** — review norms → evidence standards → decision authority → psychological safety (4 weeks)
- **Strategic Differentiation** — moat opportunities → design capability → build/test → validate moat (5 weeks)

---

### Step 9: Track Progress (Optional)

Offer to create a progress tracker: baseline maturity levels, target levels, action-plan milestones, review cadence (weekly/monthly).

1. **Yes, create tracker** — generate Markdown checklist
2. **No, I'll track separately** — provide summary

---

## Examples

For three worked end-to-end assessments (early-stage startup, growth-stage company, enterprise — each with context, scores, recommended priority, and outcome), read `references/example-assessments.md`.

---

## Common Pitfalls

1. **Mistaking Efficiency for Differentiation** — "We write PRDs 2x faster, we're AI-shaped!" → competitors copy within months. Fix: ask "if a competitor threw 2x more people at this, could they match us?" If yes, it's table stakes.
2. **Skipping Context Design** — building orchestration workflows without durable context → fragile workflows that break when context changes. Fix: build the registry, glossary, and evidence standards first.
3. **Individual Usage, Not Team Transformation** — "I'm AI-shaped, my team isn't" → can't scale; workflows die when you're on vacation. Fix: prioritize Team-AI Facilitation; shared norms beat individual productivity.
4. **Focusing on Tools, Not Workflows** — "Claude or ChatGPT?" → tool debates distract from organizational redesign. Fix: tools don't matter; redesign how work gets done.
5. **Speed Over Learning** — "AI helps us ship faster!" → you ship the wrong thing faster. Fix: Outcome Acceleration is about learning faster; validate hypotheses in days, not weeks.

---

## References

### Related Skills
- **[context-engineering-advisor](../context-engineering-advisor/SKILL.md)** (Interactive) — **Deep dive on Context Design competency:** Diagnose context stuffing, implement memory architecture, use Research→Plan→Reset→Implement cycle
- **[problem-statement](../problem-statement/SKILL.md)** (Component) — Evidence-based problem framing (Context Design)
- **[epic-hypothesis](../epic-hypothesis/SKILL.md)** (Component) — Testable hypotheses with evidence standards
- **[pol-probe-advisor](../pol-probe-advisor/SKILL.md)** (Interactive) — Use AI to compress validation cycles (Outcome Acceleration)
- **[discovery-process](../discovery-process/SKILL.md)** (Workflow) — Apply AI-shaped principles to discovery
- **[positioning-statement](../positioning-statement/SKILL.md)** (Component) — Articulate your AI-driven differentiation (Strategic Differentiation)

### External Frameworks
- **Dean Peters** — [*AI-First Is Cute. AI-Shaped Is Survival.*](https://deanpeters.substack.com/p/ai-first-is-cute-ai-shaped-is-survival) (Dean Peters' Substack, 2026)
- **Dean Peters** — [*Context Stuffing Is Not Context Engineering*](https://deanpeters.substack.com/p/context-stuffing-is-not-context-engineering) (Dean Peters' Substack, 2026) — Deep dive on Competency #1 (Context Design)

### Further Reading
- **Ethan Mollick** — *Co-Intelligence* (on AI as co-intelligence, not replacement)
- **Shreyas Doshi** — Twitter threads on PM judgment augmentation with AI
- **Lenny Rachitsky** — Newsletter interviews with AI-forward PMs
