---
name: learn-iterate
description: "Run the post-release learning checkpoint: score what shipped against the PRD's success criteria, extract insights, decide persevere/iterate/expand/kill, and update the PRD so the next cycle starts from evidence. Use when a release is past its post-launch checkpoint date. Do NOT use for operational incidents (incident-postmortem)."
type: component
domain: 4-iteration
---

# Learn & Iterate

## Purpose
Close the product loop after Delivery ships and the PRD goes Live. This is the
blueprint's final column — **Learn & Iterate** — where the team compares what
actually shipped against the Product Brief's success criteria and the PRD's
metrics, extracts insights, decides explicit adjustments, and revises the PRD
(the blueprint's "PRD – Updated (Iteration)"). The outcome: the next cycle's
intake starts from evidence, not memory, and every feature gets a real verdict
instead of quietly drifting.

## Outputs
**Artifact:** iteration review — success-criteria scorecard (target vs actual
vs verdict), insights, decided adjustments (each tagged persevere / iterate /
expand / kill), and the PRD delta.
**Format:** markdown
**Location:** `docs/product/iterations/<feature>-<date>.md` in the product
repo, plus the revision applied to the PRD itself (its "Live → Updated" step).
**Audience:** the product team and the next cycle's intake — whoever writes the
next `product-brief` reads this first.

## Prerequisites
- A shipped release that went out through `release-readiness` — its post-launch
  plan names the metrics to watch and books the checkpoint date this skill runs
  at.
- The PRD's success criteria (from `prd-development`, originally seeded by the
  `product-brief`). No criteria on record = nothing to score; write them down
  first, honestly dated, before reviewing.

## Workflow

### 1. Check the timing
Run the first checkpoint at the date booked in the `release-readiness`
post-launch plan — that date was chosen when nobody was defensive about the
result. Don't judge a feature in its first noisy week (launch spikes, novelty
effects, cache-cold performance) unless it's on fire; if it *is* on fire,
that's an incident, not an iteration review — stabilize first.

### 2. Gather the evidence
Collect signal across four channels before forming any opinion:

- **Product metrics** — the actuals for each PRD success criterion, from the
  instrumentation named in the post-launch plan.
- **Error / stability signal** — pull issue and event trends for the release
  window via `../sentry-cli/`.
- **Business movement** — where the feature claimed revenue, retention, or
  efficiency impact, quantify it with `../saas-revenue-growth-metrics/` or
  `../business-health-diagnostic/`.
- **Qualitative signal** — support-ticket themes, user feedback, sales/CS
  anecdotes. Quotes, not vibes.

### 3. Score the success criteria
Build the scorecard — one row per criterion the PRD committed to:

| Criterion | Target | Actual | Verdict |
|---|---|---|---|
| e.g. activation rate | ≥ 25% | 19% | missed |

Verdicts: **met**, **trending** (moving toward target, re-check at a named
date), **missed**. Score only the criteria that were written down before
launch — no retro-fitting kinder ones. If a criterion **can't be scored**,
that is an instrumentation gap: record it as a decided adjustment with an
owner, so it's fixed before the next checkpoint, and mark the verdict
"unmeasurable" rather than guessing.

### 4. Extract insights
Ask two questions of the evidence:

- **What surprised us?** Anything materially off-forecast, in either
  direction, is an insight worth writing down.
- **Which discovery assumption was wrong?** Trace each miss back to the
  assumption in the brief or PRD that produced it. A wrong assumption is a
  `pol-probe` candidate for the next cycle — the lesson is usually "we should
  have tested that for $100 before building it for $100k".

### 5. Decide adjustments — explicitly
Every scorecard verdict forces a decision. Tag each one:

- **Persevere** — criteria met, works as intended: leave it alone. (A real
  decision; write it down so nobody "improves" it next quarter.)
- **Iterate** — partially working, adjustment identified: open a mini-cycle
  through `prd-development` with the change scoped by this review's evidence.
- **Expand** — works better than expected: the follow-on opportunity gets its
  own `product-brief` and enters the next cycle's intake on merit.
- **Kill** — criteria missed and the evidence says the premise was wrong:
  decide retirement now. If it's user-facing, route the announcement through
  `../eol-message/`.

An insight with no adjustment attached is filed, not learned.

### 6. Update the PRD
Append the iteration record to the PRD: the scorecard, the decisions, and
what the next revision changes. This is the blueprint's "PRD – Updated
(Iteration)" output — the PRD is a living document across cycles, never a
fire-and-forget spec. The updated PRD plus this review are the evidence base
the next cycle's `product-brief` starts from.

### 7. Keep operations separate
Anything that *broke* during the window — outages, sevs, data incidents —
gets its own blameless review via `../incident-postmortem/`. Reference the
postmortem from the iteration review if it affected the metrics, but don't
mix operational failure analysis into product learning; they have different
questions, audiences, and guardrails.

## Pitfalls
- **Success theater:** the review reports activity metrics (page views,
  clicks, "engagement") instead of the PRD's actual criteria → everything
  looks fine, nothing is learned → score only the criteria written before
  launch, and flag any substitution explicitly.
- **No decision:** insights are filed and the meeting ends → the next cycle
  repeats the same bets → every verdict must carry a persevere / iterate /
  expand / kill tag with an owner.
- **Judging too early:** week-one noise read as signal → premature pivots or
  false confidence → hold to the checkpoint date booked at release; note
  "trending" and re-check rather than verdict-flipping daily.
- **Unkillable features:** criteria missed, cycle after cycle, with no kill
  decision → zombie surface area taxing every future release → a repeated
  "missed" verdict without a kill or iterate decision is itself a review
  failure; escalate it.
- **Instrumentation gaps discovered at review time and never fixed:** the same
  criterion is unmeasurable at the next checkpoint too → record the gap as an
  owned adjustment in step 3, and verify it's closed before the next review.

## Next steps
- `product-brief` — the next cycle's intake, started from this review's
  evidence (including "expand" decisions).
- `prd-development` — scope the mini-cycle for each "iterate" decision.
- `../eol-message/` — announce any "kill" decision that touches users.
