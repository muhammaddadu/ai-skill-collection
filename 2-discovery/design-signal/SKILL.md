---
name: design-signal
description: "Declare design confidence at a 30/60/90% Design Signal checkpoint with the evidence that justifies it, so design risk closes in step with the PRD. Use when running a design checkpoint, assessing design readiness, or gating the move to PRD Storming/Norming/PI Planning. Do NOT use for building UI (cleanui) or writing the PRD (prd-development)."
type: component
domain: 2-discovery
---

# Design Signal (30/60/90 checkpoints)

## Purpose

Run a **Design Signal checkpoint**: declare how confident the team is in the design
direction — 30%, 60%, or 90% — and back the number with evidence, so design risk
closes *in step with* the PRD instead of after it. The Design lane runs
Discovery → **Signal 30%** → **Signal 60%** → **Signal 90%**, paced against PRD
Forming → Storming → Norming → PI Planning. Each checkpoint produces a short,
honest report that lets product, engineering leads, and stakeholders decide
go/hold for the next stage. Design's accountability here is **experience
confidence and usability risk closure** — the signal is the instrument that
makes both visible.

The percentages are **confidence, not completion**. A signal is earned by
evidence, never by calendar. If the evidence supports 30% and the roadmap says
60%, the signal is 30% — say so.

## Outputs

**Artifact:** Design Signal report — signal level, what's validated vs still open,
UX risks with owners, and a go/hold recommendation for the next stage
**Format:** markdown
**Location:** `docs/product/design-signals/<feature>-<30|60|90>.md` (one file per
checkpoint; earlier reports stay put as the audit trail)
**Audience:** product + engineering leads + stakeholders deciding whether the
feature advances to the next PRD stage

## Prerequisites

- A forming PRD for the feature (`prd-development`) — the signal paces against
  its Forming/Storming/Norming stages; without a PRD there is nothing to pace
- Personas and journeys where available (`proto-persona`,
  `customer-journey-map`) — they define whose experience the signal is about
- For 60%: access to real or proxy users for usability input (see Stage 2)

## Workflow

### Step 0 — Establish which checkpoint you are running

Ask (or infer from the PRD stage):

| PRD stage | Design Signal checkpoint | Column output |
|---|---|---|
| Forming → Storming | **30%** | Conceptual flows + named UX risks |
| Storming → Norming | **60%** | Testable UX + usability insights |
| Norming → PI Planning | **90%** | Dev Ready Design |

If a previous signal report exists for this feature, read it first — every
checkpoint after the first opens with "what changed since the last signal."

### Calibration: what each signal means (and does NOT mean)

Percentages are **confidence in the design direction**, not percent of screens
drawn. Use this table to calibrate before declaring anything:

| Signal | DOES mean | Does NOT mean |
|---|---|---|
| **30%** | The concept holds together for the primary journey; we know what could kill it | 30% of screens exist; visual design has started; risks are resolved |
| **60%** | The direction survived contact with users; major risks have closure plans | The UX is final; edge cases are handled; engineering can start |
| **90%** | Engineering can build without design guesses; leftover risk is explicitly accepted | Pixel-perfection; zero open questions; design's involvement ends |

### Stage 1 — 30% signal (concept)

**Gate definition:** conceptual flows exist for the **primary journey**; the top
UX risks are **named**; nothing is polished. This is the cheapest point to kill
or redirect a concept — polish here is waste.

**Evidence required:**
- Flow sketches for the primary journey (whiteboard photos, boxes-and-arrows,
  low-fi wireflows — fidelity deliberately low)
- A written UX risk list: each risk stated as what could make this design fail
  for the user, ranked, with an owner

**To run the checkpoint:**
1. Walk the conceptual flow end-to-end against the persona/journey. Note where
   the flow hand-waves ("then somehow they find X") — each hand-wave is a risk.
