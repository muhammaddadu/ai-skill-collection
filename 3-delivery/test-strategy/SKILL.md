---
name: test-strategy
description: "Turn acceptance criteria into a right-sized test plan: unit vs integration vs E2E split, test-double policy, and the merge/release done-bar. Use when planning tests for a feature or epic, deciding the test pyramid, or making coverage decisions ('how should we test this'). Do NOT use for writing test cases in code or reviewing an existing diff."
type: component
domain: 3-delivery
---

# Test strategy

## Purpose

Turn a feature's acceptance criteria into a concrete, right-sized test plan
*before* implementation starts: which criteria get unit vs integration vs E2E
coverage, which test doubles stand in for which dependencies, how deep to test
each area given its risk, and exactly which checks gate merge versus release.
The output is a plan engineers implement and reviewers hold the change to —
"done" becomes provable, not asserted on intent. This skill decides the
strategy; it does not write the tests.

## Outputs

**Artifact:** Test plan for one feature/epic — a criteria→test mapping table,
double policy, risk matrix, non-functional in/out decisions, and the done-bar.
**Format:** Markdown.
**Location:** Standalone `docs/specs/<feature>-test-plan.md` in the target
repo, **or** embedded as the "Test approach" section of the feature's
tech-spec when one exists (prefer embedding — one document per feature).
**Audience:** Engineers implementing the feature, and reviewers deciding
whether it is done.

## Prerequisites

- Testable acceptance criteria for the feature — from `prd-development`,
  `user-story` (Gherkin criteria), or the requirements section of a
  `tech-spec`. Without criteria there is nothing to plan against; write
  them first.
- The target repo's `AGENTS.md` / contributor docs (see `agent-docs`), if
  they exist — they define where tests live, which runner is used, and any
  house testing rules. **Repo conventions override this skill's defaults.**

## Workflow

### 1. Extract testable acceptance criteria

List every acceptance criterion for the feature in a table. For each one:

