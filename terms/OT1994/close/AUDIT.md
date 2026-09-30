# October Term 1994 — Audit

**Result: FAIL — deterministic gate remains unsatisfied; fresh legal-substance review is deferred.**

**Audit date:** September 30, 2026. **Findings:** 4 grouped repository findings: **0 critical, 0 high, 1 medium, 3 low**. Every identified occurrence is listed below. Repeated copies count within their finding, not as additional finding IDs. These counts describe the checks performed; they are not a conclusion that the unperformed legal review would find nothing else.

The requested sequence permits a fresh AI review of legal substance **only after** the deterministic checks pass. The remaining missing-source links prevent that gate from passing. All independent deterministic checks were completed across the **99 inventory Court matters**, the **two additional Admitted Source Records**, all nine Render Inputs and renders, both Holdings passes and their cumulative candidate, the Standards and Tests candidate, and the Standing State candidate. This audit does **not** certify the legal defensibility of votes, coalitions, holdings, precedent treatment, remedies, continuity, or Justice-specific historical departures. Those questions, including the legal entailment and completeness of both doctrinal candidates, still require the fresh review after the deterministic defects are resolved. No agent was assigned a legal-substance audit before the gate passed.

Only this `close/AUDIT.md` and ignored root `tmp/` scratch were written. No adjudication, brief, handoff, workspace projection, render, candidate tracker, source, or repository tool was repaired.

## Execution and evidence

The first command was exactly `python tools/check_term.py OT1994`. It exited 0: `OK: OT1994; 76 warning(s)`. The governing files were then read, and the additional deterministic checks were performed independently. The checker's success does not cover all the separate checks requested here.

**Execution exception to the operator's no-Git instruction:** the stock checker internally invoked read-only `git cat-file -e …^{commit}` subprocesses. This was discovered on inspection of `tools/check_term.py` after its required initial execution and disclosed during the task. Thus this audit cannot claim that no Git command ran. No further Git command was run; no add, commit, push, checkout, or other Git mutation was issued. Subsequent provenance verification read and decompressed the object database directly, without invoking Git. This execution exception is recorded separately from the four unresolved repository-data findings; it cannot be undone by an adjudicative correction.

The 76 initial warnings are lexical false positives, not missing commit objects. Eighteen distinct source identifiers, numerical strings, or word fragments matched the broad hexadecimal pattern: Archive identifiers `A40385013`, `A40386002`, `A40386003`, `A40386007`, `A40386012`; source/URL strings `1000180149`, `1000180155`, `1662045`, `1994168`, `2006630`, `2035579`, `5223F70CBD862DEEE5634BA1F102E638`, `9780300050288`, `ec1395dd`; Technical Advice Memorandum `8314011`; the `b103272` fragment in `pub103272.pdf`; compressed reporter citation `e21F3d1038`; and `cceeded` within “succeeded.” The prior audit reproduced all eighteen tokens, contributing eighteen of this run's warnings. None of these strings claims to be a commit. Actual cited commits were separately verified as commit objects.

The read-only object reader verifies object SHA-1 identities, reconstructs packed deltas where necessary, checks object type, and resolves tree paths. The snapshot HEAD is `62840b9b190516cfc58a20233263292846911bf3`. All **101 current Record files** match their bytes in that HEAD tree. The pinned opening-state object `13b19ee463d16fb4377d846e5b058599f886bed3` and its Standing State link resolve. Priority completion/correction verification is reported below; no narrative history reconstruction was required.

The link scan covered **12,194 inline repository-link occurrences** outside the superseded Audit and downloaded-source directories. Candidate links to future publication locations in `state/HOLDINGS.md` were checked against the Holdings candidate where appropriate; 185 such links resolve prospectively. Fifty-five initial anchor flags were parser artifacts and were eliminated by correct heading parsing. **65 failures remain, all missing path targets; no remaining heading-anchor defect was found.** The scan inventoried 2,723 external URL occurrences but did not refetch outside sites. Repository-link resolution is not a certification of external availability or full source reading. No claim is made that a fact is absent from an unreviewed petition, brief, appendix, or transcript.

Evidence and reproducible read-only checks are in `tmp/ot1994_reaudit/`: inventory and coverage results; formal vote/topology extracts; proposition comparisons; refined link failures; candidate checks; direct-object provenance; priority comparisons; and protected-file fingerprints. Script flags were inspected before being accepted as findings. In particular, Evans's three-way 6–1–2 disposition is not a defective 6–1 tally, and NTEU's explanatory references to Scalia and Thomas in a “No opposing Justice” cell are not opposing votes.

## Unresolved findings

### F01 — Medium — Eight incorporated source links in four current Records still have missing local targets

The current Anderson v. Green Record has two missing source targets; Swint has two; the Plant Variety Protection Act Admitted Source Record has one; and the Vaccine Injury Table Admitted Source Record has three. The eight exact occurrences are in Appendix B. The previous correction repaired two other plant-variety source links, but these eight remain absent at their named locations.

This is a source-location and reproducibility defect in current authoritative Records. An available external citation or related document does not establish that the specifically incorporated local source exists. The defect does not itself establish that the recorded legal propositions are wrong. The required link-resolution gate nevertheless remains unsatisfied, and source-based legal review has not begun.

### F02 — Low — Fifty-seven additional handoff links still have missing targets

Appendix C lists every remaining occurrence in runtime and freeze files: **57 occurrences across 15 files**. Together with F01, the 65 occurrences resolve to **47 distinct missing absolute paths across 19 source files**. The surviving failures agree with the unresolved list in `freeze/OT_1994_AUDIT_CORRECTIONS.md`; the 141 previously repaired occurrences now resolve.

