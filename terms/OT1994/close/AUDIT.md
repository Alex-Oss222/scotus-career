# October Term 1994 — close audit

Audit date: September 30, 2026. Scope: all 99 inventory Court matters, both Admitted Source Records, both Holdings passes, and the complete Holdings, Standards and Tests, and Standing State candidates.

**Result: FAIL.** The deterministic coverage and integrity gate passed before the fresh substantive review began. That review found the discrepancies listed below. They include candidate-rule completeness and remedy errors, an insufficiently supported historical-departure explanation, and smaller documentation, authority-mapping, and presentation defects. No adjudication, candidate, projection, or render was corrected in this pass. Close is not ready for Commit.

**Operator summary: FAIL — 0 high, 3 medium, 14 low findings (17 total).**

Severity means: **high** would indicate a demonstrated erroneous judgment, controlling coalition, or comparably fundamental defect; **medium** identifies an operative legal projection error or an unresolved substantive audit requirement; **low** identifies a bounded omission, inaccurate status statement, authority reference, or presentation defect without a demonstrated change to the judgment. Counts are numbered findings, not the number of affected files; grouped findings enumerate their individual instances.

## Method and execution boundary

The operator instructions and the three foundation files were read first. The first validation executed was the unchanged `tools/check_term.py` main program for `OT1994`. Its normal commit-existence helper invokes Git, which the operator expressly prohibited. A scratch launcher intercepted only that helper and answered its read-only object-existence queries by decoding the local loose/packed object database and verifying object hashes. It did not launch Git. The remaining checker logic ran unchanged and returned exit code 0: `OK: OT1994; 63 warning(s)`.

All 63 warning occurrences were examined: they are hexadecimal-looking source identifiers, URL fragments, or similar text captured by the checker's broad commit-reference pattern, including text in the superseded audit. They are not 63 missing provenance commits. The three actual cited commit identities exist and their relevant contents were verified directly. The launcher handled 69 reference checks; zero Git processes were run.

The remaining deterministic checks below were completed and their parser ambiguities resolved before substantive review. Three fresh scoped review contexts then examined matters 1–36, 37–72, and 73–99, respectively. They read the governing rules, current canonical bodies and their audit annexes, relevant frozen commitments/reconciliations and Stone inputs, entering-law connections, Public Projections, public renders, and the corresponding candidate entries. They did not receive the previous audit's conclusions. The coordinating review independently checked cross-register preservation, the complete Standing State candidate, carryovers, provenance, source access, and the findings before consolidating this report. Scripts checked identity, coverage, and arithmetic; they did not decide legal meaning.

The legal review covered the full 99-matter set, rather than sampling. Historical opinions were evidence of Justice-specific positions, not substitutes for the current Records. Source handoffs, retained primary-source material, and targeted primary-opinion checks were used to test disputed propositions. This audit does not claim to have newly downloaded and reread every petition, merits brief, and appendix for all 99 matters. Existing, expressly bounded source limitations remain bounded; no omitted source fact was supplied by inference.

Only this file is the audit deliverable. Scratch scripts and evidence were written under root `tmp/`. No Git command, publication, correction, or tracker replacement occurred. The final protected-file comparison is reported below.

## Unresolved findings

### F01 — Medium — Jefferson Lines changes a mandatory remedy into permission

**Location:** [Holdings candidate](HOLDINGS.candidate.md), line 1341. **Controlling source:** [Jefferson Lines Record](../records/Oklahoma_Tax_Commission_v_Jefferson_Lines_Inc_merits_1995-04-03.md), line 154 and its Public Projection.

The candidate says the bankruptcy tax claims “may be allowed.” The Record directs that the bankruptcy court “shall allow” them to the extent they are otherwise valid. The qualification preserves independent validity questions; it does not make allowance discretionary after those questions are satisfied. The Render Input and render preserve the mandatory direction. This is an operative-remedy projection error in Holdings, contrary to the express requirement to keep permission and obligation distinct. It does not establish that the underlying adjudication needs to change.

### F02 — Medium — Schlup's Standards entry omits operative statutory and evidence qualifications

**Location:** [Standards candidate](STANDARDS_AND_TESTS.candidate.md), lines 2215–2233. **Controlling source:** [Schlup Record](../records/Schlup_v_Delo_merits_1995-01-23.md), the separate gateway and §2244(b) holdings; the Holdings candidate and public projection preserve the fuller rules.

The entry correctly states the more-likely-than-not innocence threshold and the separation between gateway access and merits relief. It does not state the complete trigger for §2244(b)'s qualified permission to refuse a subsequent state-custody petition: prior federal denial after a factual evidentiary hearing or a legal merits hearing, together with the statute's exception requiring both a newly asserted unadjudicated ground and the court's satisfaction that the ground was not deliberately withheld or otherwise abused. Nor does it preserve the related conditional duty when those requirements are met and other barriers are absent, or the State's particularized abuse pleading before the burden shifts. Saying only that the statute does not sustain refusal under the rejected clear-and-convincing crime-innocence standard does not supply those conditions. New evidence is not necessarily a new legal ground.

The same entry says to consider the whole probative record, but omits the adopted qualification that trial admissibility is not a categorical gate: excluded or later evidence can count, and improperly admitted trial evidence can remain probative subject to reliability. It also fails to make explicit the reliability/likely-credibility assessment instead of treating every submitted statement as true, and the prohibitions on categorically excluding impeachment evidence or discrediting witnesses solely because they are prisoners. These are adopted operating instructions, not Stone's unjoined preferred checklist. The defect is the Standards projection's incompleteness; the full conditions remain in the Record, Holdings, input, and render.

### F03 — Medium — Koray's departure annex does not establish its asserted changed premise

**Location:** [Koray Record](../records/Reno_v_Koray_merits_1995-06-05.md), lines 179–187.

