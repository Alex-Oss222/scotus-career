# October Term 2004 confirming re-audit

**Audit date:** November 23, 2026.
**Repair reviewed:** 379d1519; parent bd5ca837354d91fc16534f17325ae0b4fd43a760.
**Disposition:** F1-F5 are resolved. The prescribed deterministic checks pass, and the legal-substance audit remains clean. No discrepancy remains unresolved. October Term 2004 is ready for the Close Commit.

## Scope and method

This confirming re-audit verifies the operator's latest repairs against the preceding audit and reruns the prescribed deterministic checks before focused legal-substance confirmation. The required command, `python tools/check_term.py OT2004`, returned `OK: OT2004; 0 warning(s)`. It was run again after this audit was replaced, with the same result.

Read-only `git cat-file` tree and blob comparisons establish that the repair changes exactly twelve Records. Every requested F5 edit was reconstructed from the parent bytes and the preceding audit's instructions; each complete reconstructed file equals its repair blob and the current working file. The twenty-two locations are accounted for below. All twelve Public Projections are byte-identical to their parent versions. Every byte outside the specified edits is unchanged. Eleven affected Records preserve CRLF endings; Sabree preserves LF. All retain their previous line counts.

The governing foundation, opening state, approved briefs, runtime handoffs, freeze artifacts, entering-law copies, case list, workspace, generated inputs, renders and close candidates are unchanged between parent and repair and match the working files. The comparison covered 9 foundation files, 27 state files, and the OT2004 sets of 11 briefs, 273 runtime files, 404 freeze files, 85 entering-law files, 107 Record-directory files, 11 Render Input files, 11 output files, 4 workspace files, 11 close files and the case list. These are tracked-file counts, including placeholders where present; the substantive Record count is 106. The audit itself matched the repair before this replacement.

That invariance supports carrying forward the preceding complete legal-substance audit of all 105 judicial events and the admitted statutory source. This pass independently examines the legal significance of the changed passages and their surrounding rules, coalitions, remedies, continuity and candidate treatment. It does not claim a new adjudication or a complete repetition of historical-source research.

Only the expressly permitted checker and read-only `git cat-file` operations used Git. No prohibited directory or jurisprudence file was accessed. This task changes only this audit; temporary scratch code was removed. No Record, public copy, tracker, governing file or frozen handoff was changed.

## Verification of previous findings

| Finding | Verification | Status |
|---|---|---|
| F1 - Medium | [Manifest](../workspace/manifest.md), line 3 and event rows: 105 completed scheduled events, zero open, zero stopped and zero scheduled carry-forwards. Three unscheduled opening carryovers remain separately identified. | Resolved |
| F2 - Medium | [Ledger](../workspace/ledger.md), lines 7-112: one eight-column table, 106 consecutively numbered Records, correct effective-date/case-name order and exact Record-derived fields. | Resolved |
| F3 - Low | [Continuity](../workspace/continuity.md), line 7, and [neutral projection](../workspace/neutral-projection.md), line 7, continue to state the staged candidate and pending publication posture accurately. | Resolved |
| F4 - Low | The previously verified Jackson, Sabree, Shepard and Sherrill passages and ledger values remain repaired. This repair changes none of those F4 locations. Required original-decision labels remain intact. | Resolved |
| F5 - Low | All twenty-two specified locations in twelve Records implement the preceding audit's exact replacements or deletions, preserving all surrounding operative text. Detailed verification follows. | Resolved |

### F5 repair verification

Line numbers below are current and unchanged by the repair.

| Record | Lines | Verified repair and retained content |
|---|---:|---|
| [Bell v. Cone](../records/bell-v-cone_merits_2005-01-24.md) | 182 | The prescribed substantive qualification replaces the editing account. Both controlling-Holding copies and the following final-validation section are unchanged. |
| [Nordyke v. King](../records/nordyke-v-king_merits_2005-01-12.md) | 107, 111 | The two prescribed substitutions retain the conditional remedy, every qualification, the proposition counts and the precise joins. |
| [Sabree](../records/sabree-ex-rel-sabree-v-richman_merits_2005-03-29.md) | 293 | The prescribed phrase replacement retains the charging, Rule 52(b), lawful jury-waiver and Medicaid-relevance statements. |
| [ACLU of Nevada v. Heller](../records/american-civil-liberties-union-of-nevada-v-heller_merits_2005-05-16.md) | 12, 97 | Only the specified editing-history sentence and its adjacent separating space are deleted at each location. Chronology, entering law, joins and validation remain. |
| [Granholm v. Heald](../records/granholm-v-heald_merits_2005-05-16.md) | 12, 99 | The same exact sentence deletions preserve the surrounding substantive qualifications and validation. |
| [Bradshaw v. Stumpf](../records/bradshaw-v-stumpf_merits_2005-06-13.md) | 236, 257 | Both prescribed June 13 deletions are exact; the earlier-law reading and completed stage-release statements remain. |
| [Golden v. Golden](../records/golden-v-golden_merits_2005-06-13.md) | 247, 268 | Both prescribed June 13 deletions are exact; all compatibility conditions and limited fallback components remain. |
| [Grable & Sons](../records/grable-and-sons-v-darue-engineering_merits_2005-06-13.md) | 189, 210 | Both prescribed June 13 deletions are exact; the jurisdiction-only scope and release statements remain. |
| [Johnson v. California - Batson](../records/johnson-v-california-batson_merits_2005-06-13.md) | 196, 217 | Both prescribed June 13 deletions are exact; the reliable-remand conditions and release statements remain. |
| [Merck v. Integra](../records/merck-kgaa-v-integra-lifesciences_merits_2005-06-13.md) | 222, 243 | Both prescribed June 13 deletions are exact; the distinct fresh-Merck reconciliation release and substantive limits remain. |
| [Miller-El v. Dretke](../records/miller-el-v-dretke_merits_2005-06-13.md) | 248, 269 | Both prescribed June 13 deletions are exact; the separate statutory burdens and lawful-record boundary remain. |
| [Wilkinson v. Austin](../records/wilkinson-v-austin_merits_2005-06-13.md) | 221, 242 | Both prescribed June 13 deletions are exact; the actual liberty, process and prison-relief premises remain. |

