"""Historical citation metadata requires locally recorded, document-level proof."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


AREA = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AREA / "tools"))
import pilot  # noqa: E402
from source_checks import check_historical_document  # noqa: E402
from test_source_guards import QuotedSources  # noqa: E402
import test_ot1992 as fixtures  # noqa: E402


class SourceMetadataTests(unittest.TestCase):
    def document(self, citation, quote, document_type="lower_court_opinion"):
        url = "https://example.org/lower-opinion.pdf"
        quote = quote + f" Source: [{document_type}]({url})."
        evidence = {"path": "terms/OT1992/records/example.md", "locator": "L1", "quote": quote}
        doc = {"document_id": "example-lower", "document_type": document_type,
               "citation": citation, "url": url, "url_basis": "explicit_url",
               "repository_path": None, "document_date": None, "section_locator": None,
               "evidence": [evidence], "notes": ["Locally recorded metadata only."]}
        return doc, QuotedSources({evidence["path"]: quote})

    def test_all_reviewed_documents_pass_without_fetching_or_mutation(self):
        root = AREA.parents[1]
        with patch("urllib.request.urlopen") as request:
            for scope, expected in ((pilot.PILOT, 34), (pilot.catalogue_path("OT1991"), 375),
                                    (pilot.catalogue_path("OT1992"), 401)):
                with self.subTest(scope=scope):
                    path = root / scope / "historical-sources.json"
                    before = path.read_bytes()
                    historical = json.loads(before)
                    original = deepcopy(historical)
                    documents = [doc for case in historical["cases"] for doc in case["documents"]]
                    self.assertEqual(len(documents), expected)
                    sources = pilot.Sources(root)
                    for doc in documents:
                        check_historical_document(doc, sources)
                    self.assertEqual(historical, original)
                    self.assertEqual(path.read_bytes(), before)
            request.assert_not_called()

    def test_inherited_supreme_court_citation_fails_even_when_quoted(self):
        for citation in ("506 U.S. 357 (1993)", "113 S. Ct. 835", "122 L. Ed. 2d 103",
                         "506US357", "113S.Ct.835"):
            with self.subTest(citation=citation):
                doc, sources = self.document(citation, f"Historical Supreme Court report: {citation}. "
                                             "The lower judgment is 963 F.2d 1403.")
                with self.assertRaisesRegex(ValueError, "lower-court opinion cannot inherit"):
                    check_historical_document(doc, sources)

    def test_unquoted_citation_is_rejected(self):
        doc, sources = self.document("999 F.3d 12345", "The lower judgment is 963 F.2d 1403.")
        with self.assertRaisesRegex(ValueError, "whole citation is absent"):
            check_historical_document(doc, sources)

    def test_spacing_punctuation_and_unicode_typography_are_supported(self):
        for citation, quote in (
            ("945 F.2d 881", "Judgment: 945F.2d881 (September 26, 1991)."),
            ("841 F. Supp. 1444", "Opinion: **841 F.Supp.1444**."),
            ("951 F.2d 1128 (1991)", "Opinion: 951 F.2d 1128（1991）."),
            ("963 F.2d 1403", "Report: 963\u00a0F.2d\u00a01403."),
            ("Ａ12", "Local identifier: A12."),
        ):
            with self.subTest(citation=citation):
                doc, sources = self.document(citation, quote)
                check_historical_document(doc, sources)

    def test_truncated_volume_page_year_and_punctuation_only_citations_fail(self):
        for citation in ("94 F.2d 881 (1991)", "945 F.2d 88 (1991)", "945 F.2d 881 (199)",
                         "945 F.2d 881 (1992)", "."):
            with self.subTest(citation=citation):
                doc, sources = self.document(citation, "Judgment: 945 F.2d 881 (1991).")
                with self.assertRaisesRegex(ValueError, "whole citation is absent"):
                    check_historical_document(doc, sources)

    def test_numeric_separators_and_subsection_boundaries_cannot_drift(self):
        for citation, recorded in (
            ("Law377", "Law3-77"),
            ("Law3-77", "Law377"),
            ("Law3.77", "Law3-77"),
            ("Law3 77", "Law3-77"),
            ("12 C.F.R. §203", "12 C.F.R. §20.3"),
            ("12 C.F.R. §20.3", "12 C.F.R. §203"),
            ("12 C.F.R. §20-3", "12 C.F.R. §20.3"),
            ("12 C.F.R. §20(3)", "12 C.F.R. §20.3"),
            ("28 U.S.C. §2254d", "28 U.S.C. §2254(d)"),
            ("28 U.S.C. §2254(d1)", "28 U.S.C. §2254(d)(1)"),
            ("28 U.S.C. §2254(d)(1)", "28 U.S.C. §2254(d1)"),
            ("28 U.S.C. §2254(d)", "28 U.S.C. §2254(d1)"),
        ):
            with self.subTest(citation=citation, recorded=recorded):
                doc, sources = self.document(citation, f"Recorded instrument: {recorded}.", "statute")
                with self.assertRaisesRegex(ValueError, "whole citation is absent"):
                    check_historical_document(doc, sources)
        for citation, recorded in (("Law 3–77", "Law3 - 77"),
                                   ("12 C.F.R. §20.3", "12 C.F.R.§20 . 3"),
                                   ("28 U.S.C. §2254(d)(1)", "28U.S.C.§2254 ( d ) ( 1 )")):
            with self.subTest(citation=citation, recorded=recorded):
                doc, sources = self.document(citation, f"Recorded instrument: {recorded}.", "statute")
                check_historical_document(doc, sources)

    def test_citation_in_url_or_separate_fragments_is_not_bibliographic_proof(self):
        for quote in ("Pointer: https://example.org/945-F.2d-881/opinion.pdf",
                      "Volume 945 was reviewed; another text mentions F.2d 881."):
            with self.subTest(quote=quote):
                doc, sources = self.document("945 F.2d 881", quote)
                with self.assertRaisesRegex(ValueError, "whole citation is absent"):
                    check_historical_document(doc, sources)
        doc, sources = self.document("945 F.2d 881", "Volume 945 F.2d.")
        extra = {"path": "terms/OT1992/briefs/example.md", "locator": "L1", "quote": "Page 881."}
        doc["evidence"].append(extra)
        sources.files[extra["path"]] = extra["quote"]
        with self.assertRaisesRegex(ValueError, "whole citation is absent"):
            check_historical_document(doc, sources)

    def test_citation_year_and_descriptive_additions_require_quoted_support(self):
        for citation in ("951 F.2d 1128 (1991)", "951 F.2d 1128, complete verified text"):
            with self.subTest(citation=citation):
                doc, sources = self.document(citation, "Opinion: 951 F.2d 1128.")
                with self.assertRaisesRegex(ValueError, "whole citation is absent"):
                    check_historical_document(doc, sources)

    def test_legitimate_supreme_court_and_statutory_citations_remain_valid(self):
        for citation, kind in (("506 U.S. 357 (1993)", "opinion"),
                               ("28 U.S.C. § 2254(d)", "statute"),
                               ("OT1991 Journal", "court_journal")):
            with self.subTest(citation=citation):
                doc, sources = self.document(citation, f"Source label: {citation}.", kind)
                check_historical_document(doc, sources)

    def test_unknown_locations_preserve_qualified_documents_without_inventing_urls(self):
        root = AREA.parents[1]
        historical = json.loads((AREA / "catalogues/OT1992/historical-sources.json").read_text())
        documents = [doc for case in historical["cases"] for doc in case["documents"]
                     if doc["url"] is None and doc["repository_path"] is None]
        self.assertEqual(len(documents), 4)
        sources = pilot.Sources(root)
        for doc in documents:
            with self.subTest(document=doc["document_id"]):
                before = deepcopy(doc)
                check_historical_document(doc, sources)
                self.assertEqual(doc, before)
                self.assertTrue(any("no url" in note.casefold() or "do not record" in note.casefold()
                                    for note in doc["notes"]))
                invented = deepcopy(doc)
                invented.update(url="https://example.org/reconstructed-from-citation", url_basis="explicit_url")
                with self.assertRaisesRegex(ValueError, "exact URL is absent"):
                    check_historical_document(invented, sources)

    def test_unknown_citation_can_stay_null(self):
        doc, sources = self.document(None, "Lower opinion located; its reporter citation is not recorded.")
        check_historical_document(doc, sources)
        self.assertIsNone(doc["citation"])

    def test_full_term_build_rejects_inherited_citation_before_publication(self):
        fixture = fixtures.OT1992Tests(methodName="runTest")
        self.addCleanup(fixture.doCleanups)
        fixture.setUp()
        historical = json.loads(fixture.historical_path.read_text())
        case = next(case for case in historical["cases"] if "Dobbs" in case["record_path"])
        document = next(doc for doc in case["documents"] if doc["document_type"] == "lower_court_opinion")
        document["citation"] = case["citation"]
        fixture.fixture.write_json(fixture.historical_path, historical)
        with self.assertRaisesRegex(pilot.PilotError, "lower-court opinion cannot inherit"):
            pilot.build(fixture.root, catalogue="OT1992")
        self.assertFalse(fixture.pointer_path.exists())
        self.assertEqual(json.loads(fixture.historical_path.read_text()), historical)


if __name__ == "__main__":
    unittest.main()
