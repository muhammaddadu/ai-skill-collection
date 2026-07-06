---
name: adr
description: "Record an architecture decision — context, options, decision, consequences — in the repo's append-only ADR log. Use when choosing between technologies/patterns/approaches, answering 'why did we choose X', or documenting a decision (ADR / Architecture Change Record, ACR). Do NOT use for full system designs (tech-spec) or product decisions (prd-development)."
type: component
domain: 2-discovery
---

# adr — Architecture Decision Records

## Purpose

Capture one significant architecture decision — the context that forced it, the
options that were genuinely on the table, the choice made, and its consequences —
as a short, numbered, append-only record in the target repo. The artifact is a
file, but the point is the **discipline**: writing the ADR forces the options to
be enumerated honestly *before* the decision hardens, and the log preserves the
WHY so future engineers (and agents) don't relitigate or accidentally reverse it.
An ADR is a page, not a paper: if it takes more than ~30 minutes to write, the
decision probably needs a tech spec first, not a longer ADR. Known in the org
blueprint as the **Architecture Change Record (ACR)** — same artifact.

## Outputs

**Artifact:** one ADR file (plus an index line in `docs/adr/README.md`)
**Format:** markdown (MADR-flavored: context → options → decision → consequences)
**Location:** `docs/adr/NNNN-<slug>.md` in the target repo — `NNNN` is a
zero-padded sequence number (`0001`, `0002`, …) that is **never renumbered**,
`<slug>` is a short kebab-case summary of the decision
**Audience:** current and future engineers on the repo (human and AI)

## Prerequisites

- A specific decision to record — either one being made now, or one already made
  whose rationale is about to be lost. If the input is a whole system design with
  many open decisions, that's `../tech-spec` territory; spec first, then come
  back here for each decision it settles.

## Does this decision deserve an ADR?

ADRs are for decisions that are **hard to reverse, cross-cutting, contested, or
surprising**. Examples: choosing a database or framework, adopting or rejecting
an architectural pattern (hexagonal, event sourcing, monorepo), setting a
boundary (what the core may depend on), picking a wire format, deciding *not*
to do something everyone expects.

Not for reversible local choices: a variable name, one module's internal
structure, a library that one file uses and a one-line diff could swap out.

**Three-question litmus test** — record an ADR if you answer *yes* to at least
one:

1. **Expensive to undo?** Would reversing this in six months cost days of
   migration rather than minutes of refactoring?
2. **Beyond one module?** Does it constrain how other parts of the system (or
   other teams) must be built?
3. **Would a smart newcomer ask "why on earth…"?** Is the choice contested now,
   or surprising enough that someone will question it later without the context?

Three noes → skip the ADR; a code comment or commit message is enough.

## Workflow

### 1. Detect the existing convention — and follow it

Before creating anything, check whether the repo already records decisions:

- Look for `docs/adr/`, `docs/adrs/`, `docs/decisions/`, `adr/`, `doc/adr/`,
  or an `.adr-dir` file (used by adr-tools).
- If a directory exists, **adopt its conventions wholesale**: its numbering
  width, filename style, section headings, and status vocabulary — even if they
  differ from this skill's template. A consistent log beats a "better" format.
- Read the last two or three ADRs there to match tone and depth, and take the
  next sequence number (highest existing + 1; gaps are fine, reuse never).

Only if no decision log exists anywhere in the repo, scaffold one:

- Create `docs/adr/` with a `README.md` index:

  ```markdown
  # Architecture Decision Records

  Significant architecture decisions, one per file, append-only.
  See ../<how the repo routes docs, if it has a docs index>.

  | ADR | Title | Status |
  |-----|-------|--------|
  | [0001](0001-<slug>.md) | <Title> | accepted |
  ```

- Every later ADR adds one row to this table in the same change.
- If the repo uses the `agent-docs` conventions (an `AGENTS.md` /
  `docs/README.md` routing index exists), add a routing row for `docs/adr/`
  there too, and give the README the standard ownership header
  (`> **This doc owns:** architecture decision records — the WHY behind …`).

### 2. State the decision to be made

Write the question as a single sentence before anything else: *"Which X do we
use for Y?"* or *"Do we do Z?"*. If you can't phrase it as one decidable
question, it's several ADRs (or a tech spec). Run the litmus test above; if it
fails, say so and stop — don't produce a record nobody needs.

### 3. Capture context and forces

Copy `references/adr-template.md` to `docs/adr/NNNN-<slug>.md` and fill the
Context section first: the situation forcing a choice, the constraints that are
actually binding (team size, existing stack, deadlines, compliance, performance
targets), and the decision drivers ranked by importance. Context is the part
future readers can't reconstruct — spend your words here. Facts only; no
foreshadowing of the answer.

