# Rutledge historical primary-source archive

Comparator-only archive for delivery after the independent freeze. No legal conclusions, modeling, or reconciliation are included.

Official U.S. Reports source: https://www.govinfo.gov/content/pkg/USREPORTS-517/pdf/USREPORTS-517-292.pdf

The PDF has a verified `%PDF-` signature and meaningful Rutledge title content. All 16 PDF pages are preserved in `usreports_517_292.layout.txt`, produced by `pdftotext -layout` without page selection. `usreports_517_292.pdfinfo.txt` records PDF inspection output.

Cornell's syllabus was fetched first: https://www.law.cornell.edu/supct/html/94-8769.ZS.html

Its writing inventory identifies one opinion, Justice Stevens for a unanimous Court, with no separate writings identified. That opinion was then fetched individually: https://www.law.cornell.edu/supct/html/94-8769.ZO.html

Both Cornell pages are preserved as raw HTML and complete extracted text. Each source has response headers and a metadata JSON containing its URL, retrieval time, HTTP status, content type, byte count, SHA-256 hash, and extraction details. `manifest.json` records the inventory. `checksums.sha256` covers every archived file other than itself.

Review scope: the syllabus was read for the writing inventory, and document title, format, page counts, and extraction structure were checked. This archive does not claim a substantive full reading of the complete opinion or PDF.

The cloud onboarding setup skill was applied to tool readiness. Existing curl, pdftotext, pdfinfo, and Python sufficed. No installation or environment configuration changes were needed.
