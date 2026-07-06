#!/usr/bin/env bash
# Symlink-farm installer for the skills repo.
# Links every skill named in manifests/<tool>.txt into that tool's flat skills
# root, and every file in commands/ into the tool's commands/prompts dir.
# Existing REAL dirs/files at a target path are moved to a timestamped backup
# next to the root (never deleted); existing symlinks are replaced.
# Idempotent: re-run after adding/renaming skills or editing manifests.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STAMP="$(date +%Y%m%d-%H%M%S)"

find_skill() { # name -> repo path (domain dirs are one level deep)
  find "$REPO" -mindepth 2 -maxdepth 2 -type d -name "$1" -not -path "$REPO/.git/*" \
    -not -path "$REPO/retired/*" | head -1
}

backup() { # path, backup-root
  mkdir -p "$2"
  mv "$1" "$2/"
  echo "  backed up: $1 -> $2/"
}

link_skills() { # manifest, target-root
  local manifest="$1" target="$2" backup_root="$2.backup-$STAMP" n=0
  mkdir -p "$target"
  while IFS= read -r name; do
    [ -z "$name" ] && continue
    case "$name" in \#*) continue ;; esac
    local src; src="$(find_skill "$name")"
    if [ -z "$src" ]; then echo "  WARN: '$name' not in repo, skipped"; continue; fi
    local dest="$target/$name"
    if [ -e "$dest" ] && [ ! -L "$dest" ]; then backup "$dest" "$backup_root"; fi
    ln -sfn "$src" "$dest"
    n=$((n + 1))
  done <"$manifest"
  echo "$target: $n skills linked"
}

link_commands() { # target dir for slash-command .md files
  local target="$1" backup_root="$1.backup-$STAMP" n=0
  mkdir -p "$target"
  for f in "$REPO"/commands/*.md; do
    [ -e "$f" ] || continue
    local dest="$target/$(basename "$f")"
    if [ -e "$dest" ] && [ ! -L "$dest" ]; then backup "$dest" "$backup_root"; fi
    ln -sfn "$f" "$dest"
    n=$((n + 1))
  done
  echo "$target: $n commands linked"
}

link_skills "$REPO/manifests/claude.txt" "$HOME/.claude/skills"
link_skills "$REPO/manifests/codex.txt" "$HOME/.codex/skills"
link_commands "$HOME/.claude/commands"
link_commands "$HOME/.codex/prompts"

echo "Done. Open a fresh Claude Code / Codex session to pick up changes."
