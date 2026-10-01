# October Term 1994 — Close Audit

**Result: FAIL — deterministic prerequisites are not satisfied. Fresh legal review has not begun.**

**Confirmed findings: Critical 0; High 0; Medium 0; Low 3. Total 3.**

Audit date: October 1, 2026. This report replaces the prior audit and records the current files inspected. It does not authorize term-close publication or correct any artifact.

The requested sequence controls this pass: complete and pass the deterministic checks before starting a fresh AI review of legal substance. The current ledger omits the latest lineage of twelve corrected Records. Additional clerical defects and a checker false positive are documented below. Because the deterministic gate failed, **none of the 99 matters, either Holdings pass, or the Standards and Tests and Standing State candidates receives a fresh legal-substance clearance in this report**. The prior audit's legal conclusions have not been adopted as a substitute. The severity totals describe confirmed findings, not a certification that the unperformed legal review would find nothing further.

## 1. Sequence, scope and method

The governing instructions and foundation files were read before validation. The first validation command was `python tools/check_term.py OT1994`. It exited **1**, reporting one candidate-cleanup error and **58 warnings**. The cleanup error is the reproducible false positive described in F03. The warning detector matched source identifiers, numbers, citations and ordinary words rather than missing claimed commits; actual commit claims were checked separately. A second, unchanged-input run preserved the same result in the scratch evidence directory.

No Git command was run, including indirectly by the checker. Its exact `git ... cat-file -e ...^{commit}` subprocess was intercepted by an audit-only Python adapter under root `tmp/`. The adapter read loose or packed objects directly, reconstructed deltas when needed, verified SHA-1 object identities and tested for commit objects. It rejected other Git invocations. The requested checker and its ordinary read-only subchecks otherwise ran normally. No repository tool was edited.

The remaining deterministic review covered the 99 inventory matters, 101 canonical Records including the two Admitted Source Records, nine generated Render Inputs, nine chunk renders, runtime freshness, four workspace projections, both Holdings pass notes and the complete Holdings candidate, Standards and Tests candidate/pass note, and Standing State candidate. Repository link checking covered 824 current Markdown files under the term, excluding the prior audit and scratch/source directories. Published opening trackers and the composition register supplied the relevant baseline checks.

The prior audit was read to diagnose the initial checker failure and identify its reported repairs for current-file verification. No fresh substantive reviewer was started after the gate failed. Vote counting and textual comparison below establish clerical consistency only; they do not establish the legal validity of a coalition, departure, holding, remedy or source interpretation.

Scratch evidence is under `tmp/ot1994_audit_oct1_run/`; the no-Git checker adapter is under `tmp/ot1994_audit/`. Only this `AUDIT.md` was written outside root `tmp/`. No Record, brief, freeze, Render Input, render, projection, candidate, foundation file or published tracker was changed.

## 2. Unresolved findings

### F01 — Low — The current ledger omits twelve Records' latest correction lineage

**Location:** [workspace/ledger.md](../workspace/ledger.md), the rows listed below, compared with each Record's fourth opening line, `Version / lineage`.

All 101 ledger rows were compared field by field with their current Records. Case identity, event text, effective date and result agree. Twelve lineage cells stop before their Record's October 1 correction. These are stale current projection fields, rather than superseded historical artifacts. They omit the current correction identification for the public-language repair, departure-label repairs, citation/spacing repairs and source-reading-completion receipts.

The ledger is a regenerated current index under Engine §§3G and 12. Its disclosure that Records control does not make stale cells current. The omission does not change a vote or holding, but it fails the requested deterministic Record-to-workspace reconciliation. The affected cells must be regenerated or corrected in a separate authorized task; this audit has not done so.

