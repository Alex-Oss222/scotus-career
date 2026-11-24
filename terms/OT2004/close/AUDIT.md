# October Term 2004 confirming re-audit

**Audit date:** November 23, 2026.
**Repair reviewed:** 66978bf0; parent 84528e911b940788f66d1c78a6a90b02b67311ae.
**Disposition:** F1-F4 are resolved. The prescribed deterministic checks pass, and the legal-substance audit remains clean. One Low-severity discrepancy remains: F5, additional editing-history narratives in twelve internal Records. The term is not ready for Close Commit.

## Scope and method

This is the confirming re-audit of the operator's repairs. The required command, `python tools/check_term.py OT2004`, returned `OK: OT2004; 0 warning(s)`. The remaining prescribed deterministic checks were rerun before the focused legal-substance review. The checker was rerun after this audit was replaced with the same result.

Read-only `git cat-file` operations establish that the repair changes exactly five files: the Jackson, Sabree, Shepard and Sherrill Records and the ledger. Each change exactly implements a location specified in F4. The four Public Projections are byte-identical to their parent versions. All 140 current Markdown files in records, render-inputs, output, workspace and close matched the repair blobs before this audit was replaced.

The governing foundation tree, opening state tree, and OT2004 briefs, runtime, freeze, entering-law and case-list are also unchanged between parent and repair and match the working files: respectively 9, 27, 11, 273, 404, 85 and 1 tracked files. The repair leaves the candidate trackers, every public render, opinion table, assignment statement and substantive decision unchanged. This supports carrying forward the preceding complete audit of all 105 judicial events and the admitted statutory source. This pass independently reviews the operative qualifications surrounding the repairs and the additional metadata findings; it does not represent that the whole term was adjudicated or researched again.

Only the expressly permitted checker and read-only `git cat-file` operations used Git. No prohibited directory or jurisprudence file was accessed. This task replaces only this audit; it changes no Record, public copy, tracker, governing file or frozen handoff.

## Verification of previous findings

| Finding | Current location | Fresh verification | Status |
|---|---|---|---|
| F1 - Medium | [manifest.md](../workspace/manifest.md), line 3 | The summary and all event rows agree: 105 completed scheduled events, zero open, zero stopped and zero scheduled carry-forwards. Three separate unscheduled carryovers remain. | Resolved |
| F2 - Medium | [ledger.md](../workspace/ledger.md), lines 7-112 | One eight-column table contains all 106 Records, numbered consecutively and ordered by effective date and case name. Every Record-derived field agrees with its source. Gonzalez remains entry 95 and McCreary entry 102. | Resolved |
| F3 - Low | [continuity.md](../workspace/continuity.md), line 7; [neutral-projection.md](../workspace/neutral-projection.md), line 7 | Both accurately state that candidates are staged and audit/publication remain pending. The repair does not alter these paragraphs. | Resolved |
| F4 - Low | [Jackson](../records/jackson-v-birmingham-board-of-education_merits_2005-03-29.md), lines 4 and 14 | The required lineage value is `Original decision.` The identified entering-law wording is replaced exactly as requested; surrounding substance is unchanged. | Resolved |
| F4 - Low | [Sabree](../records/sabree-ex-rel-sabree-v-richman_merits_2005-03-29.md), line 4 | The required lineage value is `Original decision.` Both enumerated editing narratives and their receipt reference are removed. | Resolved |
| F4 - Low | [Shepard](../records/shepard-v-united-states_merits_2005-03-07.md), former lines 48-49 | The standalone completeness-edit paragraph and following blank line are removed. Current line 48 starts the audit annex. All operative terms survive unchanged. | Resolved |
| F4 - Low | [Sherrill](../records/city-of-sherrill-v-oneida-indian-nation_merits_2005-03-29.md), line 68 | Both requested substitutions are exact. The intervening charging, forfeiture, jury-waiver and binding-Booker rules remain byte-identical. | Resolved |
| F4 - Low | [ledger.md](../workspace/ledger.md), lines 53-54 | Only the Jackson and Sabree lineage cells change, each to `Original decision.` All other cells and ordering remain unchanged. | Resolved |

