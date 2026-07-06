# ADR template

Copy into `docs/adr/NNNN-<slug>.md` (or the repo's existing ADR directory) and
fill every section. Delete the guidance comments; keep the headings. If the
target repo already has ADRs with different headings, follow those instead.

---

```markdown
# NNNN. <Title — the decision as a short active phrase, e.g. "Use Postgres for durable workflow state">

**Status:** proposed | accepted | rejected | superseded by [ADR-NNNN](NNNN-<slug>.md) | deprecated
**Date:** YYYY-MM-DD  <!-- date decided, not date written, if recording post-hoc -->
**Deciders:** <who agreed to this — names/roles, not "the team">

## Context

<!-- The situation forcing a choice. What problem are we solving, what changed,
     what breaks if we do nothing? Facts a future reader cannot reconstruct.
     No hints of the answer here. 1–3 paragraphs. -->

## Decision Drivers

<!-- The forces that actually decide it, ranked. 3–6 bullets. -->
- <driver 1 — e.g. operational simplicity for a two-person team>
- <driver 2 — e.g. must run air-gapped>
- <driver 3>

## Options Considered

<!-- 2–4 options a reasonable engineer could pick. Include "status quo / do
     nothing" when it's genuinely viable. Every option gets real pros AND cons;
     the winner must have at least one con. -->

### Option 1: <name>

<one-line description>

- Good: <honest pro>
- Good: <honest pro>
- Bad: <honest con>

### Option 2: <name>

<one-line description>

- Good: <honest pro>
- Bad: <honest con>
- Bad: <honest con>

### Option 3: <name> (optional)

<one-line description>

- Good: <honest pro>
- Bad: <honest con>

## Decision & Rationale

Chosen option: **<Option N: name>**.

<!-- Why it won: which decision drivers it satisfied best. Then, explicitly,
     why each losing option lost — one sentence per loser naming the driver
     that killed it. This paragraph is the reason the ADR exists. -->

- Option <X> rejected because <driver it failed>.
- Option <Y> rejected because <driver it failed>.

## Consequences

<!-- Both directions, always. -->

- **Easier:** <what this enables or simplifies>
- **Harder:** <what this costs — new obligations, migrations, skills, lock-in>
- **Neutral / to watch:** <side effects worth monitoring>
- **Revisit if:** <the condition that would reopen this decision>

## Links

<!-- Optional. Related ADRs (supersedes/superseded-by/refines), the tech spec
     that spawned this, PRD requirements cited as drivers, key external
     references (benchmark, vendor doc, RFC). -->
- Supersedes: [ADR-NNNN](NNNN-<slug>.md) <!-- if applicable -->
- Spec: <link>
```
