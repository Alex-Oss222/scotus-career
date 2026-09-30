# October Term 1994 — close audit

**Result: FAIL — deterministic gate not passed; fresh substantive audit not commenced.**

**Audit date:** September 30, 2026.  
**Confirmed unresolved findings:** 2 — 0 critical, 0 high, 1 medium, 1 low.  
**Publication status:** This report does not clear the term or the candidates for close.

The audit found superseded Morales material still presented as current entering law and a missing required render boundary. External-link reachability also remains partly unverified. The instruction for this task expressly permits the fresh legal audit **only after** the deterministic checks pass. Consequently, this report does not certify the legal substance of any of the 99 matters, either Holdings pass, Standards and Tests, or Standing State. It reports the deterministic work actually completed and its limits. The prior audit's legal findings have not been freshly cleared by this pass.

Only this file and scratch files under root `tmp/ot1994_audit/` were written. No adjudication, candidate, render, runtime, freeze, entering-law slice, workspace projection, foundation file, or published tracker was changed. No Git command was executed.

## 1. Unresolved findings

### F01 — Medium — Superseded Morales law remains in four unmarked entering-law slices and two assembly copies

The current [Morales Record](../records/California_Department_of_Corrections_v_Morales_merits_1995-04-25.md) affirms the Ninth Circuit, 5–4, and preserves offense-date annual consideration. The current chunk-5 Render Input and render carry that replacement. But each of the following slices still calls itself “Actual current-chunk law effective before” its date and describes itself as a verbatim reading copy of preserved Record public fields:

| File | Exact location of the stale result |
|---|---|
| [Before April 26](../entering-law/OT_1994CHUNK5_BEFORE_1995-04-26.md) | Morales section begins at line 169; reversed 5–4/no controlling rationale at line 177; superseded current-law effect at line 198 and mandate at line 210. |
| [Before April 27](../entering-law/OT_1994CHUNK5_BEFORE_1995-04-27.md) | Same locations and stale result. |
| [Before May 8](../entering-law/OT_1994CHUNK5_BEFORE_1995-05-08.md) | Same locations and stale result. |
| [Before May 15](../entering-law/OT_1994CHUNK5_BEFORE_1995-05-15.md) | Same locations and stale result. |

Those passages state that the Ninth Circuit's hearing-frequency judgment is reversed, the habeas relief must be vacated, and the amended schedule governs. Their linked authority now says the opposite. None of the four slices marks these passages superseded or identifies the file as a retired historical snapshot. This is a documentary mismatch, independently demonstrable without reevaluating the constitutional holding.

Two assembly copies also retain the old proposition in their purported completed check of actual April 25 law: [Lopez assembly copy](../runtime/assembly/United_States_v_Lopez_merits_1995-04-26.md), line 174, and [Travelers assembly copy](../runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md), line 219. Both begin “Morales reverses the particular ex post facto hearing-frequency relief without a single controlling constitutional rationale.” Their corresponding current canonical Records have been revised, but these copies have no opening supersession notice.

**Consequence:** The requested assurance that stale versions do not survive cannot be given. A later reader can follow an apparently current derived handoff into a superseded result. The slices are not authority, so this finding does not itself invalidate the present Morales judgment or decide whether a later adjudication must change. Correcting, retiring, or explicitly identifying these derivative copies belongs to the separate correction task.

**Boundary:** The Morales and Stone v. INS assembly drafts are already explicitly labeled superseded, with links to their current Records and the correction commits. Frozen pre-correction commitments and reconciliations are stage history that the Engine requires preserving; their mere retention is not an additional finding. Ignored `terms/OT1994/tmp/` snapshots are likewise not treated as live law. The problem above is the unqualified presentation of superseded material in the six identified derived files.

### F02 — Low — Rosenberger's final render entry lacks the required horizontal divider

[Chunk 8 output](../output/OT_1994CHUNK8.md) ends at line 948 with the bold Rosenberger closing line. No horizontal divider follows it. Render Contract §3 requires both the closing line and a following divider for **every** event, including the final event in a chunk.

The case heading and closing line exist, and this omission changes no vote, holding, or remedy. It is nevertheless a deterministic render-contract failure. All other 98 rendered Court-event entries have the required closing-line/divider boundary. No repair was made.

## 2. First checker and no-Git execution method

After reading the governing files, the first validation executed was the actual `tools/check_term.py` main routine for `OT1994`. The literal shell command `python tools/check_term.py OT1994` would violate this task's no-Git instruction because `git_object_exists()` invokes `git cat-file`. A scratch Python wrapper therefore loaded the unchanged checker, supplied the same `OT1994` arguments, and replaced **only** that function with direct read-only Git-object inspection. The wrapper invoked no Git executable. The checker itself and all repository tools were left unchanged.

The replacement reads loose objects and pack indexes, decompresses objects and deltas, verifies object SHA-1 identities, resolves abbreviated references, and checks that referenced objects are commits. It does not substitute an assumption of existence. The checker also executed its normal Holdings-volume synchronization and nine runtime split checks.

**Result:** exit 0, `OK: OT1994; 58 warning(s)`. The 58 warnings are false commit candidates from the checker's broad hexadecimal-token pattern: Archive identifiers, source-document identifiers, reporter/file fragments, an ISBN, a Technical Advice Memorandum number, and text such as the substring `cceeded`. Inspection of their actual occurrences found no missing claimed commit among them. They are not 58 provenance defects.

