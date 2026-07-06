---
name: epic-breakdown-advisor
description: Guided interactive session that walks an epic through splitting — INVEST pre-check, sequential pattern selection via one-question turns, split evaluation, and a story-breakdown output. Use when you want a facilitated breakdown of a too-large backlog item. Do NOT use to look up split-pattern definitions or examples — use user-story-splitting.
intent: >-
  Facilitate an interactive session that breaks an epic into user stories using Richard Lawrence's
  Humanizing Work methodology: validate the epic against INVEST, walk the splitting patterns
  sequentially with one question per turn until one fits, generate the story breakdown, and
  evaluate the split for revealed low-value work and story-size balance. Pattern definitions and
  examples live in the canonical reference, user-story-splitting; this skill owns the facilitation
  flow, not the pattern content.
type: interactive
best_for:
  - "Splitting epics into smaller vertical slices through a guided conversation"
  - "Choosing the right story split pattern for a large backlog item interactively"
  - "Turning vague feature blobs into sprint-sized stories"
scenarios:
  - "Break this onboarding epic into smaller user stories"
  - "Help me split a large reporting feature before sprint planning"
  - "Which story-splitting pattern should I use for this admin workflow epic?"
---


## Purpose
Guide product managers through breaking down epics into user stories using Richard Lawrence's Humanizing Work methodology — a systematic, flowchart-driven approach that applies the splitting patterns sequentially. This skill owns the **facilitation**: context gathering, INVEST pre-check, walking the patterns one question at a time, and evaluating the resulting split.

**For the full definition and examples of each split pattern, read [`../user-story-splitting/SKILL.md`](../user-story-splitting/SKILL.md).** That skill is the canonical pattern reference; do not restate pattern content here — consult it when generating splits.

## Outputs
**Artifact:** Epic breakdown plan — INVEST pre-check, chosen split pattern(s), story breakdown with split evaluation
**Format:** markdown
**Location:** inline in conversation; save to `docs/product/epic-breakdown-<epic-slug>.md` if kept
**Audience:** PM and delivery team turning the epic into sprint-ready stories

## Key Concepts

### Core Principle: Vertical Slices Preserve Value
A user story is "a description of a change in system behavior from the perspective of a user." Splitting must maintain **vertical slices** — work that touches multiple architectural layers and delivers observable user value — not horizontal slices addressing single components (e.g., "front-end story" + "back-end story").

### The Three-Step Process
1. **Pre-Split Validation:** Check the story satisfies INVEST criteria (except "Small")
2. **Apply Splitting Patterns:** Work through the patterns sequentially until one fits
3. **Evaluate Splits:** Choose the split that reveals low-value work or produces equal-sized stories

### The Splitting Patterns (Walked in Order)
The pattern sequence, with full definitions, key insights, and worked examples for each, is in [`../user-story-splitting/SKILL.md`](../user-story-splitting/SKILL.md) (Step 2 and the template). In this session you walk them in order — Workflow Steps, Operations (CRUD), Business Rule Variations, Data Variations, Data Entry Methods, Acceptance Criteria Complexity, Major Effort, Simple/Complex, External Dependencies, DevOps Steps, Defer Performance, and finally TADs/Spike — asking one "does this apply?" question per pattern and stopping at the first fit.

The **meta-pattern** (identify core complexity → list variations → reduce to one complete slice → make the rest separate stories) also lives in the reference; apply it whichever pattern fits.

### Why This Works
- **Prevents arbitrary splitting:** Methodical checklist prevents guessing
- **Preserves user value:** Every story delivers observable value
- **Reveals waste:** Good splits expose low-value work you can deprioritize
- **Repeatable:** Apply to any epic consistently

---

### Facilitation Source of Truth

Use `workshop-facilitation` as the default interaction protocol for this skill.

It defines:
- session heads-up + entry mode (Guided, Context dump, Best guess)
- one-question turns with plain-language prompts
- progress labels (for example, Context Qx/8 and Scoring Qx/5)
- interruption handling and pause/resume behavior
- numbered recommendations at decision points
- quick-select numbered response options for regular questions (include `Other (specify)` when useful)

This file defines the domain-specific assessment content. If there is a conflict, follow this file's domain logic.

## Application

### Step 0: Provide Epic Context

**Agent asks:**

Please share your epic:

- Epic title/ID
- Description or hypothesis
- Acceptance criteria (especially multiple "When/Then" pairs)
- Target persona
- Rough estimate

**You can paste from Jira, Linear, or describe briefly.**

---

### Step 1: Pre-Split Validation (INVEST Check)

Before splitting, verify the story satisfies INVEST criteria (except "Small"). **Agent asks sequentially, one per turn:**

**1. Independent?** "Can this story be prioritized and developed without hard technical dependencies on other stories?"
- Yes — no blocking dependencies / No — requires other work first (flag this)

**2. Negotiable?** "Does this story leave room for the team to discover implementation details collaboratively, rather than prescribing exact solutions?"
- Yes — it's a conversation starter / No — too prescriptive (may need reframing)

