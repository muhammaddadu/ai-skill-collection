#!/usr/bin/env python3
"""Lint the skills repo against the conventions in README.md.

Checks:
  1. every skill dir has SKILL.md with frontmatter `name` == directory name
  2. description present and <= 500 chars (ads-* pack allowlisted: its
     keyword-exhaustive descriptions are that pack's own convention)
  3. no absolute skill-root paths in SKILL.md / references (breaks the other
     tool's install; install-location docs are allowlisted)
  4. no cross-directory `../<skill>` path references (use the skill name;
     path refs are allowed only between skills in the same phase/pack dir)
  5. manifests resolve: every entry names exactly one real skill dir
  6. no duplicate skill names across domains

Exit 0 clean, 1 on any failure. Run from anywhere: `python3 scripts/lint.py`.
"""

import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAINS = [
    "1-exploration", "2-discovery", "3-delivery", "4-iteration",
    "growth", "career", "utilities", "meta",
]
DESC_CAP = 500
DESC_CAP_ALLOWLIST = re.compile(r"^growth/ads(-|/)")  # pack-level convention
ABS_PATH = re.compile(r"(/Users/[a-z]+/|~/\.claude/skills|~/\.codex/skills|~/\.agents/)")
ABS_PATH_ALLOWLIST = {  # install-location documentation, not runtime references
    "3-delivery/agent-docs/SKILL.md",
    "3-delivery/agent-docs/README.md",
    "utilities/ffmpeg-usage/README.md",
    "utilities/ffmpeg-usage/AGENTS.md",
    "utilities/humanizer/README.md",
    "utilities/pdf/SKILL.md",
    "utilities/screenshot/SKILL.md",
}
CROSS_REF = re.compile(r"\.\./([a-z0-9][a-z0-9-]*)\b")
NON_SKILL_REF = {"references", "data", "scripts", "assets", "docs", "src",
                 "components", "images", "utils"}


def frontmatter(path):
    fields = {}
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except OSError:
        return fields
    if not lines or lines[0].strip() != "---":
        return fields
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^(name|description):\s*(.*)$", line)
        if m:
            fields[m.group(1)] = m.group(2).strip().strip('"')
    return fields


def main():
    errors = []
    skill_domain = {}

    # discover real skills (bridges are symlinks and skipped)
    for d in DOMAINS:
        droot = os.path.join(REPO, d)
        if not os.path.isdir(droot):
            continue
        for s in sorted(os.listdir(droot)):
            sdir = os.path.join(droot, s)
            if not os.path.isdir(sdir) or os.path.islink(sdir):
                continue
            if s in skill_domain:
                errors.append(f"duplicate skill name: {s} in {d} and {skill_domain[s]}")
            skill_domain[s] = d

            rel = f"{d}/{s}/SKILL.md"
            sk = os.path.join(sdir, "SKILL.md")
            if not os.path.isfile(sk):
                errors.append(f"missing SKILL.md: {d}/{s}")
                continue
            fm = frontmatter(sk)
            if fm.get("name") != s:
                errors.append(f"name mismatch: {rel} name='{fm.get('name')}' dir='{s}'")
            desc = fm.get("description", "")
            if not desc or desc in ("|", ">", "|-", ">-"):
                errors.append(f"missing/multiline description: {rel} (single-line required)")
            elif len(desc) > DESC_CAP and not DESC_CAP_ALLOWLIST.match(f"{d}/{s}"):
                errors.append(f"description {len(desc)}ch > {DESC_CAP}: {rel}")

    # content checks: absolute paths + cross-domain refs need bridges
    for s, d in skill_domain.items():
        sdir = os.path.join(REPO, d, s)
        for root, dirs, files in os.walk(sdir):
            for f in files:
                if not f.endswith(".md"):
                    continue
                path = os.path.join(root, f)
                rel = os.path.relpath(path, REPO)
                text = open(path, encoding="utf-8", errors="ignore").read()
                if ABS_PATH.search(text) and rel not in ABS_PATH_ALLOWLIST:
                    errors.append(f"absolute skill-root path in {rel}")
                for m in CROSS_REF.finditer(text):
                    t = m.group(1)
                    if t in NON_SKILL_REF or t in DOMAINS:
                        continue
                    td = skill_domain.get(t)
                    if td and td != d:
                        errors.append(f"cross-directory path ref: {rel} -> ../{t} (reference cross-directory skills by name in backticks, paths only within the same phase/pack dir)")

    # manifests resolve
    for mf in ("claude", "codex"):
        mpath = os.path.join(REPO, "manifests", f"{mf}.txt")
        seen = set()
        for line in open(mpath, encoding="utf-8"):
            name = line.strip()
            if not name or name.startswith("#"):
                continue
            if name in seen:
                errors.append(f"duplicate manifest entry: {name} in {mf}.txt")
            seen.add(name)
            if name not in skill_domain:
                errors.append(f"manifest entry has no skill dir: {name} ({mf}.txt)")

    if errors:
        print(f"LINT FAILED — {len(errors)} error(s):")
        for e in errors:
            print(f"  ✗ {e}")
        return 1
    print(f"lint clean: {len(skill_domain)} skills, both manifests resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