Scratch evidence: `tmp/ot1994_audit/check_term.txt`, `run_check.py`, and `git_readonly.py`. This adaptation is disclosed rather than represented as an unmodified command-line run.

## 3. Deterministic results and limits

| Check | Result and evidence |
|---|---|
| Inventory → manifest → Record → Render Input → render | **Pass for event coverage.** 99 inventory rows, 99 completed scheduled manifest entries, 99 unique Court-event Records, and 99 entries in nine Render Inputs and nine outputs. Chunks 1–8 each contain 12; chunk 9 contains 3. Every inventory caption, docket field, and event date reconciles with its manifest row and assigned Record. Consolidated companions count once. |
| Other Records and ledger coverage | **Pass for coverage.** 101 canonical files and 101 distinct ledger links: 99 Court events plus the March 10 Vaccine Table and April 4 Plant Variety Protection Act source admissions. The latter are not additional rendered Court decisions. No missing or duplicate canonical ledger link was found. |
| Effective-date order | **Pass for displayed dates and event placement; derivative-law freshness fails under F01.** The Court-event range is November 1, 1994–June 29, 1995. Each rendered event date matches its Record, and each chunk is in effective-date order. Pinette precedes Chabad in their expressly coordinated June 29 sequence. The manifest and continuity cursor are June 29. The ledger expressly uses file-preservation order, not purported verified Git commitment order; it supplies no same-day priority. Source admissions have their own effective dates. This check does not certify every legal use of entering authority, which belongs to the deferred substantive review. |
| Participation, vote and join arithmetic | **No arithmetic discrepancy detected in the mechanical checks.** 131 explicit supporting/opposing judgment rows were tallied, with narrative and combined-column formats separately inspected. NTEU's unanimous removal of senior-nonparty relief is not a 9–2 vote merely because its opposition cell explains Scalia and Thomas's different grounds. Evans's 6–1–2 disposition separates reversal, affirmance and dismissal. O'Neal's 7–2 vacatur, 5–4 remand instruction, three-Justice broader part and two-Justice concurrence remain distinct. Day's writing memberships do not add judgment votes; Nebraska's Fourth Cross-Claim is 8–1, distinct from the other 9–0 leave determinations. Named writers appearing in every source topology appear in their corresponding renders. Legal validity, scope and Justice-specific support of joins are **not** certified by these counts. |
| Runtime splits | **Pass for the prescribed normal split.** `split_chunk.py --check` passed for all nine approved briefs: all 27 normal `_NEUTRAL`, `_STONE`, and `_COMPARATOR` files match their source sections. The test does not validate every supplemental or assembly file; F01 identifies older derived copies it does not catch. Frozen handoff preservation is not permission to use superseded law as current law. |
| Public Projection → Render Input identity | **Pass.** All 99 generated Court-event source-record blocks reproduce their current Records' bounded Public Projections, using the repository checker's newline/outer-whitespace convention. Each Record has the required interface labels and eleven Public Projection blocks. |
| Render transmission | **Coverage and explanation comparison checked; boundary fails under F02.** All 236 supplied controlling explanations were compared against the corresponding rendered entries. 233 match after formatting/typographic normalization. The other three are limited wording changes: Anderson v. Edwards points to qualifications “set out below”; Celotex omits “supplied” before “connections”; Sweet Home expands “scienter” into “required knowledge or intent.” These comparisons do not adjudicate whether the underlying rules or qualifications are legally sufficient. |
| Local links and anchors | **Pass for live local/repository navigation under the staged-publication convention.** 13,836 local or repository-link occurrences were scanned, including ignored scratch copies. Live links and anchors resolve. The 185 currently unpublished Holdings-anchor occurrences in the Standards candidate resolve in the completed Holdings candidate; its pass notes expressly identify those as prospective `state/HOLDINGS.md` publication targets. Broken relative links inside ignored old scratch snapshots were excluded from live-navigation findings. |
| External links | **Incomplete reachability verification, not a confirmed broken-link finding.** Of 522 distinct external source URLs tested with a browser User-Agent, 445 returned HTTP 200; 47 returned 403, 3 returned 429, 6 returned 502, and 21 were unverified because of connection/TLS/timeout errors. None returned 404 or 410. Access denial and transient errors do not establish that a citation is nonexistent. HTTP success likewise does not validate the source's legal content or pinpoint. Appendix B identifies all 77 inconclusive URLs. |
| Commit existence and concise lineage | **Pass for actual cited commit references.** All three distinct claimed commit identifiers resolve to verified commit objects. The two correction claims were checked against the relevant parent/current tree blobs, as detailed below. No commit archaeology or Git command was used. |
| Candidate cleanup and synchronization | **Pass for this pre-Commit stage.** There is one canonical `AUDIT.md`, three candidates, two Holdings pass notes, one Standards pass note, and `.gitkeep`. No Term-Close Dossier or completed close is claimed. Candidates and temporary pass notes are retained until successful Commit, as required. All three candidate common headers match exactly: OT1993, the June 30, 1994 opening cutoff, edition September 28, 2026. The pass notes expressly stage advancement of those headers for coordinated publication. Their retained baseline header is not mistaken for substantive OT1994 coverage. |
| Open matters and carry-forward | **Pass for documentary coverage.** The seven unscheduled inherited matters, the inherited Nebraska original action, and Kansas's remedy continuation appear in the next-term candidate: nine carried matters. Completion of the two exceptions events is not treated as termination of their original proceedings. Standing State additionally lists the ten user-added OT1995 matters. No new historical closure or terminal order was inferred. Substantive correctness of every retained stage and user-added source claim remains for the legal audit. |

