"""Live-profile checks remain stricter than the intentionally flexible draft.

Mutations use one disposable OT1992 repository and repair artifact/pointer
hashes. A simulated older renderer and check_sources=False isolate structural
checks from freshness and regenerated-view checks, as in retained-snapshot
recovery. Original fixture bytes are restored before every test.
"""
from __future__ import annotations

from copy import deepcopy
import unittest

import test_ot1992 as fixtures


pilot = fixtures.pilot


class LiveSnapshotGuards(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = fixtures.OT1992Tests(methodName="runTest")
        cls.addClassCleanup(cls.fixture.doCleanups)
        cls.fixture.setUp()
        cls.root = cls.fixture.root
        cls.folder, cls.entries, cls.report = cls.fixture.build_and_load()
        cls.original_files = cls.fixture.bytes_under(cls.folder)
        cls.original_pointer = cls.fixture.pointer_path.read_bytes()

    def setUp(self):
        for relative, raw in self.original_files.items():
            (self.folder / relative).write_bytes(raw)
        self.fixture.pointer_path.write_bytes(self.original_pointer)
        self.saved_report = deepcopy(self.report)
        self.saved_report["input_sha256"][str(pilot.AREA / "tools/pilot_views.py")] = "0" * 64
        self.write("report.json", self.saved_report)

    def write(self, relative, value):
        self.fixture.rehash_artifact(self.folder, relative, value)

    def load(self):
        return pilot.load_snapshot(self.root, catalogue=fixtures.CATALOGUE, check_sources=False)

    def assert_invalid_entry(self, entry, message):
        self.write(f"entries/{entry['case_id']}.json", entry)
        before = self.fixture.pointer_path.read_bytes()
        with self.assertRaisesRegex(pilot.PilotError, message):
            self.load()
        self.assertEqual(self.fixture.pointer_path.read_bytes(), before)

    def test_draft_unknowns_do_not_become_live_records_or_dockets(self):
        validator = pilot.schema_validator(self.root)
        for target, key in (("event", "event_type"), ("event", "event_date"),
                            ("event", "effective_date"), ("docket", "court"),
                            ("docket", "number")):
            with self.subTest(target=target, key=key):
                entry = deepcopy(self.entries[0])
                item = (entry["curated"]["simulation"]["events"][0] if target == "event"
                        else entry["curated"]["dockets"][0])
                item[key] = None
                validator.validate(entry)  # Draft placeholders remain supported.
                self.assert_invalid_entry(entry, "Live event requires|Live docket metadata")

    def test_record_reference_requires_local_fingerprint_and_mixed_classification(self):
        variants = [dict(repository_path=None, content_sha256=None),
                    dict(content_sha256=None), dict(material_kind="historical"),
                    dict(material_kind="simulation_public"), dict(material_kind="unknown"),
                    dict(url="https://example.invalid/record"), dict(review_status="unreviewed")]
        for updates in variants:
            with self.subTest(updates=updates):
                entry = deepcopy(self.entries[0])
                entry["curated"]["simulation"]["events"][0]["record"].update(updates)
                self.assert_invalid_entry(entry, "Live event requires a local|Live event Record must")

    def test_missing_live_metadata_has_controlled_cli_failure(self):
        entry = deepcopy(self.entries[0])
        del entry["extensions"]
        self.assert_invalid_entry(entry, "missing its pilot metadata")
        result = self.fixture.cli("validate")
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("missing its pilot metadata", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_float_version_and_unreviewed_identity_are_not_live_metadata(self):
        for target in ("schema_version", "identity_review_status", "docket_context", "docket_review"):
            with self.subTest(target=target):
                entry = deepcopy(self.entries[0])
                if target == "schema_version":
                    entry[target] = 1.0
                elif target == "identity_review_status":
                    entry["curated"][target] = "unreviewed"
                else:
                    key, value = (("context", "unknown") if target == "docket_context"
                                  else ("review_status", "unreviewed"))
                    entry["curated"]["dockets"][0][key] = value
                self.assert_invalid_entry(entry, "Live schema version|Live case identity|Live dockets")

    def test_unknown_or_duplicate_observations_cannot_bypass_fingerprints(self):
        for mutation in ("unknown_null", "missing_hash", "duplicate"):
            with self.subTest(mutation=mutation):
                entry = deepcopy(self.entries[0])
                observations = entry["generated"]["observations"]
                if mutation == "unknown_null":
                    observations.append(dict(observations[0], repository_path="terms/OT1992/unknown.md",
                                             content_sha256=None))
                elif mutation == "missing_hash":
                    observations[0]["content_sha256"] = None
                else:
                    observations.append(deepcopy(observations[0]))
                self.assert_invalid_entry(entry, "observation differs from source manifest|Duplicate observations")

    def test_records_and_presentations_require_correct_observation_kinds(self):
        for target in ("record", "public_render", "render_input"):
            for mutation in ("omitted", "misclassified"):
                with self.subTest(target=target, mutation=mutation):
                    entry = deepcopy(self.entries[0])
                    path = (entry["curated"]["simulation"]["events"][0]["record"]["repository_path"]
                            if target == "record" else next(p["repository_path"] for p in
                            entry["extensions"]["pilot"]["publications"] if p["kind"] == target))
                    observations = entry["generated"]["observations"]
                    item = next(o for o in observations if o["repository_path"] == path)
                    if mutation == "omitted":
                        observations.remove(item)
                    else:
                        item["material_kind"] = "historical"
                    self.assert_invalid_entry(entry, "lacks a matching")

    def test_scan_and_review_provenance_must_agree_with_snapshot(self):
        for target, key, value in (
            ("generated", "last_scan_revision", None), ("generated", "last_scanned_at", None),
            ("identity", "repository_revision", "0" * 40), ("identity", "observed_at", None),
            ("record", "evidence_path", None), ("historical", "basis", "unknown"),
        ):
            with self.subTest(target=target, key=key):
                entry = deepcopy(self.entries[0])
                item = {"generated": entry["generated"],
                        "identity": entry["curated"]["identity_provenance"],
                        "record": entry["curated"]["simulation"]["events"][0]["record"]["provenance"],
                        "historical": entry["curated"]["historical_documents"][0]["reference"]["provenance"]}[target]
                item[key] = value
                self.assert_invalid_entry(entry, "provenance differs from snapshot")

    def test_cross_term_record_fails_even_with_matching_manifest_and_observation(self):
        entry = deepcopy(self.entries[0])
        ref = entry["curated"]["simulation"]["events"][0]["record"]
        old = ref["repository_path"]
        ref["repository_path"] = old.replace("OT1992", "OT1991")
        self.saved_report["input_sha256"][ref["repository_path"]] = ref["content_sha256"]
        self.write("report.json", self.saved_report)
        next(o for o in entry["generated"]["observations"] if o["repository_path"] == old)["repository_path"] = ref["repository_path"]
        self.assert_invalid_entry(entry, "Record points outside its catalogue term")

    def test_cross_term_publication_fails_even_with_matching_fingerprint(self):
        entry = deepcopy(self.entries[0])
        publication = entry["extensions"]["pilot"]["publications"][0]
        old = publication["repository_path"]
        publication["repository_path"] = old.replace("OT1992", "OT1991")
        self.saved_report["input_sha256"][publication["repository_path"]] = self.saved_report["input_sha256"][old]
        self.write("report.json", self.saved_report)
        next(o for o in entry["generated"]["observations"] if o["repository_path"] == old)["repository_path"] = publication["repository_path"]
        self.assert_invalid_entry(entry, "publication points outside its catalogue term")


if __name__ == "__main__":
    unittest.main()
