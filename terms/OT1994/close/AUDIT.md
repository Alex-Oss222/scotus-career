# October Term 1994 — Audit

**Result: FAIL — deterministic gate not passed; independent legal-substance review not started.**

**Audit date:** September 30, 2026. **Findings:** 12 grouped findings: 0 critical, 1 high, 4 medium, 7 low. The occurrence lists below are part of the findings; repeated manifestations are not counted as separate finding IDs.

The instruction permits a fresh AI review of legal substance **only after** the deterministic checks pass. They do not pass. This report completes and reports the deterministic work that can proceed independently, including coverage of all 99 inventory matters, both Holdings passes, all three candidate trackers, and the six prioritized completion/correction histories. It does **not** certify the legal defensibility of the 99 adjudications, historical departures, controlling coalitions, precedent treatment, remedies, or candidate rules. Those subjects still require the fresh review after the reported defects are corrected in a separate authorized task. No adjudication, render, candidate, source, workspace projection, or tool was repaired here.

## Method and execution boundary

After reading the governing instructions, the first validation program run was `python tools/check_term.py OT1994`. It exited 0 with `OK: OT1994; 58 warning(s)`. The stock program invokes `git cat-file` internally. To honor the express prohibition on **any Git command**, a scratch `sitecustomize.py` intercepted only that subprocess request and answered it by reading the Git object database directly. The repository checker was not edited. Loose and packed objects were decompressed, delta objects reconstructed when necessary, and object SHA-1 identities checked; commit references were type-checked as commits. All other checker subprocesses were ordinary Python checks. No Git executable or Git command ran.

The 58 warnings are false positives from the checker's broad hexadecimal-token detector, not 58 missing commits. All 18 distinct warned tokens were examined in context: Archive identifiers (`A40385013`, `A40386002`, `A40386003`, `A40386007`, `A40386012`); source/URL identifiers (`1000180149`, `1000180155`, `1662045`, `1994168`, `2006630`, `2035579`, `5223F70CBD862DEEE5634BA1F102E638`, `9780300050288`, `ec1395dd`); Technical Advice Memorandum `8314011`; a substring of `pub103272.pdf` (`b103272`); a compressed reporter citation (`e21F3d1038`); and a substring of “succeeded” (`cceeded`). None purports to identify a commit. The actual pinned baseline commit `13b19ee463d16fb4377d846e5b058599f886bed3` resolves, including its linked Standing State source. The six priority history objects are verified in the correction table below.

The separate checks covered inventory/manifest/Record/Render Input/render membership; effective dates and public boundaries; formal participation and vote/join arithmetic; normal runtime split freshness; Public Projection identity; candidate coverage and synchronized headers; repository file links and anchors; direct-object provenance; staged cleanup; and open-matter carry-forward. Repository links in candidate trackers that point to the future published `state/HOLDINGS.md` were also resolved against `close/HOLDINGS.candidate.md`; they were not incorrectly treated as missing current-term holdings in the still-unreplaced opening state.

External source URLs were inventoried, not refetched or legally re-researched. Link resolution here means repository file/anchor resolution, including pinned repository objects. It does not certify external-site availability or source completeness. No claim is made that a fact is absent from an unreviewed brief, appendix, or transcript. Ignored scratch directories and downloaded source prose are not treated as current adjudicative authority.

## Unresolved findings

### F01 — High — Robertson has no public render entry

Inventory matter 57, *United States v. Robertson*, No. 94-251, decided May 1, 1995, has a completed current Record and an exactly matching Public Projection in `render-inputs/OT_1994CHUNK5.md`. It has neither a chronology row nor a bounded decision entry in `output/OT_1994CHUNK5.md`. Chunk 5 contains 12 completed Render Input events but only 11 rendered events. The term therefore has 99 current Court Records and 99 Render Input events but only 98 public entries.

The missing entry includes the 9–0 reversal of the commerce-based Count Six judgment, Breyer's Court opinion with all eight other Justices, the actual-interstate-enterprise holding, and the bounded remaining appellate/resentencing posture. Those details are recorded here only to identify the omitted projection; this audit does not redecide them. Both Holdings-pass notes already identify the omission. The Morales correction's validation receipt expressly preserved the existing eleven-entry output, so that correction did not cure it.

### F02 — Low — Four rendered events omit their supplied dockets

The docket is absent from the entire relevant entry, not merely from its heading:

| Chunk 7 render location | Matter | Missing docket |
|---|---|---|
| `output/OT_1994CHUNK7.md:96` | Adarand Constructors, Inc. v. Peña | 93-1841 |
| `output/OT_1994CHUNK7.md:217` | Johnson v. Jones | 94-455 |
| `output/OT_1994CHUNK7.md:331` | Metropolitan Stevedore Co. v. Rambo | 94-820 |
| `output/OT_1994CHUNK7.md:503` | Wilton v. Seven Falls Co. | 94-562 |

All four dockets are supplied by their current Records and Render Inputs. This violates the public identity-preservation requirement without changing the identified judgments.

### F03 — Medium — Ten incorporated source links in four current Records have missing local targets

The current Anderson v. Green Record points to two absent source files; Swint points to two; the Plant Variety Protection Act Admitted Source Record points to three; and the Vaccine Injury Table Admitted Source Record points to three. Exact files, lines and targets appear in Appendix B. The source Notes' external references do not make the claimed local reading copies available. This is a reproducibility/source-location defect, not a finding that the legal propositions are incorrect or that the external sources do not exist. Source-based legal review remains pending.

### F04 — Low — 196 additional repository-link occurrences do not resolve

Appendix C enumerates every additional failed link occurrence, including repeated line locations. These occur in an entering-law slice, runtime handoffs, immutable freeze files, scoped copies, and assembly drafts. Common causes are source files absent from the named local location and relative links copied into a different directory without preserving their original base. For example, `entering-law/OT_1994CHUNK8.md:10727` links to `manifest.md` in its own directory; copied opening snapshots similarly retain workspace-relative links; assembly drafts point to `../freeze/` relative to `runtime/assembly/`.

Historical handoffs are not current law and need not be rewritten to make their legal content current. Their broken links are nevertheless unresolved navigation defects. A later correction must respect the prohibition on silently rewriting frozen commitments. None of the 206 total failures is an unresolved heading anchor after correct Markdown parsing and candidate-publication mapping; all are missing path targets.

### F05 — Medium — Superseded Morales and Stone v. INS assembly drafts survive

`runtime/assembly/California_Department_of_Corrections_v_Morales_merits_1995-04-25.md:3` still says “Reversed and remanded, 5–4” and “No majority constitutional rationale.” Its old outcome also survives in its Public Projection. The current canonical Record and public output instead affirm 5–4 under the replacement adjudication. This draft is explicitly noncanonical, but it remains a full obsolete decision copy outside Git history and is not marked as superseded by the Morales replacement.

`runtime/assembly/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md:175` retains the old Stevens assignment paragraph beginning “Fit:”. The current Record contains the corrected ordinary-assignment-discretion paragraph. The public projection is unaffected because the correction was internal assignment reasoning.

Thus the requested assertion that no stale version survives anywhere cannot be made. These are not duplicate files in `records/`, and no superseded Morales result was found operating as current law in the final workspace projections or candidate Holdings. Immutable pre-correction commitment/reconciliation files also preserve earlier premises as historical handoffs; the Engine expressly preserves those, so their historical content is distinguished from these leftover assembly drafts rather than labeled a second current adjudication.

### F06 — Low — Correction lineage is incomplete in Morales and inaccurate in Stone v. INS