### 4. Enumerate 2–4 real options with honest trade-offs

Each option gets a name, a one-line description, and genuine pros *and* cons.
Rules of honesty:

- Every option listed must be one a reasonable engineer could pick. If you
  can't write a sincere "pro" paragraph for it, it doesn't belong in the list.
- The winning option must have at least one real con; the losing options at
  least one real pro. A lopsided table is a straw-man tell.
- "Do nothing / status quo" is often a legitimate option — include it when it is.

### 5. Record the decision — and why the losers lost

State the chosen option in one sentence, then the rationale: which decision
drivers it won on, and **explicitly why each rejected option was rejected**.
"Option B lost because driver 1 (operational simplicity) outweighed its
performance edge" is the sentence future readers come for. A decision without
the losers' obituaries is half an ADR.

### 6. Consequences — good AND bad

What becomes easier, what becomes harder, what new obligations appear
(migrations, training, monitoring, a dependency to track), and what would
trigger revisiting this decision. Every real decision has costs; an ADR with
only positive consequences is advertising, not a record.

### 7. Set the status and keep the log append-only

Status lifecycle: `proposed` → `accepted` (or `rejected`) → later possibly
`superseded by ADR-NNNN` / `deprecated`.

- New ADR awaiting agreement: `proposed`. Once the humans who own the decision
  agree: `accepted`. Recording a decision that was already made and shipped:
  `accepted` directly, with the original decision date.
- **Never delete or rewrite an accepted ADR.** When a decision changes, write a
  *new* ADR that explains what changed and why, mark it as superseding the old
  one, and update the old ADR's status line to `superseded by ADR-NNNN` — that
  status line is the only edit an accepted ADR ever receives. The old record
  stays: it documents why the original choice was right *at the time*.
- Update the README index row in the same change.

## Relationship to sibling skills

- **`../tech-spec`** — a tech spec explores a whole design and typically
  *spawns several ADRs*, one per significant decision it settles. The spec can
  then link to the ADRs instead of restating rationale. Conversely, if what
  started as "one decision" keeps sprouting sub-decisions, stop and write the
  spec first.
- **`agent-docs`** — if the target repo uses those conventions, ADRs slot in
  cleanly: they are compatible with the one-fact-one-home rule because **the
  ADR owns the WHY** of a decision. Architecture docs state *what* the current
  design is and link to the ADR for the reasoning — never restate it. ADRs are
  append-only records, the same discipline as `LEARNINGS.md`.
- **`prd-development`** — product/scope decisions (what to build,
  for whom) belong in the PRD, not the ADR log. An ADR may *cite* a PRD
  requirement as a decision driver.

## Pitfalls

- **Post-hoc justification:** the ADR is written after the code shipped, with
  options reverse-engineered to make the outcome look inevitable → the log
  becomes marketing and readers stop trusting it → it's fine to record an
  already-made decision, but say so honestly: real alternatives that were
  considered (or "alternatives were not seriously evaluated — recorded for
  posterity"), real cons of the winner.
- **Straw-man options:** two joke options padded around the predetermined
  winner → the "decision" was never a decision, and the record misleads future
  readers about what was actually weighed → apply step 4's honesty rules; if
  only one option was ever viable, question whether this needs an ADR at all.
- **Rewriting history:** editing an accepted ADR's decision or rationale when
  the choice changes → the audit trail is destroyed and links from code/docs
  now point at text that never governed anything → supersede instead: new ADR,
  old one gets only a `superseded by ADR-NNNN` status line.
- **ADR sprawl:** recording every library bump and naming choice → dozens of
  trivial records bury the five that matter, and the team stops reading (and
  writing) them → run the three-question litmus test; when in doubt for small
  stuff, leave it to a commit message.
- **Consequences as a victory lap:** only benefits listed, no costs, no revisit
  triggers → the first engineer who hits the downside assumes the authors never
  saw it and reopens the whole debate → force at least one negative consequence
  and one "revisit if…" condition into every ADR.

## Next steps

- Decisions feed back into `../tech-spec`: an accepted ADR narrows the design
  space of the spec that spawned it (or of the next spec touching that area) —
  link the ADR from the spec rather than restating the rationale.
- Enforcing the chosen architecture (dependency rules, boundary checks,
  "does this PR violate ADR-0007?") belongs to each repo's own review
  agents/CI — e.g. an architecture-guardian subagent in that repo's
  `.claude/agents/` — not to this skill. This skill records decisions; it does
  not police them.
