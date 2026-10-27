# Group B source map and read receipt

Research retrieval: October 27, 2026. In-world cutoff: March 3, 1999 before the action. Storage and retrieval dates are provenance, not Court chronology. Original litigant papers and lower-court opinions may discuss historical post-divergence Supreme Court actions; those passages are not imported. The fresh validator should start with the objective handoff and exact excerpts, using further original research only within the Engine's separation rules.

## Sources recovered

| Source | Saved file | Verification/use |
|---|---|---|
| [Archive collection listing](https://archive.org/advancedsearch.php?q=collection%3Aus-supreme-court&output=json) | `sullivan_archive_listing.json`, `nffe_archive_listing.json`, `germany_archive_listing.json`, `stewart_archive_listing.json` | Four docket/name searches. Sullivan and NFFE items found; no matching Germany original or Stewart 98-1412 item. Full query parameters are retained in each response. |
| [Sullivan records item](https://archive.org/details/micro_IA40385014_0186) | `micro_IA40385014_0186_metadata.json`; `sullivan_02.*`, `sullivan_07.*`, `sullivan_08.*`, `sullivan_10.*`; additional school-district brief text `sullivan_09.*` | Petition, JA and both principal merits sides downloaded as PDFs and item OCR texts; docket, questions, parties, relief, revised-notice form and scope verified from selected passages. |
| [NFFE records item](https://archive.org/details/micro_IA40385014_0155) | `micro_IA40385014_0155_metadata.json`; `nffe_02.*`, `nffe_05.*`, `nffe_06.*`, `nffe_07.*` | Petition and three merits briefs downloaded as PDFs and item OCR texts. Questions and petition factual introduction read. Full merits texts preserved for additional bounded validation; not certified fully read. |
| [Companion FLRA records item](https://archive.org/details/micro_IA40385014_0160) | `micro_IA40385014_0160_metadata.json` | Companion docket and individual file listing; duplicated merits papers not downloaded again. |
| [Sullivan lower opinion](https://static.case.law/f3d/139/cases/0158-01.json) | `sullivan_below.json`, `sullivan_below.txt` | Complete opinion and footnotes read in three consecutive text segments. Cross-checked reported opening and provisions through [OpenJurist](https://openjurist.org/139/f3d/158). |
| [Interior lower opinion](https://static.case.law/f3d/132/cases/0157-01.json) | `nffe_below.json`, `nffe_below.txt` | Complete opinion/footnotes read. Cross-checked through [OpenJurist](https://openjurist.org/132/f3d/157). |
| [Karl lower opinion](https://static.case.law/f3d/173/cases/1144-01.json) | `karl_below.json`, `karl_below.txt` | Complete opinion read. It concerns Karl, not Walter; not supplied in neutral model excerpts. |
| [Germany original filing](https://www.supremecourt.gov/pdfs/recordsandbriefs/1000370938/1000370938_001.pdf) | `germany_complaint.pdf`, `germany_complaint.pdf.txt` | Motion, complaint and ICJ exhibit read; memorandum opening/conclusion and identified allegations checked. The complete memorandum was extracted but not certified fully read after output truncation. File's later service certification is distinguished from March 3 substantive filing text. |
| [Germany reply](https://www.supremecourt.gov/pdfs/recordsandbriefs/1000370938/1000370938_002.pdf) | `germany_reply.pdf`, `germany_reply.pdf.txt` | Complete substantive reply and attachment read, including its attribution of the Solicitor General's positions. Separate letter unavailable. Historical prior-Supreme-Court descriptions excluded from neutral facts. |
| [Authenticated ICJ order](https://icj-web.leman.un-icc.cloud/sites/default/files/case-related/104/104-19990303-ORD-01-00-EN.pdf) | `icj_order.pdf`, `icj_order.pdf.txt` | Complete order through signatures and end page read. Exact text copied, without treating domestic enforceability as established. |
| Official 1998 U.S. Code, title 5 sections 7101, 7102, 7103, 7105, 7106, 7114, 7116, 7117, 7119 and title 28 section 1251 | `5usc*_1998.html/.txt`, `28usc1251_1998.html/.txt`; URL list `statutes_receipt.json` | Official period-specific text recovered; operative provisions script-copied without amendment annotations. No current-code substitution. |
| Controlled Stewart facts | `../../runtime/OT_1998CHUNK5_STEWART_CONTROL_FACTS.md` | Read in full. Supplies Walter-specific objective recitations while preserving unrecovered emergency docket numbers. |

`download_receipt.json`, `pdf_receipt.json` and `statutes_receipt.json` preserve exact download URLs and byte counts/errors. Direct OpenJurist HTTP retrieval returned 403; web-tool bounded opening worked for the Sullivan and Interior lower opinions. Caselaw Access Project JSON supplied durable text copies. No Justia automated fetch was used.

## Reading boundaries and completeness

Read AGENTS.md, applicable Engine provisions including section 14, relevant composition/Standing State, the Section-I runtime packet, current public neutral projection, selected tracker passages and relevant linked public copies. No combined brief, Stone supplement, comparator file, private continuity, raw decision record, ledger or top-level Stone directory was opened. No Git command was run. Writes are confined to OT1998 research/runtime/entering-law. The entering-law build used `PYTHONDONTWRITEBYTECODE=1`.

The four source papers for Sullivan and the NFFE merits papers are recovered but **not all read in full**. No conclusion that a factual assertion or citation is absent from those papers is made. Full lower opinions support the reported facts under Engine section 14; where a later decision depends on a further contested merits-paper detail, the fresh stage must read that precise material before resolving it. Read coverage is expressly narrower than download coverage.

## Derived copies

`EXACT_PASSAGES.md` was created by script substring selection from preserved source text. The supplied sections identify source filenames and retain original words/OCR; no long quotation was retyped. It includes Sullivan's petition questions, system/procedure and other-claim recitations, pleaded relief, revised JA notice and petitioners' scope statement; NFFE's petition questions and stipulated clause/procedure; Germany's motion and complaint; the full authenticated ICJ order; and the period Code provisions.

The entering-law slice was built with `tools/build_entering_law.py` from federal-courts, administrative-law, first-amendment, business-and-commercial-law and criminal-procedure volumes, exact identified Standards headings and Court/allotment/practice headings. Seven already-generated current public copies were appended verbatim: NAACP, Calderon v. Coleman, McClellan v. Cablevision, City of West Covina, Blue Fox, AT&T v. Iowa Utilities Board and Your Home. These remain reading copies; they neither create law nor replace the current neutral projection.

Fresh independent validation is required before the handoff is frozen or used for modeling. No readiness representation in this receipt supersedes that requirement.