Frozen handoffs are historical evidence rather than current law. Their age does not make a broken source link resolve, but it also does not authorize silently rewriting their substance. These are navigation/source-copy defects, not a finding of a different current adjudication. No link destination or frozen text was changed in this pass.

### F03 — Low — Four supplied docket numbers remain absent from the Public Projection and Render Input

The chunk 7 render now correctly includes these dockets, under the expressly authorized correction recorded in `freeze/OT_1994_AUDIT_CORRECTIONS.md`. The canonical headers supply them, but each Record's bounded Public Projection omits its docket, and the generated chunk 7 Render Input faithfully reproduces that omission.

| Matter | Missing docket in projection/input | Public Projection begins |
|---|---|---|
| Adarand Constructors, Inc. v. Peña | 93-1841 | `records/Adarand_Constructors_Inc_v_Pena_merits_1995-06-12.md:135` |
| Wilton v. Seven Falls Co. | 94-562 | `records/Wilton_v_Seven_Falls_Co_merits_1995-06-12.md:99` |
| Metropolitan Stevedore Co. v. Rambo | 94-820 | `records/Metropolitan_Stevedore_Co_v_Rambo_merits_1995-06-12.md:109` |
| Johnson v. Jones | 94-455 | `records/Johnson_v_Jones_merits_1995-06-12.md:90` |

The prior audit incorrectly described these dockets as already supplied in the Render Input. Current inspection confirms they are absent throughout their respective input entries. The render omissions are repaired; the upstream metadata omissions are not. This is an Event-block completeness defect under the Engine/Render Contract, with no identified change to the judgments. The authorized render correction is not treated as an unauthorized substantive addition.

### F04 — Low — Word-separation artifacts remain in projections and candidate text

The mechanical text review found **68 occurrences on 56 lines**, listed individually by file, line, and token in Appendix D. Examples include `September1`, `Section1983`, and `PartsI andII` in Kelley's Public Projection and chunk 6 input; `October11` and `November25` in Nebraska's corresponding fields; fused month/day text in current dependency rows; and inherited `Section1500` and similar expressions in the Holdings candidate and its Standards navigation.

These are missing spaces, not findings that a date, statutory section, holding, or join is substantively wrong. The render text already separates the identified public tokens. The candidate artifacts include text carried from the term-opening registers; they were not all introduced in OT1994. Their inherited origin is disclosed rather than used to suppress the finding. Internal abbreviated research digests were not classified as public-prose defects merely because they use compressed notation. No spacing, heading, or dependent anchor was changed here.

## Deterministic results and limits

| Required check | Result |
|---|---|
| Initial `check_term.py` | Exit 0; 76 false-positive lexical warnings triaged. Its internal Git invocation is disclosed above. The separate gate fails on F01–F04. |
| Inventory → manifest → Record → Render Input → render | **99/99**, each once, with corresponding dates and canonical dockets. There are 101 Records: 99 Court matters plus two noncase source admissions. All nine renders exist; chunks 1–8 have 12 entries each and chunk 9 has 3. All 99 chronology rows and dated entry boundaries agree with their Records. Four upstream docket omissions remain F03. |
| Effective-date order | Current inventory, manifest inventory rows, generated event sequences, and renders follow November 1, 1994 through June 29, 1995. The March 10 Vaccine Table and April 4 plant-variety source admissions retain their effective dates and disclosed late-insertion treatment. Pinette precedes Chabad under their express coordinated June 29 sequence; other same-day peers acquire no priority from file order. No additional date/order discrepancy found. Substantive sufficiency of entering law is deferred. |
| Participation, votes and joins | Named formal judgment and author-inclusive topology fields were screened for all 99 matters, including prose and three-column tables. The six reduced-Court matters preserve their named exclusions: FEC (Ginsburg), Wolens (Scalia), Grubart (Stevens and Breyer), City of Milwaukee (Breyer), Wilton (Breyer), Sky Reefer (Breyer). All have a quorum. Partial joins and judgment-only votes were kept distinct. No additional formal arithmetic discrepancy found; legal compatibility and justification of the joins are deferred. |
| Runtime freshness | All nine approved briefs agree with all 27 normal `_NEUTRAL`, `_STONE`, and `_COMPARATOR` exports. Freshness does not turn historical freezes or superseded assembly drafts into current law. |
| Public Projection → Render Input identity | All **99 generated Court-event bodies match exactly**, after the builder's boundary trimming. The two admitted-source Records retain their prescribed public interfaces without being counted as additional inventory Court renders. |
| Holdings projection coverage | All **236 controlling-proposition blocks** appear in their Record's substantive portion and in the corresponding public render. The candidate contains 235 normalized exact matches and one Clearwater equivalent that deletes only the locative word “below.” This is text coverage, not legal approval. |
| Both Holdings passes | Pass 1 covers matters 1–60/chunks 1–5: **154 propositions**. Pass 2 covers matters 61–99/chunks 6–9: **82 propositions**. Both notes and the cumulative candidate were checked. Their earlier reports of missing Robertson/render dockets describe the pre-correction state and do not establish present omissions. |
| Standards and Tests candidate | **370 entries**, with the pass accounting for all 101 Records. Structural comparison confirms 275 unchanged opening entries after normalizing whitespace, nine revised entries under unchanged titles, five renamed/expanded opening entries, and 81 additions. No omitted source-file link was treated as an automatically missing reusable rule. Independent legal entailment, consolidation, component limits and omissions remain for the deferred audit. |
| Candidate header synchronization | All three candidates retain identical staged baseline fields: Last completed OT1993; processed through June 30, 1994 after all eleven chunk-8 matters and all 95 OT1993 inventory Court events; edition September 28, 2026. The retained header is expressly disclosed pending coordinated publication. Standing State separately identifies opening OT1995. |
| Links and anchors | 12,194 repository occurrences checked; **65 missing targets**, fully listed in Appendices B–C. Prospective candidate anchors resolve when mapped to their intended publication content. External-site availability and full source reading were not certified. |
| Commit existence and concise lineage | Actual cited commit objects resolve. The six priority histories were directly verified; all 101 current Records match HEAD. Current Morales/Stone lineage is accurate. The ledger now truthfully records prior preservation and the authorized file-order fallback, with first-record hashes expressly unverified. That disclosed authorized fallback is not repeated as the former false “uncommitted” finding. |
| Candidate cleanup | Exactly three active candidates, two Holdings pass notes, one Standards pass note, one Audit, and `.gitkeep` in `close/`. No duplicate candidate, close dossier, or post-Commit index implies a completed close. Candidates and temporary pass notes must remain until successful Commit; they were not deleted. |
| Open-matter carry-forward | Nine retained matters remain in the coordinated current state and Standing State candidate: Zatko and sixteen companions; Wyoming v. Oklahoma; Reynolds; Grubbs; United States v. Louisiana; Delaware v. New York; Nebraska v. Wyoming; In re Anderson; Kansas v. Colorado. The candidate separately lists the ten user-added OT1995 matters. The Nebraska exceptions decision does not close the original action. No terminal event was invented. |
| Next-term setting | OT1995 roster/seniority, all thirteen circuit allotments under the August 3, 1994 order, and the standing referral practice agree with the governing composition and opening state. Standing State has only the header and four authorized setting/docket sections. Legal assessment of the new docket items is deferred. |
| Render form and public boundary | All 99 events state a selected form: 70 full and 29 compact. Every full-form entry has judgment and opinion tables; every event has its dated boundary and closing line. No additional workflow-leak flag survived contextual review. Whether every form choice meets the material-change criterion remains part of the deferred legal review. |