| Matter | Ledger line | Current Record's omitted correction |
|---|---:|---|
| [City of Edmonds v. Oxford House, Inc.](../records/City_of_Edmonds_v_Oxford_House_merits_1995-05-15.md) | 69 | October 1, 2026 audit correction (F01): Public Projection event wording removes internal law-loading language; prior text replaced in place. Judgment, votes, coalitions, holdings and remedy unchanged; operator verification and commitment remain pending. |
| [First Options of Chicago, Inc. v. Kaplan](../records/First_Options_of_Chicago_Inc_v_Kaplan_merits_1995-05-22.md) | 72 | October 1, 2026 audit correction (F03): audited citation symbols and missing spaces corrected; prior text replaced in place. Judgment, votes, coalitions, holdings and remedy unchanged; operator verification and commitment remain pending. |
| [Kelley v. Board of Trustees of the University of Illinois](../records/Kelley_v_Board_of_Trustees_of_the_University_of_Illinois_merits_1995-05-22.md) | 73 | October 1, 2026 audit correction (F03): audited citation symbols and missing spaces corrected; prior text replaced in place. Judgment, votes, coalitions, holdings and remedy unchanged; operator verification and commitment remain pending. |
| [Wilson v. Arkansas](../records/Wilson_v_Arkansas_merits_1995-05-22.md) | 75 | October 1, 2026 audit correction (F03): audited citation symbols and missing spaces corrected; prior text replaced in place. Judgment, votes, coalitions, holdings and remedy unchanged; operator verification and commitment remain pending. |
| [Nebraska v. Wyoming](../records/Nebraska_v_Wyoming_original_exceptions_1995-05-30.md) | 77 | October 1, 2026 audit correction (F03): audited citation symbols and missing spaces corrected; prior text replaced in place. Judgment, votes, coalitions, holdings and remedy unchanged; operator verification and commitment remain pending. |
| [Gutierrez de Martinez v. Lamagno](../records/Gutierrez_de_Martinez_v_Lamagno_merits_1995-06-14.md) | 93 | October 1, 2026 audit correction (F02): existing Historical departure label moved to its own line without changing departure text; prior text replaced in place. Judgment, votes, coalitions, holdings and remedy unchanged; operator verification and commitment remain pending. |
| [National Private Truck Council, Inc. v. Oklahoma Tax Commission](../records/National_Private_Truck_Council_Inc_v_Oklahoma_Tax_Commission_merits_1995-06-19.md) | 96 | October 1, 2026 audit correction (F03): audited citation symbols and missing spaces corrected; prior text replaced in place. Judgment, votes, coalitions, holdings and remedy unchanged; operator verification and commitment remain pending. |
| [Vimar Seguros y Reaseguros, S.A. v. M/V Sky Reefer](../records/Vimar_Seguros_y_Reaseguros_SA_v_MV_Sky_Reefer_merits_1995-06-19.md) | 99 | October 1, 2026 audit correction (F02): existing Historical departure label moved to its own line without changing departure text; prior text replaced in place. Judgment, votes, coalitions, holdings and remedy unchanged; operator verification and commitment remain pending. |
| [Florida Bar v. Went For It, Inc.](../records/Florida_Bar_v_Went_For_It_Inc_merits_1995-06-21.md) | 100 | October 1, 2026 audit correction (F03): audited citation symbols and missing spaces corrected; prior text replaced in place. Judgment, votes, coalitions, holdings and remedy unchanged; operator verification and commitment remain pending. |
| [United States v. Aguilar](../records/United_States_v_Aguilar_merits_1995-06-21.md) | 101 | October 1, 2026 audit correction (F03): audited citation symbols and missing spaces corrected; prior text replaced in place. Judgment, votes, coalitions, holdings and remedy unchanged; operator verification and commitment remain pending. |
| [Babbitt v. Sweet Home Chapter of Communities for a Great Oregon](../records/Babbitt_v_Sweet_Home_Chapter_of_Communities_for_a_Great_Oregon_merits_1995-06-29.md) | 103 | October 1, 2026 audit correction (F05): official-opinion reading completion recorded from the operator’s direct report; party-material reading limits retained; prior text replaced in place. Judgment, votes, coalitions, holdings and remedy unchanged; operator verification and commitment remain pending. |
| [Rosenberger v. Rector and Visitors of the University of Virginia](../records/Rosenberger_v_Rector_and_Visitors_of_the_University_of_Virginia_merits_1995-06-29.md) | 104 | October 1, 2026 audit correction (F03/F05): audited citation symbols and missing spaces corrected; official-opinion reading completion recorded from the operator’s direct report; prior text replaced in place. Judgment, votes, coalitions, holdings and remedy unchanged; operator verification and commitment remain pending. |

This is one repeated projection defect with twelve enumerated occurrences. The current Records themselves contain the correction notices. The same notices are absent from the ledger, not from the Records or their Git objects.

### F02 — Low — Fused words, dates and citation text remain in three current internal Records

These are literal file contents, not terminal encoding substitutions. All nine affected lines listed below are before `Public Projection`; this finding does not identify a changed public holding or vote. Immutable stage handoffs may preserve their original bytes, but incorporated text in the current canonical Record remains part of its audit trail.

| Current Record | Line | Verified residual text |
|---|---:|---|
| [Babbitt v. Sweet Home Chapter of Communities for a Great Oregon](../records/Babbitt_v_Sweet_Home_Chapter_of_Communities_for_a_Great_Oregon_merits_1995-06-29.md) | 116 | `no96` |
| [Florida Bar v. Went For It, Inc.](../records/Florida_Bar_v_Went_For_It_Inc_merits_1995-06-21.md) | 79 | `WentForIt`, `December14,1992`, `appellate21F3d1038` |
| [Florida Bar v. Went For It, Inc.](../records/Florida_Bar_v_Went_For_It_Inc_merits_1995-06-21.md) | 81 | `Rule4-7`, `THAN30days`, `challenged30day` |
| [Florida Bar v. Went For It, Inc.](../records/Florida_Bar_v_Went_For_It_Inc_merits_1995-06-21.md) | 89 | `the30day`, `categorical30day` |
| [Florida Bar v. Went For It, Inc.](../records/Florida_Bar_v_Went_For_It_Inc_merits_1995-06-21.md) | 95 | `lawyer30day` |
| [Florida Bar v. Went For It, Inc.](../records/Florida_Bar_v_Went_For_It_Inc_merits_1995-06-21.md) | 102 | `of30days` |
| [Florida Bar v. Went For It, Inc.](../records/Florida_Bar_v_Went_For_It_Inc_merits_1995-06-21.md) | 112 | `published515U.S.618` |
| [Florida Bar v. Went For It, Inc.](../records/Florida_Bar_v_Went_For_It_Inc_merits_1995-06-21.md) | 133 | `THAN30days`, `day30` |
| [Rosenberger v. Rector and Visitors of the University of Virginia](../records/Rosenberger_v_Rector_and_Visitors_of_the_University_of_Virginia_merits_1995-06-29.md) | 126 | `no95`, `before95` |