`records/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md:4` still states “Initial canonical adjudication; supersedes nothing.” The verified commit `8d98261d33b6d39fda8a9ccc52ab5ad7ed3be02a` replaces exactly the assignment paragraph. The current lineage does not identify that correction at all. Its text and unchanged Public Projection otherwise match the correction commit.

`records/California_Department_of_Corrections_v_Morales_merits_1995-04-25.md:4` truthfully identifies the prior reversal and the authorized replacement, but retains “Operator verification and Git commitment remain pending” and supplies no version/commit identifier for the committed correction. The replacement is present at `d086219b424d812aaa837fda9533629c69e33833`, and the current Record is byte-identical to that committed file. Concise lineage should identify the actual correction without importing provenance into the public render. Detailed commit archaeology is unnecessary.

The other four priority matters were completions of stopped intake, not replacements of earlier Canonical Decision Records. Direct parent-object inspection confirms that their Record paths did not yet exist immediately before their completion commits; their “first record/no adjudication superseded” statements are supported.

### F07 — Medium — All 101 ledger commitment fields remain pending despite committed Records

`workspace/ledger.md:3` describes an order pending operator Git verification. Every one of its 101 `First-record commit` cells is still a pending placeholder: 40 “operator commit pending,” 37 “uncommitted; operator commit pending,” 12 “uncommitted; operator verification and commit pending,” 11 “file preserved; operator Git commit pending,” and one “operator correction pending.”

All 101 current Record files are byte-identical to their files in the verified current HEAD tree. The ledger therefore has not been brought into agreement with actual durable repository preservation. Its asserted commitment-order index and first-record provenance are not certified by this audit; a chronological/file-preservation surrogate is not a verified Git commitment history. Effective-date reconciliation separately succeeds and does not cure this ledger defect. The operator's prohibition on Git commands during this audit was honored by reporting the defect without rebuilding the ledger.

### F08 — Low — Williams's canonical file still denies canonical status

`records/United_States_v_Williams_merits_1995-04-25.md:4` describes itself as an “Initial adjudication draft for operator review” and says “Not yet preserved as a Canonical Decision Record.” It is in the canonical directory, is marked completed in the manifest, supplies the generated Render Input and render, and matches the committed file. This is a stale validation/status label. The earlier Holdings note noticed it; that notice does not remove the contradiction from the current Record. No change to its 7–2 judgment or its distinct seven- and five-Justice grounds is warranted merely by this clerical finding.

### F09 — Medium — Sky Reefer's participation-limit rows contain dependency text

The Sky Reefer row in `workspace/continuity.md:5958` and `workspace/neutral-projection.md:76` appears under the three-column participation-limit table. Its “Established exclusion” cell instead lists Allied-Bruce, Mastrobuono and First Options, and its “Expected participants” cell contains a completed-case/dependency narrative. It fails to carry Breyer's nonparticipation and the eight-member Court.

The current Sky Reefer Record states Breyer takes no part (`records/Vimar_Seguros_y_Reaseguros_SA_v_MV_Sky_Reefer_merits_1995-06-19.md:10` and `:127`); its 7–1 judgment and the public render preserve the eight-member participation. The defect is in the current workspace projection, not in the formal vote tally. The identical dependency row in an actual dependency table is appropriate and is not an additional error.

### F10 — Low — Nebraska's open-matter row is structurally misaligned

`workspace/continuity.md:5970` supplies four cells under a six-column open-matter header. It places “Nebraska v. Wyoming, No. 108, Original” together in the first cell, the stage text under “Docket,” and the next-act text under “Stage at opening”; the authority and next-act columns are absent. The corresponding manifest row and Standing State candidate retain Nebraska and its continuing Special Master proceedings correctly. Carry-forward membership is preserved, but this current continuity row is malformed and loses its proper field mapping.

### F11 — Low — Five distinct text corruptions remain in current materials

Four corruptions occur in the chunk 5 chronology table: `district court?s` at line 7, `Ninth Circuit?s` at line 11, `defendants? convictions` at line 14, and `Counts V?VII` at line 16. These are literal question marks in the file bytes, not terminal display artifacts.

The fifth is `reserved ground?s availability` in the Travelers controlling explanation. It is already in the current Record at lines 148 and 501, is faithfully copied to `render-inputs/OT_1994CHUNK5.md:608`, and appears in `output/OT_1994CHUNK5.md:634`, `workspace/continuity.md:2769`, and `workspace/neutral-projection.md:2735`. Its downstream identity is therefore a passed copying check with a preserved source typo, not proof of clean text. Correcting a derivative alone would create projection drift.

### F12 — Low — A current neutral-projection dependency still describes Lopez as future law

`workspace/neutral-projection.md:5576`, in the Harris dependency row, says “Lopez remains a future source until actually adjudicated.” The same current projection covers all 99 completed events through June 29; Lopez was decided April 26 and Harris April 27. The current Harris Record and manifest dependency treatment use actual Lopez. This sentence is stale opening-stage language retained in the final current-state projection. It should not be mistaken for a substantive chronology defect in Harris; the defect found here is the contradictory projection text.

## Deterministic coverage and results

| Check | Result and practical limit |
|---|---|
| Initial repository checker | Exit 0; all 58 lexical commit warnings triaged as false positives. Its success does not check away the separate failures above. |
| Inventory → manifest → Records → Render Inputs | 99/99 inventory matters present once, with matching dockets and effective dates; 101 Records total including two admitted noncase sources. No duplicate canonical priority-case Record. |
| Public render coverage | 98/99; Robertson missing. Four additional docket omissions. All 98 existing entries have their dated opening and closing boundaries. |
| Effective-date order | Inventory and generated event sequences follow November 1, 1994–June 29, 1995. Existing renders preserve date order. March 10 Vaccine Table and April 4 plant-variety admissions retain their effective dates and disclosed late-insertion treatment. Pinette → Chabad is the expressly coordinated June 29 sequence; other same-day peers are not assigned priority by file order. Substantive entering-law sufficiency remains for the legal review. |
| Participation / judgment / join arithmetic | Formal named vote and author-inclusive join fields were screened across all 99 matters; no additional arithmetic discrepancy was found. Evans's 6–1–2 split is not a 6–1 tally; NTEU's “No opposing Justice” cell mentions Scalia/Thomas only to explain grounds, not as opposing votes. Partial joins and judgment-only support were not added to Court-reasoning coalitions. Sky Reefer's separate workspace participation defect is F09. Legal justification and compatibility of joins are not certified. |
| Runtime split freshness | All nine approved briefs agree with their 27 normal `_NEUTRAL`, `_STONE` and `_COMPARATOR` section exports. This does not make old assembly drafts or historical frozen commitments current. |
| Public Projection → Render Input | Exact generated-body identity for all 99 Court events; the two admitted-source Records retain their required public interfaces but are not extra inventory Court renders. |
| Holdings source and render text | All 236 controlling-proposition blocks appear in their Records' substantive sections and Public Projections. All 236 are represented in the Holdings candidate: 235 normalized exact matches and one harmless deletion of the locative word “below” in Clearwater. The 235 propositions belonging to rendered matters are present in their rendered entries; Robertson's single proposition has no render. This is text coverage, not a substantive approval of the propositions. |
| Both Holdings passes | Independently counted 154 proposition blocks from matters 1–60, and 82 from matters 61–99, totaling 236 from 99 Records. Both current pass notes and the cumulative candidate were checked. |
| Standards and Tests candidate | Header, structure, repository navigation and source-reference coverage checked alongside its 101-Record pass accounting. A case need not generate a new reusable standard merely because it has a Holdings entry. Legal entailment, consolidation, limits and omissions require the deferred fresh review; the prior pass's assertions are not substituted for it. |
| Candidate synchronization | All three candidates have identical staged common fields: last completed OT1993; processed through June 30, 1994 after the eleven chunk-8 matters/all 95 OT1993 events; edition September 28, 2026. Standing State separately identifies opening OT1995. Retaining the synchronized opening header until coordinated publication is disclosed in the pass notes and is not an audit failure. |
| Repository links / anchors | 12,191 inline repository-link occurrences screened; 206 missing targets, fully listed below. Candidate links to future published Holdings resolve against the candidate. No remaining anchor failure after correct parsing. 2,719 external URL occurrences inventoried but not fetched. |
| Commit existence / lineage | Actual cited baseline object and six priority completion/correction objects verified directly, with current-file comparisons. Current HEAD contains identical bytes for all 101 Records. Ledger placeholders and correction-lineage omissions remain F06–F08. |
| Candidate cleanup | Exactly three active candidate trackers plus the two Holdings pass notes and Standards pass note; no duplicate or superseded close candidate, final dossier or post-Commit close index. Candidates/pass notes must remain during this failed pre-Commit audit; deletion is due only after successful Commit. |
| Open-matter carry-forward | Nine open matters retained: Zatko and sixteen companions; Wyoming v. Oklahoma; Reynolds; Grubbs; United States v. Louisiana; Delaware v. New York; Nebraska v. Wyoming; In re Anderson; Kansas v. Colorado. Eight inherited matters plus Kansas; Nebraska's scheduled exceptions decision does not close its original proceeding. The candidate also separately carries the ten user-added OT1995 matters. No invented terminal action was used. Nebraska's malformed continuity row remains F10. |
| Next-term Court setting | Nine Justices in the proper OT1995 order; thirteen circuit allotments agree with the August 3, 1994 composition order; standing referral practice carried. Candidate contains only the header and the four authorized setting/docket sections. |