The exact F4 replacements were reconstructed from parent bytes and compared with the repair. Jackson and Sabree preserve their existing LF endings; Shepard, Sherrill and the ledger preserve CRLF. No line-ending conversion occurred. All 106 Records retain the four required opening labels. Their standard original-decision values are compliant.

## Deterministic results

| Check | Result |
|---|---|
| Required checker and opening baseline | Passed with zero warnings, including opening Holdings-volume synchronization, runtime-split freshness, Record structure, generated-input identity and public workflow checks. |
| Inventory and coverage | All 105 inventory rows match the manifest's number, chunk, identity, date, event type, category and area. Each judicial event has one unique Record. The 106th Record admits section 703. |
| Record, input and render reconciliation | All Public Projection bodies match their generated inputs. All 105 public events have matching dated docket rows, headings and closing boundaries. Chunk counts are 13, 11, 5, 7, 11, 9, 8, 11, 15 and 15. |
| Effective order and projections | All 106 ledger rows match their Record fields and effective ordering. Continuity covers all 106 events/sources with correct dates; neutral projection references all 106. Same-date continuity ordering creates no chronology conflict. |
| Participation and vote arithmetic | All 105 judicial events establish nine participants. The 131 explicit Record margin/roster comparisons and 156 render comparisons pass. Gonzalez's prose-only disposition, Devenpeck's distinct formal dispositions and the undisclosed procedural forms were separately reconciled. |
| Opinion assignment | Sixty-one explicit eligible-set and minimum-plus-one pool comparisons pass; prose and all-eligible formulations also reconcile with their tables. The current topology supplies 101 counted signed leads. Source admission, Bell, Catholic Charities, Howell and Medellin are excluded as recorded. No assignment statement or opinion table changed in the repair. This is not independent certification of repository commitment order; later-written earlier-effective events do not reopen committed assignments. |
| Local navigation | A fresh bounded scan checked 436 Markdown files and 2,889 actual local links/fragments, with zero applicable unresolved targets. Candidate navigation was evaluated at eventual state publication paths. Eighty links in eleven byte-identical runtime copies resolve from their authoritative freeze origins. |
| Commit-reference existence | Repair and parent objects, and the preceding audit's two referenced objects, resolve as commits using `cat-file`. Apart from the replaced audit, the current Record/close set has no qualifying commit tokens. This limited check certifies object existence, not broader history. |
| Explanation ceilings | All 152 explicitly labeled controlling explanations in the public renders are within the ordinary 350-word ceiling; the largest contains 204 words by whitespace count. |
| Candidate staging and cleanup | Three candidates and six pass notes remain properly staged. Published state still ends with OT2003. Tracker publication, final synchronized publication headers, the dossier, generated indexes and candidate/pass-note cleanup belong to Close Commit. |
| Institution and carry-forward | The next-term roster has nine Justices in correct seniority order; all thirteen allotments match Composition and the referral practice is unchanged. Arizona v. California, Nebraska v. Wyoming and Kansas v. Nebraska retain their opening stages and sources. Kansas v. Colorado and Alaska retain the stages supported by current Records. Howell and Medellin are concluded; ordinary lower-court remands are not pending Supreme Court matters. |

The deliberate absence of GitHub repository URLs in published trackers is compliant. Preserved relative navigation inside freeze and entering-law copies is not a close defect. Neither exception is part of F5.

## Legal-substance confirmation

The preceding full-term legal-substance conclusion remains clean. The repair alters no judgment, vote, proposition-level coalition, opinion assignment, holding, precedent treatment, remedy, Justice-specific historical-departure ground or current-law projection. The unchanged material remains covered by that complete review; focused comparison of the affected rules and candidate treatment found no new legal discrepancy.

