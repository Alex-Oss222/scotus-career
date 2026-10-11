"""Fresh ingestion checks, unrelated to any lost implementation's test results."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))
import ingest


class IngestTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.name = "Example_v_Test_merits_1996-01-01.md"
        self.record = f"terms/OT1995/records/{self.name}"
        self.write(self.record,
            "**Case and dockets:** Example v. Test; No. 95-100.\n"
            "**Event and date:** Merits decision, 1996-01-01.\n"
            "**Result:** Affirmed.\n**Version / lineage:** Initial.\n\n"
            "## Sources\nHistorical mention: 516 U.S. 100.\n"
            "[Opinion](https://example.org/opinion) and [missing](../sources/absent.pdf).\n")
        self.write("terms/OT1995/case-list.md",
            "| No. | Chunk | Caption | Docket(s) | Event date | Area of law |\n"
            "|---|---|---|---|---|---|\n"
            "| 1 | 1 | Example v. Test | 95-100 | 1996-01-01 | Procedure |\n")
        self.write("terms/OT1995/workspace/manifest.md",
            "| Event date | Case or matter | Status |\n|---|---|---|\n"
            f"| 1996-01-01 | Example v. Test | Completed: {self.name} |\n")
        self.write("terms/OT1995/workspace/ledger.md",
            "| Effective date | Record |\n|---|---|\n"
            f"| 1996-01-02 | [record](../records/{self.name}) |\n")

    def write(self, path, text):
        path = self.root / path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def build(self):
        return ingest.build_catalogue(self.root, ["OT1995"])

    def test_dates_remain_distinct_and_have_observed_evidence(self):
        record = self.build()["records"][0]
        self.assertEqual(record["event_date"], "1996-01-01")
        self.assertEqual(record["effective_date"], "1996-01-02")
        self.assertTrue(any("Explicit ledger" in r["section"] for r in record["references"]))

    def test_empty_ledger_does_not_infer_effective_date(self):
        self.write("terms/OT1995/workspace/ledger.md", "# No ledger entry\n")
        record = self.build()["records"][0]
        self.assertIsNone(record["effective_date"])
        self.assertTrue(any("No explicit effective date" in w for w in record["warnings"]))

    def test_ledger_qualifier_is_retained(self):
        self.write("terms/OT1995/workspace/ledger.md", "| Effective date | Record |\n|---|---|\n"
                   f"| 1996-01-02, after decisions | {self.name} |\n")
        record = self.build()["records"][0]
        self.assertEqual(record["effective_date"], "1996-01-02")
        self.assertTrue(any("after decisions" in w for w in record["warnings"]))

    def test_filename_without_identity_date_remains_unknown(self):
        self.write(self.record, "# Canonical Decision Record — Example v. Test\nNo. 95-100.\n")
        self.assertIsNone(self.build()["records"][0]["event_date"])

    def test_invalid_and_conflicting_metadata_dates_not_silently_repaired(self):
        for value in ("1996-02-30", "1996-01-03"):
            self.write(self.record, f"**Case and dockets:** Example v. Test; No. 95-100.\n**Event and date:** Merits, {value}.\n")
            self.assertIsNone(self.build()["records"][0]["event_date"])

    def test_every_consumed_file_is_fingerprinted(self):
        data = self.build()
        self.assertEqual(len(data["sources"]), 4)
        for path, observed in data["sources"].items():
            raw = (self.root / path).read_bytes()
            self.assertEqual(observed, {"size": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})

    def test_build_is_deterministic_and_preserves_files(self):
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        first = self.build()
        self.assertEqual(first, self.build())
        self.assertEqual(before, {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_new_identity_stable_under_content_correction(self):
        first = self.build()["records"][0]
        with (self.root / self.record).open("a") as f:
            f.write("\nCorrection provenance supplied.\n")
        second = self.build()["records"][0]
        self.assertEqual(first["record_id"], second["record_id"])
        self.assertNotEqual(first["sha256"], second["sha256"])

    def test_citations_and_sources_are_observations_not_verification(self):
        record = self.build()["records"][0]
        self.assertEqual(record["citations"][0]["text"], "516 U.S. 100")
        self.assertEqual(record["citations"][0]["section"], "Sources")
        refs = record["references"]
        self.assertTrue(any(r["kind"] == "missing" and r["target"].endswith("absent.pdf") for r in refs))
        self.assertTrue(any(r["kind"] == "external" and r["review_status"] == "unverified" for r in refs))

    def test_unsafe_reference_urls_and_escapes_stay_non_navigable(self):
        for target in ("javascript:alert(1)", "file:///etc/passwd", "https://user:password@example.org/x",
                       "../../../../etc/passwd", "/etc/passwd", "%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd"):
            kind, _, warning = ingest.reference_target(self.root, self.record, target)
            self.assertEqual(kind, "missing", target)
            self.assertTrue(warning)

    def test_source_symlinks_rejected(self):
        target = self.root / "real.md"
        target.write_text((self.root / self.record).read_text())
        (self.root / self.record).unlink()
        (self.root / self.record).symlink_to(target)
        with self.assertRaisesRegex(ingest.IngestError, "Symlink"):
            self.build()

    def test_references_do_not_follow_symlinks(self):
        self.write("terms/OT1995/sources/source.md", "source")
        (self.root / "terms/OT1995/sources/link.md").symlink_to(self.root / "terms/OT1995/sources/source.md")
        self.assertEqual(ingest.reference_target(self.root, self.record, "../sources/link.md")[0], "missing")

    def test_duplicate_and_invalid_terms_rejected(self):
        for terms in ([], ["OT1995", "OT1995"], ["../../tmp"], ["OT1995/records"]):
            with self.assertRaises(ingest.IngestError):
                ingest.build_catalogue(self.root, terms)

    def test_escaped_pipes_and_inline_code_preserved(self):
        rows = ingest.table_rows("| Caption | Docket |\n|---|---|\n| A \\| B | `x|y` |\n")
        self.assertEqual(rows[0]["columns"], {"Caption": r"A \| B", "Docket": "`x|y`"})

    def test_multiple_chunk_tables_without_chunk_column(self):
        self.write("terms/OT1995/case-list.md", "## Chunk 3\n\n"
            "| Caption | Docket(s) | Event date | Area of law |\n|---|---|---|---|\n"
            "| Example v. Test | 95-100 | 1996-01-01 | Procedure |\n\n"
            "## Chunk 4\n\n| Caption | Docket(s) | Event date | Area of law |\n|---|---|---|---|\n"
            "| Other v. Case | 95-200 | 1996-01-03 | Procedure |\n")
        result = self.build()
        self.assertEqual(result["records"][0]["chunks"], [3])
        self.assertEqual(result["terms"][0]["chunks"], [3, 4])
        self.assertEqual(result["terms"][0]["inventory_count"], 2)
        self.assertEqual(result["terms"][0]["mapped_inventory_count"], 1)

    def test_blank_ledger_batches_preserve_headers(self):
        rows = ingest.table_rows("| Effective date | Record |\n|---|---|\n| 1996-01-01 | a.md |\n\n| 1996-01-02 | b.md |\n")
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[1]["line"], 5)

    def test_malformed_or_duplicate_table_columns_fail_closed(self):
        for text in ("| A | B |\n|---|---|\n| extra | unescaped | pipe |\n", "| A | A |\n|---|---|\n| a | b |\n"):
            with self.assertRaises(ingest.IngestError):
                ingest.table_rows(text)

    def test_ambiguous_identity_is_not_guessed(self):
        self.write("terms/OT1995/workspace/manifest.md", "# No explicit mapping\n")
        self.write("terms/OT1995/records/Another_merits_1996-01-01.md", (self.root / self.record).read_text())
        result = self.build()
        self.assertFalse(result["inventory"][0]["resolved_record_ids"])
        self.assertTrue(any("ambiguous" in w for w in result["warnings"]))

    def test_explicit_manifest_can_map_two_events_to_one_inventory_item(self):
        name = "Example_v_Test_interim_1996-01-01.md"
        self.write(f"terms/OT1995/records/{name}", (self.root / self.record).read_text())
        self.write("terms/OT1995/workspace/manifest.md", "| Event date | Case or matter | Status |\n|---|---|---|\n"
                   f"| 1996-01-01 | Example v. Test | Completed: {self.name}; {name} |\n")
        result = self.build()
        self.assertEqual(len(result["inventory"][0]["resolved_record_ids"]), 2)
        self.assertEqual(result["terms"][0]["mapped_inventory_count"], 1)

    def test_changed_curated_quote_fails_closed(self):
        self.write("development/case-library/inputs/record-mappings.json", json.dumps({
            "format": "case-library-record-mappings-v1", "mappings": [{
            "term": "OT1995", "inventory_caption": "Example v. Test", "inventory_date": "1996-01-01",
            "inventory_dockets": "95-100", "record": self.name, "evidence_quote": "no longer present"}]}))
        with self.assertRaisesRegex(ingest.IngestError, "evidence changed"):
            self.build()

    def test_noncase_admission_never_becomes_court_event(self):
        text = (self.root / self.record).read_text().replace("Merits decision,", "Admitted statutory source,")
        self.write(self.record, text)
        self.assertEqual(self.build()["records"][0]["kind"], "admitted_source")

    def test_render_markers_derive_chunk_without_importing_briefs(self):
        self.write("terms/OT1995/render-inputs/OT_1995CHUNK2.md", f"<!-- source-record: {self.name} -->\n## Event\nExample\n")
        self.write("terms/OT1995/briefs/OT_1995CHUNK2.md", "Must not be read")
        result = self.build()
        self.assertEqual(result["records"][0]["chunks"], [1, 2])
        self.assertFalse(any("/briefs/" in path for path in result["sources"]))

    def test_balanced_parenthesis_links(self):
        self.assertEqual(ingest.markdown_targets("[x](https://example.org/a_(b))"), ["https://example.org/a_(b)"])

    def test_parenthetical_bare_url_excludes_prose_parenthesis(self):
        refs, _, _ = ingest.extract_references(self.root, self.record,
            "The opinion (https://example.org/USREPORTS-431-678.pdf).\n")
        self.assertEqual([ref["target"] for ref in refs], ["https://example.org/USREPORTS-431-678.pdf"])

    def test_balanced_parentheses_in_bare_url_are_preserved(self):
        refs, _, _ = ingest.extract_references(self.root, self.record,
            "See (https://example.org/wiki/Case_(law)).\n")
        self.assertEqual([ref["target"] for ref in refs], ["https://example.org/wiki/Case_(law)"])

    def test_term_folder_code_notation_is_separate_from_markdown_destinations(self):
        refs, _, _ = ingest.extract_references(self.root, self.record,
            f"`records/{self.name}`\n[relative](records/{self.name})\n")
        self.assertEqual(refs[0]["kind"], "repository")
        self.assertEqual(refs[0]["target"], self.record)
        self.assertEqual(refs[1]["kind"], "missing")

    def test_control_characters_never_become_navigable_urls(self):
        for target in ("https://exa\nmple.org/test", "https://example.org/\x00x"):
            self.assertEqual(ingest.reference_target(self.root, self.record, target)[0], "missing")

    def test_malformed_external_urls_stay_non_navigable(self):
        for target in ("https://example.org:99999/x", "https://example.org:port/x",
                       "https://example.org/a b", "https://example.org/%0ax",
                       "https://example.org/%00x", "https://example.org/%5cx",
                       "https://example.org\\@attacker.invalid/x"):
            self.assertEqual(ingest.reference_target(self.root, self.record, target)[0], "missing", target)

    def test_duplicate_mapping_json_keys_rejected(self):
        for text in ('{"format":"old","format":"case-library-record-mappings-v1","mappings":[]}',
                     '{"format":"case-library-record-mappings-v1","mappings":[{"record":"one","record":"two"}]}'):
            self.write("development/case-library/inputs/record-mappings.json", text)
            with self.assertRaisesRegex(ingest.IngestError, "Duplicate"):
                self.build()

    def test_nonfinite_overflow_and_invalid_mapping_shapes_rejected(self):
        for text in ('{"format":NaN,"mappings":[]}', '{"format":Infinity,"mappings":[]}',
                     '{"format":1e999,"mappings":[]}', '{"format":1,"mappings":[]}',
                     '[]', '{"format":"case-library-record-mappings-v1","mappings":{}}',
                     '{"format":"case-library-record-mappings-v1","mappings":[null]}'):
            self.write("development/case-library/inputs/record-mappings.json", text)
            with self.assertRaises(ingest.IngestError):
                self.build()

    def test_unused_mapping_for_selected_term_fails_closed(self):
        for caption, ordering_date, dockets in (
                ("Misspelled v. Test", "1996-01-01", "95-100"),
                ("Example v. Test", "1996-01-03", "95-100"),
                ("Example v. Test", "1996-01-01", "95-101")):
            self.write("development/case-library/inputs/record-mappings.json", json.dumps({
                "format": "case-library-record-mappings-v1", "mappings": [{
                    "term": "OT1995", "inventory_caption": caption,
                    "inventory_date": ordering_date, "inventory_dockets": dockets,
                    "record": "Absent_merits_1996-01-01.md", "evidence_quote": "Absent evidence"}]}))
            with self.assertRaisesRegex(ingest.IngestError, "Unused explicit Record mapping"):
                self.build()

    def test_unused_mapping_outside_selected_terms_is_allowed(self):
        self.write("development/case-library/inputs/record-mappings.json", json.dumps({
            "format": "case-library-record-mappings-v1", "mappings": [{
                "term": "OT1994", "inventory_caption": "Other v. Case",
                "inventory_date": "1995-01-01", "inventory_dockets": "94-100",
                "record": "Other_merits_1995-01-01.md", "evidence_quote": "Other term evidence"}]}))
        self.assertEqual(self.build()["terms"][0]["mapped_inventory_count"], 1)


class LiveCorpusReadOnlyTests(unittest.TestCase):
    def test_closed_terms_cover_every_record_and_inventory_row(self):
        root = Path(__file__).resolve().parents[3]
        if not (root / "terms/OT1995/records").is_dir():
            self.skipTest("Canonical corpus is unavailable in this checkout")
        result = ingest.build_catalogue(root, [f"OT{year}" for year in range(1991, 1996)])
        self.assertEqual(len(result["records"]), 575)
        self.assertEqual(len(result["inventory"]), 556)
        self.assertEqual(sum(r["kind"] == "admitted_source" for r in result["records"]), 17)
        self.assertEqual(len(result["carryovers"]), 12)
        self.assertFalse(result["warnings"])
        self.assertTrue(all(row["resolved_record_ids"] for row in result["inventory"]))
        self.assertTrue(all(record["event_date"] for record in result["records"]))
        vasquez = [r for r in result["records"] if "Vasquez_v_Harris" in r["path"]]
        self.assertEqual(len(vasquez), 2)
        self.assertEqual({r["inventory_refs"][0]["dockets"] for r in vasquez}, {"A-766", "A-768"})
        bowersox = [row for row in result["inventory"] if "Bowersox" in row["raw"]]
        self.assertEqual(len(bowersox), 1)
        self.assertEqual(len(bowersox[0]["resolved_record_ids"]), 2)
        self.assertFalse(any("/briefs/" in path or "_STONE" in path or "_COMPARATOR" in path for path in result["sources"]))


if __name__ == "__main__":
    unittest.main()
