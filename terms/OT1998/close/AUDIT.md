# October Term 1998 — first coordinated close audit

**Status:** First audit complete; close staged for review, not cleared for the Commit pass. Six correction items remain below. No second audit or corrective rewrite has been performed.

**Scope:** All 130 completed Court events, the Maine admitted source, all eleven public renders, the three complete replacement candidates, relevant opening law, final manifest and continuity, and the fourteen pending carryovers. Records control; renders were cross-checks. No Record-level defect requiring a changed judgment, vote, controlling coalition, or remedy was identified in this review.

**Publication boundary:** The candidates remain under `terms/OT1998/close/`. The published `state/` baseline has not been replaced. AGENTS.md permits the Commit pass **“Only when the audit lists no unresolved discrepancy.”** The user requested the issues before another audit round; this report supplies that checkpoint. None of the findings below authorizes silently changing an adjudication.

## Findings requiring correction before final close

### 1. Title IX: an older reservation was not updated for Davis

[Standards candidate](STANDARDS_AND_TESTS.candidate.md), line 2525, says recipient attribution outside the teacher-harassment setting remains unresolved. That blanket reservation is obsolete after *Davis v. Monroe County Board of Education*.

The [Davis Record](../records/davis_v_monroe_county_board_of_education_merits_1999-05-24.md), lines 177–181, establishes the sufficient actual-notice, substantial-control and recipient-own-wrong route for peer harassment. The new Standards entry correctly states that rule at lines 3285–3290. The older entry can nevertheless mislead later research into treating peer attribution as wholly unresolved.

**Required correction:** Narrow the older open-question statement to settings the Court still leaves unresolved and cross-reference Davis's separately specified rule. Preserve the distinct coalitions and the limits of the sufficient route. This is current-law tracker maintenance, not a defect in Davis or a new adjudication.

### 2. Tseng: the Article 25 proposition lacks its separate component attribution

[Standards candidate](STANDARDS_AND_TESTS.candidate.md), line 9805, includes the proposition that intentional touching alone does not establish Article 25 willful misconduct. Its sole authority at line 9801 and navigation at line 9807 identify Part I and eight direct joins.

That proposition instead comes from Part II and seven Associate joins, expressly excluding Stone-Zsela: [Tseng Record](../records/el_al_israel_airlines_v_tseng_merits_1999-01-12.md), lines 108–109 and 125–131. Part I reserves Article 25's operation. [Holdings candidate](HOLDINGS.candidate.md), lines 39867–39869, already preserves the correct separate authority.

**Required correction:** Add a distinct Part II authority component and corresponding navigation. The substantive proposition is supported; no vote or disposition changes.

### 3. Holloway: wording can imply a preservation finding the Court did not make

[Standards candidate](STANDARDS_AND_TESTS.candidate.md), line 5860, says the construction “decides no unpreserved separate instruction request.” The [Holloway Record](../records/holloway_v_united_states_merits_1999-03-02.md), lines 46, 105 and 125, expressly leaves the request's existence and preservation unestablished and infers neither preservation nor forfeiture.

**Required clarification:** Replace the potentially misleading qualifier with the Record's unresolved status—for example, “decides no separate instruction request whose existence and preservation are unestablished.” This is a wording ambiguity, not a finding that the judgment or remedy is wrong.

### 4. Sullivan: the manifest retains the superseded supplied docket number

[Manifest](../workspace/manifest.md), line 76, lists *American Manufacturers Mutual Insurance Co. v. Sullivan* as No. **97-1620**. The [controlling Record](../records/american_manufacturers_v_sullivan_merits_1999-03-03.md), lines 1 and 4, expressly corrects that supplied number to **97-2000**. The candidate, Render Input, output and continuity use the corrected number.

**Required correction:** Update the manifest docket to 97-2000. Case identity and all adjudicative substance remain unchanged. A targeted comparison of 124 manifest rows with numbered dockets found no additional unexplained discrepancy; Tice's extra numbers are expressly labeled lower-court dockets rather than Supreme Court docket alternatives.

### 5. Hanlon: the manifest misdescribes the completed opinion's form