## Priority completion/correction consistency

The following comparisons verify current bytes, public fields and concise history, not substantive legal approval. Render Inputs exactly copy their current Records. Frozen historical comparator material and pre-correction commitments are not treated as current law.

| Matter | Current result and projection comparison | Direct-object history verification |
|---|---|---|
| Transcon Lines | Current 9–0 reversal/remand and directed-implementation remedy appear in Record, chunk 1 Render Input and compact render. No duplicate canonical Record or current stopped status found. | First completed Record at `acec437d236d6d12e54bd53b191a233f57f52916`; absent in parent; current Record identical. |
| Fargo | Current component-specific 6–3 access vacatur and 8–1 definition/penalty affirmances, separate joins and remand limits appear in Record, chunk 2 input and full render. No overall margin is substituted for the component votes. | First completed Record at `f6afbf7f1a82d7ea26633bb04df475c3c4356f43`; absent in parent; current Record identical. |
| O'Neal | Current 7–2 vacatur/remand, five-vote Chapman instruction, three-vote broader extension and conditional-writ limits appear in Record, chunk 3 input and render. | First completed Record at `b3ce99c5c54607c27c5893c25cc52fc04efcca70`; absent in parent; current Record identical. |
| Robertson | Record and chunk 5 input agree on the completed 9–0 decision and limited remaining proceedings; **no render exists**. | First completed Record at `0fcb6a5c2d5485cf0591f852f4fbf859d4b1f3bf`; absent in parent; current Record identical. F01 remains. |
| Morales | Current 5–4 affirmance: Stone-Zsela, Stevens, O'Connor, Souter and Ginsburg; O'Connor Court opinion, Stone concurrence, Kennedy dissent joined by Scalia, Thomas and Breyer; annual-consideration remedy without parole order agrees across Record, input and render. | Replacement at `d086219b424d812aaa837fda9533629c69e33833`; current Record identical. Earlier reversal remains in a noncanonical assembly draft; correction lineage remains incomplete (F05–F06). |
| Stone v. INS | Current 5–4 affirmance, Kennedy Court opinion and Breyer dissent remain consistent across public projections. Stevens's corrected assignment paragraph is internal and creates no public vote/holding/remedy change. | `8d98261d33b6d39fda8a9ccc52ab5ad7ed3be02a` changes only that paragraph; current Record identical. Old paragraph survives in assembly draft and correction is omitted from lineage (F05–F06). |

## Appendix A — All-matter coverage

Every row below was included in deterministic membership/date/interface and formal vote-field screening. “Present” means a bounded public entry was found; it does not mean the deferred legal review passed. CDR → RI body identity passes for every row. The two noncase source admissions are additional to this 99-row inventory.