The candidate scope accounted for is Holdings pass 1, chunks 1–5 (60 matters, 154 listed propositions), and Holdings pass 2, chunks 6–9 (39 matters, 82 listed propositions), plus the complete Standards and Tests and Standing State candidates. Those files were included in structural, navigation, synchronization, scope, and carry-forward checks. **Their controlling-law selection, independent derivation, qualifications, precedent treatment, and remedies have not been substantively reaudited in this pass.**

The nine continued matters are Zatko and its companions; Wyoming v. Oklahoma; Reynolds; Grubbs; United States v. Louisiana; Delaware v. New York; Nebraska v. Wyoming; In re Anderson; and Kansas v. Colorado. Nebraska and Kansas each have a completed OT1994 exceptions event and a continuing original proceeding. The manifest's seven additional unscheduled carryovers therefore do not conflict with the candidate's nine carried matters.

## 4. Six specifically requested correction/completion checks

All six have exactly one current canonical Record and one current generated event block in the appropriate Render Input and render. Their current projected results, named coalitions and supplied controlling explanations were checked for transmission; this is not a fresh endorsement of their legal merits.

| Matter | Current documentary result |
|---|---|
| Transcon Lines, chunk 1 | The current triplet supplies 9–0 reversal and a confined implementation injunction for the admitted-unlawful loss-of-discount class, preserving genuine questions beyond the concessions and excluding ordinary freight principal and other estate receivables. The lineage describes completion of preassembly revalidation, not correction of an earlier completed adjudication. |
| Fargo, chunk 2 | The current triplet preserves the 6–3 access vacatur/remand and separate 8–1 definition-vagueness/associated limited penalty affirmances; Stone votes to vacate/remand throughout. The lineage describes completion of a previously unadjudicated matter. Earlier incomplete frozen work is not a competing decision. |
| O'Neal, chunk 3 | The current triplet preserves 7–2 vacatur, the five-Justice Chapman instruction for the preserved personal-intent category, and only three votes for the broader extension. Conditional relief is not an immediate writ. The lineage describes replacement of the approved Stone input and completion of a stopped intake, not supersession of a completed decision. |
| Robertson, chunk 5 | The current triplet supplies 9–0 reversal of the commerce-based Count Six reversal and remand for remaining appellate proceedings. It does not unconditionally reinstate the conviction or sentence. Prior inconclusive research is retained as research history; the current Record describes completion of the stopped matter. |
| Morales, chunk 5 | The current triplet supplies 5–4 affirmance, annual consideration rather than release, an O'Connor Court opinion joined by Stone, Stevens, Souter and Ginsburg, and Kennedy's dissent joined by Scalia, Thomas and Breyer. The current triplet is consistent on these transmitted terms. **F01 prevents the broader requested stale-version clearance.** |
| Stone v. INS, chunk 5 | The current triplet preserves 5–4 affirmance of original-order timeliness dismissal, with Stevens, Scalia, Kennedy, Thomas and Ginsburg in the majority. Stevens assigns Kennedy because the Chief dissents. The corrected internal assignment paragraph describes Stevens's ordinary assignment discretion, not the Chief-only fit/expansion method. Assignment metadata does not enter the public triplet. |

Direct Git-object inspection verifies:

- `d086219b424d812aaa837fda9533629c69e33833` contains the Morales replacement from reversal/no controlling rationale to affirmance with the present Court opinion. After normalizing line endings, its Record differs from the current Record only in the later concise lineage line. Its Public Projection matches the current one.
- `8d98261d33b6d39fda8a9ccc52ab5ad7ed3be02a` changes Stone v. INS's assignment paragraph. Comparing that commit with its parent confirms the Public Projection was unchanged by the correction. Its Record differs from the current Record only in the later concise lineage line after line-ending normalization.
- `13b19ee463d16fb4377d846e5b058599f886bed3`, used for the prior-term Standing State source, resolves to a commit and the linked historical file/anchor resolves there.

The assembly drafts for Morales and Stone v. INS have explicit superseded-history notices naming the appropriate commits and current Record. These notices are not stale operative versions. This audit does not demand erasure of Git history or immutable stage evidence. It does identify the unmarked current-law copies in F01.

## 5. Deferred legal review and disposition

The fresh legal audit must still examine **all 99 matters and all three candidates**, including both Holdings passes, for votes, coalitions, controlling holdings and alternatives, precedent treatment, remedies, continuity, Stone compatibility, and Justice-specific historical departures. The deterministic work is not a substitute for that review. No fresh substantive sub-agent was started after the gate failed.

