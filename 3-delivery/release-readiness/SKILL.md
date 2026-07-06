---
name: release-readiness
description: "Run a go/no-go release review producing a scored readiness report — rollout plan, observability, rollback, comms verified before shipping. Use when preparing a release/launch, a go-live checklist, a rollout plan, or 'are we ready to ship'. Do NOT use for store-submission mechanics (expo-deployment) or writing the test plan itself (test-strategy)."
type: component
domain: 3-delivery
---

# Release Readiness Review

## Purpose

A structured go/no-go review run **before** shipping, producing a scored,
evidence-backed readiness report. It verifies the four things that turn a bad
deploy into a bad week — rollout plan, observability, rollback path, and
comms — plus quality gates, security, and a post-launch plan. Platform-agnostic:
the same review works for a web deploy, a mobile release, an API version, or a
library publish; only the evidence differs. The output is a decision aid — a
verdict with named blockers — for the team and whoever owns the go decision.

**Humans own the go decision.** This skill prepares the evidence and a
recommendation; it never ships, promotes, or merges anything itself.

## Outputs

**Artifact:** `RELEASE-READINESS.md` — dated readiness snapshot for one release
**Format:** markdown — per-category scores, overall 0–100 score with grade,
go / conditional-go / no-go verdict, hard-gate results, blocking items with
owners, quick-wins list
**Location:** alongside the release notes for this version (e.g.
`docs/releases/<version>/RELEASE-READINESS.md`, or wherever the repo keeps
release records) — it is part of the release's paper trail
**Audience:** the delivering team + the person who owns the go decision
(release manager, EM, on-call lead)

## Prerequisites

- A done-bar for "tests pass" — ideally defined per `../test-strategy`; if that
  skill's artifact doesn't exist, ask the team for their written equivalent and
  record it in the report (R02 scores against *something written*, not vibes).
- The tech spec's rollout section, if one exists — it seeds the intake answers
  and the rollout-strategy checks.
- Access to the evidence sources: CI, the tracker, dashboards/alerting config,
  the runbook. The review reads evidence; it does not take anyone's word.
- SLOs, alerts, and runbooks come from ../slo-design/ — run it before this review.

## Workflow

### Step 0 — Contextual intake (do this first, it scales everything)

Ask (or read from the tech spec) before opening the checklist:

1. **What is being released?** Web service, mobile app, API, library, config/infra
   change. This decides which evidence forms apply (e.g. "deploy" for a library
   means publish; rollback means yanking/deprecating a version).
2. **Blast radius:** who is exposed if it breaks — one internal team, a segment,
   all users? Revenue-path or peripheral?
3. **User-facing or internal?** Internal-only tooling can skip several comms and
   observability checks.
4. **Data involved:** schema/data migration? Regulated data (PII, payments,
   health)? Irreversible writes?
5. **Novelty:** new surface vs. change to an existing, already-monitored one.

