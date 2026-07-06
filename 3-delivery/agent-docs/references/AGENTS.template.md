<!--
TEMPLATE — AGENTS.md. The single source of agent/contributor guidance for the repo.
Replace every {{PLACEHOLDER}}. Delete sections that don't apply (e.g. Subagents if the
repo defines none). Keep the section order — the "Before Building Anything" list and the
"Engineering Principles" are the heart of the methodology; don't drop them.
Verify every command against the project's actual scripts before listing it.
-->

# AGENTS.md

Guide for any AI agent (or human) working in this repository. Read this fully, then **read `LEARNINGS.md` before starting work** — it lists mistakes already made here so you don't repeat them. If you make a mistake and correct it, append it to `LEARNINGS.md` (protocol at the bottom of this file).

## Project Overview

{{ONE_PARAGRAPH: what this project is, who it's for, and the core flow. Name the service/product, the domain, and the deploy target if any.}}

**Stack:** {{LANGUAGES_FRAMEWORKS_DATASTORES}}. {{ONE_LINE_ON_HOW_IT_RUNS_AND_DEPLOYS}}

## Before Building Anything

Consult docs in this order — `docs/README.md` is the index with reading paths:

1. `LEARNINGS.md` — mistakes already made and corrected
2. {{docs/product/epics/index.md — what to build next; omit if no epics}}
3. {{docs/product/prd.md — requirements, the source of truth for *what*; omit if no product}}
4. {{docs/architecture/... — how it's built}}
5. {{docs/guides/getting-started.md — run it locally}}

Domain terms: `docs/glossary.md`. {{Omit if no glossary.}}

## Commands

```bash
{{REAL_COMMANDS — copy verbatim from package.json / Makefile / justfile. Annotate each.
e.g.}}
npm run dev        # local dev server
npm run lint       # lint all workspaces
npm run typecheck  # type checking
npm test           # unit tests
npm run build      # build everything
```

**Before declaring any change done:** {{the lint + typecheck + test + build line that must pass}}.

## Repo Layout

```
{{ANNOTATED_TREE — top 2 levels of the important directories, each with a one-line purpose.}}
```

## Architecture Rules (non-negotiable)

{{The hard invariants for THIS project — the things an agent must never violate. Examples to adapt:}}
- **{{Backend-first / no secrets in the browser / single source of truth for keys / immutable records}}** — {{why}}.
- {{Add the 3–6 rules that, if broken, break the system.}}

### {{Subsystem deep-dives — auth, data flow, etc. Optional; link out to docs/ for the long version.}}

### Adding {{a feature / an endpoint / a component}}

{{The concrete recipe for the most common change, end to end (backend → frontend → test → docs). Link to docs/guides for the full pattern.}}

## Code Standards

- {{Language mode (strict), typing rules, what to avoid (`any`).}}
- {{Component/module style, forms, state.}}
- {{Styling approach.}}
- Named constants over magic numbers; single responsibility per function.
- Tests are colocated unit tests of pure functions (`*.test.*` next to the module). Extract logic into pure functions to make it testable.

## Engineering Principles (apply to every change)

The standing bar — apply as you write, verify before committing:

- **Separation of concerns / layering.** Each layer depends only on the one below. Handlers/routes stay thin; business logic lives in services/pure functions, not in HTTP handlers.
- **One source of truth.** A fact (a key format, a price, a constant, a contract) is defined in exactly one place and imported. Typing the same literal a second time → hoist it.
- **No abstraction leakage.** A lower layer's representation must not surface in a higher one. Don't use `as`/casts to smuggle a type across a boundary — fix the boundary.
- **No duplication — extract the shared function** the first time you'd write it twice.
- **Dependency injection for testability.** Construct dependencies at a seam and inject them; don't reach for globals/env deep in the code. This is what lets the stack run on in-memory/test doubles.
- **Pure functions, unit-tested; thin shells.** Push decisions into pure functions with colocated tests; keep I/O at the edges. Every acceptance criterion should be provable by a test.
- **Update docs in the same change as the code** they describe — stale docs are bugs. Prefer updating existing docs over creating new ones. No placeholder sections.
- Mermaid for diagrams and flows, not ASCII art (exception: ASCII page-layout mockups). "Planned" content must be labelled and trace to the PRD or data model.

## Git Conventions

- Commit messages describe **what is actually in the diff** — check `git status`/`git diff` before writing one.
- Don't commit or push unless asked; never commit secrets/`.env` files.
- {{Commit message format / trailers, if any.}}

## Common Pitfalls

{{The footguns specific to this repo — the things that have bitten people. Seed from LEARNINGS.md as they accumulate.}}

## Subagents {{omit if none}}

`.claude/agents/` defines project subagents for Claude Code:
- **`{{name}}`** — {{what it checks/does; when to run it}}.

## Learnings Protocol

When a mistake is made and then corrected during development, append an entry to `LEARNINGS.md`:

```markdown
## <short title> (<date>)

**What went wrong:** <brief description>
**Why:** <root cause or misunderstanding>
**Fix / Correct approach:** <what was done; what to do instead next time>
```

`LEARNINGS.md` is append-only — never rewrite or delete entries. Review it at the start of every working session.
