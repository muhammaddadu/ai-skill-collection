---
name: critical-review
description: "Critically review an artifact by challenging assumptions, failure modes, evidence, alternatives, measurement, scope, and accountability. Use when asked to challenge, stress-test, or red-team a draft before sign-off. Do NOT use for AI-task selection (`co-intelligence`) or line-level code review."
type: component
domain: meta
---

# Critical review

## Purpose

Challenge a finished-looking artifact instead of polishing it. AI (and tired humans) default to
improving grammar and structure while leaving the load-bearing claims untested; this skill forces the
review to attack the substance — what is assumed, what breaks, what is actually evidenced — and to end
in a decision-ready report. It works on anything with claims and consequences: a PRD, design doc,
architecture, migration plan, analysis, or an AI-generated recommendation.

The core principle: the reviewer can be AI, but judgment, evidence standards, and the final decision
remain human. Nothing important goes to production on unverified claims.

## Outputs

**Artifact:** Critical review report — per-dimension findings (covered vs gaps) + a short prioritized action list
**Format:** markdown
**Location:** chat reply by default; save to `docs/reviews/critical-review-<artifact-slug>-<YYYY-MM-DD>.md` in the target repo when the review should be kept
**Audience:** the artifact's owner and whoever signs off on it

## Prerequisites

- The artifact under review, and access to whatever ground truth can verify its claims (the codebase,
  the data, the primary sources). A review that can only read the artifact grades its prose, not its truth.

## Workflow

1. **Ground the review.** Read the artifact fully. Separate its claims into *checkable* (against code,
   data, sources) and *judgment* (targets, trade-offs, taste). Verify the checkable ones you can reach —
   findings anchored in ground truth are the ones that survive pushback.
2. **Challenge across the seven dimensions** below. For each: note briefly what the artifact already
   answers well (so strengths aren't regressed), then the gaps — specific, actionable, and tied to where
   in the artifact they belong.
3. **Demand inspectable evidence** for every important claim you keep and every finding you raise: a
   source, runnable example, test result, benchmark, trace, screenshot, or proof of concept. A
   confident sentence is presentation, not proof.
4. **Report, don't fix.** Use the report structure below, end with the 3–5 actions that most change the
   decision, and stop. Apply fixes only when the owner asks.

## The seven dimensions

Ask every question; skip none silently. The gloss under each is *why* it earns its place.

### 1. Assumptions
- **What assumptions are we making?** List explicit *and* hidden ones — the hidden ones do the damage.
- **Which assumption is the riskiest?** Order by damage-if-wrong, and put the review's weight there first.
- **What are we treating as fact without evidence?** Separate verified facts from confident-sounding
  guesses; fluency is not verification.

### 2. Failure and production risk
- **If this fails in production, how will it fail?** Realistic failure modes, not only ideal behavior.
- **What is the blast radius?** Affected users, systems, data, cost, operations.
- **How would we detect the failure?** Logs, metrics, alerts, user signals — *and a named owner who
  watches them*. Detection without ownership is a dashboard, not a control.
- **How would we recover or roll back?** A practical recovery path must exist before release, not after.

### 3. Evidence and verification
- **What evidence supports this recommendation?** Prefer primary sources, runnable examples, test
  results, real outputs.
- **Can I inspect the actual result?** Ask for the screenshot, prototype, trace, benchmark, or demo.
- **Has someone done this successfully before?** A proven pattern under comparable constraints lowers
  the burden of proof; novelty raises it.
- **If this is new, what proof of concept should we build?** The smallest experiment that tests the
  riskiest assumption.
- **What evidence would convince me this is wrong?** Define the falsifying evidence *before* becoming
  attached to the solution.

### 4. Counterarguments and alternatives
- **What is the strongest counterargument?** Make the artifact argue against itself.
- **What alternatives did we consider?** Always include the simplest option and *doing nothing*.
- **Why were the alternatives rejected?** Trade-offs must be explicit and evidence-based, not vibes.
- **What would a skeptical expert challenge here?** Adopt that reviewer's persona for a pass; weak
  reasoning surfaces fast under a hostile read.

### 5. Success and measurement
- **What does success look like?** Measurable outcomes, not vague improvement.
- **What is the baseline?** No baseline, no provable improvement.
- **Which leading and lagging indicators will we track?** Early warnings as well as final outcomes.
- **How will we detect regressions?** Thresholds, comparison periods, alerting — numbers, not intent.

### 6. Simplicity and scope
- **Where can we simplify without losing the goal?** Remove complexity before implementation, when it's cheap.
- **What is the minimum viable version?** Smallest scope that tests the value and the risk.
- **Which requirements are essential, and which are preferences?** Optional detail hardens into hidden
  commitments unless labeled.
- **What are we deliberately not solving?** Explicit boundaries are the antidote to scope creep — and to
  compatibility surfaces that grow forever (every legacy format kept "for now" needs a retirement line).

### 7. Human accountability
- **Which parts require human judgment?** Context, ethics, risk, organizational impact — not delegable.
- **Who is accountable for the final decision?** A name, not a team. Empty `Owner:` / `Reviewed by:`
  fields are themselves findings.
- **Am I trusting this because it is correct, or because it sounds confident?** Fluency is presentation
  quality, not proof.
- **What would I verify if a junior colleague had written this?** Apply exactly that standard — no lower,
  no higher.

## Report structure

ALWAYS use this shape (rename headings to match the artifact's vocabulary):

```markdown
# Critical review: <artifact> — <date>
One-line verdict: what the artifact does well and where it would fail the checklist.

## <Dimension 1..7>
**Covered:** what the artifact already answers (1–2 lines).
**Gaps:** specific findings — each with the evidence, where it belongs in the artifact, and why it matters.

## Top actions
1–5 items, ordered by how much each changes the go/no-go decision.
```

## Pitfalls

- **Polishing instead of challenging:** the review fixes commas and misses the untested assumption →
  approve-with-typos-fixed on a flawed plan → attack claims first; style last or never.
- **Findings without evidence:** "this seems risky" is an opinion → it gets argued down and ignored →
  every gap names the missing evidence or the verified contradiction.
- **Grading fluency:** a well-written section reads as a covered dimension → confident holes ship →
  check what the section *proves*, not how it reads.
- **Boiling the ocean:** forty findings bury the four that matter → nothing changes → cap the action
  list at what changes the decision.
- **Reviewing only the text:** claims are graded against the artifact itself → drift between doc and
  reality survives the review → verify against ground truth wherever it is reachable.

## Next steps

- `co-intelligence` — the working stance behind this checklist (jagged frontier, working modes) and the
  reusable self-review prompt to run on your *own* output before a human sees it.

See `ATTRIBUTION.md` for provenance.
