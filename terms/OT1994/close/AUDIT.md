# October Term 1994 — Audit

**Audit date:** October 1, 2026.  
**Result:** FAIL — the requested stale-version sweep fails; the fresh legal-substance stage is gated.  
**Unresolved findings:** 2 low-severity retention discrepancies, affecting eight derived files.  
**Change boundary:** This report only. No adjudication, brief, freeze, tracker, projection, render, or candidate was corrected. No Git command was executed.

## Scope and stage boundary

The governing AGENTS.md, Engine, Render Contract, Court Composition, and tracker instructions were consulted. The first executed repository check was `python tools/check_term.py OT1994`. The subsequent deterministic review covered the 99 inventory matters, 101 current Records (99 Court events and two Admitted Source Records), nine generated Render Inputs, nine public renders, the workspace, runtime splits, both Holdings passes in the single cumulative candidate, Standards and Tests, and Standing State.

The user's instruction requires the deterministic checks to pass **before** a fresh AI audit reviews legal substance. The current corrected adjudicative files are aligned, but obsolete assembly and entering-law copies remain in the working tree. Their explicit historical banners prevent a claim that they are current law; they nevertheless prevent the requested assurance that “no stale version survives anywhere.” Findings F01 and F02 record that narrow retention discrepancy. Severity is low because the copies are conspicuously superseded and no resulting corruption of a current Record, generated Render Input, render, or close candidate was established.

**The fresh legal-substance review was not started.** Votes' legal justification, coalition compatibility, holdings' substantive completeness, precedent treatment, remedies' legal correctness, Justice-specific historical departures, and the independent legal derivation of the three candidates remain uncertified by this audit for all 99 matters. The arithmetic and projection comparisons below do not establish those legal conclusions. Previous audits' legal conclusions are not adopted as a substitute. This report cannot support a Commit pass.

“Working tree” here excludes Git's retained history and ignored scratch directories. Frozen provisional and reconciled commitments are historical stage evidence that the Engine requires preserving; their original positions are not counted as duplicate completed adjudications. F01 and F02 concern obsolete derived copies of completed adjudicative law or assembly text.

## Unresolved findings

### F01 — Low: seven derived files retain superseded Morales law

The [current Morales Record](../records/California_Department_of_Corrections_v_Morales_merits_1995-04-25.md) states a **5–4 affirmance**, with offense-date annual consideration preserved. Its current Public Projection, chunk-5 generated Render Input, public render, workspace law, and candidate Holdings preserve that result. The auxiliary `runtime/OT_1994CHUNK5_MORALES_CORRECTION_RENDER_INPUT.md` also matches the current Public Projection after trimming the outer newline.

Seven files still retain the superseded **5–4 reversal without a controlling constitutional rationale** or descriptions of that superseded result:

| File | Exact retained text location and discrepancy |
|---|---|
| [Morales assembly draft](../runtime/assembly/California_Department_of_Corrections_v_Morales_merits_1995-04-25.md) | Line 5 states reversal/remand and no majority constitutional rationale. Lines 50 and 160 announce reversal; lines 70 and 184 reproduce the superseded judgment-without-controlling-rationale account. |
| [Entering law before April 26](../entering-law/OT_1994CHUNK5_BEFORE_1995-04-26.md) | Line 179 states reversal and vacation of the hearing-frequency habeas relief; line 212 directs implementation of that superseded result. |
| [Entering law before April 27](../entering-law/OT_1994CHUNK5_BEFORE_1995-04-27.md) | The same superseded judgment at line 179 and procedural consequence at line 212. |
| [Entering law before May 8](../entering-law/OT_1994CHUNK5_BEFORE_1995-05-08.md) | The same superseded judgment at line 179 and procedural consequence at line 212. |
| [Entering law before May 15](../entering-law/OT_1994CHUNK5_BEFORE_1995-05-15.md) | The same superseded judgment at line 179 and procedural consequence at line 212. |
| [Lopez assembly draft](../runtime/assembly/United_States_v_Lopez_merits_1995-04-26.md) | Line 176 says Morales reverses without a single controlling rationale; the following Justice-specific refresh table uses the former plurality alignment. |
| [Travelers assembly draft](../runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md) | Line 221 repeats the old reversal/no-majority account; the following refresh table uses the former alignment. |

Each has a supersession banner at line 1 pointing to the current Morales Record and correction commit. Those banners are accurate and material mitigation. This finding concerns retention under this task's literal no-stale-version condition, **not** an assertion that the obsolete passages govern Lopez, Travelers, or current law. Their presence was not silently treated as a new adjudicative conflict or as authority to change any vote. No deletion, replacement, or substantive correction was performed.

