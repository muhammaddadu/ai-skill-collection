<!--
TEMPLATE — docs/product/epics/index.md. The build plan. Only create this (and per-epic
files) when the project has a product story worth sequencing. Keep the "How to use" and
self-evaluation rules verbatim — they're what make epics honest. Order epics so each one's
groundwork is what the next builds on; don't build ahead.
-->

# Epics — Build Plan & Self-Evaluation Index

> **This doc owns:** the build plan — the ordered epics, their dependencies, and how their acceptance criteria are self-evaluated. **For scope see** [PRD](../prd.md); **for modules see** [app architecture](../../architecture/app-architecture.md).

Each **epic** is a shippable slice of scope with its own file, deliverables, and **checkbox acceptance criteria the agent uses to self-evaluate** progress. Epics are ordered because each one's groundwork is what the next builds on.

## How to use these files

- **Pick the next epic** from the table below — don't build ahead of it.
- Each epic file carries **`- [ ]` acceptance criteria** in two groups:
  - **Functional** — what the feature must do, mapped to PRD sections.
  - **E2E validation** — the end-to-end behaviour a test must prove.
- **Self-evaluation:** an epic is *done* only when **every box is checked** and the project's lint/typecheck/test/build all pass. To self-evaluate, read each unchecked box, find the code/test that satisfies it, and either check it (with the evidence) or leave it and explain the gap. Tick a box only when a test or concrete artifact proves it — never on intent.
- **Keep boxes honest.** A checked box without a passing test or shipped artifact is a bug. Criteria are append-friendly: if a requirement surfaces mid-epic, add a box rather than widening an existing one.

## Epics at a glance

| Epic | Title | Status | Depends on |
|------|-------|--------|-----------|
| [E0](E0-{{slug}}.md) | {{Skeleton / foundation}} | Planned | — |
| [E1](E1-{{slug}}.md) | {{...}} | Planned | E0 |
| [E2](E2-{{slug}}.md) | {{...}} | Planned | E1 |

## Build order & dependencies

```mermaid
graph LR
    E0[E0 {{Skeleton}}] --> E1[E1 {{...}}]
    E1 --> E2[E2 {{...}}]
```

## Testing is first-class

E2E testing is not a final phase and not its own epic — it's a standing requirement woven into every epic. The shared harness (test runner + fixtures + a test-auth path that mints tokens without the real login round-trip) lands in the foundation epic; every feature epic carries its own E2E criteria and ships the specs that prove them.

## Out of scope

{{What you're explicitly NOT building yet. Don't build ahead of the epics.}}
