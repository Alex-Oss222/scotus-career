"""Security and progressive-enhancement checks for the catalogue browser."""

from copy import deepcopy
from html.parser import HTMLParser
import importlib.util
import json
import os
from pathlib import Path
import shutil
import unittest


MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "presentation.py"
SPEC = importlib.util.spec_from_file_location("library_presentation", MODULE_PATH)
presentation = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(presentation)


class Document(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.elements = []
        self.data = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))

    def handle_data(self, value):
        self.data.append(value)

    def tagged(self, tag):
        return [attrs for name, attrs in self.elements if name == tag]


def fixture():
    return {
        "schema_version": 2,
        "development_only": True,
        "production_integration": False,
        "terms": [{"term": "OT1991"}, {"term": "OT1995"}],
        "records": [
            {
                "record_id": "ot1991-case-1",
                "term": "OT1991",
                "kind": "court_event",
                "title": "Case One v. State",
                "path": "terms/OT1991/records/case-one.md",
                "sha256": "a" * 64,
                "metadata": {"Case and dockets": "Case One, 90-123", "Result": "Affirmed"},
                "event_date": "1991-10-07",
                "effective_date": None,
                "chunks": [1, 2],
                "inventory_refs": [{"path": "terms/OT1991/case-list.md", "line": 11, "caption": "Case One", "dockets": "90-123", "area_of_law": "Civil procedure"}],
                "references": [{"kind": "external", "target": "https://example.org/historical?a=1&b=2", "source_path": "terms/OT1991/records/case-one.md", "line": 15, "section": "Sources", "review_status": "unverified", "material_kind": "historical"}],
                "citations": [{"text": "410 U.S. 113", "source_path": "terms/OT1991/records/case-one.md", "line": 19, "section": "Authority"}],
                "sections": [{"title": "Public Projection", "line": 30, "level": 2}],
                "warnings": ["A source pointer has not been reviewed."],
                "curation": {"aliases": ["The Pinebridge matter"], "notes": ["Check the attached hearing transcript."], "extensions": {"custom": {"memo": "preserved extension data"}}},
            },
            {
                "record_id": "ot1995-source-2",
                "term": "OT1995",
                "kind": "admitted_source",
                "title": "Admitted lower-court source",
                "path": "terms/OT1995/records/admitted-source.md",
                "event_date": None,
                "effective_date": "1995-10-01",
                "chunks": [10],
                "references": [{"kind": "repository", "target": "terms/OT1995/briefs/OT_1995CHUNK10.md#sources", "source_path": "terms/OT1995/records/admitted-source.md", "line": 20, "review_status": "unverified", "material_kind": "mixed"}],
                "citations": [],
            },
        ],
        "carryovers": [{"term": "OT1995", "path": "state/STANDING_STATE.md", "line": 24, "raw": "An unresolved matter carried forward."}],
        "warnings": ["Historical source availability has not been checked."],
    }


