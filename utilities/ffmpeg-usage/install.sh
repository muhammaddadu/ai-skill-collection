#!/usr/bin/env bash
#
# ffmpeg-usage installer
# Auto-detects every AI coding agent on your machine and installs the skill
# into each one. Supports Claude Code, Codex CLI, Cursor, and anything else
# that reads a skills/ or rules/ directory.

set -euo pipefail

SKILL_NAME="ffmpeg-usage"
REPO_URL="https://github.com/muhammaddadu/ffmpeg-skill.git"

# --- output helpers ---------------------------------------------------------
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; BLUE='\033[0;34m'; NC='\033[0m'
ok()   { echo -e "${GREEN}✓${NC} $1"; }
err()  { echo -e "${RED}✗${NC} $1"; }
warn() { echo -e "${YELLOW}⚠${NC} $1"; }
info() { echo -e "${BLUE}ℹ${NC} $1"; }
banner() { echo; echo -e "${BLUE}── ffmpeg-usage installer ──${NC}"; echo; }

# --- agent registry ---------------------------------------------------------
# Each agent: a label, a marker (config dir or CLI) that means "installed",
# and a destination. "skill" dests get the whole folder; "rule" dests get a
# single flattened markdown file.
#
# name | marker_dir | marker_cli | dest_kind | dest_path
AGENTS=(
  "Claude Code|$HOME/.claude|claude|skill|$HOME/.claude/skills/$SKILL_NAME"
  "Codex CLI|$HOME/.codex|codex|skill|$HOME/.codex/skills/$SKILL_NAME"
  "Cursor|$HOME/.cursor|cursor|rule|$HOME/.cursor/rules/$SKILL_NAME.md"
)

FORCE_ALL=0
ONLY=""

usage() {
  cat <<EOF
ffmpeg-usage installer

Usage: install.sh [options]

  (no options)   Detect installed agents and install into each.
  --all          Install into every supported agent, detected or not.
  --only NAME    Install only into NAME (claude|codex|cursor).
  --uninstall    Remove the skill from every agent.
  -h, --help     Show this help.
EOF
}

agent_present() {  # marker_dir, marker_cli
  [ -d "$1" ] && return 0
  command -v "$2" >/dev/null 2>&1 && return 0
  return 1
}

# --- locate the source files ------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || true)"
SRC=""; TMP=""
resolve_source() {
  if [ -n "$SCRIPT_DIR" ] && [ -f "$SCRIPT_DIR/SKILL.md" ]; then
    SRC="$SCRIPT_DIR"
    info "Installing from local checkout: $SRC"
  else
    TMP="$(mktemp -d)"
    info "Fetching $SKILL_NAME from GitHub…"
    git clone --depth 1 "$REPO_URL" "$TMP" >/dev/null 2>&1 || { err "Clone failed."; exit 1; }
    SRC="$TMP"
  fi
}
cleanup() { [ -n "$TMP" ] && rm -rf "$TMP"; }
trap cleanup EXIT

# --- install one agent ------------------------------------------------------
same_path() {  # a, b — true if both resolve to the same location
  [ "$(cd "$1" 2>/dev/null && pwd -P || echo a)" = "$(cd "$2" 2>/dev/null && pwd -P || echo b)" ]
}
install_skill() {  # dest_dir
  local dest="$1"
  if [ -d "$dest" ] && same_path "$SRC" "$dest"; then
    info "Source already lives at $dest — nothing to copy."; return 0
  fi
  mkdir -p "$dest"
  cp -R "$SRC"/. "$dest"/
  rm -rf "$dest/.git"
}
install_rule() {  # dest_file — flatten the skill to a single rules doc
  local dest="$1"
  mkdir -p "$(dirname "$dest")"
  cp "$SRC/SKILL.md" "$dest"
}

uninstall_one() {  # dest_kind, dest_path
  if [ "$1" = "skill" ]; then [ -d "$2" ] && rm -rf "$2" && return 0
  else [ -f "$2" ] && rm -f "$2" && return 0; fi
  return 1
}

# --- ffmpeg check -----------------------------------------------------------
check_ffmpeg() {
  if command -v ffmpeg >/dev/null 2>&1; then
    ok "ffmpeg: $(ffmpeg -version | head -n1)"
  else
    warn "ffmpeg not found — the skill needs it at runtime."
    echo "    macOS:  brew install ffmpeg"
    echo "    Debian: sudo apt-get install ffmpeg"
    echo "    Windows: choco install ffmpeg"
  fi
}

# --- argument parsing -------------------------------------------------------
ACTION="install"
while [ $# -gt 0 ]; do
  case "$1" in
    --all) FORCE_ALL=1 ;;
    --only) ONLY="${2:-}"; shift ;;
    --uninstall) ACTION="uninstall" ;;
    -h|--help) usage; exit 0 ;;
    *) err "Unknown option: $1"; usage; exit 1 ;;
  esac
  shift
done

# --- run --------------------------------------------------------------------
banner

if [ "$ACTION" = "uninstall" ]; then
  removed=0
  for entry in "${AGENTS[@]}"; do
    IFS='|' read -r name _ _ kind path <<< "$entry"
    if uninstall_one "$kind" "$path"; then ok "Removed from $name ($path)"; removed=1; fi
  done
  [ "$removed" = 0 ] && warn "Nothing to remove."
  exit 0
fi

check_ffmpeg
echo
resolve_source

installed=0
for entry in "${AGENTS[@]}"; do
  IFS='|' read -r name mdir mcli kind path <<< "$entry"

  # Decide whether to target this agent.
  if [ -n "$ONLY" ]; then
    echo "$name" | grep -iq "$ONLY" || continue
  elif [ "$FORCE_ALL" = 0 ]; then
    agent_present "$mdir" "$mcli" || { info "Skipping $name (not detected)."; continue; }
  fi

  if [ "$kind" = "skill" ]; then install_skill "$path"; else install_rule "$path"; fi
  ok "$name → $path"
  installed=$((installed + 1))
done

echo
if [ "$installed" = 0 ]; then
  warn "No agents installed. Re-run with --all to force, or --only NAME."
  exit 1
fi
ok "Done — $installed agent(s) configured. Restart your agent to load the skill."