| No. | Chunk | Matter | Effective date | Public render |
|---:|---:|---|---|---|
| 1 | 1 | United States v. Shabani | 1994-11-01 | Present |
| 2 | 1 | U.S. Bancorp Mortgage Co. v. Bonner Mall Partnership | 1994-11-08 | Present |
| 3 | 1 | Hess v. Port Authority Trans-Hudson Corp. | 1994-11-14 | Present |
| 4 | 1 | United States v. X-Citement Video, Inc. | 1994-11-29 | Present |
| 5 | 1 | Church of Scientology Flag Service Organization, Inc. v. City of Clearwater + | 1994-12-05 | Present |
| 6 | 1 | Federal Election Commission v. NRA Political Victory Fund | 1994-12-06 | Present |
| 7 | 1 | Reich v. Collins | 1994-12-06 | Present |
| 8 | 1 | Brown v. Gardner | 1994-12-12 | Present |
| 9 | 1 | Nebraska Department of Revenue v. Loewenstein | 1994-12-12 | Present |
| 10 | 1 | In re Baby K + | 1994-12-12 | Present |
| 11 | 1 | Plakas v. Drinski + | 1995-01-09 | Present |
| 12 | 1 | Interstate Commerce Commission v. Transcon Lines | 1995-01-10 | Present |
| 13 | 2 | Tome v. United States | 1995-01-10 | Present |
| 14 | 2 | Young v. Northern Illinois Conference of United Methodist Church + | 1995-01-17 | Present |
| 15 | 2 | Asgrow Seed Co. v. Winterboer | 1995-01-18 | Present |
| 16 | 2 | United States v. Mezzanatto | 1995-01-18 | Present |
| 17 | 2 | American Airlines, Inc. v. Wolens | 1995-01-18 | Present |
| 18 | 2 | NationsBank of North Carolina, N.A. v. Variable Annuity Life Insurance Co. / Ludwig v. Variable Annuity Life Insurance Co. | 1995-01-18 | Present |
| 19 | 2 | Allied-Bruce Terminix Cos. v. Dobson | 1995-01-18 | Present |
| 20 | 2 | Schlup v. Delo | 1995-01-23 | Present |
| 21 | 2 | McKennon v. Nashville Banner Publishing Co. | 1995-01-23 | Present |
| 22 | 2 | Fargo Women’s Health Organization v. Schafer + | 1995-02-13 | Present |
| 23 | 2 | Lebron v. National Railroad Passenger Corp. | 1995-02-21 | Present |
| 24 | 2 | Milwaukee Brewery Workers' Pension Plan v. Jos. Schlitz Brewing Co. | 1995-02-21 | Present |
| 25 | 3 | O'Neal v. McAninch | 1995-02-21 | Present |
| 26 | 3 | United States v. National Treasury Employees Union | 1995-02-22 | Present |
| 27 | 3 | Harris v. Alabama | 1995-02-22 | Present |
| 28 | 3 | Jerome B. Grubart, Inc. v. Great Lakes Dredge & Dock Co. / City of Chicago v. Great Lakes Dredge & Dock Co. | 1995-02-22 | Present |
| 29 | 3 | Anderson v. Green | 1995-02-22 | Present |
| 30 | 3 | Gustafson v. Alloyd Co. | 1995-02-28 | Present |
| 31 | 3 | Arizona v. Evans | 1995-03-01 | Present |
| 32 | 3 | Swint v. Chambers County Commission | 1995-03-01 | Present |
| 33 | 3 | Mastrobuono v. Shearson Lehman Hutton, Inc. | 1995-03-06 | Present |
| 34 | 3 | Curtiss-Wright Corp. v. Schoonejongen | 1995-03-06 | Present |
| 35 | 3 | Shalala v. Guernsey Memorial Hospital | 1995-03-06 | Present |
| 36 | 3 | Ambassador Books & Video, Inc. v. City of Little Rock + | 1995-03-20 | Present |
| 37 | 4 | Director, Office of Workers’ Compensation Programs v. Newport News Shipbuilding & Dry Dock Co. | 1995-03-21 | Present |
| 38 | 4 | Anderson v. Edwards | 1995-03-22 | Present |
| 39 | 4 | Swanner v. Anchorage Equal Rights Commission + | 1995-03-27 | Present |
| 40 | 4 | Qualitex Co. v. Jacobson Products Co. | 1995-03-28 | Present |
| 41 | 4 | Oklahoma Tax Commission v. Jefferson Lines, Inc. | 1995-04-03 | Present |
| 42 | 4 | Plaut v. Spendthrift Farm, Inc. | 1995-04-18 | Present |
| 43 | 4 | Shalala v. Whitecotton | 1995-04-18 | Present |
| 44 | 4 | Freightliner Corp. v. Myrick | 1995-04-18 | Present |
| 45 | 4 | Heintz v. Jenkins | 1995-04-18 | Present |
| 46 | 4 | Lanphere & Urbaniak v. Colorado + | 1995-04-18 | Present |
| 47 | 4 | Celotex Corp. v. Edwards | 1995-04-19 | Present |
| 48 | 4 | McIntyre v. Ohio Elections Commission | 1995-04-19 | Present |
| 49 | 5 | Stone v. Immigration and Naturalization Service | 1995-04-19 | Present |
| 50 | 5 | Kyles v. Whitley | 1995-04-19 | Present |
| 51 | 5 | Rubin v. Coors Brewing Co. | 1995-04-19 | Present |
| 52 | 5 | California Department of Corrections v. Morales | 1995-04-25 | Present |
| 53 | 5 | United States v. Williams | 1995-04-25 | Present |
| 54 | 5 | United States v. Lopez | 1995-04-26 | Present |
| 55 | 5 | New York State Conference of Blue Cross & Blue Shield Plans v. Travelers Insurance Co. / Pataki v. Travelers Insurance Co. / Hospital Association of New York State v. Travelers Insurance Co. | 1995-04-26 | Present |
| 56 | 5 | United States v. Harris + | 1995-04-27 | Present |
| 57 | 5 | United States v. Robertson | 1995-05-01 | **MISSING — F01** |
| 58 | 5 | United States v. Pinson + | 1995-05-08 | Present |
| 59 | 5 | Kansas v. Colorado | 1995-05-15 | Present |
| 60 | 5 | Hubbard v. United States | 1995-05-15 | Present |
| 61 | 6 | City of Edmonds v. Oxford House, Inc. | 1995-05-15 | Present |
| 62 | 6 | Reynoldsville Casket Co. v. Hyde | 1995-05-15 | Present |
| 63 | 6 | Day v. Holahan + | 1995-05-15 | Present |
| 64 | 6 | U.S. Term Limits, Inc. v. Thornton / Bryant v. Hill | 1995-05-22 | Present |
| 65 | 6 | Wilson v. Arkansas | 1995-05-22 | Present |
| 66 | 6 | First Options of Chicago, Inc. v. Kaplan | 1995-05-22 | Present |
| 67 | 6 | Kelley v. Board of Trustees of the University of Illinois + | 1995-05-22 | Present |
| 68 | 6 | Nebraska v. Wyoming | 1995-05-30 | Present |
| 69 | 6 | North Star Steel Co. v. Thomas / Crown Cork & Seal Co., Inc. v. United Steelworkers of America, AFL-CIO-CLC | 1995-05-30 | Present |
| 70 | 6 | Garlotte v. Fordice | 1995-05-30 | Present |
| 71 | 6 | United States v. Wellons + | 1995-05-30 | Present |
| 72 | 6 | Reno v. Koray | 1995-06-05 | Present |
| 73 | 7 | Metropolitan Washington Airports Authority v. Hechinger + | 1995-06-05 | Present |
| 74 | 7 | Missouri v. Jenkins | 1995-06-12 | Present |
| 75 | 7 | Ryder v. United States | 1995-06-12 | Present |
| 76 | 7 | City of Milwaukee v. Cement Division, National Gypsum Co. | 1995-06-12 | Present |
| 77 | 7 | Adarand Constructors, Inc. v. Peña | 1995-06-12 | Present; docket omitted — F02 |
| 78 | 7 | Wilton v. Seven Falls Co. | 1995-06-12 | Present; docket omitted — F02 |
| 79 | 7 | Metropolitan Stevedore Co. v. Rambo | 1995-06-12 | Present; docket omitted — F02 |
| 80 | 7 | Johnson v. Jones | 1995-06-12 | Present; docket omitted — F02 |
| 81 | 7 | Kimberlin v. Quinlan | 1995-06-12 | Present |
| 82 | 7 | Commissioner v. Schleier | 1995-06-14 | Present |
| 83 | 7 | Chandris, Inc. v. Latsis | 1995-06-14 | Present |
| 84 | 7 | Witte v. United States | 1995-06-14 | Present |
| 85 | 8 | Gutierrez de Martinez v. Lamagno | 1995-06-14 | Present |
| 86 | 8 | Oklahoma Tax Commission v. Chickasaw Nation | 1995-06-14 | Present |
| 87 | 8 | Sandin v. Conner | 1995-06-19 | Present |
| 88 | 8 | United States v. Gaudin | 1995-06-19 | Present |
| 89 | 8 | Vimar Seguros y Reaseguros, S.A. v. M/V Sky Reefer | 1995-06-19 | Present |
| 90 | 8 | Hurley v. Irish-American Gay, Lesbian and Bisexual Group of Boston | 1995-06-19 | Present |
| 91 | 8 | National Private Truck Council, Inc. v. Oklahoma Tax Commission | 1995-06-19 | Present |
| 92 | 8 | United States v. Aguilar | 1995-06-21 | Present |
| 93 | 8 | Florida Bar v. Went For It, Inc. | 1995-06-21 | Present |
| 94 | 8 | Vernonia School District 47J v. Acton | 1995-06-26 | Present |
| 95 | 8 | Rosenberger v. Rector and Visitors of the University of Virginia | 1995-06-29 | Present |
| 96 | 8 | Babbitt v. Sweet Home Chapter of Communities for a Great Oregon | 1995-06-29 | Present |
| 97 | 9 | Miller v. Johnson / Abrams v. Johnson / United States v. Johnson | 1995-06-29 | Present |
| 98 | 9 | Capitol Square Review and Advisory Board v. Pinette | 1995-06-29 | Present |
| 99 | 9 | Chabad-Lubavitch of Georgia v. Miller + | 1995-06-29 | Present |

## Appendix B — Missing targets incorporated by current Records (F03)

Paths in the target column are reproduced exactly as linked. They are absent at the location obtained by resolving them relative to the source file. This list establishes missing local targets, not absence of the underlying legal source elsewhere.