class PresentationTests(unittest.TestCase):
    def test_all_records_pointers_and_citations_exist_without_javascript(self):
        doc = Document(presentation.render(fixture()))
        cards = doc.tagged("article")
        self.assertEqual([card["id"] for card in cards], ["ot1991-case-1", "ot1995-source-2"])
        self.assertTrue(all("hidden" not in card for card in cards))
        text = " ".join(doc.data)
        for value in ("Case One v. State", "Admitted lower-court source", "410 U.S. 113", "An unresolved matter carried forward."):
            self.assertIn(value, text)
        self.assertEqual(len(doc.tagged("noscript")), 1)
        self.assertIn("../../../../terms/OT1991/records/case-one.md", [a["href"] for a in doc.tagged("a")])

    def test_search_includes_docket_area_citation_and_source_location(self):
        card = Document(presentation.render(fixture())).tagged("article")[0]
        for value in ("90-123", "Civil procedure", "410 U.S. 113", "https://example.org/historical", "Sources"):
            self.assertIn(value, card["data-search"])

    def test_operator_aliases_and_notes_are_static_searchable_and_separate(self):
        doc = Document(presentation.render(fixture()))
        text = " ".join(doc.data)
        for value in ("The Pinebridge matter", "Check the attached hearing transcript."):
            self.assertIn(value, text)
            self.assertIn(value, doc.tagged("article")[0]["data-search"])
        self.assertIn("Operator annotations", text)
        self.assertIn("separate from the canonical record", text)
        self.assertIn("do not establish identity, legal authority, or precedent treatment", text)
        self.assertNotIn("preserved extension data", text)
        self.assertNotIn("preserved extension data", doc.tagged("article")[0]["data-search"])

    def test_accessible_disabled_controls_and_live_result_count(self):
        doc = Document(presentation.render(fixture()))
        controls = doc.tagged("input") + doc.tagged("select")
        labels = {item["for"] for item in doc.tagged("label")}
        self.assertEqual({control["id"] for control in controls}, labels)
        self.assertTrue(all("disabled" in control for control in controls))
        status = next(attrs for _, attrs in doc.elements if attrs.get("id") == "results-summary")
        self.assertEqual(status["aria-live"], "polite")
        self.assertEqual(status["role"], "status")

    def test_filter_values_preserve_multichunk_and_record_kind(self):
        cards = Document(presentation.render(fixture())).tagged("article")
        self.assertEqual(cards[0]["data-chunks"], "|1|2|")
        self.assertEqual(cards[1]["data-chunks"], "|10|")
        self.assertEqual(cards[1]["data-kind"], "admitted_source")

    def test_unsafe_external_urls_never_become_links(self):
        bad = [
            "javascript:alert(1)", "data:text/html,hello", "//evil.example/path",
            "https://user:secret@example.org/path", "https://user@example.org/path",
            "https://example.org\\@evil.example/", "https://example.org/a\nb",
            "https://example.org/%0aevil", "https://example.org:invalid/", "https://[bad/",
            "file:///tmp/file", "https:///no-host", "https://example.org/a b",
        ]
        for target in bad:
            with self.subTest(target=target):
                value = fixture()
                value["records"][0]["references"][0]["target"] = target
                links = Document(presentation.render(value)).tagged("a")
                self.assertNotIn(target, [a["href"] for a in links])
                self.assertIsNone(presentation._external_href(target))

    def test_http_and_https_pointers_remain_clickable_without_referrer(self):
        for target in ("https://example.org/a?x=1&b=2", "http://example.org/a", "https://example.org:8443/a"):
            with self.subTest(target=target):
                value = fixture()
                value["records"][0]["references"][0]["target"] = target
                link = next(a for a in Document(presentation.render(value)).tagged("a") if a["href"] == target)
                self.assertIn("noreferrer", link["rel"])
                self.assertIn("noopener", link["rel"])

    def test_repository_links_reject_escape_and_absolute_paths(self):
        for target in ("../secret", "/etc/passwd", "terms/../secret", "terms//file.md", "terms/./file.md", "terms\\secret", "C:/file.md", "https://evil.example", "terms/%2e%2e/secret", "terms/file?query=1", "terms/fi\x00le"):
            with self.subTest(target=target):
                self.assertIsNone(presentation._repository_href(target, "../../../../"))

    def test_repository_names_are_quoted_and_explicit_fragment_preserved(self):
        self.assertEqual(
            presentation._repository_href("terms/OT1995/records/a name & café.md#public-projection", "../../../../"),
            "../../../../terms/OT1995/records/a%20name%20%26%20caf%C3%A9.md#public-projection",
        )

    def test_line_labels_do_not_invent_markdown_line_anchors(self):
        source = presentation.render(fixture())
        self.assertIn("line 19", source)
        self.assertNotIn("#L19", source)

    def test_untrusted_text_cannot_create_elements_attributes_or_scripts(self):
        payload = '\"><img src=x onerror=alert(1)></script><script>alert(2)</script>&'
        value = fixture()
        first = value["records"][0]
        first.update(title=payload, record_id=payload, term=payload, warnings=[payload], sha256=payload)
        first["metadata"] = {payload: payload}
        first["inventory_refs"][0].update(caption=payload, area_of_law=payload, line=payload)
        first["references"][0].update(target=payload, section=payload, review_status=payload)
        first["citations"][0].update(text=payload, section=payload, line=payload)
        first["sections"][0].update(title=payload, line=payload)
        first["curation"] = {"aliases": [payload], "notes": [payload], "extensions": {"custom": {"memo": payload}}}
        value["warnings"] = [payload]
        value["carryovers"] = [{"raw": payload, "path": payload, "line": payload}]
        value["schema_version"] = payload
        doc = Document(presentation.render(value))
        self.assertEqual(len(doc.tagged("script")), 1)
        self.assertEqual(doc.tagged("img"), [])
        self.assertTrue(all(not key.startswith("on") for _, attrs in doc.elements for key in attrs))
        self.assertIn(payload, " ".join(doc.data))
        self.assertEqual(doc.tagged("article")[0]["id"], payload)

    def test_javascript_has_no_data_interpolation_or_innerhtml_updates(self):
        value = fixture()
        value["records"][0]["title"] = "UNIQUE-DATA-MARKER"
        source = presentation.render(value)
        script = source.rsplit("<script>", 1)[1].split("</script>", 1)[0]
        self.assertNotIn("UNIQUE-DATA-MARKER", script)
        self.assertNotIn("innerHTML", script)
        self.assertIn("textContent", script)

    def test_no_remote_scripts_styles_fonts_or_automatic_fetches(self):
        source = presentation.render(fixture())
        doc = Document(source)
        self.assertTrue(all("src" not in attrs for attrs in doc.tagged("script")))
        self.assertEqual(doc.tagged("link"), [])
        self.assertNotIn("@import", source)
        self.assertNotIn("fetch(", source)
        self.assertNotIn("XMLHttpRequest", source)

    def test_development_and_material_limits_are_explicit(self):
        text = " ".join(Document(presentation.render(fixture())).data)
        for phrase in ("Production integration is disabled", "Historical pointers are unverified", "static view cannot check freshness", "Full record: mixed / internal material", "Citation mentions", "Admitted source"):
            self.assertIn(phrase, text)

    def test_render_does_not_mutate_catalogue(self):
        value = fixture()
        before = deepcopy(value)
        presentation.render(value)
        self.assertEqual(value, before)

    def test_render_is_identical_after_sorted_json_roundtrip(self):
        value = fixture()
        value["records"][0]["metadata"] = {
            "Version / lineage": "Original",
            "Result": "Affirmed",
            "Event and date": "Decision, 1991-10-07",
            "Case and dockets": "Case One, 90-123",
        }
        roundtripped = json.loads(json.dumps(value, sort_keys=True))
        self.assertEqual(presentation.render(value), presentation.render(roundtripped))

    def test_empty_catalogue_and_missing_optional_fields_render(self):
        for value in ({}, {"records": [{"record_id": "empty", "path": "terms/OT1991/records/a.md"}]}):
            with self.subTest(value=value):
                doc = Document(presentation.render(value))
                self.assertEqual(len(doc.tagged("html")), 1)
                self.assertEqual(len(doc.tagged("main")), 1)
        self.assertIn("This snapshot contains no records", presentation.render({}))

    def test_invalid_repository_prefix_is_rejected(self):
        for prefix in ("javascript:alert(1)", "//evil.example/", "../../x/", '\"><script>', None):
            with self.subTest(prefix=prefix):
                with self.assertRaises(ValueError):
                    presentation.render(fixture(), prefix)
        self.assertIn('href="../../terms/', presentation.render(fixture(), "../../"))