Florida Bar's examples include a fused reported citation and decision date, as well as repeated missing spaces around the thirty-day condition and rule identifiers. Sweet Home and Rosenberger retain fused prose around matter numbers in their source/isolation receipts. A later clerical correction should preserve the legal content and truthful lineage. No such correction was made here. This list states the occurrences verified in this pass; it does not claim a completed legal or stylistic review of every sentence.

### F03 — Low — The stock checker mistakes a sentence in a failed audit for a completed close

**Location:** [tools/check_term.py](../../../tools/check_term.py), lines 176–181, especially line 178.

The cleanup condition searches the entire audit for the two-word phrase `no unresolved`, without checking the audit result or whether the Commit pass occurred. Before this pass, the audit expressly reported FAIL and five outstanding findings. Its line 84 used that phrase only to describe repository link targets. The checker nevertheless emitted:

> completed close still contains candidate files: HOLDINGS.candidate.md, STANDARDS_AND_TESTS.candidate.md, STANDING_STATE.candidate.md

The three candidates and current pass notes are required staged artifacts before a successful Commit. No dossier or completed-close publication establishes that they should already have been deleted. Thus the error is a checker status-detection defect, not a reason to delete candidates. The same broad search can also match this report's explanation of the defect. A future tool correction must distinguish an actual completed close from arbitrary audit prose; changing the term's adjudications or deleting its staged candidates would not address the defect.

F03 is reported separately as an unresolved validation-tool defect. Even after rejecting its cleanup conclusion, F01 independently prevents the deterministic gate from passing.

## 3. Deterministic results

| Check | Current result and practical limit |
|---|---|
| Required first checker | Exit 1; one cleanup false positive (F03), 58 broad-token warnings. Other stock checks reported no error. This is not reported as a zero-error run. |
| Opening Holdings synchronization | The checker's `holdings_volumes.py check` subcheck passed. Opening doctrinal volumes and continuous view remain synchronized. |
| Inventory → manifest → Record → Render Input → render | 99 inventory matters map to 99 completed manifest entries, 99 Court-event Records, 99 generated public entries and 99 bounded render entries. Dockets, event dates and closing dates match. No missing or duplicate Court event. |
| Admitted sources | The March 10, 1995 Vaccine Injury Table and April 4, 1995 PVPA effectiveness Records bring the ledger total to 101. They are source events, not two missing public Court judgments. |
| Effective-date order | Inventory, manifest and generated entries agree on effective dates; each render follows its supplied event order. June 29 remains the cursor. Pinette precedes Chabad under the express sequence; other same-day peers are not mechanically resequenced as dependencies. Whether each decision actually used only eligible legal premises is reserved for the blocked substantive review. |
| Ledger | All 101 records are present once. Case, event and result fields agree; twelve lineage fields fail (F01). Its disclosed file-preservation-order fallback is not represented as verified first-commit order. |
| Participation and judgment arithmetic | Named judgment votes reconcile across all 99 matters, including prose dispositions and the special three-column tables in Kansas, Day, Nebraska and chunk 9. Reduced participation is retained in FEC, Wolens, Grubart, City of Milwaukee, Wilton and Sky Reefer. Evans's 6–1–2 disposition is three positions, not a faulty two-way tally. |
| Join arithmetic | The 256 tabular opinion-topology rows and prose topologies were inspected. Authors were counted once, named partial joins were counted at their specified scope, and concurrence membership was not added as another judgment vote. No numerical mismatch was confirmed. This is not a new Marks or compatibility determination. |
| Runtime freshness | All nine canonical neutral/comparator/Stone runtime splits pass the checker's comparison with the current approved briefs. Historical, superseded or stage-specific handoffs are not substituted for those current splits. |
| Public Projection → Render Input | All 99 bounded eleven-block projections match their generated source-record blocks after newline/end-of-block normalization. No public handoff drift was found. |
| Record holding text → render and candidate | All 236 explicit controlling-proposition strings appear in the corresponding kernels and renders after ordinary typography normalization. 235 also match the Holdings candidate literally after normalization; Clearwater's remaining difference is only removal of the navigational word “below” from “designated below as section”. This textual check does not certify all legal qualifications, explanations or candidate consolidation. |
| Workspace law and procedure copies | Every nonempty Holdings, Law After Decision and Procedure After Action block from all 101 Records is present in both continuity and neutral projections after typography/whitespace normalization. The former Robertson duplicate event blocks are absent: each projection has one Robertson law block and one procedure block. |
| Render structure | All 99 entries have the required heading, event/date line and matching closing line. 71 full-form and 28 compact-form entries are present; each full-form entry has judgment and opinion-topology tables. Substantive eligibility for the selected form is not newly adjudicated here. |
| Links and anchors | 12,259 repository link occurrences checked across 824 term Markdown files. No broken repository target or anchor remains after treating 188 candidate links to future published Holdings anchors against the complete staged candidate. Those links are publication destinations, not claims that OT1994 law is already in state/. External-site availability was not tested. |
| Commit existence | The three actual commit references found in the scanned material resolve to commit objects: the opening baseline, Morales replacement and Stone assignment correction. Source-document IDs, numeric citations, an ISBN, statutory-URL fragments and the substring of “succeeded” explain the stock warnings. The six priority matters' relevant preservation/correction commits and parent states were separately inspected as described below. |
| Current Record preservation | All 101 working-tree Records match their HEAD objects. Inspected HEAD: `ca658674280f530f388f1a7cafca9f4387cfc305`. This is read-only object evidence; it does not claim this new audit has been committed. |
| Candidate headers | All three candidates have matching Last completed October Term, Processed through and Edition fields: OT1993; June 30, 1994 after all 95 OT1993 events; September 28, 2026. Their own staged-close descriptions reserve advancement of those common fields for coordinated publication. |
| Candidate cleanup | close/ contains one audit, three current candidates, the two Holdings pass notes, one Standards pass note and .gitkeep. No extra candidate edition or published close dossier is present. Retention is proper before Commit; F03 must not trigger premature deletion. |
| Open-matter carry-forward | Standing State contains all 19 required docket lines: eight inherited open matters, Kansas's retained remedy proceeding and ten stated user-added OT1995 matters. Nebraska's completed exceptions event remains distinct from the retained original proceeding. No passed deadline alone closes Zatko, Reynolds or Grubbs. |

