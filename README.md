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

The installer also maintains a marked global `divergent-ideation` activation rule
for detected Codex, Claude Code, Gemini CLI, OpenCode, and Cursor configuration
directories. It points to this checkout's skill and applies to brainstorming,
naming, strategy, design alternatives, and choices between approaches. Simple
questions and routine edits keep their direct path. The rule is a model instruction,
not an enforcement mechanism; project settings or explicit user requests may override it.

The same managed block routes substantial visual work to the shared visual-refinement
reference owned by `cleanui`. Frontend, image-to-code, and brand review workflows
reuse its evidence, bounded iteration, and subtraction procedure. Domain rubrics
and human checkpoints remain in their original skills. An optional external-seed
technique in `divergent-ideation` helps vary stalled visual exploration without
randomizing requirements or replacing an established design direction.

Existing instructions are preserved, updates are atomic, and each changed existing
file receives a unique adjacent `.ideation-backup-*` copy. Repeated installs do
not duplicate the block. Supported home/config environment overrides are honored;
Gemini uses the standard `GEMINI.md` filename. Symlink instruction paths and
malformed managed blocks require manual resolution. Detection means a supported
configuration directory exists; no running app or account is inspected.

```bash
# Link skills without changing global instructions
./install.sh --skip-global-instructions
# Preview or remove the managed rules (from the repo root)
python3 meta/divergent-ideation/scripts/setup_global.py --dry-run
python3 meta/divergent-ideation/scripts/setup_global.py --remove
```

Removal leaves the instruction files in place, including an empty dedicated Cursor
file when applicable. A later default install reinstates the rule; use the opt-out
flag to keep it removed. The checkout must remain available for referenced skills.
Claude Desktop, ChatGPT, and other browser-only clients require instructions set
inside their app or project; this installer reports that limitation. Third-party
skill installers do not automatically run this repository's post-install step.
Global instruction locations follow the official
[Gemini CLI](https://geminicli.com/docs/cli/gemini-md/),
[OpenCode](https://dev.opencode.ai/docs/rules/), and
[Cursor](https://prod.cursor.com/help/customization/rules) documentation.

## Layout

Organized around the product blueprint — "Make Building Products Fun Again":
Exploration -> Sign-Off -> Discovery -> Sign-Off -> Delivery -> Learn & Iterate.
`BLUEPRINT.md` maps every stage, lane, sign-off, and output to its skill;
`WALKTHROUGH.md` drives the map once end-to-end with a worked feature.

| Dir | Blueprint phase | Contents |
|---|---|---|
| `1-exploration/` | Exploration (human) — intake/intent framing -> **Sign-Off 1** | problem framing, stakeholders, market/company research, positioning, strategy, roadmap, prioritization, product-brief |
| `2-discovery/` | Discovery (humans + AI) — PRD Forming/Storming/Norming, design discovery, eng feasibility -> **Sign-Off 2** | prd-development, user research (JTBD, personas, journeys, interviews), stories/epics, design-signal, eng-feasibility-spike, tech-spec, adr, api-design |
| `3-delivery/` | Delivery (AI codes, humans review/ship) — PI Planning -> build/test/release | pi-planning, test-strategy, release-readiness, agent-docs, brand creation, UI/design + framework packs (cleanui, tailwind, Expo, NestJS), ralph |
| `4-iteration/` | Learn & Iterate + operate | learn-iterate, SaaS/finance metrics, business health, pricing, incident-postmortem, sentry-cli, eol-message |
| `growth/` | (pack, off-blueprint) | `ads-*` marketing pack, acquisition/organic growth |
| `career/` | (pack, off-blueprint) | PM career coaching |
| `utilities/` | (pack) | outlook, pdf, ffmpeg, screenshot, gpt-image, humanizer, comic-sketch-story |
| `meta/` | (pack) | find-skills, skill authoring, workshop-facilitation protocol |
| `commands/` | — | slash-command .md files (linked into both tools) |
| `retired/` | — | history only; never linked |

## Conventions (enforced by `TEMPLATE/SKILL.md`)

Choose one primary workflow for the requested output. Add a specialist only for
a distinct part of that work, and pass existing context forward instead of
repeating intake. Common overlaps are resolved as follows:

| Need | Primary skill | Adjacent scope |
|---|---|---|
| Positioning from agreed inputs | `positioning-statement` | `positioning-workshop` elicits the inputs |
| Broad alternatives before choosing | `divergent-ideation` | Domain skills own implementation; `critical-review` challenges an existing artifact |
| Customer experience map | `customer-journey-map` | `customer-journey-mapping-workshop` facilitates discovery |
| Backlog and release slices | `user-story-mapping` | `user-story-mapping-workshop` facilitates planning |
| General interface implementation | `cleanui` | `design-taste-frontend` specializes in marketing and portfolio art direction |
| Particular visual treatment | One matching style preset | Avoid stacking conflicting style presets |
| Website reference images | `imagegen-frontend-web` | `image-to-code` adds implementation; mobile concepts use `imagegen-frontend-mobile` |
| Complete identity journey | `brand-creation-studio` | `brandkit` produces a single overview board; `ads-dna` extracts an existing identity |
| Ordinary images in Codex | Built-in `imagegen` | `gpt-image` supports requested CLI/API execution or prompt-gallery consultation |
| Paid-account health review | `ads-audit` | `ads` routes broad requests; channel skills handle one platform |

Interactive skills read `workshop-facilitation` for the shared interaction
protocol and keep their own domain questions. Keep optional examples and mode
catalogs in routed references rather than copying them into every entrypoint.

- **Name:** `<domain>-<object>[-workshop|-advisor]`, kebab-case, dir name ==
  frontmatter `name`. One skill = one deliverable or one decision.
- **Description:** `"Verb the artifact… Use when <trigger>. Do NOT use for
  <adjacent case>."` Hard cap 350 chars — descriptions are
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
(agent-docs, ffmpeg-usage, humanizer, the Leonxlnx taste-skill bundle, and the
adopted community skills — tdd, diagnosing-bugs, resolving-merge-conflicts,
postgres-best-practices, mcp-builder, react-best-practices,
react-native-skills, web-design-guidelines).

## Companion tooling (per-project, not vendored here)

- **skilld** (`npx -y skilld`) — generates version-aware skills from a
  project's npm dependencies; run inside project repos, never vendor output.
- **@tanstack/intent** (`npx @tanstack/intent install`) — wires up SKILL.md
  files shipped inside npm packages (Expo, Prisma, Stripe, Vercel adopt it).
- **AWS Agent Toolkit** — `/plugin install aws-core@claude-plugins-official`,
  enabled per-project for CDK/serverless/IAM/observability work.

> Watch item: Expo now ships official intent skills — dedupe the `expo-*`
> pack against them at the next portfolio audit.