## Priority completion/correction reconciliation

These are current-file, public-field, and concise-provenance checks. They do not stand in for the deferred Justice-specific legal audit. In every row, the current Public Projection exactly equals the generated input entry; the render carries the indicated current disposition, writing structure, and bounded remedy.

| Matter | Current Record, input and render | Verified concise history |
|---|---|---|
| Interstate Commerce Commission v. Transcon Lines | Chunk 1: 9–0 reversal/remand; Kennedy's unanimous Court opinion; implementation confined to the admitted-unlawful loss-of-discount class, preserving genuine inclusion/amount questions and excluding ordinary freight principal and other receivables. Current render present. | `acec437d236d6d12e54bd53b191a233f57f52916`: first completed Record; path absent in parent; current Record unchanged from this object. Earlier stopped intake is not an earlier adjudication. |
| Fargo Women's Health Organization v. Schafer | Chunk 2: access vacatur/remand 6–3; the two definition-vagueness rejections and bounded penalty rejection affirmed 8–1. Souter's part-specific joins and Stone's partial concurrence/dissent are preserved; access remand is not extended to the affirmed components. | `f6afbf7f1a82d7ea26633bb04df475c3c4356f43`: first completed Record; path absent in parent; current Record unchanged. Earlier incomplete freezes are stage history. |
| O'Neal v. McAninch | Chunk 3: 7–2 vacatur/remand; five votes for the confined Chapman instruction, three for the proposed broader extension. O'Connor's controlling portions and the separate Stevens/Kennedy judgment agreement remain distinct; conditional-writ limits preserved. | `b3ce99c5c54607c27c5893c25cc52fc04efcca70`: first completed Record; path absent in parent; current Record unchanged. No earlier completed adjudication is silently displaced. |
| United States v. Robertson | Chunk 5 now includes the previously missing public entry and chronology row. Record, input and render agree on 9–0 reversal of the commerce-based Count Six ruling, Breyer's unanimous Court opinion, remaining RICO appellate proceedings, and the independent drug resentencing posture. | `0fcb6a5c2d5485cf0591f852f4fbf859d4b1f3bf`: first completed Record; path absent in parent; current Record unchanged. The prior inconclusive source report remains expressly superseded research history. |
| California Department of Corrections v. Morales | Chunk 5: **5–4 affirmance**, Stone-Zsela, Stevens, O'Connor, Souter and Ginsburg; O'Connor's Court opinion, Stone concurrence, Kennedy dissent joined by Scalia, Thomas and Breyer. Offense-date annual consideration is preserved; no parole order is entered. Candidate Holdings and Standards retain this current outcome/limited rule rather than the former reversal. | `d086219b424d812aaa837fda9533629c69e33833`: replacement verified. Current Record differs from that object only in the subsequently corrected lineage line; Public Projection unchanged. Its old assembly draft has a top-line superseded-history notice and link to the current Record. |
| Stone v. Immigration and Naturalization Service | Chunk 5: 5–4 affirmance; Kennedy Court opinion and Breyer dissent unchanged. Current internal paragraph models Stevens's ordinary assignment discretion; it does not apply the Chief's fit/expansion method to Stevens. Public Projection and render were unaffected by that internal correction. | `8d98261d33b6d39fda8a9ccc52ab5ad7ed3be02a`: comparison with its parent confirms exactly one assignment-paragraph replacement. Current Record differs from that correction object only in the repaired lineage line. The historical assembly draft is now expressly labeled superseded. |

