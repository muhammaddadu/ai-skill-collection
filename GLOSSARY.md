# Glossary

One term, one meaning, used identically across every skill in this repo. When
writing or editing a skill, use these words — don't invent synonyms.

## Skill mechanics

- **Skill** — a directory with a `SKILL.md` playbook; installed into a tool's
  flat skills root by `install.sh`.
- **Component** — a skill that produces an artifact directly from a request.
- **Interactive** — a skill run as a facilitated multi-turn session; delegates
  pacing to `workshop-facilitation` (one-question turns, progress labels).
- **Advisor** — a skill that helps choose between options and outputs a
  recommendation, not an artifact.
- **Workflow** — a skill that orchestrates other skills across phases.
- **Reference file** — depth stored in a skill's `references/`, loaded only
  when the SKILL.md routing line calls for it (progressive disclosure).
- **Name reference** — how skills cite skills outside their own directory: the
  bare skill name in backticks (skills install flat, so names resolve in the
  skills root); `../<skill>/` paths are only for same-directory siblings.
- **Trigger** — the `description` frontmatter; the only always-on signal the
  model uses to pick a skill. Triggers within a domain must be mutually
  exclusive, using "Do NOT use for …" pointers.

## Lifecycle artifacts (each owned by exactly one skill)

- **Problem statement** — user-centered framing of who is blocked and why
  (`problem-statement`).
- **PRD** — product requirements document: problem, users, solution, success
  criteria (`prd-development`).
- **Epic** — a large initiative, framed as a testable hypothesis
  (`epic-hypothesis`); split into stories via `epic-breakdown-advisor`.
- **Story** — smallest development-ready unit with acceptance criteria
  (`user-story`); acceptance criteria are assertions, not vibes.
- **Tech spec** — engineering design doc / RFC turning a PRD into an
  implementable design (`tech-spec`).
- **ADR** — architecture decision record; append-only, superseded never
  rewritten (`adr`).
- **Contract** — an API's agreed shape: REST endpoints, GraphQL schema, or
  event/message schema (`api-design`).
- **Test plan** — the unit/integration/E2E split, double policy, and done-bar
  for a feature (`test-strategy`).
- **Done-bar** — which checks gate merge vs gate release (`test-strategy`,
  consumed by `release-readiness`).
- **Readiness report** — scored go/no-go evidence before shipping
  (`release-readiness`).
- **Postmortem** — blameless incident write-up with contributing factors and
  owned action items (`incident-postmortem`).
- **Product Brief** — the intake artifact that earns Sign-Off 1: intent,
  constraints, success criteria, priority (`product-brief`).
- **Design Signal** — declared design confidence at 30/60/90% with evidence;
  confidence, not completion (`design-signal`).
- **Spike report** — the evidenced answer to one feasibility question from a
  time-boxed investigation; its POC is disposable (`eng-feasibility-spike`).
- **PI plan** — the committed increment: MVP cut-line, sequence, epics/tickets;
  marks the PRD **Commitment-Ready** (`pi-planning`).
- **Iteration review** — post-release scorecard against success criteria with
  persevere/iterate/expand/kill decisions; produces PRD-Updated (`learn-iterate`).
- **Feature flag / TTL** — a toggle with an owner and a removal date set at
  creation; a flag past its TTL is a defect (`progressive-delivery`).
- **Ramp** — staged percentage rollout with per-step abort criteria and soak
  time; rollback is a config flip, not a deploy (`progressive-delivery`).
- **Expand-and-contract** — parallel-change data migration so old and new
  paths coexist until 100% + soak (`progressive-delivery`).
- **Threat model / trust boundary** — the design-time "what could go wrong":
  STRIDE per boundary where trust level changes; mitigations land in the spec
  or an ADR (`threat-modeling`).
- **SLI / SLO / error budget** — user-centric health metric, its internal
  target, and the allowed failure (1 − SLO); budget exhausted = reliability
  work first (`slo-design`).
- **Burn-rate alert** — page on SLO budget burning fast, not on causes like
  CPU; every page has a runbook (`slo-design`).
- **Flake quarantine** — a flaky E2E test leaves the gate the same day, with
  an owner and a fix-or-delete TTL (`e2e-automation`).
- **Sign-Off 1 / Sign-Off 2** — the blueprint's human gates: brief approved to
  enter Discovery; scope/sequencing/outcomes validated to enter Delivery
  (see BLUEPRINT.md).

## Review & scoring (ads-pack conventions, reused by api-design and release-readiness)

- **Check** — one ID'd, testable review item (e.g. `A20`, `R17`).
- **Category weight** — a check group's share of the 0–100 score.
- **Grade** — A ≥90, B 75–89, C 60–74, D 40–59, F <40.
- **Hard gate** — a check whose failure blocks the outcome regardless of
  score (auto no-go / grade cap).
- **Quick win** — severity Critical/High AND fix time < 15 min; sorted by
  impact. The "do this first" list.
- **Evidence** — the named proof a check passed; no evidence = FAIL.

## Process terms

- **Blameless** — postmortem stance: people acted reasonably on what they
  knew; factors name roles and systems, never people.
- **Contributing factors** — the several conditions that made an incident
  possible; used instead of a single "root cause".
- **Detection gap / mitigation gap** — incident start → known / known → fixed.
- **Rollout** — how a change reaches users (flagged, percentage, gradual);
  chosen deliberately in the tech spec and verified by release-readiness.
- **One-question turns** — the `workshop-facilitation` pacing rule: ask one
  thing, wait, then proceed with a progress label (e.g. `Context Q2/8`).