2. Name the top UX risks (aim for 3–7). Typical shapes: comprehension ("will
   users understand this model?"), findability, effort/friction, trust,
   platform fit.
3. Assign each risk an owner and a rough closure idea (interview, probe,
   prototype test) — closure *plans* come at 60%; at 30% it's enough that the
   risk is named and owned.
4. Declare the signal honestly (see "Declaring the signal" below).

**Exit criterion:** the team agrees the concept is **worth storming** — the flow
is coherent enough, and the risks scary-but-addressable enough, to invest PRD
Storming effort. If the team can't agree the primary journey even makes sense,
the signal is not 30% yet; it's still Discovery.

### Stage 2 — 60% signal (validated direction)

**Gate definition:** the UX is **testable** — a clickable prototype or concrete
mockups exist for the primary journey; **usability insights from real or proxy
users** are in hand; every major risk from the 30% list has a **closure plan**
(and ideally some are already closed).

**Evidence required:**
- The testable artifact itself (prototype link, mockup set)
- Usability findings: who was tested (real users, or proxies and why they're
  valid proxies), what tasks, what was observed — not opinions, observations
- Risk register updated: each 30% risk marked closed (with the evidence),
  or open with a concrete closure plan and owner

**To run the checkpoint:**
1. Confirm the artifact is genuinely testable: a user can attempt the primary
   journey without a designer narrating. Static "vision decks" don't count.
2. Get usability input cheaply — you do not need a lab. Route to
   `discovery-interview-prep` to plan sessions with real users, or `pol-probe`
   to define a disposable validation probe when users are hard to reach.
   Five users finding the same snag beats zero users and a confident team.
3. Reconcile findings against the risk list: which risks did the sessions
   close, which did they confirm, which *new* risks appeared?
4. For every still-open major risk, write the closure plan: what evidence will
   close it, by whom, by when (before 90%).
5. Declare the signal honestly.

**Exit criterion:** the design direction **survives contact with users** — the
observed behavior supports the concept (even if details need rework). If users
consistently stumbled on the core model, that is a 30%-grade finding: the
direction did not validate, and the honest move is to re-storm, not to advance.

### Stage 3 — 90% signal (dev-ready)

**Gate definition:** **Dev Ready Design.** Edge cases, states, and platform
rules are resolved; handoff is complete; whatever risk remains is **explicitly
accepted** by name, not silently carried. This is the design input to
`pi-planning`'s Dev Ready Design check.

**Evidence required:**
- State coverage: **empty, error, and loading** states specified for every
  screen in scope — plus permission-denied, offline, and long-content where
  relevant
- Edge cases enumerated and answered (boundary inputs, concurrent edits,
  first-run vs returning user — whatever the feature exposes)
- Platform rules resolved: responsive behavior, accessibility requirements,
  platform conventions (iOS/Android/web) decided, not "TBD"
- Handoff artifacts engineering will actually build from: final flows, specs or
  design-system references, copy, interaction notes
- Residual-risk acceptance: each remaining open risk listed with who accepted
  it and why it's tolerable to build anyway

**To run the checkpoint:**
1. Sweep every screen against the state checklist (empty/error/loading at
   minimum). An unspecified error state is an automatic hold — it is the most
   common "90% that wasn't."
2. Have an engineer (not a designer) walk the handoff and list every question
   they'd need to ask before building. Each question is a design guess you're
   about to delegate to whoever writes the code. Zero-question walkthrough =
   handoff-complete.
3. Close or formally accept every remaining risk. "Accepted" means a named
   person agreed, in the report, that the team builds despite it.
4. Declare the signal honestly.

**Exit criterion:** **engineering can build without design guesses.** The
feature can enter `pi-planning` with design as a known quantity, and
implementation can proceed (via `cleanui` for UI build) without blocking on
design decisions.

### Declaring the signal (every checkpoint)

Each report follows the same skeleton — keep it to 1–2 pages:

```markdown
# Design Signal: <feature> — <30|60|90>%

**Date:** … · **Declared by:** … · **PRD stage:** Forming|Storming|Norming

## What changed since the last signal
(First checkpoint: summarize the discovery inputs instead.)

## Evidence
| Claim | Evidence |
|---|---|
| e.g. "Primary journey is comprehensible" | 4/5 usability sessions completed task unaided (notes link) |

## UX risks
| Risk | Status (open/closed/accepted) | Owner | Closure plan / evidence |
|---|---|---|---|

## Signal declaration
Declared signal: **NN%** — <one honest sentence on why the evidence supports it>

## Recommendation
**Go / Hold** for <next stage>, because …
```

**Honest-by-default rule:** the declared signal is set by the *evidence table*,
not the checkpoint you scheduled. A 60% checkpoint whose evidence rows are
"we're pretty sure" and "design reviewed internally" is a **30% report with a
60% title — retitle it**. Declaring the lower number is not failure; it's the
mechanism that keeps the design lane synchronized with reality. A "Hold"
recommendation with a clear evidence gap is a *successful* checkpoint.

## Pitfalls

- **Signal inflation:** the declared percent tracks the calendar ("PI Planning
  is next sprint, so we're at 90%") instead of the evidence → engineering
  builds on guesses and design risk resurfaces mid-delivery as rework → the
  signal number may only come from the evidence table; if the date and the
  evidence disagree, report the evidence and let the go/hold decision carry
  the schedule conversation.
- **Polishing at 30%:** high-fidelity visuals appear at the concept gate →
  stakeholders react to the polish instead of the concept, sunk cost makes the
  concept unkillable, and the checkpoint's cheap-kill purpose is lost → cap
  30% artifacts at sketch/wireflow fidelity on purpose; if someone asks "why
  does it look rough," that's the checkpoint working.
- **"We know the user" usability skips:** the 60% gate passes on internal
  review because the team feels expert in the domain → the direction first
  meets a real user in production, where course-correction is most expensive →
  60% *requires* observed user behavior; when real users are hard to reach,
  proxy users via `discovery-interview-prep` or a cheap `pol-probe` still beat
  zero sessions.
- **90% with unresolved error states:** the happy path is specified beautifully
  but empty/error/loading are "engineering can figure those out" → each gap
  becomes an on-the-spot design decision made in code, inconsistently → the
  state sweep (empty/error/loading per screen) is a hard precondition; any
  unspecified state means Hold, however complete the rest looks.
- **Signal as a one-way ratchet:** a feature declared 60% is treated as never
  able to go back → invalidating evidence gets suppressed to avoid "losing"
  the signal → signals can and should regress when evidence turns; a
  documented drop from 60% to 30% is risk closure doing its job.

## Next steps

- `pi-planning` — the 90% report is the design input to the Dev Ready Design
  check before delivery commits
- `cleanui` — implement the validated, dev-ready UI
- `prd-development` — feed each checkpoint's go/hold and open risks back into
  the PRD stage decision (Storming → Norming → PI Planning)