**Retained history and the “no stale version anywhere” request.** No duplicate priority-case Canonical Decision Record or undisclosed competing current result was found. A literal assertion that all superseded text has disappeared would be false: `runtime/assembly/California_Department_of_Corrections_v_Morales_merits_1995-04-25.md` and `runtime/assembly/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md` retain old drafting text, each now explicitly marked as superseded historical material on line 1. Immutable pre-correction commitments/reconciliations and stopped-intake research also remain. The recorded prior correction expressly authorized labeled retention; those files are not counted as unresolved current-law defects. The old reversal and old assignment paragraph were not found operating as current law in the Record/input/render set or current candidate projections. Ignored scratch copies and Git history are evidence, not current authority.

## Previous audit findings resolved by the intervening correction

- Robertson now has a full bounded public entry; all 99 matters are rendered.
- The four chunk 7 render dockets are present. Their upstream omission is separately retained as current F03.
- Of the former 206 failed repository-link occurrences, 141 now resolve; F01–F02 enumerate the surviving 65.
- The two historical assembly drafts are now explicitly marked superseded, as the authorized correction required.
- Morales and Stone v. INS now have concise accurate correction lineage; Williams identifies itself as a completed Canonical Decision Record.
- The 101 ledger rows no longer falsely mark preserved Records as uncommitted. The authorized file-preservation-order fallback and unverified first-record hashes are expressly disclosed.
- Sky Reefer's two participation rows now identify Breyer's nonparticipation and eight participants.
- Nebraska's six-column continuity row is correctly aligned and preserves the May 30 authority and continued original proceeding.
- All five previously identified question-mark corruptions are absent from their current Record/input/render/workspace locations. The final neutral projection no longer describes Lopez as future law.

These are fresh checks of the current files, not reliance on the repair receipt as proof. Temporary pass notes and historical validation receipts accurately remain records of their respective earlier passes; they are not new current-state certifications.

## Appendix A — Every inventory matter

Every row received membership, date, public-boundary, interface-identity, and formal vote/topology screening. All have one current Record, one generated input entry and one public render entry. **Legal-substance review is deferred for every row.** “Pass” below concerns these deterministic coverage checks only; other findings affecting source links or metadata remain as identified above.

