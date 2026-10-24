# Arteaga archive source-read receipt -- CONTROL ONLY

The source reader is a control context. All five OCR files were read in full, with no omitted pages or appendices; the substantive documents are bundles 2-5. Bundle 1 is the docket. Historical Supreme Court material was encountered and excluded from the neutral handoff. Do not expose this source bundle, docket, or receipt as a new neutral-model input. No Stone material or combined chunk brief was read. No git command was used.

Parent control searched the Internet Archive collection by docket/name and supplied item `micro_IA40385014_0197`, https://archive.org/details/micro_IA40385014_0197 . The listing supplied no separate joint appendix. This receipt claims full reading of the recovered four document bundles and docket, not proof that no other court-file document ever existed.

| Bundle | PDF | PDF pages | OCR lines fully read | OCR SHA-256 |
|---|---|---:|---|---|
| 1 | micro_IA40385014_0197 1. Docket.pdf | 1 | 1-79 | `f80eb2d420e321b23b5980f9f33930c5ed06fb190c30c29133dacf35d6306e60` |
| 2 | micro_IA40385014_0197 2. Petition for Writ of Certiorari.pdf | 11 | 1-1016 | `d0f9fcf9bfcaa9491b1ad150c02bc0ab804eb31dca11ba0d9ee2871ae4c872d3` |
| 3 | micro_IA40385014_0197 3. Respondents Brief.pdf | 25 | 1-2373 | `5b0b1da0dcb5281aa8d4f57a1cc310ea93f240e40fdb55fe92e7ab4cc6a79426` |
| 4 | micro_IA40385014_0197 4. Supplemental Brief.pdf | 12 | 1-1439 | `cad3db393eb76108806e7411a7fbad9c89c3fb6975f145cfa8bc6461d6be3183` |
| 5 | micro_IA40385014_0197 5. Reply Brief.pdf | 29 | 1-2871 | `8b2b3e4e0ef5c85320bacae6217f8d6bbf712f2874b62ddd989aaad6e5cc522a` |

Full-reading sequence: 1 and 2 as complete raw text; 3 sequential lines 1-800, 801-1600, 1601-end; 4 lines 1-750 and 751-end; 5 lines 1-950, 951-1900, 1901-end. PDF text was additionally used for source-page localization. OCR warnings appear in the originals.

The PDF skill was read. Visual checks used rendered downloaded PDF images: bundle 2 pages 8-11 (joint appellate memorandum, dismissal judgment/order, March 7 extension/library/stay order) and bundle 3 page 24 (entire IFP motion and financial declaration). These images are saved as `arteaga_verify_2_8.png` through `arteaga_verify_2_11.png` and `arteaga_verify_3_24.png` in this directory.

Material visual corrections: IFP respondent is crossed-out Superior Court of Santa Clara County, not Wilson; last employment is October 18, 1988, not the OCR's dates; approximately $1,000/month describes former employment. Motion and declaration dated August 17, 1997. The district dismissal order specifies prejudice to filing the allegations in other unpaid complaints. The separate judgment has an apparent wording error ('with filing'); the operative order is clear. January stay-lifting date varies by one day in the two recitations, so neutral handoff uses January 1996.

Catalog provenance: bundle 3's 'Respondents Brief' is petitioner's supplemental habeas/certiorari material. Bundle 5 replies to an administrative Corrections letter reproduced in bundle 4 page 12, not a demonstrated respondent court brief. The financial form is appended earlier material, not demonstrated separately executed Wilson-captioned financial paper.

Safe output: `ARTEAGA_ARCHIVE_NEUTRAL_FACTS.md`. It includes only document identity, objective lower-court procedure, expressly attributed party allegations and arguments, and sworn personal financial statements with linkage limits. It excludes current and earlier historical Supreme Court actions, outcomes, rationales, lineups, and filing directives, including those reproduced in clerk correspondence. No votes or modeling were performed. Root must route the safe file through fresh clean validation before a model receives it.
