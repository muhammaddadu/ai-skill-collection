#!/usr/bin/env bash
# Install the agent-docs skill into Claude Code and/or Codex by symlinking this
# directory into their skills folders. Idempotent: safe to re-run.
#
#   ./install.sh            # install into whichever of ~/.claude / ~/.codex exist
#
# The canonical copy stays wherever you cloned it; the tools just point at it,
# so `git pull` here updates the skill everywhere at once.
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NAME="$(basename "$SRC")"
installed=0

link_into() {
  local tool_dir="$1" label="$2"
  [ -d "$tool_dir" ] || return 0
  mkdir -p "$tool_dir/skills"
  local dest="$tool_dir/skills/$NAME"
  if [ -L "$dest" ] || [ -e "$dest" ]; then
    rm -rf "$dest"
  fi
  ln -s "$SRC" "$dest"
  echo "  ✓ $label  →  $dest"
  installed=1
}

echo "Installing '$NAME' from: $SRC"
link_into "$HOME/.claude" "Claude Code"
link_into "$HOME/.codex"  "Codex"

if [ "$installed" -eq 0 ]; then
  echo "  ! Neither ~/.claude nor ~/.codex found — nothing to link."
  echo "    Move this folder under your agent's skills dir manually."
  exit 1
fi
echo "Done. Restart your agent (or start a new session) to pick it up."
