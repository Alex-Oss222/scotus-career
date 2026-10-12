"""Tests for the case library. Run from the repository root:

    python -m unittest discover -s development/case-library/tests
"""
from __future__ import annotations

import contextlib
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))
import library  # noqa: E402

HEADER = "| No. | Chunk | Caption | Docket(s) | Event date | Event type | Category | Area of law |\n|---:|---:|---|---|---|---|---|---|\n"

CASE_LIST = f"""# OT1991 case index

{HEADER}| 1 | 1 | Planned Parenthood of Southeastern Pennsylvania v. Casey | 91-744; 91-902 | 1992-06-29 | Merits decision | MERITS | Abortion |
| 2 | 1 | Vasquez v. Harris | A-766 | 1992-04-21 | Application to vacate execution stay | APPLICATION | Capital habeas |

{HEADER}| 3 | 2 | Vasquez v. Harris | A-768 | 1992-04-21 | Application to vacate execution stay | APPLICATION | Capital habeas |
| 4 | 2 | Benten v. Kessler | A-40 | 1992-07-17 | Application to vacate stay | APPLICATION | Abortion |
| 5 | 2 | Earlier v. Matter | 91-1 | 1992-01-10 | Merits decision | MERITS | Other |
"""

RECORDS = {
    "Planned_Parenthood_v_Casey_merits_1992-06-29.md":
        "# Canonical Decision Record — Planned Parenthood of Southeastern Pennsylvania v. Casey\n\n"
        "- **Case:** Planned Parenthood of Southeastern Pennsylvania v. Casey, 505 U.S. 833 (1992); Nos. 91-744 and 91-902.\n"
        "Casey decides itself here; this is not a later mention.\n"
        "See [the master build](../../../stone/BUILD.md) and [history](https://www.law.cornell.edu/supremecourt/text/505/833).\n",
    "Vasquez_v_Harris_A-766_application_1992-04-21.md":
        "# Record — Vasquez v. Harris, No. A-766\n\nApplication No. A-766; also mentions A-768 in sequence.\n",
    "Vasquez_v_Harris_A-768_application_1992-04-21.md":
        "# Record — Vasquez v. Harris, No. A-768\n\nApplication No. A-768.\n",
    "Benten_v_Kessler_application_1992-07-17.md":
        "# Record — Benten v. Kessler, No. A-40\n\n"
        "The simulated Casey standard governs.\n"
        "Historical Casey language is comparison only.\n"
        "Casey, 505 U.S., at 846, is quoted.\n"
        "West Virginia University Hospitals v. Casey is a different case.\n"
        "The planned review, the planned hearing and the planned order were dropped.\n",
    "Earlier_v_Matter_merits_1992-01-10.md":
        "# Record — Earlier v. Matter, No. 91-1\n\nCasey is mentioned before it was decided.\n",
}


class Fixture:
    def __init__(self):
        self.dir = Path(tempfile.mkdtemp())
        records = self.dir / "terms" / "OT1991" / "records"
        records.mkdir(parents=True)
        (self.dir / "terms" / "OT1991" / "case-list.md").write_text(CASE_LIST, encoding="utf-8")
        for name, text in RECORDS.items():
            (records / name).write_text(text, encoding="utf-8")
        holdings = self.dir / "state" / "holdings"
        holdings.mkdir(parents=True)
        (holdings / "civil-rights.md").write_text(
            "#### Planned Parenthood of Southeastern Pennsylvania v. Casey, 505 U.S. 833 (1992)\n", encoding="utf-8")
        (self.dir / "stone").mkdir()
        (self.dir / "stone" / "BUILD.md").write_text("locked", encoding="utf-8")

    def close(self):
        shutil.rmtree(self.dir, ignore_errors=True)


