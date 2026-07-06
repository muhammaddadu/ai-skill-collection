# Runbook: <alert name>

> Copy to `docs/runbooks/<alert-slug>.md` in the target repo — one runbook per
> pageable alert, written **before** the alert ships. Replace every `<...>`.
> Keep triage steps as exact commands and links; a 3am responder should never
> have to guess a query. Fill the sentry-cli examples using the `sentry-cli`
> skill for command details.

## Alert & meaning

- **Alert:** `<alert-rule-name>` — fast-burn page on `<SLO name>`
  (`<e.g. 14x burn over 1h>`)
- **User pain this means:** `<what the user is experiencing right now, in
  user terms — "checkout requests failing", not "error rate elevated">`
- **SLI source:** `<where the metric comes from — LB logs / RUM / synthetic>`

## Severity & escalation

- **Severity:** `<SEV level>` — `<why: blast radius, revenue path, SLA>`
- **Paged:** `<on-call rotation name>`
- **Escalate to `<role/rotation>` if:** `<condition — e.g. no mitigation
  within 20 min, or data integrity in question>`

## Quick triage (in order, ~5 minutes)

1. **Is it real and current?** `<dashboard link>` — confirm the SLI panel
   shows active burn, not a recovered spike.
2. **What changed?** `<deploy-log / release link>`. Check recent releases
   against first-seen errors:
   ```
   sentry release list
   sentry issue list --query "is:unresolved" --period 1h
   ```
3. **What is failing?** Top offending issue and its scope:
   ```
   sentry issue view <ISSUE-ID>
   ```
   `<what to look for: release tag, affected endpoint, user count>`
4. `<check 4 — e.g. dependency/status page link, queue-depth panel>`
5. `<check 5 — optional; delete if triage is complete in 4>`

## Common causes & fixes

| Symptom detail | Likely cause | Fix |
|---|---|---|
| `<e.g. errors start at a release boundary>` | `<bad deploy>` | `<rollback command / link>` |
| `<e.g. single dependency timing out>` | `<downstream outage>` | `<ops kill switch flag>` |
| `<...>` | `<...>` | `<...>` |

## Mitigation vs fix — stop the bleeding first

Mitigate **before** diagnosing root cause. In order of preference:

1. **Kill switch:** flip `<flag name>` OFF (see `../progressive-delivery/`
   for flag conventions) — `<exact command / console link>`
2. **Rollback:** `<exact command / pipeline link to redeploy N-1>`
3. `<degrade gracefully: shed load / disable feature — command>`

Root-cause work happens after impact ends, not instead of mitigation.

## Escalation path

| When | Who | How |
|---|---|---|
| `<20 min, no mitigation>` | `<secondary on-call / EM>` | `<page alias>` |
| `<data integrity or security in question>` | `<incident commander>` | `<channel>` |
| `<customer-facing comms needed>` | `<support/comms owner>` | `<channel>` |

## Post-incident

- Declare resolution in `<incident channel>`; confirm the SLI has recovered
  and note the error-budget spend.
- Run `incident-postmortem` — bring this runbook; every step that confused
  the responder is a finding, and detection gaps feed back into the SLO spec.

## Verified by

> A runbook is verified by someone **other than its author** following it
> cold. Re-verify after any material change to the steps.

| Verifier | Date | Result / gaps found |
|---|---|---|
| `<name>` | `<YYYY-MM-DD>` | `<followed cold; step 3 needed the project slug>` |
