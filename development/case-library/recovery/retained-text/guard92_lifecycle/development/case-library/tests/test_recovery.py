"""Failure injection for snapshot publication and explicit recovery.

All mutation targets are temporary copies. These checks do not repair or modify
the repository's real pilot, curated manifests, or authoritative source files.
"""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import unittest
from unittest.mock import patch

from jsonschema import ValidationError

import test_pilot as fixture_module


pilot = fixture_module.pilot


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        # Compose the existing fixture rather than inheriting its test methods.
        self.fixture = fixture_module.PilotTests(methodName="runTest")
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()
        self.root = self.fixture.root
        self.selection_path = self.fixture.selection_path
        self.historical_path = self.fixture.historical_path
        self.pilot_folder = self.root / pilot.PILOT
        self.pointer_path = self.pilot_folder / "CURRENT.json"

    def build_and_load(self):
        return self.fixture.build_and_load()

    def current_bytes(self):
        return self.fixture.current_bytes()

    def change_curated_alias(self, alias="Recovery fixture alias"):
        selection = json.loads(self.selection_path.read_text())
        selection["cases"][0]["aliases"].append(alias)
        self.fixture.write_json(self.selection_path, selection)

    def curator_bytes(self):
        return {path: path.read_bytes()
                for path in (self.selection_path, self.historical_path)}

    @staticmethod
    def file_bytes(folder):
        return {path.relative_to(folder): path.read_bytes()
                for path in folder.rglob("*") if path.is_file()}

    def assert_bytes_preserved_in_recovery(self, raw):
        recovery = self.pilot_folder / "recovery"
        self.assertTrue(recovery.is_dir(), "Recovery must retain diagnostic backups")
        self.assertTrue(any(path.read_bytes() == raw
                            for path in recovery.rglob("*") if path.is_file()),
                        "The exact damaged bytes were not retained in recovery")

    def test_interrupted_pointer_publish_preserves_previous_and_reuses_orphan(self):
        old_folder, _, _ = self.build_and_load()
        pointer = self.current_bytes()
        old_bytes = self.file_bytes(old_folder)
        previous_builds = set((self.pilot_folder / "builds").iterdir())
        self.change_curated_alias()
        curated = self.curator_bytes()
        original_atomic = pilot.atomic_file

        def interrupt_pointer(path, data):
            if Path(path) == self.pointer_path:
                raise OSError("Injected interruption before pointer publication")
            return original_atomic(path, data)

        with patch.object(pilot, "atomic_file", side_effect=interrupt_pointer):
            with self.assertRaises((OSError, pilot.PilotError)):
                pilot.build(self.root)

        self.assertEqual(self.current_bytes(), pointer)
        self.assertEqual(self.file_bytes(old_folder), old_bytes)
        orphans = set((self.pilot_folder / "builds").iterdir()) - previous_builds
        self.assertEqual(len(orphans), 1, "A promoted snapshot should survive publication failure")
        orphan, = orphans
        orphan_bytes = self.file_bytes(orphan)
        folder, _, _ = pilot.build(self.root)
        self.assertEqual(folder, orphan)
        self.assertEqual(self.file_bytes(orphan), orphan_bytes)
        _, entries, _ = pilot.load_snapshot(self.root)
        self.assertEqual(len(pilot.lookup(entries, "Recovery fixture alias")), 1)
        self.assertEqual(self.curator_bytes(), curated)

    def test_corrupt_pointer_requires_explicit_recovery_and_retains_raw_bytes(self):
        self.build_and_load()
        damaged = b'{"build_id": "broken pointer"'
        self.pointer_path.write_bytes(damaged)
        self.change_curated_alias("Revised mapping retained by recovery")
        curated = self.curator_bytes()

        with self.assertRaises((pilot.PilotError, json.JSONDecodeError)):
            pilot.build(self.root)
        self.assertEqual(self.current_bytes(), damaged)

        pilot.build(self.root, recover=True)
        _, entries, report = pilot.load_snapshot(self.root)
        self.assertEqual((len(entries), report["event_count"]), (24, 24))
        self.assertEqual(len(pilot.lookup(entries, "Revised mapping retained by recovery")), 1)
        self.assert_bytes_preserved_in_recovery(damaged)
        self.assertEqual(self.curator_bytes(), curated)

    def test_corrupt_active_card_recovers_without_destroying_damaged_snapshot(self):
        folder, entries, _ = self.build_and_load()
        pointer = self.current_bytes()
        card = folder / "cards" / f"{entries[0]['case_id']}.md"
        damaged = card.read_bytes() + b"\nInjected corruption retained for diagnosis.\n"
        card.write_bytes(damaged)
        curated = self.curator_bytes()

        with self.assertRaises(pilot.PilotError):
            pilot.build(self.root)
        self.assertEqual(self.current_bytes(), pointer)
        self.assertEqual(card.read_bytes(), damaged)

        pilot.build(self.root, recover=True)
        _, rebuilt, _ = pilot.load_snapshot(self.root)
        self.assertEqual([entry["case_id"] for entry in rebuilt],
                         [entry["case_id"] for entry in entries])
        self.assertEqual(card.read_bytes(), damaged)
        self.assert_bytes_preserved_in_recovery(pointer)
        self.assertEqual(self.curator_bytes(), curated)

    def test_recover_cli_repairs_corrupt_pointer_and_retains_backup(self):
        self.build_and_load()
        damaged = b"Invalid pointer for explicit command-line recovery\n"
        self.pointer_path.write_bytes(damaged)
        command = [sys.executable, "-B", str(self.root / pilot.AREA / "tools/pilot.py"),
                   "--root", str(self.root), "recover"]
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        _, entries, _ = pilot.load_snapshot(self.root)
        self.assertEqual(len(entries), 24)
        self.assert_bytes_preserved_in_recovery(damaged)

    def test_invalid_curated_mapping_cannot_be_bypassed_by_recovery(self):
        folder, _, _ = self.build_and_load()
        snapshot_bytes = self.file_bytes(folder)
        damaged = b"not a current pointer\n"
        self.pointer_path.write_bytes(damaged)
        selection = json.loads(self.selection_path.read_text())
        selection["cases"][0]["identity_evidence"][0]["quote"] = "Fabricated recovery evidence"
        self.fixture.write_json(self.selection_path, selection)
        curated = self.curator_bytes()

        with self.assertRaisesRegex(pilot.PilotError, "Evidence no longer matches"):
            pilot.build(self.root, recover=True)

        self.assertEqual(self.current_bytes(), damaged)
        self.assertEqual(self.curator_bytes(), curated)
        self.assertEqual(self.file_bytes(folder), snapshot_bytes)

    def test_source_change_at_pointer_publish_rolls_back_previous_pointer(self):
        old_folder, entries, _ = self.build_and_load()
        pointer = self.current_bytes()
        self.change_curated_alias()
        record = self.root / entries[0]["curated"]["simulation"]["events"][0]["record"]["repository_path"]
        original_record = record.read_bytes()
        original_atomic = pilot.atomic_file
        injected = False

        def mutate_before_pointer_publish(path, data):
            nonlocal injected
            if Path(path) == self.pointer_path and not injected:
                injected = True
                record.write_bytes(original_record + b"\n<!-- concurrent source change -->\n")
            return original_atomic(path, data)

        with patch.object(pilot, "atomic_file", side_effect=mutate_before_pointer_publish):
            with self.assertRaises(pilot.PilotError):
                pilot.build(self.root)

        self.assertTrue(injected, "The test must reach pointer publication")
        self.assertEqual(self.current_bytes(), pointer)
        preserved, _, _ = pilot.load_snapshot(self.root, check_sources=False)
        self.assertEqual(preserved, old_folder)
        self.assertNotEqual(record.read_bytes(), original_record,
                            "Rollback must not undo a concurrent authoritative-source edit")

    def test_second_builder_is_rejected_while_lock_is_held(self):
        self.build_and_load()
        pointer = self.current_bytes()
        with pilot.build_lock(self.root):
            with self.assertRaises(pilot.PilotError):
                pilot.build(self.root)
        self.assertEqual(self.current_bytes(), pointer)
        pilot.load_snapshot(self.root)

    def test_separate_process_builder_cannot_take_held_lock(self):
        self.build_and_load()
        pointer = self.current_bytes()
        command = [sys.executable, "-B", str(self.root / pilot.AREA / "tools/pilot.py"),
                   "--root", str(self.root), "build"]
        with pilot.build_lock(self.root):
            result = subprocess.run(command, capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("Another pilot build/recovery is running", result.stderr)
        self.assertEqual(self.current_bytes(), pointer)
        pilot.load_snapshot(self.root)

    def test_external_valid_pointer_replacement_is_preserved_and_reported(self):
        self.build_and_load()
        self.change_curated_alias()
        original_atomic = pilot.atomic_file
        external_pointer = None
        external_folder = None

        def replace_with_other_valid_pointer(path, data):
            nonlocal external_pointer, external_folder
            result = original_atomic(path, data)
            if Path(path) == self.pointer_path and external_pointer is None:
                published = json.loads(data)
                source_folder = self.pilot_folder / "builds" / published["build_id"]
                # An uncooperative writer redirects CURRENT to an equally valid
                # immutable snapshot after the intended pointer was published.
                external_id = pilot.digest(b"external-writer-fixture-snapshot")
                external_folder = self.pilot_folder / "builds" / external_id
                shutil.copytree(source_folder, external_folder)
                published["build_id"] = external_id
                external_pointer = pilot.json_bytes(published)
                self.pointer_path.write_bytes(external_pointer)
            return result

        with patch.object(pilot, "atomic_file", side_effect=replace_with_other_valid_pointer):
            with self.assertRaises(pilot.PilotError):
                pilot.build(self.root)

        self.assertIsNotNone(external_pointer)
        self.assertEqual(self.current_bytes(), external_pointer,
                         "An external writer's pointer must not be silently overwritten")
        folder, entries, _ = pilot.load_snapshot(self.root)
        self.assertEqual(folder, external_folder)
        self.assertEqual(len(pilot.lookup(entries, "Recovery fixture alias")), 1)

    def test_lock_is_released_after_exception(self):
        with self.assertRaisesRegex(RuntimeError, "Injected lock failure"):
            with pilot.build_lock(self.root):
                raise RuntimeError("Injected lock failure")
        pilot.build(self.root)
        _, entries, _ = pilot.load_snapshot(self.root)
        self.assertEqual(len(entries), 24)

    def test_candidate_validation_fails_before_promotion_or_pointer_switch(self):
        old_folder, _, _ = self.build_and_load()
        pointer = self.current_bytes()
        original_builds = set((self.pilot_folder / "builds").iterdir())
        self.change_curated_alias()
        original_render = pilot.render_files

        def poison_staged_entry(entries, report, prefix):
            rendered = original_render(entries, report, prefix)
            # Input preparation has already validated entries. A post-render
            # staging defect must still be caught before publication.
            entries[0]["production_integration"] = True
            return rendered

        with patch.object(pilot, "render_files", side_effect=poison_staged_entry):
            with self.assertRaises((pilot.PilotError, ValidationError)):
                pilot.build(self.root)

        self.assertEqual(self.current_bytes(), pointer)
        self.assertEqual(set((self.pilot_folder / "builds").iterdir()), original_builds)
        preserved, _, _ = pilot.load_snapshot(self.root, check_sources=False)
        self.assertEqual(preserved, old_folder)


if __name__ == "__main__":
    unittest.main()
