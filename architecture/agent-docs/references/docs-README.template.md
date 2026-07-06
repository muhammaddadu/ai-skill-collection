<!--
TEMPLATE — docs/README.md. The routing index for the docs/ tree. Every row must link to a
real (or stubbed) file. Include only the rows for docs you actually create. Keep the
"Conventions" block verbatim — it's the contract the whole tree obeys.
-->

# Documentation

Routing table for {{PROJECT_NAME}}. Each doc owns one concern; find the right one here, then read it. Every doc opens with a one-line "owns / for X see Y" header.

## Find the right doc

| If you need… | Go to | Which owns |
|--------------|-------|-----------|
{{One row per doc. Examples — keep what applies:}}
| Why we're building this, value, success metrics | [value-proposition](product/value-proposition.md) | the *why* |
| What must be true — requirements, scope, roles, acceptance criteria | [PRD](product/prd.md) | the *what* |
| What to build next, in what order | [epics](product/epics/index.md) | build order |
| How it looks — IA, routes, UX principles | [UX hub](ux/index.md) | UX |
| How it's stored — entities, keys, access patterns | [data-model](architecture/data-model.md) | storage |
| System topology, auth flow, env | [system-architecture](architecture/system-architecture.md) | infrastructure |
| Code structure, module map | [app-architecture](architecture/app-architecture.md) | code layout |
| Library/dependency choices | [tech-stack](architecture/tech-stack.md) | dependencies |
| Run it locally | [getting-started](guides/getting-started.md) | local dev |
| API reference + how to add an endpoint | [api-integration](guides/api-integration.md) | API |
| Deploy it | [deployment](operations/deployment.md) | deployment |
| Logs, common issues, rollback | [runbook](operations/runbook.md) | ops |
| What a domain term means | [glossary](glossary.md) | vocabulary |

> Working in the repo (human or AI)? Start with [`AGENTS.md`](../AGENTS.md) and [`LEARNINGS.md`](../LEARNINGS.md) at the repo root.

## Reading paths

- **New to the project:** {{getting-started → app-architecture → glossary}}
- **Understanding the product:** {{value-proposition → PRD → UX → epics}}
- **Building a feature:** {{epics → PRD → UX → data-model → api-integration}}
- **Deploying / debugging:** {{deployment → runbook → system-architecture}}

## Conventions

- **One fact, one home.** Each concern lives in exactly one doc; others link to it rather than restate it. If you're tempted to duplicate, link instead.
- Every doc opens with a one-line ownership header (`> **This doc owns:** … **For X see** …`).
- Keep docs current in the same change as the code/decision. No placeholder sections.
- Mermaid for diagrams and flows, not ASCII art — **except** page-layout mockups, where ASCII wireframes are allowed (they show responsive layouts Mermaid can't). "Planned" content must be labelled and trace to the PRD or data model.
- The requirements doc keeps **stable section numbers** (§1, §2, …) so cross-references resolve; slim bodies, don't renumber.