Lines 179 and 185 correctly acknowledge that the historical opinion gave the BOP's permissible interpretation some weight, without making the program statement independently controlling. Line 183 nevertheless describes omission of an “independently sufficient administrative-deference ground.” Line 185 treats the narrower explanation as a material change, and line 187 offers the frozen majority's preference for sufficient statutory reasoning and the Wilson/Crandon/Thomas Jefferson University distinctions as the changed premise. Those scope choices do not identify a different legal, factual, procedural, or simulated predicate explaining why each affected Justice would abandon even the historical nonconclusive interpretive support. The cited doctrines distinguish conclusive agency authority; the historical opinion did not claim such authority. The [historical majority opinion](https://www.law.cornell.edu/supct/html/94-790.ZO.html) was checked for this distinction.

The annex therefore contains both an inaccurate description of what was omitted and an unresolved explanation for the material departure it claims. The Engine requires a concrete, Justice-specific changed premise for a material departure, not merely a frozen choice to omit support. This finding does not establish an erroneous judgment, require importing historical deference into current law, or presume every omitted supporting citation is material. The separate correction task must resolve the characterization and premise, including whether omission of redundant support is actually a material departure.

### F04 — Low — Hurley misdescribes Turner's cable context as broadcasting

**Locations:** [Hurley Record](../records/Hurley_v_Irish_American_Gay_Lesbian_and_Bisexual_Group_of_Boston_merits_1995-06-19.md), lines 34/40 and repeated Public Projection lines 157/163; [chunk-8 input](../render-inputs/OT_1994CHUNK8.md), lines 186/192; [chunk-8 render](../output/OT_1994CHUNK8.md), lines 180/186; [Holdings candidate](HOLDINGS.candidate.md), line 12680.

The explanation calls Turner's medium its “separate broadcast context,” and the treatment line refers to “broadcast results.” The controlling [OT1993 Turner Record](../../OT1993/records/Turner_Broadcasting_System_Inc_v_FCC_merits_1994-06-27.md), lines 46–50, concerns cable operators and expressly distinguishes broadcasting's spectrum-scarcity rationale. The medium description is inaccurate and has propagated into the candidate. Hurley's parade rule, unanimous coalition, and remedy remain intact. Because the error originates in the Record, a candidate-only change would leave the source discrepancy unresolved.

### F05 — Low — Standards lacks component-specific authority mappings in three entries

The [Standards candidate](STANDARDS_AND_TESTS.candidate.md) states the rules accurately in these instances, but the question-level authority and navigation identify a different holding from the same case. The template requires separate mapping when authorities supply distinct operative components.

| Instance | Candidate location | Missing authority and consequence |
|---|---|---|
| Hechinger | Statutory qualification at 5809; authority 5805; navigation 5811 | The §2456(h) covered-action disability and survival qualifications come from “The enacted contingency limits the remedy,” [Record](../records/Metropolitan_Washington_Airports_Authority_v_Hechinger_merits_1995-06-05.md) lines 48–56, not solely the listed constitutional agency/control holding. Both have a unanimous Stevens coalition, but the statutory component still requires its own mapping. |
| Aguilar | Constitutional qualification at 2446; authorities 2441–2442; navigation 2448 | “The as-applied speech objection,” [Record](../records/United_States_v_Aguilar_merits_1995-06-21.md) lines 60–68, is supported by Ginsburg and all seven other associates; Stone agrees in disposition only under his fallback. That eight-Justice rationale is different from the listed eight-Justice §2232(c) coalition, which includes Stone and excludes Stevens, and from the six-Justice §1503 coalition. The entry omits this mapping; it does not affirmatively cast a false constitutional vote. |
| Jenkins | Release qualifications at 3126; authority 3122; navigation 3128 | The complete Freeman showing, low-score limits, and national-parity clarification come from “Partial release requires the complete Freeman showing,” [Record](../records/Missouri_v_Jenkins_merits_1995-06-12.md) lines 49–57. The listed salary-support holding does not supply that separate component. The Souter/Stone/Stevens/Ginsburg/Breyer coalition is the same, but the inherited Freeman entry does not separately identify Jenkins's clarification. |

### F06 — Low — Transcon's assignment explanation misstates Kennedy's existing workload

**Location:** [Transcon Record](../records/Interstate_Commerce_Commission_v_Transcon_Lines_merits_1995-01-10.md), line 53.

The assignment paragraph says Kennedy had not authored another chunk-1 Court opinion. The immediately preceding January 9 [Plakas Record](../records/Plakas_v_Drinski_merits_1995-01-09.md), lines 35/38/46, assigns him the Court's opinion. The workload statement is false. Workload is secondary, and this audit finds no resulting defect in Kennedy's Transcon assignment, opinion joins, or judgment. The internal explanation nevertheless needs truthful correction.

### F07 — Low — Current canonical chronology recitals retain superseded stopped-case status

These are unqualified statements in current Records, not merely retained historical freeze files. Later validation establishes completion and checks dependencies, so no substantive effect is demonstrated; the stale current text still prevents an unqualified stale-version clearance.

| Current Record | Location and stale statement | Current authority |
|---|---|---|
| [Milwaukee Brewery](../records/Milwaukee_Brewery_Workers_Pension_Plan_v_Jos_Schlitz_Brewing_Co_merits_1995-02-21.md) | Line 14 says Fargo has no adjudication and supplies no law. | Fargo was completed effective February 13. |
| [NTEU](../records/United_States_v_National_Treasury_Employees_Union_merits_1995-02-22.md) | Line 10 says O'Neal remains unresolved and supplies no law. | O'Neal was completed effective February 21. |
| [Harris v. Alabama](../records/Harris_v_Alabama_merits_1995-02-22.md) | Line 10 retains the same O'Neal assertion. | Same February 21 completion. |
| [Grubart](../records/Jerome_B_Grubart_Inc_v_Great_Lakes_Dredge_Dock_Co_merits_1995-02-22.md) | Line 10 retains the same O'Neal assertion. | Same February 21 completion. |
| [Anderson v. Green](../records/Anderson_v_Green_decision_1995-02-22.md) | Line 12 says O'Neal remains undecided and supplies no law. | Same February 21 completion. |
| [Swint](../records/Swint_v_Chambers_County_Commission_merits_1995-03-01.md) | Line 112 says O'Neal remains stopped and supplies no law. | Same February 21 completion. |
| [Mastrobuono](../records/Mastrobuono_v_Shearson_Lehman_Hutton_Inc_merits_1995-03-06.md), [Curtiss-Wright](../records/Curtiss_Wright_Corp_v_Schoonejongen_merits_1995-03-06.md), [Guernsey](../records/Shalala_v_Guernsey_Memorial_Hospital_merits_1995-03-06.md) | Each line 22 describes 31 earlier events, an earlier set of 24, and says no O'Neal adjudication enters. | The completed February 21 O'Neal is part of the current effective chronology. The old preparation totals and exclusion are not labeled as superseded in these current passages. |
| [Ambassador](../records/Ambassador_Books_Video_Inc_v_City_of_Little_Rock_merits_1995-03-20.md) | Line 22 describes 34 earlier events and excludes O'Neal. | Same completed O'Neal authority; original preparation is distinguishable from the present effective baseline. |
| [Pinson](../records/United_States_v_Pinson_merits_1995-05-08.md) | Lines 18/195 describe Robertson as unadjudicated or supplying no law. | Robertson was completed effective May 1. |
| [Kansas](../records/Kansas_v_Colorado_original_exceptions_1995-05-15.md) | Lines 38/350 retain the same obsolete Robertson status. | Same May 1 completion. |
| [Hubbard](../records/Hubbard_v_United_States_merits_1995-05-15.md) | Lines 20/269 retain the same obsolete Robertson status. | Same May 1 completion. |

The completion/revalidation material expressly addresses the absence of material doctrinal dependency. That supports the bounded severity; it does not make the current status recitals accurate. No deletion of truthful earlier freeze history is proposed.

### F08 — Low — Completed Records retain present-tense draft or pending-validation stamps

**Locations:** Mastrobuono lines 4/95/126; Curtiss-Wright 4/104/135; Guernsey 4/124/155; Ambassador 4/167/198, in the current Records linked in F07. The passages still call the files drafts awaiting promotion, say they have not been applied to current law, or leave promotion/clearance pending, although they occupy canonical paths and are included in the ledger, render inputs, outputs, and candidates.

In addition, [Whitecotton](../records/Shalala_v_Whitecotton_merits_1995-04-18.md), line 169, says the regulatory transition is subject to the root's pending complete chronology refresh; line 183 and the completed validation material report the refresh complete. The authority of the completed decisions is established, but these surviving internal statements are inconsistent with their current status. No legal reopening is implied.

### F09 — Low — Robertson's manifest row still calls the decision per curiam

**Location:** [manifest](../workspace/manifest.md), line 63.

The current row describes a “Per curiam decision after merits submission.” The completed [Robertson Record](../records/United_States_v_Robertson_merits_1995-05-01.md), input, and render identify Breyer's authored Opinion of the Court. The historical expectation in the original inventory can remain an input; the current workspace event description should reflect the actual adjudication. Coverage and the public opinion are otherwise consistent.

### F10 — Low — Swint's source label calls a text file a PDF

**Location:** [Swint Record](../records/Swint_v_Chambers_County_Commission_merits_1995-03-01.md), line 118.

The link labeled “PDF” points to a `.txt` transcription. The source is linked and the audit identifies no missing legal proposition from this labeling error, but the format description is inaccurate.

### F11 — Low — The Standards pass note still reports five resolved render gaps as open

**Location:** [Standards pass note](STANDARDS_AND_TESTS_PASS.md), line 26.

The note says the Holdings-pass notes report an absent Robertson entry and four missing chunk-7 dockets, and says they remain matters for render work and audit. Both current Holdings pass notes expressly mark those five gaps resolved; Robertson, Adarand, Wilton, Rambo, and Johnson are present in their current renders. This is a replaceable close note making an inaccurate current cross-reference assertion, rather than an immutable historical modeling receipt. It changes no law but must not be mistaken for five still-missing decisions.

### F12 — Low — Wilson's public render starts a sentence with a lowercase letter

**Location:** [chunk-6 render](../output/OT_1994CHUNK6.md), line 488, Wilson entry.

The second sentence begins with lowercase “the.” This is a copyediting defect only; the rule and vote are unaffected.

### F13 — Low — Nebraska's public render repeats its chronology sentence

**Location:** [chunk-6 render](../output/OT_1994CHUNK6.md), lines 560/562, Nebraska entry.

The original-action posture, report/exception dates, questions, and argument date are repeated in immediate succession. The repeated dates agree, so this is duplication rather than a chronology contradiction.

### F14 — Low — North Star's compact render leaves table cells as semicolon lists

**Location:** [chunk-6 render](../output/OT_1994CHUNK6.md), lines 716–717 and 721–722.

The judgment and opinion-topology content is pasted as semicolon-delimited cell sequences rather than the required compact-form prose. The names, unanimity, and disposition are present; the defect is public presentation under the render form, not missing votes or a false coalition.

### F15 — Low — Swint's Holdings entry omits the express connected-review reservation

**Location:** [Holdings candidate](HOLDINGS.candidate.md), lines 5071–5077. **Source:** [Swint Record](../records/Swint_v_Chambers_County_Commission_merits_1995-03-01.md), lines 67/181.

The candidate correctly states the narrow rejection of this county appeal and says earlier connected-review examples are not converted into a general pendent-party doctrine. It omits Part IV's express reservation whether genuinely inextricable or necessary connected review is available at all, adopted by the eight associates. Stone's affirmative view remains separate. The Standards entry correctly preserves the reservation. The Holdings wording does not affirmatively adopt Stone's exception or create a categorical prohibition, but it fails to carry an express question left open by the controlling writing.

### F16 — Low — Guernsey uses a transition label for continuing qualifications

**Location:** [Standards candidate](STANDARDS_AND_TESTS.candidate.md), line 5648.

The field labeled “Effective transition” contains recall-without-new-debt scope, necessary-borrowing qualifications, the ordinary refinancing-cost ceiling, and its compelling-factors exception. These are continuing limits, not prospective, delayed, stayed, or transitional operation as the template defines that field. The actual July 1, 1983 applicability rule is correctly supplied in the preceding paragraph, and all the legal qualifications are present. This is a label-only defect, not an incorrect effective date or missing exception.

### F17 — Low — Kelley contains a doubled space in the render source

**Location:** [chunk-6 render](../output/OT_1994CHUNK6.md), line 382.

The text contains “remains;  No” with two spaces. This is a source-text copyediting defect only; ordinary Markdown display can collapse the extra space, and no substantive or visible-layout consequence is established. It is recorded because the requested audit includes discrepancies however small.

## Deterministic checks

| Check | Result and scope |
|---|---|
| Required initial checker | Passed, exit 0, with the read-only Git-object substitution disclosed above. All 63 pattern warnings were classified. |
| Inventory → manifest → Record → Render Input → render | All 99 inventory matters match one scheduled manifest entry, one current Court-event Record, one generated input entry, and one public entry. Nine chunks contain 12 matters each in chunks 1–8 and three in chunk 9. The two additional Records are admitted-source events, not missing Court renders. Finding F09 concerns Robertson's event-type description, not coverage. |
| Ledger and natural keys | 101 distinct canonical files and 101 distinct ledger references; no duplicate current event or missing ledger target. All 101 files exist in the directly read HEAD tree. |
| Effective dates and chronology | Inventory, manifest, Records, ledger, and output dates reconcile. Same-day cases use their common prior baseline unless an expressly ordered relationship applies; Pinette precedes the dependent Chabad action. The final Court-event date is June 29, 1995. The March 10 Vaccine Table and April 4 plant-variety transitions retain their separate applicability rules. The later-discovered stale narrative recitals are listed in F07/F08, rather than being treated as actual new event dates. |
| Participation and arithmetic | All component votes and opinion joins were checked by names and legal scope. A script examined 131 conventional judgment rows; the NTEU and Evans parser flags were resolved from the actual entries, not counted as defects. Combined/narrative formats were read individually. No unexplained duplicate join, participating retired Justice, or unsupported majority count was found. |
| Reduced Courts | Ginsburg does not participate in FEC; Scalia in Wolens; Stevens and Breyer in Grubart; Breyer in City of Milwaukee, Wilton, and Sky Reefer. Reduced denominators reconcile. No reason for nonparticipation was invented. |
| Runtime freshness | All nine approved briefs match their generated neutral, Stone, and comparator splits: 27 checked outputs. Frozen historical stage artifacts were separately distinguished from current authority. |
| Public Projection → Render Input | All 99 bounded eleven-block projections match the generated inputs under the tool's newline/outer-whitespace convention. No separately authored substantive input was found. |
| Render completeness and form | All 99 entries have docket/caption coverage, supplied chronology or express date limits, end markers, and required following boundaries. All 71 full-form entries contain judgment and topology tables; the other 28 use compact form. Semantic transmission was read, including distinct components, separate writings, qualifications, remedies, and source limits. F12–F14 report the small surviving presentation defects. |
| Holdings explanation depth | All 236 controlling explanations are within 120–200 words (138–185 by whitespace count). None of these OT1994 matters requires the Casey special-consideration length. Of 236 explanations, 233 render verbatim after typography/format normalization; the three remaining bounded paraphrases in Anderson v. Edwards, Celotex, and Sweet Home were checked and introduce no additional substantive discrepancy. |
| Local links and anchors | 12,218 live local/repository-link occurrences checked; zero broken current targets or anchors. 185 prospective publication references to new `state/HOLDINGS.md` anchors resolve against the completed candidate and are intentionally awaiting Commit. Ignored scratch snapshots were excluded from the live-artifact count. |
| External links | 522 unique source URLs checked: 418 HTTP 200, 47 HTTP 403, three HTTP 429, one HTTP 502, and 53 connection/TLS/timeout failures. No 404 or 410 was returned. Restricted or inconclusive access is not proof that an authority is absent. The inconclusive URLs are preserved below. |
| Commit references and correction provenance | Three genuine commit references verified by object decoding and hash validation. The Morales and Stone v. INS claims match the relevant committed changes. No Git command was used. |
| Candidate staging and cleanup | Exactly the three coordinated candidates, two Holdings pass notes, one Standards pass note, the canonical audit, and `.gitkeep` occupy `close/`. Candidates and temporary pass notes properly remain before a successful Commit. There is no premature close dossier or publication. F11 reports a stale assertion inside a retained pass note. |
| Open-matter carry-forward | Nine continuing matters are preserved, with the stages described below. All 99 term inventory events are completed; completion of an exceptions event does not falsely terminate an original proceeding. No stopped inventory matter is silently dropped. |

The deterministic gate tests coverage and structural consistency. It cannot establish that a correctly linked rule preserves every legal qualification or that an annex supplies a persuasive Justice-specific changed premise. Those are the reasons the subsequent substantive findings coexist with a passed initial gate.

## Candidate review and preservation

The Holdings candidate was reviewed across both passes: pass 1 covers matters 1–60 and 154 controlling propositions; pass 2 covers matters 61–99 and 82 propositions. Together they account for all 236 propositions and the two effective source transitions. Its 508 case-area entries retain all 381 opening entries and add 127 case-area entries. Of 25 changed inherited entries, 23 differ only in spacing; the two substantive additions are the Brecht-to-O'Neal and Cavanaugh-to-Morales references. No prior holding was silently erased. Findings F01 and F15 identify the candidate's remedy and express-reservation defects.

The Standards candidate contains 370 current rules against the opening 289: 81 additions and 14 substantive revisions, consolidations, or new cross-references, leaving 275 substantively preserved entries. Five apparent removed titles are accounted for by the Wilson/Koray detention-credit consolidation, Brecht/O'Neal protected-silence rule, religious-public-access consolidation, Greater Washington/Travelers ERISA treatment, and Southwest Marine/Chandris overlap. The remaining changed rules were reviewed against the current Records. All 370 entries have the four required fields; presence of those fields does not cure the omissions in F02 and F05.

All three candidate headers deliberately retain the synchronized published opening baseline: last completed OT1993, processed through June 30, 1994, edition September 28, 2026. Their substantive additions cover OT1994. Advancing that common publication header belongs to coordinated Commit; the staged header is not a failed audit item.

The candidates preserve distinctions that are easy to collapse: O'Neal's five-Justice narrow Chapman extension is separate from the three-Justice broader rationale; Morales does not adopt Stone's entire concurrence; Lopez does not adopt the Chief's six-route framework; Day's financing judgment has no controlling rationale; Chandris's general rule and thirty-percent guide have different supporting coalitions; the Miller clarification does not turn its conditional statutory question into an independently controlling holding; and Pinette, Chabad, and Rosenberger remain separate component-specific decisions. No additional vote or doctrine discrepancy was identified in those checks.

## Corrected matters and stale-version review

The current Record/Public Projection, generated Render Input, and public render were compared for each of the six specified matters. The following conclusions concern their present substantive content; they do not erase the separate documentation findings.

| Matter | Current comparison and provenance result |
|---|---|
| Interstate Commerce Commission v. Transcon Lines | The current liability/collection distinction, statutory enforcement rule, remedy, author, and named joins agree across the three artifacts. No competing live merits version was found. F06 identifies an inaccurate workload assertion in its internal assignment paragraph; it does not change the assignment or public decision. |
| Fargo Women's Health Organization v. Schafer | The completed February 13 decision and its component structure agree in the Record, chunk-2 input, and chunk-2 render. The earlier stop is not the current adjudication. F07 separately identifies later current Records that still describe its old status. |
| O'Neal v. McAninch | The February 21 decision is consistently projected in chunk 3. Its narrow controlling extension rests on the changed simulated Brecht baseline and is not expanded to all preserved constitutional habeas errors. The five-Justice controlling ground remains distinct from the three-Justice broader position. F07 addresses stale statements elsewhere about the previously unresolved matter. |
| United States v. Robertson | The current unanimous, Breyer-authored decision, interstate-enterprise ground, bounded remand, six preserved RICO issues, and separate drug-resentencing posture agree across Record/input/render. The chunk-5 render is present. F09 identifies the manifest's lingering per-curiam label; F07 identifies later Records' obsolete statements that Robertson was unadjudicated. |
| California Department of Corrections v. Morales | The user-directed replacement affirms 5–4 with O'Connor's controlling opinion. The Cavanaugh-based, Justice-specific reasons for the associate positions were checked, and Stone's broader separate framework remains noncontrolling. Commit `d086219b424d812aaa837fda9533629c69e33833` contains the substantive replacement of the former reversal without a controlling constitutional rationale; the current Public Projection matches that commit. The later difference in the file is the concise lineage statement. |
| Stone v. Immigration and Naturalization Service | The current assignment paragraph uses Stevens's ordinary senior-associate assignment discretion because Stone dissents; it does not impose the Chief-only Fit/Expansion procedure on Stevens. Commit `8d98261d33b6d39fda8a9ccc52ab5ad7ed3be02a` changes the assignment explanation without changing the judgment or Public Projection. Current input and render remain consistent. |

Four Morales entering-law snapshots and the Lopez/Travelers assembly copies that retain the former position now expressly identify themselves as superseded and point to the current correction. Frozen commitments and source handoffs preserve stage history; they do not compete with the corrected Record as law. Ignored scratch drafts likewise are not live authority. No unmarked alternative Morales holding was found in the live candidates, workspace, inputs, or outputs. The earlier Rosenberger missing terminal-divider defect is also resolved.

The requested broad assurance that no stale statement survives anywhere cannot be given: F07, F08, F09, and F11 identify surviving current-document statements, even though the six corrected substantive triplets agree. This report does not recommend deleting truthful, clearly labeled historical freezes or repository history.

The other genuine provenance reference, `13b19ee463d16fb4377d846e5b058599f886bed3`, also resolves. Review was limited to the truth of the concise claims and relevant object contents; no narrative commit archaeology was undertaken.

## Standing State and continuing matters

The complete Standing State candidate contains the permitted setting only: header, the correct nine-Justice OT1995 roster and seniority, 13 circuit allotments under the August 3, 1994 order, the existing referral practice, and 19 docket lines. It does not add a positions, dependencies, or history register. The assignment order correctly distinguishes the Chief's authority when in the component majority from the senior associate's authority otherwise.

Eight inherited continuing matters plus Kansas yield nine carryovers. The manifest's seven additional unscheduled entries omit Nebraska because Nebraska already has an inventory event; adding that continuing original proceeding and Kansas produces the same nine, not a count conflict.

| Continuing matter | Preserved stage |
|---|---|
| Zatko and the sixteen companion petitions | Fee rulings do not invent disposition of unresolved paid-status petitions. |
| Wyoming v. Oklahoma | Retained implementation jurisdiction continues. |
| Reynolds | Interim relief remains subject to further order; no invented expiration or final adjudication. |
| Grubbs | The administrative stay remains pending in its recorded posture. |
| Louisiana | Retained decree jurisdiction continues. |
| Delaware | The Master's accounting remains open. |
| Nebraska v. Wyoming | The resolved exceptions do not end the proceeding before Special Master Olpin on the admitted claims. |
| In re Anderson | The fee ruling does not decide the pending petition. |
| Kansas v. Colorado | Liability exceptions are resolved, but remedy proceedings before Special Master Littleworth remain; no final monetary amount is invented. |

The other ten docket lines are expressly user-added lower-court matters. Primary-source disposition passages were checked for the eight identified judgments: American Life League, Klinger, Love, SCLC, Bishop/Stokes, Hale, Voting Rights Coalition, and SSC. The candidate's concise descriptions agree. A. St. P. C. v. B. C. lacks identifying source details, and the user-reconstructed Bush lower judgment has not been supplied; the candidate explicitly preserves those two future-intake limits. They are not missing OT1994 decisions. Later lower-court dates belong to the next-term docket and are not backdated as OT1994 law. Ordinary appellate remands were not converted into pending Supreme Court matters.

## Complete matter coverage

Every row below received substantive review of votes, component coalitions, controlling grounds, precedent treatment, remedy, continuity, historical departures, and its candidate/render transmission. An em dash means no additional discrepancy was found for that matter; it is not an assertion that every external source was freshly retrieved. A finding concerning another document's stale reference is identified as such. Consolidated dockets remain one inventory matter and retain their component dispositions.

| No. | Matter and canonical Record | Chunk / effective date | Principal review focus | Findings |
|---:|---|---|---|---|
| 1 | [United States v. Shabani](../records/United_States_v_Shabani_merits_1994-11-01.md) | 1 / 1994-11-01 | §846 agreement/knowledge proof; no overt act; reserved appellate issues; unanimous construction. | — |
| 2 | [U.S. Bancorp Mortgage Co. v. Bonner Mall Partnership](../records/US_Bancorp_Mortgage_Co_v_Bonner_Mall_Partnership_mootness_vacatur_1994-11-08.md) | 1 / 1994-11-08 | §2106 authority after mootness, equitable settlement refusal and exceptional-circumstance limit; no automatic Rule 60 relief. | — |
| 3 | [Hess v. Port Authority Trans-Hudson Corp.](../records/Hess_v_Port_Authority_Trans_Hudson_Corp_merits_1994-11-14.md) | 1 / 1994-11-14 | Six-Justice entity-status ground; treasury and conditional consent distinctions; both employee actions. | — |
| 4 | [United States v. X-Citement Video, Inc.](../records/United_States_v_X_Citement_Video_Inc_merits_1994-11-29.md) | 1 / 1994-11-29 | Seven-Justice knowledge rule; six-Justice renewed-defense rationale; Stone fallback and two nonreach positions. | — |
| 5 | [Church of Scientology Flag Service Organization, Inc. v. City of Clearwater](../records/Church_of_Scientology_Flag_Service_Organization_Inc_v_City_of_Clearwater_merits_1994-12-05.md) | 1 / 1994-12-05 | Eight-Justice RFRA remand; statutory burdens; favorable relief/purpose/severability retained; ordinance exceptions and (f)/(g) distinct. | — |
| 6 | [Federal Election Commission v. NRA Political Victory Fund](../records/Federal_Election_Commission_v_NRA_Political_Victory_Fund_jurisdictional_dismissal_1994-12-06.md) | 1 / 1994-12-06 | Eight participants; six dismiss; independent authority and ratification timing; Stone and Stevens grounds distinct. | — |
| 7 | [Reich v. Collins](../records/Reich_v_Collins_merits_1994-12-06.md) | 1 / 1994-12-06 | Clear postpayment remedy, unlawful withdrawal, fair prospective change and actual lawful backward relief; no fixed refund. | — |
| 8 | [Brown v. Gardner](../records/Brown_v_Gardner_merits_1994-12-12.md) | 1 / 1994-12-12 | Causation rather than fault, continuing eligibility, consent/natural-progress limits and FTCA coordination. | — |
| 9 | [Nebraska Department of Revenue v. Loewenstein](../records/Nebraska_Department_of_Revenue_v_Loewenstein_merits_1994-12-12.md) | 1 / 1994-12-12 | Private return versus federal income; separate discrimination/borrowing objections; Stone limited nonjoin; add-back reserved. | — |
| 10 | [In re Baby K](../records/In_re_Baby_K_merits_1994-12-12.md) | 1 / 1994-12-12 | Acute emergency duty; transfer alternatives and conditions; informed refusal; capacity; direct state conflict and liability distinctions. | — |
| 11 | [Plakas v. Drinski](../records/Plakas_v_Drinski_merits_1995-01-09.md) | 1 / 1995-01-09 | Officer merits versus county ground; earlier conduct and supported record; no invented immunity/provocation finding. | — |
| 12 | [Interstate Commerce Commission v. Transcon Lines](../records/Interstate_Commerce_Commission_v_Transcon_Lines_merits_1995-01-10.md) | 1 / 1995-01-10 | Three controlling propositions; confined implementation; actual concessions and credit qualifications | F06 |
| 13 | [Tome v. United States](../records/Tome_v_United_States_merits_1995-01-10.md) | 2 / 1995-01-10 | Premotive requirement and all Rule 801 predicates; six/three split; alternate exceptions and harmlessness reserved. | — |
| 14 | [Young v. Northern Illinois Conference of United Methodist Church](../records/Young_v_Northern_Illinois_Conference_merits_1995-01-17.md) | 2 / 1995-01-17 | Ministerial-selection defense distinct from federal jurisdiction; eight-Justice formal vacatur versus Stone; no invented independent claim. | — |
| 15 | [Asgrow Seed Co. v. Winterboer](../records/Asgrow_Seed_Co_v_Winterboer_merits_1995-01-18.md) | 2 / 1995-01-18 | Saved-seed construction, unlawful-sale application, conditional notice nonreach, former-law and April 4 transition; distinct Stone and Stevens positions. | — |
| 16 | [United States v. Mezzanatto](../records/United_States_v_Mezzanatto_merits_1995-01-18.md) | 2 / 1995-01-18 | Impeachment waiver only; six-Justice presumption versus Stone burden; broader uses reserved; Rule 410 exceptions. | — |
| 17 | [American Airlines, Inc. v. Wolens](../records/American_Airlines_Inc_v_Wolens_merits_1995-01-18.md) | 2 / 1995-01-18 | Scalia absent; fraud preemption seven/five rationale; contract six/two; actual undertaking and outside policy limits. | — |
| 18 | [NationsBank of North Carolina, N.A. v. Variable Annuity Life Insurance Co. / Ludwig v. Variable Annuity Life Insurance Co.](../records/NationsBank_Ludwig_v_Variable_Annuity_Life_Insurance_Co_merits_1995-01-18.md) | 2 / 1995-01-18 | Both dockets; eight-Justice Chevron/statutory reasoning versus Stone; conditioned agency sales and §92 scope preserved. | — |
| 19 | [Allied-Bruce Terminix Cos. v. Dobson](../records/Allied_Bruce_Terminix_Cos_v_Dobson_merits_1995-01-18.md) | 2 / 1995-01-18 | Southland retained; commerce in fact/full power; assent, defenses and remedy; Scalia/Thomas state-court objection only. | — |
| 20 | [Schlup v. Delo](../records/Schlup_v_Delo_merits_1995-01-23.md) | 2 / 1995-01-23 | Six-Justice probability gateway, five-Justice statutory rationale, no automatic hearing/writ | F02 |
| 21 | [McKennon v. Nashville Banner Publishing Co.](../records/McKennon_v_Nashville_Banner_Publishing_Co_merits_1995-01-23.md) | 2 / 1995-01-23 | Actual-motive liability, actual would-discharge employer showing, ordinary remedy cutoff and extraordinary equity; corrected Stone remedy. | — |
| 22 | [Fargo Women’s Health Organization v. Schafer](../records/Fargo_Womens_Health_Organization_v_Schafer_merits_1995-02-13.md) | 2 / 1995-02-13 | Complete six-step access inquiry; separate vagueness, fault and remedies; no broad good-faith cure. | F07 (references elsewhere) |
| 23 | [Lebron v. National Railroad Passenger Corp.](../records/Lebron_v_National_Railroad_Passenger_Corp_merits_1995-02-21.md) | 2 / 1995-02-21 | Disavowed argument/reachability; permanent appointment control; O'Connor procedural ground; speech merits and relief reserved. | — |
| 24 | [Milwaukee Brewery Workers' Pension Plan v. Jos. Schlitz Brewing Co.](../records/Milwaukee_Brewery_Workers_Pension_Plan_v_Jos_Schlitz_Brewing_Co_merits_1995-02-21.md) | 2 / 1995-02-21 | Assumed first-payment date, actual payments, caps/mass withdrawal/default and prepayment qualifications | F07 |
| 25 | [O'Neal v. McAninch](../records/ONeal_v_McAninch_merits_1995-02-21.md) | 3 / 1995-02-21 | Five/three/two standard distinctions, seven-Justice vacatur, Justice-specific changed premises and conditional conviction-specific relief. | F07 (references elsewhere) |
| 26 | [United States v. National Treasury Employees Union](../records/United_States_v_National_Treasury_Employees_Union_merits_1995-02-22.md) | 3 / 1995-02-22 | Distinct rule/invalidity/class/Crane/nonparty coalitions; statutory qualifications | F07 |
| 27 | [Harris v. Alabama](../records/Harris_v_Alabama_merits_1995-02-22.md) | 3 / 1995-02-22 | Nine against fixed numerical weight, seven affirm sentence; actual findings/review; distinct Stone/Stevens objections | F07 |
| 28 | [Jerome B. Grubart, Inc. v. Great Lakes Dredge & Dock Co. / City of Chicago v. Great Lakes Dredge & Dock Co.](../records/Jerome_B_Grubart_Inc_v_Great_Lakes_Dredge_Dock_Co_merits_1995-02-22.md) | 3 / 1995-02-22 | Seven participants; five complete maritime test/two locality route; three holdings; no automatic liability/limitation | F07 |
| 29 | [Anderson v. Green](../records/Anderson_v_Green_decision_1995-02-22.md) | 3 / 1995-02-22 | Unripe approval-dependent case, pre-petition chronology and nonautomatic equitable vacatur | F07 |
| 30 | [Gustafson v. Alloyd Co.](../records/Gustafson_v_Alloyd_Co_merits_1995-02-28.md) | 3 / 1995-02-28 | Five-Justice bespoke-acquisition rule versus four broader rationale; statutory text/exceptions and nonliability remand. | — |
| 31 | [Arizona v. Evans](../records/Arizona_v_Evans_merits_1995-03-01.md) | 3 / 1995-03-01 | Seven jurisdiction/six merits; Ginsburg nonreach; attribution and objective reliance; paired irregularity evidence. | — |
| 32 | [Swint v. Chambers County Commission](../records/Swint_v_Chambers_County_Commission_merits_1995-03-01.md) | 3 / 1995-03-01 | Independent adequate-review/conclusiveness failures; Part IV reservation; county-only mandate | F07, F10, F15 |
| 33 | [Mastrobuono v. Shearson Lehman Hutton, Inc.](../records/Mastrobuono_v_Shearson_Lehman_Hutton_Inc_merits_1995-03-06.md) | 3 / 1995-03-06 | Integrated contract, actual NASD transition, independent preserved vacatur grounds and paid award | F07, F08 |
| 34 | [Curtiss-Wright Corp. v. Schoonejongen](../records/Curtiss_Wright_Corp_v_Schoonejongen_merits_1995-03-06.md) | 3 / 1995-03-06 | Corporate-person amendment procedure, actual adoption/ratification and ordinary benefits relief | F07, F08 |
| 35 | [Shalala v. Guernsey Memorial Hospital](../records/Shalala_v_Guernsey_Memorial_Hospital_merits_1995-03-06.md) | 3 / 1995-03-06 | Actual accounting/allocation ground, interpretive-rule boundary, PRM conditions and distinct method portion | F07, F08, F16 |
| 36 | [Ambassador Books & Video, Inc. v. City of Little Rock](../records/Ambassador_Books_Video_Inc_v_City_of_Little_Rock_merits_1995-03-20.md) | 3 / 1995-03-20 | Speech classification/avenues, conditional transition, categorical takings and attainder; seven/two plus unanimous components | F07, F08 |
| 37 | [Director, Office of Workers’ Compensation Programs v. Newport News Shipbuilding & Dry Dock Co.](../records/Director_Office_of_Workers_Compensation_Programs_v_Newport_News_Shipbuilding_and_Dry_Dock_Co_merits_1995-03-21.md) | 4 / 1995-03-21 | Nine affirm; O'Connor's Court explanation has eight joins including Stone, while Ginsburg remains judgment-only. | — |
| 38 | [Anderson v. Edwards](../records/Anderson_v_Edwards_merits_1995-03-22.md) | 4 / 1995-03-22 | Nine reverse under all five grounds: lawful assistance-unit formation versus imputed outsider income; mandatory inclusion without exclusivity; both equity regulations; distinct outsider-proration rules; independent construction without an agency trump. | — |
| 39 | [Swanner v. Anchorage Equal Rights Commission](../records/Swanner_v_Anchorage_Equal_Rights_Commission_merits_1995-03-27.md) | 4 / 1995-03-27 | Five (O'Connor, Scalia, Kennedy, Souter, Thomas) vacate the prospective federal RFRA determination; Stone, Stevens, Ginsburg and Breyer dissent on application-specific justification. | — |
| 40 | [Qualitex Co. v. Jacobson Products Co.](../records/Qualitex_Co_v_Jacobson_Products_Co_merits_1995-03-28.md) | 4 / 1995-03-28 | Nine support source-identifying, acquired-distinctive, nonfunctional color eligibility. | — |
| 41 | [Oklahoma Tax Commission v. Jefferson Lines, Inc.](../records/Oklahoma_Tax_Commission_v_Jefferson_Lines_Inc_merits_1995-04-03.md) | 4 / 1995-04-03 | Seven reverse; Kennedy's five support each Complete Auto component, Scalia/Thomas concur on their narrower method, O'Connor/Breyer dissent on external apportionment. | F01 |
| 42 | [Plaut v. Spendthrift Farm, Inc.](../records/Plaut_v_Spendthrift_Farm_Inc_merits_1995-04-18.md) | 4 / 1995-04-18 | Seven affirm, Stevens/Ginsburg dissent; all seven directly support the narrow existing Morgan Stanley application. | — |
| 43 | [Shalala v. Whitecotton](../records/Shalala_v_Whitecotton_merits_1995-04-18.md) | 4 / 1995-04-18 | Nine support first onset in the applicable interval, with significant aggravation and actual causation distinct. | F08 |
| 44 | [Freightliner Corp. v. Myrick](../records/Freightliner_Corp_v_Myrick_merits_1995-04-18.md) | 4 / 1995-04-18 | Nine affirm; Ginsburg's rationale has eight, Scalia remains judgment-only without an invented separate explanation. | — |
| 45 | [Heintz v. Jenkins](../records/Heintz_v_Jenkins_merits_1995-04-18.md) | 4 / 1995-04-18 | Nine support FDCPA coverage of regularly collecting attorneys including litigation, subject to actual statutory exceptions and defenses. | — |
| 46 | [Lanphere & Urbaniak v. Colorado](../records/Lanphere_and_Urbaniak_v_Colorado_merits_1995-04-18.md) | 4 / 1995-04-18 | Seven reverse; O'Connor/Scalia dissent. | — |
| 47 | [Celotex Corp. v. Edwards](../records/Celotex_Corp_v_Edwards_merits_1995-04-19.md) | 4 / 1995-04-19 | Seven reverse; six associates support actual relatedness, sufficient interim authority and qualified orderly review. | — |
| 48 | [McIntyre v. Ohio Elections Commission](../records/McIntyre_v_Ohio_Elections_Commission_merits_1995-04-19.md) | 4 / 1995-04-19 | Eight reverse; seven adopt exacting scrutiny, Thomas has a distinct ground, Scalia dissents. | — |
| 49 | [Stone v. Immigration and Naturalization Service](../records/Stone_v_Immigration_and_Naturalization_Service_merits_1995-04-19.md) | 5 / 1995-04-19 | Current five-to-four jurisdictional affirmance preserves separate original-order and reconsideration review periods. | — |
| 50 | [Kyles v. Whitley](../records/Kyles_v_Whitley_merits_1995-04-19.md) | 5 / 1995-04-19 | Six-to-three reversal; cumulative Brady materiality and investigative-team responsibility remain controlling, without a second duplicative harmless-error screen. | — |
| 51 | [Rubin v. Coors Brewing Co.](../records/Rubin_v_Coors_Brewing_Co_merits_1995-04-19.md) | 5 / 1995-04-19 | Nine affirm; Kennedy's eight-Justice rationale and Stevens's judgment concurrence remain distinct. | — |
| 52 | [California Department of Corrections v. Morales](../records/California_Department_of_Corrections_v_Morales_merits_1995-04-25.md) | 5 / 1995-04-25 | Current user-revised five-to-four AFFIRMANCE controls: O'Connor with Stone, Stevens, Souter and Ginsburg; Kennedy dissent with Scalia, Thomas and Breyer. | — |
| 53 | [United States v. Williams](../records/United_States_v_Williams_merits_1995-04-25.md) | 5 / 1995-04-25 | Seven support the express refund waiver; the separate taxpayer-definition ground has five, excluding Stone and Scalia. | — |
| 54 | [United States v. Lopez](../records/United_States_v_Lopez_merits_1995-04-26.md) | 5 / 1995-04-26 | Five-to-four bounded invalidation through Kennedy. | — |
| 55 | [New York State Conference of Blue Cross & Blue Shield Plans v. Travelers Insurance Co. / Pataki v. Travelers Insurance Co. / Hospital Association of New York State v. Travelers Insurance Co.](../records/New_York_State_Conference_of_Blue_Cross_Blue_Shield_Plans_v_Travelers_Insurance_Co_merits_1995-04-26.md) | 5 / 1995-04-26 | Nine support all three reviewed commercial/HMO no-preemption applications. | — |
| 56 | [United States v. Harris](../records/United_States_v_Harris_merits_1995-04-27.md) | 5 / 1995-04-27 | Nine reject the challenges. | — |
| 57 | [United States v. Robertson](../records/United_States_v_Robertson_merits_1995-05-01.md) | 5 / 1995-05-01 | Completed nine-to-zero direct-enterprise-commerce holding through Breyer. | F09; F07 (references elsewhere) |
| 58 | [United States v. Pinson](../records/United_States_v_Pinson_merits_1995-05-08.md) | 5 / 1995-05-08 | Seven find the targeted concealed-home-information examination a search; six join the justification analysis apart from Stone. | F07 |
| 59 | [Kansas v. Colorado](../records/Kansas_v_Colorado_original_exceptions_1995-05-15.md) | 5 / 1995-05-15 | Nine support seven exceptions dispositions, three unexcepted components and recommittal. | F07 |
| 60 | [Hubbard v. United States](../records/Hubbard_v_United_States_merits_1995-05-15.md) | 5 / 1995-05-15 | Seven reverse counts V–VII; six support entity construction and full incompatible Bramblett displacement, while Stone joins a narrower ground. | F07 |
| 61 | [City of Edmonds v. Oxford House, Inc.](../records/City_of_Edmonds_v_Oxford_House_merits_1995-05-15.md) | 6 / 1995-05-15 | Six-to-three reversal. | — |
| 62 | [Reynoldsville Casket Co. v. Hyde](../records/Reynoldsville_Casket_Co_v_Hyde_merits_1995-05-15.md) | 6 / 1995-05-15 | Nine reverse, with seven in Breyer's rationale and Kennedy/O'Connor judgment-only. | — |
| 63 | [Day v. Holahan](../records/Day_v_Holahan_merits_1995-05-15.md) | 6 / 1995-05-15 | Responsive financing falls five-to-four but the four-Justice Kennedy framework plus Stone's different ground do not yield a Marks synthesis. | — |
| 64 | [U.S. Term Limits, Inc. v. Thornton / Bryant v. Hill](../records/US_Term_Limits_v_Thornton_Bryant_v_Hill_merits_1995-05-22.md) | 6 / 1995-05-22 | Six-to-three Article I exclusive-qualifications holding. | — |
| 65 | [Wilson v. Arkansas](../records/Wilson_v_Arkansas_merits_1995-05-22.md) | 6 / 1995-05-22 | Nine support constitutional announcement as part of reasonableness with danger, futility, escape and evidence-destruction qualifications. | F12 |
| 66 | [First Options of Chicago, Inc. v. Kaplan](../records/First_Options_of_Chicago_Inc_v_Kaplan_merits_1995-05-22.md) | 6 / 1995-05-22 | Nine affirm antecedent consent/delegation and ordinary appellate review. | — |
| 67 | [Kelley v. Board of Trustees of the University of Illinois](../records/Kelley_v_Board_of_Trustees_of_the_University_of_Illinois_merits_1995-05-22.md) | 6 / 1995-05-22 | Nine support programwide Title IX participation under alternative routes and an independent Hogan equal-protection application grounded in actual inequality and restructuring. | F17 |
| 68 | [Nebraska v. Wyoming](../records/Nebraska_v_Wyoming_original_exceptions_1995-05-30.md) | 6 / 1995-05-30 | All four Wyoming exceptions are overruled nine-to-zero; the federal Fourth Cross-Claim is admitted eight-to-one, Thomas dissenting. | F13 |
| 69 | [North Star Steel Co. v. Thomas / Crown Cork & Seal Co., Inc. v. United Steelworkers of America, AFL-CIO-CLC](../records/North_Star_Steel_v_Thomas_and_Crown_Cork_merits_1995-05-30.md) | 6 / 1995-05-30 | Nine affirm both limitations judgments; Souter's rationale has eight, Scalia judgment-only. | F14 |
| 70 | [Garlotte v. Fordice](../records/Garlotte_v_Fordice_merits_1995-05-30.md) | 6 / 1995-05-30 | Eight-to-one aggregate-custody rule, Thomas dissenting. | — |
| 71 | [United States v. Wellons](../records/United_States_v_Wellons_merits_1995-05-30.md) | 6 / 1995-05-30 | Nine support Stone's vehicle and personal-luggage privacy distinctions. | — |
| 72 | [Reno v. Koray](../records/Reno_v_Koray_merits_1995-06-05.md) | 6 / 1995-06-05 | Seven-to-two federal release-status rule; Stone and Stevens have separate dissents, Ginsburg's notice observation reserves an unpresented issue. | F03 |
| 73 | [Metropolitan Washington Airports Authority v. Hechinger](../records/Metropolitan_Washington_Airports_Authority_v_Hechinger_merits_1995-06-05.md) | 7 / 1995-06-05 | Nine-Justice Stevens agency-plus-operative-control holding is distinct from Stone’s unjoined independent Article I ground. | F05 |
| 74 | [Missouri v. Jenkins](../records/Missouri_v_Jenkins_merits_1995-06-12.md) | 7 / 1995-06-12 | Five-Justice Souter/Stone/Stevens/Ginsburg/Breyer affirmance of both salary and quality-education components remains supported by injury-linked repair and personnel necessity. | F05 |
| 75 | [Ryder v. United States](../records/Ryder_v_United_States_merits_1995-06-12.md) | 7 / 1995-06-12 | Unanimous timely direct appointments challenge produces fresh Article 66 review by a lawfully appointed court. | — |
| 76 | [City of Milwaukee v. Cement Division, National Gypsum Co.](../records/City_of_Milwaukee_v_Cement_Division_National_Gypsum_Co_merits_1995-06-12.md) | 7 / 1995-06-12 | Eight participating Justices; Breyer’s nonparticipation is not supplied an invented reason. | — |
| 77 | [Adarand Constructors, Inc. v. Peña](../records/Adarand_Constructors_Inc_v_Pena_merits_1995-06-12.md) | 7 / 1995-06-12 | Five-Justice affirmance preserves the actual Metro Broadcasting intermediate-scrutiny rule through Stone’s expressly approved fallback branch; his preferred replacement framework is not adopted without five votes. | — |
| 78 | [Wilton v. Seven Falls Co.](../records/Wilton_v_Seven_Falls_Co_merits_1995-06-12.md) | 7 / 1995-06-12 | Eight-Justice declaration-only Brillhart/§2201 discretion is distinguished from coercive-action Colorado River doctrine. | — |
| 79 | [Metropolitan Stevedore Co. v. Rambo](../records/Metropolitan_Stevedore_Co_v_Rambo_merits_1995-06-12.md) | 7 / 1995-06-12 | Eight-Justice §22 rule permits changed earning-capacity treatment for a nonscheduled disability despite unchanged physical condition; Stevens’s dissent remains separate. | — |
| 80 | [Johnson v. Jones](../records/Johnson_v_Jones_merits_1995-06-12.md) | 7 / 1995-06-12 | Unanimous denial of immediate appeal of record-sufficiency/participation disputes preserves separable Mitchell legal review on assumed facts. | — |
| 81 | [Kimberlin v. Quinlan](../records/Kimberlin_v_Quinlan_merits_1995-06-12.md) | 7 / 1995-06-12 | Unanimous vacatur of the direct-evidence directive concerns a separable legal evidentiary barrier, not interlocutory review of motive sufficiency. | — |
| 82 | [Commissioner v. Schleier](../records/Commissioner_v_Schleier_merits_1995-06-14.md) | 7 / 1995-06-14 | Six votes reverse, but the personal-injury causation rationale has five (Stevens/Stone/Kennedy/Ginsburg/Breyer); Scalia joins judgment only. | — |
| 83 | [Chandris, Inc. v. Latsis](../records/Chandris_Inc_v_Latsis_merits_1995-06-14.md) | 7 / 1995-06-14 | Unanimous new-trial result does not imply unanimous adoption of the O’Connor framework. | — |
| 84 | [Witte v. United States](../records/Witte_v_United_States_merits_1995-06-14.md) | 7 / 1995-06-14 | Eight uphold later prosecution, with distinct six-Justice constitutional and sentencing-coordination coalitions; Stevens dissents on the former while joining the latter, and Kennedy’s coordination refusal is preserved. | — |
| 85 | [Gutierrez de Martinez v. Lamagno](../records/Gutierrez_de_Martinez_v_Lamagno_merits_1995-06-14.md) | 8 / 1995-06-14 | Six permit judicial scope review, three dissent. | — |
| 86 | [Oklahoma Tax Commission v. Chickasaw Nation](../records/Oklahoma_Tax_Commission_v_Chickasaw_Nation_merits_1995-06-14.md) | 8 / 1995-06-14 | Fuel tax is unanimously barred on tribal legal incidence; the income component divides five to four on off-Indian-country residence. | — |
| 87 | [Sandin v. Conner](../records/Sandin_v_Conner_merits_1995-06-19.md) | 8 / 1995-06-19 | Five adopt Breyer’s sufficient, nonexclusive whole-law constraint plus meaningful-deprivation rule and remand; they do not all adopt either four-Justice concurrence’s affirmative application. | — |
| 88 | [United States v. Gaudin](../records/United_States_v_Gaudin_merits_1995-06-19.md) | 8 / 1995-06-19 | All nine require the jury to decide the conceded §1001 materiality element beyond reasonable doubt. | — |
| 89 | [Vimar Seguros y Reaseguros, S.A. v. M/V Sky Reefer](../records/Vimar_Seguros_y_Reaseguros_SA_v_MV_Sky_Reefer_merits_1995-06-19.md) | 8 / 1995-06-19 | Seven-to-one participating Court enforces the arbitration agreement while retaining jurisdiction; Breyer does not participate. | — |
| 90 | [Hurley v. Irish-American Gay, Lesbian and Bisexual Group of Boston](../records/Hurley_v_Irish_American_Gay_Lesbian_and_Bisexual_Group_of_Boston_merits_1995-06-19.md) | 8 / 1995-06-19 | Unanimous protection of private expressive selection includes a varied parade without one coherent theme. | F04 |
| 91 | [National Private Truck Council, Inc. v. Oklahoma Tax Commission](../records/National_Private_Truck_Council_Inc_v_Oklahoma_Tax_Commission_merits_1995-06-19.md) | 8 / 1995-06-19 | Unanimous §1983 tax-equity restraint operates within the cause of action and does not give §1341 jurisdictional effect in state court. | — |
| 92 | [United States v. Aguilar](../records/United_States_v_Aguilar_merits_1995-06-21.md) | 8 / 1995-06-21 | Six-Justice §1503 nexus disposition, eight-Justice §2232(c) construction and nine-vote constitutional rejection are distinguished, with only eight adopting the constitutional rationale. | F05 |
| 93 | [Florida Bar v. Went For It, Inc.](../records/Florida_Bar_v_Went_For_It_Inc_merits_1995-06-21.md) | 8 / 1995-06-21 | Kennedy/Stone/Stevens/Souter/Ginsburg invalidate the actual 30-day direct-mail restriction on the assembled record; the four dissenters remain separate. | — |
| 94 | [Vernonia School District 47J v. Acton](../records/Vernonia_School_District_47J_v_Acton_merits_1995-06-26.md) | 8 / 1995-06-26 | Five-Justice federal validity judgment is separated from unanimous threshold agreement and the eight-Justice rejection of the facial prescription objection. | — |
| 95 | [Rosenberger v. Rector and Visitors of the University of Virginia](../records/Rosenberger_v_Rector_and_Visitors_of_the_University_of_Virginia_merits_1995-06-29.md) | 8 / 1995-06-29 | Five-Justice viewpoint-discrimination and program-specific Establishment holdings preserve Kennedy’s actual forum/controlled-payment boundaries. | — |
| 96 | [Babbitt v. Sweet Home Chapter of Communities for a Great Oregon](../records/Babbitt_v_Sweet_Home_Chapter_of_Communities_for_a_Great_Oregon_merits_1995-06-29.md) | 8 / 1995-06-29 | Seven uphold the statutory harm construction and causation/boundary components; six, excluding Stone, adopt the separate deference ground. | — |
| 97 | [Miller v. Johnson / Abrams v. Johnson / United States v. Johnson](../records/Miller_and_consolidated_merits_1995-06-29.md) | 9 / 1995-06-29 | Reviewed all seven controlling holdings and Stone’s full unjoined framework. | — |
| 98 | [Capitol Square Review and Advisory Board v. Pinette](../records/Pinette_merits_1995-06-29.md) | 9 / 1995-06-29 | Seven affirm the actual unconditioned preliminary injunction; Stevens and Ginsburg have distinct dissents. | — |
| 99 | [Chabad-Lubavitch of Georgia v. Miller](../records/Chabad_Lubavitch_v_Miller_merits_1995-06-29.md) | 9 / 1995-06-29 | Eight affirm reversal of state summary judgment on Count II; Stevens dissents. | — |

The two additional [Vaccine Table](../records/Vaccine_Injury_Table_regulatory_effectiveness_1995-03-10.md) and [Plant Variety Protection Act](../records/Plant_Variety_Protection_Act_Amendments_statutory_effectiveness_1995-04-04.md) source-admission Records were also reviewed. Their effective dates, application triggers, grandfathering, reservations, and candidate effects were checked independently of the 99 judicial rows. Neither was mistaken for a Court holding or given an invented Court render.

## External-access limitations

An HTTP 200 response is reachability evidence, not proof of a legal proposition. The 104 URLs below did not return a successful response during the automated access check. A denial, rate limit, or timeout is not classified as a missing authority, and no 404/410 defect was found. Local source handoffs and alternative primary texts were available for the substantive review; this list preserves the access limitation instead of silently treating it as successful verification.

| Source URL | Observed access result |
|---|---|
| [app.midpage.ai/document/allied-bruce-terminix-v-dobson-1662045](<https://app.midpage.ai/document/allied-bruce-terminix-v-dobson-1662045>) | HTTP 429 |
| [app.midpage.ai/document/william-m-kelley-joseph-s-677868](<https://app.midpage.ai/document/william-m-kelley-joseph-s-677868>) | HTTP 429 |
| [app.midpage.ai/document/wolens-v-american-airlines-inc-2035579](<https://app.midpage.ai/document/wolens-v-american-airlines-inc-2035579>) | HTTP 429 |
| [archive.org/details/micro_IA40385013_0510](<https://archive.org/details/micro_IA40385013_0510>) | The read operation timed out |
| [archive.org/details/micro_IA40385013_0512](<https://archive.org/details/micro_IA40385013_0512>) | The read operation timed out |
| [archive.org/details/micro_IA40385013_0551](<https://archive.org/details/micro_IA40385013_0551>) | The read operation timed out |
| [archive.org/details/micro_IA40385013_0554](<https://archive.org/details/micro_IA40385013_0554>) | The read operation timed out |
| [archive.org/details/micro_IA40385013_0558](<https://archive.org/details/micro_IA40385013_0558>) | The read operation timed out |
| [archive.org/details/micro_IA40385013_0559](<https://archive.org/details/micro_IA40385013_0559>) | The read operation timed out |
| [archive.org/details/micro_IA40385013_0560](<https://archive.org/details/micro_IA40385013_0560>) | The read operation timed out |
| [archive.org/details/micro_IA40385013_0563](<https://archive.org/details/micro_IA40385013_0563>) | The read operation timed out |
| [archive.org/details/micro_IA40385013_0565](<https://archive.org/details/micro_IA40385013_0565>) | The read operation timed out |
| [archive.org/details/micro_IA40385013_0600](<https://archive.org/details/micro_IA40385013_0600>) | The read operation timed out |
| [archive.org/details/micro_IA40385013_0613](<https://archive.org/details/micro_IA40385013_0613>) | The read operation timed out |
| [archive.org/details/micro_IA40386002_0673](<https://archive.org/details/micro_IA40386002_0673>) | The read operation timed out |
| [archive.org/details/micro_IA40386002_0698](<https://archive.org/details/micro_IA40386002_0698>) | The read operation timed out |
| [archive.org/details/micro_IA40386002_0800](<https://archive.org/details/micro_IA40386002_0800>) | The read operation timed out |
| [archive.org/details/micro_IA40386002_1197](<https://archive.org/details/micro_IA40386002_1197>) | The read operation timed out |
| [archive.org/details/micro_IA40386003_1788](<https://archive.org/details/micro_IA40386003_1788>) | The read operation timed out |
| [archive.org/details/micro_IA40386007_1451](<https://archive.org/details/micro_IA40386007_1451>) | The read operation timed out |
| [archive.org/details/micro_IA40386012_0076](<https://archive.org/details/micro_IA40386012_0076>) | The read operation timed out |
| [archive.org/details/micro_IA40386012_0394](<https://archive.org/details/micro_IA40386012_0394>) | The read operation timed out |
| [archive.org/details/micro_IA40386012_0701](<https://archive.org/details/micro_IA40386012_0701>) | The read operation timed out |
| [archive.org/details/micro_IA40386012_0721](<https://archive.org/details/micro_IA40386012_0721>) | The read operation timed out |
| [archive.org/details/micro_IA40386012_0738](<https://archive.org/details/micro_IA40386012_0738>) | The read operation timed out |
| [archive.org/details/micro_IA40386012_0804](<https://archive.org/details/micro_IA40386012_0804>) | The read operation timed out |
| [archive.org/details/micro_IA40386012_0864](<https://archive.org/details/micro_IA40386012_0864>) | The read operation timed out |
| [archive.org/details/micro_IA40386012_1752](<https://archive.org/details/micro_IA40386012_1752>) | The read operation timed out |
| [archive.org/details/micro_IA40386012_1825](<https://archive.org/details/micro_IA40386012_1825>) | The read operation timed out |
| [archive.org/details/micro_IA40386012_2001](<https://archive.org/details/micro_IA40386012_2001>) | The read operation timed out |
| [archive.org/details/us-supreme-court](<https://archive.org/details/us-supreme-court>) | The read operation timed out |
| [law.justia.com/cases/california/supreme-court/3d/39/464.html](<https://law.justia.com/cases/california/supreme-court/3d/39/464.html>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F2/982/486/137058/](<https://law.justia.com/cases/federal/appellate-courts/F2/982/486/137058/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/12/154/528248/](<https://law.justia.com/cases/federal/appellate-courts/F3/12/154/528248/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/13/934/631993/](<https://law.justia.com/cases/federal/appellate-courts/F3/13/934/631993/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/16/1537/492197/](<https://law.justia.com/cases/federal/appellate-courts/F3/16/1537/492197/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/17/374/567311/](<https://law.justia.com/cases/federal/appellate-courts/F3/17/374/567311/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/18/1034/531004/](<https://law.justia.com/cases/federal/appellate-courts/F3/18/1034/531004/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/2/899/616218/](<https://law.justia.com/cases/federal/appellate-courts/F3/2/899/616218/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/20/45/523011/](<https://law.justia.com/cases/federal/appellate-courts/F3/20/45/523011/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/21/558/622869/](<https://law.justia.com/cases/federal/appellate-courts/F3/21/558/622869/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/25/250/572049/](<https://law.justia.com/cases/federal/appellate-courts/F3/25/250/572049/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/26/95/619021/](<https://law.justia.com/cases/federal/appellate-courts/F3/26/95/619021/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/28/86/581336/](<https://law.justia.com/cases/federal/appellate-courts/F3/28/86/581336/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/29/727/480225/](<https://law.justia.com/cases/federal/appellate-courts/F3/29/727/480225/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/3/225/539495/](<https://law.justia.com/cases/federal/appellate-courts/F3/3/225/539495/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/31/581/592042/](<https://law.justia.com/cases/federal/appellate-courts/F3/31/581/592042/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/32/53/633439/](<https://law.justia.com/cases/federal/appellate-courts/F3/32/53/633439/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/34/1356/552077/](<https://law.justia.com/cases/federal/appellate-courts/F3/34/1356/552077/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/41/934/563873/](<https://law.justia.com/cases/federal/appellate-courts/F3/41/934/563873/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/6/789/576708/](<https://law.justia.com/cases/federal/appellate-courts/F3/6/789/576708/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/8/175/614852/](<https://law.justia.com/cases/federal/appellate-courts/F3/8/175/614852/>) | HTTP 403 |
| [law.justia.com/cases/federal/appellate-courts/F3/9/64/540228/](<https://law.justia.com/cases/federal/appellate-courts/F3/9/64/540228/>) | HTTP 403 |
| [law.justia.com/cases/oklahoma/supreme-court/1994/20198.html](<https://law.justia.com/cases/oklahoma/supreme-court/1994/20198.html>) | HTTP 403 |
| [openjurist.org/11/f3d/755](<https://openjurist.org/11/f3d/755>) | The read operation timed out |
| [openjurist.org/13/f3d/1170](<https://openjurist.org/13/f3d/1170>) | The read operation timed out |
| [openjurist.org/29/f3d/727](<https://openjurist.org/29/f3d/727>) | The read operation timed out |
| [openjurist.org/31/f3d/581](<https://openjurist.org/31/f3d/581>) | The read operation timed out |
| [openjurist.org/35/f3d/265/kelley-v-board-of-trustees-w-e](<https://openjurist.org/35/f3d/265/kelley-v-board-of-trustees-w-e>) | HTTP 502 |
| [openjurist.org/36/f3d/97](<https://openjurist.org/36/f3d/97>) | The read operation timed out |
| [supreme.justia.com/cases/federal/us/301/397/](<https://supreme.justia.com/cases/federal/us/301/397/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/450/24/](<https://supreme.justia.com/cases/federal/us/450/24/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/482/423/](<https://supreme.justia.com/cases/federal/us/482/423/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/497/37/](<https://supreme.justia.com/cases/federal/us/497/37/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/513/179/](<https://supreme.justia.com/cases/federal/us/513/179/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/513/18/](<https://supreme.justia.com/cases/federal/us/513/18/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/513/527/](<https://supreme.justia.com/cases/federal/us/513/527/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/513/557/](<https://supreme.justia.com/cases/federal/us/513/557/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/514/122/](<https://supreme.justia.com/cases/federal/us/514/122/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/514/143/](<https://supreme.justia.com/cases/federal/us/514/143/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/514/268/](<https://supreme.justia.com/cases/federal/us/514/268/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/514/673/](<https://supreme.justia.com/cases/federal/us/514/673/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/514/73/](<https://supreme.justia.com/cases/federal/us/514/73/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/515/1/](<https://supreme.justia.com/cases/federal/us/515/1/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/515/277/](<https://supreme.justia.com/cases/federal/us/515/277/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/515/29/](<https://supreme.justia.com/cases/federal/us/515/29/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/515/291/](<https://supreme.justia.com/cases/federal/us/515/291/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/515/321/](<https://supreme.justia.com/cases/federal/us/515/321/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/515/347/](<https://supreme.justia.com/cases/federal/us/515/347/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/515/389/](<https://supreme.justia.com/cases/federal/us/515/389/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/515/50/](<https://supreme.justia.com/cases/federal/us/515/50/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/515/528/](<https://supreme.justia.com/cases/federal/us/515/528/>) | HTTP 403 |
| [supreme.justia.com/cases/federal/us/515/582/](<https://supreme.justia.com/cases/federal/us/515/582/>) | HTTP 403 |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?edition=1994&num=0&req=granuleid%3AUSC-1994-title28-section2244>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-1994-title28-section151&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-1994-title28-section2106&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-1994-title7-section2567&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title26-section9010&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title26-section9040&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title28-section2101&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title28-section2111&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title28-section2243&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title28-section2254&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title28-section518&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title29-section1399&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title29-section626&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title30-section932&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title33-section907&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title33-section919&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title33-section923&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title49-section24301&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title49-section24302&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [uscode.house.gov/view.xhtml](<https://uscode.house.gov/view.xhtml?req=granuleid:USC-1994-title5-section556&num=0&edition=1994>) | &lt;urlopen error _ssl.c:1063: The handshake operation timed out&gt; |
| [www.cambridge.org/core/books/abs/minority-representation-and-the-quest-for-voting-equality/right-to-vote-and-the-right-to-representation/5223F70CBD862DEEE5634BA1F102E638](<https://www.cambridge.org/core/books/abs/minority-representation-and-the-quest-for-voting-equality/right-to-vote-and-the-right-to-representation/5223F70CBD862DEEE5634BA1F102E638>) | HTTP 403 |

## Final boundary verification and operator handoff

SHA-256 fingerprints of all 3,547 preexisting protected files under the governing and term scopes were compared before delivery. The sole changed protected file is `terms/OT1994/close/AUDIT.md`; no protected file was added or deleted. The case briefs, foundation, state, tools, Records, freezes, workspace, inputs, renders, candidates, and pass notes remain byte-identical to the audit-start copies. All final report local links resolve, the coverage table contains exactly matters 1–99, and the severity total agrees with the 17 numbered findings. No `git add`, commit, push, checkout, or other Git command was run.

This audit changes no case, no legal rule, no vote, and no public render. Every numbered finding remains open for a separate authorized correction task. The operator verifies and commits after reviewing this report.

**Operator summary: FAIL — 0 high, 3 medium, 14 low findings (17 total).**
