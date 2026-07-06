# Postmortem: <incident title>

<!--
Fill-in template. Copy to docs/postmortems/YYYY-MM-DD-<slug>.md.
All timestamps in UTC. Blameless: roles, not names, in factors and analysis;
no counterfactuals ("should have" → "the system allowed"); record what was
known at each moment. Append-only after publication — corrections go under
Addenda, never as edits.
-->

- **Date of incident:** YYYY-MM-DD
- **Severity:** <sev level>
- **Status:** draft | published
- **Author/facilitator:** <role or name — ideally not the primary responder>
- **Published:** YYYY-MM-DD

## Summary

<!-- 3–5 sentences a person who wasn't there can understand: what broke, for
how long, who was affected, how it was resolved. State the blameless framing:
everyone acted reasonably given what they knew; this document examines the
system. -->

## Impact

| Measure | Value |
|---|---|
| Duration (start → full resolution) | |
| Users affected (count / %) | |
| Requests failed / degraded | |
| Revenue impact | |
| SLA / error-budget impact | |
| Support tickets | |

## Timeline

<!-- UTC. "What was known" records what responders could actually see at that
moment — dashboards, alerts, messages — not what hindsight now shows. -->

| Time (UTC) | Event | What was known at this moment | Source |
|---|---|---|---|
| | <first triggering change/event> | | deploy log / alert / chat / sentry |
| | <problem starts (often known only in hindsight)> | | |
| | <first alert / first human awareness> | | |
| | <key responder actions, escalations, dead ends> | | |
| | <mitigation applied> | | |
| | <impact ends / full resolution> | | |

## Detection

- **Problem started:** <UTC time> (evidence: <e.g. sentry first-seen, metric inflection>)
- **First human awareness:** <UTC time> (via: <alert / customer report / chance>)
- **Detection gap:** <duration> — how the system stayed invisible for this long
- **Mitigation gap:** <duration> (awareness → impact end)
- If detection gap > mitigation gap: at least one action item below must be
  `detect-faster`.

## Contributing factors

<!-- Plural — "what made this possible?" asked across dimensions. Not one root
cause. Roles only, never names. System statements, not "should have"s. Aim for
3–7 across several dimensions; exactly one factor means the analysis stopped
early. Delete unused dimension rows. -->

| # | Dimension | Factor (what the system allowed / lacked) |
|---|---|---|
| 1 | code | |
| 2 | process | |
| 3 | tooling | |
| 4 | knowledge | |
| 5 | alerting | |

## What went well

<!-- Practices, alerts, runbooks, fallbacks that limited blast radius — named
so they are kept and invested in, not accidentally deleted. -->

- 

## Action items

<!-- Max ~5. Every row: a named owner and a due date. Type: prevent |
detect-faster | mitigate-faster. Each item is ALSO filed in the team backlog —
this table is a record, not the tracker. -->

| # | Action | Type | Owner | Due date | Backlog link |
|---|---|---|---|---|---|
| 1 | | prevent / detect-faster / mitigate-faster | | YYYY-MM-DD | |
| 2 | | | | | |

## Lessons

<!-- What this incident taught us that doesn't fit an action item: surprising
system behavior, assumptions that turned out false, useful debugging paths for
the next responder. Write for the person reading this during the NEXT
incident. -->

- 

## Addenda

<!-- Append-only. Dated entries for corrections, later discoveries, and
action-item outcomes. The original text above is never edited. -->

- **YYYY-MM-DD:** <correction or follow-up>