For each June 13 Record, the first deletion removes only the Kincade delivery-line editing notice. The second removes only the four sentences describing earlier copies, receipts and repair verification. The complete paragraph from the clean neutral/model release onward survives, including the six-case reconciliation release, separate fresh-Merck release, reading confirmations, discharged June 6 conditions and final compatibility conclusions. All F5 locations precede Public Projection. No header or ledger-derived cell changes.

A targeted current-Record scan found no further established saved-Record editing narrative. Descriptions of original neutral/model reconciliation, provisional commitments and substantive circulation remain distinct from accounts of correcting saved Records. The required `**Version / lineage:**` field and its standard `Original decision.` value are compliant.

## Deterministic results

| Check | Fresh result |
|---|---|
| Required checker and baseline | Passed with zero warnings before review and after audit replacement. Includes opening Holdings-volume synchronization, runtime-split freshness, Record interfaces, generated-input identity and public workflow checks. |
| Inventory and coverage | All 105 inventory/manifest rows agree on number, chunk, identity, docket, date, event type, category and area. Each has one unique judicial Record; the 106th Record admits section 703. |
| Record, input and render reconciliation | All 105 Public Projection bodies equal their generated event blocks. All rendered events have matching docket dates, headings and closing boundaries. Chunk counts are 13, 11, 5, 7, 11, 9, 8, 11, 15 and 15. |
| Effective order and projections | All 106 ledger rows match their Record fields and effective-date/case-name order. Continuity and the neutral projection cover all 106 Records with correct event dates. Same-date continuity ordering creates no chronology conflict. |
| Participation and judgment arithmetic | Nine participants are established in all 105 judicial events. All 151 explicit Record margin/roster comparisons and 156 render comparisons pass. The larger Record comparison count than the preceding audit reflects broader parsing of existing forms, not changed decisions. |
| Prose and procedural exceptions | Gonzalez's seven affirmance supporters and two opponents reconcile. Devenpeck preserves eight reversal votes, the Chief's vacatur position and nine remand votes. Howell and Medellin preserve their undisclosed procedural forms. The admitted source has no judicial vote. |
| Opinion joins | All 105 topologies were checked: 83 table forms and 22 prose forms. Partial joins and proposition coalitions reconcile. Spector preserves its distinct 7/6/5/4/6 parts without treating four-Justice sequencing reasoning as a majority holding. |
| Opinion assignment | All 102 checked assignment statements, comprising 47 explicit colon forms and 55 prose/all-eligible forms, reconcile their stated counts, eligibility and selected-author membership. Minimum-plus-one pools are correct where the Chief's rule applies; Associate assignments preserve their stated selection authority. This includes Catholic Charities' signed threshold assignment, while that lead remains excluded from the 101 counted signed leads. Sherrill's separately assigned Part II also reconciles. Source admission, Bell's per curiam action, Howell and Medellin supply no counted lead. The check does not independently certify repository commitment order; later-written earlier-effective events do not reopen committed assignments. |
| Local navigation | A bounded scan inspected 441 Markdown files and 2,915 parsed local links/fragments. Two are explicit case-index authoring-template placeholders; all 2,913 applicable links resolve. Candidate navigation was checked at eventual publication paths. Eighty links in eleven byte-identical runtime copies resolve from their authoritative freeze origins. |
| Commit-reference existence | The repair and parent, together with preceding-audit references 66978bf0 and 84528e911b940788f66d1c78a6a90b02b67311ae, resolve as commits through read-only `cat-file`. Apart from audit references, the current Record/close set has no qualifying commit tokens. This certifies object existence, not broader history. |
| Explanation ceilings | All 152 expressly labeled controlling explanations in the public renders remain within the ordinary 350-word ceiling, including a conservative capture of adjacent explanation paragraphs. |
| Candidate staging and cleanup | Three candidates and six pass notes remain properly staged. Published state still ends with OT2003. Coordinated publication headers, tracker publication, the dossier, generated indexes and removal of candidates/pass notes belong to Close Commit. |
| Institution and carry-forward | The next-term candidate has nine Justices in correct seniority order, all thirteen allotments matching Composition, the unchanged referral practice, the authorized substantive sections and five pending docket rows. Arizona v. California, Nebraska v. Wyoming and Kansas v. Nebraska preserve their opening stages and sources. Kansas v. Colorado retains compensation/decree proceedings before the Special Master; Alaska retains conforming-decree proceedings. Howell and Medellin are concluded. Ordinary lower-court remands and the separate Texas proceeding are not pending Supreme Court grants. |