- **Restate it as an assertion** — a sentence with a subject, an action, and
  an observable outcome ("importing the same file twice creates no duplicate
  contacts"), not a quality ("import is robust").
- **Name at least one test** that would prove it. The name should read as the
  assertion (`rejects_duplicate_rows_by_email`), because a criterion without
  a named test is a criterion nobody will notice regressing.
- **Flag untestable criteria back to the PRD.** "Fast", "intuitive",
  "reliable" are vibes. Push back with a proposed quantification ("p95 import
  under 30s for 10k rows") rather than silently dropping them — an
  unmeasurable criterion is a requirements bug, not a testing gap.

Every criterion ends this step either mapped to a named test or explicitly
returned to the requirements owner. No third state.

### 2. Classify each test by pyramid layer

Assign each named test a layer using these heuristics:

| Signal in the criterion | Layer | Why |
|---|---|---|
| A decision, calculation, validation, state transition, parse/format rule | **Unit** (colocated with the module) | Pure logic; fastest, most precise failure signal |
| Behavior at a component boundary — an adapter, a port, a repository, an API contract | **Integration / contract** | Proves the translation, not the logic behind it |
| A user-visible journey that crosses the whole system | **E2E** | Proves the wiring; reserve for critical paths only |

Two rules make the pyramid come out right-side up:

- **Push logic into pure functions to make it unit-testable.** If a criterion
  looks like it needs an integration test just to reach the logic (the
  decision is buried inside an HTTP handler, a DB call, or a UI event
  handler), that is **design feedback, not test placement**: extract the
  decision into a pure function with a colocated unit test, and leave a thin
  I/O shell that needs only a smoke-level check. The test plan should say so
  explicitly ("extract `resolveDuplicatePolicy()` so criteria 2–3 are unit
  tests").
- **E2E is for journeys, not criteria.** Most criteria are proven at unit or
  contract level; E2E exists to prove that the proven parts are actually
  wired together. Plan one or two golden-path E2E tests plus any invariant
  the system must never regress (e.g. "no write happens without approval") —
  not one E2E per criterion.

### 3. Set the test-double policy

Decide, per external dependency, what stands in for it — and write it down so
every test in the feature uses the same double:

| Dependency | Double | Rationale |
|---|---|---|
| A port/interface **you own** (repo store, queue, mailer, payment port) | **In-memory fake** — a real, if simple, implementation | Fakes encode behavior, so they survive refactors; mocks encode call sequences, so they break on every rename and prove only that the code calls what it calls |
| A **third-party API/SDK you don't own** | **Wrap it in a thin adapter you own, then fake the adapter** | Never mock what you don't own: your mock encodes your guess about their behavior, and both can be wrong together |
| The **real thing** (real DB, real filesystem, real service) | Used in **one E2E/smoke path only** | Fidelity where it matters — proving the wiring — without paying its cost in every test |

Preferences, in order: real pure function > in-memory fake > real dependency
in one E2E path > mock. Mocks are a last resort for verifying an interaction
that *is* the requirement (e.g. "exactly one notification is sent"), not a
default. If the plan calls for mocking more than a couple of collaborators
per test, revisit step 2 — the design is fighting you.

If the repo already ships in-memory doubles for its ports, plan a
**conformance suite**: the same contract tests run against both the fake and
the real adapter, so the fake is guaranteed to stay honest.

### 4. Apply risk-based depth

Uniform depth is waste in one place and negligence in another. Score each
area of the feature on **failure impact** (what breaks for users/business if
this is wrong) × **change likelihood** (how often this code will be touched
or how novel it is), and let the product set the depth:

| | Low likelihood | High likelihood |
|---|---|---|
| **High impact** | Happy path + the known failure modes | Exhaustive: edge cases, property-based/table tests, unhappy paths, concurrency |
| **Low impact** | Smoke-level or none — say so explicitly | Happy path + the most likely error |

Record the scores in the plan (a one-line rationale per area is enough).
Unhappy paths concentrate in the high-impact cells: partial failures,
retries, malformed input at boundaries, permission-denied. These are where
production incidents live and where plans habitually go thin.

### 5. Decide non-functional coverage — explicitly IN or OUT

For each category below, the plan must state **IN** (with the test or check
that covers it) or **OUT** (with the reason). Silence is the failure mode —
an undecided category is an untested one:

- **Performance / load** — IN if a criterion carries a number (latency,
  throughput, volume); OUT with reason otherwise ("no SLA on this path").
- **Migration & rollback** — IN whenever the change alters schema or stored
  data: forward migration on production-shaped data, plus a rollback or
  roll-forward story. OUT only if no persistent state changes.
- **Concurrency & idempotency** — IN for anything retried, delivered
  at-least-once, or reachable by two actors at once ("same event delivered
  twice creates one record"). These bugs never surface in serial unit tests.
- **Auth boundaries** — IN for any new endpoint or permission-gated action:
  test the *denied* case per role, not just the allowed one. Absence of a
  403 test is how privilege escalations ship.

### 6. Define the done-bar

Split the plan's checks into two gates and name them in the plan:

- **Merge gate** (every PR, fast, deterministic): typecheck, lint, unit
  tests, integration/contract tests against fakes. Target: minutes, no
  flakes, no external services.
- **Release gate** (before ship, may be slower): E2E golden paths against
  real dependencies, smoke tests, migration rehearsal, any performance check
  from step 5.

A criterion proven only at the release gate is a criterion that can rot for
days between releases — prefer proving at merge and *confirming wiring* at
release. Anything in the merge gate must be deterministic: a check that flakes
gets skipped, and a skipped check gates nothing — fix or demote it. This split
feeds directly into `../release-readiness`, which owns the ship/no-ship
decision.

### Plan skeleton

The finished plan is short. Emit exactly these sections (the worked example
below shows them filled in):

```markdown
## Test approach: <feature>

### Criteria → tests
| # | Criterion (as assertion) | Layer | Named test | Depth rationale |
|---|---|---|---|---|

Returned to PRD as untestable: <criterion> — proposed restatement: <...>

### Test doubles
- <dependency>: <fake | wrapped adapter + fake | real, E2E only> — <why>

### Non-functional coverage
- Performance: IN/OUT — <reason / gating check>
- Migration & rollback: IN/OUT — <reason>
- Concurrency & idempotency: IN/OUT — <reason>
- Auth boundaries: IN/OUT — <reason>

### Done-bar
- Merge gate: <checks>
- Release gate: <checks>
```

If a section would be empty, keep the heading and say why — an absent section
reads as "not considered", an explicit OUT reads as a decision.

## Worked example

Feature: **bulk CSV import of contacts** (up to 10k rows, dedupe by email,
partial-failure report).

**Criteria → plan:**

| # | Criterion (as assertion) | Layer | Named test | Depth rationale |
|---|---|---|---|---|
| 1 | Valid rows create contacts with mapped fields | Unit | `maps_csv_row_to_contact` | High impact, high churn → exhaustive: table test over field variants |
| 2 | Rows duplicating an existing email are skipped and reported | Unit + contract | `skips_duplicate_by_email`; `import_reports_skipped_rows` | Extract `classifyRow(row, existingEmails)` as a pure function (design feedback) |
| 3 | A malformed row fails that row, not the import | Unit | `malformed_row_isolated` | High impact (data loss) → cover the known malformations |
| 4 | Re-uploading the same file creates no duplicates | Contract | `import_is_idempotent_per_file_hash` | Concurrency/idempotency: IN (step 5) — retried uploads are certain |
| 5 | User sees a summary: created / skipped / failed | E2E | `golden_path_import_summary` | One golden path proves UI→API→store wiring |
| 6 | "Import feels fast" | — | *returned to PRD* | Not an assertion; proposed: "p95 < 30s for 10k rows" → then a release-gate perf check |

**Doubles:** `ContactStore` port → in-memory fake with conformance suite
shared with the Postgres adapter; the third-party email-validation API →
wrapped in an owned `EmailVerifier` adapter, faked in tests; real Postgres
appears only in test #5.

**Non-functional:** migration IN (new `import_batches` table — forward + rollback
test); auth IN (`importer` role required; test the 403); performance OUT until
criterion 6 is quantified; concurrency IN via test #4.

**Done-bar:** merge gate = typecheck + lint + tests 1–4 on fakes; release
gate = test 5 + migration rehearsal.

That table — plus the doubles, non-functional, and done-bar paragraphs — *is*
the deliverable. For a small feature it fits in half a page of the tech-spec.

## Boundaries

- **This skill plans; it does not write or review test code.** Implementing
  the named tests is the coding agent's job; judging test code in a diff is
  `/code-review`'s job.
- **Repo conventions win.** Where tests live (colocated vs `tests/`), which
  runner and assertion style to use, and any house invariant suite come from
  the target repo's `AGENTS.md` / contributor docs (per `agent-docs`
  conventions). This skill's defaults (colocated unit tests, in-memory
  fakes) apply only where the repo is silent.
- **Ship/no-ship is downstream.** This skill defines which checks exist and
  which gate they belong to; `../release-readiness` decides whether the
  release gate is actually green enough to ship.

## Pitfalls

- **Inverted cone:** most criteria proven only via E2E → suite is slow and
  flaky, failures point nowhere, engineers stop trusting red → reclassify
  per step 2; extract pure functions until each criterion is provable at the
  lowest layer that can observe it, keep E2E for one or two journeys.
- **Mock-everything suites:** every collaborator mocked per test → tests
  assert call sequences, pass while the system is broken, and shatter on
  refactor → switch owned dependencies to in-memory fakes (step 3); if a
  test still needs three mocks, the unit under test is too big.
- **Coverage-percentage worship:** a % target becomes the goal → trivial
  assertions farm lines while unhappy paths stay bare → the bar is
  "every acceptance criterion has a named passing test" (step 1), with depth
  set by risk (step 4); use coverage reports to find *unplanned* gaps, never
  as the done-bar.
- **Vibes criteria:** criteria like "fast", "seamless", "robust" get waved
  through → nothing fails when the promise is broken → return them to the
  requirements owner with a proposed measurable restatement before planning
  against them (step 1).
- **Testing the framework:** tests assert that the router routes, the ORM
  saves, or the validator library validates → effort burns on code you don't
  own and can't fix → test *your* configuration and logic at the boundary
  (contract tests on your adapter), and trust the framework's own suite for
  the rest.

## Next steps

- `../release-readiness` — consumes this plan's done-bar: the release-gate
  checks become its ship/no-ship checklist.