class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.fx = Fixture()
        self.lib = library.Library(self.fx.dir)

    def tearDown(self):
        self.fx.close()

    def test_rows_map_to_records_across_chunk_tables(self):
        self.assertEqual(len(self.lib.matters), 5)
        self.assertFalse(self.lib.unmatched_rows)
        self.assertFalse(self.lib.conflicts)
        self.assertEqual(self.lib.by_key["OT1991-2"].records, ["terms/OT1991/records/Vasquez_v_Harris_A-766_application_1992-04-21.md"])
        self.assertEqual(self.lib.by_key["OT1991-3"].records, ["terms/OT1991/records/Vasquez_v_Harris_A-768_application_1992-04-21.md"])
        self.assertEqual(self.lib.by_key["OT1991-3"].chunk, 2)

    def test_citation_comes_from_holdings_and_record(self):
        self.assertIn("505 U.S. 833", self.lib.by_key["OT1991-1"].cites)
        self.assertTrue(self.lib.by_key["OT1991-1"].holdings[0].startswith("state/holdings/civil-rights.md:"))

    def test_cited_by_names_tags_and_exclusions(self):
        hits = self.lib.cited_by(self.lib.by_key["OT1991-1"], "records")
        by_line: dict = {}
        for h in hits:
            by_line.setdefault((Path(h.path).name, h.line), []).append(h)
        benten = "Benten_v_Kessler_application_1992-07-17.md"
        self.assertEqual({h.tag for h in by_line[(benten, 3)]}, {"simulated"})
        self.assertEqual({h.tag for h in by_line[(benten, 4)]}, {"historical"})
        self.assertIn("citation", {h.how for h in by_line[(benten, 5)]})   # 505 U.S., at 846
        self.assertNotIn((benten, 6), by_line)                             # a different Casey case
        self.assertFalse(any("Planned_Parenthood" in h.path for h in hits))  # its own Record
        earlier = [h for h in hits if "Earlier" in h.path]
        self.assertEqual([h.tag for h in earlier], ["before-decision"])

    def test_show_withholds_stone_links_and_never_reads_stone(self):
        opened = []
        real_read_text = Path.read_text

        def spy(path, *args, **kwargs):
            opened.append(Path(path).resolve())
            return real_read_text(path, *args, **kwargs)

        Path.read_text = spy
        try:
            lib = library.Library(self.fx.dir)
            outside, inside, withheld = lib.links(lib.by_key["OT1991-1"])
            for key in lib.by_key:
                lib.cited_by(lib.by_key[key], "all")
        finally:
            Path.read_text = real_read_text
        self.assertEqual(withheld, 1)
        self.assertFalse(any(p.startswith("stone/") for p in inside))
        self.assertIn("www.law.cornell.edu", outside)
        stone = (self.fx.dir / "stone").resolve()
        self.assertTrue(opened)
        self.assertFalse(any(p == stone or stone in p.parents for p in opened))

    def test_ordinary_word_is_not_a_name(self):
        idx = self.lib.alias_index()
        self.assertIn("casey", idx)
        self.assertNotIn("planned", idx)  # "Planned" is the start of an organization's name

    def test_find_by_docket_citation_and_chunk(self):
        self.assertEqual([m.key for m in self.lib.find("91-744")], ["OT1991-1"])
        self.assertEqual([m.key for m in self.lib.find("505 U.S. 833")], ["OT1991-1"])
        self.assertEqual(sorted(m.key for m in self.lib.find("", chunk=2)), ["OT1991-3", "OT1991-4", "OT1991-5"])

    def test_withholding_judges_path_parts(self):
        doc = "terms/OT1991/records/x.md"
        self.assertNotIn("STONE_FULL", library.withhold("see [r](../../../stone/STONE_FULL.md#m) here", doc))
        self.assertNotIn("Y.md", library.withhold("a scotus-career/stone/Y.md path", doc))
        kept = "Stone/Breyer and [Stone v. INS](../records/Stone_v_INS.md) and milestone/x"
        self.assertEqual(library.withhold(kept, doc), kept)

    def test_party_names_with_commas_and_whole_captions(self):
        parties = library.split_parties("Planned Parenthood, Sioux Falls Clinic v. Miller")
        self.assertEqual(parties[0][0], ["Planned", "Parenthood", "Sioux", "Falls", "Clinic"])
        m = library.CAPTION.search("Bray v. Alexandria Women's Health Clinic, 506 U.S. 263")
        self.assertIn("Women's Health Clinic", m[2])

    def test_command_line_json(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = library.main(["--root", str(self.fx.dir), "cited-by", "OT1991-1", "--json"])
        data = json.loads(out.getvalue())
        self.assertEqual(code, 0)
        self.assertEqual(data["matter"]["key"], "OT1991-1")
        self.assertTrue(data["mentions"])


REPO = Path(os.environ.get("CASE_LIBRARY_ROOT", Path(__file__).resolve().parents[3]))


@unittest.skipUnless((REPO / "terms" / "OT1991" / "case-list.md").is_file(), "repository terms not present")
class RepositorySmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lib = library.Library(REPO)

    def test_every_row_of_a_run_term_has_its_record(self):
        self.assertFalse(self.lib.unmatched_rows, [m.key for m in self.lib.unmatched_rows[:5]])
        self.assertFalse(self.lib.conflicts, self.lib.conflicts[:5])

    def test_casey_is_traced_by_name(self):
        casey = [m for m in self.lib.find("Planned Parenthood of Southeastern Pennsylvania v. Casey")][0]
        docs = {h.path for h in self.lib.cited_by(casey, "records") if h.tag != "before-decision" and not h.ambiguous}
        self.assertGreaterEqual(len(docs), 10)


if __name__ == "__main__":
    unittest.main()
