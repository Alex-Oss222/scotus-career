"""OT1992 coverage and cross-term boundaries, using disposable repositories.

These are catalogue checks against reviewed repository mappings. They do not
infer legal treatment, fetch historical documents, or rerun adjudication.
"""
from __future__ import annotations

from copy import deepcopy
import json
import shutil
import subprocess
import sys
import unittest

import test_pilot as fixtures


pilot = fixtures.pilot
REPOSITORY = fixtures.REPOSITORY
CATALOGUE = "OT1992"


class OT1992Tests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.PilotTests(methodName="runTest")
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()
        self.root = self.fixture.root
        self.scope = pilot.catalogue_path(CATALOGUE)
        self.selection_path = self.root / self.scope / "selection.json"
        self.historical_path = self.root / self.scope / "historical-sources.json"
        self.pointer_path = self.root / self.scope / "CURRENT.json"
        self.copy_catalogue(CATALOGUE)
        self.assertEqual(len(list((self.root / "terms/OT1992/records").glob("*.md"))), 126,
                         "The reviewed mappings must account for every OT1992 Record")

    def copy_catalogue(self, catalogue):
        scope = pilot.catalogue_path(catalogue)
        paths = set()
        for name in ("selection.json", "historical-sources.json"):
            relative = scope / name
            paths.add(relative.as_posix())
            paths.update(fixtures.referenced_paths(json.loads((REPOSITORY / relative).read_text())))
        for directory, pattern in (("schemas", "*.json"), ("tools", "*.py")):
            paths.update(path.relative_to(REPOSITORY).as_posix()
                         for path in (REPOSITORY / pilot.AREA / directory).glob(pattern))
        for relative in paths:
            source = pilot.safe_path(REPOSITORY, relative)
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)

    def selection(self):
        return json.loads(self.selection_path.read_text())

    def prepare_selection(self, selection):
        self.fixture.write_json(self.selection_path, selection)
        return pilot.prepare(self.root, catalogue=CATALOGUE)

    def prepare(self):
        return pilot.prepare(self.root, catalogue=CATALOGUE)

    def build_and_load(self):
        pilot.build(self.root, catalogue=CATALOGUE)
        return pilot.load_snapshot(self.root, catalogue=CATALOGUE)

    def cli(self, *arguments, catalogue=CATALOGUE):
        return subprocess.run(
            [sys.executable, "-B", str(self.root / pilot.AREA / "tools/pilot.py"),
             "--root", str(self.root), "--catalogue", catalogue, *arguments],
            capture_output=True, text=True, timeout=30,
        )

    @staticmethod
    def bytes_under(folder):
        return {path.relative_to(folder): path.read_bytes()
                for path in folder.rglob("*") if path.is_file()}

    def rehash_artifact(self, folder, relative, value):
        raw = pilot.json_bytes(value)
        (folder / relative).write_bytes(raw)
        manifest_path = folder / "artifacts.json"
        manifest = json.loads(manifest_path.read_bytes())
        manifest[relative] = pilot.digest(raw)
        manifest_path.write_bytes(pilot.json_bytes(manifest))
        self.pointer_path.write_bytes(pilot.json_bytes({
            "build_id": folder.name,
            "artifacts_sha256": pilot.digest(manifest_path.read_bytes()),
        }))

    def test_full_term_covers_123_events_and_three_admitted_sources(self):
        folder, entries, report = self.build_and_load()
        self.assertEqual((len(entries), report["case_count"], report["event_count"]), (123, 123, 123))
        self.assertEqual((report["term"], report["catalogue"], report["selection_version"]),
                         (CATALOGUE, CATALOGUE, 4))
        self.assertEqual(report["chunks"], list(range(1, 12)))
        self.assertEqual(report["chunk_counts"], {**{str(c): 12 for c in range(1, 11)}, "11": 3})
        self.assertEqual((report["inventory_event_count"], report["supplemental_event_count"]), (123, 0))
        excluded = {item["record_path"] for item in report["excluded_records"]}
        self.assertEqual(excluded, {
            "terms/OT1992/records/White_retirement_institutional_transition_1993-06-28.md",
            "terms/OT1992/records/Forfeiture_jurisdiction_amendment_1992-10-28.md",
            "terms/OT1992/records/Energy_Policy_Act_1992_depletion_amendment_1992-10-24.md",
        })
        records = [event["record"]["repository_path"] for entry in entries
                   for event in entry["curated"]["simulation"]["events"]]
        self.assertEqual(len(records), len(set(records)))
        self.assertEqual(set(records) | excluded, set(report["record_inventory"]))
        self.assertEqual(len(report["record_inventory"]), 126)
        self.assertEqual(len(list((folder / "entries").glob("*.json"))), 123)
        self.assertEqual(len(list((folder / "cards").glob("*.md"))), 123)
        self.assertTrue(all(entry["production_integration"] is False for entry in entries))
        self.assertTrue(all(not entry["curated"]["simulation"]["later_treatment"] for entry in entries))
        result = self.cli("validate")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS: 123 entries", result.stdout)

    def test_two_smith_cases_remain_distinct_by_docket_citation_and_date(self):
        entries, _ = self.prepare()
        by_name = pilot.lookup(entries, "Smith v. United States")
        self.assertEqual(len(by_name), 2)
        identities = set()
        for docket, citation, date in (
            ("91-1538", "507 U.S. 197", "1993-03-08"),
            ("91-8674", "508 U.S. 223", "1993-06-01"),
        ):
            with self.subTest(docket=docket):
                entry, = pilot.lookup(entries, docket)
                self.assertEqual([found["case_id"] for found in pilot.lookup(entries, citation)],
                                 [entry["case_id"]])
                event, = entry["curated"]["simulation"]["events"]
                self.assertEqual((event["event_date"], event["effective_date"]), (date, date))
                self.assertEqual(entry["extensions"]["pilot"]["event_details"][event["event_id"]]
                                 ["docket_numbers"], [docket])
                identities.add((entry["case_id"], event["event_id"], event["record"]["repository_path"]))
        self.assertEqual(len(identities), 2)

    def test_original_jurisdiction_dockets_are_explicit_and_searchable(self):
        entries, _ = self.prepare()
        for docket, caption in (("9, Original", "United States v. Louisiana"),
                                ("111, Original", "Delaware v. New York"),
                                ("108, Original", "Nebraska v. Wyoming")):
            with self.subTest(docket=docket):
                entry, = pilot.lookup(entries, docket)
                self.assertIn(caption, entry["curated"]["case_name"])
                event, = entry["curated"]["simulation"]["events"]
                detail = entry["extensions"]["pilot"]["event_details"][event["event_id"]]
                self.assertEqual(detail["docket_numbers"], [docket])
                self.assertTrue(detail["owned_docket_evidence"])

    def test_corrections_and_prior_term_continuity_do_not_add_adjudications(self):
        entries, report = self.prepare()
        for query, date in (("Demos v. Storrie", "1993-03-08"),
                            ("Moreau v. Klevenhagen", "1993-05-03"),
                            ("Delo v. Blair", "1993-07-21")):
            with self.subTest(case=query):
                entry, = pilot.lookup(entries, query)
                event, = entry["curated"]["simulation"]["events"]
                self.assertEqual((event["event_date"], event["effective_date"]), (date, date))
                self.assertIsNotNone(entry["extensions"]["pilot"]["event_details"][event["event_id"]]
                                     ["inventory_match"])
        self.assertEqual(pilot.lookup(entries, "Coleman"), [])
        self.assertEqual(pilot.lookup(entries, "91-8336"), [])
        self.assertEqual(report["supplemental_event_count"], 0)

    def test_ot1992_build_and_refresh_preserve_both_ot1991_catalogues(self):
        self.copy_catalogue("OT1991")
        self.fixture.build_and_load()
        pilot.build(self.root, catalogue="OT1991")
        older_scopes = [self.root / pilot.PILOT, self.root / pilot.catalogue_path("OT1991")]
        before = {scope: self.bytes_under(scope) for scope in older_scopes}
        folder, entries, _ = self.build_and_load()
        repeated, _, changed = pilot.build(self.root, catalogue=CATALOGUE)
        self.assertEqual(repeated, folder)
        self.assertFalse(changed)
        record = self.root / entries[0]["curated"]["simulation"]["events"][0]["record"]["repository_path"]
        record.write_text(record.read_text() + "\n<!-- Disposable fixture observation refresh. -->\n")
        with self.assertRaisesRegex(pilot.PilotError, "Stale snapshot"):
            pilot.load_snapshot(self.root, catalogue=CATALOGUE)
        refreshed, _, changed = pilot.build(self.root, catalogue=CATALOGUE)
        self.assertTrue(changed)
        self.assertNotEqual(refreshed, folder)
        for scope in older_scopes:
            self.assertEqual(self.bytes_under(scope), before[scope])
        self.assertEqual(len(pilot.load_snapshot(self.root)[1]), 24)
        self.assertEqual(len(pilot.load_snapshot(self.root, catalogue="OT1991")[1]), 124)
        self.assertEqual(len(pilot.load_snapshot(self.root, catalogue=CATALOGUE)[1]), 123)

    def test_cross_term_selection_records_and_presentations_are_rejected(self):
        original = self.selection()
        old_selection = json.loads((self.root / pilot.PILOT / "selection.json").read_text())
        old_record = old_selection["cases"][0]["events"][0]["record_path"]
        for mutation in ("selection_term", "record", "public_render", "render_input"):
            with self.subTest(mutation=mutation):
                selection = deepcopy(original)
                event = selection["cases"][0]["events"][0]
                if mutation == "selection_term":
                    selection["term"] = "OT1991"
                elif mutation == "record":
                    event["record_path"] = old_record
                else:
                    publication = next(p for p in event["publications"] if p["kind"] == mutation)
                    directory = "output" if mutation == "public_render" else "render-inputs"
                    publication["repository_path"] = f"terms/OT1991/{directory}/OT_1991CHUNK1.md"
                with self.assertRaises(pilot.PilotError):
                    self.prepare_selection(selection)
                self.assertFalse(self.pointer_path.exists())
        self.fixture.write_json(self.selection_path, original)
        historical = json.loads(self.historical_path.read_text())
        historical["term"] = "OT1991"
        self.fixture.write_json(self.historical_path, historical)
        with self.assertRaises(pilot.PilotError):
            self.prepare()

    def test_rehashed_report_cannot_claim_another_term_or_chunk_scope(self):
        folder, _, original = self.build_and_load()
        for field, value in (("term", "OT1991"), ("catalogue", "OT1991"),
                             ("chunks", list(range(1, 15)))):
            with self.subTest(field=field):
                report = deepcopy(original)
                report[field] = value
                self.rehash_artifact(folder, "report.json", report)
                pointer = self.pointer_path.read_bytes()
                with self.assertRaises(pilot.PilotError):
                    pilot.load_snapshot(self.root, catalogue=CATALOGUE)
                self.assertEqual(self.pointer_path.read_bytes(), pointer)

    def test_unreviewed_record_membership_blocks_lookup_and_rebuild(self):
        _, entries, _ = self.build_and_load()
        before = self.pointer_path.read_bytes()
        record = self.root / entries[0]["curated"]["simulation"]["events"][0]["record"]["repository_path"]
        added = self.root / "terms/OT1992/records/fixture_unreviewed_event.md"
        added.write_bytes(record.read_bytes())
        with self.assertRaisesRegex(pilot.PilotError, "Record inventory changed"):
            pilot.load_snapshot(self.root, catalogue=CATALOGUE)
        result = self.cli("lookup", "Smith")
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("Record inventory changed", result.stderr)
        self.assertNotIn("match(es)", result.stdout)
        with self.assertRaisesRegex(pilot.PilotError, "Record coverage mismatch"):
            pilot.build(self.root, catalogue=CATALOGUE)
        self.assertEqual(self.pointer_path.read_bytes(), before)

    def test_repeated_event_headings_bind_occurrence_and_identity_quote(self):
        selection = self.selection()
        located = [(case, event, publication) for case in selection["cases"] for event in case["events"]
                   for publication in event["publications"]
                   if publication["kind"] == "render_input" and "heading_occurrence" in publication]
        self.assertGreaterEqual(len(located), 2)
        _, _, first = located[0]
        _, _, second = next(item for item in located[1:]
                            if item[2]["repository_path"] == first["repository_path"]
                            and item[2]["heading"] == first["heading"])
        for field in ("heading_occurrence", "identity_quote"):
            with self.subTest(field=field):
                saved = first[field]
                first[field] = second[field]
                with self.assertRaises(pilot.PilotError):
                    self.prepare_selection(selection)
                first[field] = saved
        self.fixture.write_json(self.selection_path, selection)
        folder, entries, _ = self.build_and_load()
        for case, _, publication in located:
            occurrence = publication["heading_occurrence"]
            anchor = "event" + (f"-{occurrence - 1}" if occurrence > 1 else "")
            card = (folder / "cards" / (case["case_id"] + ".md")).read_text()
            self.assertIn("OT_1992CHUNK4.md#" + anchor, card)
        result = self.cli("lookup", "91-1538")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(next(entry["case_id"] for entry in pilot.lookup(entries, "91-1538")), result.stdout)

    def test_missing_admitted_source_exception_cannot_hide_record_inventory(self):
        selection = self.selection()
        self.assertEqual(len(selection["exceptions"]), 3)
        selection["exceptions"].pop()
        with self.assertRaisesRegex(pilot.PilotError, "Record coverage mismatch"):
            self.prepare_selection(selection)

    def test_unsupported_catalogues_fail_without_creating_output(self):
        for catalogue in ("OT1993", "ot1992", "../OT1992"):
            with self.subTest(catalogue=catalogue):
                with self.assertRaises(pilot.PilotError):
                    pilot.catalogue_path(catalogue)
                result = self.cli("build", catalogue=catalogue)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertNotIn("Traceback", result.stderr)
        self.assertFalse(self.pointer_path.exists())


if __name__ == "__main__":
    unittest.main()