| Source file and line | Unresolved target |
|---|---|
| `terms/OT1994/records/Anderson_v_Green_decision_1995-02-22.md:85` | `../sources/chunk3-b-neutral/SOURCES.md` |
| `terms/OT1994/records/Anderson_v_Green_decision_1995-02-22.md:85` | `../sources/chunk3-b-neutral/Anderson_primary_excerpts.md` |
| `terms/OT1994/records/Plant_Variety_Protection_Act_Amendments_statutory_effectiveness_1995-04-04.md:8` | `../sources/chunk4/Pub_L_103-349.pdf` |
| `terms/OT1994/records/Plant_Variety_Protection_Act_Amendments_statutory_effectiveness_1995-04-04.md:8` | `../sources/chunk4/Pub_L_103-349.txt` |
| `terms/OT1994/records/Plant_Variety_Protection_Act_Amendments_statutory_effectiveness_1995-04-04.md:8` | `../sources/chunk4/S_1406_enrolled.html` |
| `terms/OT1994/records/Swint_v_Chambers_County_Commission_merits_1995-03-01.md:118` | `../sources/chunk3-b-swint-supplement/Swint_lower_orders_App_44_73.pdf` |
| `terms/OT1994/records/Swint_v_Chambers_County_Commission_merits_1995-03-01.md:118` | `../sources/chunk3-b-swint-supplement/Swint_lower_orders_App_44_73.txt` |
| `terms/OT1994/records/Vaccine_Injury_Table_regulatory_effectiveness_1995-03-10.md:8` | `../sources/chunk4/Vaccine_Table_60_FR_7678.pdf` |
| `terms/OT1994/records/Vaccine_Injury_Table_regulatory_effectiveness_1995-03-10.md:8` | `../sources/chunk4/Vaccine_Table_60_FR_7678_pdf_text.txt` |
| `terms/OT1994/records/Vaccine_Injury_Table_regulatory_effectiveness_1995-03-10.md:8` | `../sources/chunk4/Vaccine_Table_60_FR_7678.txt` |

## Appendix C — Other missing repository-link targets (F04)

All 196 occurrences are retained below, grouped only when the same source file repeats the exact same target; each line number is shown. Frozen historical material remains historical, and its inclusion here does not authorize rewriting its commitments.