### F02 — Low: the superseded Stone v. INS assignment paragraph remains in an assembly draft

The [historical assembly draft](../runtime/assembly/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md), line 177, retains the paragraph beginning “Stevens is the senior Justice” and then applying “Fit:” and expansion reasoning to Stevens's assignment. Its line-1 banner correctly identifies it as a superseded historical draft.

The [current Record](../records/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md) instead models Stevens's ordinary assignment discretion because the Chief dissents. The 5–4 affirmance, Kennedy Court opinion, Breyer dissent, and current public handoffs agree. Direct reading of commit `8d98261d33b6d39fda8a9ccc52ab5ad7ed3be02a` and its immediate parent confirms that the cited assignment correction replaced this paragraph while leaving that commit's Public Projection unchanged. The remaining obsolete draft prevents the requested assurance that the old paragraph survives only in repository history. No evidence was found that the current Record or render still applies it.

## Deterministic checks and evidence

| Check | Result and scope |
|---|---|
| Required first checker | Exit 0: `OK: OT1994; 58 warning(s)`. The checker was left unchanged. Its internal `git cat-file -e` requests were serviced by a scratch-only Python adapter reading Git objects directly; no Git executable was launched. All other checker operations ran normally. |
| Holdings-volume synchronization | Passed through the checker's read-only `holdings_volumes.py check` invocation. |
| Inventory → manifest → Record → Render Input → render | 99 inventory rows, 99 completed manifest rows, 99 distinct Court Records, 99 generated source-record blocks and 99 bounded public entries. Chunks 1–8 each contain 12 matters; chunk 9 contains 3. No missing or duplicate current event was found. Consolidated companions remain one inventory matter with their supplied dockets. |
| Additional Records | The other two Records are the Vaccine Injury Table change effective March 10, 1995, and Plant Variety Protection Act amendments effective April 4, 1995. They are source admissions, not additional Court decisions requiring case-render entries. |
| Effective-date order | Current event dates agree with inventory, manifest, filenames, generated inputs, public event lines and public closing lines. Chunk ordering is chronological, November 1, 1994–June 29, 1995. Same-day ties are preserved; Pinette precedes Chabad under the recorded coordinated sequence. The ledger expressly uses file-preservation order, not purported verified Git commitment order. The two admitted-source dates appear in the manifest's effective-law calendar. No new chronology correction was made. |
| Participation, vote and join arithmetic | All 99 public judgment/participation/topology accounts were inspected, including prose and nonnumeric rows. The sitting roster is Stone, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. The seven-member Grubart Court satisfies quorum. Evans's 6–1–2 disposition is a three-way tally, not a malformed 6–1 vote. NTEU's unanimous removal of unrepresented beneficiaries does not count its explanatory reference to Scalia and Thomas as opposition. Nonreach, conditional positions, and separate writings were not counted as additional votes. No tally discrepancy remained after review. This is not a legal endorsement of those votes. |
| Participation exclusions | FEC: Ginsburg; Wolens: Scalia; Grubart: Stevens and Breyer; Milwaukee/National Gypsum: Breyer; Wilton: Breyer; Sky Reefer: Breyer. The six affected matters' reduced Court totals reconcile. No reason for nonparticipation was inferred. |
| Runtime-split freshness | All nine `split_chunk.py … --check` calls passed through the first checker: 27 generated neutral/Stone/comparator files match the current nine approved briefs. This does not erase historically frozen stage commitments or obsolete derived copies identified in F01/F02. |
| Public Projection → Render Input identity | All 99 generated source-record bodies exactly match the corresponding bounded Public Projection after the builder/checker's outer-whitespace treatment. All eleven blocks are present in order. |
| Public render cross-check | All 99 events have their case heading, event/date line, closing line and supplied docket identity. All 236 operative-rule/controlling-proposition texts survive after ordinary Markdown and typographic normalization. Full and compact arithmetic/topology accounts were compared; compact restatement of authority is not treated as a lost vote. The three explanation wording differences flagged mechanically—Anderson v. Edwards, Celotex, and Sweet Home—are reference/voice restatements, not contradictory operative text. The checker's public workflow-leak checks passed. A comprehensive legal/prose-completeness audit remains gated. |
| Holdings explanation length | All 236 supplied controlling explanations fall within 120–200 whitespace-delimited words. This measures length only. |
| Local links and anchors | 12,281 local/repository Markdown link occurrences checked across current term materials outside ignored scratch and the audit being replaced; 1,033 distinct target/revision combinations. No target or anchor failure remained after handling directories, binary source files, pinned-revision targets and the prospective candidate links below. |
| Candidate publication links | 188 candidate links point to future `state/HOLDINGS.md` or `state/STANDARDS_AND_TESTS.md` anchors. Each resolves in the corresponding candidate that would be published at Commit. They do not yet resolve in the unchanged opening tracker; that expected staging condition is explicitly distinguished from a broken candidate anchor. |
| External links | External public-source URLs were not all live-retrieved. Local resolution is not a claim that every remote site currently returns its source or that its legal content has been reverified. |
| Commit-hash existence | All 16 detected genuine commit-reference occurrences outside the replaced audit resolve to three SHA-1-verified commit objects: `13b19ee463d16fb4377d846e5b058599f886bed3`, `d086219b424d812aaa837fda9533629c69e33833`, and `8d98261d33b6d39fda8a9ccc52ab5ad7ed3be02a`. Object data were read and validated directly from loose/packed storage. |
| Concise lineage | Morales's referenced commit and immediate-parent comparison support the replacement lineage; Stone v. INS's comparison supports the assignment-only correction claim. The latter unchanged-projection claim concerns that correction, not an assertion that subsequent clerical revisions never occurred. Transcon, Fargo, O'Neal and Robertson describe completion of previously unadjudicated/stopped intake rather than inventing a superseded completed decision. No first-record hash or narrative commit archaeology is claimed. |
| Candidate cleanup | Pre-Commit staging is intact: one Holdings candidate, one Standards candidate, one Standing State candidate, the two current Holdings pass notes, one Standards pass note, this Audit and `.gitkeep`. No Term-Close Dossier marks a completed publication. Required candidates/pass notes have not been prematurely deleted. F01/F02 concern separate obsolete derived files. |
| Open-matter carry-forward | Nine continuing matters appear in Standing State: the eight inherited matters, with Nebraska's current original-proceeding stage, plus Kansas's remedy phase. The seven unscheduled carryovers outside the inventory are retained. No expired date alone is treated as a terminal order. Ten separate user-added OT1995 docket matters are also listed. Ordinary remands below are not silently converted into pending Supreme Court proceedings. |