The deliberate absence of GitHub repository URLs in published trackers and candidates is compliant. Preserved navigation inside freeze and entering-law source copies was excluded from defect detection as directed. Seamless Records properly contain no account or receipt describing correction of saved text; the mandatory standard lineage field is not such an account.

## Legal-substance confirmation

The preceding full-term legal-substance conclusion remains clean. The repair changes no judgment, vote, controlling coalition, opinion assignment, holding, precedent treatment, remedy, Justice-specific historical-departure ground or current-law projection. Focused review found no operative condition or material premise lost with the deleted editing narratives.

Bell's replacement preserves the Dicks torture qualification as a condition attached to the described crime, consistently with the operative holding and the Holdings candidate. It does not create a separate disjunctive alternative. The nine/eight/six proposition coalitions, seven-to-two judgment, permissive section 2254(b)(2) route, 1984 adjudication cutoff, distinct jury-guidance and actual-cure inquiry, and noncontrolling broader remand position remain intact.

Nordyke retains an actual adjudicated unlawful operation and every applicable relief prerequisite as conditions of the common remedial instruction. Its reach remains confined to the persons governed by that operation; the county may establish a narrower complete cure; lawful safety conditions and the claimants' ordinary burdens survive. Both judgment components remain unanimous. Parts I and III have nine joins; Part II has five direct framework joins, with the two paired reservations preserved. The historical-departure account still rests on Love and Wright's displacement of the lower court's collective-right premise, without inventing a historical Supreme Court vote. Holdings and Standards preserve those same boundaries.

Sabree's revised cross-reference accurately preserves Shepard's charging, forfeiture and lawful jury-waiver subjects while explaining that they supply no different Medicaid rule. Its own unanimous rights and enforcement holdings retain the dated payment definition, adopted benefit, actual statutory eligibility and treatment conditions, the combined hearing/funding comparison, and the separation between an enforcement channel and proof of breach and lawful relief. The financing-versus-furnishing question, proper representative scope and effective prospective-remedy requirements remain as adjudicated. Both relevant Holdings entries and the existing provision-specific Standards entry preserve these distinctions.

Heller retains the distinct statutory triggers and exceptions, the government-justification burden, associational protection and genuinely open facial inquiry. Its nine-member Part I and six-member Parts II-III remain supported, including Scalia's recorded alternative remand path. Granholm retains its six-Justice alcohol-specific ground, ordinary-proof alternatives burden, state-specific remedial choices, narrower-complete-cure condition and independent New York dispositions. Their chronology and completed reconciliation statements survive the deletions.

The seven June 13 Records retain their full compatibility screen, common earlier-law boundary, distinct adjudicated scopes and surviving stage releases. Their same-date decisions do not become entering law for one another. Golden's two disposition-only fallback components remain limited as recorded. Bradshaw's independent sentencing inquiry, Grable's jurisdiction-only scope, Johnson's reliable Batson inquiry, Merck's record and dependent-damages limits, Miller-El's distinct statutory burdens, and Wilkinson's actual liberty/process predicates and independent section 3626 conditions all survive. The referenced releases and corresponding candidate treatment confirm that no legal qualification, release condition, material assumption or departure basis was removed.

The previous F4 legal conclusions remain unaffected: Shepard's six-Justice conviction-record rule and unanimous bounded resentencing mandate, Sherrill's seven-Justice nonrevival ground and independent procedural dispositions, Jackson's six-Justice retaliation holding, and Sabree's provision-specific rights and remedy limits are unchanged. The earlier full-term review continues to cover the unchanged remainder of the term.

## Operator disposition

No discrepancy remains unresolved. F1-F5 are closed, and no new finding is required. The term is ready for the Close Commit. Publication, final header synchronization, dossier/index generation and candidate/pass-note cleanup remain the authorized work of that separate pass.

The only retained file change from this task is `terms/OT2004/close/AUDIT.md`, replaced with this repair verification, fresh deterministic results and focused legal confirmation while preserving its CRLF endings. No repair, tracker publication or Git mutation was performed.

READY FOR CLOSE COMMIT: YES