| Source file | Line(s) | Unresolved target |
|---|---|---|
| `terms/OT1994/entering-law/OT_1994CHUNK8.md` | 10727 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK1_OPENING_CONTINUITY.md` | 28 | `ledger.md` |
| `terms/OT1994/freeze/OT_1994CHUNK1_OPENING_CONTINUITY.md` | 13 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK1_OPENING_CONTINUITY.md` | 114 | `manifest.md#material-dependencies` |
| `terms/OT1994/freeze/OT_1994CHUNK1_OPENING_MANIFEST.md` | 176 | `continuity.md#5-current-procedure-and-institution` |
| `terms/OT1994/freeze/OT_1994CHUNK1_OPENING_MANIFEST.md` | 176 | `neutral-projection.md#court-and-public-procedure` |
| `terms/OT1994/freeze/OT_1994CHUNK2_OPENING_CONTINUITY.md` | 32 | `ledger.md` |
| `terms/OT1994/freeze/OT_1994CHUNK2_OPENING_CONTINUITY.md` | 11 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK2_OPENING_CONTINUITY.md` | 456 | `manifest.md#material-dependencies` |
| `terms/OT1994/freeze/OT_1994CHUNK2_OPENING_MANIFEST.md` | 154 | `continuity.md#5-current-procedure-and-institution` |
| `terms/OT1994/freeze/OT_1994CHUNK2_OPENING_MANIFEST.md` | 177 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK2_OPENING_MANIFEST.md` | 154 | `neutral-projection.md#court-and-public-procedure` |
| `terms/OT1994/freeze/OT_1994CHUNK2_OPENING_NEUTRAL_PROJECTION.md` | 13 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK3_CHRONOLOGY_B.md` | 22 | `../sources/chunk3-b-neutral/Gustafson_lower_orders_App_1_14.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_COMMITMENTS_B.md` | 150 | `../sources/chunk3-b-neutral/Leon_468_US_897_Stevens_separate.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_COMMITMENTS_B.md` | 185 | `../sources/chunk3-b-neutral/Mitchell_472_US_511_OConnor_separate.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_COMMITMENTS_B.md` | 185 | `../sources/chunk3-b-neutral/Mitchell_472_US_511_Stevens_separate.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_COMMITMENTS_B.md` | 7 | `../sources/chunk3-b-neutral/SOURCES.md` |
| `terms/OT1994/freeze/OT_1994CHUNK3_COMMITMENTS_B.md` | 150 | `../sources/chunk3-b-neutral/State_Evans_177_Ariz_201.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_COMMITMENTS_B.md` | 185 | `../sources/chunk3-b-neutral/Swint_5_F3d_1435.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_EVANS_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 9 | `../sources/chunk3-b-evans-supplement/Evans_joint_appendix.pdf` |
| `terms/OT1994/freeze/OT_1994CHUNK3_EVANS_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 9 | `../sources/chunk3-b-evans-supplement/Evans_joint_appendix.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_EVANS_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 10 | `../sources/chunk3-b-evans-supplement/Evans_petitioners_brief.pdf` |
| `terms/OT1994/freeze/OT_1994CHUNK3_EVANS_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 10 | `../sources/chunk3-b-evans-supplement/Evans_petitioners_brief.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_EVANS_NEUTRAL_VALIDATED.md` | 63 | `../sources/chunk3-b-evans-supplement/Evans_joint_appendix.pdf` |
| `terms/OT1994/freeze/OT_1994CHUNK3_EVANS_NEUTRAL_VALIDATED.md` | 63 | `../sources/chunk3-b-evans-supplement/Evans_petitioners_brief.pdf` |
| `terms/OT1994/freeze/OT_1994CHUNK3_EVANS_NEUTRAL_VALIDATED.md` | 65 | `../sources/chunk3-b-neutral/28_USC_1257.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_EVANS_NEUTRAL_VALIDATED.md` | 65 | `../sources/chunk3-b-neutral/State_Evans_177_Ariz_201.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_CANDIDATE.md` | 67 | `../sources/chunk3-b-neutral/15_USC_77b_1994.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_CANDIDATE.md` | 69 | `../sources/chunk3-b-neutral/15_USC_77j_1994.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_CANDIDATE.md` | 71 | `../sources/chunk3-b-neutral/15_USC_77l_1994.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_CANDIDATE.md` | 73 | `../sources/chunk3-b-neutral/15_USC_77q_1994.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_CANDIDATE.md` | 101 | `../sources/chunk3-b-neutral/28_USC_1257.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_CANDIDATE.md` | 127 | `../sources/chunk3-b-neutral/28_USC_1291.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_CANDIDATE.md` | 131 | `../sources/chunk3-b-neutral/28_USC_1292.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_CANDIDATE.md` | 133 | `../sources/chunk3-b-neutral/28_USC_2072.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_CANDIDATE.md` | 31 | `../sources/chunk3-b-neutral/Anderson_primary_excerpts.md` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_CANDIDATE.md` | 61 | `../sources/chunk3-b-neutral/Gustafson_lower_orders_App_1_14.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_CANDIDATE.md` | 13 | `../sources/chunk3-b-neutral/SOURCES.md` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_VALIDATED.md` | 69 | `../sources/chunk3-b-neutral/15_USC_77b_1994.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_VALIDATED.md` | 71 | `../sources/chunk3-b-neutral/15_USC_77j_1994.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_VALIDATED.md` | 75 | `../sources/chunk3-b-neutral/15_USC_77l_1994.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_VALIDATED.md` | 77 | `../sources/chunk3-b-neutral/15_USC_77q_1994.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_VALIDATED.md` | 105 | `../sources/chunk3-b-neutral/28_USC_1257.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_VALIDATED.md` | 131 | `../sources/chunk3-b-neutral/28_USC_1291.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_VALIDATED.md` | 135 | `../sources/chunk3-b-neutral/28_USC_1292.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_VALIDATED.md` | 137 | `../sources/chunk3-b-neutral/28_USC_2072.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_VALIDATED.md` | 33 | `../sources/chunk3-b-neutral/Anderson_primary_excerpts.md` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_VALIDATED.md` | 63 | `../sources/chunk3-b-neutral/Gustafson_lower_orders_App_1_14.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NEUTRAL_B_VALIDATED.md` | 15 | `../sources/chunk3-b-neutral/SOURCES.md` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NTEU_CRANE_NEUTRAL_VALIDATED.md` | 9 | `../sources/chunk3-a-crane-supplement/NTEU_petitioners_brief.pdf` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NTEU_CRANE_NEUTRAL_VALIDATED.md` | 9 | `../sources/chunk3-a-crane-supplement/NTEU_petitioners_brief.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NTEU_CRANE_NEUTRAL_VALIDATED.md` | 10 | `../sources/chunk3-a-crane-supplement/NTEU_reply_brief.pdf` |
| `terms/OT1994/freeze/OT_1994CHUNK3_NTEU_CRANE_NEUTRAL_VALIDATED.md` | 10 | `../sources/chunk3-a-crane-supplement/NTEU_reply_brief.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_OPENING_CONTINUITY.md` | 44 | `ledger.md` |
| `terms/OT1994/freeze/OT_1994CHUNK3_OPENING_CONTINUITY.md` | 11 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK3_OPENING_CONTINUITY.md` | 1360 | `manifest.md#material-dependencies` |
| `terms/OT1994/freeze/OT_1994CHUNK3_OPENING_MANIFEST.md` | 154 | `continuity.md#5-current-procedure-and-institution` |
| `terms/OT1994/freeze/OT_1994CHUNK3_OPENING_MANIFEST.md` | 182 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK3_OPENING_MANIFEST.md` | 154 | `neutral-projection.md#court-and-public-procedure` |
| `terms/OT1994/freeze/OT_1994CHUNK3_OPENING_NEUTRAL_PROJECTION.md` | 13 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK3_PREFLIGHT_B.md` | 8 | `../sources/chunk3-b-neutral/SOURCES.md` |
| `terms/OT1994/freeze/OT_1994CHUNK3_RECONCILED_B.md` | 11 | `../sources/chunk3-b-neutral/SOURCES.md` |
| `terms/OT1994/freeze/OT_1994CHUNK3_SWINT_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 7 | `../sources/chunk3-b-swint-supplement/Swint_lower_orders_App_44_73.pdf` |
| `terms/OT1994/freeze/OT_1994CHUNK3_SWINT_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 7 | `../sources/chunk3-b-swint-supplement/Swint_lower_orders_App_44_73.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_SWINT_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 5 | `../sources/chunk3-b-swint-supplement/Swint_petition_appendix.pdf` |
| `terms/OT1994/freeze/OT_1994CHUNK3_SWINT_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 5 | `../sources/chunk3-b-swint-supplement/Swint_petition_appendix.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK3_SWINT_NEUTRAL_RECORD_VALIDATED.md` | 13 | `../sources/chunk3-b-swint-supplement/Swint_lower_orders_App_44_73.pdf` |
| `terms/OT1994/freeze/OT_1994CHUNK3_SWINT_NEUTRAL_RECORD_VALIDATED.md` | 13 | `../sources/chunk3-b-swint-supplement/Swint_lower_orders_App_44_73.txt` |
| `terms/OT1994/freeze/OT_1994CHUNK5_OPENING_CONTINUITY.md` | 70 | `ledger.md` |
| `terms/OT1994/freeze/OT_1994CHUNK5_OPENING_CONTINUITY.md` | 11 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK5_OPENING_CONTINUITY.md` | 2813 | `manifest.md#material-dependencies` |
| `terms/OT1994/freeze/OT_1994CHUNK5_OPENING_MANIFEST.md` | 154 | `continuity.md#5-current-procedure-and-institution` |
| `terms/OT1994/freeze/OT_1994CHUNK5_OPENING_MANIFEST.md` | 183 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK5_OPENING_MANIFEST.md` | 154 | `neutral-projection.md#court-and-public-procedure` |
| `terms/OT1994/freeze/OT_1994CHUNK5_OPENING_NEUTRAL_PROJECTION.md` | 13 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK5_RECONCILED_B_PRE_REFRESH.md` | 17 | `OT_1994CHUNK5_COMPARATOR_54.md` |
| `terms/OT1994/freeze/OT_1994CHUNK5_RECONCILED_B_PRE_REFRESH.md` | 17 | `OT_1994CHUNK5_COMPARATOR_55.md` |
| `terms/OT1994/freeze/OT_1994CHUNK5_RECONCILED_B_PRE_REFRESH.md` | 14 | `OT_1994CHUNK5_NEUTRAL_B_SOURCE_SUPPLEMENT.md` |
| `terms/OT1994/freeze/OT_1994CHUNK5_RECONCILED_B_PRE_REFRESH.md` | 14 | `OT_1994CHUNK5_NEUTRAL_B_VALIDATED.md` |
| `terms/OT1994/freeze/OT_1994CHUNK8_OPENING_CONTINUITY.md` | 108 | `ledger.md` |
| `terms/OT1994/freeze/OT_1994CHUNK8_OPENING_CONTINUITY.md` | 11 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK8_OPENING_CONTINUITY.md` | 5058 | `manifest.md#material-dependencies` |
| `terms/OT1994/freeze/OT_1994CHUNK8_OPENING_MANIFEST.md` | 154 | `continuity.md#5-current-procedure-and-institution` |
| `terms/OT1994/freeze/OT_1994CHUNK8_OPENING_MANIFEST.md` | 183 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK8_OPENING_MANIFEST.md` | 154 | `neutral-projection.md#court-and-public-procedure` |
| `terms/OT1994/freeze/OT_1994CHUNK8_OPENING_NEUTRAL_PROJECTION.md` | 13 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK9_OPENING_CONTINUITY.md` | 120 | `ledger.md` |
| `terms/OT1994/freeze/OT_1994CHUNK9_OPENING_CONTINUITY.md` | 11 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK9_OPENING_CONTINUITY.md` | 5710 | `manifest.md#material-dependencies` |
| `terms/OT1994/freeze/OT_1994CHUNK9_OPENING_MANIFEST.md` | 154 | `continuity.md#5-current-procedure-and-institution` |
| `terms/OT1994/freeze/OT_1994CHUNK9_OPENING_MANIFEST.md` | 179 | `manifest.md` |
| `terms/OT1994/freeze/OT_1994CHUNK9_OPENING_MANIFEST.md` | 154 | `neutral-projection.md#court-and-public-procedure` |
| `terms/OT1994/freeze/OT_1994CHUNK9_OPENING_NEUTRAL_PROJECTION.md` | 13 | `manifest.md` |
| `terms/OT1994/runtime/OT_1994CHUNK2_COMMITMENTS.md` | 521 | `OT_1994CHUNK2_LEBRON_NEUTRAL_REFRESH.md` |
| `terms/OT1994/runtime/OT_1994CHUNK2_COMMITMENTS.md` | 640 | `OT_1994CHUNK2_SCHLUP_NEUTRAL_REFRESH.md` |
| `terms/OT1994/runtime/OT_1994CHUNK2_RECONCILED.md` | 563 | `OT_1994CHUNK2_LEBRON_COMMITMENTS_REFRESH.md` |
| `terms/OT1994/runtime/OT_1994CHUNK2_RECONCILED.md` | 563 | `OT_1994CHUNK2_LEBRON_NEUTRAL_REFRESH.md` |
| `terms/OT1994/runtime/OT_1994CHUNK3_COMMITMENTS.md` | 493 | `../sources/chunk3-b-neutral/Leon_468_US_897_Stevens_separate.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK3_COMMITMENTS.md` | 528 | `../sources/chunk3-b-neutral/Mitchell_472_US_511_OConnor_separate.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK3_COMMITMENTS.md` | 528 | `../sources/chunk3-b-neutral/Mitchell_472_US_511_Stevens_separate.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK3_COMMITMENTS.md` | 350 | `../sources/chunk3-b-neutral/SOURCES.md` |
| `terms/OT1994/runtime/OT_1994CHUNK3_COMMITMENTS.md` | 493 | `../sources/chunk3-b-neutral/State_Evans_177_Ariz_201.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK3_COMMITMENTS.md` | 528 | `../sources/chunk3-b-neutral/Swint_5_F3d_1435.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK3_RECONCILED.md` | 314 | `../sources/chunk3-b-neutral/SOURCES.md` |
| `terms/OT1994/runtime/OT_1994CHUNK4_JEFFERSON_SOURCE_SUPPLEMENT.md` | 40 | `../sources/chunk4/jefferson_briefs/joint_appendix.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_JEFFERSON_SOURCE_SUPPLEMENT.md` | 3 | `../sources/chunk4/jefferson_briefs/manifest.json` |
| `terms/OT1994/runtime/OT_1994CHUNK4_JEFFERSON_SOURCE_SUPPLEMENT.md` | 40 | `../sources/chunk4/jefferson_briefs/petitioner.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_JEFFERSON_SOURCE_SUPPLEMENT.md` | 40 | `../sources/chunk4/jefferson_briefs/respondent.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 43 | `../sources/chunk4/Anderson_lower_12_F3d_154.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 183 | `../sources/chunk4/Bankruptcy_1994_105.htm` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 43 | `../sources/chunk4/Beaton_913_F2d_701.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 213 | `../sources/chunk4/Bowen_Gilliard_483_US_587.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 183 | `../sources/chunk4/Edwards_6_F3d_312.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 153 | `../sources/chunk4/FDCPA_1977_91_Stat_874.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 151 | `../sources/chunk4/FDCPA_1986_amendment.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 91 | `../sources/chunk4/Jefferson_Lines_15_F3d_90.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 151 | `../sources/chunk4/Jenkins_25_F3d_536.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 25 | `../sources/chunk4/LHWCA_1994_921.htm` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 25 | `../sources/chunk4/LHWCA_1994_939.htm` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 75 | `../sources/chunk4/Lanham_1994_1052.htm` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 75 | `../sources/chunk4/Lanham_1994_1127.htm` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 169 | `../sources/chunk4/Lanphere_21_F3d_1508.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 197 | `../sources/chunk4/McIntyre_67_Ohio_St3d_391.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 139 | `../sources/chunk4/Myrick_13_F3d_1516.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 25 | `../sources/chunk4/Newport_News_8_F3d_175.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 139 | `../sources/chunk4/Paccar_573_F2d_632.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 107 | `../sources/chunk4/Plaut_1_F3d_1487.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 75 | `../sources/chunk4/Qualitex_13_F3d_1297.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 55 | `../sources/chunk4/RFRA_107_Stat_1488.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 209 | `../sources/chunk4/Shapero_486_US_466.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 61 | `../sources/chunk4/Swanner_874_P2d_274.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 123 | `../sources/chunk4/Vaccine_Table_60_FR_7678_pdf_text.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 123 | `../sources/chunk4/Whitecotton_17_F3d_374.txt` |
| `terms/OT1994/runtime/OT_1994CHUNK5_COMMITMENTS.md` | 25 | `OT_1994CHUNK5_NEUTRAL_VALIDATION_A.md` |
| `terms/OT1994/runtime/OT_1994CHUNK5_COMMITMENTS_A.md` | 19 | `OT_1994CHUNK5_NEUTRAL_VALIDATION_A.md` |
| `terms/OT1994/runtime/OT_1994CHUNK5_COMMITMENTS_B_PRE_REFRESH.md` | 20 | `OT_1994CHUNK5_NEUTRAL_VALIDATION_B.md` |
| `terms/OT1994/runtime/OT_1994CHUNK5_COMMITMENTS_B_PRE_REFRESH.md` | 20 | `OT_1994CHUNK5_PREFLIGHT_B.md` |
| `terms/OT1994/runtime/OT_1994CHUNK8_COMMITMENTS.md` | 206 | `OT_1994CHUNK8_COMMITMENTS_B91_FINAL.md` |
| `terms/OT1994/runtime/OT_1994CHUNK8_COMMITMENTS.md` | 207 | `OT_1994CHUNK8_COMMITMENTS_B92_FINAL.md` |
| `terms/OT1994/runtime/OT_1994CHUNK8_COMMITMENTS.md` | 208 | `OT_1994CHUNK8_COMMITMENTS_B93_FINAL.md` |
| `terms/OT1994/runtime/OT_1994CHUNK8_COMMITMENTS.md` | 209 | `OT_1994CHUNK8_COMMITMENTS_B94_FINAL.md` |
| `terms/OT1994/runtime/OT_1994CHUNK8_COMMITMENTS.md` | 210 | `OT_1994CHUNK8_COMMITMENTS_B95_FINAL.md` |
| `terms/OT1994/runtime/OT_1994CHUNK8_COMMITMENTS.md` | 211 | `OT_1994CHUNK8_COMMITMENTS_B96_FINAL.md` |
| `terms/OT1994/runtime/assembly/Hubbard_v_United_States_merits_1995-05-15.md` | 285 | `../freeze/OT_1994CHUNK5_VALIDATION.md` |
| `terms/OT1994/runtime/assembly/Kansas_v_Colorado_original_exceptions_1995-05-15.md` | 54 | `../../../state/HOLDINGS.md` |
| `terms/OT1994/runtime/assembly/Kansas_v_Colorado_original_exceptions_1995-05-15.md` | 54 | `../../../state/STANDARDS_AND_TESTS.md` |
| `terms/OT1994/runtime/assembly/Kansas_v_Colorado_original_exceptions_1995-05-15.md` | 54 | `../../../state/STANDING_STATE.md` |
| `terms/OT1994/runtime/assembly/Kansas_v_Colorado_original_exceptions_1995-05-15.md` | 422 | `../freeze/OT_1994CHUNK5_VALIDATION.md` |
| `terms/OT1994/runtime/assembly/Kyles_v_Whitley_merits_1995-04-19.md` | 20 | `../entering-law/OT_1994CHUNK5_A.md` |
| `terms/OT1994/runtime/assembly/Kyles_v_Whitley_merits_1995-04-19.md` | 20 | `../entering-law/OT_1994CHUNK5_A_VALIDATION_SUPPLEMENT.md` |
| `terms/OT1994/runtime/assembly/Kyles_v_Whitley_merits_1995-04-19.md` | 121 | `../freeze/OT_1994CHUNK5_COMMITMENTS_A.md` |
| `terms/OT1994/runtime/assembly/Kyles_v_Whitley_merits_1995-04-19.md` | 121 | `../freeze/OT_1994CHUNK5_RECONCILED_A.md` |
| `terms/OT1994/runtime/assembly/Kyles_v_Whitley_merits_1995-04-19.md` | 191 | `../freeze/OT_1994CHUNK5_VALIDATION.md` |
| `terms/OT1994/runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md` | 278 | `../../../tmp/ot1994_chunk5_b/section2106_1994.txt` |
| `terms/OT1994/runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md` | 280 | `../../../tmp/ot1994_chunk5_comparators/Travelers_514_645.txt` |
| `terms/OT1994/runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md` | 42 | `../entering-law/OT_1994CHUNK5_B.md` |
| `terms/OT1994/runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md` | 42 | `../entering-law/OT_1994CHUNK5_BEFORE_1995-04-26.md` |
| `terms/OT1994/runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md` | 42 | `../entering-law/OT_1994CHUNK5_B_FABE_SUPPLEMENT.md` |
| `terms/OT1994/runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md` | 171 | `../freeze/OT_1994CHUNK5_COMMITMENTS_B.md` |
| `terms/OT1994/runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md` | 261, 277 | `../freeze/OT_1994CHUNK5_COMMITMENTS_TRAVELERS_REMEDY.md` |
| `terms/OT1994/runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md` | 259, 276 | `../freeze/OT_1994CHUNK5_NEUTRAL_VALIDATION_TRAVELERS_REMEDY.md` |
| `terms/OT1994/runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md` | 171, 280 | `../freeze/OT_1994CHUNK5_RECONCILED_B.md` |
| `terms/OT1994/runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md` | 261 | `../freeze/OT_1994CHUNK5_RECONCILED_TRAVELERS_REMEDY.md` |
| `terms/OT1994/runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md` | 280 | `../freeze/OT_1994CHUNK5_RECONCILED_TRAVELERS_REMEDY_CLARIFICATION.md` |
| `terms/OT1994/runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md` | 379 | `../freeze/OT_1994CHUNK5_VALIDATION.md` |
| `terms/OT1994/runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md` | 259, 275 | `../runtime/OT_1994CHUNK5_NEUTRAL_TRAVELERS_REMEDY_SUPPLEMENT.md` |
| `terms/OT1994/runtime/assembly/Rubin_v_Coors_Brewing_Co_merits_1995-04-19.md` | 22 | `../entering-law/OT_1994CHUNK5_A.md` |
| `terms/OT1994/runtime/assembly/Rubin_v_Coors_Brewing_Co_merits_1995-04-19.md` | 22 | `../entering-law/OT_1994CHUNK5_A_PUBLIC_WRITINGS.md` |
| `terms/OT1994/runtime/assembly/Rubin_v_Coors_Brewing_Co_merits_1995-04-19.md` | 22 | `../entering-law/OT_1994CHUNK5_A_VALIDATION_SUPPLEMENT.md` |
| `terms/OT1994/runtime/assembly/Rubin_v_Coors_Brewing_Co_merits_1995-04-19.md` | 123 | `../freeze/OT_1994CHUNK5_COMMITMENTS_A.md` |
| `terms/OT1994/runtime/assembly/Rubin_v_Coors_Brewing_Co_merits_1995-04-19.md` | 123 | `../freeze/OT_1994CHUNK5_RECONCILED_A.md` |
| `terms/OT1994/runtime/assembly/Rubin_v_Coors_Brewing_Co_merits_1995-04-19.md` | 206 | `../freeze/OT_1994CHUNK5_VALIDATION.md` |
| `terms/OT1994/runtime/assembly/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md` | 36 | `../../../state/HOLDINGS.md` |
| `terms/OT1994/runtime/assembly/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md` | 36 | `../../../state/STANDARDS_AND_TESTS.md` |
| `terms/OT1994/runtime/assembly/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md` | 36 | `../../../state/STANDING_STATE.md` |
| `terms/OT1994/runtime/assembly/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md` | 20 | `../entering-law/OT_1994CHUNK5_A.md` |
| `terms/OT1994/runtime/assembly/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md` | 126 | `../freeze/OT_1994CHUNK5_COMMITMENTS_A.md` |
| `terms/OT1994/runtime/assembly/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md` | 126 | `../freeze/OT_1994CHUNK5_RECONCILED_A.md` |
| `terms/OT1994/runtime/assembly/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md` | 185 | `../freeze/OT_1994CHUNK5_VALIDATION.md` |
| `terms/OT1994/runtime/assembly/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md` | 20 | `../runtime/OT_1994CHUNK5_NEUTRAL_A_VALIDATED.md` |
| `terms/OT1994/runtime/assembly/United_States_v_Lopez_merits_1995-04-26.md` | 24 | `../entering-law/OT_1994CHUNK5_B.md` |
| `terms/OT1994/runtime/assembly/United_States_v_Lopez_merits_1995-04-26.md` | 24 | `../entering-law/OT_1994CHUNK5_BEFORE_1995-04-26.md` |
| `terms/OT1994/runtime/assembly/United_States_v_Lopez_merits_1995-04-26.md` | 131 | `../freeze/OT_1994CHUNK5_COMMITMENTS_B.md` |
| `terms/OT1994/runtime/assembly/United_States_v_Lopez_merits_1995-04-26.md` | 131 | `../freeze/OT_1994CHUNK5_RECONCILED_B.md` |
| `terms/OT1994/runtime/assembly/United_States_v_Lopez_merits_1995-04-26.md` | 217 | `../freeze/OT_1994CHUNK5_VALIDATION.md` |
| `terms/OT1994/runtime/scoped/OT_1994CHUNK1_STONE_A.md` | 39 | `../../../state/HOLDINGS.md` |
| `terms/OT1994/runtime/scoped/OT_1994CHUNK1_STONE_A.md` | 39 | `../../../state/STANDARDS_AND_TESTS.md` |
| `terms/OT1994/runtime/scoped/OT_1994CHUNK1_STONE_A.md` | 39 | `../../../state/STANDING_STATE.md` |
| `terms/OT1994/runtime/scoped/OT_1994CHUNK1_STONE_C.md` | 103 | `../../../state/HOLDINGS.md` |
| `terms/OT1994/runtime/scoped/OT_1994CHUNK1_STONE_C.md` | 103 | `../../../state/STANDARDS_AND_TESTS.md` |
| `terms/OT1994/runtime/scoped/OT_1994CHUNK1_STONE_C.md` | 103 | `../../../state/STANDING_STATE.md` |

