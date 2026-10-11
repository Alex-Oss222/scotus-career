"""Live reads bind generated metadata to reviewed inputs in disposable copies.

Repaired checksums and matching rendered views model a consistent generator
error or manual edit. They must not promote unreviewed metadata into lookup,
show or validate; retained historical snapshots remain available for diagnosis.
"""
from __future__ import annotations

from copy import deepcopy
import json
import os
import subprocess
import unittest
from unittest.mock import patch

import test_ot1994 as fixtures
import test_pilot as pilot_fixtures


pilot = fixtures.pilot


def rewrite_snapshot(root, folder, pointer_path, entries, report):
    """Keep all generated outputs and both hash layers internally consistent."""
    for entry in entries:
        (folder / "entries" / f"{entry['case_id']}.json").write_bytes(pilot.json_bytes(entry))
    (folder / "report.json").write_bytes(pilot.json_bytes(report))
    for relative, text in pilot.render_files(entries, report, os.path.relpath(root, folder)).items():
        (folder / relative).write_text(text)
    manifest = json.loads((folder / "artifacts.json").read_bytes())
    manifest = {relative: pilot.digest((folder / relative).read_bytes()) for relative in manifest}
    (folder / "artifacts.json").write_bytes(pilot.json_bytes(manifest))
    pointer_path.write_bytes(pilot.json_bytes({
        "build_id": folder.name,
        "artifacts_sha256": pilot.digest((folder / "artifacts.json").read_bytes()),
    }))