| No. | Chunk | Matter | Effective date | Record/input/render coverage |
|---:|---:|---|---|---|
| 1 | 1 | United States v. Shabani | 1994-11-01 | Pass |
| 2 | 1 | U.S. Bancorp Mortgage Co. v. Bonner Mall Partnership | 1994-11-08 | Pass |
| 3 | 1 | Hess v. Port Authority Trans-Hudson Corp. | 1994-11-14 | Pass |
| 4 | 1 | United States v. X-Citement Video, Inc. | 1994-11-29 | Pass |
| 5 | 1 | Church of Scientology Flag Service Organization, Inc. v. City of Clearwater + | 1994-12-05 | Pass |
| 6 | 1 | Federal Election Commission v. NRA Political Victory Fund | 1994-12-06 | Pass |
| 7 | 1 | Reich v. Collins | 1994-12-06 | Pass |
| 8 | 1 | Brown v. Gardner | 1994-12-12 | Pass |
| 9 | 1 | Nebraska Department of Revenue v. Loewenstein | 1994-12-12 | Pass |
| 10 | 1 | In re Baby K + | 1994-12-12 | Pass |
| 11 | 1 | Plakas v. Drinski + | 1995-01-09 | Pass |
| 12 | 1 | Interstate Commerce Commission v. Transcon Lines | 1995-01-10 | Pass |
| 13 | 2 | Tome v. United States | 1995-01-10 | Pass |
| 14 | 2 | Young v. Northern Illinois Conference of United Methodist Church + | 1995-01-17 | Pass |
| 15 | 2 | Asgrow Seed Co. v. Winterboer | 1995-01-18 | Pass |
| 16 | 2 | United States v. Mezzanatto | 1995-01-18 | Pass |
| 17 | 2 | American Airlines, Inc. v. Wolens | 1995-01-18 | Pass |
| 18 | 2 | NationsBank of North Carolina, N.A. v. Variable Annuity Life Insurance Co. / Ludwig v. Variable Annuity Life Insurance Co. | 1995-01-18 | Pass |
| 19 | 2 | Allied-Bruce Terminix Cos. v. Dobson | 1995-01-18 | Pass |
| 20 | 2 | Schlup v. Delo | 1995-01-23 | Pass |
| 21 | 2 | McKennon v. Nashville Banner Publishing Co. | 1995-01-23 | Pass |
| 22 | 2 | Fargo Women’s Health Organization v. Schafer + | 1995-02-13 | Pass |
| 23 | 2 | Lebron v. National Railroad Passenger Corp. | 1995-02-21 | Pass |
| 24 | 2 | Milwaukee Brewery Workers' Pension Plan v. Jos. Schlitz Brewing Co. | 1995-02-21 | Pass |
| 25 | 3 | O'Neal v. McAninch | 1995-02-21 | Pass |
| 26 | 3 | United States v. National Treasury Employees Union | 1995-02-22 | Pass |
| 27 | 3 | Harris v. Alabama | 1995-02-22 | Pass |
| 28 | 3 | Jerome B. Grubart, Inc. v. Great Lakes Dredge & Dock Co. / City of Chicago v. Great Lakes Dredge & Dock Co. | 1995-02-22 | Pass |
| 29 | 3 | Anderson v. Green | 1995-02-22 | Pass |
| 30 | 3 | Gustafson v. Alloyd Co. | 1995-02-28 | Pass |
| 31 | 3 | Arizona v. Evans | 1995-03-01 | Pass |
| 32 | 3 | Swint v. Chambers County Commission | 1995-03-01 | Pass |
| 33 | 3 | Mastrobuono v. Shearson Lehman Hutton, Inc. | 1995-03-06 | Pass |
| 34 | 3 | Curtiss-Wright Corp. v. Schoonejongen | 1995-03-06 | Pass |
| 35 | 3 | Shalala v. Guernsey Memorial Hospital | 1995-03-06 | Pass |
| 36 | 3 | Ambassador Books & Video, Inc. v. City of Little Rock + | 1995-03-20 | Pass |
| 37 | 4 | Director, Office of Workers’ Compensation Programs v. Newport News Shipbuilding & Dry Dock Co. | 1995-03-21 | Pass |
| 38 | 4 | Anderson v. Edwards | 1995-03-22 | Pass |
| 39 | 4 | Swanner v. Anchorage Equal Rights Commission + | 1995-03-27 | Pass |
| 40 | 4 | Qualitex Co. v. Jacobson Products Co. | 1995-03-28 | Pass |
| 41 | 4 | Oklahoma Tax Commission v. Jefferson Lines, Inc. | 1995-04-03 | Pass |
| 42 | 4 | Plaut v. Spendthrift Farm, Inc. | 1995-04-18 | Pass |
| 43 | 4 | Shalala v. Whitecotton | 1995-04-18 | Pass |
| 44 | 4 | Freightliner Corp. v. Myrick | 1995-04-18 | Pass |
| 45 | 4 | Heintz v. Jenkins | 1995-04-18 | Pass |
| 46 | 4 | Lanphere & Urbaniak v. Colorado + | 1995-04-18 | Pass |
| 47 | 4 | Celotex Corp. v. Edwards | 1995-04-19 | Pass |
| 48 | 4 | McIntyre v. Ohio Elections Commission | 1995-04-19 | Pass |
| 49 | 5 | Stone v. Immigration and Naturalization Service | 1995-04-19 | Pass |
| 50 | 5 | Kyles v. Whitley | 1995-04-19 | Pass |
| 51 | 5 | Rubin v. Coors Brewing Co. | 1995-04-19 | Pass |
| 52 | 5 | California Department of Corrections v. Morales | 1995-04-25 | Pass |
| 53 | 5 | United States v. Williams | 1995-04-25 | Pass |
| 54 | 5 | United States v. Lopez | 1995-04-26 | Pass |
| 55 | 5 | New York State Conference of Blue Cross & Blue Shield Plans v. Travelers Insurance Co. / Pataki v. Travelers Insurance Co. / Hospital Association of New York State v. Travelers Insurance Co. | 1995-04-26 | Pass |
| 56 | 5 | United States v. Harris + | 1995-04-27 | Pass |
| 57 | 5 | United States v. Robertson | 1995-05-01 | Pass |
| 58 | 5 | United States v. Pinson + | 1995-05-08 | Pass |
| 59 | 5 | Kansas v. Colorado | 1995-05-15 | Pass |
| 60 | 5 | Hubbard v. United States | 1995-05-15 | Pass |
| 61 | 6 | City of Edmonds v. Oxford House, Inc. | 1995-05-15 | Pass |
| 62 | 6 | Reynoldsville Casket Co. v. Hyde | 1995-05-15 | Pass |
| 63 | 6 | Day v. Holahan + | 1995-05-15 | Pass |
| 64 | 6 | U.S. Term Limits, Inc. v. Thornton / Bryant v. Hill | 1995-05-22 | Pass |
| 65 | 6 | Wilson v. Arkansas | 1995-05-22 | Pass |
| 66 | 6 | First Options of Chicago, Inc. v. Kaplan | 1995-05-22 | Pass |
| 67 | 6 | Kelley v. Board of Trustees of the University of Illinois + | 1995-05-22 | Pass |
| 68 | 6 | Nebraska v. Wyoming | 1995-05-30 | Pass |
| 69 | 6 | North Star Steel Co. v. Thomas / Crown Cork & Seal Co., Inc. v. United Steelworkers of America, AFL-CIO-CLC | 1995-05-30 | Pass |
| 70 | 6 | Garlotte v. Fordice | 1995-05-30 | Pass |
| 71 | 6 | United States v. Wellons + | 1995-05-30 | Pass |
| 72 | 6 | Reno v. Koray | 1995-06-05 | Pass |
| 73 | 7 | Metropolitan Washington Airports Authority v. Hechinger + | 1995-06-05 | Pass |
| 74 | 7 | Missouri v. Jenkins | 1995-06-12 | Pass |
| 75 | 7 | Ryder v. United States | 1995-06-12 | Pass |
| 76 | 7 | City of Milwaukee v. Cement Division, National Gypsum Co. | 1995-06-12 | Pass |
| 77 | 7 | Adarand Constructors, Inc. v. Peña | 1995-06-12 | Pass |
| 78 | 7 | Wilton v. Seven Falls Co. | 1995-06-12 | Pass |
| 79 | 7 | Metropolitan Stevedore Co. v. Rambo | 1995-06-12 | Pass |
| 80 | 7 | Johnson v. Jones | 1995-06-12 | Pass |
| 81 | 7 | Kimberlin v. Quinlan | 1995-06-12 | Pass |
| 82 | 7 | Commissioner v. Schleier | 1995-06-14 | Pass |
| 83 | 7 | Chandris, Inc. v. Latsis | 1995-06-14 | Pass |
| 84 | 7 | Witte v. United States | 1995-06-14 | Pass |
| 85 | 8 | Gutierrez de Martinez v. Lamagno | 1995-06-14 | Pass |
| 86 | 8 | Oklahoma Tax Commission v. Chickasaw Nation | 1995-06-14 | Pass |
| 87 | 8 | Sandin v. Conner | 1995-06-19 | Pass |
| 88 | 8 | United States v. Gaudin | 1995-06-19 | Pass |
| 89 | 8 | Vimar Seguros y Reaseguros, S.A. v. M/V Sky Reefer | 1995-06-19 | Pass |
| 90 | 8 | Hurley v. Irish-American Gay, Lesbian and Bisexual Group of Boston | 1995-06-19 | Pass |
| 91 | 8 | National Private Truck Council, Inc. v. Oklahoma Tax Commission | 1995-06-19 | Pass |
| 92 | 8 | United States v. Aguilar | 1995-06-21 | Pass |
| 93 | 8 | Florida Bar v. Went For It, Inc. | 1995-06-21 | Pass |
| 94 | 8 | Vernonia School District 47J v. Acton | 1995-06-26 | Pass |
| 95 | 8 | Rosenberger v. Rector and Visitors of the University of Virginia | 1995-06-29 | Pass |
| 96 | 8 | Babbitt v. Sweet Home Chapter of Communities for a Great Oregon | 1995-06-29 | Pass |
| 97 | 9 | Miller v. Johnson / Abrams v. Johnson / United States v. Johnson | 1995-06-29 | Pass |
| 98 | 9 | Capitol Square Review and Advisory Board v. Pinette | 1995-06-29 | Pass |
| 99 | 9 | Chabad-Lubavitch of Georgia v. Miller + | 1995-06-29 | Pass |

