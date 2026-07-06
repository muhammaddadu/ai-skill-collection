# ffmpeg-usage

An agent skill for making polished videos with ffmpeg — not just running commands. It pairs a library of vetted ffmpeg recipes (conversion, scaling, GIFs, audio, subtitles, presets) with a reusable production pipeline: story beats, scene composition, animated captions, device/product framing, voiceover and music, and platform-ready export. Built for demos, ads, tutorials, launches, social clips, explainers, app-store previews, and pitches. Works with **Claude Code, Codex CLI, Cursor**, and anything else that reads a skills or rules directory.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Quickstart

One command. It detects every AI agent on your machine and installs the skill into each:

```bash
curl -sSL https://raw.githubusercontent.com/muhammaddadu/ffmpeg-skill/main/install.sh | bash
```

Then restart your agent and ask it to do something with a video. If an agent doesn't pick the skill up on its own, name it: *"use the ffmpeg-usage skill."*

Already cloned the repo? Run `./install.sh` from inside it — same behaviour, no download.

## How it works (30 seconds)

The skill is just markdown: `SKILL.md` holds a library of vetted ffmpeg recipes plus the rules an agent follows when choosing and running them. The installer copies that into wherever each agent looks for skills. No daemon, no dependency beyond ffmpeg itself.

The value isn't the commands — your agent already knows ffmpeg — it's the judgement baked in: sane CRF defaults, the two-pass palette GIF pipeline that actually looks decent, `+faststart` on web output, and aspect-correct presets per platform.

## Multi-agent install

The installer auto-detects what's present and writes to the right place for each:

| Agent | Installed to |
| --- | --- |
| Claude Code | `~/.claude/skills/ffmpeg-usage/` |
| Codex CLI | `~/.codex/skills/ffmpeg-usage/` |
| Cursor | `~/.cursor/rules/ffmpeg-usage.md` |

Detection keys off each agent's config directory or CLI on your `PATH`. Useful flags:

```bash
./install.sh              # detect and install into every agent found
./install.sh --all        # install into all supported agents, detected or not
./install.sh --only codex # target a single agent
./install.sh --uninstall  # remove from everywhere
```

## What it covers

**Recipes:** conversion (MP4/WebM/MOV/AVI) · scaling with letterbox padding · palette GIFs · audio extraction, mixing, backing tracks · trim/concat/speed/rotate · subtitle burn-in, soft subs, extraction · thumbnails · compression and web optimisation · YouTube/Instagram/TikTok/X presets.

**Production pipeline:** story beats · scene-by-scene composition · animated text and captions · device/product/mockup framing · voiceover, music, ducking, and loudness · motion (push-in, parallax, Ken Burns, eased transitions) · `ffprobe` QA and preview frames · a "Useful Libraries and Tools" guide (Pillow, Remotion, Blender, OpenCV, Whisper, TTS) with selection rules for when ffmpeg alone isn't enough.

| You say | What you get |
| --- | --- |
| "Convert this MOV to MP4" | H.264 + AAC, balanced quality |
| "5-second GIF from 0:10" | Palette pipeline, trimmed |
| "4K down to 1080p for web" | Scaled with `+faststart` |
| "Pull the audio as MP3" | High-quality VBR extraction |
| "Prep for Instagram Stories" | 9:16 padded fit, capped at 15s |
| "Convert every MOV here to MP4" | Batch loop over the folder |

## Requirements

- **ffmpeg ≥ 4.0** (ships with `ffprobe`). The installer warns if it's missing but won't block.
  ```bash
  brew install ffmpeg                                  # macOS
  sudo apt-get update && sudo apt-get install ffmpeg   # Debian/Ubuntu
  choco install ffmpeg                                 # Windows
  ```
- An agent that reads skills/rules: Claude Code, Codex CLI, Cursor, or similar. Hosted Claude (Desktop / claude.ai) takes the skill as an uploaded zip — **Settings → Capabilities → Skills → Upload Skill** — and needs a Pro/Max/Team/Enterprise plan.

## Documentation

- **[SKILL.md](SKILL.md)** — the recipe library your agent reads, plus the rules it follows. This is the single source of truth.
- **[validate.js](validate.js)** — `node validate.js` checks ffmpeg/ffprobe, probes capabilities, and reports your setup.
- **[AGENTS.md](AGENTS.md)** — notes for AI agents and contributors working in this repo.

## Make it yours

Recipes are plain markdown, so editing *is* the customisation. Add presets, change the default CRF, drop in your own filters:

````markdown
### Logo overlay (bottom-right)
```bash
ffmpeg -i video.mp4 -i logo.png \
  -filter_complex "overlay=W-w-10:H-h-10" output.mp4
```
````

## Safety

This runs ffmpeg against your local files. Read the command before it runs, only point it at files you trust, and watch for paths that escape your working directory.

## License

MIT — see [LICENSE](LICENSE).
