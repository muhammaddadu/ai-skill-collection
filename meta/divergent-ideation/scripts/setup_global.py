#!/usr/bin/env python3
"""Maintain one reversible ideation rule in detected clients' global instructions."""
import argparse
import os
from pathlib import Path
import stat
import tempfile
import uuid

START = "<!-- skills:divergent-ideation:start -->"
END = "<!-- skills:divergent-ideation:end -->"


def rule(skill):
    visual_review = skill.parents[2] / "3-delivery/cleanui/references/visual-refinement.md"
    if not visual_review.is_file():
        raise ValueError(f"Shared visual-review guidance missing: {visual_review}")
    return (
        f"{START}\n"
        "## Exploring alternatives\n\n"
        "Use divergent-ideation whenever I ask for brainstorming, naming, strategy, "
        "design alternatives, or help choosing between approaches. Apply it before "
        "recommending a solution. For simple factual questions or routine edits, "
        "respond directly. Honor explicit requests for a quick or conventional answer.\n\n"
        f"Read the skill at {skill.as_posix()} when it applies. Generate distinct "
        "approaches before judging them, group by mechanism, identify attractive traps, "
        "and recommend a practical shortlist with the next useful experiment. "
        "Retain a conventional baseline and existing constraints. Use isolated agent "
        "branches only when available and authorized; otherwise use a single-session "
        "pass. Keep the effort proportionate and preserve the task's human decision gates.\n"
        "\n## Substantial visual work\n\n"
        "Establish the intended experience, explore distinct directions when needed, "
        "inspect the rendered result, refine against concrete references, and remove "
        "unnecessary elements. Use the relevant design skill and scale the process to "
        "the task; preserve existing design systems and accessibility. "
        f"Read the shared review procedure at {visual_review.as_posix()} for substantial "
        "visual creation or redesign. Keep critique grounded in visible evidence, "
        "use bounded iteration, and verify working behavior separately from appearance.\n"
        f"{END}\n\n"
    ).encode()


def managed_content(original, block, remove=False):
    start, end = START.encode(), END.encode()
    if original.count(start) != original.count(end) or original.count(start) > 1:
        raise ValueError("Malformed or duplicate managed markers; repair before updating")
    if start not in original:
        return original if remove else block + original
    first, last = original.index(start), original.index(end)
    if last < first:
        raise ValueError("Managed markers are out of order")
    stop = last + len(end)
    # Only consume the separator that this installer owns.
    if original[stop:stop + 2] == b"\n\n":
        stop += 2
    elif original[stop:stop + 1] == b"\n":
        stop += 1
    return original[:first] + (b"" if remove else block) + original[stop:]


def safe_path(path):
    for part in (path, *path.parents):
        if part.is_symlink():
            raise ValueError(f"Refusing symlink instruction path: {part}")
    if path.exists() and not path.is_file():
        raise ValueError(f"Not a regular instruction file: {path}")


def targets(home, environment):
    def root(key, default):
        return Path(environment.get(key) or default).expanduser().absolute()

    codex = root("CODEX_HOME", home / ".codex")
    claude = root("CLAUDE_CONFIG_DIR", home / ".claude")
    gemini = root("GEMINI_CLI_HOME", home) / ".gemini"
    opencode = root("OPENCODE_CONFIG_DIR", root("XDG_CONFIG_HOME", home / ".config") / "opencode")
    candidates = [
        ("Codex", codex, codex / "AGENTS.md", b""),
        ("Claude Code", claude, claude / "CLAUDE.md", b""),
        ("Gemini CLI", gemini, gemini / "GEMINI.md", b""),
        ("OpenCode", opencode, opencode / "AGENTS.md", b""),
        ("Cursor", home / ".cursor", home / ".cursor/rules/divergent-ideation.mdc",
         b"---\ndescription: Explore alternatives before recommending a solution\nalwaysApply: true\n---\n\n"),
    ]
    return [item for item in candidates if item[1].is_dir()]


def configure(home, environment, dry_run=False, remove=False):
    skill = Path(__file__).resolve().parents[1] / "SKILL.md"
    if not skill.is_file():
        raise ValueError(f"Skill source missing: {skill}")
    plan = []
    for client, _, path, header in targets(home, environment):
        safe_path(path)
        original = path.read_bytes() if path.exists() else None
        if header and original and START.encode() not in original:
            raise ValueError(f"Refusing to replace an unmanaged dedicated rule: {path}")
        updated = managed_content(original or b"", rule(skill), remove)
        if header:
            if remove and updated == header:
                updated = b""
            elif not original and not remove:
                updated = header + updated
        plan.append((client, path, original, updated))

    for client, path, original, updated in plan:
        if updated == (original or b""):
            print(f"{client}: unchanged ({path})")
            continue
        print(f"{client}: {'would update' if dry_run else 'updating'} {path}")
        if dry_run:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        safe_path(path)
        mode = stat.S_IMODE(path.stat().st_mode) if original is not None else 0o600
        descriptor, temporary = tempfile.mkstemp(prefix=".ideation-", dir=path.parent)
        try:
            with os.fdopen(descriptor, "wb") as output:
                output.write(updated)
                output.flush()
                os.fsync(output.fileno())
            os.chmod(temporary, mode)
            current = path.read_bytes() if path.exists() else None
            if current != original:
                raise ValueError(f"Instructions changed during setup; retry: {path}")
            if original is not None:
                backup = path.with_name(path.name + f".ideation-backup-{uuid.uuid4().hex}")
                with backup.open("xb") as output:
                    os.chmod(backup, mode)
                    output.write(original)
                print(f"  Backup: {backup}")
            os.replace(temporary, path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
    print("Local rules only: Claude Desktop, ChatGPT, and browser-only clients need app/project instructions.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--remove", action="store_true", help="Remove only the managed rule")
    parser.add_argument("--home", type=Path, default=Path.home(), help="Home directory to inspect")
    args = parser.parse_args()
    try:
        configure(args.home.absolute(), os.environ, args.dry_run, args.remove)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Ideation setup failed: {error}\n")


if __name__ == "__main__":
    main()
