---
name: e2e-automation
description: "Build and maintain a durable automated E2E suite — Playwright for web, Maestro for Expo/React Native: stable selectors, owned test data, CI gating, and a flake policy with teeth. Use when automating the E2E journeys a test plan defines or fixing a slow/flaky suite. Do NOT use for deciding what to test (test-strategy) or unit tests (tdd)."
type: component
domain: 3-delivery
---

# E2E automation

## Purpose

Build and maintain a durable automated end-to-end suite — one that stays green
for the right reasons: stable user-visible selectors, test data every test owns
outright, deliberate CI integration, and a flake policy with teeth. The
journeys come from `../test-strategy/` (it decides *what* gets E2E coverage);
this skill is *how* to automate those journeys and keep the suite trustworthy
for years, not weeks. A suite nobody trusts is worse than no suite — red gets
ignored, green gets assumed, and the one real regression sails through.

## Outputs

**Artifact:** The E2E suite itself in the target repo (`e2e/` by default, or
the repo's own convention per its `AGENTS.md`), plus a suite `README.md`
documenting four things:
1. **Covered journeys** — each traced back to the E2E slice of the feature's
   test plan from `../test-strategy/`.
2. **Data strategy** — how tests create/destroy their data and which
   environment they run against.
3. **How to run** — locally and in CI, including the smoke vs full split.
4. **Flake policy** — quarantine rules, TTL, and the current flake budget.

**Format:** Test code (Playwright TypeScript or Maestro YAML) + markdown README.
**Location:** Target repo, alongside the app it tests.
**Audience:** Engineers extending the suite; CI; reviewers reading a red gate.

## Prerequisites

- The E2E slice of a test plan from `../test-strategy/` — the named
  critical-journey tests. Without it you are guessing what deserves E2E.
- The app runnable in a **controllable environment** — you can boot it, point
  it at a database you own, and reach it from the test runner. If you can't,
  fix that first; automation against an environment you don't control is
  flake by construction.

## Workflow

### 1. Scope from the plan — and push back if it's long

Take the E2E tests named in the feature's test plan (`../test-strategy/`
step 2: journeys plus never-regress invariants). E2E covers **critical user
journeys only** — sign-up, checkout, the golden path of the feature, the
invariant the business cannot survive breaking.

If the list is long (more than a handful of journeys per feature, or criteria
that read like unit tests), **that is a test-strategy problem — push back
before automating**. Every E2E test you write is a permanent tax on every
merge; don't pay it for coverage a unit test provides better. Reclassify with
the plan's owner, then automate what survives.

### 2. Choose the tool and route to its reference

| Target | Tool | Reference |
|---|---|---|
| Web app | **Playwright** | read `references/playwright.md` |
| Expo / React Native app | **Maestro** — flows in plain YAML, runs against real builds including EAS builds | read `references/maestro.md` |

**Detox** is the code-first RN alternative: gray-box, synchronized with the
app's internals, JavaScript API. Prefer it over Maestro when the team wants
E2E in the same language/toolchain as the app, needs tight synchronization
with app internals (custom idling resources), or already has a Detox suite.
Default to Maestro for Expo projects: no native test code to maintain, flows
are readable by non-engineers, and it works on prebuilt binaries.

Repo conventions override these defaults — check `AGENTS.md` first (per
`agent-docs`).

### 3. Suite architecture

- **Page-object / screen-object layer.** Every selector and every low-level
  interaction lives in one object per page/screen. The payoff is a change
  contract: **one selector change = one file changed**. Tests read as
  journeys (`checkoutPage.payWith(card)`), not as DOM/UI plumbing.
- **User-visible selectors first.** Prefer what the user perceives: roles and
  accessible labels, then explicit test IDs (`data-testid` on web, `testID`
  on RN). **Never** brittle structural CSS/XPath paths (`div:nth-child(3) >
  .btn`) — they encode today's layout and break on tomorrow's refactor.
  Adding a test ID to the app is a normal, reviewable app change; do it
  rather than writing a clever selector.
- **Every test independent and order-free.** Any test can run alone, first,
  last, or in parallel with any other. No test reads state a previous test
  wrote. If two tests must share a step, that step belongs in a fixture/flow
  helper both call — not in an ordering dependency.

### 4. Test data lifecycle

- **Every test creates and destroys its own data.** Setup makes the user, the
  account, the records it needs; teardown removes them (or the environment is
  ephemeral and thrown away whole).
- **Seed via API, not UI.** The UI path is what the test *proves*; everything
  the test merely *needs* is arranged through APIs, fixtures, or direct
  seeding. Clicking through sign-up to test checkout makes every checkout
  test hostage to the sign-up UI.