[Manifest](../workspace/manifest.md), line 118, calls *Hanlon v. Berger* a per curiam decision after merits submission. The [Hanlon Record](../records/hanlon_v_berger_merits_1999-05-24.md), line 14, adopts an independent signed, counted lead, and line 168 identifies O'Connor as author.

**Required correction:** Describe the event as a signed merits decision, or simply a merits decision. The current eight-to-one limited vacatur and seven-to-two immunity ruling are correct; this is manifest metadata, not an authorship reassignment or new vote.

### 6. Fifteen Holdings remedy tables have malformed Markdown headers

The [Holdings candidate](HOLDINGS.candidate.md) places the bold “Operative remedy or transition” label on the same line as each affected table header. The label becomes an extra apparent header cell while the delimiter row retains the intended column count, preventing normal GitHub-flavored Markdown table rendering.

**Required correction:** Put the label on its own line, then a blank line, then the unchanged table. Preserve every cell's substance. The first audit identified the problem in AADC; a targeted search established the following fifteen-instance scope. None occurs in the opening Holdings baseline.

| Candidate line | Affected entry |
|---:|---|
| 2621 | Department of Commerce / House / Glavin |
| 13447 | Martin v. Hadix |
| 20848 | Lilly v. Virginia |
| 21041 | Neder v. United States |
| 21220 | Stewart v. LaGrand |
| 21266 | Strickler v. Greene |
| 26317 | American Manufacturers v. Sullivan |
| 26359 | Bruneau v. South Kortright |
| 26467 | City of Dallas v. Dallas Fire Fighters |
| 26984 | Olmstead v. L.C. |
| 31859 | Buckley v. American Constitutional Law Foundation |
| 32073 | National Committee of the Reform Party v. DNC |
| 34232 | Reno v. American-Arab Anti-Discrimination Committee |
| 39597 | Jefferson County v. Acker |
| 42052 | Wright v. Ernst & Young |

## Nonblocking wording and administrative notes

These are distinguished from the six correction items. None establishes a different final vote or a need to re-adjudicate a case.

- **Richardson's retained preliminary table:** [Record](../records/richardson_v_united_states_merits_1999-06-01.md), lines 80 and 83, retain Ginsburg's provisional position and a preliminary six-Associate coalition. Explicitly labeling that table provisional would improve clarity. Line 68 states that the provisional departure was corrected; the following reconciliation and final table at lines 107–110 correctly place Ginsburg with the affirmers. The public result and candidates are consistent.
- **Knowles's stale review flag:** [Continuity](../workspace/continuity.md), line 6491, retains the old concern described in chunk 3 validation. The current [Record](../records/knowles_v_iowa_merits_1998-12-08.md), line 182; chunk 2 Render Input, line 630; output, line 610; and Holdings candidate, line 20794, consistently exclude Stone from Part II and give it eight Associate votes including its author. The flag describes a superseded presentation concern, not an unresolved coalition defect.
- **FOP's compressed statutory description:** Standards candidate, line 13776, could state attempted force and the conviction-relief qualifications more explicitly. The [Record](../records/fraternal_order_of_police_v_united_states_merits_1998-10-07.md), lines 143–145, and Holdings retain the full rule. The existing statutory references do not establish a proven narrowing; this is an optional precision improvement.
- **Reorganized CF&I and PBGC:** Holdings candidate, line 38474, retains the original Code-directed-classification phrasing without a nearby PBGC clarification. The new PBGC entry and Standards, line 10191, correctly recognize applicable external statutory direction without a reciprocal Code cross-reference. A bounded later-authority note could prevent a universal Code-only reading. The original §4971 holding remains intact; no overruling or confirmed merits defect is inferred.

## Material questions resolved without a finding

