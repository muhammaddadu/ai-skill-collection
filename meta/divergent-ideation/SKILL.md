---
name: divergent-ideation
description: "Generate distinct approaches, cluster them by mechanism, expose attractive traps, and develop a practical shortlist. Use for open-ended brainstorming, naming, strategy, or design alternatives; use domain skills for implementation and critical-review for reviewing an existing artifact."
metadata:
  type: component
  provenance: Adapted from UditAkhourii/adhd; see .upstream and LICENSE.
---

# Divergent ideation

Widen the options before evaluating them. Use when several plausible approaches
exist and a wider search could change the decision. A lookup, known-root-cause
fix, or request for a quick conventional answer usually needs a direct response.
The method is a workflow for generating alternatives, not a claim about model
internals or clinical ADHD.

## Output

**Artifact:** A clustered option set, recommended shortlist, traps with reasons,
and a concrete next experiment for the strongest candidates.
**Format:** Concise Markdown in chat; save only when requested or required by the
hosting workflow, using that workflow's existing document.
**Audience:** The decision-maker and people who will develop the selected option.

## Installation preference

The repository installer runs `scripts/setup_global.py` after linking skills to
maintain a scoped activation rule in detected local clients. A standalone skill
copy does not execute a post-install hook automatically. For requested setup,
preview with `python3 scripts/setup_global.py --dry-run`, apply by omitting that
flag, or remove the managed block with `--remove`. These paths are relative to
this skill folder. Do not run setup merely because this skill is used for ideation.
See the repository README for supported clients, opt-out, and limits.

## 1. Bound the search

Reuse the supplied brief. Identify the outcome, audience, hard constraints,
known evidence, and preferences. Ask only about missing information that would
materially change the options; otherwise label assumptions and proceed.

Keep a conventional or do-less baseline for comparison. Define what a useful
option must achieve before seeing candidates. Scale breadth to the request:
a few lenses and a handful of candidates per lens is usually a useful start.
Do not impose a long workshop on a small decision.

Choose the execution mode allowed by the current session:

- **Single-session pass:** Generate under distinct lenses, then evaluate in a
  separate pass. Describe this honestly as a lens-based exploration; it does not
  provide isolated contexts or independent judgment.
- **Isolated branches:** Only when delegation is available and authorized, run
  bounded generator branches in fresh contexts, using supported concurrency.
  Each receives the same brief and constraints plus one lens, with no candidate
  lists, preferred solution, or other branches' outputs. Give the evaluator the
  combined candidates after generation. Never silently install an SDK, launch
  external paid model calls, or grant agents extra permissions for ideation.

Keep branch output to candidate concepts and concise rationales; do not request
private reasoning traces. State the actual mode when describing the result.

## 2. Generate before judging

Read [references/lenses.md](references/lenses.md) to choose lenses that change
assumptions or mechanisms, rather than merely changing the speaker's job title.
Use contrasting lenses relevant to the brief, with an unusual one when helpful.

Generate short candidates without ranking during this pass. Keep immutable
constraints visible; treat a deliberately relaxed assumption as a hypothetical,
not permission to violate it. Preserve the baseline and explore beyond it.
Do not ban obvious approaches: a conventional solution may still win.

If using branches, a compact assignment is:

> Generate distinct candidate approaches to the supplied brief through this lens.
> Return each concept with a short mechanism/rationale and any assumption it
> changes. Do not rank candidates or expand into implementation. Respect the
> supplied hard constraints. Return concise results, not a reasoning transcript.

## 3. Evaluate and prune

After generation, merge duplicates by underlying mechanism while retaining useful
differences. Group by how an approach works, not shared vocabulary. If every idea
is a variation of the same mechanism, change the lenses for one bounded extra
pass; stop when new candidates repeat existing mechanisms or the budget is used.

Evaluate candidates against the brief: fit, feasibility, novelty, evidence,
cost, and reversibility. Prefer brief grounded comparisons; optional scores are
judgment aids, not measured probabilities. Explain any weights that determine
the choice. Hard-constraint failures cannot be averaged away by novelty.

Name attractive traps with a specific failure mechanism: a displaced cost,
unsupported assumption, incentive problem, operational burden, or hidden dependency.
Distinguish a disqualifying trap from a manageable risk or an unanswered question.
Unknown feasibility calls for a small test, not an invented fact or automatic rejection.

## 4. Develop the survivors

Recommend a small shortlist, usually 2–4 materially different options, and explain
why they beat the baseline. If the baseline wins, say so. Highlight a non-obvious
viable option only when one survives evaluation; do not manufacture a wildcard.

For each serious contender, give a short working sketch, its load-bearing
assumption, main trade-off, and smallest useful experiment with an observable
success/failure criterion. Combine candidates only when the hybrid has a clear
mechanism and addresses a real weakness.

Honor the hosting workflow's human decision gates. When selection would change
the agreed brief, surface the trade-off for the decision-maker. If the user has
delegated selection, make a recommendation and continue within that authority.
Ideation alone does not authorize implementation, publishing, or external writes.

## Handoff

Present the brief, clusters with concise candidates, shortlist and recommendation,
traps, and next experiment. Show the full pool only when useful or requested.
Keep rejected ideas compact so they do not bury the decision. Link evidence for
load-bearing factual claims; label hypotheses and untested analogies.

Pass selected options into the existing domain workflow: `tech-spec` for design,
`brand-creation-studio` for rendered brand exploration, or `ads-create` for campaign
briefs. Their contracts and quality gates still apply. Use `critical-review` for
a requested substantive review of the resulting artifact rather than duplicating
its full checklist here.
