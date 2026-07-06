---
name: agent-docs
description: "Scaffold (or retrofit) a project with the docs-driven agent conventions: a root AGENTS.md as the single source of agent guidance, a thin CLAUDE.md that imports it, an append-only LEARNINGS.md, and a docs/ tree with a routing index, one-fact-one-home ownership headers, and self-evaluating epics. Use when the user asks to set up project conventions, an AGENTS.md, agent/contributor docs, a docs/ structure, or to make a repo agent-ready — on a new or existing project."
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
  - AskUserQuestion
  - Agent
---

# agent-docs

Set up a project so any AI agent (or human) can work in it the same disciplined way: one canonical guide, an honest learnings log, and a `docs/` tree where every fact has exactly one home.

This skill **installs a methodology**, not a fixed set of files. Tailor the doc taxonomy to the project — a CLI tool has no UX hub, a library has no deployment ops. Fill in what you can verify from the codebase; mark everything else as a clearly-labelled TODO. **Never fabricate facts** (commands, architecture, requirements) — a confidently-wrong doc is worse than a `TODO`.

## The artifacts

Five things, in priority order. Templates live in `references/` — read each one before writing its file.

1. **`AGENTS.md`** (repo root) — the single source of agent/contributor guidance. Everything an agent must know to work safely lives here or is linked from here. Template: `references/AGENTS.template.md`.
2. **`CLAUDE.md`** (repo root) — thin; imports `AGENTS.md` with `@AGENTS.md` and points at `LEARNINGS.md`. Claude-specific overrides only. Template: `references/CLAUDE.template.md`.
3. **`LEARNINGS.md`** (repo root) — append-only log of mistakes made and corrected. Reviewed at the start of every session; appended to when a mistake is made and fixed. Template: `references/LEARNINGS.template.md`.
4. **`docs/README.md`** — the routing index: a "If you need… / Go to / Which owns" table, reading paths, and the doc conventions. Template: `references/docs-README.template.md`.
5. **`docs/**`** — the actual docs, one concern per file, tailored to the project. Epics get a special pattern: `references/epics-index.template.md` and `references/epic.template.md`.

## The conventions these encode

These are the point of the whole exercise — preserve them verbatim in the generated docs:

- **One fact, one home.** Each concern lives in exactly one doc; others link to it rather than restate it. Tempted to duplicate → link instead. (Same rule for constants in code: define once, import.)
- **Ownership headers.** Every doc opens with one line: `> **This doc owns:** <concern>. **For X see** [other](link).`
- **Docs current in the same change as the code/decision they describe.** Stale docs are bugs. No placeholder sections that never get filled.
- **Mermaid for diagrams and flows**, not ASCII art — *except* page-layout/responsive mockups, where ASCII wireframes are allowed.
- **"Planned" content is labelled** as such and traces to a requirement (PRD / data model).
- **Stable section numbers** in the requirements doc (PRD §1, §2, …) so cross-references don't rot — slim bodies, don't renumber.
- **Epics are self-evaluating.** Each epic carries `- [ ]` acceptance criteria; a box is ticked only when a test or shipped artifact proves it, never on intent. Don't build ahead of the current epic.
- **Learnings are append-only.** Never rewrite or delete an entry.

## Workflow

### 1. Read the templates and the target repo

Read every file in `references/`. Then inventory the target project so the docs describe *this* repo, not a generic one:

- `git rev-parse --show-toplevel` (confirm root), `ls` the root, and look for: `package.json` / `pyproject.toml` / `go.mod` / `Cargo.toml` / `Gemfile` etc. to learn the stack and the real **commands** (build, test, lint, dev, deploy).
- Existing `README.md`, `docs/`, `CONTRIBUTING.md`, `AGENTS.md`, `CLAUDE.md`, `.cursorrules` — these are the source of truth for what already exists; **read them, don't overwrite blind**.
- For a non-trivial existing codebase, dispatch an `Explore` agent (or use CodeGraph if a `.codegraph/` dir exists) to map the module layout, entry points, and architecture rather than reading file-by-file.

### 2. Profile the project

Decide two things:

- **New vs existing.** New (empty/near-empty repo) → docs describe what *will* be built; lean on the product docs (value-prop, PRD, epics) and label everything planned. Existing → docs describe what *is* there; lead with architecture/app-layout/getting-started and infer commands from the build files.
- **Project type → doc taxonomy.** Pick only the categories that apply:

| Category | Include when… | Typical files |
|----------|---------------|---------------|
| `product/` | the project has end users / a product story | `value-proposition.md`, `prd.md`, `epics/` |
| `ux/` | there's a UI | `index.md` (IA, routes), per-surface files, `theme.md` |
| `architecture/` | almost always | `system-architecture.md`, `app-architecture.md`, `data-model.md`, `tech-stack.md` |
| `guides/` | almost always | `getting-started.md`, `api-integration.md` |
| `operations/` | it gets deployed/run as a service | `deployment.md`, `runbook.md` |
| `glossary.md` | the domain has jargon | one file |

If the type or which categories apply is genuinely ambiguous and changes what you scaffold, ask with `AskUserQuestion` (project type; new vs existing; whether to include product/UX/ops). Otherwise infer and proceed, stating what you assumed.

### 3. Scaffold

- **Root files first** (`AGENTS.md`, `CLAUDE.md`, `LEARNINGS.md`) from the templates, filled with the real project name, stack, commands, and layout.
- **`docs/README.md`** routing index covering exactly the files you will create — every row links to a real (or stubbed) file.
- **The doc files**, one concern each, every one opening with an ownership header. Stub unbuilt docs with the header + a short "what this will own" line + a `TODO` — don't ship empty headings.
- **Epics** (if `product/`): an `epics/index.md` (ordered table + dependency mermaid + "how to use / self-evaluate") and one file per epic with Functional + E2E checkbox criteria.

**Merge, don't clobber.** If a target file already exists, read it and fold its real content into the new structure; never blow away existing guidance. When unsure whether to overwrite, show the user the diff intent and ask.

### 4. Wire cross-links and verify

- Make sure `CLAUDE.md` imports `@AGENTS.md`, `AGENTS.md`'s "Before Building Anything" reading order points at real docs, and `docs/README.md` rows resolve.
- Every doc has an ownership header. No dangling links. No fabricated commands — each command in `AGENTS.md` must exist in the project's scripts (verify against `package.json`/Makefile/etc.).
- Report what you created, what you stubbed as TODO, and the one-line summary of each convention so the user knows the rules the repo now follows.

## Notes

- Default install location for the *skill* is personal (`~/.claude/skills/agent-docs/`) so it's available everywhere. The *output* always lands in the target repo.
- Keep `AGENTS.md` the one file other tools also read; put Claude-only guidance in `CLAUDE.md`. If the repo uses other agent tools (Cursor, Cline), have their config point at `AGENTS.md` too rather than duplicating rules.
- This skill produces structure and conventions, not content you can't back up. When the project genuinely lacks a fact (no tests yet, no deploy yet), say so in the doc as a labelled gap — that honesty is itself the convention.