From the answers, assign a **risk tier** — the tier decides which checks apply
(N/A the rest; the checklist's Tier column encodes this):

| Tier | Profile | Path |
|------|---------|------|
| **1 — small** | Internal or tiny blast radius, no data migration, trivially reverted (config tweak, copy change, patch release) | Short path: ~17 `All`-tier checks. Target: done in under 30 minutes. |
| **2 — standard** | User-facing change of ordinary size; existing surface; reversible | `All` + `2+` checks (~39) |
| **3 — high-risk** | Large blast radius, data migration, new user-facing surface, regulated data, or hard-to-reverse | Every check (46), plus extra scrutiny on hard gates |

Record the tier and the intake answers at the top of the report — the verdict
is only meaningful relative to them. If two answers conflict (e.g. "small
change" but there's a data migration), the riskier answer wins the tier.

### Step 1 — Walk the checklist

Read `references/readiness-checklist.md` for the full 46 checks, IDs R01–R46,
in 7 weighted categories. For each check in this release's tier:

- Mark **PASS / WARNING / FAIL / N/A**.
- **Record the evidence** named by the check (a CI link, a dashboard link, a
  runbook section, a named reviewer). *No evidence = FAIL*, even if everyone
  in the room is sure it's fine — that rule is the entire difference between
  a review and a ritual.
- N/A needs a one-line reason ("no schema change in this release").
- For each FAIL, estimate **fix time** — it feeds the quick-wins list.

### Step 2 — Check the hard gates

Four conditions are an **automatic no-go regardless of score**:

| Gate | Condition | Why it can't be scored around |
|------|-----------|------------------------------|
| HG1 | Data migration with no rollback path *and* no tested roll-forward plan (R19 FAIL) | An irreversible bad state has no "fix it live" option |
| HG2 | New user-facing surface with zero monitoring — no dashboard, no alert, no error tracking (R23+R24+R25 all FAIL) | You'd learn about the incident from customers |
| HG3 | Release-blocking tests failing on the release candidate (R01 FAIL) | Shipping a known-red build is not a risk, it's a decision to break |
| HG4 | Security-sensitive change (auth, payments, data access, crypto) with no second reviewer (R33 FAIL on such a change) | Single-author security changes are how backdoors and blunders ship |

A hard-gate failure short-circuits the review: report **NO-GO**, name the gate,
name the fix, stop. Everything else becomes follow-up detail.

### Step 3 — Score

Use the shared scoring formula (full algorithm, severity multipliers, and
category weights in `references/readiness-checklist.md`):

```
Score = Σ(check_result × severity_weight × category_weight)
      / Σ(possible × severity_weight × category_weight) × 100

check_result: PASS = 1, WARNING = 0.5, FAIL = 0, N/A excluded
```

| Category | Weight |
|----------|--------|
| Quality gates | 20% |
| Rollout strategy | 20% |
| Rollback | 15% |
| Observability | 15% |
| Security & compliance | 10% |
| Comms & support | 10% |
| Post-launch plan | 10% |

### Step 4 — Verdict

| Grade | Score | Verdict |
|-------|-------|---------|
| A | ≥90 | **GO** |
| B | 75–89 | **GO with follow-ups** — file every FAIL as a ticket before shipping |
| C | 60–74 | **CONDITIONAL GO** — list blockers explicitly; each gets an owner and a deadline; the go-owner accepts them by name |
| D/F | <60 | **NO-GO** — remediate, re-run the review |

Hard gates override all of this (Step 2). A conditional go without named owners
for the blockers is a no-go wearing a costume — don't emit one.

Then compute **quick wins** — the fastest way to raise the score before the
ship date:

```
severity ∈ {Critical, High} AND estimated_fix_time < 15 min → Quick Win
sorted by (severity × estimated_impact) DESC
```

Typical quick wins: wire the error tracker's release tag (5 min), add the
kill-switch flag check to the runbook (10 min), send the on-call briefing
message (10 min), pin the CI run link to the RC SHA (2 min).

### Step 5 — Snapshot the report

Write `RELEASE-READINESS.md`, dated, and save it with the release notes for
this version. Structure:

```markdown
# Release Readiness — <name/version> — <YYYY-MM-DD>

**Verdict: GO | GO WITH FOLLOW-UPS | CONDITIONAL GO | NO-GO**
**Score: NN/100 (Grade X)** · Tier: N · Go-owner: <name>

## Intake
<release type, blast radius, user-facing?, data/migration, novelty — 5 lines>

## Hard gates
HG1–HG4: PASS/FAIL each, one line of evidence

## Scores by category
| Category | Score | Notable failures |

## Blocking items (conditional go / no-go only)
| ID | Item | Owner | Deadline |

## Quick wins
| ID | Fix | Est. time | Severity |

## Full check results
| ID | Result | Evidence (link) | Note |
```

The snapshot is append-only history: if checks are fixed, re-run and write a
new dated report rather than editing the old one — the delta between snapshots
is itself useful evidence at the post-launch checkpoint and in any postmortem.

**Re-review triggers.** A verdict binds to a specific release candidate. Re-run
(at least the affected categories) when any of these change after the review:

- new commits land on the RC (invalidates R01/R06 immediately);
- the ship date moves into a freeze window or away from on-call cover (R16);
- scope grows — a "small" release absorbing a migration jumps a tier;
- more than ~a week passes between verdict and ship (evidence goes stale).

## Evidence by release type

The checks are platform-agnostic; the *form* of the evidence is not. When a
check names its evidence, translate it for the release type:

| Concept | Web service | Mobile app | API | Library |
|---------|------------|------------|-----|---------|
| "Deploy" | Rollout to servers | Store release / phased rollout / OTA update | New version live behind gateway | Publish to registry |
| Kill switch (R10) | Feature flag / traffic drain | Remote flag or forced-update path (a store rollback can take days — flags matter *more*) | Version pin / route toggle | Deprecate + advisory; consumers pin |
| Rollback (R17–R20) | Redeploy N-1 | Halt phased rollout; OTA revert if applicable; store rollback is slow | Restore previous version routing | Yank/deprecate release, publish patched N-1 |
| Version skew (R15) | Sticky sessions during rollout | Months of old clients in the wild — the dominant risk | Consumers on old contract | Downstream ranges resolving both versions |
| Observability (R23–R25) | Service dashboards, alerts | Crash reporting, release-health (adoption, crash-free rate) | Endpoint metrics, consumer error rates | Download stats + issue-tracker watch |

Two type-specific emphases:

- **Mobile:** treat every release as harder to reverse than it looks — the
  store review pipeline means rollback ≠ redeploy. Weight R10 (kill switch)
  and R15 (skew) as if they were one severity higher. Store-submission
  mechanics themselves belong to `expo-deployment`, not this review.
- **Library/API:** "blast radius" is consumers, not end users — intake
  question 2 should count downstream dependents, and R14 (contract
  compatibility) is usually the check that decides the verdict.

## Boundaries

- **The go decision is human.** The report recommends; a named person decides
  and is recorded as the go-owner. This skill never triggers a deploy, promotes
  a rollout stage, or merges anything — it prepares evidence. (Same
  human-in-the-loop principle as plan approval in agent-driven SDLC work.)
- **Platform mechanics live elsewhere.** Store submission, build signing, EAS
  specifics → `expo-deployment` (engineering domain). CI pipeline specifics
  are per-repo — this review asks *whether* the gate passed, not how to
  configure it.
- **Writing the test plan is upstream.** This skill consumes the
  `../test-strategy` done-bar; it doesn't define what "tested" means.

## Pitfalls

- **Checklist theater:** ticks appear without evidence → the review passes but
  reality doesn't; the score is fiction → every check names its evidence, and
  no evidence = FAIL. If a check keeps failing on evidence only, fix the
  evidence trail, not the checklist.
- **Big-bang when gradual was available:** a flag system exists but the release
  goes 0→100% anyway → the whole user base is the canary → R09 requires the
  mechanism to be *chosen deliberately*; big-bang must carry a written
  justification, not a default.
- **Monitoring added after the incident:** dashboards and alerts are created
  in the retro, not the release → the first outage is invisible for hours →
  R23–R25 require observability to exist *before* launch; HG2 makes the
  worst case an automatic no-go.
- **Release notes written for the author:** the changelog lists PR titles and
  internal refactors → users and support learn nothing they can act on →
  R36 scores the notes as read by a user; "what changes for me?" must be
  answerable from the notes alone.

## Next steps

- **If the release goes wrong** → `incident-postmortem` (operations domain);
  bring this report — the gap between what was checked and what broke is the
  postmortem's first lead.
- **Post-launch checkpoint (R44)** → compare actuals against the success
  metrics named in R42; the result feeds the next iteration's PRD
  (`prd-development`, product domain) as validated learning.
- Follow-ups from a B or conditional-go verdict are tickets in the normal
  backlog — check them at the next release's R45.