Shepard retains the six-Justice conviction-record restriction, the unanimous bounded resentencing result, preserved indispensable charging limits, all Rule 52(b) conditions for forfeited error, lawful jury waiver and binding Booker treatment. Sherrill retains its seven-Justice nonrevival/taxability ground, unanimous reviewed procedural dispositions and surviving independent immunity judgments. Jackson retains the six-Justice Title IX retaliation holding and ordinary breach, causation and remedy proceedings. Sabree retains its unanimous provision-specific rights and remedial-compatibility holdings, dated payment definition, statutory eligibility and treatment conditions, and prospective breach/remedy limits. The candidate Holdings and relevant Standards treatment preserve those distinctions.

Sherrill's absence as a new standalone Standards entry is deliberate and supported by the [Standards pass](STANDARDS_AND_TESTS_PASS.md), line 76: its exceptional territorial-dormancy facts yield controlling Holdings without inventing a reusable delay threshold or converting those facts into general factors. Sabree is incorporated under the existing provision-specific rights and foreclosure instruction, with its detailed statutory qualifications retained in Holdings. Neither point is an omission caused by the repair.

The additional F5 locations were also checked for substantive content that must survive cleanup. Bell's Dicks torture qualification continues to modify the described crime, with distinct narrowing and jury-guidance questions and the actual 9/8/6 proposition coalitions and 7-2 judgment preserved. Nordyke retains the actual-violation and applicable-relief predicates, persons covered by the adjudicated unlawful operation, the county's narrower-complete-cure alternative, lawful safety conditions and unchanged claimant burdens. Parts I and III remain unanimous; Part II has five direct framework joins. The proposed metadata deletions below preserve those rules and every operative Public Projection byte. The remaining locations similarly concern editing history, not a changed merits premise.

## Remaining unresolved discrepancy

### F5 - Low - Additional saved-Record editing narratives remain

**Rule and effect:** The user's seamless-correction direction forbids a Record from carrying a note, receipt or narrative describing correction of saved canonical or public text. The exact F4 locations are repaired, but twenty-two other paragraphs in twelve Records still contain such accounts. They are internal presentation/provenance defects. They do not undermine the clean legal-substance conclusion or require adjudicative reopening.

**Files, current lines and exact fixes:**

| Record | Lines | Exact fix |
|---|---:|---|
| [Bell v. Cone](../records/bell-v-cone_merits_2005-01-24.md) | 182 | Replace this paragraph with: `Under State v. Dicks, the torture qualification remains attached to the described crime; it is not a separate disjunctive alternative.` Leave both controlling-Holding copies and the following final-validation section unchanged. |
| [Nordyke v. King](../records/nordyke-v-king_merits_2005-01-12.md) | 107 | Preserve the paragraph through `No new historical departure results.` Replace only its final two sentences with: `The Chief's identical conditional position is included in the common rule.` |
| [Nordyke v. King](../records/nordyke-v-king_merits_2005-01-12.md) | 111 | Replace only the sentence beginning `The supplemental clean audit is now incorporated:` with: `All nine join Anderson's bounded conditional remedial rule in Part I.` Preserve the surrounding component counts, limited joins and substantive limits. |
| [Sabree](../records/sabree-ex-rel-sabree-v-richman_merits_2005-03-29.md) | 293 | Replace only `The regenerated Shepard holding II was reread after its completeness expansion concerning` with `Shepard holding II addresses`. Preserve all remaining charging, Rule 52(b), jury-waiver and Medicaid-relevance language. |
| [ACLU of Nevada v. Heller](../records/american-civil-liberties-union-of-nevada-v-heller_merits_2005-05-16.md) | 12, 97 | At each location delete only the sentence beginning `Final completeness, statutory-title citation and negative-statement edits` and ending `without changing a vote or ground.` Preserve all surrounding entering-law, chronology, join and validation statements. |
| [Granholm v. Heald](../records/granholm-v-heald_merits_2005-05-16.md) | 12, 99 | Apply the same single-sentence deletion specified for Heller at each location. |
| [Bradshaw v. Stumpf](../records/bradshaw-v-stumpf_merits_2005-06-13.md) | 236, 257 | Apply the two June 13 fixes below, respectively. |
| [Golden v. Golden](../records/golden-v-golden_merits_2005-06-13.md) | 247, 268 | Apply the two June 13 fixes below, respectively. |
| [Grable & Sons](../records/grable-and-sons-v-darue-engineering_merits_2005-06-13.md) | 189, 210 | Apply the two June 13 fixes below, respectively. |
| [Johnson v. California - Batson](../records/johnson-v-california-batson_merits_2005-06-13.md) | 196, 217 | Apply the two June 13 fixes below, respectively. |
| [Merck v. Integra](../records/merck-kgaa-v-integra-lifesciences_merits_2005-06-13.md) | 222, 243 | Apply the two June 13 fixes below, respectively. |
| [Miller-El v. Dretke](../records/miller-el-v-dretke_merits_2005-06-13.md) | 248, 269 | Apply the two June 13 fixes below, respectively. |
| [Wilkinson v. Austin](../records/wilkinson-v-austin_merits_2005-06-13.md) | 221, 242 | Apply the two June 13 fixes below, respectively. |

