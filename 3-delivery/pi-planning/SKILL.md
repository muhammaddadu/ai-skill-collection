---
name: pi-planning
description: "Convert a signed-off, normed PRD into a committed increment: verify design/architecture dev-readiness, draw the MVP cut-line, sequence by risk, cut epics and tickets, mark the PRD Commitment-Ready. Use when planning an increment after Sign-Off 2. Do NOT use for writing the PRD (prd-development) or splitting one epic (epic-breakdown-advisor)."
type: component
domain: 3-delivery
---

# PI Planning

## Purpose

The first Delivery activity, run immediately after Sign-Off 2. Discovery ends
with a normed PRD that stakeholders have validated for scope, sequencing, and
outcomes; this skill turns that validated *intent* into a committed,
executable *plan*: the MVP cut-line is drawn, design and architecture are
verified dev-ready with evidence, work is sequenced by dependency and risk,
and epics/tickets are cut with acceptance criteria attached. It is also the
step where the blueprint's PRD reaches **Commitment-Ready** — scope frozen for
the increment, changes routed through explicit re-planning. The output is what
Engineering executes: AI codes, humans consult, review, and ship.

**This skill plans; it does not relitigate.** Stakeholders already validated
scope and outcomes at Sign-Off 2. If planning surfaces a genuine scope
problem, the move is *back* to `prd-development` and a new sign-off — not a
quiet renegotiation inside a planning session.

## Outputs

**Artifact:** PI plan — MVP scope with explicit cut-lines, dependency-ordered
sequence, readiness verdicts with evidence, and the epic/ticket list
**Format:** markdown (template in Step 8), plus the tickets themselves created
in the team's tracker (or `prd.json` for AI-agent execution via `../ralph/`)
**Location:** `docs/product/pi/<increment-slug>.md` in the product repo,
linked from the PRD it commits
**Audience:** the delivering team (human and AI executors), the PM who owns
the PRD, and the stakeholders who signed off — the plan is how they see their
validated scope become a schedule

## Prerequisites

- A **signed-off, normed PRD** (`prd-development`) — Sign-Off 2 recorded with
  date and attendees. No sign-off, no planning session.
- **Design Signal 90 report** (`design-signal`) — or a plan to reach it, which
  becomes a first-sequence item (Step 2).
- **Current tech spec** (`tech-spec`) covering the increment's scope, with
  open spikes resolved (`eng-feasibility-spike`) and decisions recorded
  (`adr`).
- A story map for the PRD's journey (`user-story-mapping`) — if none exists,
  build it as the first activity of the session; the cut-line in Step 3 is
  drawn on it.

## Workflow

### Step 1 — Entry check (gate, not formality)

Confirm before anything else:

1. **Sign-Off 2 is recorded** — a dated record that stakeholders validated
   scope, sequencing, and outcomes. Note: Sign-Off 2 validates *what and in
   which order*, not solution details — so open design/architecture questions
   do not invalidate it, but open scope questions do.
2. **The PRD is normed** — it has been through forming/storming and the team
   shares one reading of it. A PRD with unresolved comment threads on its
   scope sections is not normed.

If either fails, stop and route back to `prd-development`. Running planning on
an unsigned PRD produces a plan that gets relitigated ticket by ticket — the
most expensive possible way to discover disagreement.

### Step 2 — Readiness gate: evidence, not vibes

Two verdicts, each backed by a named artifact. "The designer says it's fine"
and "the architecture is basically settled" are not evidence.

| Verdict | Standard | Evidence required |
|---|---|---|
| **Dev Ready Design** | Design Signal 90 — the design has been validated to the blueprint's 90% signal bar | The `design-signal` report exists, is dated, and covers the screens/flows in this increment's scope |
| **Dev Ready Architecture** | The technical approach is decided, spiked, and recorded | `tech-spec` current for this scope; every feasibility question either closed by an `eng-feasibility-spike` result or explicitly accepted as a risk; ACRs recorded via `adr` for the decisions the spec rests on |

Record each verdict in the plan as **READY / NOT READY** with a link to the
evidence.

**NOT READY is a scheduling fact, not a blocker-by-vibes.** Anything not ready
becomes a *named first-sequence item* — "reach Design Signal 90 for checkout
flow, owner X, by date Y" — and downstream tickets that depend on it are
sequenced behind it. What is never acceptable is hand-waving: declaring
"dev-ready" without the artifact, or starting dependent build work and hoping
design/architecture catches up.

### Step 3 — Draw the MVP cut-line

Walk the story map (`user-story-mapping`) with the PRD's success criteria in
hand:

1. For each backbone activity, walk down the tasks and mark the **smallest
   slice that tests the PRD's success criteria** — not the smallest thing that
   compiles, and not everything stakeholders would enjoy. The test: *if this
   slice ships and the success metrics don't move, have we learned the PRD's
   hypothesis is wrong?* If yes, the slice is right-sized.
2. Draw the line explicitly in the plan: **above the line = this increment's
   MVP**, committed.
3. **Everything below the line gets a named release** — "Release 2:
   \<slug\>", "Release 3: \<slug\>" — with the stories listed under each.
   A bucket called "later" or "backlog" is where validated scope goes to die;
   a named release keeps it visible, sequenced, and honest with the
   stakeholders who signed off on it.

