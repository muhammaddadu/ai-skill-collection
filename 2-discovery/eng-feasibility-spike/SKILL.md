---
name: eng-feasibility-spike
description: "Run a time-boxed spike answering ONE engineering feasibility question with evidence — a throwaway POC, benchmark, or vendor-API probe — so the PRD storms on facts. Use when a PRD assumption needs technical proof or architectural impact must surface before Sign-Off 2. Do NOT use for product/demand validation (pol-probe) or full designs (tech-spec)."
type: component
domain: 2-discovery
---

# Engineering Feasibility Spike

## Purpose

Answer **one** engineering feasibility question with evidence, inside a hard
time-box, while the PRD is still storming. This is the Eng Lead's
Investigation/spike lane in the blueprint — the "Eng Feasibility / POC" output
that sits between the Discovery consult and the Architecture Change Record.
Its job is to replace hunches ("the vendor API should handle our volume",
"we can probably do this on-device") with facts *before* the PRD norms and
Sign-Off 2 locks scope, and to surface architectural impact early enough that
it becomes a deliberate decision (an ADR) rather than a mid-delivery surprise.
The deliverable is the **report**, not the code: any POC written along the way
is explicitly disposable.

A spike that proves the approach infeasible is a *success* — it just saved a
delivery cycle. Feasibility here means engineering feasibility (can it be
built, at what cost, with what architectural consequences); whether anyone
*wants* it is `../pol-probe/` territory.

## Outputs

**Artifact:** Spike report — the question, the time-box, what was tried,
findings with evidence, a feasibility verdict, architectural implications, and
a recommendation
**Format:** markdown; evidence inline (numbers, error messages, API responses)
**Location:** `docs/specs/spikes/<question-slug>.md` in the target repo
**Audience:** the PRD-storming group (PM + Eng Lead + design), and the future
tech-spec/ADR authors who inherit the findings

POC code, if any, is **linked from the report and never merged** — an archived
branch, a gist, or a scratch repo. The report must stand alone without it.

### Report skeleton

```markdown
# Spike: <the question, verbatim>

- **Time-box:** <N days>, <start> → <end>
- **Decision this unblocks:** <the PRD/design choice waiting on the answer>
- **Verdict:** feasible | feasible-with-cost | infeasible | unknown-in-time-box

## What was tried
<probe(s) run, in order, and why each was chosen>

## Findings (evidence)
<numbers, error messages, API responses, latency tables — not impressions>

## Architectural implications
<what this forces or forbids in the design; "none" is a valid, explicit answer>

## Recommendation
<what the PRD/design should do given the verdict; next artifact to produce>

## POC disposal
<link to archived branch/gist; confirmation nothing was merged>
```

## Prerequisites