**3. Valuable?** "Does this story deliver observable value to a user?"
- Yes — users see/experience something different / No — it's a technical task

**⚠️ Critical check:** If the story fails "Valuable," STOP. Don't split. Instead, combine with other work to create a meaningful increment.

**4. Estimable?** "Can your team size this story relatively (even if roughly)?"
- Yes — team can estimate days/points / No — too much uncertainty (may need a spike first)

**5. Testable?** "Does this story have concrete acceptance criteria that QA can verify?"
- Yes — clear pass/fail conditions / No — refine acceptance criteria before splitting

**If the story passes all checks → Step 2. If it fails any check → fix that issue first.**

---

### Step 2: Walk the Splitting Patterns Sequentially

Read the pattern definitions in [`../user-story-splitting/SKILL.md`](../user-story-splitting/SKILL.md) (Step 2) before this phase. For each pattern in order, ask the diagnostic question below; on the first YES, gather the specifics and generate the split per the reference's definition and examples. On NO, continue to the next pattern.

| # | Pattern | Diagnostic question | If YES, gather |
|---|---------|--------------------|----------------|
| 1 | Workflow Steps | "Does your epic involve a multi-step workflow where you could deliver a simple end-to-end case first, then add intermediate steps later?" | The workflow steps |
| 2 | Operations (CRUD) | "Does your epic use words like 'manage,' 'handle,' or 'maintain' — bundling multiple operations?" | The operations (Create/Read/Update/Delete/etc.) |
| 3 | Business Rule Variations | "Are there different business rules for different scenarios (user types, regions, tiers, conditions)?" | The rule variations |
| 4 | Data Variations | "Does it handle different data types, formats, or structures?" | The data variations (deliver simplest first) |
| 5 | Data Entry Methods | "Are there fancy UI elements (date pickers, autocomplete, drag-and-drop) that aren't essential to core functionality?" | The UI enhancements (basic input first) |
| 6 | Acceptance Criteria Complexity | "Do the acceptance criteria contain multiple When/Then pairs?" | The When/Then boundaries |
| 7 | Major Effort | "Is the first implementation hard, with later additions trivial?" | The first implementation + the additions |
| 8 | Simple/Complex | "What's the simplest version that still delivers value — can you strip complexity and add it back later?" | The simplest core + deferred variations |
| 9 | External Dependencies | "Does it depend on multiple external systems or APIs?" | The dependency boundaries |
| 10 | DevOps Steps | "Does it require complex deployment, infrastructure, or operational work?" | The operational increments |
| 11 | Defer Performance | "Can you deliver functional value first and optimize performance/security/scale later?" | The functional version + the optimization |
| 12 | TADs / Break Out a Spike | Nothing applied — high uncertainty. "What's the biggest unknown preventing you from splitting this epic?" | See below |

**Pattern 1 caution (most common mistake):** split into thin end-to-end slices, not step-by-step stages — see the reference's Pattern 1 for the wrong-vs-right example.

**If you reach Pattern 12,** offer the unknowns as options:
1. **Technical feasibility** — "Can we build this with our stack?"
2. **Approach uncertainty** — "Multiple ways to solve it, unclear which is best"
3. **External dependency** — "Don't know what the third-party API provides"

Then recommend: "Run a 1-2 day spike to answer [question]. After the spike, come back and we'll split the epic with better understanding." Spikes produce learning, not shippable code — after the spike, restart at Pattern 1.

---

### Step 3: Evaluate Split Quality

**After splitting, agent asks:**

**1. Does this split reveal low-value work you can deprioritize or eliminate?**
- Good splits expose the 80/20 principle: most value concentrates in a small portion of functionality
- Example: after splitting "Flight search" into 4 stories, you realize "flexible dates" is rarely used → deprioritize or kill it

**2. Does this split produce more equally-sized stories?**
- Equal-sized stories give Product Owners greater prioritization flexibility
- Example: instead of one 10-day epic, five 2-day stories allow reordering mid-sprint

**If the split doesn't satisfy either criterion, try a different pattern.**

---

### Cynefin Domain Considerations

**Agent asks:** "How much uncertainty surrounds this epic?"

1. **Low uncertainty (Obvious/Complicated)** — "We know what to build; it's just engineering work" → find all stories, prioritize by value/risk
2. **High uncertainty (Complex)** — "We're not sure what customers want or what will work" → identify 1-2 **learning stories**; avoid exhaustive enumeration (the work itself teaches what matters)
3. **Chaos** — "Everything is on fire; priorities shift daily" → **defer splitting** until stability emerges; stabilize first

---

### Output: Generate Story Breakdown

Write each story using the format in `../user-story/SKILL.md`.