### Checker-warning disposition

The 58 warnings are false positives from the checker's broad hexadecimal-token regex, not missing cited commits. The exact token counts are: `A40385013` (33), `A40386012` (7), `A40386002` (2), `cceeded` (2), and one each of `8314011`, `A40386007`, `1662045`, `2035579`, `1994168`, `e21F3d1038`, `ec1395dd`, `A40386003`, `2006630`, `b103272`, `5223F70CBD862DEEE5634BA1F102E638`, `9780300050288`, `1000180149`, and `1000180155`. These occur as archive/source identifiers, URL/report/document identifiers, an ISBN, or a within-word match. None is asserted in context to be a Git commit. They were not converted into 58 substantive findings.

### Candidate coverage and publication boundary

The single cumulative [Holdings candidate](HOLDINGS.candidate.md) contains all 236 source holding blocks: **154 from matters 1–60 (pass 1)** and **82 from matters 61–99 (pass 2)**. Every current Court Record has a source reference. 235 operative propositions match after formatting normalization; Clearwater's remaining comparison differs only by removal of the deictic word “below” from “designated below as,” leaving the same enumerated sections and rule. This is coverage and transcription evidence, not a new determination of controlling authority.

[Standards and Tests](STANDARDS_AND_TESTS.candidate.md) was checked for synchronized header fields, file/anchor resolution and source navigation. Its full independent doctrinal derivation remains for the gated legal pass. Absence of a new stand-alone entry or literal Record filename for an application of an existing rule is not itself treated as an omission. [Standing State](STANDING_STATE.candidate.md) was checked against the Composition and manifest for the nine-Justice roster and seniority, thirteen circuit assignments, retained referral practice and docket counts/stages.

All three candidates retain the same prepublication fields: **Last completed October Term: 1993; Processed through: June 30, 1994, after all eleven chunk-8 matters and all 95 OT1993 inventory Court events.; Edition: September 28, 2026.** Standing State separately identifies its intended OT1995 opening posture. No common published cutoff has been advanced during this Audit.

## Six specifically requested correction checks

