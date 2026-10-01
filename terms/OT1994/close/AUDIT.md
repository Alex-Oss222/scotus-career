# October Term 1994 — close audit

**Audit date:** September 30, 2026.  
**Result: FAIL.** **Two unresolved findings: 0 high, 0 medium, 2 low.** The remaining findings concern malformed section-boundary comments and residual clerical spacing. No substantive discrepancy was found in the term's 99 current adjudications or the three candidate trackers. The nine findings in the preceding audit have been resolved at their identified current locations; additional locations of clerical defects are listed here. Neither low-severity finding is waived merely because it leaves the adjudications intact.

This pass replaces only this audit. No adjudication, approved brief, candidate, runtime, freeze, entering-law slice, workspace projection, Render Input, public render, foundation file, or tool was corrected. No Git command was run. The operator retains verification and commitment. Close should return for correction of F01 and F02 before a clean Audit result and coordinated Commit.

Severity describes effect: high would undermine an adjudication or identification of operative law; medium would misstate a reusable rule or controlling authority in a current derivative; low identifies an actual clerical, attribution, navigation, status, or presentation defect without an established change in operative law. Repeated copies of the same marker-generation defect constitute one finding, not 119 separate findings.

## Scope, sequence, and limits

The repository instructions, Engine, Render Contract, and Composition were read before validation; the tracker instructions were also consulted. The first validator executed was the unchanged `tools/check_term.py` main with argument `OT1994`. Because that program normally invokes `git cat-file`, a scratch Python launcher intercepted only that lookup and answered it through a read-only Git-object reader. The unchanged validator otherwise executed normally, including its Python checks. No Git executable was invoked, directly or indirectly, and the repository scripts were not edited.

That first run exited **0**: `OK: OT1994; 58 warning(s)`. All 58 warnings were inspected as overly broad hexadecimal-token matches in source identifiers, URLs, or ordinary text rather than missing claimed commits. Examples include `A40385013`, `1662045`, and `cceeded`. Genuine commit references were checked separately against the actual object database. These warnings are not 58 unresolved provenance findings.

The requested deterministic gate completed before the fresh legal review: inventory coverage, dates, participation and component arithmetic, regenerated-split freshness, Public Projection identity, local links and anchors, actual commit objects, staged-close cleanup, and open-matter continuity. The later supplementary comment-balance inspection discovered F01, which the stock freshness check does not test. Thus an initially successful deterministic gate is not represented as proof that every internal formatting invariant passed.

The fresh legal audit was conducted in this context, not delegated and not represented as a new blind Run. It reviewed all 99 matters at the judgment, opinion, proposition, remedy, and continuity levels; all 236 controlling holding blocks and their authority; the term's explicit historical-departure accounts; the corresponding public entries; both Holdings-pass contributions; the changed/new Standards entries against their Record sources; and the complete Standing State candidate. The six specifically identified matters received additional internal commitment, reconciliation, compatibility, assignment, and provenance review. The preceding audit was consulted after the initial independent matter review to test whether its nine findings remained outstanding.

Records and admitted sources controlled the review. Historical outcomes did not displace this timeline's law, and neither Stone-only reasoning nor agreement in a judgment was treated as a rationale join. The review checked the legal sufficiency and consistency of the recorded explanations; it did not rerun adjudication or invent new Justice choices. It does not claim fresh full-page rereading or downloading of every petition, merits brief, appendix, and historical opinion, or live testing of every external URL. Preserved source limitations are identified below rather than treated as newly resolved research.

## Unresolved findings

### F01 — Low — Generated section comments mislabel and fail to close the sections they accompany

The approved nine chunk briefs have balanced `BEGIN_SECTION` / `END_SECTION` comments. Their generated derivatives do not. `tools/split_chunk.py`, in `split_case`, copies the pre-Section-I header—including `<!-- BEGIN_SECTION I -->`—into all three outputs. It then slices at the visible `### SECTION` headings, retaining comments belonging to the next section. Consequently:

- A neutral split can finish a case's neutral text with an unclosed `BEGIN_SECTION II`.
- A Stone split can begin with `BEGIN_SECTION I`, display `SECTION II`, close `END_SECTION II` without a matching begin, and leave `BEGIN_SECTION III` open.
- A comparator split can carry `BEGIN_SECTION I` above `SECTION III` and an unmatched `END_SECTION III`.

This affects **all 27 standard chunk splits**, **64 additional scoped/derived runtime files**, **20 current Records containing copied Stone supplements**, and **8 preserved freeze files**: **119 files containing the malformed comments** in the inspected runtime/record/freeze/entering-law trees. The complete affected-file register follows at the end of this report. No affected entering-law file was found by this marker check.

Concrete examples are [chunk 5 Stone runtime](../runtime/OT_1994CHUNK5_STONE.md), lines 9, 11, 60 and 62, and the [Stone v. INS Record](../records/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md), lines 26, 28, 77 and 79. In the Record the unmatched `BEGIN_SECTION III` immediately precedes the internal public-action section, although that section is not the historical comparator. The comparator and neutral versions exhibit the corresponding errors described above. The visible Section II text remains Stone's actual supplement.

**Effect and bounds:** This is a real internal labeling/boundary discrepancy. The current splitter and freshness validator use the visible headings, so their exact-byte comparison passes while reproducing malformed comments. Inspection found no substantive Stone/comparator text crossing the visible standard split boundaries because of this bug. The bounded Public Projections, generated Render Inputs, and public renders do not inherit these internal supplement markers. No vote, holding, remedy, or historical departure changes as a result. F01 is therefore low severity, not a finding that the Run's physical contexts received forbidden substantive material.

**Separate correction needed:** Repair the mechanical boundary handling and reconcile the affected current derivatives and embedded Record comments without altering approved words. Preserved historical freeze material requires truthful correction annotation or other authorized provenance treatment; this report does not direct silent rewriting of old commitments. Regeneration alone with the present splitter will reproduce the defect. No such repair was made during this audit.

### F02 — Low — Residual spacing defects remain in current Record text and the Holdings candidate

The previously reported punctuation locations were repaired, but the final scan found these additional current locations. They are clerical defects, not new rules or vote discrepancies:

| Current location | Defect |
|---|---|
| `records/First_Options_of_Chicago_Inc_v_Kaplan_merits_1995-05-22.md:2` | Event header ends `OT1994,chunk6.` |
| `records/Kelley_v_Board_of_Trustees_of_the_University_of_Illinois_merits_1995-05-22.md:2` | Same compressed event-header text. |
| `records/Nebraska_v_Wyoming_original_exceptions_1995-05-30.md:2` | Same compressed event-header text. |
| `records/Wilson_v_Arkansas_merits_1995-05-22.md:2` | Same compressed event-header text. |
| `records/Nebraska_v_Wyoming_original_exceptions_1995-05-30.md:311` | Missing separators/spaces in the source paragraph, including `Apps.C-E,supplies`, `November25,1994,supply`, `objections;Government`, `Nebraska1945,1953,April20,1993`, and `finding,Glendo`. These are current source-description prose, outside an embedded approved Stone quotation and outside the bounded Public Projection. |
| `close/HOLDINGS.candidate.md:3683,3684` | `Williams,May` and `Escondido,April` in the precedent citations. |
| `close/HOLDINGS.candidate.md:6727,6741` | `Collins,January` in the Graham and Herrera citations. |
| `close/HOLDINGS.candidate.md:13656` | `Atchison,Topeka` in the Arizona Grocery case name. |
| `close/HOLDINGS.candidate.md:18745,18757` | `Services,June` and `States,December` in the Eastman Kodak and Griffin citations. |

The seven candidate lines are inherited citation typography, not substantive changes introduced by OT1994. Their inherited origin does not remove them from the requested candidate audit. No incorrect citation identity, proposition, or date is inferred merely from the missing space. These defects do not occur in the affected Records' Public Projections and do not change their matching inputs or renders.

The scan distinguished current prose from expressly incorporated immutable handoffs. Compressed wording and literal extraction characters inside the identified historical Aguilar and Rosenberger freeze reproductions were not silently reclassified as newly authored current law or a new adjudication. This finding calls for clerical treatment of the listed current prose/candidate locations in a separate task, not rewriting approved quotations or old freezes.

