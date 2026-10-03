# Shieh historical primary-source archive

Comparator-only source archive. Supply to a reconciliation context only after the independent freeze. Source-only archival inspection and inventory are permitted before that gate.

Official report: https://www.govinfo.gov/content/pkg/USREPORTS-517/pdf/USREPORTS-517-343.pdf

`usreports_517_343.pdf` is a genuine PDF with a verified `%PDF-` signature and Shieh v. Kakita title content. Its two pages cover 517 U.S. 343–344. `usreports_517_343.layout.txt` preserves the complete unfiltered output of `pdftotext -layout`, without page selection. `usreports_517_343.pdfinfo.txt` records the PDF inspection output.

The report prints a decision date of April 1, 1996. Page 343 identifies No. 95–7587, Shieh v. Kakita et al.; its asterisk note identifies companion No. 95–7588, Shieh v. United States Court of Appeals for the Ninth Circuit, and No. 95–7589, Shieh v. Krieger et al. That note is included in the preserved extraction.

Actual writing inventory: reporter syllabus on page 343; per curiam opinion on pages 343–344; Justice Stevens's dissent on page 344. The extraction includes the complete dissent and its references.

Cornell's expected primary-docket URLs were attempted individually: `95-7587.ZS.html`, `95-7587.ZO.html`, and `95-7587.ZD.html`. Each returned HTTP 404 with a Page not found HTML document. Those responses and their extracted error-page text are retained as failed retrieval evidence, not primary opinion text. These attempts do not establish absence from every possible Cornell URL. The official Reports source supplies the complete document.

Every retrieval has headers and metadata recording URL, timestamp, HTTP status, content type, byte count, and SHA-256 hash. Metadata also records extraction methods and hashes. `manifest.json` records the source and writing inventory; `checksums.sha256` covers every other archived file.

Reading scope: the complete two-page extracted text was read to verify source identity, writing inventory, reporter coverage, and notes. No legal conclusions, vote modeling, reconciliation, or claim of full substantive legal analysis is included.

The cloud onboarding setup skill was already applied to tool readiness. Existing curl, pdftotext, pdfinfo, and Python sufficed. No installation or environment configuration changes were needed.
