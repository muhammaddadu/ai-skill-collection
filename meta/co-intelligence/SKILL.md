---
name: co-intelligence
description: "Decide whether and how to use AI on a task, choose a human-AI working mode, and review drafts for over-reliance. Use when delegating or dividing knowledge work with AI; not for prompt syntax, model selection, or artifact-specific critical review."
type: advisor
domain: meta
---

# Co-intelligence

## Purpose

Turn the framework in Ethan Mollick's *Co-Intelligence: Living and Working with AI* into checkable working
practice, and pair it with the strongest published evidence on where AI measurably helps and hurts. The book
supplies the operating stance. The research supplies the guardrails. Held together they are more useful than
either alone — because the stance without guardrails produces confident wrong work, and the guardrails
without the stance produce paralysis.

For whom: anyone doing knowledge work with AI where being wrong has a cost.

## Outputs

**Artifact:** A go/no-go decision on using AI for a task, a chosen working mode, and a verified draft
**Format:** No file — this is a decision and a review discipline applied to other work
**Audience:** Yourself, before a human sees the output

## The jagged frontier — the one concept to internalise

AI capability is **uneven, and the boundary is invisible**. Two tasks that look equally hard to a human can
sit on opposite sides of it: one the model does excellently, the next it fails at confidently. The frontier
is jagged rather than a clean line, and you cannot see its shape from outside — only by probing.

The clearest published illustration: the same model scored **91.2%** on a standard text-to-SQL benchmark and
**21.3%** on real enterprise warehouses with 1,000+ columns `[PREPRINT, Spider 2.0, arXiv 2411.07763]`. Same
model, same task type, harder database. That gap *is* the frontier's edge, measured.

