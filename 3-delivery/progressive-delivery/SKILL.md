---
name: progressive-delivery
description: "Ship dark behind a feature flag, test in production, ramp by percentage with abort criteria, then delete the flag — build fast, break things safely. Use when planning a flag-based rollout, canary ramp, kill switch, or expand-and-contract migration. Do NOT use for the go/no-go review (release-readiness) or the test plan (test-strategy)."
type: component
domain: 3-delivery
---

# Progressive Delivery

## Purpose

The team motto made operational: **"Build fast, break things safely."** This
skill standardizes the full lifecycle of shipping a change behind a feature
flag — deploy it dark, test it in production on a zero-exposure cohort, ramp
it by percentage on a deliberate schedule with per-step abort criteria, keep
the data layer reversible via expand-and-contract, and then do the step
everyone skips: delete the old path and the flag so the new thing becomes THE
thing. Deploy and release become independent events; rollback becomes a config
change, not a deploy. `../release-readiness/` *verifies* that a rollout plan
exists before ship — this skill is *how you write that plan* and run it.

## Outputs

**Artifact 1:** Rollout plan — flag definition (name, type, owner, TTL),
cohort plan, ramp schedule with abort criteria and soak time per step,
kill-switch procedure, cleanup checklist with a date
**Format:** markdown
**Location:** `docs/specs/rollouts/<feature>.md` in the target repo
**Artifact 2:** Flag registry entry (same fields as the flag definition, plus
a link to the rollout plan) — in whatever the repo/org uses as the registry
(a `flags.md`, a config file, or the flag vendor's dashboard)
**Audience:** the delivering team, the on-call rotation, and the reviewer
running `../release-readiness/`

## Prerequisites

- A committed increment from `../pi-planning/` — you know what the feature is
  and where its cut-line sits.
- A done-bar from `../test-strategy/` — with the explicit note that **both
  paths (old and new) stay covered by tests for as long as both exist**.
- `../release-readiness/` passed for the **dark deploy** (Step 1 below ships
  real code to prod; it deserves the same review as any deploy, even OFF).
- A flag mechanism that can change state **without a deploy** (vendor SaaS,
  homegrown config service, or a fast-propagating config file). If flipping a
  flag requires a release, you have branches with extra steps, not flags.

## Workflow

### Step 1 — Flag it (build fast)

Put the new code path behind a feature toggle, **default OFF**, and deploy it
to production dark. Deploy ≠ release: the code being on the servers and the
code running for users are now two separate decisions.

**Pick the flag type first** — the type determines the lifetime, and mixing
them up is how flag debt starts:

| Type | Purpose | Lifetime | Prefix |
|------|---------|----------|--------|
| **Release** | Decouple deploy from release of one feature | Days–weeks; **deleted** after 100% + soak | `rel_` |
| **Ops kill switch** | Degrade gracefully; disable a risky dependency under load | Long-lived by design; reviewed periodically | `ops_` |
| **Experiment** | A/B measurement of a hypothesis | Duration of the experiment, then deleted | `exp_` |
| **Permission** | Entitlement / plan / role gating | Permanent product config, not a rollout tool | `perm_` |

This skill's lifecycle governs **release flags** (and the ramp mechanics apply
to experiments). If what you're building is really a permission or an ops
switch, name it that from day one — see the "flag as permanent config" pitfall.

**Naming:** `<type>_<area>_<feature>`, e.g. `rel_checkout_payment_v2`. The
name should tell a stranger what flips and roughly when it can die.

**Register the flag at creation** — the registry entry is part of the flag's
definition, not paperwork after the fact:

```markdown
| name | type | owner | default | created | removal date (TTL) | rollout plan |
| rel_checkout_payment_v2 | release | A. Rivera | OFF | 2026-07-06 | 2026-08-20 | docs/specs/rollouts/checkout-v2.md |
```

The TTL is a promise: past that date, the flag is a **defect** (see Hard
rules). Pick a realistic date — ramp length + soak + cleanup buffer — and
treat moving it like moving a deadline: explicitly, with a reason.

Write the rollout plan (`docs/specs/rollouts/<feature>.md`) now, before any
user sees the feature. It contains everything below: cohorts, ramp table,
kill-switch procedure, cleanup checklist with its date.