The standing roster, seniority and all thirteen circuit allotments match the Composition register's August 3, 1994 order at the OT1995 opening. The referral practice remains present. The candidate states the missing identification for A. St. P. C. v. B. C. and the missing reconstructed lower judgment for Bush v. Vera; this audit supplies neither.

The two Holdings notes account for 154 propositions from matters 1–60 and 82 from matters 61–99, matching the 236 extracted current proposition blocks. The complete candidate includes links to all 99 Court-event Records. The Standards candidate's structure and baseline comparison were checked: 370 rule headings, compared with 289 in the opening register, with 86 added headings, five removed headings, 34 changed surviving entries and 250 unchanged entries. Those counts locate the proposed work; they do not prove that the additions, removals or edits are legally warranted.

## 4. The six priority matters

The following findings concern current file identity, published counts, preservation and correction lineage. They do **not** replace the fresh legal examination of the complete current Record, every rendered qualification, or every Justice-specific departure that the failed gate prevents.

| Matter | Current deterministic reconciliation | Provenance and stale-version check |
|---|---|---|
| Interstate Commerce Commission v. Transcon Lines, matter 12 | One current Record and entry; generated projection identity passes; 9–0 reversal/remand and Kennedy authorship are consistent in the named fields. | `acec437d236d6d12e54bd53b191a233f57f52916` contains its first Record; the parent has none. Current Public Projection is unchanged from that committed completion. This supports the concise “no completed adjudication superseded” lineage. |
| Fargo Women's Health Organization v. Schafer, matter 22 | One current Record and entry; projection identity passes; access component 6–3 and the three limited affirmances 8–1 reconcile. | `f6afbf7f1a82d7ea26633bb04df475c3c4356f43` first preserves the Record; the parent has none. The current Public Projection differs only by the recorded repair of `injunction?s` to `injunction's`. Earlier incomplete freezes are stage history. |
| O'Neal v. McAninch, matter 25 | One current Record and entry; projection identity passes; 7–2 vacatur, five joins in the specified Chapman instruction and three in the broader proposal are counted separately. | `b3ce99c5c54607c27c5893c25cc52fc04efcca70` first preserves the Record; the parent has none. Current Public Projection is unchanged from that completion. This was resolution of stopped intake, not silent replacement of an adjudication. |
| United States v. Robertson, matter 57 | One current Record and entry; projection identity passes; 9–0 disposition and Breyer authorship agree. Each current workspace now has one law block and one procedure block. | `0fcb6a5c2d5485cf0591f852f4fbf859d4b1f3bf` first preserves the Record; the parent has none. Current Public Projection differs only by source-citation spacing. No duplicate current Robertson event remains. |
| California Department of Corrections v. Morales, matter 52 | One current replacement Record and entry; projection identity passes; the revised 5–4 affirmance is the current result, with O'Connor writing and Stone, Stevens, Souter and Ginsburg joining. | `d086219b424d812aaa837fda9533629c69e33833` and its parent verify replacement of the earlier 5–4 reversal. The current Public Projection matches that committed replacement. Old reversal bytes in history are not a second current decision. |
| Stone v. Immigration and Naturalization Service, matter 49 | One current Record and entry; projection identity passes; the five affirming Justices are Stevens, Scalia, Kennedy, Thomas and Ginsburg. The current assignment paragraph identifies Stevens assigning Kennedy while the Chief dissents. | At `8d98261d33b6d39fda8a9ccc52ab5ad7ed3be02a`, the parent/current diff changes only the assignment paragraph. Its Public Projection is identical across that correction and remains identical to the current projection. The claimed judgment/public-projection preservation is verified. |

The actual opening reference `13b19ee463d16fb4377d846e5b058599f886bed3` also resolves. This provenance work verifies concise claims and the relevant parent/current files; it is not narrative commit archaeology.

No second canonical Record or duplicate generated/rendered entry was found for any of these six matters. No stale current result was identified in the fields and copied blocks checked. A universal assertion that no stale substantive premise survives anywhere cannot be certified before the fresh legal review of active candidate rules, dependencies and handoffs. Immutable briefs, superseded freezes, earlier entering-law slices and Git history must not be erased merely because they retain superseded positions.

## 5. Previously reported repairs and limits of this pass

Current-file inspection confirms that Edmonds's Public Projection no longer contains the previously identified law-loading sentence; Gutierrez and Sky Reefer now put their Historical departure labels at the start of a line; and the Robertson workspace duplication has been removed. Those current changes account for some of the new lineage missing from the ledger.

The Rosenberger and Sweet Home Records now contain the operator's October 1 report of complete per-writing official-opinion readings, including footnotes, and state that the earlier partial-opinion-reading limitation is superseded. The current receipts separately retain their party-material and record limitations. This audit verifies the presence of the completion receipts, not the legal sufficiency of their conclusions or a new independent reading of those opinions. The fresh source, coalition and departure review remains pending. Residual internal typography is specifically reported in F02.

No external litigation source was newly retrieved in this deterministic pass. Existing reservations about argument dates, underlying trial materials, state-law constructions and future relief have not been filled by inference. No new chronology fact, vote, holding, remedy, historical departure or continuity closure is supplied.

## 6. Per-matter coverage of the completed deterministic phase

Every row below has a matching inventory/manifest event, current Record, generated Public Projection and bounded render entry, with matching dockets and event dates. Participation and named vote/join arithmetic were checked. **Fresh legal review is deferred for every row**, including legal support for the listed coalitions, precedent treatment, remedies, continuity and historical departures. The table is a coverage record, not a legal pass list.

| No. | Chunk | Matter and current Record | Effective date |
|---:|---:|---|---|
| 1 | 1 | [United States v. Shabani](../records/United_States_v_Shabani_merits_1994-11-01.md) | 1994-11-01 |
| 2 | 1 | [U.S. Bancorp Mortgage Co. v. Bonner Mall Partnership](../records/US_Bancorp_Mortgage_Co_v_Bonner_Mall_Partnership_mootness_vacatur_1994-11-08.md) | 1994-11-08 |
| 3 | 1 | [Hess v. Port Authority Trans-Hudson Corp.](../records/Hess_v_Port_Authority_Trans_Hudson_Corp_merits_1994-11-14.md) | 1994-11-14 |
| 4 | 1 | [United States v. X-Citement Video, Inc.](../records/United_States_v_X_Citement_Video_Inc_merits_1994-11-29.md) | 1994-11-29 |
| 5 | 1 | [Church of Scientology Flag Service Organization, Inc. v. City of Clearwater](../records/Church_of_Scientology_Flag_Service_Organization_Inc_v_City_of_Clearwater_merits_1994-12-05.md) | 1994-12-05 |
| 6 | 1 | [Federal Election Commission v. NRA Political Victory Fund](../records/Federal_Election_Commission_v_NRA_Political_Victory_Fund_jurisdictional_dismissal_1994-12-06.md) | 1994-12-06 |
| 7 | 1 | [Reich v. Collins](../records/Reich_v_Collins_merits_1994-12-06.md) | 1994-12-06 |
| 8 | 1 | [Brown v. Gardner](../records/Brown_v_Gardner_merits_1994-12-12.md) | 1994-12-12 |
| 9 | 1 | [Nebraska Department of Revenue v. Loewenstein](../records/Nebraska_Department_of_Revenue_v_Loewenstein_merits_1994-12-12.md) | 1994-12-12 |
| 10 | 1 | [In re Baby K](../records/In_re_Baby_K_merits_1994-12-12.md) | 1994-12-12 |
| 11 | 1 | [Plakas v. Drinski](../records/Plakas_v_Drinski_merits_1995-01-09.md) | 1995-01-09 |
| 12 | 1 | [Interstate Commerce Commission v. Transcon Lines](../records/Interstate_Commerce_Commission_v_Transcon_Lines_merits_1995-01-10.md) | 1995-01-10 |
| 13 | 2 | [Tome v. United States](../records/Tome_v_United_States_merits_1995-01-10.md) | 1995-01-10 |
| 14 | 2 | [Young v. Northern Illinois Conference of United Methodist Church](../records/Young_v_Northern_Illinois_Conference_merits_1995-01-17.md) | 1995-01-17 |
| 15 | 2 | [Asgrow Seed Co. v. Winterboer](../records/Asgrow_Seed_Co_v_Winterboer_merits_1995-01-18.md) | 1995-01-18 |
| 16 | 2 | [United States v. Mezzanatto](../records/United_States_v_Mezzanatto_merits_1995-01-18.md) | 1995-01-18 |
| 17 | 2 | [American Airlines, Inc. v. Wolens](../records/American_Airlines_Inc_v_Wolens_merits_1995-01-18.md) | 1995-01-18 |
| 18 | 2 | [NationsBank of North Carolina, N.A. v. Variable Annuity Life Insurance Co. / Ludwig v. Variable Annuity Life Insurance Co.](../records/NationsBank_Ludwig_v_Variable_Annuity_Life_Insurance_Co_merits_1995-01-18.md) | 1995-01-18 |
| 19 | 2 | [Allied-Bruce Terminix Cos. v. Dobson](../records/Allied_Bruce_Terminix_Cos_v_Dobson_merits_1995-01-18.md) | 1995-01-18 |
| 20 | 2 | [Schlup v. Delo](../records/Schlup_v_Delo_merits_1995-01-23.md) | 1995-01-23 |
| 21 | 2 | [McKennon v. Nashville Banner Publishing Co.](../records/McKennon_v_Nashville_Banner_Publishing_Co_merits_1995-01-23.md) | 1995-01-23 |
| 22 | 2 | [Fargo Women’s Health Organization v. Schafer](../records/Fargo_Womens_Health_Organization_v_Schafer_merits_1995-02-13.md) | 1995-02-13 |
| 23 | 2 | [Lebron v. National Railroad Passenger Corp.](../records/Lebron_v_National_Railroad_Passenger_Corp_merits_1995-02-21.md) | 1995-02-21 |
| 24 | 2 | [Milwaukee Brewery Workers' Pension Plan v. Jos. Schlitz Brewing Co.](../records/Milwaukee_Brewery_Workers_Pension_Plan_v_Jos_Schlitz_Brewing_Co_merits_1995-02-21.md) | 1995-02-21 |
| 25 | 3 | [O'Neal v. McAninch](../records/ONeal_v_McAninch_merits_1995-02-21.md) | 1995-02-21 |
| 26 | 3 | [United States v. National Treasury Employees Union](../records/United_States_v_National_Treasury_Employees_Union_merits_1995-02-22.md) | 1995-02-22 |
| 27 | 3 | [Harris v. Alabama](../records/Harris_v_Alabama_merits_1995-02-22.md) | 1995-02-22 |
| 28 | 3 | [Jerome B. Grubart, Inc. v. Great Lakes Dredge & Dock Co. / City of Chicago v. Great Lakes Dredge & Dock Co.](../records/Jerome_B_Grubart_Inc_v_Great_Lakes_Dredge_Dock_Co_merits_1995-02-22.md) | 1995-02-22 |
| 29 | 3 | [Anderson v. Green](../records/Anderson_v_Green_decision_1995-02-22.md) | 1995-02-22 |
| 30 | 3 | [Gustafson v. Alloyd Co.](../records/Gustafson_v_Alloyd_Co_merits_1995-02-28.md) | 1995-02-28 |
| 31 | 3 | [Arizona v. Evans](../records/Arizona_v_Evans_merits_1995-03-01.md) | 1995-03-01 |
| 32 | 3 | [Swint v. Chambers County Commission](../records/Swint_v_Chambers_County_Commission_merits_1995-03-01.md) | 1995-03-01 |
| 33 | 3 | [Mastrobuono v. Shearson Lehman Hutton, Inc.](../records/Mastrobuono_v_Shearson_Lehman_Hutton_Inc_merits_1995-03-06.md) | 1995-03-06 |
| 34 | 3 | [Curtiss-Wright Corp. v. Schoonejongen](../records/Curtiss_Wright_Corp_v_Schoonejongen_merits_1995-03-06.md) | 1995-03-06 |
| 35 | 3 | [Shalala v. Guernsey Memorial Hospital](../records/Shalala_v_Guernsey_Memorial_Hospital_merits_1995-03-06.md) | 1995-03-06 |
| 36 | 3 | [Ambassador Books & Video, Inc. v. City of Little Rock](../records/Ambassador_Books_Video_Inc_v_City_of_Little_Rock_merits_1995-03-20.md) | 1995-03-20 |
| 37 | 4 | [Director, Office of Workers’ Compensation Programs v. Newport News Shipbuilding & Dry Dock Co.](../records/Director_Office_of_Workers_Compensation_Programs_v_Newport_News_Shipbuilding_and_Dry_Dock_Co_merits_1995-03-21.md) | 1995-03-21 |
| 38 | 4 | [Anderson v. Edwards](../records/Anderson_v_Edwards_merits_1995-03-22.md) | 1995-03-22 |
| 39 | 4 | [Swanner v. Anchorage Equal Rights Commission](../records/Swanner_v_Anchorage_Equal_Rights_Commission_merits_1995-03-27.md) | 1995-03-27 |
| 40 | 4 | [Qualitex Co. v. Jacobson Products Co.](../records/Qualitex_Co_v_Jacobson_Products_Co_merits_1995-03-28.md) | 1995-03-28 |
| 41 | 4 | [Oklahoma Tax Commission v. Jefferson Lines, Inc.](../records/Oklahoma_Tax_Commission_v_Jefferson_Lines_Inc_merits_1995-04-03.md) | 1995-04-03 |
| 42 | 4 | [Plaut v. Spendthrift Farm, Inc.](../records/Plaut_v_Spendthrift_Farm_Inc_merits_1995-04-18.md) | 1995-04-18 |
| 43 | 4 | [Shalala v. Whitecotton](../records/Shalala_v_Whitecotton_merits_1995-04-18.md) | 1995-04-18 |
| 44 | 4 | [Freightliner Corp. v. Myrick](../records/Freightliner_Corp_v_Myrick_merits_1995-04-18.md) | 1995-04-18 |
| 45 | 4 | [Heintz v. Jenkins](../records/Heintz_v_Jenkins_merits_1995-04-18.md) | 1995-04-18 |
| 46 | 4 | [Lanphere & Urbaniak v. Colorado](../records/Lanphere_and_Urbaniak_v_Colorado_merits_1995-04-18.md) | 1995-04-18 |
| 47 | 4 | [Celotex Corp. v. Edwards](../records/Celotex_Corp_v_Edwards_merits_1995-04-19.md) | 1995-04-19 |
| 48 | 4 | [McIntyre v. Ohio Elections Commission](../records/McIntyre_v_Ohio_Elections_Commission_merits_1995-04-19.md) | 1995-04-19 |
| 49 | 5 | [Stone v. Immigration and Naturalization Service](../records/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md) | 1995-04-19 |
| 50 | 5 | [Kyles v. Whitley](../records/Kyles_v_Whitley_merits_1995-04-19.md) | 1995-04-19 |
| 51 | 5 | [Rubin v. Coors Brewing Co.](../records/Rubin_v_Coors_Brewing_Co_merits_1995-04-19.md) | 1995-04-19 |
| 52 | 5 | [California Department of Corrections v. Morales](../records/California_Department_of_Corrections_v_Morales_merits_1995-04-25.md) | 1995-04-25 |
| 53 | 5 | [United States v. Williams](../records/United_States_v_Williams_merits_1995-04-25.md) | 1995-04-25 |
| 54 | 5 | [United States v. Lopez](../records/United_States_v_Lopez_merits_1995-04-26.md) | 1995-04-26 |
| 55 | 5 | [New York State Conference of Blue Cross & Blue Shield Plans v. Travelers Insurance Co. / Pataki v. Travelers Insurance Co. / Hospital Association of New York State v. Travelers Insurance Co.](../records/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md) | 1995-04-26 |
| 56 | 5 | [United States v. Harris](../records/United_States_v_Harris_merits_1995-04-27.md) | 1995-04-27 |
| 57 | 5 | [United States v. Robertson](../records/United_States_v_Robertson_merits_1995-05-01.md) | 1995-05-01 |
| 58 | 5 | [United States v. Pinson](../records/United_States_v_Pinson_merits_1995-05-08.md) | 1995-05-08 |
| 59 | 5 | [Kansas v. Colorado](../records/Kansas_v_Colorado_original_exceptions_1995-05-15.md) | 1995-05-15 |
| 60 | 5 | [Hubbard v. United States](../records/Hubbard_v_United_States_merits_1995-05-15.md) | 1995-05-15 |
| 61 | 6 | [City of Edmonds v. Oxford House, Inc.](../records/City_of_Edmonds_v_Oxford_House_merits_1995-05-15.md) | 1995-05-15 |
| 62 | 6 | [Reynoldsville Casket Co. v. Hyde](../records/Reynoldsville_Casket_Co_v_Hyde_merits_1995-05-15.md) | 1995-05-15 |
| 63 | 6 | [Day v. Holahan](../records/Day_v_Holahan_merits_1995-05-15.md) | 1995-05-15 |
| 64 | 6 | [U.S. Term Limits, Inc. v. Thornton / Bryant v. Hill](../records/US_Term_Limits_v_Thornton_Bryant_v_Hill_merits_1995-05-22.md) | 1995-05-22 |
| 65 | 6 | [Wilson v. Arkansas](../records/Wilson_v_Arkansas_merits_1995-05-22.md) | 1995-05-22 |
| 66 | 6 | [First Options of Chicago, Inc. v. Kaplan](../records/First_Options_of_Chicago_Inc_v_Kaplan_merits_1995-05-22.md) | 1995-05-22 |
| 67 | 6 | [Kelley v. Board of Trustees of the University of Illinois](../records/Kelley_v_Board_of_Trustees_of_the_University_of_Illinois_merits_1995-05-22.md) | 1995-05-22 |
| 68 | 6 | [Nebraska v. Wyoming](../records/Nebraska_v_Wyoming_original_exceptions_1995-05-30.md) | 1995-05-30 |
| 69 | 6 | [North Star Steel Co. v. Thomas / Crown Cork & Seal Co., Inc. v. United Steelworkers of America, AFL-CIO-CLC](../records/North_Star_Steel_v_Thomas_and_Crown_Cork_merits_1995-05-30.md) | 1995-05-30 |
| 70 | 6 | [Garlotte v. Fordice](../records/Garlotte_v_Fordice_merits_1995-05-30.md) | 1995-05-30 |
| 71 | 6 | [United States v. Wellons](../records/United_States_v_Wellons_merits_1995-05-30.md) | 1995-05-30 |
| 72 | 6 | [Reno v. Koray](../records/Reno_v_Koray_merits_1995-06-05.md) | 1995-06-05 |
| 73 | 7 | [Metropolitan Washington Airports Authority v. Hechinger](../records/Metropolitan_Washington_Airports_Authority_v_Hechinger_merits_1995-06-05.md) | 1995-06-05 |
| 74 | 7 | [Missouri v. Jenkins](../records/Missouri_v_Jenkins_merits_1995-06-12.md) | 1995-06-12 |
| 75 | 7 | [Ryder v. United States](../records/Ryder_v_United_States_merits_1995-06-12.md) | 1995-06-12 |
| 76 | 7 | [City of Milwaukee v. Cement Division, National Gypsum Co.](../records/City_of_Milwaukee_v_Cement_Division_National_Gypsum_Co_merits_1995-06-12.md) | 1995-06-12 |
| 77 | 7 | [Adarand Constructors, Inc. v. Peña](../records/Adarand_Constructors_Inc_v_Pena_merits_1995-06-12.md) | 1995-06-12 |
| 78 | 7 | [Wilton v. Seven Falls Co.](../records/Wilton_v_Seven_Falls_Co_merits_1995-06-12.md) | 1995-06-12 |
| 79 | 7 | [Metropolitan Stevedore Co. v. Rambo](../records/Metropolitan_Stevedore_Co_v_Rambo_merits_1995-06-12.md) | 1995-06-12 |
| 80 | 7 | [Johnson v. Jones](../records/Johnson_v_Jones_merits_1995-06-12.md) | 1995-06-12 |
| 81 | 7 | [Kimberlin v. Quinlan](../records/Kimberlin_v_Quinlan_merits_1995-06-12.md) | 1995-06-12 |
| 82 | 7 | [Commissioner v. Schleier](../records/Commissioner_v_Schleier_merits_1995-06-14.md) | 1995-06-14 |
| 83 | 7 | [Chandris, Inc. v. Latsis](../records/Chandris_Inc_v_Latsis_merits_1995-06-14.md) | 1995-06-14 |
| 84 | 7 | [Witte v. United States](../records/Witte_v_United_States_merits_1995-06-14.md) | 1995-06-14 |
| 85 | 8 | [Gutierrez de Martinez v. Lamagno](../records/Gutierrez_de_Martinez_v_Lamagno_merits_1995-06-14.md) | 1995-06-14 |
| 86 | 8 | [Oklahoma Tax Commission v. Chickasaw Nation](../records/Oklahoma_Tax_Commission_v_Chickasaw_Nation_merits_1995-06-14.md) | 1995-06-14 |
| 87 | 8 | [Sandin v. Conner](../records/Sandin_v_Conner_merits_1995-06-19.md) | 1995-06-19 |
| 88 | 8 | [United States v. Gaudin](../records/United_States_v_Gaudin_merits_1995-06-19.md) | 1995-06-19 |
| 89 | 8 | [Vimar Seguros y Reaseguros, S.A. v. M/V Sky Reefer](../records/Vimar_Seguros_y_Reaseguros_SA_v_MV_Sky_Reefer_merits_1995-06-19.md) | 1995-06-19 |
| 90 | 8 | [Hurley v. Irish-American Gay, Lesbian and Bisexual Group of Boston](../records/Hurley_v_Irish_American_Gay_Lesbian_and_Bisexual_Group_of_Boston_merits_1995-06-19.md) | 1995-06-19 |
| 91 | 8 | [National Private Truck Council, Inc. v. Oklahoma Tax Commission](../records/National_Private_Truck_Council_Inc_v_Oklahoma_Tax_Commission_merits_1995-06-19.md) | 1995-06-19 |
| 92 | 8 | [United States v. Aguilar](../records/United_States_v_Aguilar_merits_1995-06-21.md) | 1995-06-21 |
| 93 | 8 | [Florida Bar v. Went For It, Inc.](../records/Florida_Bar_v_Went_For_It_Inc_merits_1995-06-21.md) | 1995-06-21 |
| 94 | 8 | [Vernonia School District 47J v. Acton](../records/Vernonia_School_District_47J_v_Acton_merits_1995-06-26.md) | 1995-06-26 |
| 95 | 8 | [Rosenberger v. Rector and Visitors of the University of Virginia](../records/Rosenberger_v_Rector_and_Visitors_of_the_University_of_Virginia_merits_1995-06-29.md) | 1995-06-29 |
| 96 | 8 | [Babbitt v. Sweet Home Chapter of Communities for a Great Oregon](../records/Babbitt_v_Sweet_Home_Chapter_of_Communities_for_a_Great_Oregon_merits_1995-06-29.md) | 1995-06-29 |
| 97 | 9 | [Miller v. Johnson / Abrams v. Johnson / United States v. Johnson](../records/Miller_and_consolidated_merits_1995-06-29.md) | 1995-06-29 |
| 98 | 9 | [Capitol Square Review and Advisory Board v. Pinette](../records/Pinette_merits_1995-06-29.md) | 1995-06-29 |
| 99 | 9 | [Chabad-Lubavitch of Georgia v. Miller](../records/Chabad_Lubavitch_v_Miller_merits_1995-06-29.md) | 1995-06-29 |

## 7. Close readiness and operator handoff

The term is not ready for the Commit pass. F01–F03 remain reported without repair. After a separate authorized correction task, rerun the deterministic gate and then perform the requested fresh legal review across all 99 matters, both Holdings passes and all three candidates. This report must not be used to treat that unperformed stage as complete.

**Operator summary: FAIL.**

**Findings by severity: Critical 0; High 0; Medium 0; Low 3 — 3 total (twelve stale ledger cells, residual typography in three Records, and one checker defect). No Git commands or fixes performed.**