## Deterministic findings and chronology

| Check | Result and evidence |
|---|---|
| Inventory → manifest → Record → input → render | All **99** inventory matters occur once in the manifest, have their current natural-key Record, and appear once in the appropriate Render Input and public chunk entry. Consolidated captions resolve by docket and date. There are **107 inventory dockets**, **41 event dates**, and nine chunks: 12 entries each in chunks 1–8 and three in chunk 9. |
| Record completeness | **101** Records: 99 scheduled adjudicative events plus two admitted noncase changes. All have distinct ledger references; no extra operative correction Record or duplicate completed event was found. The 99 events comprise 94 merits decisions, three decisions designated per curiam after merits submission, and two original exceptions proceedings. |
| Admitted sources | The Vaccine Injury Table change is effective **March 10, 1995** and follows petition date, preserving both the old Table and qualifications for Whitecotton. The Plant Variety Protection Act amendments are effective **April 4, 1995**, preserving qualifying earlier certificates/applications and the actual refiling, notice, and contract-producer qualifications. Neither is falsely counted as a Supreme Court merits holding or missing public merits entry. |
| Effective-date order | Manifest and chunk event order agree with Record dates. Corrections retain the original event dates. Effective-law refreshes distinguish same-day peers from earlier law; the express Pinette-to-Chabad coordination is preserved. Johnson is not silently made earlier law for Kimberlin. Ledger preservation order is not misrepresented as effective-law order. |
| Participation and arithmetic | Named judgment and rationale support, author/joins, judgment-only positions, partial joins, and nonparticipants were reconciled. The ordinary table parser checked 131 rows; combined/narrative forms were read separately. NTEU's unanimous nonparty remedy and Evans's **6–1–2** disposition were resolved manually, not treated as parser failures. |
| Nonparticipation | Ginsburg is excluded in FEC; Scalia in Wolens; Stevens and Breyer in Grubart; Breyer in City of Milwaukee, Wilton, and Sky Reefer. Reduced-Court denominators and direct rationale majorities are correct. No predecessor's vote is assigned to Breyer. |
| Runtime freshness | All **27** standard `_NEUTRAL`, `_STONE`, and `_COMPARATOR` outputs match what the current splitter produces from the approved briefs. Completion/replacement handoffs govern the corrected matters. Exact freshness does not cure the separate malformed-comment defect in F01. |
| Public Projection → Render Input | All **99** bounded eleven-block projections agree with their generated input entries. No independent rewrite or stale public projection was found. |
| Public render | All 99 entries have the correct event identifiers, dates, end boundaries, and required structure. **71 full / 28 compact** forms follow the designated forms. All full entries have judgment and topology tables. The controlling explanations run **138–185 words** in their Record blocks, within the 120–200-word requirement. |
| Explanation fidelity | Of 236 controlling explanations, **233** match the render after normalization. The three wording changes were individually compared: Anderson v. Edwards makes a same-entry exception pointer explicit; Celotex removes the word “supplied”; Sweet Home explains “scienter” as required knowledge or intent. None changes the rule, adopted reasoning, or reservation. |
| Links and anchors | **12,259** local/repository-main link occurrences resolve. **188** prospective links to new `state/HOLDINGS.md` anchors resolve in the candidate and are proper pending coordinated publication. No broken local target or anchor was found. External source links were inventoried, not all live-tested. |
| Commit references | Every genuine cited commit resolves to a commit object. The three distinct hashes and the two specifically requested correction comparisons are described below. File digests and source identifiers are not treated as commits. |
| Staged cleanup | `close/` contains the three candidates, two Holdings pass notes, one Standards pass note, this audit, and `.gitkeep`. Candidates and pass notes properly remain before Commit. No premature final dossier or generated close index was used as authority. Their later deletion/publication remains a Commit task. |
| Open matters | All 99 scheduled events are completed; no scheduled matter is silently stopped or omitted. Completion of an exceptions event is distinguished from closure of the original action. Nine genuinely open matters are carried to Standing State, described below. |

The current ledger candidly leaves first-record hashes unverified where the operator forbade Git. Direct read-only inspection nevertheless confirms that all 101 Record paths exist in the current HEAD tree. This is corroboration of preservation, not an invented first-commit chronology or a claim that the operator has committed this audit.

## Six corrected matters and current-version checks

| Matter | Current adjudication and consistency result |
|---|---|
| Interstate Commerce Commission v. Transcon Lines | The current Record, input, and compact render agree on **9–0 reversal and a confined implementation remand**, with Kennedy writing for all nine. The express public enforcement route, original-notice omission, late revised billing measured from authorized-credit expiration, prohibited aggregation, and conceded loss-of-discount class are retained. Ordinary freight principal is not cancelled; genuine inclusion, amount, and scope questions beyond the concessions remain. The prior open-proof preparation is stage history, not a competing completed decision. |
| Fargo Women's Health Organization v. Schafer | All three public representations agree on the **six-vote access vacatur/remand**, **eight-vote definition/enforcement affirmances**, and their separate grounds. Stone joins access relief and dissents from the affirmances; he does not acquire a rationale through fallback. Actual Casey's full six-step framework governs rather than a freestanding historical large-fraction gate. Purposeful termination, emergency intelligibility versus substantive health adequacy, Title 12.1's limited reach, distinct civil/criminal rules, and prompt but nonautomatic interim consideration remain explicit. No historical Supreme Court merits poll is invented. |
| O'Neal v. McAninch | The current Section II replacement, completion Record, generated input, and full render agree. **Seven** vote to vacate; **five**—Stone, O'Connor, Souter, Ginsburg, Breyer—adopt Chapman for the preserved personal-intent instructional/argument claim. Only Stone, O'Connor, and Souter support the broader extension. Stevens/Kennedy's Kotteakos judgment concurrence and Scalia/Thomas's affirmance dissent are not converted into Chapman joins. The conditional writ/retrial mandate does not decide that constitutional error occurred or order immediate release. The earlier unadjudicated preparation is not current law. |
| United States v. Robertson | The current Record, input, completed chunk-5 render, manifest, ledger, and final workspace agree on **9–0 reversal**, Breyer for the Court, and the cumulative direct-enterprise commerce ground. Actual inputs, interstate workers, and carried mine output remain the basis; procurement alone is not an independently sufficient adopted holding. Count VI reinstatement remains subject to six reserved appellate claims, and the independent drug-count Rule 32 resentencing posture is preserved. The exposed chunk-5 aggregates now expressly identify completion and supersession of their earlier nonadjudication description. |
| California Department of Corrections v. Morales | The revised-position replacement is consistently **5–4 affirmance**, O'Connor for Stone, Stevens, Souter, and Ginsburg, with Kennedy's four-Justice dissent. Relief preserves offense-date annual consideration, not release. The narrower Court rule remains distinct from Stone's complete enforceable-substitute concurrence; claimant ultimate proof and State substantiation of an asserted substitute are not reversed. O'Connor's own Cavanaugh opinion and Ginsburg's published Cavanaugh position supply the Justice-specific departure premises. The original reversal is retained only as superseded phase history; current law, both candidates, workspace, input, and render use the replacement. |
| Stone v. Immigration and Naturalization Service | The current adjudication remains **5–4**, Kennedy for Stevens, Scalia, Thomas, and Ginsburg; Stone joins Breyer's dissent with O'Connor and Souter. The corrected internal assignment paragraph gives **Stevens**, as senior member of the majority, assignment authority and explains Kennedy's selection without pretending that the Chief assigned while dissenting. The public projection is unchanged by the assignment correction and agrees with the input and render. The separate original-order and reconsideration review objects, mandatory consolidation when both are pending, and nonreach of immigration merits remain intact. F01 separately affects this Record's embedded supplement comments, not its assignment or public adjudication. |

