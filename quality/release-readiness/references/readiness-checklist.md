# Release Readiness Checklist

<!-- v1.0 | Scoring pattern shared with the `ads` skill (its references/scoring-system.md
     in the growth domain for the original) — same formula, severities, grades, quick-wins logic. -->

## Check ID Convention

- Sequential IDs **R01–R46**, grouped by category.
- Every check names its **evidence** — a check without evidence is scored FAIL,
  not PASS ("checklist theater" guard).
- **Tier** column says which release tiers the check applies to
  (see SKILL.md intake step): `All`, `2+` (standard and high-risk), `3` (high-risk only).
  Checks outside the release's tier are scored **N/A** and excluded from the total.

## Scoring Algorithm

```
Score = Σ(C_pass × W_sev × W_cat) / Σ(C_total × W_sev × W_cat) × 100
```

- `C_pass` = 1 for PASS, 0.5 for WARNING (partial/undocumented evidence), 0 for FAIL
- `W_sev` = severity multiplier of the check
- `W_cat` = category weight
- N/A checks (wrong tier, or genuinely inapplicable — e.g. no data migration) are
  excluded from the denominator.

### Severity Multipliers

| Severity | Multiplier | Criteria |
|----------|-----------|----------|
| Critical | 5.0 | Can cause an incident, data loss, or an unrecoverable state. Blocker-class. |
| High | 3.0 | Materially raises incident probability or blast radius. |
| Medium | 1.5 | Degrades response quality or user experience if missing. |
| Low | 0.5 | Best practice; minor impact. |

### Category Weights

| Category | Weight | Rationale |
|----------|--------|-----------|
| Quality gates | 20% | Untested code invalidates every other safeguard (8 checks) |
| Rollout strategy | 20% | Deliberate exposure control is the biggest incident-size lever (8 checks) |
| Rollback | 15% | The difference between a blip and an outage is how fast you can undo (6 checks) |
| Observability | 15% | You cannot roll back what you cannot see failing (7 checks) |
| Security & compliance | 10% | Low frequency, unbounded downside (6 checks) |
| Comms & support | 10% | Most "incidents" are surprised humans, not broken code (6 checks) |
| Post-launch plan | 10% | A release without a checkpoint is fire-and-forget (5 checks) |

### Grading Thresholds

| Grade | Score | Verdict |
|-------|-------|---------|
| A | 90–100 | **Go** |
| B | 75–89 | **Go with follow-ups** (file them before shipping) |
| C | 60–74 | **Conditional go** — blockers listed, owner + deadline per blocker |
| D/F | <60 | **No-go** — remediate and re-run the review |

**Hard gates override the score** — any hard-gate failure (SKILL.md) is an
automatic no-go even at 95/100.

### Quick Wins Logic

```
IF severity IN {Critical, High}
AND estimated_fix_time < 15 minutes
THEN flag as Quick Win
SORT BY (severity_multiplier × estimated_impact) DESC
```

---

## Quality gates (20%)

