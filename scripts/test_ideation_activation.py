"""Exercise global instruction edits in isolated homes; never touch real settings."""
import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "meta/divergent-ideation/scripts/setup_global.py"
SPEC = importlib.util.spec_from_file_location("activation", SOURCE)
activation = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(activation)


class ActivationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.home = Path(self.temporary.name).resolve()

    def run_setup(self, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            activation.configure(self.home, {}, **kwargs)

    def test_preserves_bytes_mode_and_backup_then_is_idempotent_and_reversible(self):
        path = self.home / ".claude/CLAUDE.md"
        path.parent.mkdir()
        original = b"Existing instructions\r\nwith no final newline"
        path.write_bytes(original)
        path.chmod(0o640)
        self.run_setup()
        first = path.read_bytes()
        self.assertTrue(first.endswith(original))
        self.assertEqual(path.stat().st_mode & 0o777, 0o640)
        backups = list(path.parent.glob("*.ideation-backup-*"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_bytes(), original)
        self.run_setup()
        self.assertEqual(first, path.read_bytes())
        self.assertEqual(len(list(path.parent.glob("*.ideation-backup-*"))), 1)
        self.run_setup(remove=True)
        self.assertEqual(path.read_bytes(), original)

    def test_preview_does_not_write(self):
        (self.home / ".codex").mkdir()
        self.run_setup(dry_run=True)
        self.assertEqual(list((self.home / ".codex").iterdir()), [])

    def test_detects_all_five_supported_clients_only(self):
        for name in (".codex", ".claude", ".gemini", ".config/opencode", ".cursor"):
            (self.home / name).mkdir(parents=True)
        self.run_setup()
        for _, _, path, _ in activation.targets(self.home, {}):
            self.assertIn(activation.START.encode(), path.read_bytes())
        self.assertEqual(len(activation.targets(self.home, {})), 5)
        self.assertFalse((self.home / ".unknown-ai").exists())

    def test_uninstalled_clients_are_not_created(self):
        self.run_setup()
        self.assertEqual(list(self.home.iterdir()), [])

    def test_malformed_markers_preflight_before_any_writes(self):
        (self.home / ".codex").mkdir()
        bad = self.home / ".claude/CLAUDE.md"
        bad.parent.mkdir()
        bad.write_text(activation.START)
        with self.assertRaises(ValueError):
            self.run_setup()
        self.assertFalse((self.home / ".codex/AGENTS.md").exists())

    def test_symlink_is_rejected_and_target_preserved(self):
        external = self.home / "original.md"
        external.write_text("Keep this")
        (self.home / ".codex").mkdir()
        (self.home / ".codex/AGENTS.md").symlink_to(external)
        with self.assertRaises(ValueError):
            self.run_setup()
        self.assertEqual(external.read_text(), "Keep this")

    def test_cursor_rule_remove_and_reinstall(self):
        (self.home / ".cursor").mkdir()
        self.run_setup()
        path = self.home / ".cursor/rules/divergent-ideation.mdc"
        self.assertTrue(path.read_text().startswith("---\n"))
        self.run_setup(remove=True)
        self.assertEqual(path.read_bytes(), b"")
        self.run_setup(remove=True)
        self.run_setup()
        self.assertTrue(path.read_text().startswith("---\n"))

    def test_environment_overrides_select_effective_roots(self):
        custom = self.home / "custom-codex"
        custom.mkdir()
        result = activation.targets(self.home, {"CODEX_HOME": str(custom)})
        self.assertEqual(result[0][2], custom / "AGENTS.md")

    def test_upgrade_existing_managed_rule_preserves_surrounding_bytes(self):
        path = self.home / ".codex/AGENTS.md"
        path.parent.mkdir()
        prefix = b"Prior user preferences\r\n\r\n"
        suffix = b"Other project guidance\n"
        old = (activation.START + "\nOld activation policy\n" + activation.END + "\n\n").encode()
        path.write_bytes(prefix + old + suffix)
        self.run_setup()
        updated = path.read_bytes()
        self.assertTrue(updated.startswith(prefix))
        self.assertTrue(updated.endswith(suffix))
        self.assertNotIn(b"Old activation policy", updated)
        self.assertEqual(updated.count(activation.START.encode()), 1)
        # The installed policy points to both real, readable resources.
        skill = SOURCE.parents[1] / "SKILL.md"
        visual = skill.parents[2] / "3-delivery/cleanui/references/visual-refinement.md"
        for resource in (skill, visual):
            self.assertTrue(resource.is_file())
            self.assertIn(resource.as_posix().encode(), updated)
        self.run_setup()
        self.assertEqual(path.read_bytes(), updated)
        self.run_setup(remove=True)
        self.assertEqual(path.read_bytes(), prefix + suffix)

    def test_standalone_setup_rejects_missing_visual_reference(self):
        fake_skill = self.home / "meta/divergent-ideation/SKILL.md"
        with self.assertRaises(ValueError):
            activation.rule(fake_skill)
        self.assertEqual(list(self.home.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