| Matter | Current Record / generated Input / public render comparison | Remaining exception |
|---|---|---|
| Interstate Commerce Commission v. Transcon Lines | 9–0 reversal and confined injunction-implementation remand; Kennedy for all nine. Ordinary unpaid freight principal/other receivables excluded; actual scope questions beyond concessions retained. Current three-way projection consistent. | None found in the current adjudicative projections. Completion of earlier revalidation is not labeled a second adjudication. |
| Fargo Women's Health Organization v. Schafer | Access vacatur/remand 6–3; definition-vagueness and limited associated penalty affirmances 8–1. Souter's component joins remain distinct; no single 6–3 or 8–1 overall judgment invented. Current three-way projection consistent. | Earlier incomplete freezes remain identified stage history. |
| O'Neal v. McAninch | Vacatur/remand 7–2; narrow Chapman instruction 5–4; broader extension only three votes. O'Connor's parts and conditional-writ limits preserved in all three current artifacts. | No superseded Kotteakos remand was found as the current Court rule. |
| United States v. Robertson | 9–0 Count Six commerce reversal/remand; Breyer for all nine. Remaining appellate/RICO sentencing work and independent drug-sentence consequences preserved. Chunk-5 render contains the completed event. | Original provisional/stopped stage descriptions are qualified by current completion notices and the current Record. |
| California Department of Corrections v. Morales | 5–4 affirmance; O'Connor joined by Stone, Stevens, Souter and Ginsburg; Kennedy dissent joined by Scalia, Thomas and Breyer. Annual consideration preserved; no parole award. Current three-way projection consistent. | F01: seven obsolete derived copies remain, each labeled superseded. |
| Stone v. Immigration and Naturalization Service | 5–4 affirmance; Kennedy joined by Stevens, Scalia, Thomas and Ginsburg; Breyer dissent joined by Stone, O'Connor and Souter. Current assignment paragraph states Stevens's ordinary discretion. Current three-way projection consistent. | F02: the historical assembly copy still contains the pre-correction paragraph. |

## All-matter deterministic coverage register

Every row below received the inventory/date/Record/generated-projection/render-presence and participation/vote/topology arithmetic checks described above. “D passed” is limited to those current adjudicative interfaces. The stale-retention exceptions are listed separately. **Legal review is deferred for every row**, including rows without a retention finding.

