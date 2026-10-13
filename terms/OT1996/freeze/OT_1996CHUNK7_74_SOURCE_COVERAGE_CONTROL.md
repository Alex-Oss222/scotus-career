# Brown complete-filings source coverage — control only

The substantive handoff is `OT_1996CHUNK7_74_FULL_SOURCE_HANDOFF.md`. This control file is separate because coverage, reader exposure and workflow are not substantive inputs for modeling.

## Direct complete reads

This source-control reader directly read every page and both page sides of the saved primary PDFs for petition 02 (37 PDF pages, 15,800 extracted words), Joint Appendix 04 (72 pages, 32,240 words), and respondent merits 06 (30 pages, 18,559 words). Covers, tables, notes, appendices and conclusions were included. The complete substituted lower opinion, with its separate lower-court writing and all notes, was directly read as reproduced in the petition appendix; the separately saved `Brown_lower.txt` was not needed for another duplicate complete read.

The saved TXT extraction interleaves the two printed pages on landscape PDF spreads. For readable full coverage, a mechanical PyMuPDF extraction assigned **every** embedded PDF word exactly once to its page side using the word's horizontal midpoint, then retained block/line/word order within that side. Portrait pages were retained as one side. The script asserted that the sum of side word counts equaled each full PDF page's word count. It did not remove words, abbreviate text, repair OCR or infer missing text. The complete derived reading files are `sources/chunk7-neutral-a/Brown_02_full_read.json`, `Brown_04_full_read.json`, and `Brown_06_full_read.json`. Coverage is of these complete saved filings, not a claim to have obtained or read the entire trial transcript beyond the filed excerpts.

Contiguous completed displays were: petition pages 1–10, 11–20, 21–30, 31–37; JA pages 1–10, 11–20, 21–30, 31–40, 41–50, 51–60, 61–72; respondent pages 1–10, 11–15, 16–20, 21–25, 26–30. One attempted respondent display covering pages 11–20 was truncated at the orchestration output cap. **The whole attempted interval was reread**, in the two smaller complete displays 11–15 and 16–20; no coverage claim depends on the truncated display. All listed completed displays returned in full without truncation.

## Inherited complete reads, accurately delimited

Root directly read petitioner merits 05 and reply 07 in full and provided the separate `OT_1996CHUNK7_74_PETITIONER_SOURCE_HANDOFF.md` and `OT_1996CHUNK7_74_ROOT_SOURCE_COVERAGE_CONTROL.md`. This reader read both handoffs and incorporated the petitioner-side content with attribution. Root's receipt records normalized petitioner intervals [0,30000) and [30000,60773), and reply [0,30252), all without truncation. This reader additionally read saved TXT extracted pages 1–8 of petitioner 05 before the division of work, but does **not** claim a separate full direct read of 05 or any full direct read of 07. The five complete filings are therefore covered by the combined direct readers, not by a falsely attributed single-reader review.

## Exposure and isolation

This reader received and read `OT_1996CHUNK7_74_RECONCILIATION_HANDBACK.md`, including its historical-comparison discussion. It did not open the underlying historical Supreme Court opinions, target Section III file, Stone material, Justice commitments, term Records, private user positions, or repository history. It is a source-control reader, **not** a neutral, modeling or reconciliation context. Nothing about the target Supreme Court's disposition, reasoning, lineup, author or opinion metadata was transferred into the substantive handoff or primary extracts. Lower-court actions, the parties' requests and date-eligible authorities cited by counsel remain identified as such. Source front-matter metadata was read for coverage but is not supplied as substantive target-decision information.

No Git commands were used. No top-level `stone/` path was read, listed or searched. Writes were confined to `terms/OT1996/`; all Python invocations used `-B`. No new target search was needed: the five saved filings and root's supplied receipt were the complete source set for this work.

## Exact-copy and hash controls

The primary-extract file was written by script copying the saved mechanical PDF extraction, with source PDF page and side coordinates. No lengthy source quotation was recreated by hand. The actual municipal interrogatories and constitutional charge embedded in the substantive handoff were also copied by script from those source spans. The excerpts retain OCR spelling and printed-page interruptions rather than silently repairing them. `OT_1996CHUNK7_74_PRIMARY_COPY_CONTROL.json` records each extract's coordinates, length and SHA-256; `OT_1996CHUNK7_74_SOURCE_COVERAGE_CONTROL.json` records the complete PDF/TXT source hashes, direct reading intervals, normalized reading hashes and embedded-span hashes. The petitioner extract file has its separate root copy receipt.

A first selection script failed before writing output due to a comprehension variable mistake; it was corrected and rerun successfully. A later attempt to tighten the interrogatory span failed before changing the file; the successful replacement uses ASCII source delimiters and preserves the full source questions and answers. These were copy-tool issues, not source gaps. The final source-copy check verified all 180 selected page sides against the derived source and verified both embedded spans against their source bytes. The actual-damage line items were also independently summed arithmetically: $927,302 less $216,000 earnings items equals $711,302.

Fresh neutral validation and fresh affected modeling remain the appropriate next substantive stages. This handoff chooses no Justice position, coalition, author, disposition or remedy.