The March 10, 1995 Vaccine Injury Table and April 4, 1995 Plant Variety Protection Act source admissions were additionally checked as noncase Records; they are not additional Court inventory matters.

## Appendix B — F01: missing source links in current Records

| Current Record | Line | Missing target as written |
|---|---:|---|
| `records/Anderson_v_Green_decision_1995-02-22.md` | 85 | `../sources/chunk3-b-neutral/SOURCES.md` |
| `records/Anderson_v_Green_decision_1995-02-22.md` | 85 | `../sources/chunk3-b-neutral/Anderson_primary_excerpts.md` |
| `records/Plant_Variety_Protection_Act_Amendments_statutory_effectiveness_1995-04-04.md` | 8 | `../sources/chunk4/S_1406_enrolled.html` |
| `records/Swint_v_Chambers_County_Commission_merits_1995-03-01.md` | 118 | `../sources/chunk3-b-swint-supplement/Swint_lower_orders_App_44_73.pdf` |
| `records/Swint_v_Chambers_County_Commission_merits_1995-03-01.md` | 118 | `../sources/chunk3-b-swint-supplement/Swint_lower_orders_App_44_73.txt` |
| `records/Vaccine_Injury_Table_regulatory_effectiveness_1995-03-10.md` | 8 | `../sources/chunk4/Vaccine_Table_60_FR_7678.pdf` |
| `records/Vaccine_Injury_Table_regulatory_effectiveness_1995-03-10.md` | 8 | `../sources/chunk4/Vaccine_Table_60_FR_7678_pdf_text.txt` |
| `records/Vaccine_Injury_Table_regulatory_effectiveness_1995-03-10.md` | 8 | `../sources/chunk4/Vaccine_Table_60_FR_7678.txt` |

## Appendix C — F02: remaining handoff link failures

Each row is one current unresolved link occurrence. Line numbers refer to the audited working files, not the older audit.

