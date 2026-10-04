# Foman reading receipt

- Task: source-only extraction of Rule 15(a), undue delay, and the distinction between a declared reason and an apparent justification. No adjudication or judicial modeling.
- Governing instructions read: AGENTS.md (the initial read included general instructions beyond Research), with its Research section subsequently read separately; Engine §14, including incomplete-and-counterfactual-record paragraphs 2, 4, 5, 6, and 8. The cloud setup skill and onboarding reference were read as required by the environment instructions; no setup changes were needed for this extraction.
- Primary source: *Foman v. Davis*, 371 U.S. 178 (1962), official United States Reports PDF, <https://www.govinfo.gov/content/pkg/USREPORTS-371/pdf/USREPORTS-371-178.pdf>.
- Retrieval date: October 4, 2026 (environment date). The opinion's legal date is December 3, 1962; no later legal authority was consulted.
- Retrieval: HTTPS download with ordinary TLS verification; `pdftotext -layout` generated the retained complete text. `pdfinfo` confirms six pages and 1,387,031 PDF bytes.
- Complete substantive reading: reporter pages 178–183, PDF pages 1–6. This includes the syllabus at 178; opinion at 179–182; both footnotes at 180; and separate memorandum at 183. No source text was omitted from the displayed complete extraction. The page-182 scan was additionally rendered and visually checked for the quoted Rule 15(a) passage.
- PDF SHA-256: `ccb3c8b9aa777faa26f255d50fd08fdee7fb158355445d50392071f820d64f95`.
- Extracted-text SHA-256: `a73b186db388a8fdb67257085ec0d4464ccac82b9383969c0d2ac113e2b7b9a6`.
- Retained source files: `FOMAN_USREPORTS-371-178.pdf` and `FOMAN_USREPORTS-371-178.txt`.
- Output: `FOMAN_SOURCE_SCOPE.md`. Quotations preserve the opinion's language, with line-break hyphenation removed and typographic quotation marks normalized.
- Current-matter input: only the parent's supplied descriptions of amendment timing and procedural stage, plus the statement that the actual denial rationale is unknown. Those descriptions were not independently verified in this extraction and are labeled accordingly in the source note.
- Current-matter boundary: no current-matter briefs, private positions, comparator, outcomes, votes, model artifacts, or adjudicative records were opened. The source directory listing and worktree status were inspected for file placement and collision avoidance; other source contents were not read. The initial AGENTS.md read exposed general standing instructions, not current-matter private positions or outcomes.
- This extraction creates no reconstructed event, inferred historical finding, assigned lower-court rationale, disposition, or change to entered law. It leaves evaluation of any record-supported apparent justification to the authorized substantive stage.
- No commit or shared-index operation performed.
