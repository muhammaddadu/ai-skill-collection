# Product Brief: <Initiative name>

> Copy to `docs/product/briefs/<slug>.md`. Keep it to 1–2 pages — this is the
> Sign-Off 1 artifact, not a PRD. Delete the guidance blockquotes when done.

**Status:** draft | in review | signed off
**Author:** <name>
**Date:** <YYYY-MM-DD>

---

## Original intake

> The ask **verbatim** — paste the Slack message, ticket text, or meeting
> quote unedited. Note the source.

- **Received from:** <who>, via <channel>, on <date>
- **Verbatim ask:**

  > "<exact words>"

## Intent — what and why now

> The outcome the stakeholders want in the world (not the feature they asked
> for), and what changed that makes this the moment. One or two sentences
> each. Link any `problem-statement` or `jobs-to-be-done` output that shaped
> this framing.

- **What we want to be true:** <outcome>
- **Why now:** <the trigger — deadline, competitor move, threshold crossed,
  strategic bet>

## Requesting stakeholders

> Who is asking, and their intent in their own words. Divergent intents are
> recorded, not smoothed over.

| Stakeholder | Role | Intent (their words) |
|---|---|---|
| <name> | <role> | <what they said they want> |

## Users affected

> Who experiences the change — usually not the requesters. Segment and rough
> count.

- <segment> — <how they are affected, approx. how many>

## Constraints

> Provided by stakeholders — elicited, never invented. Hard constraints kill
> the initiative if violated; soft constraints are owned preferences with a
> relaxation cost.

### Hard

- <constraint> — <source: regulation / contract / budget / platform mandate>

### Soft

| Constraint | Owner | Cost of relaxing it |
|---|---|---|
| <preference> | <stakeholder> | <what it would take / cost> |

## Success criteria

> Measurable: every row needs metric, target, and horizon. Anything that
> can't be made measurable yet is a hypothesis for Discovery — flag it as
> such, don't dress it up as a criterion.

| Criterion | Metric | Target | Horizon |
|---|---|---|---|
| <what "worked" means> | <how it's measured> | <number> | <by when> |

**Hypotheses for Discovery** (not yet measurable):

- <assumed outcome Discovery must validate and quantify>

## Out of scope

> The adjacent things this deliberately does NOT cover — the neighboring
> feature people will assume is included, the second segment, the legacy
> path. Each line prevents a future argument.

- <excluded item> — <one-line reason>

## Priority rationale

> Why this deserves a slot ahead of the alternatives: cost of delay, what it
> displaces, why now beats next quarter. If priority was contested, record
> the framework used (via `prioritization-advisor`), the scores, and who
> agreed.

- **Argument:** <why this, why now, versus what>
- **Contested?** <no | yes — framework used, outcome, who agreed>

## Sign-off record (Sign-Off 1)

> A brief without a recorded sign-off has not passed the gate. Conditions
> attached to approval are part of the record.

| Approver | Role | Decision | Date | Conditions |
|---|---|---|---|---|
| <name> | <role> | approved / rejected | <YYYY-MM-DD> | <none or listed> |

**Hand-off:** on sign-off, this brief is Discovery's charter — see
`prd-development` and `discovery-process`. Material changes to intent,
constraints, or success criteria go back through the approvers above.
