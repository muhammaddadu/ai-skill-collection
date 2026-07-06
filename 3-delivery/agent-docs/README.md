# agent-docs

A portable [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills) that scaffolds any project — new or existing — with a **docs-driven convention set** that AI agents and humans can both follow:

- **`AGENTS.md`** — the single source of agent/contributor guidance (the one file every tool reads)
- **`CLAUDE.md`** — thin; imports `@AGENTS.md`, holds Claude-only overrides
- **`LEARNINGS.md`** — an append-only log of mistakes made and corrected
- **`docs/`** — one concern per file, behind a routing index, with **one-fact-one-home** ownership headers and **self-evaluating epics**

The skill installs the *methodology*, not boilerplate: it inventories your repo first, infers real commands/stack/layout, tailors the doc taxonomy to the project type, fills in what it can verify, and marks the rest as honest `TODO`s — it never fabricates facts.

Works in both **Claude Code** and **Codex** (any tool that reads `~/.claude/skills` or `~/.codex/skills`).

## Install

### Option A — npx (recommended)

Clone the skill (no git history) into the shared skills dir and run the installer, which symlinks it into Claude Code and Codex:

```bash
npx degit muhammaddadu/agent-docs-skill ~/.agents/skills/agent-docs
~/.agents/skills/agent-docs/install.sh
```

> `~/.agents/skills/` is just the canonical home — `install.sh` symlinks from there into each tool, so a single `git pull` updates the skill everywhere.

### Option B — clone + install

```bash
git clone git@github.com:muhammaddadu/agent-docs-skill.git ~/.agents/skills/agent-docs
~/.agents/skills/agent-docs/install.sh
```

### Option C — ask your agent (prompt install)

Paste this to Claude Code or Codex:

> Install the agent-docs skill: clone `git@github.com:muhammaddadu/agent-docs-skill.git` into `~/.agents/skills/agent-docs`, then run its `install.sh` to symlink it into `~/.claude/skills` and `~/.codex/skills`.

Restart the agent (or start a new session) after installing so it picks up the skill.

## Use

Once installed, just ask — the skill triggers on requests like:

> - "Set up an AGENTS.md and docs structure for this repo"
> - "Make this project agent-ready"
> - "Scaffold the contributor/agent conventions here"

Or invoke it explicitly: `/agent-docs` (Claude Code).

The skill will profile the project (new vs existing, project type), confirm anything genuinely ambiguous, then scaffold the root files and a tailored `docs/` tree — merging with, never clobbering, anything already there.

## What's in here

```
agent-docs/
  SKILL.md                  # the skill: workflow + the conventions it encodes
  install.sh                # symlink installer for Claude Code + Codex
  references/               # templates the skill fills in per-project
    AGENTS.template.md
    CLAUDE.template.md
    LEARNINGS.template.md
    docs-README.template.md
    epics-index.template.md
    epic.template.md
```

## The conventions it encodes

- **One fact, one home** — each concern lives in one doc; others link, never duplicate
- **Ownership headers** — every doc opens with `> **This doc owns:** … **For X see** …`
- **Docs current in the same change as the code** — stale docs are bugs; no placeholder sections
- **Mermaid for diagrams** (ASCII only for page-layout mockups)
- **Stable requirement section numbers** so cross-references don't rot
- **Self-evaluating epics** — `- [ ]` criteria ticked only when a test or shipped artifact proves it; don't build ahead
- **Append-only learnings** — never rewrite or delete an entry

## License

MIT