If the cut-line debate turns into a scope debate ("do we even need activity
X?"), that is Sign-Off 2 material — Step 1's rule applies: route back, don't
relitigate here.

### Step 4 — Sequence by dependency and risk

Order the above-the-line work:

1. **Dependencies first** — draw the edges: readiness items from Step 2,
   technical prerequisites from the tech spec, data/contract dependencies
   between stories. Anything with an inbound edge waits for its source.
2. **Risky and irreversible items early** — schema migrations, external
   contracts, novel integrations, anything a spike flagged as uncertain. The
   sooner a risky item runs, the more increment is left to absorb what it
   teaches. Sequencing the easy wins first feels productive and discovers the
   hard problem in the final week.
3. **Mark what can parallelize** — independent tracks with no shared edges,
   explicitly labelled. For AI-agent execution this is what turns into
   concurrent work; for humans it's who can start without waiting.

The output is a numbered sequence with a one-line "why this position" for
every item that isn't obvious — the reason is what survives when the plan is
re-read in week three.

### Step 5 — Cut epics and tickets

Turn the sequenced slice into tracker-ready work:

1. **Epics** come from `epic-breakdown-advisor` output — one epic per
   coherent, independently-valuable chunk of the sequence. If an epic fails
   the INVEST pre-check there, split before ticketing, not after.
2. **Stories** follow `user-story` — Mike Cohn format with **Gherkin
   acceptance criteria**. Every ticket carries:
   - its acceptance criteria *in the ticket body* (not a link to a doc that
     will drift), and
   - a **link back to the PRD section** it implements — the traceability that
     lets anyone ask "why does this ticket exist" and get the signed-off
     answer.
3. **Create the tickets in the team's tracker** as part of this session — a
   plan whose tickets exist only in the plan document is a plan nobody
   executes.
4. **For AI-agent execution**, run `../ralph/` to convert the PRD into
   `prd.json` so the Ralph loop can pick up the committed scope directly.
   The ticket acceptance criteria and the prd.json stories must agree — same
   source, two formats.

A ticket without acceptance criteria is not a ticket; it is a conversation
scheduled for the worst possible time (mid-implementation).

### Step 6 — Mark the PRD Commitment-Ready

With scope cut, sequenced, and ticketed, update the PRD's status to
**Commitment-Ready** and record it in the plan:

- **Scope is frozen for this increment.** The above-the-line list in Step 3
  is the commitment.
- **Changes now go through explicit re-planning** — a new PI-planning pass (or
  a recorded amendment to this plan with the same rigor: what enters, what
  leaves to make room, who agreed). Mid-increment additions that skip this are
  scope creep wearing an urgent hat.
- Note in the PRD where the plan lives, and in the plan which PRD version was
  committed — the pair is the audit trail.

This is the moment the blueprint's PRD lane completes: formed, stormed,
normed, signed off, and now committed.

### Step 7 — Define the done-bar and book the exit gate

Before execution starts:

1. Run `../test-strategy/` for the increment — the unit/integration/E2E
   split, test-double policy, and the merge done-bar every ticket is held to.
   Doing this now means the first ticket is built against the bar, not
   retrofitted to it.
2. **Book the `../release-readiness/` review date** in the calendar now, tied
   to the increment's target ship date. A go/no-go review that gets scheduled
   "when we're close" gets scheduled after the decision has already been made.

### Step 8 — Write the plan

Save `docs/product/pi/<increment-slug>.md`:

```markdown
# PI Plan — <increment name> — <YYYY-MM-DD>

**PRD:** <link + version committed> · **Status: Commitment-Ready**
**Sign-Off 2:** <date, attendees> · **Release-readiness review booked:** <date>

## Readiness
| Verdict | READY / NOT READY | Evidence |
| Dev Ready Design | … | <design-signal report link> |
| Dev Ready Architecture | … | <tech-spec / spikes / ADR links> |
(NOT READY items appear as sequence items 1..n below)

## MVP scope
**Above the line (committed):** <stories/slices>
**Cut-line rationale:** <which success criteria this slice tests>
**Below the line:**
- Release 2 "<name>": <stories>
- Release 3 "<name>": <stories>

## Sequence
| # | Item | Depends on | Why this position | Parallel track |

## Epics & tickets
| Epic | Tickets (tracker links) | PRD section |

## Done-bar
<link to test-strategy output; merge bar in one line>
```

## Pitfalls

- **Relitigating signed-off scope in planning:** the session drifts from "how
  do we sequence this" to "should we build this" → Sign-Off 2 is silently
  voided and stakeholders learn their validation didn't hold → enforce Step
  1's rule: scope questions route back to `prd-development` and a re-sign;
  planning only sequences what was validated.
- **"Dev-ready" declared without the 90% design signal:** the design "feels
  close enough" so build starts → engineers improvise the missing 10%, which
  is always the hard 10%, and rework lands mid-increment → Step 2 requires the
  `design-signal` report as evidence; no report = NOT READY = first-sequence
  item.
- **Below-the-line work with no named release:** cut scope goes into a
  "later" bucket → "later" means never, and the stakeholders who signed off
  on that scope discover it evaporated → every below-the-line story sits
  under a named release in the plan.
- **Tickets without acceptance criteria:** tickets are cut fast as titles →
  every ambiguity is resolved by whoever (or whatever agent) implements it,
  unreviewed → Step 5: Gherkin criteria in the ticket body plus a PRD link,
  or the ticket doesn't exist yet.
- **Sequencing by ease instead of risk:** the comfortable items go first to
  "build momentum" → the risky item detonates in the final stretch with no
  runway to absorb it → Step 4 puts risky/irreversible items early,
  deliberately, with the reason written down.

## Next steps

- **Execution** — Engineering delivers the sequence: AI codes against the
  ticketed acceptance criteria (via `../ralph/` for autonomous loops), humans
  consult, review, and ship.
- `../test-strategy/` — if not completed in Step 7, do it before the first
  ticket starts; it is the merge bar for everything above the line.
- `../release-readiness/` — the booked go/no-go review at the end of the
  increment; bring this plan, it seeds the intake.
- `learn-iterate` — after ship, compare actuals against the PRD's success
  criteria; the learning feeds the next increment's Exploration/Discovery
  pass.