| Source file | Line | Missing target as written |
|---|---:|---|
| `freeze/OT_1994CHUNK3_CHRONOLOGY_B.md` | 22 | `../sources/chunk3-b-neutral/Gustafson_lower_orders_App_1_14.txt` |
| `freeze/OT_1994CHUNK3_COMMITMENTS_B.md` | 7 | `../sources/chunk3-b-neutral/SOURCES.md` |
| `freeze/OT_1994CHUNK3_EVANS_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 9 | `../sources/chunk3-b-evans-supplement/Evans_joint_appendix.pdf` |
| `freeze/OT_1994CHUNK3_EVANS_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 9 | `../sources/chunk3-b-evans-supplement/Evans_joint_appendix.txt` |
| `freeze/OT_1994CHUNK3_EVANS_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 10 | `../sources/chunk3-b-evans-supplement/Evans_petitioners_brief.pdf` |
| `freeze/OT_1994CHUNK3_EVANS_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 10 | `../sources/chunk3-b-evans-supplement/Evans_petitioners_brief.txt` |
| `freeze/OT_1994CHUNK3_EVANS_NEUTRAL_VALIDATED.md` | 63 | `../sources/chunk3-b-evans-supplement/Evans_joint_appendix.pdf` |
| `freeze/OT_1994CHUNK3_EVANS_NEUTRAL_VALIDATED.md` | 63 | `../sources/chunk3-b-evans-supplement/Evans_petitioners_brief.pdf` |
| `freeze/OT_1994CHUNK3_NEUTRAL_B_CANDIDATE.md` | 13 | `../sources/chunk3-b-neutral/SOURCES.md` |
| `freeze/OT_1994CHUNK3_NEUTRAL_B_CANDIDATE.md` | 31 | `../sources/chunk3-b-neutral/Anderson_primary_excerpts.md` |
| `freeze/OT_1994CHUNK3_NEUTRAL_B_CANDIDATE.md` | 61 | `../sources/chunk3-b-neutral/Gustafson_lower_orders_App_1_14.txt` |
| `freeze/OT_1994CHUNK3_NEUTRAL_B_VALIDATED.md` | 15 | `../sources/chunk3-b-neutral/SOURCES.md` |
| `freeze/OT_1994CHUNK3_NEUTRAL_B_VALIDATED.md` | 33 | `../sources/chunk3-b-neutral/Anderson_primary_excerpts.md` |
| `freeze/OT_1994CHUNK3_NEUTRAL_B_VALIDATED.md` | 63 | `../sources/chunk3-b-neutral/Gustafson_lower_orders_App_1_14.txt` |
| `freeze/OT_1994CHUNK3_NTEU_CRANE_NEUTRAL_VALIDATED.md` | 9 | `../sources/chunk3-a-crane-supplement/NTEU_petitioners_brief.pdf` |
| `freeze/OT_1994CHUNK3_NTEU_CRANE_NEUTRAL_VALIDATED.md` | 9 | `../sources/chunk3-a-crane-supplement/NTEU_petitioners_brief.txt` |
| `freeze/OT_1994CHUNK3_NTEU_CRANE_NEUTRAL_VALIDATED.md` | 10 | `../sources/chunk3-a-crane-supplement/NTEU_reply_brief.pdf` |
| `freeze/OT_1994CHUNK3_NTEU_CRANE_NEUTRAL_VALIDATED.md` | 10 | `../sources/chunk3-a-crane-supplement/NTEU_reply_brief.txt` |
| `freeze/OT_1994CHUNK3_PREFLIGHT_B.md` | 8 | `../sources/chunk3-b-neutral/SOURCES.md` |
| `freeze/OT_1994CHUNK3_RECONCILED_B.md` | 11 | `../sources/chunk3-b-neutral/SOURCES.md` |
| `freeze/OT_1994CHUNK3_SWINT_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 5 | `../sources/chunk3-b-swint-supplement/Swint_petition_appendix.pdf` |
| `freeze/OT_1994CHUNK3_SWINT_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 5 | `../sources/chunk3-b-swint-supplement/Swint_petition_appendix.txt` |
| `freeze/OT_1994CHUNK3_SWINT_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 7 | `../sources/chunk3-b-swint-supplement/Swint_lower_orders_App_44_73.pdf` |
| `freeze/OT_1994CHUNK3_SWINT_NEUTRAL_RECORD_SUPPLEMENT_CANDIDATE.md` | 7 | `../sources/chunk3-b-swint-supplement/Swint_lower_orders_App_44_73.txt` |
| `freeze/OT_1994CHUNK3_SWINT_NEUTRAL_RECORD_VALIDATED.md` | 13 | `../sources/chunk3-b-swint-supplement/Swint_lower_orders_App_44_73.pdf` |
| `freeze/OT_1994CHUNK3_SWINT_NEUTRAL_RECORD_VALIDATED.md` | 13 | `../sources/chunk3-b-swint-supplement/Swint_lower_orders_App_44_73.txt` |
| `runtime/OT_1994CHUNK3_COMMITMENTS.md` | 350 | `../sources/chunk3-b-neutral/SOURCES.md` |
| `runtime/OT_1994CHUNK3_RECONCILED.md` | 314 | `../sources/chunk3-b-neutral/SOURCES.md` |
| `runtime/OT_1994CHUNK4_JEFFERSON_SOURCE_SUPPLEMENT.md` | 3 | `../sources/chunk4/jefferson_briefs/manifest.json` |
| `runtime/OT_1994CHUNK4_JEFFERSON_SOURCE_SUPPLEMENT.md` | 40 | `../sources/chunk4/jefferson_briefs/petitioner.txt` |
| `runtime/OT_1994CHUNK4_JEFFERSON_SOURCE_SUPPLEMENT.md` | 40 | `../sources/chunk4/jefferson_briefs/respondent.txt` |
| `runtime/OT_1994CHUNK4_JEFFERSON_SOURCE_SUPPLEMENT.md` | 40 | `../sources/chunk4/jefferson_briefs/joint_appendix.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 25 | `../sources/chunk4/Newport_News_8_F3d_175.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 25 | `../sources/chunk4/LHWCA_1994_921.htm` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 25 | `../sources/chunk4/LHWCA_1994_939.htm` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 43 | `../sources/chunk4/Anderson_lower_12_F3d_154.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 43 | `../sources/chunk4/Beaton_913_F2d_701.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 55 | `../sources/chunk4/RFRA_107_Stat_1488.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 61 | `../sources/chunk4/Swanner_874_P2d_274.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 75 | `../sources/chunk4/Qualitex_13_F3d_1297.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 75 | `../sources/chunk4/Lanham_1994_1052.htm` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 75 | `../sources/chunk4/Lanham_1994_1127.htm` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 91 | `../sources/chunk4/Jefferson_Lines_15_F3d_90.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 107 | `../sources/chunk4/Plaut_1_F3d_1487.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 123 | `../sources/chunk4/Whitecotton_17_F3d_374.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 123 | `../sources/chunk4/Vaccine_Table_60_FR_7678_pdf_text.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 139 | `../sources/chunk4/Myrick_13_F3d_1516.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 139 | `../sources/chunk4/Paccar_573_F2d_632.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 151 | `../sources/chunk4/Jenkins_25_F3d_536.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 151 | `../sources/chunk4/FDCPA_1986_amendment.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 153 | `../sources/chunk4/FDCPA_1977_91_Stat_874.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 169 | `../sources/chunk4/Lanphere_21_F3d_1508.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 183 | `../sources/chunk4/Edwards_6_F3d_312.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 183 | `../sources/chunk4/Bankruptcy_1994_105.htm` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 197 | `../sources/chunk4/McIntyre_67_Ohio_St3d_391.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 209 | `../sources/chunk4/Shapero_486_US_466.txt` |
| `runtime/OT_1994CHUNK4_VALIDATED_NEUTRAL.md` | 213 | `../sources/chunk4/Bowen_Gilliard_483_US_587.txt` |