There is one operative natural-key Record, one current generated entry, and one public entry for each of these six matters. No competing stale **operative adjudication** was found. Earlier neutral packets, provisional commitments, original freezes, approved source briefs, and dated opening snapshots still exist. Their retained older text is provenance, not an assurance that every historical file contains the latest result. Current supersession/completion notices and Record boundaries identify the controlling versions. This audit does not request erasing that history.

### Concise Git provenance

The object reader verified SHA-1 identity/type and read the relevant commit trees and parent versions directly:

- `13b19ee463d16fb4377d846e5b058599f886bed3`: the pinned prior Standing State source exists and supports the preserved referral-practice reference.
- `d086219b424d812aaa837fda9533629c69e33833`: the Morales replacement commit contains the substantive revised adjudication. Its Public Projection differs from the parent and matches the current projection. The subsequent current-file difference is concise lineage identifying the preserved correction, not another legal change.
- `8d98261d33b6d39fda8a9ccc52ab5ad7ed3be02a`: the Stone v. INS assignment correction changes the internal assignment explanation. The Public Projection is identical before and after that correction and matches the current one. The subsequent current-file difference records concise lineage.

Transcon, Fargo, O'Neal, and Robertson describe completion of previously unadjudicated preparations rather than claiming invented predecessor adjudications or unsupported hashes. Those distinctions were respected. No narrative commit archaeology was required or performed.

## Candidate trackers and continuity

**Holdings, both passes.** The completed candidate includes all **236** OT1994 controlling propositions: **154** from the first 60 matters and **82** from the remaining 39, in **127 area-specific case placements** covering all 99 Record identities. All 236 rules are present; 235 match the Record after ordinary normalization, and Clearwater's one editorial removal of the directional word “below” does not change its specifically named provisions. Authorities, remedies, qualifications, and material precedent treatment were checked at their actual component scope. The candidate need not reproduce every opinion's explanation; its template calls for the exact proposition and durable limits.

The four independently sufficient alternative blocks in pass 1 and Sweet Home's separate Chevron alternative remain independently attributed. A judgment concurrence supplies no missing Court rationale. In particular, Gustafson has no controlling public-offering-only rule; Guernsey has no five-Justice deference methodology; Day has no controlling financing framework; Williams's taxpayer alternative has only its own five joins; Chandris's temporal guide has five rather than six; Witte's constitutional and coordination coalitions differ; Pinette's general attribution approach has four; Chabad's additional remedial inquiry has four; Miller's conditional statutory-defense discussion is not a holding. Earlier Brecht and Cavanaugh receive bounded later-authority treatment without replacing their original holdings. Hewitt's limited treatment, Sinclair's partial overruling, Bramblett's displaced construction, and the retained Grady, Metro/Fullilove, Shaw, and Lemon premises remain consistent with the operative Records.

**Standards and Tests.** The candidate has **370 entries**, compared with 289 in the opening register. Its 86 newly titled entries and five displaced/renamed titles produce the net increase of 81; apparent additional textual changes include whitespace and section-boundary changes as well as revised entries. The changed/new rules, conditions, burdens, authority, limits, and transitions were compared against the Records, not inferred merely from inclusion in Holdings. No substantive discrepancy remains. Rambo now attaches the one-year period to seeking/reviewing modification. Witte states subsection (a)'s priority before (b) and (c). Morales preserves ultimate claimant proof, the bounded substantiation rule, and the separate concurrence. Fargo preserves permission versus obligation and the separate statutory predicates. The Asgrow and Vaccine transitions follow the admitted sources rather than dates of later adjudication. The private Aguilar fallback wording has been removed from the register while its eight-rationale/one-judgment distinction remains.

**Standing State.** The opening-OT1995 roster, seniority, offices, dates, and all thirteen circuit allotments agree with Composition. The referral practice is carried unchanged. The candidate contains the Court setting and docket, not a positions register or a history/dependency ledger. Nine matters remain open: Zatko and its companion petitions; Wyoming v. Oklahoma; Reynolds; Grubbs; United States v. Louisiana; Delaware v. New York; Nebraska v. Wyoming; In re Anderson; and Kansas v. Colorado. Nebraska's pleading event is completed while the original action remains before the Master; Kansas's liability exceptions are completed while remedy remains before the Master. No release, termination, vacatur, or resolution of an inherited application is invented.

The ten recorded user-added OT1995 matters are retained separately as docket additions, including the expressly unidentified A. St. P. C. matter and Bush's reconstructed posture. Their missing identification/lower judgment is stated; no merits facts or adjudication are invented. These are acknowledged prerequisites to future work, not unresolved adjudications among OT1994's 99 events. This audit does not claim a separately existing OT1995 case-list or independently recovered authorization history beyond the recorded additions.

The three candidate publication fields intentionally retain the synchronized OT1993 cutoff pending Commit. The Standing State's distinct opening-OT1995 label identifies the setting it stages. Neither fact is a stale-publication discrepancy. Current `state/` remains the opening baseline and was not overwritten.

**Current workspace.** All 236 complete operative rules are present in both continuity and the sanitized neutral projection. The previously stale Nebraska Fourth Cross-Claim authority now excludes Thomas from that eight-Justice leave vote while retaining the unanimous other leave directions. The complete Witte sequence and Hurley's cable context are propagated. Published noncontrolling positions remain available as positions rather than being promoted into law. No hidden stopped-matter status or invented terminal event was found.

**Historical departures and source limits.** The audit inspected all 53 explicit departure lines across 43 Records together with the relevant coalition/scope accounts. Chief-specific changes remain distinct from associate changes. The significant changed-law chains include Brecht → O'Neal → Kyles; Cavanaugh → Morales; Morgan Stanley → Plaut; Dixon/Grady → Witte; operative Shaw/Adarand → Miller; and procedural-only Zobrest → Rosenberger. Reconciliation withdrawals of unsupported provisional departures in Stone v. INS, Robertson, Guernsey, and O'Neal are not treated as new adjudications. The restored historical alignment is evidence weighed against each Justice's actual sources, not a command to copy history. No specific later historical matter is expressly displaced by an unindexed consequence finding; no invented Consequence line is required.

Clearwater's source subsection-label issue, Sweet Home's unresolved exact §6(g)(2) application, the plant-amendment text's awkward contract-producer clause, and other expressly unadjudicated applications remain bounded limitations. They are not silently filled in, treated as automatic injunctions or exemptions, or promoted into new rules. A reservation necessary for a future different application is not itself a stopped completed event.

## Resolution of the preceding audit's findings

| Previous finding | Current verification |
|---|---|
| F01 — Rambo timing | Correct actor/timing relationship in the current Standards rule; no condition-occurrence window substituted. |
| F02 — Nebraska workspace coalition | Both live workspace copies preserve nine-Justice other leave directions and eight-Justice Fourth Cross-Claim leave. |
| F03 — Witte workspace qualification | Both live copies carry subsection (a)'s trigger and priority, then (b), then (c). |
| F04 — Hurley cable description | Both live workspace copies now say cable context/results. |
| F05 — Chunk-5 status | Both current aggregate headers point to completed Robertson and the revised Morales Record/commit, expressly labeling older phase descriptions superseded. |
| F06 — Gustafson/Evans status | Current Records state completion and chronology clearance; ledger lineage agrees. Operator commitment remains a separate responsibility. |
| F07 — Kimberlin attribution | Current Record and identified commitment/reconciliation copies describe O'Connor as joining Scalia's Anderson opinion. The Record identifies the correction; the substantive join remains supported. |
| F08 — Aguilar private provenance | Standards retains the public rationale/judgment distinction and no longer uses the private standing-fallback description. |
| F09 — Clerical text | The identified current Brown citation, Fargo apostrophes/runtime pointers, four Record bodies, and live workspace/ledger spacing have been corrected. Old reading snapshots do not become competing current adjudications merely by preserving older typography. |

None of those nine findings is carried forward as unresolved. F01 in **this** report is a newly identified marker defect and must not be confused with the previous report's Rambo finding.

## All-matter legal coverage register

Each row records the principal issue checked in addition to the common vote, authority, scope, remedy, and projection checks. Finding references identify internal clerical defects; they do not qualify the substantive consistency result. F02 also covers the seven prior-term citation lines retained in the Holdings candidate.