| No. | Chunk | Matter and current Record | Effective date | Deterministic status |
|---:|---:|---|---|---|
| 1 | 1 | [United States v. Shabani](../records/United_States_v_Shabani_merits_1994-11-01.md) | 1994-11-01 | D passed |
| 2 | 1 | [U.S. Bancorp Mortgage Co. v. Bonner Mall Partnership](../records/US_Bancorp_Mortgage_Co_v_Bonner_Mall_Partnership_mootness_vacatur_1994-11-08.md) | 1994-11-08 | D passed |
| 3 | 1 | [Hess v. Port Authority Trans-Hudson Corp.](../records/Hess_v_Port_Authority_Trans_Hudson_Corp_merits_1994-11-14.md) | 1994-11-14 | D passed |
| 4 | 1 | [United States v. X-Citement Video, Inc.](../records/United_States_v_X_Citement_Video_Inc_merits_1994-11-29.md) | 1994-11-29 | D passed |
| 5 | 1 | [Church of Scientology Flag Service Organization, Inc. v. City of Clearwater](../records/Church_of_Scientology_Flag_Service_Organization_Inc_v_City_of_Clearwater_merits_1994-12-05.md) | 1994-12-05 | D passed |
| 6 | 1 | [Federal Election Commission v. NRA Political Victory Fund](../records/Federal_Election_Commission_v_NRA_Political_Victory_Fund_jurisdictional_dismissal_1994-12-06.md) | 1994-12-06 | D passed |
| 7 | 1 | [Reich v. Collins](../records/Reich_v_Collins_merits_1994-12-06.md) | 1994-12-06 | D passed |
| 8 | 1 | [Brown v. Gardner](../records/Brown_v_Gardner_merits_1994-12-12.md) | 1994-12-12 | D passed |
| 9 | 1 | [Nebraska Department of Revenue v. Loewenstein](../records/Nebraska_Department_of_Revenue_v_Loewenstein_merits_1994-12-12.md) | 1994-12-12 | D passed |
| 10 | 1 | [In re Baby K](../records/In_re_Baby_K_merits_1994-12-12.md) | 1994-12-12 | D passed |
| 11 | 1 | [Plakas v. Drinski](../records/Plakas_v_Drinski_merits_1995-01-09.md) | 1995-01-09 | D passed |
| 12 | 1 | [Interstate Commerce Commission v. Transcon Lines](../records/Interstate_Commerce_Commission_v_Transcon_Lines_merits_1995-01-10.md) | 1995-01-10 | D passed |
| 13 | 2 | [Tome v. United States](../records/Tome_v_United_States_merits_1995-01-10.md) | 1995-01-10 | D passed |
| 14 | 2 | [Young v. Northern Illinois Conference of United Methodist Church](../records/Young_v_Northern_Illinois_Conference_merits_1995-01-17.md) | 1995-01-17 | D passed |
| 15 | 2 | [Asgrow Seed Co. v. Winterboer](../records/Asgrow_Seed_Co_v_Winterboer_merits_1995-01-18.md) | 1995-01-18 | D passed |
| 16 | 2 | [United States v. Mezzanatto](../records/United_States_v_Mezzanatto_merits_1995-01-18.md) | 1995-01-18 | D passed |
| 17 | 2 | [American Airlines, Inc. v. Wolens](../records/American_Airlines_Inc_v_Wolens_merits_1995-01-18.md) | 1995-01-18 | D passed |
| 18 | 2 | [NationsBank of North Carolina, N.A. v. Variable Annuity Life Insurance Co. / Ludwig v. Variable Annuity Life Insurance Co.](../records/NationsBank_Ludwig_v_Variable_Annuity_Life_Insurance_Co_merits_1995-01-18.md) | 1995-01-18 | D passed |
| 19 | 2 | [Allied-Bruce Terminix Cos. v. Dobson](../records/Allied_Bruce_Terminix_Cos_v_Dobson_merits_1995-01-18.md) | 1995-01-18 | D passed |
| 20 | 2 | [Schlup v. Delo](../records/Schlup_v_Delo_merits_1995-01-23.md) | 1995-01-23 | D passed |
| 21 | 2 | [McKennon v. Nashville Banner Publishing Co.](../records/McKennon_v_Nashville_Banner_Publishing_Co_merits_1995-01-23.md) | 1995-01-23 | D passed |
| 22 | 2 | [Fargo Women’s Health Organization v. Schafer](../records/Fargo_Womens_Health_Organization_v_Schafer_merits_1995-02-13.md) | 1995-02-13 | D passed |
| 23 | 2 | [Lebron v. National Railroad Passenger Corp.](../records/Lebron_v_National_Railroad_Passenger_Corp_merits_1995-02-21.md) | 1995-02-21 | D passed |
| 24 | 2 | [Milwaukee Brewery Workers' Pension Plan v. Jos. Schlitz Brewing Co.](../records/Milwaukee_Brewery_Workers_Pension_Plan_v_Jos_Schlitz_Brewing_Co_merits_1995-02-21.md) | 1995-02-21 | D passed |
| 25 | 3 | [O'Neal v. McAninch](../records/ONeal_v_McAninch_merits_1995-02-21.md) | 1995-02-21 | D passed |
| 26 | 3 | [United States v. National Treasury Employees Union](../records/United_States_v_National_Treasury_Employees_Union_merits_1995-02-22.md) | 1995-02-22 | D passed |
| 27 | 3 | [Harris v. Alabama](../records/Harris_v_Alabama_merits_1995-02-22.md) | 1995-02-22 | D passed |
| 28 | 3 | [Jerome B. Grubart, Inc. v. Great Lakes Dredge & Dock Co. / City of Chicago v. Great Lakes Dredge & Dock Co.](../records/Jerome_B_Grubart_Inc_v_Great_Lakes_Dredge_Dock_Co_merits_1995-02-22.md) | 1995-02-22 | D passed |
| 29 | 3 | [Anderson v. Green](../records/Anderson_v_Green_decision_1995-02-22.md) | 1995-02-22 | D passed |
| 30 | 3 | [Gustafson v. Alloyd Co.](../records/Gustafson_v_Alloyd_Co_merits_1995-02-28.md) | 1995-02-28 | D passed |
| 31 | 3 | [Arizona v. Evans](../records/Arizona_v_Evans_merits_1995-03-01.md) | 1995-03-01 | D passed |
| 32 | 3 | [Swint v. Chambers County Commission](../records/Swint_v_Chambers_County_Commission_merits_1995-03-01.md) | 1995-03-01 | D passed |
| 33 | 3 | [Mastrobuono v. Shearson Lehman Hutton, Inc.](../records/Mastrobuono_v_Shearson_Lehman_Hutton_Inc_merits_1995-03-06.md) | 1995-03-06 | D passed |
| 34 | 3 | [Curtiss-Wright Corp. v. Schoonejongen](../records/Curtiss_Wright_Corp_v_Schoonejongen_merits_1995-03-06.md) | 1995-03-06 | D passed |
| 35 | 3 | [Shalala v. Guernsey Memorial Hospital](../records/Shalala_v_Guernsey_Memorial_Hospital_merits_1995-03-06.md) | 1995-03-06 | D passed |
| 36 | 3 | [Ambassador Books & Video, Inc. v. City of Little Rock](../records/Ambassador_Books_Video_Inc_v_City_of_Little_Rock_merits_1995-03-20.md) | 1995-03-20 | D passed |
| 37 | 4 | [Director, Office of Workers’ Compensation Programs v. Newport News Shipbuilding & Dry Dock Co.](../records/Director_Office_of_Workers_Compensation_Programs_v_Newport_News_Shipbuilding_and_Dry_Dock_Co_merits_1995-03-21.md) | 1995-03-21 | D passed |
| 38 | 4 | [Anderson v. Edwards](../records/Anderson_v_Edwards_merits_1995-03-22.md) | 1995-03-22 | D passed |
| 39 | 4 | [Swanner v. Anchorage Equal Rights Commission](../records/Swanner_v_Anchorage_Equal_Rights_Commission_merits_1995-03-27.md) | 1995-03-27 | D passed |
| 40 | 4 | [Qualitex Co. v. Jacobson Products Co.](../records/Qualitex_Co_v_Jacobson_Products_Co_merits_1995-03-28.md) | 1995-03-28 | D passed |
| 41 | 4 | [Oklahoma Tax Commission v. Jefferson Lines, Inc.](../records/Oklahoma_Tax_Commission_v_Jefferson_Lines_Inc_merits_1995-04-03.md) | 1995-04-03 | D passed |
| 42 | 4 | [Plaut v. Spendthrift Farm, Inc.](../records/Plaut_v_Spendthrift_Farm_Inc_merits_1995-04-18.md) | 1995-04-18 | D passed |
| 43 | 4 | [Shalala v. Whitecotton](../records/Shalala_v_Whitecotton_merits_1995-04-18.md) | 1995-04-18 | D passed |
| 44 | 4 | [Freightliner Corp. v. Myrick](../records/Freightliner_Corp_v_Myrick_merits_1995-04-18.md) | 1995-04-18 | D passed |
| 45 | 4 | [Heintz v. Jenkins](../records/Heintz_v_Jenkins_merits_1995-04-18.md) | 1995-04-18 | D passed |
| 46 | 4 | [Lanphere & Urbaniak v. Colorado](../records/Lanphere_and_Urbaniak_v_Colorado_merits_1995-04-18.md) | 1995-04-18 | D passed |
| 47 | 4 | [Celotex Corp. v. Edwards](../records/Celotex_Corp_v_Edwards_merits_1995-04-19.md) | 1995-04-19 | D passed |
| 48 | 4 | [McIntyre v. Ohio Elections Commission](../records/McIntyre_v_Ohio_Elections_Commission_merits_1995-04-19.md) | 1995-04-19 | D passed |
| 49 | 5 | [Stone v. Immigration and Naturalization Service](../records/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md) | 1995-04-19 | D passed; F02 retained draft |
| 50 | 5 | [Kyles v. Whitley](../records/Kyles_v_Whitley_merits_1995-04-19.md) | 1995-04-19 | D passed |
| 51 | 5 | [Rubin v. Coors Brewing Co.](../records/Rubin_v_Coors_Brewing_Co_merits_1995-04-19.md) | 1995-04-19 | D passed |
| 52 | 5 | [California Department of Corrections v. Morales](../records/California_Department_of_Corrections_v_Morales_merits_1995-04-25.md) | 1995-04-25 | D passed; F01 retained derivatives |
| 53 | 5 | [United States v. Williams](../records/United_States_v_Williams_merits_1995-04-25.md) | 1995-04-25 | D passed |
| 54 | 5 | [United States v. Lopez](../records/United_States_v_Lopez_merits_1995-04-26.md) | 1995-04-26 | D passed |
| 55 | 5 | [New York State Conference of Blue Cross & Blue Shield Plans v. Travelers Insurance Co. / Pataki v. Travelers Insurance Co. / Hospital Association of New York State v. Travelers Insurance Co.](../records/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md) | 1995-04-26 | D passed |
| 56 | 5 | [United States v. Harris](../records/United_States_v_Harris_merits_1995-04-27.md) | 1995-04-27 | D passed |
| 57 | 5 | [United States v. Robertson](../records/United_States_v_Robertson_merits_1995-05-01.md) | 1995-05-01 | D passed |
| 58 | 5 | [United States v. Pinson](../records/United_States_v_Pinson_merits_1995-05-08.md) | 1995-05-08 | D passed |
| 59 | 5 | [Kansas v. Colorado](../records/Kansas_v_Colorado_original_exceptions_1995-05-15.md) | 1995-05-15 | D passed |
| 60 | 5 | [Hubbard v. United States](../records/Hubbard_v_United_States_merits_1995-05-15.md) | 1995-05-15 | D passed |
| 61 | 6 | [City of Edmonds v. Oxford House, Inc.](../records/City_of_Edmonds_v_Oxford_House_merits_1995-05-15.md) | 1995-05-15 | D passed |
| 62 | 6 | [Reynoldsville Casket Co. v. Hyde](../records/Reynoldsville_Casket_Co_v_Hyde_merits_1995-05-15.md) | 1995-05-15 | D passed |
| 63 | 6 | [Day v. Holahan](../records/Day_v_Holahan_merits_1995-05-15.md) | 1995-05-15 | D passed |
| 64 | 6 | [U.S. Term Limits, Inc. v. Thornton / Bryant v. Hill](../records/US_Term_Limits_v_Thornton_Bryant_v_Hill_merits_1995-05-22.md) | 1995-05-22 | D passed |
| 65 | 6 | [Wilson v. Arkansas](../records/Wilson_v_Arkansas_merits_1995-05-22.md) | 1995-05-22 | D passed |
| 66 | 6 | [First Options of Chicago, Inc. v. Kaplan](../records/First_Options_of_Chicago_Inc_v_Kaplan_merits_1995-05-22.md) | 1995-05-22 | D passed |
| 67 | 6 | [Kelley v. Board of Trustees of the University of Illinois](../records/Kelley_v_Board_of_Trustees_of_the_University_of_Illinois_merits_1995-05-22.md) | 1995-05-22 | D passed |
| 68 | 6 | [Nebraska v. Wyoming](../records/Nebraska_v_Wyoming_original_exceptions_1995-05-30.md) | 1995-05-30 | D passed |
| 69 | 6 | [North Star Steel Co. v. Thomas / Crown Cork & Seal Co., Inc. v. United Steelworkers of America, AFL-CIO-CLC](../records/North_Star_Steel_v_Thomas_and_Crown_Cork_merits_1995-05-30.md) | 1995-05-30 | D passed |
| 70 | 6 | [Garlotte v. Fordice](../records/Garlotte_v_Fordice_merits_1995-05-30.md) | 1995-05-30 | D passed |
| 71 | 6 | [United States v. Wellons](../records/United_States_v_Wellons_merits_1995-05-30.md) | 1995-05-30 | D passed |
| 72 | 6 | [Reno v. Koray](../records/Reno_v_Koray_merits_1995-06-05.md) | 1995-06-05 | D passed |
| 73 | 7 | [Metropolitan Washington Airports Authority v. Hechinger](../records/Metropolitan_Washington_Airports_Authority_v_Hechinger_merits_1995-06-05.md) | 1995-06-05 | D passed |
| 74 | 7 | [Missouri v. Jenkins](../records/Missouri_v_Jenkins_merits_1995-06-12.md) | 1995-06-12 | D passed |
| 75 | 7 | [Ryder v. United States](../records/Ryder_v_United_States_merits_1995-06-12.md) | 1995-06-12 | D passed |
| 76 | 7 | [City of Milwaukee v. Cement Division, National Gypsum Co.](../records/City_of_Milwaukee_v_Cement_Division_National_Gypsum_Co_merits_1995-06-12.md) | 1995-06-12 | D passed |
| 77 | 7 | [Adarand Constructors, Inc. v. Peña](../records/Adarand_Constructors_Inc_v_Pena_merits_1995-06-12.md) | 1995-06-12 | D passed |
| 78 | 7 | [Wilton v. Seven Falls Co.](../records/Wilton_v_Seven_Falls_Co_merits_1995-06-12.md) | 1995-06-12 | D passed |
| 79 | 7 | [Metropolitan Stevedore Co. v. Rambo](../records/Metropolitan_Stevedore_Co_v_Rambo_merits_1995-06-12.md) | 1995-06-12 | D passed |
| 80 | 7 | [Johnson v. Jones](../records/Johnson_v_Jones_merits_1995-06-12.md) | 1995-06-12 | D passed |
| 81 | 7 | [Kimberlin v. Quinlan](../records/Kimberlin_v_Quinlan_merits_1995-06-12.md) | 1995-06-12 | D passed |
| 82 | 7 | [Commissioner v. Schleier](../records/Commissioner_v_Schleier_merits_1995-06-14.md) | 1995-06-14 | D passed |
| 83 | 7 | [Chandris, Inc. v. Latsis](../records/Chandris_Inc_v_Latsis_merits_1995-06-14.md) | 1995-06-14 | D passed |
| 84 | 7 | [Witte v. United States](../records/Witte_v_United_States_merits_1995-06-14.md) | 1995-06-14 | D passed |
| 85 | 8 | [Gutierrez de Martinez v. Lamagno](../records/Gutierrez_de_Martinez_v_Lamagno_merits_1995-06-14.md) | 1995-06-14 | D passed |
| 86 | 8 | [Oklahoma Tax Commission v. Chickasaw Nation](../records/Oklahoma_Tax_Commission_v_Chickasaw_Nation_merits_1995-06-14.md) | 1995-06-14 | D passed |
| 87 | 8 | [Sandin v. Conner](../records/Sandin_v_Conner_merits_1995-06-19.md) | 1995-06-19 | D passed |
| 88 | 8 | [United States v. Gaudin](../records/United_States_v_Gaudin_merits_1995-06-19.md) | 1995-06-19 | D passed |
| 89 | 8 | [Vimar Seguros y Reaseguros, S.A. v. M/V Sky Reefer](../records/Vimar_Seguros_y_Reaseguros_SA_v_MV_Sky_Reefer_merits_1995-06-19.md) | 1995-06-19 | D passed |
| 90 | 8 | [Hurley v. Irish-American Gay, Lesbian and Bisexual Group of Boston](../records/Hurley_v_Irish_American_Gay_Lesbian_and_Bisexual_Group_of_Boston_merits_1995-06-19.md) | 1995-06-19 | D passed |
| 91 | 8 | [National Private Truck Council, Inc. v. Oklahoma Tax Commission](../records/National_Private_Truck_Council_Inc_v_Oklahoma_Tax_Commission_merits_1995-06-19.md) | 1995-06-19 | D passed |
| 92 | 8 | [United States v. Aguilar](../records/United_States_v_Aguilar_merits_1995-06-21.md) | 1995-06-21 | D passed |
| 93 | 8 | [Florida Bar v. Went For It, Inc.](../records/Florida_Bar_v_Went_For_It_Inc_merits_1995-06-21.md) | 1995-06-21 | D passed |
| 94 | 8 | [Vernonia School District 47J v. Acton](../records/Vernonia_School_District_47J_v_Acton_merits_1995-06-26.md) | 1995-06-26 | D passed |
| 95 | 8 | [Rosenberger v. Rector and Visitors of the University of Virginia](../records/Rosenberger_v_Rector_and_Visitors_of_the_University_of_Virginia_merits_1995-06-29.md) | 1995-06-29 | D passed |
| 96 | 8 | [Babbitt v. Sweet Home Chapter of Communities for a Great Oregon](../records/Babbitt_v_Sweet_Home_Chapter_of_Communities_for_a_Great_Oregon_merits_1995-06-29.md) | 1995-06-29 | D passed |
| 97 | 9 | [Miller v. Johnson / Abrams v. Johnson / United States v. Johnson](../records/Miller_and_consolidated_merits_1995-06-29.md) | 1995-06-29 | D passed |
| 98 | 9 | [Capitol Square Review and Advisory Board v. Pinette](../records/Pinette_merits_1995-06-29.md) | 1995-06-29 | D passed |
| 99 | 9 | [Chabad-Lubavitch of Georgia v. Miller](../records/Chabad_Lubavitch_v_Miller_merits_1995-06-29.md) | 1995-06-29 | D passed |

## Preservation and operator handoff

Scratch readers, object verification, fresh extraction/check outputs, the initial protected-file fingerprint inventory, and provenance comparisons are under ignored `tmp/ot1994_audit/`. Scratch results are supporting evidence; the findings and scope limits needed to use this report are stated above. Scripts did not determine legal meaning or authorize correction.

SHA-256 comparison of 3,546 captured files under `foundation/`, `state/`, `terms/`, and `tools/` found exactly one changed file: `terms/OT1994/close/AUDIT.md`. No file in that protected set was added or removed. The remaining work belongs to a separately authorized correction task and a subsequent audit that clears the deterministic gate before reviewing all 99 matters and all three candidates on legal substance.

**Operator summary: FAIL — fresh legal review remains gated by the two retention findings.**  
**Findings by severity: critical 0; high 0; medium 0; low 2.**
