"""Copy the relevant historical text from authenticated official PDFs.

Run with python -B. This writes only beside this script; no source text is retyped.
"""
from pathlib import Path
import hashlib
import json
import pymupdf

ROOT = Path(__file__).resolve().parent
SOURCES = {
    "USCODE-1995-title28-appendix.pdf": "https://www.govinfo.gov/content/pkg/USCODE-1995-title28/pdf/.pdf",
    "USCODE-1995-title28-mods.xml": "https://www.govinfo.gov/metadata/pkg/USCODE-1995-title28/mods.xml",
    "FRAP-1996-amendments-517US1255.pdf": "https://www.govinfo.gov/content/pkg/USREPORTS-517/pdf/USREPORTS-517-BackMatter-3.pdf",
    "FRCP-1996-amendments-517US1277.pdf": "https://tile.loc.gov/storage-services/service/ll/usrep/usrep517/usrep5171277/usrep5171277.pdf",
}

doc = pymupdf.open(ROOT / "USCODE-1995-title28-appendix.pdf")
page42 = doc[41].get_text()
page115 = doc[114].get_text()
page116 = doc[115].get_text()
frap = page42[page42.index("Rule 43. Substitution of parties"):page42.index("Rule 44. Cases involving")]
frcp = page115[page115.index("Rule 25. Substitution of Parties"):]
frcp += "\n[PDF page boundary; continuation of Rule 25 notes]\n" + page116[:page116.index("V. DEPOSITIONS AND DISCOVERY")]
frap_c = frap[frap.index("(c) Public officers;"):frap.index("(As amended")]
frcp_d = frcp[frcp.index("(d) PUBLIC OFFICERS;"):frcp.index("(As amended")]

extracts = {
    "FRAP43-1996-operative-full-rule-and-notes.txt": frap,
    "FRAP43c-1996-operative-exact-extract.txt": frap_c,
    "FRCP25-1996-operative-full-rule-and-notes.txt": frcp,
    "FRCP25d-1996-operative-exact-extract.txt": frcp_d,
    "USCODE-1995-rule-edition-pages.txt": doc[2].get_text() + "\n[PDF page boundary]\n" + doc[46].get_text(),
}
for name in ("FRAP-1996-amendments-517US1255.pdf", "FRCP-1996-amendments-517US1277.pdf"):
    with pymupdf.open(ROOT / name) as amendments:
        extracts[name.replace(".pdf", "-full-text.txt")] = "\n[PDF page boundary]\n".join(page.get_text() for page in amendments)

for name, text in extracts.items():
    (ROOT / name).write_bytes(text.encode("utf-8"))

manifest = {
    "legal_cutoff": "1996-11-04",
    "edition": "United States Code, 1994 Edition, Supplement I (1995), Title 28 appendix; rules as amended to January 16, 1996",
    "copy_method": "PyMuPDF page.get_text(), then literal substring boundaries; no manual retyping, dehyphenation, punctuation correction, or whitespace normalization. Bracketed page-boundary labels are editorial.",
    "rule_pages_one_based": {"FRAP43": [42], "FRCP25": [115, 116], "edition_headings": [3, 47]},
    "sources": [],
    "derived": [],
}
for name, url in SOURCES.items():
    data = (ROOT / name).read_bytes()
    manifest["sources"].append({"path": name, "url": url, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
for name in list(extracts) + [Path(__file__).name]:
    data = (ROOT / name).read_bytes()
    manifest["derived"].append({"path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
(ROOT / "OFFICER_RULES_SOURCE_MANIFEST.json").write_bytes((json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
print(json.dumps(manifest, indent=2, ensure_ascii=False))
