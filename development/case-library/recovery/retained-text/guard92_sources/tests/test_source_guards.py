"""Historical pointer checks use local evidence without modifying any source."""
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


class QuotedSources:
    """Small read-only witness: altered or invented source quotations fail."""
    def __init__(self, files):
        self.files = files

    def evidence(self, items):
        for item in items:
            if item["path"] not in self.files or item["quote"] not in self.files[item["path"]]:
                raise ValueError("Evidence no longer matches its local source")


class SourceGuardTests(unittest.TestCase):
    def document(self, quote=None):
        url = "https://example.org/cases/1992/one/"
        quote = quote or f"Source: [opinion]({url}). Decision June 1, 1992."
        evidence = {"path": "terms/OT1991/records/example.md", "locator": "L1", "quote": quote}
        doc = {"document_id": "example-opinion", "url": url, "url_basis": "explicit_url",
               "repository_path": None, "document_date": "1992-06-01", "evidence": [evidence],
               "notes": ["Remote source not freshly verified."]}
        return doc, QuotedSources({evidence["path"]: quote})

    def test_current_pilot_and_full_term_sources_pass_without_network_or_mutation(self):
        root = AREA.parents[1]
        with patch("urllib.request.urlopen") as request:
            for scope, expected in ((pilot.PILOT, 34), (pilot.catalogue_path("OT1991"), 375)):
                with self.subTest(scope=scope):
                    path = root / scope / "historical-sources.json"
                    before = path.read_bytes()
                    historical = json.loads(before)
                    original = deepcopy(historical)
                    sources = pilot.Sources(root)
                    documents = [doc for case in historical["cases"] for doc in case["documents"]]
                    self.assertEqual(len(documents), expected)
                    for doc in documents:
                        check_historical_document(doc, sources)
                    self.assertEqual(historical, original)
                    self.assertEqual(path.read_bytes(), before)
            request.assert_not_called()

    def test_url_prefix_or_homepage_cannot_replace_recorded_document(self):
        for replacement in ("https://example.org/", "https://example.org/cases/1992/", "https://example.org/cases/1992/one"):
            with self.subTest(replacement=replacement):
                doc, sources = self.document()
                doc["url"] = replacement
                with self.assertRaisesRegex(ValueError, "exact URL is absent"):
                    check_historical_document(doc, sources)

    def test_markdown_punctuation_and_balanced_url_parentheses_are_supported(self):
        for url, quote in (
            ("https://example.org/opinion.pdf", "[Official](https://example.org/opinion.pdf),read in full."),
            ("https://example.org/case_(one)", "[Opinion](https://example.org/case_(one))."),
            ("https://example.org/opinion.pdf?raw=1&view=true", "`https://example.org/opinion.pdf?raw=1&view=true`; source."),
        ):
            with self.subTest(url=url):
                doc, sources = self.document(quote)
                doc.update(url=url, document_date=None)
                check_historical_document(doc, sources)

    def test_shared_quote_preserves_each_exact_url_and_existing_qualification(self):
        quote = "Orders: https://example.org/order1.pdf and https://example.org/order2.pdf."
        for url in ("https://example.org/order1.pdf", "https://example.org/order2.pdf"):
            with self.subTest(url=url):
                doc, sources = self.document(quote)
                doc.update(url=url, document_date=None, notes=["Paired sources; exact attribution remains qualified."])
                before = deepcopy(doc)
                check_historical_document(doc, sources)
                self.assertEqual(doc, before)

    def test_archive_identifiers_must_be_whole_tokens(self):
        quote = "Recorded Archive item: `micro_IA40385013_0208`."
        doc, sources = self.document(quote)
        doc.update(url="https://archive.org/details/micro_IA40385013_0208",
                   url_basis="recorded_archive_identifier", document_date=None)
        check_historical_document(doc, sources)
        for identifier in ("micro_IA40385013", "micro_IA40385013_020", "IA40385013_0208"):
            with self.subTest(identifier=identifier):
                doc["url"] = "https://archive.org/details/" + identifier
                with self.assertRaisesRegex(ValueError, "exact Archive identifier is absent"):
                    check_historical_document(doc, sources)

    def test_local_pointer_must_have_actual_local_link_evidence(self):
        doc, sources = self.document()
        doc["repository_path"] = "terms/OT1991/briefs/unrelated-excerpt.md"
        with self.assertRaisesRegex(ValueError, "exact local target is absent"):
            check_historical_document(doc, sources)
        doc, sources = self.document("Remote link: https://example.org/?path=terms/OT1991/sources/excerpt.pdf")
        doc.update(url=None, url_basis="not_recorded", document_date=None,
                   repository_path="terms/OT1991/sources/excerpt.pdf")
        with self.assertRaisesRegex(ValueError, "exact local target is absent"):
            check_historical_document(doc, sources)
        doc, sources = self.document("Saved at terms/OT1991/sources/excerpt.pdf.backup.")
        doc.update(url=None, url_basis="not_recorded", document_date=None,
                   repository_path="terms/OT1991/sources/excerpt.pdf")
        with self.assertRaisesRegex(ValueError, "exact local target is absent"):
            check_historical_document(doc, sources)

    def test_relative_statutory_excerpt_link_and_explicit_path_are_supported(self):
        path = "terms/OT1991/briefs/CASEY_STATUTE.md"
        for quote in ("Supplied [statute](../briefs/CASEY_STATUTE.md).", f"Supplied text: `{path}`."):
            with self.subTest(quote=quote):
                doc, sources = self.document(quote)
                doc.update(url=None, url_basis="not_recorded", document_date=None, repository_path=path)
                check_historical_document(doc, sources)

    def test_simulated_internal_and_control_files_cannot_be_historical_documents(self):
        paths = [f"terms/OT1991/{folder}/example.md" for folder in
                 ("records", "runtime", "freeze", "output", "render-inputs", "workspace", "entering-law", "close")]
        paths += ["terms/OT1991/workspace.md", "terms/OT1991/case-list.md", "state/HOLDINGS.md",
                  "foundation/ENGINE.md", "development/case-library/README.md", "AGENTS.md"]
        for path in paths:
            with self.subTest(path=path):
                doc, sources = self.document(f"Pointer: `{path}`.")
                doc.update(url=None, url_basis="not_recorded", document_date=None, repository_path=path)
                with self.assertRaisesRegex(ValueError, "historical source cannot target"):
                    check_historical_document(doc, sources)

    def test_missing_date_proof_cannot_be_replaced_by_filename_or_other_year(self):
        for quote in ("Decision June 1.", "Decision June 1, 1993.",
                      "Recorded at terms/OT1991/records/example_1992-06-01.md.",
                      "Source https://example.org/1992-06-01/opinion.pdf",
                      "Source https://example.org/June1,1992/opinion.pdf"):
            with self.subTest(quote=quote):
                doc, sources = self.document(quote)
                doc.update(url=None, url_basis="not_recorded")
                with self.assertRaisesRegex(ValueError, "complete calendar date is absent"):
                    check_historical_document(doc, sources)

    def test_calendar_date_proof_accepts_supported_legacy_typography(self):
        for quote in ("Decided June 1, 1992.", "Decided June1,1992.", "Date: 1992-06-01.",
                      "Issued Jun. 1, 1992.", "Issued Jun 1, 1992."):
            with self.subTest(quote=quote):
                doc, sources = self.document(quote)
                doc.update(url=None, url_basis="not_recorded")
                check_historical_document(doc, sources)

    def test_unknown_date_is_preserved_instead_of_inventing_metadata(self):
        doc, sources = self.document("Decision June 1; year is not supplied in this quotation.")
        doc.update(url=None, url_basis="not_recorded", document_date=None)
        check_historical_document(doc, sources)
        self.assertIsNone(doc["document_date"])

    def test_evidence_must_still_match_the_local_source(self):
        doc, sources = self.document()
        doc["evidence"][0]["quote"] = "Invented https://example.org/cases/1992/one/ dated June 1, 1992."
        with self.assertRaisesRegex(ValueError, "Evidence no longer matches"):
            check_historical_document(doc, sources)

    def test_date_repairs_preserve_document_identity_and_explicit_uncertainty(self):
        historical = json.loads((AREA / "catalogues/OT1991/historical-sources.json").read_text())
        by_id = {doc["document_id"]: doc for case in historical["cases"] for doc in case["documents"]}
        for identifier in ("scotus-a-767-application-to-vacate-stay-1992-04-21-historical-4",
                           "scotus-a-40-district-cap", "scotus-a-40-district-justia"):
            with self.subTest(identifier=identifier):
                self.assertIsNone(by_id[identifier]["document_date"])
                self.assertIn("complete calendar date", " ".join(by_id[identifier]["notes"]))
        self.assertEqual(by_id["scotus-a-877-stay-application-1992-05-20-historical-5"]["document_date"], "1992-05-18")
        self.assertEqual(by_id["scotus-91-155-historical-companion-report"]["document_date"], "1992-06-26")


if __name__ == "__main__":
    unittest.main()