| No. | Matter | Principal legal/continuity check | Current result |
|---:|---|---|---|
| 1 | [United States v. Shabani](../records/United_States_v_Shabani_merits_1994-11-01.md) | Section 846 agreement and knowing participation; reserved sufficiency claims. | Consistent |
| 2 | [U.S. Bancorp Mortgage Co. v. Bonner Mall Partnership](../records/US_Bancorp_Mortgage_Co_v_Bonner_Mall_Partnership_mootness_vacatur_1994-11-08.md) | Post-mootness dispositional power and settlement-caused vacatur discretion kept distinct. | Consistent |
| 3 | [Hess v. Port Authority Trans-Hudson Corp.](../records/Hess_v_Port_Authority_Trans_Hudson_Corp_merits_1994-11-14.md) | Entity identity, limited state appropriations, and no treasury-only immunity rule. | Consistent |
| 4 | [United States v. X-Citement Video, Inc.](../records/United_States_v_X_Citement_Video_Inc_merits_1994-11-29.md) | Factual knowledge, alternative-ground reach, and separate six-Justice definition holdings. | Consistent |
| 5 | [Church of Scientology Flag Service Organization, Inc. v. City of Clearwater +](../records/Church_of_Scientology_Flag_Service_Organization_Inc_v_City_of_Clearwater_merits_1994-12-05.md) | Bounded RFRA remand, retained constitutional questions, and provision-specific limits. | Consistent |
| 6 | [Federal Election Commission v. NRA Political Victory Fund](../records/Federal_Election_Commission_v_NRA_Political_Victory_Fund_jurisdictional_dismissal_1994-12-06.md) | Agency litigation authority, timely ratification, and eight-member participation. | Consistent |
| 7 | [Reich v. Collins](../records/Reich_v_Collins_merits_1994-12-06.md) | Held-out refund remedy cannot be withdrawn after payment. | Consistent |
| 8 | [Brown v. Gardner](../records/Brown_v_Gardner_merits_1994-12-12.md) | Section 1151 causation without provider fault; no automatic benefits award. | Consistent |
| 9 | [Nebraska Department of Revenue v. Loewenstein](../records/Nebraska_Department_of_Revenue_v_Loewenstein_merits_1994-12-12.md) | Private repo return distinguished from protected federal interest. | Consistent |
| 10 | [In re Baby K +](../records/In_re_Baby_K_merits_1994-12-12.md) | Stabilization, lawful transfer, and the two distinct informed-refusal routes. | Consistent |
| 11 | [Plakas v. Drinski +](../records/Plakas_v_Drinski_merits_1995-01-09.md) | Reasonableness and county judgment; no general duty to choose less force first. | Consistent |
| 12 | [Interstate Commerce Commission v. Transcon Lines](../records/Interstate_Commerce_Commission_v_Transcon_Lines_merits_1995-01-10.md) | Express ICC enforcement, conceded penalty defects, and confined implementation. | Consistent |
| 13 | [Tome v. United States](../records/Tome_v_United_States_merits_1995-01-10.md) | Premotive statements, alternative evidence grounds, and conditional harmlessness review. | Consistent |
| 14 | [Young v. Northern Illinois Conference of United Methodist Church +](../records/Young_v_Northern_Illinois_Conference_merits_1995-01-17.md) | Ministerial-selection defense is substantive rather than jurisdictional. | Consistent |
| 15 | [Asgrow Seed Co. v. Winterboer](../records/Asgrow_Seed_Co_v_Winterboer_merits_1995-01-18.md) | Own-planting saved seed, notice, and preserved former-law transition. | Consistent |
| 16 | [United States v. Mezzanatto](../records/United_States_v_Mezzanatto_merits_1995-01-18.md) | Personal-testimony impeachment waiver; Stone's separate proof allocation. | Consistent |
| 17 | [American Airlines, Inc. v. Wolens](../records/American_Airlines_Inc_v_Wolens_merits_1995-01-18.md) | Consumer-fraud preemption versus enforcement of actual airline undertakings. | Consistent |
| 18 | [NationsBank of North Carolina, N.A. v. Variable Annuity Life Insurance Co. / Ludwig v. Variable Annuity Life Insurance Co.](../records/NationsBank_Ludwig_v_Variable_Annuity_Life_Insurance_Co_merits_1995-01-18.md) | Annuity brokerage permission, real statutory limits, and eight-rationale coalition. | Consistent |
| 19 | [Allied-Bruce Terminix Cos. v. Dobson](../records/Allied_Bruce_Terminix_Cos_v_Dobson_merits_1995-01-18.md) | Actual commerce, state-court enforcement, and independent contract defenses. | Consistent |
| 20 | [Schlup v. Delo](../records/Schlup_v_Delo_merits_1995-01-23.md) | Crime-innocence gateway, all probative evidence, and qualified statutory refusal. | Consistent |
| 21 | [McKennon v. Nashville Banner Publishing Co.](../records/McKennon_v_Nashville_Banner_Publishing_Co_merits_1995-01-23.md) | After-acquired misconduct affects remedies only on the employer's actual-discharge showing. | Consistent |
| 22 | [Fargo Women’s Health Organization v. Schafer +](../records/Fargo_Womens_Health_Organization_v_Schafer_merits_1995-02-13.md) | Actual Casey access review separated from definitions, penalty rules, and interim relief. | Consistent |
| 23 | [Lebron v. National Railroad Passenger Corp.](../records/Lebron_v_National_Railroad_Passenger_Corp_merits_1995-02-21.md) | Governmental status, prudential reach, and merits-remand limits. | Consistent |
| 24 | [Milwaukee Brewery Workers' Pension Plan v. Jos. Schlitz Brewing Co.](../records/Milwaukee_Brewery_Workers_Pension_Plan_v_Jos_Schlitz_Brewing_Co_merits_1995-02-21.md) | Withdrawal-liability amortization assumption distinct from demand and default interest. | Consistent |
| 25 | [O'Neal v. McAninch](../records/ONeal_v_McAninch_merits_1995-02-21.md) | Seven-vote vacatur versus five-vote instructional Chapman rule and three-vote broader proposal. | Consistent |
| 26 | [United States v. National Treasury Employees Union](../records/United_States_v_National_Treasury_Employees_Union_merits_1995-02-22.md) | Prospective expression burden and distinct class, named-party, and nonparty remedies. | Consistent |
| 27 | [Harris v. Alabama](../records/Harris_v_Alabama_merits_1995-02-22.md) | Unanimous no-numerical-weight rule versus the seven-Justice actual-record judgment. | Consistent |
| 28 | [Jerome B. Grubart, Inc. v. Great Lakes Dredge & Dock Co. / City of Chicago v. Great Lakes Dredge & Dock Co.](../records/Jerome_B_Grubart_Inc_v_Great_Lakes_Dredge_Dock_Co_merits_1995-02-22.md) | Admiralty locality/connection; five direct joins on a seven-member Court. | Consistent |
| 29 | [Anderson v. Green](../records/Anderson_v_Green_decision_1995-02-22.md) | Ripeness after approval removal and equitable clearing of unreviewable preliminary judgments. | Consistent |
| 30 | [Gustafson v. Alloyd Co.](../records/Gustafson_v_Alloyd_Co_merits_1995-02-28.md) | Five-Justice acquisition-contract rule; broader offering-only position remains four. | Consistent |
| 31 | [Arizona v. Evans](../records/Arizona_v_Evans_merits_1995-03-01.md) | Seven jurisdiction votes, six merits votes, one affirmance, two dismissals. | Consistent |
| 32 | [Swint v. Chambers County Commission](../records/Swint_v_Chambers_County_Commission_merits_1995-03-01.md) | Legal collateral-order boundaries and independent tentative-ruling ground. | Consistent |
| 33 | [Mastrobuono v. Shearson Lehman Hutton, Inc.](../records/Mastrobuono_v_Shearson_Lehman_Hutton_Inc_merits_1995-03-06.md) | Contractual choice-of-law/arbitration interpretation; no universal punitive-award permission. | Consistent |
| 34 | [Curtiss-Wright Corp. v. Schoonejongen](../records/Curtiss_Wright_Corp_v_Schoonejongen_merits_1995-03-06.md) | Adequate amendment procedure versus actual corporate authorization or ratification. | Consistent |
| 35 | [Shalala v. Guernsey Memorial Hospital](../records/Shalala_v_Guernsey_Memorial_Hospital_merits_1995-03-06.md) | Five-Justice accounting construction versus four-Justice deference methodology. | Consistent |
| 36 | [Ambassador Books & Video, Inc. v. City of Little Rock +](../records/Ambassador_Books_Video_Inc_v_City_of_Little_Rock_merits_1995-03-20.md) | Adult-business definitions, location proof, practical alternatives, and bounded relief. | Consistent |
| 37 | [Director, Office of Workers’ Compensation Programs v. Newport News Shipbuilding & Dry Dock Co.](../records/Director_Office_of_Workers_Compensation_Programs_v_Newport_News_Shipbuilding_and_Dry_Dock_Co_merits_1995-03-21.md) | Administrator aggrievement requires more than general statutory-administration interest. | Consistent |
| 38 | [Anderson v. Edwards](../records/Anderson_v_Edwards_merits_1995-03-22.md) | AFDC grouping, mandatory membership, availability, and distinct proration/disregard rules. | Consistent |
| 39 | [Swanner v. Anchorage Equal Rights Commission +](../records/Swanner_v_Anchorage_Equal_Rights_Commission_merits_1995-03-27.md) | RFRA person-specific burden/justification; commercial participation is not forfeiture. | Consistent |
| 40 | [Qualitex Co. v. Jacobson Products Co.](../records/Qualitex_Co_v_Jacobson_Products_Co_merits_1995-03-28.md) | Source-identifying color, secondary meaning, and independent functionality. | Consistent |
| 41 | [Oklahoma Tax Commission v. Jefferson Lines, Inc.](../records/Oklahoma_Tax_Commission_v_Jefferson_Lines_Inc_merits_1995-04-03.md) | Local ticket-sale tax and full-price measure distinguished from carrier gross receipts. | Consistent |
| 42 | [Plaut v. Spendthrift Farm, Inc.](../records/Plaut_v_Spendthrift_Farm_Inc_merits_1995-04-18.md) | Existing Morgan Stanley private-final-judgment rule; no absolute finality extension. | Consistent |
| 43 | [Shalala v. Whitecotton](../records/Shalala_v_Whitecotton_merits_1995-04-18.md) | Table onset, entitlement, unrelated-factor rebuttal, and petition-date preserved law. | Consistent |
| 44 | [Freightliner Corp. v. Myrick](../records/Freightliner_Corp_v_Myrick_merits_1995-04-18.md) | Actual operative federal standard or conflict; invalidation is not a no-regulation policy. | Consistent |
| 45 | [Heintz v. Jenkins](../records/Heintz_v_Jenkins_merits_1995-04-18.md) | Regular attorney debt collection and separate coverage, communication, and defense conditions. | Consistent |
| 46 | [Lanphere & Urbaniak v. Colorado +](../records/Lanphere_and_Urbaniak_v_Colorado_merits_1995-04-18.md) | Speech-selected records access, advancement/fit, and independent tailoring ground. | Consistent |
| 47 | [Celotex Corp. v. Edwards](../records/Celotex_Corp_v_Edwards_merits_1995-04-19.md) | Actual relatedness, interim authority, review routes, and qualified order-obedience limits. | Consistent |
| 48 | [McIntyre v. Ohio Elections Commission](../records/McIntyre_v_Ohio_Elections_Commission_merits_1995-04-19.md) | Anonymous individual political leaflets; no universal campaign-disclosure rule. | Consistent |
| 49 | [Stone v. Immigration and Naturalization Service](../records/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md) | Separate finality periods; Stevens's assignment authority while Stone dissents. | Substantively consistent; F01 markup only |
| 50 | [Kyles v. Whitley](../records/Kyles_v_Whitley_merits_1995-04-19.md) | Collective Brady materiality, investigating-team duty, and no duplicative prejudice inquiry. | Substantively consistent; F01 markup only |
| 51 | [Rubin v. Coors Brewing Co.](../records/Rubin_v_Coors_Brewing_Co_merits_1995-04-19.md) | Inconsistent alcohol-content restrictions and independent advancement/fit grounds. | Substantively consistent; F01 markup only |
| 52 | [California Department of Corrections v. Morales](../records/California_Department_of_Corrections_v_Morales_merits_1995-04-25.md) | Meaningful annual consideration, source substantiation, and claimant ultimate proof. | Consistent |
| 53 | [United States v. Williams](../records/United_States_v_Williams_merits_1995-04-25.md) | Seven-vote refund waiver and separate five-vote taxpayer-definition alternative. | Substantively consistent; F01 markup only |
| 54 | [United States v. Lopez](../records/United_States_v_Lopez_merits_1995-04-26.md) | Bounded school-zone commerce failure; Chief's six-route framework not adopted. | Substantively consistent; F01 markup only |
| 55 | [New York State Conference of Blue Cross & Blue Shield Plans v. Travelers Insurance Co. / Pataki v. Travelers Insurance Co. / Hospital Association of New York State v. Travelers Insurance Co.](../records/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md) | Indirect insurer/HMO cost effects and precise treatment of unresolved direct-plan relief. | Substantively consistent; F01 markup only |
| 56 | [United States v. Harris +](../records/United_States_v_Harris_merits_1995-04-27.md) | Economic carjacking class, actual statutory nexus, and authorized cumulative punishment. | Substantively consistent; F01 markup only |
| 57 | [United States v. Robertson](../records/United_States_v_Robertson_merits_1995-05-01.md) | Cumulative direct-enterprise interstate conduct and conditional appellate reinstatement. | Consistent |
| 58 | [United States v. Pinson +](../records/United_States_v_Pinson_merits_1995-05-08.md) | Targeted thermal home examination; search, justification, and exclusion remain separate. | Substantively consistent; F01 markup only |
| 59 | [Kansas v. Colorado](../records/Kansas_v_Colorado_original_exceptions_1995-05-15.md) | Compact liability, actual-use accounting, and retained remedy before the Master. | Substantively consistent; F01 markup only |
| 60 | [Hubbard v. United States](../records/Hubbard_v_United_States_merits_1995-05-15.md) | Court-entity construction, Bramblett treatment, and narrower Chief judgment ground. | Substantively consistent; F01 markup only |
| 61 | [City of Edmonds v. Oxford House, Inc.](../records/City_of_Edmonds_v_Oxford_House_merits_1995-05-15.md) | Household composition outside the crowding exemption; no automatic liability. | Consistent |
| 62 | [Reynoldsville Casket Co. v. Hyde](../records/Reynoldsville_Casket_Co_v_Hyde_merits_1995-05-15.md) | Retroactivity versus independent remedial defenses; no disguised prospectivity. | Consistent |
| 63 | [Day v. Holahan +](../records/Day_v_Holahan_merits_1995-05-15.md) | Financing fracture kept separate from three directly supported constitutional holdings. | Consistent |
| 64 | [U.S. Term Limits, Inc. v. Thornton / Bryant v. Hill](../records/US_Term_Limits_v_Thornton_Bryant_v_Hill_merits_1995-05-22.md) | Service-based ballot exclusion adds congressional qualifications in both dockets. | Consistent |
| 65 | [Wilson v. Arkansas](../records/Wilson_v_Arkansas_merits_1995-05-22.md) | Announcement is part of reasonableness, with actual danger/futility/escape/evidence exceptions. | Substantively consistent; F01 and F02 clerical |
| 66 | [First Options of Chicago, Inc. v. Kaplan](../records/First_Options_of_Chicago_Inc_v_Kaplan_merits_1995-05-22.md) | Nine-vote antecedent assent versus eight-vote conditional delegation review. | Substantively consistent; F01 and F02 clerical |
| 67 | [Kelley v. Board of Trustees of the University of Illinois +](../records/Kelley_v_Board_of_Trustees_of_the_University_of_Illinois_merits_1995-05-22.md) | Alternative Title IX accommodation routes and independent equal-protection review. | Substantively consistent; F01 and F02 clerical |
| 68 | [Nebraska v. Wyoming](../records/Nebraska_v_Wyoming_original_exceptions_1995-05-30.md) | Enforcement/modification distinction and Thomas's Fourth Cross-Claim dissent. | Substantively consistent; F01 and F02 clerical |
| 69 | [North Star Steel Co. v. Thomas / Crown Cork & Seal Co., Inc. v. United Steelworkers of America, AFL-CIO-CLC](../records/North_Star_Steel_v_Thomas_and_Crown_Cork_merits_1995-05-30.md) | State borrowing and narrow federal exception; no universal state limitations period. | Substantively consistent; F01 markup only |
| 70 | [Garlotte v. Fordice](../records/Garlotte_v_Fordice_merits_1995-05-30.md) | Continuous consecutive custody supports jurisdiction; habeas merits remain open. | Substantively consistent; F01 markup only |
| 71 | [United States v. Wellons +](../records/United_States_v_Wellons_merits_1995-05-30.md) | Vehicle possession and luggage privacy; search justifications and remedy unresolved. | Substantively consistent; F01 markup only |
| 72 | [Reno v. Koray](../records/Reno_v_Koray_merits_1995-06-05.md) | Official detention status, administrative weight, and Chief's separate institutional-restraint view. | Substantively consistent; F01 markup only |
| 73 | [Metropolitan Washington Airports Authority v. Hechinger +](../records/Metropolitan_Washington_Airports_Authority_v_Hechinger_merits_1995-06-05.md) | Congressional-agent execution control and section 2456(h)'s cessation consequence. | Consistent |
| 74 | [Missouri v. Jenkins](../records/Missouri_v_Jenkins_merits_1995-06-12.md) | Violation-linked salary support and complete Freeman withdrawal showing. | Consistent |
| 75 | [Ryder v. United States](../records/Ryder_v_United_States_merits_1995-06-12.md) | Timely appointment challenge and fresh lawful appellate adjudication; no automatic acquittal. | Consistent |
| 76 | [City of Milwaukee v. Cement Division, National Gypsum Co.](../records/City_of_Milwaukee_v_Cement_Division_National_Gypsum_Co_merits_1995-06-12.md) | Compensatory maritime interest; mutual fault and ordinary dispute insufficient to deny it. | Consistent |
| 77 | [Adarand Constructors, Inc. v. Peña](../records/Adarand_Constructors_Inc_v_Pena_merits_1995-06-12.md) | Actual Metro/Fullilove baseline, source-qualified certification, and authorized Chief fallback. | Consistent |
| 78 | [Wilton v. Seven Falls Co.](../records/Wilton_v_Seven_Falls_Co_merits_1995-06-12.md) | Reasoned declaration-only stay, retained jurisdiction, and abuse-of-discretion review. | Consistent |
| 79 | [Metropolitan Stevedore Co. v. Rambo](../records/Metropolitan_Stevedore_Co_v_Rambo_merits_1995-06-12.md) | Economic-capacity modification, section 8(h), and the correct one-year modification period. | Consistent |
| 80 | [Johnson v. Jones](../records/Johnson_v_Jones_merits_1995-06-12.md) | Legal immunity appeals distinguished from factual sufficiency and separate false-arrest disposition. | Consistent |
| 81 | [Kimberlin v. Quinlan](../records/Kimberlin_v_Quinlan_merits_1995-06-12.md) | Categorical direct-evidence screen rejected on common entering law; no invented historical poll. | Consistent |
| 82 | [Commissioner v. Schleier](../records/Commissioner_v_Schleier_merits_1995-06-14.md) | Receipt-specific injury causation; no controlling Burke alternative or categorical health test. | Consistent |
| 83 | [Chandris, Inc. v. Latsis](../records/Chandris_Inc_v_Latsis_merits_1995-06-14.md) | Six-vote connection rule, five-vote temporal guide, and preserved drydock instruction. | Consistent |
| 84 | [Witte v. United States](../records/Witte_v_United_States_merits_1995-06-14.md) | Retained Grady and different constitutional/Guidelines coalitions; (a)/(b)/(c) priority. | Consistent |
| 85 | [Gutierrez de Martinez v. Lamagno](../records/Gutierrez_de_Martinez_v_Lamagno_merits_1995-06-14.md) | Reviewable employment-scope certification; removal conclusiveness remains distinct. | Consistent |
| 86 | [Oklahoma Tax Commission v. Chickasaw Nation](../records/Oklahoma_Tax_Commission_v_Chickasaw_Nation_merits_1995-06-14.md) | Fuel-tax legal incidence and separate off-country-resident income/treaty holding. | Consistent |
| 87 | [Sandin v. Conner](../records/Sandin_v_Conner_merits_1995-06-19.md) | Sufficient nonexclusive state-entitlement rule; separate positive-interest applications. | Consistent |
| 88 | [United States v. Gaudin](../records/United_States_v_Gaudin_merits_1995-06-19.md) | Jury determines criminal materiality when an element; no universal structural-error rule. | Consistent |
| 89 | [Vimar Seguros y Reaseguros, S.A. v. M/V Sky Reefer](../records/Vimar_Seguros_y_Reaseguros_SA_v_MV_Sky_Reefer_merits_1995-06-19.md) | Foreign cargo arbitration, nonwaivable protection, and retained enforcement jurisdiction. | Consistent |
| 90 | [Hurley v. Irish-American Gay, Lesbian and Bisexual Group of Boston](../records/Hurley_v_Irish_American_Gay_Lesbian_and_Bisexual_Group_of_Boston_merits_1995-06-19.md) | Private expressive parade composition; cable analogy properly bounded. | Consistent |
| 91 | [National Private Truck Council, Inc. v. Oklahoma Tax Commission](../records/National_Private_Truck_Council_Inc_v_Oklahoma_Tax_Commission_merits_1995-06-19.md) | Actual adequacy of tax remedies, exceptional equity, and derivative fee limits. | Consistent |
| 92 | [United States v. Aguilar](../records/United_States_v_Aguilar_merits_1995-06-21.md) | Obstruction nexus, interception notice, and separate eight-vote constitutional rationale. | Consistent |
| 93 | [Florida Bar v. Went For It, Inc.](../records/Florida_Bar_v_Went_For_It_Inc_merits_1995-06-21.md) | Actual commercial-speech advancement and fit for both solicitation restrictions. | Consistent |
| 94 | [Vernonia School District 47J v. Acton](../records/Vernonia_School_District_47J_v_Acton_merits_1995-06-26.md) | Athlete-specific testing, prescription limits, written permission versus testified practice. | Consistent |
| 95 | [Rosenberger v. Rector and Visitors of the University of Virginia](../records/Rosenberger_v_Rector_and_Visitors_of_the_University_of_Virginia_merits_1995-06-29.md) | Private printing benefit and actual safeguards under retained Lemon. | Consistent |
| 96 | [Babbitt v. Sweet Home Chapter of Communities for a Great Oregon](../records/Babbitt_v_Sweet_Home_Chapter_of_Communities_for_a_Great_Oregon_merits_1995-06-29.md) | Actual habitat injury, seven statutory/six deference votes, and distinct ESA exceptions. | Consistent |
| 97 | [Miller v. Johnson / Abrams v. Johnson / United States v. Johnson](../records/Miller_and_consolidated_merits_1995-06-29.md) | Reconstructed posture, actual Shaw, accepted predominance, and conditional nonholding. | Substantively consistent; F01 markup only |
| 98 | [Capitol Square Review and Advisory Board v. Pinette](../records/Pinette_merits_1995-06-29.md) | Recurring permit dispute, bounded seven-vote access rule, and four-vote attribution reasoning. | Consistent |
| 99 | [Chabad-Lubavitch of Georgia v. Miller +](../records/Chabad_Lubavitch_v_Miller_merits_1995-06-29.md) | Indoor access, five-vote contextual attribution, and four-vote proposed remedial inquiry. | Substantively consistent; F01 markup only |

## F01 affected-file register

Line numbers identify the first malformed section marker reported in each file; multiple later copies within a file are part of the same finding. The standard split pattern below denotes exactly the 27 files obtained by combining chunks 1–9 with the three suffixes. The additional runtime list excludes those 27 to avoid duplicate counting.

**Standard runtime files (27):** `runtime/OT_1994CHUNK<n>_<kind>.md`, where `<n>` is each of 1–9 and `<kind>` is each of `NEUTRAL`, `STONE`, and `COMPARATOR`. Every one is affected.

### Current Records (20)

| Record | First affected marker line |
|---|---:|
| [Chabad_Lubavitch_v_Miller_merits_1995-06-29.md](../records/Chabad_Lubavitch_v_Miller_merits_1995-06-29.md) | 32 |
| [First_Options_of_Chicago_Inc_v_Kaplan_merits_1995-05-22.md](../records/First_Options_of_Chicago_Inc_v_Kaplan_merits_1995-05-22.md) | 20 |
| [Garlotte_v_Fordice_merits_1995-05-30.md](../records/Garlotte_v_Fordice_merits_1995-05-30.md) | 30 |
| [Hubbard_v_United_States_merits_1995-05-15.md](../records/Hubbard_v_United_States_merits_1995-05-15.md) | 30 |
| [Kansas_v_Colorado_original_exceptions_1995-05-15.md](../records/Kansas_v_Colorado_original_exceptions_1995-05-15.md) | 44 |
| [Kelley_v_Board_of_Trustees_of_the_University_of_Illinois_merits_1995-05-22.md](../records/Kelley_v_Board_of_Trustees_of_the_University_of_Illinois_merits_1995-05-22.md) | 20 |
| [Kyles_v_Whitley_merits_1995-04-19.md](../records/Kyles_v_Whitley_merits_1995-04-19.md) | 26 |
| [Miller_and_consolidated_merits_1995-06-29.md](../records/Miller_and_consolidated_merits_1995-06-29.md) | 30 |
| [Nebraska_v_Wyoming_original_exceptions_1995-05-30.md](../records/Nebraska_v_Wyoming_original_exceptions_1995-05-30.md) | 20 |
| [New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md](../records/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md) | 50 |
| [North_Star_Steel_v_Thomas_and_Crown_Cork_merits_1995-05-30.md](../records/North_Star_Steel_v_Thomas_and_Crown_Cork_merits_1995-05-30.md) | 30 |
| [Reno_v_Koray_merits_1995-06-05.md](../records/Reno_v_Koray_merits_1995-06-05.md) | 30 |
| [Rubin_v_Coors_Brewing_Co_merits_1995-04-19.md](../records/Rubin_v_Coors_Brewing_Co_merits_1995-04-19.md) | 28 |
| [Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md](../records/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md) | 26 |
| [United_States_v_Harris_merits_1995-04-27.md](../records/United_States_v_Harris_merits_1995-04-27.md) | 30 |
| [United_States_v_Lopez_merits_1995-04-26.md](../records/United_States_v_Lopez_merits_1995-04-26.md) | 30 |
| [United_States_v_Pinson_merits_1995-05-08.md](../records/United_States_v_Pinson_merits_1995-05-08.md) | 26 |
| [United_States_v_Wellons_merits_1995-05-30.md](../records/United_States_v_Wellons_merits_1995-05-30.md) | 30 |
| [United_States_v_Williams_merits_1995-04-25.md](../records/United_States_v_Williams_merits_1995-04-25.md) | 24 |
| [Wilson_v_Arkansas_merits_1995-05-22.md](../records/Wilson_v_Arkansas_merits_1995-05-22.md) | 20 |

### Additional runtime copies (64)

These include scoped and preserved-phase transports. Listing them does not make their historical substantive positions current law.

| Runtime file | First affected marker line |
|---|---:|
| [OT_1994CHUNK3_COMPARATOR_A.md](../runtime/OT_1994CHUNK3_COMPARATOR_A.md) | 5 |
| [OT_1994CHUNK3_COMPARATOR_A_READY.md](../runtime/OT_1994CHUNK3_COMPARATOR_A_READY.md) | 5 |
| [OT_1994CHUNK3_COMPARATOR_B.md](../runtime/OT_1994CHUNK3_COMPARATOR_B.md) | 5 |
| [OT_1994CHUNK3_COMPARATOR_C.md](../runtime/OT_1994CHUNK3_COMPARATOR_C.md) | 5 |
| [OT_1994CHUNK3_STONE_A.md](../runtime/OT_1994CHUNK3_STONE_A.md) | 5 |
| [OT_1994CHUNK3_STONE_A_ASSEMBLY.md](../runtime/OT_1994CHUNK3_STONE_A_ASSEMBLY.md) | 5 |
| [OT_1994CHUNK3_STONE_B.md](../runtime/OT_1994CHUNK3_STONE_B.md) | 5 |
| [OT_1994CHUNK3_STONE_B_ASSEMBLY.md](../runtime/OT_1994CHUNK3_STONE_B_ASSEMBLY.md) | 5 |
| [OT_1994CHUNK3_STONE_C.md](../runtime/OT_1994CHUNK3_STONE_C.md) | 5 |
| [OT_1994CHUNK4_COMPARATOR_37_39_40_41.md](../runtime/OT_1994CHUNK4_COMPARATOR_37_39_40_41.md) | 5 |
| [OT_1994CHUNK4_COMPARATOR_38_42_43_44_45.md](../runtime/OT_1994CHUNK4_COMPARATOR_38_42_43_44_45.md) | 5 |
| [OT_1994CHUNK4_COMPARATOR_46_47_48.md](../runtime/OT_1994CHUNK4_COMPARATOR_46_47_48.md) | 5 |
| [OT_1994CHUNK4_STONE_37_39_40.md](../runtime/OT_1994CHUNK4_STONE_37_39_40.md) | 5 |
| [OT_1994CHUNK4_STONE_38_47.md](../runtime/OT_1994CHUNK4_STONE_38_47.md) | 5 |
| [OT_1994CHUNK4_STONE_41_46_48.md](../runtime/OT_1994CHUNK4_STONE_41_46_48.md) | 9 |
| [OT_1994CHUNK4_STONE_42_45.md](../runtime/OT_1994CHUNK4_STONE_42_45.md) | 9 |
| [OT_1994CHUNK5_COMPARATOR_49.md](../runtime/OT_1994CHUNK5_COMPARATOR_49.md) | 6 |
| [OT_1994CHUNK5_COMPARATOR_50.md](../runtime/OT_1994CHUNK5_COMPARATOR_50.md) | 6 |
| [OT_1994CHUNK5_COMPARATOR_51.md](../runtime/OT_1994CHUNK5_COMPARATOR_51.md) | 6 |
| [OT_1994CHUNK5_COMPARATOR_52.md](../runtime/OT_1994CHUNK5_COMPARATOR_52.md) | 6 |
| [OT_1994CHUNK5_COMPARATOR_53.md](../runtime/OT_1994CHUNK5_COMPARATOR_53.md) | 6 |
| [OT_1994CHUNK5_COMPARATOR_54.md](../runtime/OT_1994CHUNK5_COMPARATOR_54.md) | 6 |
| [OT_1994CHUNK5_COMPARATOR_55.md](../runtime/OT_1994CHUNK5_COMPARATOR_55.md) | 6 |
| [OT_1994CHUNK5_COMPARATOR_56.md](../runtime/OT_1994CHUNK5_COMPARATOR_56.md) | 6 |
| [OT_1994CHUNK5_COMPARATOR_57.md](../runtime/OT_1994CHUNK5_COMPARATOR_57.md) | 6 |
| [OT_1994CHUNK5_COMPARATOR_58.md](../runtime/OT_1994CHUNK5_COMPARATOR_58.md) | 6 |
| [OT_1994CHUNK5_COMPARATOR_59.md](../runtime/OT_1994CHUNK5_COMPARATOR_59.md) | 6 |
| [OT_1994CHUNK5_COMPARATOR_60.md](../runtime/OT_1994CHUNK5_COMPARATOR_60.md) | 6 |
| [OT_1994CHUNK5_COMPARATOR_A.md](../runtime/OT_1994CHUNK5_COMPARATOR_A.md) | 5 |
| [OT_1994CHUNK5_COMPARATOR_B.md](../runtime/OT_1994CHUNK5_COMPARATOR_B.md) | 5 |
| [OT_1994CHUNK5_COMPARATOR_C.md](../runtime/OT_1994CHUNK5_COMPARATOR_C.md) | 5 |
| [OT_1994CHUNK5_MORALES_CORRECTION_COMPARATOR.md](../runtime/OT_1994CHUNK5_MORALES_CORRECTION_COMPARATOR.md) | 3 |
| [OT_1994CHUNK5_MORALES_CORRECTION_STONE.md](../runtime/OT_1994CHUNK5_MORALES_CORRECTION_STONE.md) | 3 |
| [OT_1994CHUNK5_MORALES_SOURCE_CANDIDATE.md](../runtime/OT_1994CHUNK5_MORALES_SOURCE_CANDIDATE.md) | 56 |
| [OT_1994CHUNK5_NEUTRAL_A.md](../runtime/OT_1994CHUNK5_NEUTRAL_A.md) | 198 |
| [OT_1994CHUNK5_NEUTRAL_A_CANDIDATE.md](../runtime/OT_1994CHUNK5_NEUTRAL_A_CANDIDATE.md) | 213 |
| [OT_1994CHUNK5_NEUTRAL_B.md](../runtime/OT_1994CHUNK5_NEUTRAL_B.md) | 55 |
| [OT_1994CHUNK5_NEUTRAL_C.md](../runtime/OT_1994CHUNK5_NEUTRAL_C.md) | 56 |
| [OT_1994CHUNK5_STONE_A.md](../runtime/OT_1994CHUNK5_STONE_A.md) | 5 |
| [OT_1994CHUNK5_STONE_B.md](../runtime/OT_1994CHUNK5_STONE_B.md) | 5 |
| [OT_1994CHUNK5_STONE_C.md](../runtime/OT_1994CHUNK5_STONE_C.md) | 5 |
| [OT_1994CHUNK8_COMPARATOR_A.md](../runtime/OT_1994CHUNK8_COMPARATOR_A.md) | 9 |
| [OT_1994CHUNK8_COMPARATOR_B.md](../runtime/OT_1994CHUNK8_COMPARATOR_B.md) | 9 |
| [OT_1994CHUNK8_NEUTRAL_A.md](../runtime/OT_1994CHUNK8_NEUTRAL_A.md) | 60 |
| [OT_1994CHUNK8_NEUTRAL_B.md](../runtime/OT_1994CHUNK8_NEUTRAL_B.md) | 246 |
| [OT_1994CHUNK8_STONE_A.md](../runtime/OT_1994CHUNK8_STONE_A.md) | 9 |
| [OT_1994CHUNK8_STONE_B.md](../runtime/OT_1994CHUNK8_STONE_B.md) | 9 |
| [assembly/California_Department_of_Corrections_v_Morales_merits_1995-04-25.md](../runtime/assembly/California_Department_of_Corrections_v_Morales_merits_1995-04-25.md) | 26 |
| [assembly/Hubbard_v_United_States_merits_1995-05-15.md](../runtime/assembly/Hubbard_v_United_States_merits_1995-05-15.md) | 30 |
| [assembly/Kansas_v_Colorado_original_exceptions_1995-05-15.md](../runtime/assembly/Kansas_v_Colorado_original_exceptions_1995-05-15.md) | 44 |
| [assembly/Kyles_v_Whitley_merits_1995-04-19.md](../runtime/assembly/Kyles_v_Whitley_merits_1995-04-19.md) | 26 |
| [assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md](../runtime/assembly/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md) | 52 |
| [assembly/Rubin_v_Coors_Brewing_Co_merits_1995-04-19.md](../runtime/assembly/Rubin_v_Coors_Brewing_Co_merits_1995-04-19.md) | 28 |
| [assembly/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md](../runtime/assembly/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md) | 28 |
| [assembly/United_States_v_Harris_merits_1995-04-27.md](../runtime/assembly/United_States_v_Harris_merits_1995-04-27.md) | 30 |
| [assembly/United_States_v_Lopez_merits_1995-04-26.md](../runtime/assembly/United_States_v_Lopez_merits_1995-04-26.md) | 32 |
| [assembly/United_States_v_Pinson_merits_1995-05-08.md](../runtime/assembly/United_States_v_Pinson_merits_1995-05-08.md) | 26 |
| [assembly/United_States_v_Williams_merits_1995-04-25.md](../runtime/assembly/United_States_v_Williams_merits_1995-04-25.md) | 24 |
| [scoped/OT_1994CHUNK1_COMPARATOR_A.md](../runtime/scoped/OT_1994CHUNK1_COMPARATOR_A.md) | 5 |
| [scoped/OT_1994CHUNK1_COMPARATOR_B.md](../runtime/scoped/OT_1994CHUNK1_COMPARATOR_B.md) | 5 |
| [scoped/OT_1994CHUNK1_COMPARATOR_C.md](../runtime/scoped/OT_1994CHUNK1_COMPARATOR_C.md) | 5 |
| [scoped/OT_1994CHUNK1_STONE_A.md](../runtime/scoped/OT_1994CHUNK1_STONE_A.md) | 5 |
| [scoped/OT_1994CHUNK1_STONE_B.md](../runtime/scoped/OT_1994CHUNK1_STONE_B.md) | 5 |
| [scoped/OT_1994CHUNK1_STONE_C.md](../runtime/scoped/OT_1994CHUNK1_STONE_C.md) | 5 |

### Preserved freeze copies (8)

These are provenance copies of the same malformed internal delimiters. Any later treatment must preserve truthful stage history; they are not eight competing adjudications.

| Freeze file | First affected marker line |
|---|---:|
| [OT_1994CHUNK2_FARGO_COMPARATOR.md](../freeze/OT_1994CHUNK2_FARGO_COMPARATOR.md) | 3 |
| [OT_1994CHUNK2_FARGO_STONE.md](../freeze/OT_1994CHUNK2_FARGO_STONE.md) | 3 |
| [OT_1994CHUNK3_NEUTRAL_A.md](../freeze/OT_1994CHUNK3_NEUTRAL_A.md) | 56 |
| [OT_1994CHUNK3_NEUTRAL_B.md](../freeze/OT_1994CHUNK3_NEUTRAL_B.md) | 201 |
| [OT_1994CHUNK3_NEUTRAL_C.md](../freeze/OT_1994CHUNK3_NEUTRAL_C.md) | 54 |
| [OT_1994CHUNK6_NEUTRAL.md](../freeze/OT_1994CHUNK6_NEUTRAL.md) | 58 |
| [OT_1994CHUNK8_NEUTRAL_SANITIZED.md](../freeze/OT_1994CHUNK8_NEUTRAL_SANITIZED.md) | 63 |
| [OT_1994CHUNK9_ASSEMBLY_MILLER_PRE_QA.md](../freeze/OT_1994CHUNK9_ASSEMBLY_MILLER_PRE_QA.md) | 30 |

## Preservation and operator disposition

A SHA-256 snapshot taken before validation was compared with the protected repository files. Before this audit was written, none had changed. Final verification is confined to this audit's links and the protected-file comparison; scratch material is under root `tmp/`. The three state baselines retain these hashes:

| Opening tracker | SHA-256 |
|---|---|
| Holdings | `c3c94000e869c13a669c8032b7e046f6ab9e647be95762956154ff86c7dedb86` |
| Standards and Tests | `fcab34dcc8209078e6ef16572f05759a9716e33385783162efce5e6be3d9467a` |
| Standing State | `4dc38bbd249bddfb6084783436ed101d38cad4b224aa999fbe89e6a90278049a` |

**Operator summary: FAIL — 2 unresolved findings.**  
**Severity count: high 0; medium 0; low 2.**