## Preservation and handoff

Current repository HEAD verified by direct object reading: `152aac795afc78e99021445ab99db65d2d58b20a`. All 2,541 captured preexisting Markdown, Python and JSON files under `foundation/`, `state/`, `terms/` and `tools/` remained byte-identical through report preparation. Those fingerprints include the three candidates and existing close pass notes. The only repository deliverable written by this task is `terms/OT1994/close/AUDIT.md`; scratch scripts and check data are under root `tmp/ot1994_audit/`. No Git command was run.

Reproducibility scratch includes `inventory_checks.json`, `coverage_refined.json`, `formal_votes.json`, `vote_summaries.json`, `projection_checks.json`, `candidate_checks.json`, `links_refined.json`, `table_widths.json`, `correction_provenance.json`, `provenance.json`, and `protected_before.json`. Scratch flags were manually triaged; their unfiltered heuristic alerts are not additional findings.

The term is not ready for coordinated Commit. A later authorized correction task must address the reported defects; then deterministic checks must be rerun, followed by a fresh legal-substance audit across all 99 matters and all three candidates. This pass neither silently fixes a discrepancy nor treats a previous pass's legal assurances as a fresh audit.

**Operator summary: FAIL. Findings by severity: 0 critical; 1 high; 4 medium; 7 low (12 grouped findings). Independent legal-substance review remains pending behind the failed deterministic gate.**