class ReviewedReadGuards(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = fixtures.OT1994Tests(methodName="runTest")
        cls.addClassCleanup(cls.fixture.doCleanups)
        cls.fixture.setUp()
        cls.root = cls.fixture.root
        cls.folder, cls.pristine_entries, cls.pristine_report = cls.fixture.build_and_load()
        cls.original_files = cls.fixture.bytes_under(cls.folder)
        cls.original_pointer = cls.fixture.pointer_path.read_bytes()

    def setUp(self):
        for relative, raw in self.original_files.items():
            (self.folder / relative).write_bytes(raw)
        self.fixture.pointer_path.write_bytes(self.original_pointer)
        self.entries = deepcopy(self.pristine_entries)
        self.report = deepcopy(self.pristine_report)

    def rewrite(self):
        rewrite_snapshot(self.root, self.folder, self.fixture.pointer_path, self.entries, self.report)

    def assert_read_refuses_without_changes(self, *command):
        before = self.fixture.bytes_under(self.folder)
        pointer = self.fixture.pointer_path.read_bytes()
        reviewed = {p: p.read_bytes() for p in (self.fixture.selection_path, self.fixture.historical_path)}
        result = self.fixture.cli(*command)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("Snapshot content differs from reviewed inputs", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(result.stdout, "", "A refused read must not emit a partial answer")
        self.assertEqual(self.fixture.pointer_path.read_bytes(), pointer)
        self.assertEqual(self.fixture.bytes_under(self.folder), before)
        self.assertEqual({p: p.read_bytes() for p in reviewed}, reviewed)

    def test_lookup_refuses_self_consistent_unreviewed_alias(self):
        self.entries[0]["curated"]["aliases"].append("Unreviewed generated identity")
        self.rewrite()
        self.assert_read_refuses_without_changes("lookup", "Unreviewed generated identity")
        # Structural history reads remain useful for diagnosing exact bad bytes.
        _, historical, _ = pilot.load_snapshot(self.root, catalogue="OT1994", check_sources=False)
        self.assertEqual(len(pilot.lookup(historical, "Unreviewed generated identity")), 1)

    def test_show_refuses_substituted_historical_url_even_with_matching_views(self):
        entry = next(e for e in self.entries if any(d["reference"]["url"]
                     for d in e["curated"]["historical_documents"]))
        reference = next(d["reference"] for d in entry["curated"]["historical_documents"]
                         if d["reference"]["url"])
        reference["url"] = "https://example.invalid/unreviewed-historical-copy"
        self.rewrite()
        self.assert_read_refuses_without_changes("show", entry["case_id"])

    def test_validate_refuses_removed_review_limitations(self):
        self.assertGreater(len(self.report["limitations"]), 1)
        self.report["limitations"] = self.report["limitations"][:1]
        self.rewrite()
        self.assert_read_refuses_without_changes("validate")

    def test_omitted_auxiliary_fingerprint_cannot_hide_changed_review_evidence(self):
        relative = "development/case-library/catalogues/OT1994/review/coverage-audit.json"
        path = self.root / relative
        original = path.read_bytes()
        self.addCleanup(path.write_bytes, original)
        del self.report["input_sha256"][relative]
        path.write_bytes(original + b"\n")
        self.rewrite()
        self.assert_read_refuses_without_changes("validate")

    def test_unreviewed_extension_data_cannot_enter_a_live_saved_profile(self):
        self.entries[0]["extensions"]["manual_experiment"] = {"note": "Unreviewed generated annotation"}
        self.rewrite()
        self.assert_read_refuses_without_changes("validate")

    def test_new_git_revision_does_not_invalidate_unchanged_reviewed_content(self):
        before = self.fixture.bytes_under(self.folder)
        subprocess.run(
            ["git", "-C", str(self.root), "-c", "user.name=Pilot Test",
             "-c", "user.email=pilot-test@example.invalid", "-c", "commit.gpgsign=false",
             "commit", "--allow-empty", "-qm", "Unrelated temporary fixture revision"],
            check=True, capture_output=True,
        )
        self.assertNotEqual(pilot.repository_revision(self.root), self.report["source_revision"])
        folder, entries, report = pilot.load_snapshot(self.root, catalogue="OT1994")
        self.assertEqual((folder, len(entries), report["event_count"]), (self.folder, 99, 99))
        reused, _, changed = pilot.build(self.root, catalogue="OT1994")
        self.assertEqual(reused, self.folder)
        self.assertFalse(changed)
        self.assertEqual(self.fixture.bytes_under(self.folder), before)
        self.assertEqual(self.fixture.pointer_path.read_bytes(), self.original_pointer)

    def test_source_change_during_live_review_is_detected_before_return(self):
        path = self.root / self.entries[0]["curated"]["simulation"]["events"][0]["record"]["repository_path"]
        original = path.read_bytes()
        self.addCleanup(path.write_bytes, original)
        prepare = pilot.prepare

        def change_after_review(root, **kwargs):
            reviewed = prepare(root, **kwargs)
            path.write_bytes(original + b"\nConcurrent source update fixture.\n")
            return reviewed

        with patch.object(pilot, "prepare", side_effect=change_after_review):
            with self.assertRaisesRegex(pilot.PilotError, "Stale snapshot: .* changed"):
                pilot.load_snapshot(self.root, catalogue="OT1994")
        self.assertEqual(self.fixture.pointer_path.read_bytes(), self.original_pointer)
        self.assertTrue(path.read_bytes().endswith(b"Concurrent source update fixture.\n"),
                        "Read failure must preserve the concurrent edit")

    def test_recovery_removes_generated_edit_and_retains_exact_diagnostic_bytes(self):
        self.entries[0]["curated"]["aliases"].append("Generated recovery impostor")
        self.rewrite()
        damaged = self.fixture.bytes_under(self.folder)
        pointer = self.fixture.pointer_path.read_bytes()
        with self.assertRaisesRegex(pilot.PilotError, "Snapshot content differs from reviewed inputs"):
            pilot.build(self.root, catalogue="OT1994")
        rebuilt, _, changed = pilot.build(self.root, catalogue="OT1994", recover=True)
        self.assertTrue(changed)
        self.assertNotEqual(rebuilt, self.folder)
        _, entries, report = pilot.load_snapshot(self.root, catalogue="OT1994")
        self.assertEqual((len(entries), report["event_count"]), (99, 99))
        self.assertEqual(pilot.lookup(entries, "Generated recovery impostor"), [])
        self.assertEqual(self.fixture.bytes_under(self.folder), damaged)
        recovery = self.fixture.pointer_path.parent / "recovery"
        self.assertTrue(any(p.read_bytes() == pointer for p in recovery.glob("*/CURRENT.before.json")))


class PilotReviewedReadGuard(unittest.TestCase):
    def test_retained_pilot_lookup_has_the_same_reviewed_input_boundary(self):
        fixture = pilot_fixtures.PilotTests(methodName="runTest")
        self.addCleanup(fixture.doCleanups)
        fixture.setUp()
        folder, entries, report = fixture.build_and_load()
        pointer = fixture.root / pilot.PILOT / "CURRENT.json"
        entries[0]["curated"]["aliases"].append("Unreviewed pilot alias")
        rewrite_snapshot(fixture.root, folder, pointer, entries, report)
        with self.assertRaisesRegex(pilot.PilotError, "Snapshot content differs from reviewed inputs"):
            pilot.load_snapshot(fixture.root)
        _, history, _ = pilot.load_snapshot(fixture.root, check_sources=False)
        self.assertEqual(len(pilot.lookup(history, "Unreviewed pilot alias")), 1)


if __name__ == "__main__":
    unittest.main()