```markdown
# Epic Breakdown Plan

**Epic:** [Original epic]
**Pre-Split Validation:** ✅ Passes INVEST (except Small)
**Splitting Pattern Applied:** [Pattern name]
**Rationale:** [Why this pattern fits]

---

## Story Breakdown

### Story 1: [Title] (Simplest Complete Slice)

**Summary:** [User-value-focused title]

**Use Case:**
- **As a** [persona]
- **I want to** [action]
- **so that** [outcome]

**Acceptance Criteria:**
- **Given:** [Preconditions]
- **When:** [Action]
- **Then:** [Outcome]

**Why This First:** [Delivers core value; simpler variations follow]
**Estimated Effort:** [Days/points]

### Story 2..N: [Title] (Variations)
[Repeat the structure above]

---

## Split Evaluation
- **Reveals low-value work?** [Which stories could be deprioritized/eliminated?]
- **Equal-sized stories?** [Are stories roughly equal in effort?]

## INVEST Validation (Each Story)
[Confirm Independent / Negotiable / Valuable / Estimable / Small (1-5 days) / Testable]

## Next Steps
1. **Review with team:** Do PM, design, engineering agree?
2. **Check for further splitting:** Any story still >5 days? Restart at Pattern 1 for that story.
3. **Prioritize:** Which story delivers most value first?
4. **Consider eliminating:** Did the split reveal low-value stories? Kill or defer them.
```

---

## Examples

### Example: Iterative Splitting Across Multiple Patterns

**Epic:** "Checkout flow with discounts (member, VIP, first-time) and payment (Visa, Mastercard, Amex)"

**First pass — Pattern 1 (Workflow):** YES →
- Story 1: Add items to cart · Story 2: Apply discount · Story 3: Complete payment

**Story 2 still 4 days → re-split. Pattern 3 (Business Rules):** YES →
- Story 2a: Member discount (10%) · 2b: VIP discount (20%) · 2c: First-time discount (5%)

**Story 3 still 5 days → re-split. Pattern 7 (Major Effort):** YES →
- Story 3a: Accept Visa (build payment infrastructure) · 3b: Add Mastercard, Amex

**Final breakdown:** 6 stories, all 1-2 days each. For per-pattern worked examples (CRUD, Simple/Complex, thin end-to-end workflow), see the reference skill.

---

## Common Pitfalls

### Pitfall 1: Skipping Pre-Split Validation
**Symptom:** Jump straight to splitting without checking INVEST.
**Consequence:** You split a story that shouldn't be split (not Valuable = technical task).
**Fix:** Always run Step 1 before Step 2.

### Pitfall 2: Restating Pattern Content Instead of Consulting the Reference
**Symptom:** Improvising pattern definitions from memory mid-session.
**Consequence:** Drift from the methodology; wrong splits (especially step-by-step workflow slicing).
**Fix:** Read `../user-story-splitting/SKILL.md` before Step 2 and generate splits from its definitions and examples.

### Pitfall 3: Forcing a Pattern That Doesn't Fit
**Symptom:** "We'll split by workflow even though there's no sequence."
**Consequence:** Arbitrary, meaningless split.
**Fix:** If a pattern doesn't apply, say NO and continue to the next one.

### Pitfall 4: Not Re-Splitting Large Stories
**Symptom:** Split the epic into 3 stories, but each is still 5+ days.
**Consequence:** Stories too large for a sprint.
**Fix:** Restart at Pattern 1 for each large story until all are 1-5 days.

### Pitfall 5: Ignoring Split Evaluation (Step 3)
**Symptom:** Split but never ask whether it reveals low-value work.
**Consequence:** Miss the opportunity to eliminate waste.
**Fix:** After splitting, ask: "Does this reveal work we can kill or defer?"

---

## Practice & Skill Development

**Humanizing Work recommendation:** Teams reach fluency in **2.5-3 hours** across multiple practice sessions.

1. **Analyze recently completed features** (hindsight makes patterns obvious)
2. **Walk completed work through the flowchart** — which pattern would have applied?
3. **Find multiple split approaches** for each feature
4. **Build shared vocabulary** of domain-specific pattern examples

**Don't skip practice work.** Skill develops through analyzing past deliverables, not just refining future work.

---

## Prerequisites
- `epic-hypothesis` — the epic to split (or any backlog item too large to deliver in one iteration)

## Next steps
- `user-story` — write out the split stories with acceptance criteria
- `prd-development` — feed the story breakdown into the PRD's requirements section

## References

### Related Skills
- [`../user-story-splitting/SKILL.md`](../user-story-splitting/SKILL.md) — **The canonical pattern reference**: full definitions, examples, and anti-patterns for every split pattern used in this session
- [`../user-story/SKILL.md`](../user-story/SKILL.md) — Format for writing the split stories
- [`../epic-hypothesis/SKILL.md`](../epic-hypothesis/SKILL.md) — Original epic format
- `workshop-facilitation` — Facilitation protocol for this session

### External Frameworks
- Richard Lawrence & Peter Green, *The Humanizing Work Guide to Splitting User Stories* — Complete methodology (https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/)
- Bill Wake, *INVEST in Good Stories* (2003) — Quality criteria

---

**Skill type:** Interactive
**Suggested filename:** `epic-breakdown-advisor.md`
**Suggested placement:** `/skills/interactive/`
**Dependencies:** Delegates pattern definitions to `user-story-splitting`; uses `user-story`, `epic-hypothesis`, `workshop-facilitation`
