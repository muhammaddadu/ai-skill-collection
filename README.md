# skills

Single source of truth for all agent Skills (Claude Code + Codex), organized as
an SDLC portfolio. Tools consume skills via symlinks — edit here, commit, and
every tool sees the change in its next session.

## Install

```bash
./install.sh
```

Links every skill listed in `manifests/claude.txt` into `~/.claude/skills/` and
`manifests/codex.txt` into `~/.codex/skills/` (flat, as the tools expect), plus
`commands/*.md` into `~/.claude/commands/` and `~/.codex/prompts/`. Existing
real directories are moved to a timestamped `*.backup-*` folder, never deleted.
Re-run after adding a skill or editing a manifest. Restart sessions to pick up
changes — skills are scanned at session start.

## Layout

| Domain | Contents |
|---|---|
| `product/` | discovery, strategy, requirements (PRD, stories, personas, roadmaps…) |
| `growth/` | `ads-*` marketing pack, SaaS/finance metrics, pricing, growth advisors |
| `design/` | UI guidance (cleanui), design-system lookup, Tailwind skills |
| `architecture/` | agent-docs conventions, context engineering; ADR/tech-spec (planned) |
| `engineering/` | Expo pack, NestJS pack, framework-specific skills |
| `quality/` | test-strategy, release-readiness (planned) |
| `operations/` | sentry-cli; SLO design, incident postmortem (planned) |
| `career/` | PM career coaching (off-SDLC, kept separate) |
| `utilities/` | outlook, pdf, ffmpeg, screenshot, image gen, humanizer |
| `meta/` | find-skills, skill authoring, workshop-facilitation protocol |
| `commands/` | slash-command .md files (linked into both tools) |
| `retired/` | kept for history only; never linked |

## Conventions (enforced by `TEMPLATE/SKILL.md`)

- **Name:** `<domain>-<object>[-workshop|-advisor]`, kebab-case, dir name ==
  frontmatter `name`. One skill = one deliverable or one decision.
- **Description:** `"Verb the artifact… Use when <trigger>. Do NOT use for
  <adjacent case>."` Target ≤350 chars, hard cap 500 — descriptions are
  injected into every session; triggers must be mutually exclusive within a
  domain.
- **Body:** ≤~500 lines; push detail into `references/` with explicit routing
  lines ("for X, read `references/x.md`").
- **Paths:** never absolute. Own files: relative (`references/…`). A skill in
  the *same* phase/pack dir: sibling-relative (`../<skill>/…`) is fine. A
  skill anywhere else: reference it **by name in backticks** (e.g. "see
  `prd-development`") — skills install flat, so a name is resolvable in the
  skills root, and path refs across dirs would break (installed symlinks
  resolve `..` physically into the repo dir).
- **Outputs:** every skill declares artifact, format, save location, audience.
- **Freshness:** anything pinned to a moving target (SDK, CLI, ad platform)
  carries `tested_date:` and version constraints in frontmatter.
- Skills must not duplicate harness built-ins (`/code-review`,
  `/security-review`, `/verify`) or per-repo subagents (repo invariant
  guardians live in each repo's `.claude/agents/`).

Vendored third-party skills record their origin in a `.upstream` file
(agent-docs, ffmpeg-usage, humanizer).