The previous audit report was preserved in ignored scratch as `tmp/ot1994_audit/prior_AUDIT.md` before this canonical report was replaced. Its prior findings are not silently certified corrected by the new, narrower failed-gate report. Their correction evidence must be tested during the later substantive audit. This report's count of two findings is a count of **confirmed discrepancies in this pass**, not a claim that only two defects exist in the term's law.

Corrections remain for a separately authorized task. After the gate defects are addressed, rerun deterministic validation and conduct the fresh substantive review. This pass neither fixes a finding nor clears publication.

## Appendix A. Coverage of every inventory matter

Each row below was included in the inventory/manifest/Record/Render Input/render mapping and projection checks. “Mapped” certifies those documentary checks only. The substantive legal audit is **deferred for every row**. Rosenberger also has F02; Morales has F01 in derivative copies.

| No. | Chunk | Matter | Documentary coverage |
|---:|---:|---|---|
| 1 | 1 | United States v. Shabani | Mapped |
| 2 | 1 | U.S. Bancorp Mortgage Co. v. Bonner Mall Partnership | Mapped |
| 3 | 1 | Hess v. Port Authority Trans-Hudson Corp. | Mapped |
| 4 | 1 | United States v. X-Citement Video, Inc. | Mapped |
| 5 | 1 | Church of Scientology Flag Service Organization, Inc. v. City of Clearwater + | Mapped |
| 6 | 1 | Federal Election Commission v. NRA Political Victory Fund | Mapped |
| 7 | 1 | Reich v. Collins | Mapped |
| 8 | 1 | Brown v. Gardner | Mapped |
| 9 | 1 | Nebraska Department of Revenue v. Loewenstein | Mapped |
| 10 | 1 | In re Baby K + | Mapped |
| 11 | 1 | Plakas v. Drinski + | Mapped |
| 12 | 1 | Interstate Commerce Commission v. Transcon Lines | Mapped |
| 13 | 2 | Tome v. United States | Mapped |
| 14 | 2 | Young v. Northern Illinois Conference of United Methodist Church + | Mapped |
| 15 | 2 | Asgrow Seed Co. v. Winterboer | Mapped |
| 16 | 2 | United States v. Mezzanatto | Mapped |
| 17 | 2 | American Airlines, Inc. v. Wolens | Mapped |
| 18 | 2 | NationsBank of North Carolina, N.A. v. Variable Annuity Life Insurance Co. / Ludwig v. Variable Annuity Life Insurance Co. | Mapped |
| 19 | 2 | Allied-Bruce Terminix Cos. v. Dobson | Mapped |
| 20 | 2 | Schlup v. Delo | Mapped |
| 21 | 2 | McKennon v. Nashville Banner Publishing Co. | Mapped |
| 22 | 2 | Fargo Women’s Health Organization v. Schafer + | Mapped |
| 23 | 2 | Lebron v. National Railroad Passenger Corp. | Mapped |
| 24 | 2 | Milwaukee Brewery Workers' Pension Plan v. Jos. Schlitz Brewing Co. | Mapped |
| 25 | 3 | O'Neal v. McAninch | Mapped |
| 26 | 3 | United States v. National Treasury Employees Union | Mapped |
| 27 | 3 | Harris v. Alabama | Mapped |
| 28 | 3 | Jerome B. Grubart, Inc. v. Great Lakes Dredge & Dock Co. / City of Chicago v. Great Lakes Dredge & Dock Co. | Mapped |
| 29 | 3 | Anderson v. Green | Mapped |
| 30 | 3 | Gustafson v. Alloyd Co. | Mapped |
| 31 | 3 | Arizona v. Evans | Mapped |
| 32 | 3 | Swint v. Chambers County Commission | Mapped |
| 33 | 3 | Mastrobuono v. Shearson Lehman Hutton, Inc. | Mapped |
| 34 | 3 | Curtiss-Wright Corp. v. Schoonejongen | Mapped |
| 35 | 3 | Shalala v. Guernsey Memorial Hospital | Mapped |
| 36 | 3 | Ambassador Books & Video, Inc. v. City of Little Rock + | Mapped |
| 37 | 4 | Director, Office of Workers’ Compensation Programs v. Newport News Shipbuilding & Dry Dock Co. | Mapped |
| 38 | 4 | Anderson v. Edwards | Mapped |
| 39 | 4 | Swanner v. Anchorage Equal Rights Commission + | Mapped |
| 40 | 4 | Qualitex Co. v. Jacobson Products Co. | Mapped |
| 41 | 4 | Oklahoma Tax Commission v. Jefferson Lines, Inc. | Mapped |
| 42 | 4 | Plaut v. Spendthrift Farm, Inc. | Mapped |
| 43 | 4 | Shalala v. Whitecotton | Mapped |
| 44 | 4 | Freightliner Corp. v. Myrick | Mapped |
| 45 | 4 | Heintz v. Jenkins | Mapped |
| 46 | 4 | Lanphere & Urbaniak v. Colorado + | Mapped |
| 47 | 4 | Celotex Corp. v. Edwards | Mapped |
| 48 | 4 | McIntyre v. Ohio Elections Commission | Mapped |
| 49 | 5 | Stone v. Immigration and Naturalization Service | Mapped |
| 50 | 5 | Kyles v. Whitley | Mapped |
| 51 | 5 | Rubin v. Coors Brewing Co. | Mapped |
| 52 | 5 | California Department of Corrections v. Morales | Mapped; F01 in derivative copies |
| 53 | 5 | United States v. Williams | Mapped |
| 54 | 5 | United States v. Lopez | Mapped |
| 55 | 5 | New York State Conference of Blue Cross & Blue Shield Plans v. Travelers Insurance Co. / Pataki v. Travelers Insurance Co. / Hospital Association of New York State v. Travelers Insurance Co. | Mapped |
| 56 | 5 | United States v. Harris + | Mapped |
| 57 | 5 | United States v. Robertson | Mapped |
| 58 | 5 | United States v. Pinson + | Mapped |
| 59 | 5 | Kansas v. Colorado | Mapped |
| 60 | 5 | Hubbard v. United States | Mapped |
| 61 | 6 | City of Edmonds v. Oxford House, Inc. | Mapped |
| 62 | 6 | Reynoldsville Casket Co. v. Hyde | Mapped |
| 63 | 6 | Day v. Holahan + | Mapped |
| 64 | 6 | U.S. Term Limits, Inc. v. Thornton / Bryant v. Hill | Mapped |
| 65 | 6 | Wilson v. Arkansas | Mapped |
| 66 | 6 | First Options of Chicago, Inc. v. Kaplan | Mapped |
| 67 | 6 | Kelley v. Board of Trustees of the University of Illinois + | Mapped |
| 68 | 6 | Nebraska v. Wyoming | Mapped |
| 69 | 6 | North Star Steel Co. v. Thomas / Crown Cork & Seal Co., Inc. v. United Steelworkers of America, AFL-CIO-CLC | Mapped |
| 70 | 6 | Garlotte v. Fordice | Mapped |
| 71 | 6 | United States v. Wellons + | Mapped |
| 72 | 6 | Reno v. Koray | Mapped |
| 73 | 7 | Metropolitan Washington Airports Authority v. Hechinger + | Mapped |
| 74 | 7 | Missouri v. Jenkins | Mapped |
| 75 | 7 | Ryder v. United States | Mapped |
| 76 | 7 | City of Milwaukee v. Cement Division, National Gypsum Co. | Mapped |
| 77 | 7 | Adarand Constructors, Inc. v. Peña | Mapped |
| 78 | 7 | Wilton v. Seven Falls Co. | Mapped |
| 79 | 7 | Metropolitan Stevedore Co. v. Rambo | Mapped |
| 80 | 7 | Johnson v. Jones | Mapped |
| 81 | 7 | Kimberlin v. Quinlan | Mapped |
| 82 | 7 | Commissioner v. Schleier | Mapped |
| 83 | 7 | Chandris, Inc. v. Latsis | Mapped |
| 84 | 7 | Witte v. United States | Mapped |
| 85 | 8 | Gutierrez de Martinez v. Lamagno | Mapped |
| 86 | 8 | Oklahoma Tax Commission v. Chickasaw Nation | Mapped |
| 87 | 8 | Sandin v. Conner | Mapped |
| 88 | 8 | United States v. Gaudin | Mapped |
| 89 | 8 | Vimar Seguros y Reaseguros, S.A. v. M/V Sky Reefer | Mapped |
| 90 | 8 | Hurley v. Irish-American Gay, Lesbian and Bisexual Group of Boston | Mapped |
| 91 | 8 | National Private Truck Council, Inc. v. Oklahoma Tax Commission | Mapped |
| 92 | 8 | United States v. Aguilar | Mapped |
| 93 | 8 | Florida Bar v. Went For It, Inc. | Mapped |
| 94 | 8 | Vernonia School District 47J v. Acton | Mapped |
| 95 | 8 | Rosenberger v. Rector and Visitors of the University of Virginia | Mapped; F02 render boundary |
| 96 | 8 | Babbitt v. Sweet Home Chapter of Communities for a Great Oregon | Mapped |
| 97 | 9 | Miller v. Johnson / Abrams v. Johnson / United States v. Johnson | Mapped |
| 98 | 9 | Capitol Square Review and Advisory Board v. Pinette | Mapped |
| 99 | 9 | Chabad-Lubavitch of Georgia v. Miller + | Mapped |