⚠️ Mollick's own field research with BCG consultants is widely cited as showing AI improved quality inside
the frontier and made results **worse** outside it — figures around a 40% improvement inside and roughly 19
percentage points worse outside. **Verify those numbers against the paper before quoting them**
(Dell'Acqua, Mollick et al.). They are exactly the kind of round figure that circulates unchecked.

### Working practice

Before handing a task to AI, ask which side of the frontier it is on. If you don't know, **probe cheaply
rather than assuming**.

| Reliably inside | Reliably outside |
|---|---|
| Drafting, restructuring, summarising text you can check | Anything resting on a fact you cannot verify |
| Generating options to react to | Arithmetic that becomes load-bearing |
| Finding the shape of an argument | Judging what an organisation will politically tolerate |
| Extraction from a source in front of it | Knowing what a source *doesn't* say |
| Critique against explicit criteria | Deciding the criteria |

**The dangerous zone is not "outside the frontier." It is "just outside, and fluent about it."** Confident
wrong output on an adjacent-looking task is the failure mode, and sweeping negative claims are its most
common form — "nobody has done this," "no vendor offers that." Those are usually written from an incomplete
sample, and usually in the direction that flatters the author.

## The four principles, and the guardrail each one needs

Mollick's four. Each is sound; each has a measured limit worth knowing.

### 1. Always invite AI to the table

**The principle:** use it on everything, because you learn the frontier's shape only by probing.

**The guardrail:** for experienced practitioners on familiar work, it is not free. A randomised trial of 16
experienced open-source developers found them **19% slower** with AI — while predicting a 24% speedup
beforehand and still believing in a 20% speedup afterwards `[METR, July 2025]`. METR's own more favourable
follow-up is one **they explicitly disown** as unreliable.

**Resolution, not contradiction.** Invite it in *to learn where it helps* — that is the principle's point.
But do not assume the answer is "everywhere," and **never build a business case on self-reported
productivity**: the same researchers measured people overestimating AI's effect on their own task time by
**40 percentage points**.

### 2. Be the human in the loop

**The principle:** you remain accountable. Check the work.

**The guardrail — the one most people get wrong.** Being in the loop is harder than it sounds, and
transparency can make it worse:

- 22 professional analysts reviewing AI analyses that contained deliberate errors mostly checked *procedure*
  ("what did it do?") rather than *data* ("does this number make sense?") `[PEER-REVIEWED, CHI 2024]`
- 14 practitioners shown the agent's reasoning trace **used it to rationalise wrong answers**; the authors
  concluded the trace "instilled confidence in incorrect answers" and recommended adding friction
  `[PEER-REVIEWED, AVI 2026]`
- Hallucination warnings are the **weakest** intervention measured. A disclaimer is not a control

**So "human in the loop" means data-oriented verification against an independent source — not reading the
output and finding it reasonable.** If your check is "that looks right," you are not in the loop.

### 3. Treat AI like a person, but tell it what kind of person it is

**The principle:** personas and role framing change output quality.

**The guardrail: curated context beats persona by a wide margin.** One published internal deployment went
from **21% to over 95%** accuracy on the same model and same data, purely from curated procedural context —
then decayed to **~65% within a single month** when that context wasn't maintained. Giving the model raw
access to thousands of prior queries moved accuracy **under one percentage point** `[FIRST-PARTY ENG, 2026]`.

Persona is cheap and helps at the margin. **Context is the lever, and it is a standing maintenance cost,
not a one-off setup.**

### 4. Assume this is the worst AI you will ever use

**The principle:** capability is improving; design for what is coming.

**The guardrail:** true for your own tooling, dangerous in a commitment. Build so that improvement helps you
— curated context, clean interfaces, measured baselines — but **never promise anyone an outcome contingent
on a model getting better.** Separate "I expect this to get easier" from "I have committed to deliver it."

## Centaur or cyborg — pick deliberately

Mollick's two working modes:

- **Centaur** — clear division of labour. You do the parts you're better at, AI does the rest, with a
  visible handoff line.
- **Cyborg** — deeply interleaved. Blending at the level of the sentence or step, back and forth.

Neither is superior. The choice turns on **whether you need to know who authored what**.

| Use centaur when | Use cyborg when |
|---|---|
| The work is load-bearing and must be traceable | The work is exploratory, or will be checked later |
| You must state which parts you authored | Iteration speed matters more than provenance |
| A reviewer, auditor or regulator may ask | You are still finding the shape of the problem |

**Default: centaur for anything going to a stakeholder, cyborg for exploration.** The reason is provenance.
If your process requires tagging claims as fact versus assumption — and any serious analytical work does —
interleaved drafting destroys the audit trail that tagging depends on. You cannot attribute what you cannot
remember writing.

## Human accountability — four questions

| Question | The discipline behind it |
|---|---|
| **Which parts require human judgment?** | Decisions involving context, ethics, risk or organisational impact do not get delegated |
| **Who is accountable for the final decision?** | AI can advise; accountability belongs to a person. Name them |
| **Am I trusting this because it is correct, or because it sounds confident?** | Treat fluency as presentation quality, **not proof** |
| **What would I verify if this had been written by a junior colleague?** | Apply the *same* standard to AI output. No lower, no higher |

**The third question is the most valuable line in this skill**, and there is a measurement behind it. In one
published deployment, users rated a system whose expert-reviewed accuracy was **53% correct** as **95%
acceptable** — same system, same period. The difference was fluency `[PREPRINT, 2025]`.

**Fluency and correctness are independent variables.** Ask the question out loud on anything load-bearing.

The fourth question is what makes the third actionable. If a junior colleague handed you this, you would
check the two numbers carrying the argument and the one claim that sounds too clean. Do exactly that.

### Two scope questions worth keeping

- **"Which requirements are essential, and which are preferences?"** — stops optional detail hardening into
  hidden commitment.
- **"What are we deliberately not solving?"** — makes boundaries explicit rather than leaving them to be
  discovered. Work that cannot answer this reads as unbounded, which is how scope arguments start.

## The reusable review prompt

Run this on your own output before a human sees it. It is the most directly actionable thing here.

> Review your previous answer critically. Identify hidden assumptions, the riskiest failure modes, missing
> evidence, strong counterarguments, and simpler alternatives. Separate verified facts from inferences. For
> every important claim, provide an inspectable form of evidence such as a source, runnable example, test,
> diagram, screenshot, benchmark, or proof of concept. End with a clear recommendation, confidence level,
> unresolved questions, and what a human must verify before acting.

**Why this works** where a generic "check your work" does not:

- **"Separate verified facts from inferences"** forces the fact/assumption distinction explicitly
- **"An inspectable form of evidence"** is the fix for verification theatre. A URL that resolves is not
  inspectable evidence for a *specific sentence* — a citation can resolve and still fail on evidentiary fit
- **"Strong counterarguments"** forces the counter-evidence a one-sided case omits, and a one-sided case
  loses the room
- **"Simpler alternatives"** is the check nobody runs, and where over-engineering gets caught
- **"What a human must verify before acting"** converts a draft into a handover with a named next step

**Run it alongside the workflow below, not instead of it.** A model critiquing itself is still inside its own
frontier.

## Workflow

Four checks, in order, before AI output goes anywhere:

1. **Frontier check.** Which side is this task on? If unknown, probe cheaply before committing.
2. **Mode check.** Centaur or cyborg? If it's going to a stakeholder, centaur.
3. **Verification check.** Did you verify against an independent source, or find it plausible? Only the
   first counts. Data-oriented, not procedure-oriented.
4. **Convenience check.** Is this the conclusion you wanted? If yes, **raise** the evidence bar rather than
   lowering it. Convenient conclusions are where confident errors live.

Then run the review prompt above, and act on what it surfaces rather than noting it.

## Pitfalls

- **Fluent means correct:** well-structured prose reads as verified → a false claim ships → ask the fluency
  question; check the numbers that carry the argument.
- **Convenient means true:** the conclusion you hoped for gets less scrutiny → confident error → raise the
  bar when the answer flatters you.
- **Verification theatre:** confirming a source *exists* rather than that it supports the specific sentence
  → citations that resolve and still mislead → check the claim against the source, not the URL.
- **Arithmetic as analysis:** multiplying numbers nobody stated into a total that looks researched →
  fabricated figure treated as fact → never introduce a number the source did not state.
- **Inheriting a paraphrase:** a summary of a summary, carried several documents deep → compounding drift →
  re-fetch the primary source and state the correction.
- **Assuming the frontier is smooth:** trusting a benchmark number as a production number → 50-point
  surprises → treat benchmark and production as different measurements.

## What this skill does not claim

- It is **not** the book. Read *Co-Intelligence* for the argument, the evidence and the futures discussion.
- It does **not** settle whether AI improves knowledge work overall. The evidence is genuinely mixed:
  throughput up and stability down `[DORA 2025]`; a 15% gain concentrated in the *least* experienced workers
  in the strongest peer-reviewed study `[QJE 140(2), 2025]`; and a clean RCT showing a slowdown for experts.
- It does **not** license using AI on work you cannot check. That is the one line it does not bend.

## Next steps

- `divergent-ideation` — widen and evaluate alternatives when the task needs a
  broader option set; it owns the generation workflow and its execution modes
- `humanizer` — strip AI register from anything a human will read
- `fewer-permission-prompts` — reduce friction once you know which tasks you delegate routinely

See `ATTRIBUTION.md` for sources and what is original here.
