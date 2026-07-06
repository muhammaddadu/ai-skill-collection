---
name: slo-design
description: "Define production health before launch: user-centric SLIs, SLO targets with error budgets, burn-rate alerts that page on user pain (not CPU), and a runbook per pageable alert. Use when designing SLOs, alerts, error budgets, or runbooks. Do NOT use for the go/no-go review (release-readiness) or post-incident analysis (incident-postmortem)."
type: component
domain: 3-delivery
---

# SLO Design

## Purpose

Define what "healthy in production" means **before** launch — not in the first
incident's retro. The output is the operating contract for a service: which
user-visible signals matter (SLIs), what "good enough" is (SLOs), how much
failure is affordable (error budget), what wakes a human (alerts on user pain,
never on CPU), and what that human does next (the runbook a responder reaches
for at 3am). This is what makes `../release-readiness/`'s "monitoring exists"
checks meaningful rather than dashboard theater: that review verifies evidence;
this skill is where the evidence comes from.

## Outputs

**Artifact:** observability spec + one runbook per pageable alert
**Format:** markdown
**Location:** `docs/specs/<service-or-feature>-slo.md` in the target repo,
containing: SLI definitions **with measurement source**, SLO targets **with
rationale**, the error-budget policy, alert definitions (threshold, duration,
severity, WHO is paged, WHICH runbook), and the dashboard list. Runbooks live
in `docs/runbooks/<alert-slug>.md` — one per pageable alert, from
`references/runbook-template.md`.
**Audience:** the on-call responder (above all the 3am one), the delivering
team, and the go-owner reading the release-readiness report.

## Prerequisites

- A `tech-spec` for the service — what it does, who its users are, and what
  they actually wait on. You cannot pick user-centric SLIs without it.
- Error tracking wired up (`sentry-cli`) — several SLIs and most runbook
  triage steps read from it.

## Workflow

### Step 1 — Pick SLIs from the user's point of view

An SLI is a ratio of good events to total events, measured where the *user*
experiences the service — not where it's convenient to instrument. Standard
menu:

- **Availability:** good requests / total requests. Define "good" explicitly
  (e.g. non-5xx and completed).
- **Latency:** p95/p99 of what the user actually waits on — the full
  page-interactive or API-round-trip time, not one backend hop.
- **Correctness / freshness** where relevant: right answer, data no staler
  than X (pipelines, caches, search indexes).

**2–4 SLIs per service — more means none get watched.** For each SLI, state
the **measurement source**: where the number actually comes from (LB access
logs, RUM, Sentry, synthetic probes, client SDK). If two sources disagree,
prefer the one closer to the user.

### Step 2 — Set SLOs deliberately

- **Measure the baseline first.** Run the SLI for at least a week before
  promising a target. Setting an SLO above your current performance is
  declaring an incident on day one.
- **Tie the target to user tolerance, not vanity.** "Three nines" costs
  roughly 10x "two and a half" — engineering time, redundancy, on-call load.
  Write down what the extra nine *buys the user*; if the answer is "nothing
  they'd notice", pick the cheaper target.
- **SLO ≠ SLA.** The SLO is an internal target with an error budget; an SLA is
  a contractual promise with penalties. Keep the SLO stricter than any SLA so
  the budget burns internally before money does.

Record each target with a one-line rationale in the spec.

### Step 3 — Error budget and the policy that gives it teeth

Budget = **1 − SLO over the window** (e.g. 99.9% over 30 days ≈ 43 minutes of
badness). The budget is permission to ship: spend it on releases, experiments,
and planned risk.

The **policy** is what happens when it runs out — without one, an SLO is a
poster. Minimum viable policy, written in the spec:

- Budget exhausted → **feature work yields to reliability work** until the
  SLI recovers and the budget is back in credit.
- Active `../progressive-delivery/` ramps **pause**; new ramps don't start.
- Who declares it, who can override, and where it's announced.

### Step 4 — Alert design: page on symptoms, burn-rate on SLOs

- **Page ONLY on symptoms** — SLO burn, the user hurting *now*. Causes (CPU,
  memory, disk, queue depth) go to dashboards and tickets; a cause with no
  user pain is maintenance, not an emergency.
- **Use burn-rate alerting, not static thresholds.** Alert on how fast the
  budget is being consumed:
  - **Fast burn → page:** e.g. 14x budget rate over 1h (an outage in
    progress — at that rate a 30-day budget dies in ~2 days).
  - **Slow burn → ticket:** e.g. 2x over 24h (a leak — fix this week, not
    tonight).
- **Every page must be actionable + urgent + have a runbook.** Each alert
  definition names its threshold, duration, severity, WHO is paged, and WHICH
  runbook — an alert missing any of these doesn't ship.
- **The deletion rule:** if a page fires and the responder correctly does
  nothing, delete the alert or demote it to a ticket. Every unactionable page
  trains on-call to ignore the pager.

### Step 5 — Runbooks, written before the alert ships

One runbook per pageable alert, at `docs/runbooks/<alert-slug>.md`. Fill in
`references/runbook-template.md` — alert meaning in user terms, quick triage
with exact commands, mitigation-before-fix, escalation path.

A runbook is **verified by someone OTHER than its author following it cold**.
If the author has to explain a step out loud, the step is wrong. Record the
verifier and date in the runbook itself.

### Step 6 — Instrument-before-launch check

Walk the spec against the release build: every SLI must be **measurable in the
build that ships** — the metric exists, the dashboard renders it, the alerts
are wired and have been test-fired once. This is exactly the evidence
`../release-readiness/`'s observability checks (R23–R29) ask for; hand the
spec and dashboard/alert links to that review.

## Pitfalls

- **Cause-based paging:** pages on CPU/memory/disk instead of SLO burn →
  alert fatigue, and the real user-pain pages get ignored in the noise →
  demote causes to dashboards/tickets; page on burn rate only (Step 4).
- **100%-uptime SLOs:** no error budget exists → either no one can ever
  release, or the SLO is ignored from week one → set the target from baseline
  + user tolerance; 100% is not a target, it's a refusal to choose.
- **SLIs measured where convenient, not where the user is:** server-side
  metrics look green during a CDN/DNS/client outage → dashboards say healthy
  while users see errors → state the measurement source per SLI and prefer
  LB-edge/RUM/synthetic over in-process counters (Step 1).
- **Alerts without runbooks:** the page fires at 3am and the responder starts
  archaeology in the dashboard jungle → mitigation is delayed by discovery →
  no runbook, no pageable alert (Step 5); write it before the alert ships.
- **Dashboard sprawl as a substitute for SLOs:** dozens of panels, no
  definition of "healthy" → during an incident nobody knows which graph is
  the truth → the SLO spec names the few numbers that matter; dashboards
  exist to explain *why* an SLO is burning, not to replace it.
- **SLOs set without a baseline:** target promised before measuring a week of
  reality → instant budget bankruptcy and a permanently red dashboard nobody
  believes → baseline first (Step 2), then negotiate the target.

## Next steps

- `../release-readiness/` — bring the spec, dashboard links, and test-fired
  alerts as the evidence for its observability checks (R23–R29).
- `../progressive-delivery/` — ramp abort criteria are SLO burn: wire each
  ramp step's gate to the SLIs defined here, and pause ramps per the
  error-budget policy.
- `incident-postmortem` — after any incident, its detection gap is a direct
  test of this design; repeated `detect-faster` action items loop back here
  as missing SLIs, alerts, or runbook steps.
