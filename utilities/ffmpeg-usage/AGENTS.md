# AGENTS.md

Guidance for AI agents (and humans) working *on* this repository. If you're an
agent that has *installed* the skill and want to run ffmpeg, read `SKILL.md`
instead — that's the recipe library. This file is about maintaining the repo.

## What this is

A single-skill repo. The deliverable is `SKILL.md`: a markdown library of vetted
ffmpeg recipes plus the rules an agent follows when choosing and running them.
Everything else exists to ship, install, or verify that file.

## Layout

| Path | Purpose |
| --- | --- |
| `SKILL.md` | The skill itself — recipes + agent guidelines. The product. |
| `README.md` | Human-facing overview, quickstart, multi-agent install table. |
| `install.sh` | Intelligent installer; detects agents and writes to each. |
| `validate.js` | `node validate.js` — checks ffmpeg, probes capabilities, writes a report. |
| `LICENSE` | MIT. |

## How installation works

`install.sh` auto-detects each agent by its config directory or its CLI on
`PATH`, then installs to the right place:

| Agent | Destination | Form |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/ffmpeg-usage/` | whole folder |
| Codex CLI | `~/.codex/skills/ffmpeg-usage/` | whole folder |
| Cursor | `~/.cursor/rules/ffmpeg-usage.md` | flattened `SKILL.md` |

To add another agent, append one line to the `AGENTS` registry near the top of
`install.sh`: `name|marker_dir|marker_cli|dest_kind|dest_path`, where
`dest_kind` is `skill` (copy the folder) or `rule` (copy `SKILL.md` only). Then
add the matching target to `checkSkillInstallation()` in `validate.js` and a row
to the table in `README.md`.

## Conventions

- **`SKILL.md` is agent-neutral.** Never write "Claude should…"; say "the agent".
  It's consumed by multiple tools and gets flattened into Cursor rules verbatim.
- **British English** in all prose (optimise, normalise, colour, licence as noun).
- **Token-frugal.** `SKILL.md` loads into an agent's context, so keep prose tight
  and let the commands carry the weight. Don't pad.
- **Commands must be correct and runnable** — they're the whole point. If you
  change one, test it against a real file before committing.
- **No external dependencies.** `install.sh` is POSIX-friendly bash; `validate.js`
  uses only Node's standard library. Keep it that way.

## Before you commit

```bash
bash -n install.sh     # shell syntax
node --check validate.js   # JS syntax
node validate.js       # full check on this machine
```

Then sanity-check the installer without touching your real home:

```bash
HOME=$(mktemp -d) bash install.sh --all   # should write into the temp HOME
```

## Out of scope

This repo ships recipes, not a media pipeline. Don't add a CLI wrapper, a build
step, or runtime dependencies. If a recipe is genuinely useful and correct, it
belongs in `SKILL.md`; if it's niche, leave it out to keep context small.