### Step 2 — Test in production (break things safely)

Enable the flag for a **zero-customer-exposure cohort** first: internal
users / employees / a dogfood group. They get real traffic, real data, real
dependencies — everything staging can't fake — while no customer can be hurt.

- Define the cohort by a stable attribute (employee email domain, allowlisted
  account IDs), not by ad-hoc toggling.
- Keep the `../test-strategy/` done-bar honest: while both paths exist, CI
  runs the suite against **both** flag states (or at minimum: full suite on
  the default, targeted suite on the new path). A green build that only
  exercised OFF tells you nothing about what you're about to ramp.
- Exit criterion for this step: the new path has served the dogfood cohort for
  an agreed period with metrics at parity — written in the rollout plan, not
  decided in the moment.

### Step 3 — Percentage ramp

Ramp on a **deliberate schedule**, e.g. 1% → 5% → 25% → 50% → 100%. Each step
in the plan is a row with three mandatory cells:

1. **Abort criteria tied to named metrics** — e.g. "5xx rate > baseline
   +0.1pp", "checkout p95 > baseline +50ms", "conversion −1% vs control".
   Name the metric, the threshold, and the comparison window. "We'll watch
   it" is not an abort criterion.
2. **Soak time** — minimum time at this percentage before the next step
   (long enough to cover a traffic cycle: 24h minimum for anything
   user-facing; 48h+ at the bigger steps). No soak, no promotion.
3. **Who watches** — the dashboards come from the observability checks
   already required by `../release-readiness/` (its R23–R25); the ramp plan
   names which of those dashboards gate each step and who is looking at them.

**Stickiness:** bucket by a stable user/account ID hash, so 1% means "the
same 1% of users, consistently on the new path" — not 1% of requests. A user
flip-flopping between paths on every request corrupts both the UX and the
metrics (see Pitfalls).

**The kill switch is the whole point:** at any step, an abort criterion
firing means **flip the flag back — instantly, via config, no deploy, no
rollback release**. Write the exact procedure in the plan (who can flip it,
where, how fast it propagates) and verify it once at the 1% step so the first
real use isn't also the first test. After a kill: fix, redeploy dark, resume
at the step that failed — the ramp restarts a step, not from zero, unless the
failure was data-corrupting.

Ramp on days with full on-call cover. Not Fridays. Not the day before a
holiday freeze.

### Step 4 — Data-layer safety (expand and contract)

Flags make **code** reversible. Schema and data changes need their own
reversibility: **expand-and-contract** (parallel change), so the old and new
code paths can coexist at every ramp percentage:

1. **Expand** — additive only: new columns/tables/topics alongside the old.
   Old path untouched; new path writes both (dual-write) or writes new.
2. **Migrate** — backfill historical data; verify parity (counts, checksums)
   between representations.
3. **Contract** — remove the old columns/paths **only after** the flag has
   been at 100% through its full soak. Contract is its own change with its
   own review; it is the point of no return, so it goes last.

**Never let a flag guard an irreversible migration.** If flipping the flag
OFF cannot restore correct behavior — because data was destructively
transformed, dropped, or written in only the new shape — the kill switch is
theater and every abort criterion above it is fiction. Test the OFF path
*after* dual-writes begin, not just before.

### Step 5 — Cleanup (the new thing becomes THE thing)

At 100% + soak, the rollout is not done — it's *removable*. This is the step
everyone skips, and skipping it is how a codebase accretes 2^N untested flag
combinations. **Flag debt is tech debt.** Merge one cleanup change (dated in
the rollout plan from day one) with this checklist:

- [ ] Old code path deleted (not commented out, not `if (false)`)
- [ ] Flag check removed from code; abstraction collapsed (the branch point,
      the strategy interface, the duplicated template — gone)
- [ ] Flag deleted from config and the registry (registry row moved to a
      "removed" section or marked removed with the date)
- [ ] Tests for the old path deleted; tests for the new path no longer
      mention the flag
- [ ] Docs/runbooks updated — the new path is now just "the path"

Only after cleanup merges do you run the **contract** step of Step 4 (drop
the old columns). Then close the rollout plan with the final dates — it
doubles as the historical record `learn-iterate` reads.

## Hard rules (never-break gates)

Violating any of these is a defect, not a style choice:

1. **No flag without an owner and a removal date** — both set at creation,
   in the registry. An unowned flag has no one accountable for its death.
2. **No ramp step without an abort criterion** — a named metric with a
   threshold, per step. No criterion → no promotion.
3. **No irreversible migration behind a flag** — if OFF can't restore
   correctness, the change may not ride the flag lifecycle; redesign it as
   expand-and-contract first.
4. **No "temporary" flag older than its TTL** — a release flag past its
   removal date is a bug: file it, prioritize it like one, and either delete
   the flag or explicitly re-date it with a reason.

## Worked example — `rel_checkout_payment_v2`

| Day | Stage | Flag state | Gate (abort criteria / soak) | Outcome |
|-----|-------|-----------|------------------------------|---------|
| 0 | Register flag; write rollout plan; `../release-readiness/` for dark deploy | OFF (deployed dark) | Readiness verdict: GO | In prod, zero users on it |
| 0 | DB **expand**: new `payment_intents` table, dual-write ON | OFF | Parity checks on dual-writes | Old schema untouched |
| 1–3 | Dogfood: employees | ON for `@yum.com` accounts | Error parity + checkout success, 48h | 2 bugs found, fixed, redeployed dark |
| 4 | Ramp 1% (sticky by account-ID hash) | ON 1% | Abort: 5xx > +0.1pp, p95 > +50ms · soak 24h | Pass |
| 5 | Ramp 5% | ON 5% | Same + conversion −1% vs control · soak 24h | Pass |
| 6 | Ramp 25% | ON 25% | Same · soak 48h | **p99 regression → kill switch OFF** (config flip, 2 min, no deploy) |
| 7–8 | Fix N+1 query; redeploy dark; resume | ON 25% | Same gate re-armed · soak 48h | Pass |
| 10 | Ramp 50% | ON 50% | Same · soak 48h | Pass |
| 12 | Ramp 100% | ON 100% | Same · soak 7 days | Pass |
| 19 | **Cleanup**: old path + flag + old-path tests deleted, docs updated, registry row closed | Flag gone | Cleanup checklist merged | New path is THE path |
| 20 | DB **contract**: drop legacy payment columns | — | Post-cleanup, own review | Done — 26 days before TTL (day 45) |

## Pitfalls

- **Flag graveyard:** flags accumulate past 100% because cleanup is never
  scheduled → combinatorial state explosion — 2^N configurations, most never
  tested, and nobody dares delete anything → the removal date is set at
  creation (hard rule 1), the cleanup checklist has a date in the plan, and a
  flag past TTL is filed as a defect.
- **Testing only the new path:** CI runs with the flag in one state → the
  path most of production is on (or about to fall back to via kill switch) is
  unverified; the kill switch flips users onto rotten code → per
  `../test-strategy/`, both paths stay covered for as long as both exist —
  the old path's tests die only in the cleanup step.
- **Ramping on a Friday / without soak:** promotion happens on wall-clock
  optimism → the abort fires into an empty on-call room, or a
  slow-burn regression (memory, queue depth, daily-cycle traffic) ships to
  50% before anyone sees it → every step has a minimum soak covering a full
  traffic cycle, and promotions happen when on-call cover is full.
- **Flag as permanent config:** a release flag quietly becomes the way a
  plan/tier/customer is gated → a "temporary" branch point becomes
  load-bearing product logic with a `rel_` name, no entitlement model, and no
  cleanup path → if a flag needs to live, redesign it: rename/re-register it
  as a permission or ops flag with the lifetime that type carries, and give
  the release flag its removal date back.
- **Percentage ramp without user-stickiness:** bucketing by request instead
  of by stable user ID → the same user flip-flops between old and new UX
  mid-session, and metrics compare polluted cohorts → hash a stable ID into
  buckets so a user stays on one path for the whole ramp step.

## Next steps

- `learn-iterate` — feed in the ramp learnings: which abort criteria fired,
  actual vs planned schedule, and the post-100% review of whether the feature
  earned its keep.
- `incident-postmortem` — **any kill-switch event gets one**, even when the
  flip worked perfectly; the abort firing means an expectation was wrong, and
  that gap is the postmortem's first lead.
- The next release of this surface starts again at `../release-readiness/`
  with this rollout plan as prior art.
