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

Organized around the product blueprint — "Make Building Products Fun Again":
Exploration -> Sign-Off -> Discovery -> Sign-Off -> Delivery -> Learn & Iterate.
`BLUEPRINT.md` maps every stage, lane, sign-off, and output to its skill;
`WALKTHROUGH.md` drives the map once end-to-end with a worked feature.

| Dir | Blueprint phase | Contents |
|---|---|---|
| `1-exploration/` | Exploration (human) — intake/intent framing -> **Sign-Off 1** | problem framing, stakeholders, market/company research, positioning, strategy, roadmap, prioritization, product-brief |
| `2-discovery/` | Discovery (humans + AI) — PRD Forming/Storming/Norming, design discovery, eng feasibility -> **Sign-Off 2** | prd-development, user research (JTBD, personas, journeys, interviews), stories/epics, design-signal, eng-feasibility-spike, tech-spec, adr, api-design |
| `3-delivery/` | Delivery (AI codes, humans review/ship) — PI Planning -> build/test/release | pi-planning, test-strategy, release-readiness, agent-docs, UI/design + framework packs (cleanui, tailwind, Expo, NestJS), ralph |
| `4-iteration/` | Learn & Iterate + operate | learn-iterate, SaaS/finance metrics, business health, pricing, incident-postmortem, sentry-cli, eol-message |
| `growth/` | (pack, off-blueprint) | `ads-*` marketing pack, acquisition/organic growth |
| `career/` | (pack, off-blueprint) | PM career coaching |
| `utilities/` | (pack) | outlook, pdf, ffmpeg, screenshot, gpt-image, humanizer |
| `meta/` | (pack) | find-skills, skill authoring, workshop-facilitation protocol |
| `commands/` | — | slash-command .md files (linked into both tools) |
| `retired/` | — | history only; never linked |

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
(agent-docs, ffmpeg-usage, humanizer, and the adopted community skills —
tdd, diagnosing-bugs, resolving-merge-conflicts, postgres-best-practices,
mcp-builder, react-best-practices, react-native-skills, web-design-guidelines).

## Companion tooling (per-project, not vendored here)

- **skilld** (`npx -y skilld`) — generates version-aware skills from a
  project's npm dependencies; run inside project repos, never vendor output.
- **@tanstack/intent** (`npx @tanstack/intent install`) — wires up SKILL.md
  files shipped inside npm packages (Expo, Prisma, Stripe, Vercel adopt it).
- **AWS Agent Toolkit** — `/plugin install aws-core@claude-plugins-official`,
  enabled per-project for CDK/serverless/IAM/observability work.

> Watch item: Expo now ships official intent skills — dedupe the `expo-*`
> pack against them at the next portfolio audit.