## Appendix D — F04: word-separation artifacts

The table groups tokens on the same line; repeated tokens are retained. It accounts for all 68 observed occurrences on 56 lines. Candidate occurrences carried from the opening baseline remain candidate-text issues, not newly adjudicated OT1994 law.

| Current file | Line | Token(s) lacking word separation |
|---|---:|---|
| `records/Kelley_v_Board_of_Trustees_of_the_University_of_Illinois_merits_1995-05-22.md` | 155 | `September1`, `October5`, `March28` |
| `records/Kelley_v_Board_of_Trustees_of_the_University_of_Illinois_merits_1995-05-22.md` | 167 | `Section1983` |
| `records/Kelley_v_Board_of_Trustees_of_the_University_of_Illinois_merits_1995-05-22.md` | 171 | `PartsI`, `andII` |
| `records/Nebraska_v_Wyoming_original_exceptions_1995-05-30.md` | 323 | `October11`, `November25` |
| `records/Nebraska_v_Wyoming_original_exceptions_1995-05-30.md` | 466 | `November25`, `April20` |
| `render-inputs/OT_1994CHUNK6.md` | 329 | `September1`, `October5`, `March28` |
| `render-inputs/OT_1994CHUNK6.md` | 341 | `Section1983` |
| `render-inputs/OT_1994CHUNK6.md` | 345 | `PartsI`, `andII` |
| `render-inputs/OT_1994CHUNK6.md` | 600 | `October11`, `November25` |
| `render-inputs/OT_1994CHUNK6.md` | 743 | `November25`, `April20` |
| `workspace/manifest.md` | 143 | `June19` |
| `workspace/manifest.md` | 144 | `June19` |
| `workspace/manifest.md` | 145 | `June19` |
| `workspace/manifest.md` | 146 | `June21` |
| `workspace/manifest.md` | 147 | `June21` |
| `workspace/manifest.md` | 148 | `June29` |
| `workspace/neutral-projection.md` | 5588 | `June19` |
| `workspace/neutral-projection.md` | 5589 | `June19` |
| `workspace/neutral-projection.md` | 5590 | `June19` |
| `workspace/neutral-projection.md` | 5591 | `June21` |
| `workspace/neutral-projection.md` | 5592 | `June21` |
| `workspace/neutral-projection.md` | 5593 | `June29` |
| `close/HOLDINGS.candidate.md` | 3683 | `May4` |
| `close/HOLDINGS.candidate.md` | 3684 | `April1` |
| `close/HOLDINGS.candidate.md` | 3775 | `February25` |
| `close/HOLDINGS.candidate.md` | 3853 | `Section1500` |
| `close/HOLDINGS.candidate.md` | 3855 | `Section1500` |
| `close/HOLDINGS.candidate.md` | 4115 | `Section1255a` |
| `close/HOLDINGS.candidate.md` | 4123 | `Section1255a` |
| `close/HOLDINGS.candidate.md` | 7088 | `March9` |
| `close/HOLDINGS.candidate.md` | 7103 | `March9` |
| `close/HOLDINGS.candidate.md` | 7127 | `December8` |
| `close/HOLDINGS.candidate.md` | 7230 | `December4` |
| `close/HOLDINGS.candidate.md` | 7231 | `April21` |
| `close/HOLDINGS.candidate.md` | 7251 | `May17` |
| `close/HOLDINGS.candidate.md` | 10475 | `Section1401` |
| `close/HOLDINGS.candidate.md` | 10485 | `Section1393` |
| `close/HOLDINGS.candidate.md` | 10486 | `Section1401` |
| `close/HOLDINGS.candidate.md` | 11806 | `March24`, `April26` |
| `close/HOLDINGS.candidate.md` | 13679 | `December16` |
| `close/HOLDINGS.candidate.md` | 14554 | `Section243` |
| `close/HOLDINGS.candidate.md` | 15114 | `Section502` |
| `close/HOLDINGS.candidate.md` | 15129 | `May26` |
| `close/HOLDINGS.candidate.md` | 15130 | `February26` |
| `close/HOLDINGS.candidate.md` | 15141 | `Section302` |
| `close/HOLDINGS.candidate.md` | 15178 | `April20` |
| `close/HOLDINGS.candidate.md` | 16124 | `Section1322` |
| `close/HOLDINGS.candidate.md` | 16617 | `Section4975` |
| `close/HOLDINGS.candidate.md` | 17451 | `February26` |
| `close/HOLDINGS.candidate.md` | 17514 | `Section1012` |
| `close/HOLDINGS.candidate.md` | 18376 | `February22` |
| `close/HOLDINGS.candidate.md` | 18745 | `June8` |
| `close/HOLDINGS.candidate.md` | 18757 | `December3` |
| `close/HOLDINGS.candidate.md` | 18786 | `January25` |
| `close/HOLDINGS.candidate.md` | 18865 | `Section6a` |
| `close/STANDARDS_AND_TESTS.candidate.md` | 411 | `Section1500`, `Section1500` |

## Completion boundary

The deterministic gate fails. The fresh substantive review of all 99 matters and the full close candidates has **not** been performed and must not be inferred from this report's arithmetic or text-coverage results. This audit authorizes no correction and no term close. The operator verifies and commits the Audit; any corrections and later audit are separate tasks.

**Operator summary: FAIL. Findings: 0 critical; 0 high; 1 medium; 3 low.**