- **No shared magic accounts.** `test-user-1@example.com` shared across tests
  is a mutex you haven't written: parallel runs corrupt each other and
  Monday's failures come from Friday's leftovers. Generate unique
  identities per test run.
- **Decide the environment question explicitly and write it down** in the
  suite README. Preference order: **ephemeral environment** (built per run —
  strongest isolation) > **staging** (shared — acceptable with owned data and
  unique identities) > **prod-dogfood** (smoke-only, read-mostly, feature-
  flagged). "Whatever staging happens to contain" is not a data strategy.

### 5. CI integration

- **Two gates, matching the done-bar split from `../test-strategy/` step 6:**
  a **smoke subset** (the 3–10 fastest, highest-value journeys, tagged
  `@smoke`) runs on the **merge gate**; the **full suite** runs on the
  **release gate** and on a schedule (nightly) so drift surfaces between
  releases.
- **Parallel sharding.** Split the suite across CI workers so wall-clock time
  stays flat as the suite grows. A gate that takes an hour is a gate people
  bypass.
- **Artifacts on failure — non-negotiable.** Trace, video, screenshots, and
  logs uploaded for every failed test. **A failure nobody can debug is a
  failure of the suite**, and it will be handled by re-running until green —
  which is how flake culture starts.

### 6. Flake policy with teeth

A flaky test — one that fails without a product change — is the most
expensive artifact in CI: it trains everyone to ignore red.

- **Quarantine same day.** The moment a test is identified as flaky it is
  tagged (`@quarantine` / skipped-with-reason), **removed from the gate**,
  and a ticket is opened **with a named owner**. It does not stay in the gate
  "because it usually passes".
- **Quarantine has a TTL.** The ticket carries a date (one or two weeks).
  By that date the test is **fixed or deleted** — quarantine is a repair
  queue, not a retirement home. A permanently quarantined test is coverage
  you're lying to yourself about.
- **Retries are a diagnostic tool, never a permanent setting.** A retry that
  turns red to green tells you the test is flaky — that's signal for the
  quarantine process, not a fix. A suite that only passes with retries is
  masking real races, some of which are product bugs your users will find.
- **Track the flake rate** (flaky failures / total runs) per week. If it's
  above **2–3%, the suite is lying to you** — stop adding tests and pay down
  flake debt first.

### 7. Maintenance contract

E2E code is production code: it is **reviewed** like app code (selector
quality, data ownership, independence), **refactored** when page objects
drift from the UI, and **deleted when the journey dies** — a test for a
removed feature is pure cost. Put the suite in code ownership like any other
module; a suite owned by nobody rots until someone deletes it in anger
(see Pitfalls).

## Pitfalls

- **E2E-as-unit-test:** hundreds of tiny E2Es each proving one field
  validation → hour-long gates, failures that point nowhere → push those
  cases down the pyramid per `../test-strategy/` step 2; keep E2E for
  journeys and wiring.
- **sleep()-driven waits:** fixed `sleep(3000)` / `wait: 5000` sprinkled
  until it passes locally → flaky in CI (slower) and slow everywhere (waits
  are worst-case) → use the framework's synchronized waits: web-first
  assertions in Playwright, `extendedWaitUntil` / `waitForAnimationToEnd` in
  Maestro. See each reference for specifics.
- **Shared test accounts:** one login reused everywhere → parallel runs
  corrupt each other's state; failures reproduce only "sometimes" → unique
  per-test identities, API-seeded (step 4).
- **Permanent retries:** `retries: 2` set globally and forgotten → real races
  (including product bugs) pass on attempt two forever → retries only as
  temporary diagnostics; the flake policy (step 6) owns the fix-or-delete.
- **Suite ownership by nobody:** suite added in a sprint, no owner after →
  selectors rot, quarantine list grows, gate gets disabled "temporarily",
  suite deleted in anger a year later → maintenance contract (step 7): code
  ownership, review, and the flake budget make neglect visible early.
- **Testing through the UI what an API call can arrange:** each test clicks
  through login + navigation before its actual subject → every test is
  hostage to every screen it crosses; minutes wasted per test → seed state
  via API/fixtures/deep links; drive the UI only for the journey under test
  (step 4; both references show the mechanics).

## Next steps

- `../release-readiness/` — the full suite's green run is release-gate
  evidence; this suite's results feed its ship/no-ship checklist.
- `../progressive-delivery/` — the smoke subset re-validates each ramp step
  of a progressive rollout.