## Appendix B. External URLs whose reachability remains unverified

These are verification limitations, not findings that the sources are absent or legally incorrect. The status is the response to this pass's HEAD request; access-denied and transient failures were not converted into missing-source claims. Full occurrences and connection errors are retained in `tmp/ot1994_audit/url_results.json`. Each row identifies one affected file and line; repeated uses of the same URL do not create additional findings.

| Status | URL | First occurrence |
|---|---|---|
| 403 | [https://law.justia.com/cases/california/supreme-court/3d/39/464.html](https://law.justia.com/cases/california/supreme-court/3d/39/464.html) | `terms/OT1994/briefs/OT_1994CHUNK5.md`, line 566 (3 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F2/982/486/137058/](https://law.justia.com/cases/federal/appellate-courts/F2/982/486/137058/) | `terms/OT1994/briefs/OT_1994CHUNK2.md`, line 415 (2 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/12/154/528248/](https://law.justia.com/cases/federal/appellate-courts/F3/12/154/528248/) | `terms/OT1994/briefs/OT_1994CHUNK4.md`, line 528 (3 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/13/934/631993/](https://law.justia.com/cases/federal/appellate-courts/F3/13/934/631993/) | `terms/OT1994/briefs/OT_1994CHUNK5.md`, line 193 (4 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/16/1537/492197/](https://law.justia.com/cases/federal/appellate-courts/F3/16/1537/492197/) | `terms/OT1994/briefs/OT_1994CHUNK7.md`, line 693 (2 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/17/374/567311/](https://law.justia.com/cases/federal/appellate-courts/F3/17/374/567311/) | `terms/OT1994/briefs/OT_1994CHUNK4.md`, line 1231 (3 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/18/1034/531004/](https://law.justia.com/cases/federal/appellate-courts/F3/18/1034/531004/) | `terms/OT1994/briefs/OT_1994CHUNK3.md`, line 1427 (3 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/2/899/616218/](https://law.justia.com/cases/federal/appellate-courts/F3/2/899/616218/) | `terms/OT1994/briefs/OT_1994CHUNK1.md`, line 286 (4 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/20/45/523011/](https://law.justia.com/cases/federal/appellate-courts/F3/20/45/523011/) | `terms/OT1994/briefs/OT_1994CHUNK7.md`, line 2139 (2 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/21/558/622869/](https://law.justia.com/cases/federal/appellate-courts/F3/21/558/622869/) | `terms/OT1994/briefs/OT_1994CHUNK6.md`, line 1943 (3 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/25/250/572049/](https://law.justia.com/cases/federal/appellate-courts/F3/25/250/572049/) | `terms/OT1994/briefs/OT_1994CHUNK7.md`, line 2487 (2 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/26/95/619021/](https://law.justia.com/cases/federal/appellate-courts/F3/26/95/619021/) | `terms/OT1994/briefs/OT_1994CHUNK3.md`, line 749 (3 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/28/86/581336/](https://law.justia.com/cases/federal/appellate-courts/F3/28/86/581336/) | `terms/OT1994/briefs/OT_1994CHUNK7.md`, line 1275 (2 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/29/727/480225/](https://law.justia.com/cases/federal/appellate-courts/F3/29/727/480225/) | `terms/OT1994/briefs/OT_1994CHUNK8.md`, line 584 (4 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/3/225/539495/](https://law.justia.com/cases/federal/appellate-courts/F3/3/225/539495/) | `terms/OT1994/briefs/OT_1994CHUNK3.md`, line 450 (3 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/31/581/592042/](https://law.justia.com/cases/federal/appellate-courts/F3/31/581/592042/) | `terms/OT1994/briefs/OT_1994CHUNK7.md`, line 533 (2 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/32/53/633439/](https://law.justia.com/cases/federal/appellate-courts/F3/32/53/633439/) | `terms/OT1994/briefs/OT_1994CHUNK6.md`, line 1449 (3 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/34/1356/552077/](https://law.justia.com/cases/federal/appellate-courts/F3/34/1356/552077/) | `terms/OT1994/briefs/OT_1994CHUNK6.md`, line 252 (5 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/41/934/563873/](https://law.justia.com/cases/federal/appellate-courts/F3/41/934/563873/) | `terms/OT1994/briefs/OT_1994CHUNK7.md`, line 979 (2 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/6/789/576708/](https://law.justia.com/cases/federal/appellate-courts/F3/6/789/576708/) | `terms/OT1994/briefs/OT_1994CHUNK7.md`, line 1708 (2 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/8/175/614852/](https://law.justia.com/cases/federal/appellate-courts/F3/8/175/614852/) | `terms/OT1994/briefs/OT_1994CHUNK4.md`, line 193 (3 occurrences). |
| 403 | [https://law.justia.com/cases/federal/appellate-courts/F3/9/64/540228/](https://law.justia.com/cases/federal/appellate-courts/F3/9/64/540228/) | `terms/OT1994/briefs/OT_1994CHUNK1.md`, line 1430 (4 occurrences). |
| 403 | [https://law.justia.com/cases/oklahoma/supreme-court/1994/20198.html](https://law.justia.com/cases/oklahoma/supreme-court/1994/20198.html) | `terms/OT1994/briefs/OT_1994CHUNK8.md`, line 1030 (4 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/301/397/](https://supreme.justia.com/cases/federal/us/301/397/) | `terms/OT1994/briefs/OT_1994CHUNK5.md`, line 562 (3 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/450/24/](https://supreme.justia.com/cases/federal/us/450/24/) | `terms/OT1994/briefs/OT_1994CHUNK5.md`, line 560 (3 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/482/423/](https://supreme.justia.com/cases/federal/us/482/423/) | `terms/OT1994/briefs/OT_1994CHUNK5.md`, line 562 (3 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/497/37/](https://supreme.justia.com/cases/federal/us/497/37/) | `terms/OT1994/briefs/OT_1994CHUNK5.md`, line 564 (3 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/513/179/](https://supreme.justia.com/cases/federal/us/513/179/) | `terms/OT1994/briefs/OT_1994CHUNK2.md`, line 529 (2 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/513/18/](https://supreme.justia.com/cases/federal/us/513/18/) | `terms/OT1994/briefs/OT_1994CHUNK1.md`, line 386 (3 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/513/527/](https://supreme.justia.com/cases/federal/us/513/527/) | `terms/OT1994/briefs/OT_1994CHUNK3.md`, line 551 (4 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/513/557/](https://supreme.justia.com/cases/federal/us/513/557/) | `terms/OT1994/briefs/OT_1994CHUNK3.md`, line 850 (3 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/514/122/](https://supreme.justia.com/cases/federal/us/514/122/) | `terms/OT1994/briefs/OT_1994CHUNK4.md`, line 296 (3 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/514/143/](https://supreme.justia.com/cases/federal/us/514/143/) | `terms/OT1994/briefs/OT_1994CHUNK4.md`, line 638 (3 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/514/268/](https://supreme.justia.com/cases/federal/us/514/268/) | `terms/OT1994/briefs/OT_1994CHUNK4.md`, line 1342 (3 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/514/673/](https://supreme.justia.com/cases/federal/us/514/673/) | `terms/OT1994/briefs/OT_1994CHUNK5.md`, line 1738 (4 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/514/73/](https://supreme.justia.com/cases/federal/us/514/73/) | `terms/OT1994/briefs/OT_1994CHUNK3.md`, line 1537 (3 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/515/1/](https://supreme.justia.com/cases/federal/us/515/1/) | `terms/OT1994/briefs/OT_1994CHUNK6.md`, line 1255 (2 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/515/277/](https://supreme.justia.com/cases/federal/us/515/277/) | `terms/OT1994/briefs/OT_1994CHUNK7.md`, line 1077 (2 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/515/29/](https://supreme.justia.com/cases/federal/us/515/29/) | `terms/OT1994/briefs/OT_1994CHUNK6.md`, line 1553 (2 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/515/291/](https://supreme.justia.com/cases/federal/us/515/291/) | `terms/OT1994/briefs/OT_1994CHUNK7.md`, line 1376 (2 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/515/321/](https://supreme.justia.com/cases/federal/us/515/321/) | `terms/OT1994/briefs/OT_1994CHUNK7.md`, line 1821 (2 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/515/347/](https://supreme.justia.com/cases/federal/us/515/347/) | `terms/OT1994/briefs/OT_1994CHUNK7.md`, line 2252 (2 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/515/389/](https://supreme.justia.com/cases/federal/us/515/389/) | `terms/OT1994/briefs/OT_1994CHUNK7.md`, line 2604 (2 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/515/50/](https://supreme.justia.com/cases/federal/us/515/50/) | `terms/OT1994/briefs/OT_1994CHUNK6.md`, line 2042 (2 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/515/528/](https://supreme.justia.com/cases/federal/us/515/528/) | `terms/OT1994/briefs/OT_1994CHUNK8.md`, line 702 (3 occurrences). |
| 403 | [https://supreme.justia.com/cases/federal/us/515/582/](https://supreme.justia.com/cases/federal/us/515/582/) | `terms/OT1994/briefs/OT_1994CHUNK8.md`, line 1147 (3 occurrences). |
| 403 | [https://www.cambridge.org/core/books/abs/minority-representation-and-the-quest-for-voting-equality/right-to-vote-and-the-right-to-representation/5223F70CBD862DEEE5634BA1F102E638](https://www.cambridge.org/core/books/abs/minority-representation-and-the-quest-for-voting-equality/right-to-vote-and-the-right-to-representation/5223F70CBD862DEEE5634BA1F102E638) | `terms/OT1994/briefs/OT_1994CHUNK9.md`, line 221 (4 occurrences). |
| 429 | [https://app.midpage.ai/document/allied-bruce-terminix-v-dobson-1662045](https://app.midpage.ai/document/allied-bruce-terminix-v-dobson-1662045) | `terms/OT1994/entering-law/OT_1994CHUNK2_FARGO_EARLIER_PUBLIC.md`, line 1385 (11 occurrences). |
| 429 | [https://app.midpage.ai/document/william-m-kelley-joseph-s-677868](https://app.midpage.ai/document/william-m-kelley-joseph-s-677868) | `terms/OT1994/output/OT_1994CHUNK6.md`, line 378 (4 occurrences). |
| 429 | [https://app.midpage.ai/document/wolens-v-american-airlines-inc-2035579](https://app.midpage.ai/document/wolens-v-american-airlines-inc-2035579) | `terms/OT1994/entering-law/OT_1994CHUNK2_FARGO_EARLIER_PUBLIC.md`, line 1470 (11 occurrences). |
| 502 | [https://openjurist.org/11/f3d/755](https://openjurist.org/11/f3d/755) | `terms/OT1994/output/OT_1994CHUNK7.md`, line 442 (4 occurrences). |
| 502 | [https://openjurist.org/13/f3d/1170](https://openjurist.org/13/f3d/1170) | `terms/OT1994/output/OT_1994CHUNK7.md`, line 442 (4 occurrences). |
| 502 | [https://openjurist.org/29/f3d/727](https://openjurist.org/29/f3d/727) | `terms/OT1994/freeze/OT_1994CHUNK8_COMMITMENTS.md`, line 192 (4 occurrences). |
| 502 | [https://openjurist.org/31/f3d/581](https://openjurist.org/31/f3d/581) | `terms/OT1994/output/OT_1994CHUNK7.md`, line 207 (4 occurrences). |
| 502 | [https://openjurist.org/35/f3d/265/kelley-v-board-of-trustees-w-e](https://openjurist.org/35/f3d/265/kelley-v-board-of-trustees-w-e) | `terms/OT1994/output/OT_1994CHUNK6.md`, line 378 (4 occurrences). |
| 502 | [https://openjurist.org/36/f3d/97](https://openjurist.org/36/f3d/97) | `terms/OT1994/output/OT_1994CHUNK7.md`, line 84 (4 occurrences). |
| unverified | [https://archive.org/details/micro_IA40386012_1825](https://archive.org/details/micro_IA40386012_1825) | `terms/OT1994/close/STANDING_STATE.candidate.md`, line 72 (1 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?edition=1994&num=0&req=granuleid%3AUSC-1994-title28-section2244](https://uscode.house.gov/view.xhtml?edition=1994&num=0&req=granuleid%3AUSC-1994-title28-section2244) | `terms/OT1994/entering-law/OT_1994CHUNK2_FARGO_EARLIER_PUBLIC.md`, line 1913 (16 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-1994-title28-section151&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-1994-title28-section151&num=0&edition=1994) | `terms/OT1994/freeze/OT_1994CHUNK5_COMMITMENTS_PH_SOURCE_REFRESH.md`, line 35 (10 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-1994-title28-section2106&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-1994-title28-section2106&num=0&edition=1994) | `terms/OT1994/freeze/OT_1994CHUNK5_COMMITMENTS.md`, line 505 (16 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-1994-title7-section2567&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-1994-title7-section2567&num=0&edition=1994) | `terms/OT1994/entering-law/OT_1994CHUNK2_FARGO_EARLIER_PUBLIC.md`, line 1570 (9 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title26-section9010&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title26-section9010&num=0&edition=1994) | `terms/OT1994/freeze/OT_1994CHUNK1_NEUTRAL_FEC.md`, line 143 (1 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title26-section9040&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title26-section9040&num=0&edition=1994) | `terms/OT1994/freeze/OT_1994CHUNK1_NEUTRAL_FEC.md`, line 143 (1 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title28-section2101&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title28-section2101&num=0&edition=1994) | `terms/OT1994/entering-law/OT_1994CHUNK2_FARGO_EARLIER_PUBLIC.md`, line 569 (11 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title28-section2111&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title28-section2111&num=0&edition=1994) | `terms/OT1994/freeze/OT_1994CHUNK3_ONEAL_NEUTRAL_CANDIDATE.md`, line 129 (2 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title28-section2243&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title28-section2243&num=0&edition=1994) | `terms/OT1994/freeze/OT_1994CHUNK3_ONEAL_NEUTRAL_CANDIDATE.md`, line 129 (3 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title28-section2254&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title28-section2254&num=0&edition=1994) | `terms/OT1994/freeze/OT_1994CHUNK3_ONEAL_NEUTRAL_CANDIDATE.md`, line 129 (6 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title28-section518&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title28-section518&num=0&edition=1994) | `terms/OT1994/entering-law/OT_1994CHUNK2_FARGO_EARLIER_PUBLIC.md`, line 569 (11 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title29-section1399&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title29-section1399&num=0&edition=1994) | `terms/OT1994/entering-law/OT_1994CHUNK3_EFFECTIVE_BEFORE_1995-02-28.md`, line 2271 (11 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title29-section626&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title29-section626&num=0&edition=1994) | `terms/OT1994/entering-law/OT_1994CHUNK2_FARGO_EARLIER_PUBLIC.md`, line 1809 (13 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title30-section932&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title30-section932&num=0&edition=1994) | `terms/OT1994/entering-law/OT_1994CHUNK5_KANSAS_SUPPLEMENT.md`, line 345 (1 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title33-section907&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title33-section907&num=0&edition=1994) | `terms/OT1994/entering-law/OT_1994CHUNK5_KANSAS_SUPPLEMENT.md`, line 345 (1 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title33-section919&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title33-section919&num=0&edition=1994) | `terms/OT1994/entering-law/OT_1994CHUNK5_KANSAS_SUPPLEMENT.md`, line 345 (1 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title33-section923&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title33-section923&num=0&edition=1994) | `terms/OT1994/entering-law/OT_1994CHUNK5_KANSAS_SUPPLEMENT.md`, line 345 (1 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title49-section24301&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title49-section24301&num=0&edition=1994) | `terms/OT1994/entering-law/OT_1994CHUNK3_EFFECTIVE_BEFORE_1995-02-28.md`, line 2211 (11 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title49-section24302&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title49-section24302&num=0&edition=1994) | `terms/OT1994/entering-law/OT_1994CHUNK3_EFFECTIVE_BEFORE_1995-02-28.md`, line 2211 (11 occurrences). |
| unverified | [https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title5-section556&num=0&edition=1994](https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title5-section556&num=0&edition=1994) | `terms/OT1994/entering-law/OT_1994CHUNK5_KANSAS_SUPPLEMENT.md`, line 345 (1 occurrences). |

**Operator summary: FAIL.** Deterministic defects remain; the fresh substantive audit was not reached.  
**Findings by severity:** critical 0; high 0; medium 1; low 1 — total 2. External reachability is additionally incomplete for 77 URLs.