- A storming PRD with a technical assumption in it — see `prd-development` —
  **or** a tech-spec option that needs proof before it can be honestly weighed
  (see `../tech-spec/`, Step 3: options you can't evaluate on paper).
- An Eng Lead (or delegate) who can run the probe and is accountable for the
  verdict — feasibility and architectural impact are their lane.

## Workflow

### 1. Extract the feasibility question — one per spike

Pull the riskiest technical assumption out of the forming PRD and phrase it as
a single **falsifiable** question:

- ✅ "Can vendor X's OCR API process our 30-page scanned PDFs in <10s at
  p95, within the $0.02/doc budget?"
- ✅ "Does streaming 5k concurrent WebSocket sessions fit on our current
  node size without a broker?"
- ❌ "Is the integration feasible?" — not falsifiable; no evidence could
  settle it.
- ❌ "Can we use vendor X, and will the data model scale, and what about
  offline mode?" — three questions, three spikes.

If you can't phrase it as one question whose answer could be *no*, it is not
spike-ready — go back to the PRD and sharpen the assumption first. If several
questions surface, rank them by (risk to the PRD × cost of being wrong) and
spike the top one; the rest queue behind it as separate spikes only if they
still matter after the first answer lands.

### 2. Set the time-box FIRST, and name the decision it unblocks

Before touching any tool, fix two things in the report header:

- **Time-box:** 1–3 days is typical; a spike that needs more than a week is a
  project wearing a disguise — split the question or accept the risk openly.
- **The decision the answer unblocks:** which PRD scope call, tech-spec
  option, or sign-off is waiting on this. If no decision is waiting, the spike
  is curiosity, not discovery — don't run it.

The time-box **ends the spike even without an answer**. That outcome is itself
a finding: "unknown after N days" means the approach carries schedule risk
that the PRD must now carry explicitly. Verdict: `unknown-in-time-box`; the
recommendation says whether to fund a second, differently-shaped spike or to
de-risk by choosing another approach.

### 3. Choose the cheapest sufficient probe

Escalate only as far as the question demands:

| Probe | Cost | Sufficient when… |
|---|---|---|
| Paper analysis | hours | docs/pricing/limits pages can settle it (rate limits, data residency, license terms) |
| Benchmark | hours–1 day | the question is a number (throughput, latency, model accuracy on your data) |
| Vendor sandbox / API probe | ~1 day | the question is "does their API actually do X with our shape of data" |
| Throwaway POC | 1–3 days | the question is integration — do parts A and B actually talk end-to-end |

Two rules govern the choice:

- **Don't build what you can read.** If the vendor's rate-limit page answers
  the question, a POC is waste.
- **Know what a working POC proves — and what it doesn't.** A POC proves
  *integration is possible*; it says nothing about architecture quality,
  operability, error handling, or scale. Never let "the demo works" launder
  itself into "the design is sound" — that laundering is what the
  architectural-implications section exists to prevent.

### 4. Run it; capture evidence as you go

Log evidence *during* the probe, not from memory afterwards:

- Numbers with units and conditions ("p95 412ms at 50 rps, us-east-1, cold
  cache"), not "it was fast enough".
- Verbatim error messages and status codes, with what triggered them.
- Actual API request/response pairs (redact secrets) when behavior deviates
  from the docs — the deviation *is* the finding.
- Costs observed vs. pricing-page promises.

If mid-probe the question mutates ("oh, the real question is auth, not
throughput"), stop and rewrite the header: new question, check the remaining
time-box against it. Don't silently answer a different question than the one
the report promises.

### 5. Verdict, implications, and routing

Close the report with one of four verdicts and route the consequences:

- **feasible** — evidence supports the approach at acceptable cost. Say what
  was *not* tested so the tech spec doesn't over-trust the result.
- **feasible-with-cost** — it works, but with a price the PRD didn't assume:
  latency budget, vendor lock-in, an extra service, an ops burden. Quantify
  the cost; the PRD group decides if it's worth paying.
- **infeasible** — the evidence kills the approach. **That's a win — say so
  plainly in the PRD**, name the killed option and the evidence, and propose
  what to explore instead. A quietly-shelved dead approach gets re-proposed
  in six months.
- **unknown-in-time-box** — the time-box expired first (step 2); the finding
  is schedule risk.

Then route the implications:

- Finding **changes the architecture** (forces a component, forbids a pattern,
  picks a vendor)? Record it via the sibling `../adr/` — this is the
  blueprint's Architecture Change Record, due during PRD Norming, before
  Sign-Off 2. The spike report is the ADR's evidence; link it, don't restate.
- Finding **reshapes the design** without being one crisp decision? Feed it
  into `../tech-spec/` — it hardens an option's trade-off row or eliminates
  the option outright.
- Finding **changes product scope** (a requirement is infeasible or newly
  expensive)? It goes into the storming PRD verbatim — the PM reshapes scope
  on facts, which is the whole point of spiking during Storming.

### 6. Dispose of the POC

Archive the code (branch named `spike/<question-slug>`, or a gist), link it
from the report, and **never merge it**. This rule exists because spike code
is written to answer a question, not to ship: no tests, no error handling,
secrets pasted in, happy path only. Every codebase has a haunted module that
started as "the spike worked, let's just build on it" — spike code merged is
untested code in production with a demo's confidence and a prototype's rigor.
If the approach proceeds, the delivery team **re-implements from the report's
findings** under normal quality gates; the archived POC is a reference for
*what worked*, never a foundation. Delete local scratch copies once archived.

## Pitfalls

- **The spike becomes the implementation:** the POC works, momentum takes
  over, and it ships → untested, unreviewed code becomes a production
  foundation and the quality gate was silently skipped → enforce step 6:
  archive, link, never merge; delivery re-implements from findings.
- **Multi-question mega-spike:** "let's evaluate the whole vendor" bundles
  auth, scale, pricing, and data model into one probe → weeks pass, nothing
  is settled decisively, the time-box is meaningless → one falsifiable
  question per spike (step 1); rank and queue the rest.
- **No time-box — "we'll know it when we see it":** the spike runs until it
  finds a comfortable answer → discovery stalls and the spike quietly becomes
  a pet project → set the box before starting (step 2); expiry-without-answer
  is itself a reportable finding.
- **Verdict without evidence:** the report says "feasible" backed by "it
  seemed fine" → the tech spec inherits a hunch dressed as a fact, and the
  risk resurfaces mid-delivery → every verdict cites numbers, errors, or
  responses captured during the probe (step 4); no evidence, no verdict.
- **Feasibility theater:** spiking the thing everyone already knows works,
  to look diligent while dodging the genuinely scary question → the real risk
  ships unexamined behind a green checkmark → spike the assumption whose
  failure would hurt most (step 1's risk ranking), not the one easiest to
  confirm.

## Next steps

- `../adr/` — record any architecture-changing finding as an Architecture
  Change Record during PRD Norming; the spike report is its linked evidence.
- `../tech-spec/` — fold findings into the design: harden or eliminate the
  option the spike tested.
- `prd-development` — the verdict lands in the storming PRD: scope confirmed,
  re-costed, or cut, with the report linked.
- `pi-planning` — a spiked-and-verdicted question is what makes the
  architecture Dev Ready when Discovery hands off to Delivery.
