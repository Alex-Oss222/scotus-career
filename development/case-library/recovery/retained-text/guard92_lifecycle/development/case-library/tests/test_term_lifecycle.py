"""Full-term publication must preserve reviewed inputs and fail recoverably.

These tests use disposable repository copies. Rehashed fixtures model repaired
or buggy generated output; agreeing checksums alone must not make that output
override the separately reviewed mappings.
"""
from __future__ import annotations

from copy import deepcopy
import json
import os
from pathlib import Path
import unittest
from unittest.mock import patch

from jsonschema import ValidationError

import test_term_catalogue as fixtures


pilot = fixtures.pilot
CATALOGUE = fixtures.CATALOGUE


class TermLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.TermCatalogueTests(methodName="runTest")
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()
        self.root = self.fixture.root
        self.folder = self.fixture.folder
        self.pointer_path = self.fixture.pointer_path
        self.selection_path = self.fixture.selection_path
        self.historical_path = self.fixture.historical_path

    def build_and_load(self):
        return self.fixture.build_and_load()

    def current_bytes(self):
        return self.fixture.current_bytes()

    def curated_bytes(self):
        return {path: path.read_bytes()
                for path in (self.selection_path, self.historical_path)}

    def change_reviewed_alias(self):
        selection = self.fixture.read_selection()
        selection["cases"][0]["aliases"].append("Reviewed lifecycle update")
        self.fixture.write_json(self.selection_path, selection)

    def rehash_snapshot(self, folder, *, update_pointer):
        manifest_path = folder / "artifacts.json"
        manifest = json.loads(manifest_path.read_bytes())
        for relative in manifest:
            manifest[relative] = pilot.digest((folder / relative).read_bytes())
        manifest_path.write_bytes(pilot.json_bytes(manifest))
        if update_pointer:
            self.pointer_path.write_bytes(pilot.json_bytes({
                "build_id": folder.name,
                "artifacts_sha256": pilot.digest(manifest_path.read_bytes()),
            }))

    def inject_consistent_unreviewed_alias(self, folder, *, update_pointer):
        """Keep generated views and hashes consistent with an unreviewed edit."""
        paths = sorted((folder / "entries").glob("*.json"))
        entries = [json.loads(path.read_bytes()) for path in paths]
        entries[0]["curated"]["aliases"].append("Unreviewed generated alias")
        paths[0].write_bytes(pilot.json_bytes(entries[0]))
        report = json.loads((folder / "report.json").read_bytes())
        rendered = pilot.render_files(entries, report, os.path.relpath(self.root, folder))
        for relative, content in rendered.items():
            (folder / relative).write_text(content)
        self.rehash_snapshot(folder, update_pointer=update_pointer)
        return paths[0], paths[0].read_bytes()

    def test_self_consistent_orphan_cannot_override_reviewed_inputs_and_recovers(self):
        old_folder, _, _ = self.build_and_load()
        previous = self.current_bytes()
        self.change_reviewed_alias()
        curator_bytes = self.curated_bytes()
        original_atomic = pilot.atomic_file

        def interrupt_before_pointer(path, data):
            if Path(path) == self.pointer_path:
                raise OSError("Injected full-term pointer interruption")
            return original_atomic(path, data)

        with patch.object(pilot, "atomic_file", side_effect=interrupt_before_pointer):
            with self.assertRaises((pilot.PilotError, OSError)):
                pilot.build(self.root, catalogue=CATALOGUE)
        self.assertEqual(self.current_bytes(), previous)
        orphans = [path for path in (self.folder / "builds").iterdir() if path != old_folder]
        self.assertEqual(len(orphans), 1)
        orphan, = orphans
        damaged_entry, damaged_bytes = self.inject_consistent_unreviewed_alias(
            orphan, update_pointer=False)

        with self.assertRaises(pilot.PilotError):
            pilot.build(self.root, catalogue=CATALOGUE)
        self.assertEqual(self.current_bytes(), previous)
        self.assertEqual(damaged_entry.read_bytes(), damaged_bytes)

        fresh, _, _ = pilot.build(self.root, catalogue=CATALOGUE, recover=True)
        self.assertNotIn(fresh, (old_folder, orphan))
        _, restored, report = pilot.load_snapshot(self.root, catalogue=CATALOGUE)
        self.assertEqual((len(restored), report["event_count"]), (124, 125))
        self.assertEqual(len(pilot.lookup(restored, "Reviewed lifecycle update")), 1)
        self.assertEqual(pilot.lookup(restored, "Unreviewed generated alias"), [])
        self.assertEqual(damaged_entry.read_bytes(), damaged_bytes)
        self.assertEqual(self.curated_bytes(), curator_bytes)
        self.assertTrue(any(path.read_bytes() == previous
                            for path in (self.folder / "recovery").rglob("*") if path.is_file()))

    def test_self_consistent_current_snapshot_cannot_override_reviewed_inputs(self):
        folder, _, _ = self.build_and_load()
        curator_bytes = self.curated_bytes()
        damaged_entry, damaged_bytes = self.inject_consistent_unreviewed_alias(
            folder, update_pointer=True)
        previous = self.current_bytes()
        with self.assertRaises(pilot.PilotError):
            pilot.build(self.root, catalogue=CATALOGUE)
        self.assertEqual(self.current_bytes(), previous)
        self.assertEqual(damaged_entry.read_bytes(), damaged_bytes)
        self.assertEqual(self.curated_bytes(), curator_bytes)

    def test_rehashed_generated_card_and_html_must_agree_with_snapshot_entries(self):
        folder, entries, _ = self.build_and_load()
        for relative in (f"cards/{entries[0]['case_id']}.md", "index.html"):
            with self.subTest(artifact=relative):
                path = folder / relative
                original = path.read_bytes()
                damaged = original + b"\nUnreviewed generated presentation fixture.\n"
                path.write_bytes(damaged)
                self.rehash_snapshot(folder, update_pointer=True)
                previous = self.current_bytes()
                try:
                    with self.assertRaises(pilot.PilotError):
                        pilot.load_snapshot(self.root, catalogue=CATALOGUE)
                    with self.assertRaises(pilot.PilotError):
                        pilot.build(self.root, catalogue=CATALOGUE)
                    self.assertEqual(self.current_bytes(), previous)
                    self.assertEqual(path.read_bytes(), damaged)
                finally:
                    path.write_bytes(original)
                    self.rehash_snapshot(folder, update_pointer=True)
        pilot.load_snapshot(self.root, catalogue=CATALOGUE)

    def test_record_membership_change_at_publication_rolls_back_full_term_pointer(self):
        old_folder, entries, _ = self.build_and_load()
        previous = self.current_bytes()
        self.change_reviewed_alias()
        curator_bytes = self.curated_bytes()
        source = self.root / entries[0]["curated"]["simulation"]["events"][0]["record"]["repository_path"]
        added = self.root / "terms/OT1991/records/lifecycle_unreviewed_event.md"
        original_atomic = pilot.atomic_file
        injected = False

        def add_record_before_publication(path, data):
            nonlocal injected
            if Path(path) == self.pointer_path and not injected:
                injected = True
                added.write_bytes(source.read_bytes())
            return original_atomic(path, data)

        with patch.object(pilot, "atomic_file", side_effect=add_record_before_publication):
            with self.assertRaisesRegex(pilot.PilotError, "Record inventory changed"):
                pilot.build(self.root, catalogue=CATALOGUE)
        self.assertTrue(injected)
        self.assertEqual(self.current_bytes(), previous)
        preserved, _, _ = pilot.load_snapshot(self.root, check_sources=False, catalogue=CATALOGUE)
        self.assertEqual(preserved, old_folder)
        self.assertEqual(added.read_bytes(), source.read_bytes(),
                         "Publication rollback must preserve concurrent authoritative-source additions")
        self.assertEqual(self.curated_bytes(), curator_bytes)

    def test_unborn_git_head_refuses_cli_build_without_traceback_or_pointer_change(self):
        self.build_and_load()
        previous = self.current_bytes()
        before_builds = set((self.folder / "builds").iterdir())
        (self.root / ".git/HEAD").write_text("ref: refs/heads/unborn-lifecycle-fixture\n")
        result = self.fixture.cli("build")
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("Pilot error:", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(self.current_bytes(), previous)
        self.assertEqual(set((self.folder / "builds").iterdir()), before_builds)

    def test_null_live_case_name_refuses_cleanly_after_rehash(self):
        folder, entries, _ = self.build_and_load()
        changed = deepcopy(entries[0])
        changed["curated"]["case_name"] = None
        path = folder / "entries" / f"{changed['case_id']}.json"
        path.write_bytes(pilot.json_bytes(changed))
        self.rehash_snapshot(folder, update_pointer=True)
        previous = self.current_bytes()
        with self.assertRaises((pilot.PilotError, ValidationError)):
            pilot.load_snapshot(self.root, catalogue=CATALOGUE)
        result = self.fixture.cli("validate")
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("Pilot error:", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        with self.assertRaises(pilot.PilotError):
            pilot.build(self.root, catalogue=CATALOGUE)
        self.assertEqual(self.current_bytes(), previous)


if __name__ == "__main__":
    unittest.main()