| ID | Check | Severity | Tier | Evidence |
|----|-------|----------|------|----------|
| R01 | Release-blocking test suite is green on the exact release candidate (same commit/build ID) | Critical | All | CI run link pinned to the RC SHA |
| R02 | Tests meet the done-bar defined per `../test-strategy` (or the team's written equivalent) | High | All | Done-bar doc + coverage/report against it |
| R03 | No known Critical or release-blocking bugs open against the RC | Critical | All | Tracker query (saved filter link), triage note per exception |
| R04 | Regression executed on the critical user paths touched by this release | High | 2+ | Test run record (automated report or signed-off manual run) |
| R05 | Performance on the changed surface is within budget (latency, memory, bundle/app size) | Medium | 2+ | Benchmark or perf test output vs stated budget |
| R06 | The artifact shipping is the artifact tested — no commits after the tested build | High | All | Build provenance: RC SHA/build ID matches the tested one |
| R07 | Dependency changes reviewed: breaking changes read, licenses acceptable | Medium | 2+ | Diff of lockfile/deps + reviewer note |
| R08 | New user-facing UI passed an accessibility pass (keyboard, contrast, screen reader basics) | Medium | 2+ | A11y checklist or tooling output |

## Rollout strategy (20%)

| ID | Check | Severity | Tier | Evidence |
|----|-------|----------|------|----------|
| R09 | Rollout mechanism chosen **deliberately** — flag, percentage, canary, staged, or big-bang *with written justification* | High | All | Rollout section of the release plan naming the mechanism and why |
| R10 | Kill switch exists: the new surface can be disabled without a redeploy | Critical | 2+ | Flag name/config key + where it is toggled |
| R11 | First exposure stage limits blast radius (internal cohort, single region, small %) | High | 2+ | Stage plan with cohort/percentage per stage |
| R12 | Promotion criteria between stages are defined: which metrics, what thresholds, how long the soak | High | 3 | Written promote/hold/rollback criteria per stage |
| R13 | Schema/data migration is forward-compatible with the previous app version (expand–contract; old code runs against new schema) | Critical | All | Migration review note or test of old version against migrated schema |
| R14 | API/contract changes are backward-compatible or explicitly versioned | Critical | 2+ | Contract diff + consumer compatibility note |
| R15 | Client/server version skew considered — old clients keep working (mobile clients live for months) | High | 2+ | Skew analysis: oldest supported client vs new server behavior |
| R16 | Release window is sane: on-call coverage exists, freeze windows respected, not pre-weekend/holiday without cover | Medium | All | Date + on-call schedule reference |

## Rollback (15%)

| ID | Check | Severity | Tier | Evidence |
|----|-------|----------|------|----------|
| R17 | A documented rollback procedure exists with concrete steps and an owner | Critical | All | Runbook link/section, not "we'll revert" |
| R18 | The rollback path was actually exercised — in staging, a drill, or a prior release of the same shape | High | 2+ | Record of the rollback test (date, environment, outcome) |
| R19 | Data migration is reversible, or a tested roll-forward fix plan is documented instead | Critical | All | Down-migration + test, or written roll-forward plan |
| R20 | Artifacts are versioned and the previous version is retrievable and deployable right now | High | All | Registry/store entry for version N-1 + deploy command/path |
| R21 | Time-to-restore via rollback is estimated and acceptable against the SLO | Medium | 3 | Estimate with basis (measured or reasoned) |
| R22 | Flag-off vs deploy-rollback are distinguished: the team knows which failures need which, and both are documented | Medium | 2+ | Decision table or runbook note |

## Observability (15%)

| ID | Check | Severity | Tier | Evidence |
|----|-------|----------|------|----------|
| R23 | Dashboards for the new surface exist **before** launch, not after the first incident | Critical | 2+ | Dashboard link showing the new surface's panels |
| R24 | Alerts on the new failure modes are wired to the on-call channel and tested (fired once) | High | 2+ | Alert rule + test-fire record |
| R25 | Error tracking captures the new code paths and tags events with the release version | High | All | Error-tracker project/release config (e.g. Sentry release tagging) |
| R26 | SLO impact assessed: expected error-budget consumption of the rollout is stated | Medium | 3 | SLO note in the release plan |
| R27 | Telemetry distinguishes new-path from old-path traffic so the rollout can be compared, not guessed | High | 2+ | Metric/log dimension (flag state, version label) |
| R28 | Health check or synthetic probe covers the new endpoint/flow | Medium | 2+ | Probe config or uptime-check link |
| R29 | Pre-launch baseline for the key metrics is recorded, so "worse" is measurable | Medium | 2+ | Baseline snapshot (numbers + date) in the release notes |

## Security & compliance (10%)

| ID | Check | Severity | Tier | Evidence |
|----|-------|----------|------|----------|
| R30 | No secrets in the release artifact, image, bundle, or repo history added by this release | Critical | All | Secret-scan output on the RC artifact |
| R31 | Every new endpoint/screen/queue enforces authentication and authorization | Critical | All | Route/authz review note or test covering the new surface |
| R32 | PII or regulated-data flows introduced/changed were reviewed; retention and consent unchanged or re-approved | Critical | 3 | Privacy/DPO review record |
| R33 | Security-sensitive changes (auth, crypto, payment, data access) reviewed by someone other than the author | High | All | Named reviewer on the specific change |
| R34 | Dependency vulnerability scan shows no unaddressed Critical CVEs in the shipped artifact | High | 2+ | Scanner output (with triage notes for accepted risks) |
| R35 | Compliance/legal sign-off obtained where this tier requires it (regulated market, app-store policy, contractual) | Medium | 3 | Sign-off record |

## Comms & support (10%)

| ID | Check | Severity | Tier | Evidence |
|----|-------|----------|------|----------|
| R36 | Release notes/changelog written **for the user** — what changes for them, not which PRs merged | High | All | The notes themselves, read as a user |
| R37 | Stakeholders notified of the date, the impact, and what to watch | Medium | 2+ | Sent announcement (channel/message link) |
| R38 | Support and on-call briefed: what changed, known rough edges, how to escalate, how to toggle the kill switch | High | 2+ | Briefing note or handoff message |
| R39 | User-facing docs/help updated in the same release, not "next sprint" | Medium | 2+ | Doc diff/link |
| R40 | Internal demo/announcement scheduled for releases big enough to change how colleagues work | Low | 3 | Calendar entry or post |
| R41 | Status-page or maintenance-window comms prepared if any downtime or degradation is possible | Medium | 3 | Draft status-page entry |

## Post-launch plan (10%)

| ID | Check | Severity | Tier | Evidence |
|----|-------|----------|------|----------|
| R42 | Success metrics named with target values **before** launch (what number, by when, means "worked") | High | All | Metrics section of the release plan |
| R43 | A named owner is watching the release through the monitoring window (not "the team") | High | All | Owner's name + window in the release plan |
| R44 | A checkpoint is scheduled (e.g. +24h and +7d) with an explicit expand/hold/rollback decision | Medium | 2+ | Calendar entry or scheduled task |
| R45 | Conditional-go follow-ups are filed as tickets with owners and deadlines, not left in the report | Medium | All | Ticket links in the readiness report |
| R46 | Cleanup scheduled: flag removal, old-path deletion, migration contract phase | Low | 2+ | Ticket for the contract/cleanup step |

---

## Tier applicability summary

- **Tier 1 (small/low-risk)** runs only `All`-tier checks: R01, R03, R06, R09,
  R13, R16, R17, R19, R20, R25, R30, R31, R33, R36, R42, R43, R45 — 17 checks,
  the short path.
- **Tier 2 (standard)** adds the `2+` checks (39 total).
- **Tier 3 (high-risk)** runs everything (46 checks).
- A check can still be N/A within its tier when the subject doesn't exist
  (no data migration → R13/R19 N/A; no API change → R14 N/A). N/A requires a
  one-line reason in the report.