@unittest.skipUnless(os.environ.get("CASE_LIBRARY_BROWSER_TESTS") == "1", "optional browser tests; set CASE_LIBRARY_BROWSER_TESTS=1")
class BrowserTests(unittest.TestCase):
    """Optional real-browser checks; the library itself needs no browser package."""

    @classmethod
    def setUpClass(cls):
        try:
            from playwright.sync_api import sync_playwright
        except ImportError as error:
            raise unittest.SkipTest("Playwright is not installed") from error
        cls.playwright = sync_playwright().start()
        executable = os.environ.get("CASE_LIBRARY_CHROMIUM") or shutil.which("chromium")
        cls.browser = cls.playwright.chromium.launch(executable_path=executable)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def setUp(self):
        self.page = self.browser.new_page()
        self.errors = []
        self.page.on("pageerror", lambda error: self.errors.append(str(error)))
        self.page.set_content(presentation.render(fixture()))

    def tearDown(self):
        self.page.close()
        self.assertEqual(self.errors, [])

    def test_combined_filters_and_exact_chunk_membership(self):
        self.page.locator("#chunk-filter").select_option("1")
        self.assertEqual(self.page.locator(".record:visible").count(), 1)
        self.assertEqual(self.page.locator(".record:visible").get_attribute("id"), "ot1991-case-1")
        self.page.locator("#kind-filter").select_option("admitted_source")
        self.assertEqual(self.page.locator(".record:visible").count(), 0)
        self.assertTrue(self.page.locator("#empty-state").is_visible())
        self.page.locator("#clear-filters").click()
        self.assertEqual(self.page.locator(".record:visible").count(), 2)
        self.page.locator("#term-filter").select_option("OT1995")
        self.page.locator("#chunk-filter").select_option("10")
        self.page.locator("#kind-filter").select_option("admitted_source")
        self.assertEqual(self.page.locator(".record:visible").count(), 1)

    def test_search_case_docket_citation_and_source_with_multiple_words(self):
        for query in ("CASE ONE", "90-123", "410 U.S. 113", "civil procedure", "historical example.org"):
            with self.subTest(query=query):
                self.page.locator("#search").fill(query)
                self.assertEqual(self.page.locator(".record:visible").count(), 1)
                self.assertEqual(self.page.locator(".record:visible").get_attribute("id"), "ot1991-case-1")
        self.page.locator("#search").fill("  missing-title  ")
        self.assertEqual(self.page.locator("#results-summary").inner_text(), "0 of 2 records shown")

    def test_search_finds_operator_alias_and_note(self):
        for query in ("Pinebridge", "hearing transcript"):
            with self.subTest(query=query):
                self.page.locator("#search").fill(query)
                self.assertEqual(self.page.locator(".record:visible").count(), 1)
                self.assertEqual(self.page.locator(".record:visible").get_attribute("id"), "ot1991-case-1")

    def test_term_shortcut_and_hash_reveal_hidden_record(self):
        self.page.locator('[data-term-shortcut="OT1995"]').click()
        self.assertEqual(self.page.locator("#term-filter").input_value(), "OT1995")
        self.page.evaluate("window.location.hash = 'ot1991-case-1'")
        self.page.wait_for_function("!document.getElementById('ot1991-case-1').hidden")
        self.assertEqual(self.page.locator("#term-filter").input_value(), "")

    def test_no_javascript_still_exposes_all_records_and_sources(self):
        context = self.browser.new_context(java_script_enabled=False)
        try:
            page = context.new_page()
            page.set_content(presentation.render(fixture()))
            self.assertEqual(page.locator(".record:visible").count(), 2)
            self.assertTrue(page.locator("noscript").is_visible())
            self.assertTrue(page.locator("#search").is_disabled())
            page.locator(".record").first.locator("summary", has_text="Source pointers").click()
            self.assertTrue(page.get_by_role("link", name="https://example.org/historical?a=1&b=2", exact=True).is_visible())
            page.locator(".record").first.locator("summary", has_text="Operator annotations").click()
            self.assertTrue(page.get_by_text("The Pinebridge matter", exact=True).is_visible())
            self.assertTrue(page.get_by_text("Check the attached hearing transcript.", exact=True).is_visible())
        finally:
            context.close()

    def test_untrusted_metadata_stays_text_and_does_not_execute(self):
        value = fixture()
        value["records"][0]["title"] = '<img src=x onerror="window.injected=true"></script><script>window.injected=true</script>'
        value["records"][0]["references"][0]["target"] = "javascript:window.injected=true"
        value["records"][0]["curation"] = {"aliases": ['<img src=x onerror="window.injected=true">'], "notes": ['</script><script>window.injected=true</script>'], "extensions": {}}
        self.page.set_content(presentation.render(value))
        self.assertEqual(self.page.locator("img").count(), 0)
        self.assertEqual(self.page.locator("script").count(), 1)
        self.assertFalse(self.page.evaluate("Boolean(window.injected)"))
        self.assertEqual(self.page.locator('a[href^="javascript:"]').count(), 0)

    def test_mobile_layout_fits_with_long_source_and_metadata(self):
        value = fixture()
        value["records"][0]["metadata"]["Long field"] = "x" * 1000
        value["records"][0]["references"][0]["target"] = "https://example.org/" + "x" * 1000
        self.page.set_content(presentation.render(value))
        self.page.locator("details").evaluate_all("nodes => nodes.forEach(node => node.open = true)")
        for width in (320, 375, 768, 1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width": width, "height": 900})
                self.assertTrue(self.page.evaluate("document.documentElement.scrollWidth <= window.innerWidth"))


if __name__ == "__main__":
    unittest.main()