For each of the seven June 13 Records:

1. At the first location, delete only: `The corrected Kincade delivery line was rechecked after the literal office-placeholder repair.` Preserve the preceding public-law reading statement and following additive-release statement.
2. At the second location, delete the first four sentences, ending with the sentence beginning `The independent A review verifies`. These describe the prior-copy hash and correction-receipt filename, current-copy hash, subsequent Spector/Kincade deletions and repair verification. Preserve the paragraph from `The clean neutral/model release is` onward, including all completed stage releases, reading confirmations, discharged conditions and compatibility conclusions.

**Evidence and boundary:** The [Bell final audit](../runtime/OT_2004CHUNK2_AUDIT_BELL.md), lines 3-9, expressly identifies the final Canonical Record and its qualification repair. The [January 12 assembly audit](../runtime/OT_2004CHUNK2_ASSEMBLY_B_AUDIT.md), lines 3, 7 and 11, and [validation](../runtime/OT_2004CHUNK2_ASSEMBLY_B_VALIDATION.md), lines 3 and 20-24, establish that Nordyke's concurrence-removal account concerns an already saved Record. The [chunk 5 validation](../freeze/OT_2004CHUNK5_VALIDATION.md), line 49, and [Sabree commitments](../freeze/OT_2004CHUNK5_SABREE_COMMITMENTS.md), line 129, identify the same Shepard completeness-edit event already covered by F4.

The [May 16 reconciliation refresh](../freeze/OT_2004CHUNK7_MAY16_RECONCILIATION_REFRESH.md), line 58, and [chunk 7 validation](../freeze/OT_2004CHUNK7_VALIDATION.md), lines 30-32, identify edits to completed public copies underlying the Heller/Granholm notices. The [June 6 independent review](../freeze/OT_2004CHUNK9_A_INDEPENDENT_REVIEW.md), lines 3 and 21-24, identifies the saved Records and subsequent Spector/Kincade deletions; the [neutral refresh](../freeze/OT_2004CHUNK9_JUNE6_NEUTRAL_REFRESH.md), line 5, preserves the source hash and office-label cleanup. These receipts distinguish the notices from permissible provisional modeling changes. Frozen provenance artifacts remain unchanged.

The targeted scan found no further established example. Brown and Castle Rock describe expressly uncommitted provisional changes; Rousey's supporting validation establishes pre-Record draft review. Ordinary legal corrections, standard original-decision labels, normal runtime generation and preserved frozen navigation are not F5 defects.

All F5 locations precede Public Projection. Apply the specified edits in an authorized repair task while preserving each file's existing line endings and every operative statement. The edits affect no Record header or ledger-derived cell. Verify unchanged Public Projections, Render Inputs, renders and candidates, then rerun the permitted checker. No underlying decision or tracker rule requires alteration.

## Operator disposition

F1-F4 are closed. F5 is the sole unresolved discrepancy. The deterministic checks and legal-substance confirmation pass, but the remaining internal correction narratives must be removed before Close Commit. This task changes only `terms/OT2004/close/AUDIT.md`, preserving its CRLF endings, to record the repair verification, fresh checks, focused legal review and exact remaining fixes. No repair or publication was performed.

READY FOR CLOSE COMMIT: NO