- **June 22 ADA group:** Albertson's disability-method discussion is expressly noncontrolling. Sutton and Murphy separately establish the mitigation rule. The Bragdon backlink and current mitigation standard preserve the resolved reservation. Albertson's case-specific nonreach is not a competing controlling rule.
- **June 23 immunity group:** Florida Prepaid supplies no controlling affirmative amenability or commercial-consent rationale of its own. College Savings separately supplies five direct votes rejecting the specified ordinary-commercial consent theory. The candidates preserve both propositions without manufacturing an affirmative Article I/§5 synthesis. Alden separately has a five-Justice state-court FLSA holding.
- **Fractures and component coalitions:** Carter, Coleman, Census, Minns, Jones, Kumho, the bank cases and the later employment decisions retain judgment/rationale distinctions, partial joins and noncontrolling proposals. No unexplained material Justice-specific historical departure was identified in the completed scoped reviews.
- **Carryovers:** Fourteen genuine pending matters remain: thirteen inherited matters plus Germany's original-leave request. New Jersey's implementing-decree submission is completed. General retained implementation jurisdiction in New Jersey or Louisiana does not itself create an additional pending request. No execution, deadline, filing or terminal disposition was invented.

## Completed first-pass validation and coverage

[Deterministic preflight](preflight/FIRST_PASS.md) records the single canonical checker invocation, which returned `OK: OT1998; 0 warning(s)`, and the inventory, chronology, runtime, Public Projection/Render Input, arithmetic and link checks. [Candidate gates](preflight/CANDIDATE_GATES.json) record synchronized headers, exact candidate identities, preservation of 2,142 opening Holding fields, all 131 event-source identities, 195 new navigation links and fourteen pending rows. Those mechanical checks do not supersede the substantive and presentation findings above.

The 139 initially unavailable linked targets were checkout omissions: their exact bytes existed on the pinned main revision and were verified or restored. They are not 139 repository or adjudication defects. Opening volumes were checked inside the canonical invocation; no duplicate volume check or second canonical-check pass was run.

Fresh, scoped Astra Ultra contexts performed one coordinated first substantive audit. Work was partitioned without overlapping case review; unusually long, still-unread portions were reassigned before reading to reduce elapsed time.

| Scope | Completed substantive coverage |
|---|---:|
| Chunks 1–2 | 24 Court Records |
| Chunks 3–4 excluding the two cases below | 22 Court Records plus Maine admitted source |
| AT&T and Reno AADC | 2 Court Records |
| Chunks 5–6 | 26 Court Records |
| Chunks 7–8 | 23 Court Records |
| Chunks 9–11 | 33 Court Records |
| Separate Standing State review | Roster, allotments, standing practice and all fourteen carryovers |

Each case scope included the unique Record kernel and annex, relevant opening/current authority, corresponding candidate provisions, manifest/continuity and public-render cross-checks. Supporting frozen/source material was consulted for concrete ambiguities; this was not wholesale re-adjudication or an assertion that every external source was recrawled.

**Discovery-boundary limitation:** One auditor used `rg --files state terms/OT1998` with a downstream filter for the permitted trackers, workspace files and two chunk outputs. That was broader discovery than intended: filtering output does not guarantee excluded names were never traversed internally. No `stone/` path or `MASTER_JURISPRUDENCE` filename appeared to that auditor, and no such file content was opened. Subsequent reads used explicit permitted paths. No further search was made to investigate excluded locations. This limitation is disclosed rather than claiming a fully verified exclusion at that discovery step. No Git command was used.

## Candidate identities and next boundary

The immutable opening/input identities are in [INPUT_SNAPSHOT.json](INPUT_SNAPSHOT.json). The reviewed candidate identities are:

| Candidate | SHA-256 |
|---|---|
| Holdings | `33ce239af3af5affb990907733700134557559cd4fb8e7afcd958fb1912f7a52` |
| Standards and Tests | `a93fe75e85445908079971811269e6675d929f1bee4d611ad0d394e971e90fc0` |
| Standing State | `102295da767d405e04b8a8d1df25e56b8e389b2e7c4c333e40c6abc4d296054d` |

The Holdings pass snapshots and receipts preserve the three chronological preparation passes. Standards were derived independently before navigation reconciliation. The Standing draft's mistaken OT1999 reference in the completed-event cutoff was corrected to OT1998 before final candidate placement and is recorded in its preparation receipt; its opening term correctly remains OT1999.

No Record, frozen handoff, public render, approved brief, governing infrastructure, workspace projection or published tracker was changed during this close preparation and first audit. The six findings and four nonblocking notes are presented for the requested review. Corrections, any ensuing verification, the Term-Close Dossier, coordinated state publication, volume rebuilding, generated indexes and final candidate cleanup remain outside this completed first-audit checkpoint.
