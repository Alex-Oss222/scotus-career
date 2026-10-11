"""Snapshot metadata corruption must fail closed and remain recoverable.

Every mutation uses an isolated copy. Rehashed fixtures deliberately bypass the
byte-integrity layer to exercise semantic metadata checks independently.
"""
from __future__ import annotations

from copy import deepcopy
import json
import subprocess
import sys
import unittest

import test_pilot as fixture_module


pilot = fixture_module.pilot


class SnapshotTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixture_module.PilotTests(methodName="runTest")
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()
        self.root = self.fixture.root
        self.pilot_folder = self.root / pilot.PILOT
        self.pointer_path = self.pilot_folder / "CURRENT.json"
        self.folder, self.entries, self.report = self.fixture.build_and_load()

    def rehash_artifact(self, relative, raw):
        """Make hashes agree so structural checks, not checksums, reject damage."""
        (self.folder / relative).write_bytes(raw)
        manifest_path = self.folder / "artifacts.json"
        manifest = json.loads(manifest_path.read_bytes())
        manifest[relative] = pilot.digest(raw)
        manifest_path.write_bytes(pilot.json_bytes(manifest))
        self.pointer_path.write_bytes(pilot.json_bytes({
            "build_id": self.folder.name,
            "artifacts_sha256": pilot.digest(manifest_path.read_bytes()),
        }))

    def cli(self, command):
        return subprocess.run(
            [sys.executable, "-B", str(self.root / pilot.AREA / "tools/pilot.py"),
             "--root", str(self.root), command],
            capture_output=True, text=True,
        )

    def test_pointer_shapes_and_duplicate_keys_fail_closed(self):
        original = self.pointer_path.read_bytes()
        pointer = json.loads(original)
        duplicate = (b'{"build_id": ' + json.dumps(pointer["build_id"]).encode()
                     + b', "build_id": ' + json.dumps(pointer["build_id"]).encode()
                     + b', "artifacts_sha256": ' + json.dumps(pointer["artifacts_sha256"]).encode() + b'}')
        variants = [b'{"build_id":', b'[]', pilot.json_bytes(dict(pointer, build_id=[])),
                    pilot.json_bytes(dict(pointer, unexpected="metadata")), duplicate]
        for raw in variants:
            with self.subTest(raw=raw):
                self.pointer_path.write_bytes(raw)
                with self.assertRaises(pilot.PilotError):
                    pilot.load_snapshot(self.root)
                with self.assertRaises(pilot.PilotError):
                    pilot.build(self.root)
                self.assertEqual(self.pointer_path.read_bytes(), raw)
        self.pointer_path.write_bytes(original)
        pilot.load_snapshot(self.root)

    def test_report_wrong_types_counts_and_unknown_fields_fail_after_rehash(self):
        for field, value in (("case_count", "24"), ("case_count", True),
                             ("event_count", 25), ("historical_document_count", 35),
                             ("linked_historical_document_count", 0), ("chunk_counts", []),
                             ("chunks", [True, 2, 3]), ("chunks", [1.0, 2, 3]),
                             ("generated_at", None), ("excluded_records", {}),
                             ("input_sha256", []), ("unexpected", "unrecognized field")):
            with self.subTest(field=field, value=value):
                report = deepcopy(self.report)
                report[field] = value
                self.rehash_artifact("report.json", pilot.json_bytes(report))
                pointer = self.pointer_path.read_bytes()
                with self.assertRaises(pilot.PilotError):
                    pilot.load_snapshot(self.root)
                self.assertEqual(self.pointer_path.read_bytes(), pointer)
        self.rehash_artifact("report.json", pilot.json_bytes(self.report))
        pilot.load_snapshot(self.root)

    def test_duplicate_report_keys_reject_matching_artifact_hashes(self):
        raw = pilot.json_bytes(self.report).rstrip()
        raw = raw[:-1] + b', "case_count": 24}\n'
        self.rehash_artifact("report.json", raw)
        with self.assertRaisesRegex(pilot.PilotError, "duplicate JSON key"):
            pilot.load_snapshot(self.root)
        result = self.cli("validate")
        self.assertEqual(result.returncode, 2)
        self.assertIn("duplicate JSON key", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_missing_or_nonstring_pilot_citation_is_rejected_before_lookup(self):
        entry = self.entries[0]
        relative = f"entries/{entry['case_id']}.json"
        for value in (None, [], {}, 7, ""):
            with self.subTest(value=value):
                changed = deepcopy(entry)
                changed["extensions"]["pilot"]["inventory_citation"] = value
                self.rehash_artifact(relative, pilot.json_bytes(changed))
                with self.assertRaises(pilot.PilotError):
                    pilot.load_snapshot(self.root)
        changed = deepcopy(entry)
        del changed["extensions"]["pilot"]["inventory_citation"]
        self.rehash_artifact(relative, pilot.json_bytes(changed))
        with self.assertRaises(pilot.PilotError):
            pilot.load_snapshot(self.root)
        result = self.cli("validate")
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("Traceback", result.stderr)

    def test_missing_or_malformed_pilot_publications_are_rejected(self):
        entry = self.entries[0]
        relative = f"entries/{entry['case_id']}.json"
        for value in (None, "publication", [{"kind": "public_render"}],
                      [{"kind": "public_render", "repository_path": "../outside.md", "heading": None}]):
            with self.subTest(value=value):
                changed = deepcopy(entry)
                changed["extensions"]["pilot"]["publications"] = value
                self.rehash_artifact(relative, pilot.json_bytes(changed))
                with self.assertRaises(pilot.PilotError):
                    pilot.load_snapshot(self.root)
        changed = deepcopy(entry)
        del changed["extensions"]["pilot"]["publications"]
        self.rehash_artifact(relative, pilot.json_bytes(changed))
        with self.assertRaises(pilot.PilotError):
            pilot.load_snapshot(self.root)

    def test_unresolved_local_case_schema_ref_stops_before_publication(self):
        schema_path = self.root / pilot.AREA / "schemas/case.schema.json"
        schema = json.loads(schema_path.read_bytes())
        schema["allOf"] = [{"$ref": "#/$defs/no_such_definition"}]
        schema_path.write_bytes(pilot.json_bytes(schema))
        before_pointer = self.pointer_path.read_bytes()
        before_builds = set((self.pilot_folder / "builds").iterdir())
        with self.assertRaises(pilot.PilotError):
            pilot.build(self.root)
        self.assertEqual(self.pointer_path.read_bytes(), before_pointer)
        self.assertEqual(set((self.pilot_folder / "builds").iterdir()), before_builds)
        result = self.cli("build")
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("Traceback", result.stderr)
        self.assertIn("Pilot error:", result.stderr)
        self.assertEqual(self.pointer_path.read_bytes(), before_pointer)

    def test_recovery_retains_duplicate_pointer_bytes_and_curated_inputs(self):
        pointer = json.loads(self.pointer_path.read_bytes())
        damaged = (b'{"build_id": ' + json.dumps(pointer["build_id"]).encode()
                   + b', "build_id": ' + json.dumps(pointer["build_id"]).encode()
                   + b', "artifacts_sha256": ' + json.dumps(pointer["artifacts_sha256"]).encode() + b'}')
        self.pointer_path.write_bytes(damaged)
        curated = {path: path.read_bytes() for path in
                   (self.fixture.selection_path, self.fixture.historical_path)}
        pilot.build(self.root, recover=True)
        _, entries, _ = pilot.load_snapshot(self.root)
        self.assertEqual(len(entries), 24)
        self.assertTrue(any(path.read_bytes() == damaged
                            for path in (self.pilot_folder / "recovery").rglob("*") if path.is_file()))
        self.assertEqual({path: path.read_bytes() for path in curated}, curated)

    def test_recovery_preserves_rehashed_invalid_report_and_rebuilds(self):
        damaged_report = dict(self.report, event_count=999)
        damaged_bytes = pilot.json_bytes(damaged_report)
        self.rehash_artifact("report.json", damaged_bytes)
        previous_pointer = self.pointer_path.read_bytes()
        with self.assertRaises(pilot.PilotError):
            pilot.build(self.root)
        self.assertEqual(self.pointer_path.read_bytes(), previous_pointer)
        pilot.build(self.root, recover=True)
        folder, entries, report = pilot.load_snapshot(self.root)
        self.assertNotEqual(folder, self.folder)
        self.assertEqual((len(entries), report["event_count"]), (24, 24))
        self.assertEqual((self.folder / "report.json").read_bytes(), damaged_bytes)
        self.assertTrue(any(path.read_bytes() == previous_pointer
                            for path in (self.pilot_folder / "recovery").rglob("*") if path.is_file()))


if __name__ == "__main__":
    unittest.main()
