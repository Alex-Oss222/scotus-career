# October Term 2004 confirming close audit

**Audit date:** November 23, 2026.
**Repair reviewed:** 49749c85 (parent e8221e5faea00ca51c8731a4b4704f0e408413ba).
**Disposition:** F1–F3 are resolved and the fresh legal-substance audit is clean. One Low-severity discrepancy remains under the user's seamless-correction instruction: F4, correction narratives in internal Records and their ledger copies. The term is not yet ready for Close Commit.

## Scope and method

The first operation was the expressly permitted command, python tools/check_term.py OT2004. It returned OK: OT2004; 0 warning(s). The remaining prescribed deterministic checks passed before fresh substantive review began. The saved preceding audit had expressly deferred that substantive review; this pass completes it rather than treating the earlier audit as a legal certification.

Review covered all 105 scheduled judicial events, the section 703 Admitted Source Record, ten Render Inputs, ten public renders, the four workspace projections, the three staged tracker candidates, the six close-pass notes, and relevant opening law and institutional sources. Records controlled; renders and candidates were compared with them. The substantive review was divided into chunks 1–3 (29 events), 4–6 (27), 7–9 (34), and 10 (15), with the statutory source reviewed separately.

Only read-only git cat-file operations were used outside the authorized checker. They verified the repair object and parent, compared the four repaired workspace files with both versions, and established that all 140 current Markdown files in records, render-inputs, output, workspace and close matched the repair commit before this audit was replaced. The repair leaves the records, render-inputs, output, freeze, entering-law, briefs, runtime, close, state and foundation trees unchanged from its parent. No prohibited directory or prohibited jurisprudence filename was accessed. No adjudication, source, tracker, frozen handoff or public copy was edited.

## Verification of the previous findings

| Finding | Current location | Verification | Status |
|---|---|---|---|
| F1 — Medium | [manifest.md](../workspace/manifest.md), line 3 | The summary reports 105 completed scheduled events, zero open, zero stopped and zero scheduled carry-forwards. It agrees with all 105 event rows. The three separate unscheduled carryovers remain. Only the requested counts changed. | Resolved |
| F2 — Medium | [ledger.md](../workspace/ledger.md), lines 7–112; Gonzalez at line 101, McCreary at line 108 | One eight-column table contains all 106 Records, sorted by effective date and case name and numbered 1–106. Gonzalez is entry 95 and McCreary entry 102. All Record-derived cells are preserved; the extra table is gone and the existing history-verification disclosure remains. | Resolved |
| F3 — Low | [continuity.md](../workspace/continuity.md), line 7; [neutral-projection.md](../workspace/neutral-projection.md), line 7 | Both paragraphs now state that close candidates are staged and audit/publication remain pending. The replacement is the requested sentence; all surrounding chronology, retained-proceeding and assignment text remains intact. | Resolved |

All four repaired files match their 49749c85 blobs byte-for-byte and retain CRLF without bare LF line endings. None of these repairs changes legal substance.

## Remaining unresolved discrepancy

### F4 — Low — Saved-Record correction narratives remain contrary to the seamless-correction instruction

**Rule and effect:** The user's current direction requires corrected Records to contain no note, receipt or narrative describing their correction, while retaining the required opening labels and an ordinary original-decision value. The passages below describe changes to saved canonical text or repeat that editing history. Calling the changes pre-integration does not make those narratives compliant. This is an internal presentation/provenance defect, not a defect in any vote, holding, remedy or public decision.

**Files, lines and exact fix:**

| File | Current line | Exact fix |
|---|---:|---|
| [Jackson Record](../records/jackson-v-birmingham-board-of-education_merits_2005-03-29.md) | 4 | Preserve the required label and replace its entire value so the line reads: **Version / lineage:** Original decision. |
| [Jackson Record](../records/jackson-v-birmingham-board-of-education_merits_2005-03-29.md) | 14 | Replace only “the corrected Shepard completeness formulation” with “Shepard's completeness formulation”. Preserve the rest of the entering-law paragraph. |
| [Sabree Record](../records/sabree-ex-rel-sabree-v-richman_merits_2005-03-29.md) | 4 | Preserve the required label and replace its entire value so the line reads: **Version / lineage:** Original decision. This removes the two editing narratives and the correction-receipt reference. |
| [Shepard Record](../records/shepard-v-united-states_merits_2005-03-07.md) | 48 | Delete this standalone paragraph describing the completeness-review expansion, pre-integration clarification and public-slice regeneration. Preserve all operative Gatewood, Rule 52(b), jury-waiver and Booker terms elsewhere in the Record. |
| [Sherrill Record](../records/city-of-sherrill-v-oneida-indian-nation_merits_2005-03-29.md) | 68 | Replace only “The regenerated Shepard Part II was reread after its completeness clarification:” with “Shepard Part II supplies the governing sentencing terms:”, and replace “These clarified sentencing terms” with “These sentencing terms”. Preserve the intervening charging, forfeiture, jury-waiver and binding-Booker rules and all other text. |
| [ledger.md](../workspace/ledger.md) | 53–54 | Mechanically refresh only the Version / lineage cells for Jackson and Sabree from the amended Record headers, yielding Original decision. in each. Preserve every other cell, the effective ordering and all row numbers. |

The [Sabree source receipt](../freeze/OT_2004CHUNK5_SABREE_SOURCE_CLARIFICATION.md), lines 3–7, and the [Jackson/Sabree scope receipt](../freeze/OT_2004CHUNK5_JACKSON_SABREE_SCOPE_CLARIFICATION.md), lines 3–9, establish that these particular narratives describe edits to already saved canonical files. Those frozen provenance artifacts may remain unchanged. Brown's distinct discussion concerns reconciliation of provisional non-Stone commitments before a Canonical Decision Record existed; it is not this defect. Original source-admission chronology and the standard opening labels are likewise not defects.

Make these metadata-only edits in an authorized repair task, preserving CRLF. All affected material precedes the Public Projection; its bytes, the Render Inputs and the public renders need no substantive change. Then rerun the permitted term checker, verify the two ledger-header cells and confirm unchanged Public Projections. No adjudicative reopening is required by F4.

## Deterministic results

| Check | Result |
|---|---|
| Required term checker | Passed initially with zero warnings; rerun after replacing this audit with the same result. Opening Holdings-volume synchronization, runtime freshness, Record structure and generated-input identity passed. |
| Inventory and coverage | All 105 inventory rows match the manifest's identity, chunk, date, event type, category and area fields. All are completed and uniquely represented. The 106 Records comprise those 105 judicial events and one admitted statutory source. |
| Record to input to render | All judicial Public Projections are copied exactly into the ten inputs, without omission, duplication or extras. Render headings and closing boundaries account for all 105 events. Chunk counts are 13, 11, 5, 7, 11, 9, 8, 11, 15 and 15. |
| Effective chronology | Ledger and continuity cover all 106 Records in effective-date order. Inputs preserve their supplied event order and same-day boundaries. Later-written, earlier-effective Records were not used to reopen committed assignments. |
| Participation and arithmetic | All 105 judicial events establish nine participants. The statutory source correctly has no judicial poll. The 146 machine-readable Record and 156 output margin/roster comparisons pass; compact, component-specific and undisclosed procedural forms were separately reviewed. |
| Opinion assignment | The 101 counted signed lead opinions and recorded author pools reconcile. Within-Record eligible minima and minimum-plus-one pools are consistent. Apparent differences from a retrospective effective-order count arise from later-written earlier-date events, as Engine section 8 permits. Repository commitment order was not independently certified. |
| Local navigation | The bounded scan checked 436 Markdown files and 2,905 local links/fragments, with no applicable unresolved target. Candidate links were tested at their publication location. Eighty relative links in eleven runtime copies resolve from their byte-identical authoritative freeze locations. Two template examples were excluded. |
| Commit-reference existence | The checker's pre-existing Record/close reference set contained no qualifying commit tokens; that empty set is not a history certification. The repair commit and its parent were independently verified with cat-file. No missing required object was established. |
| Candidate staging | Three candidates and six pass notes are properly retained before Commit. Holdings preserves the opening case headings and 23 doctrinal areas, with 158 added case-area entries. Standards contains 1,149 entries against 1,113 at opening. Final synchronized publication headers, dossier, generated indexes and candidate cleanup belong to Commit. |
| Carry-forward and institution | The next-term setting has nine correctly ordered Justices, thirteen allotments and the unchanged referral practice. Arizona v. California, Kansas v. Colorado, Nebraska v. Wyoming, Kansas v. Nebraska and Alaska v. United States retain their supported stages. Howell and Medellin are concluded; ordinary lower-court remands are not pending Supreme Court matters. |

The four required opening labels remain present in every Record. All 152 expressly labeled controlling explanations tested in the public renders fall within the ordinary 350-word ceiling. F4 is additional instruction-specific text hygiene; it does not invalidate these structural results.

## Fresh legal-substance conclusion

The legal-substance review found no defect. The review compared controlling propositions, actual joins, material separate positions, operative remedies, precedent treatment, effective entering law and Justice-specific historical departures with the corresponding candidate treatment and public account. The staged trackers do not acquire law from a dissent, a private position, a historical result or mere judgment agreement.

- **Chunks 1–3:** Anderson's component coalitions, Kansas's eligible-loss cohort and interest components, Brosseau's immunity/merits separation, Clark and Jama's distinct statutory conditions, Booker's constitutional/remedial coalitions, Bell v. Cone's separate rationale coalitions, and Nordyke and Taft's component-specific limits remain intact. Karaha Bodas preserves arbitral-law and relief distinctions; Smith and Stewart retain their precise judgment consequences. The 171 reviewed substantive holding paragraphs and all 29 rendered remedy/stage blocks preserve the Records' substance. Howell properly creates no Holdings entry.
- **Chunks 4–6:** Johnson, Shepard, Wilkinson, Muehler, Brown, Galvin, Sherrill, Jackson, Sabree and Monsanto retain their controlling grounds, statutory gates and remedy limits under the actual prior law. The changed-premise grounds are Justice-specific. All 44 expressly labeled operative rules survive the render comparison; candidate paraphrases preserve authority and scope. The 21 affected Standards entries satisfy the reusable-rule boundary. Smith's disputed reasonable-factors proof burden remains noncontrolling. The section 703 admission preserves the otherwise-allowable condition, covered claims, recovery cap and both post-October 22, 2004 timing triggers without altering earlier Banks tax years.
- **Chunks 7–9:** Spector's seven-, six- and five-Justice propositions remain distinct from its four-vote sequencing view. Johanns preserves the difference between five rationale joins and six formal-vacatur votes. Tucson retains its complete-framework, narrower-protection and independent-ground coalitions. Lingle displaces the identified Del Monte Dunes efficacy holding while preserving the prior final judgment and surviving jury rules. Raich, Lofton, Clingman and Kincade have supported changed-law grounds; Golden and Rompilla preserve judgment-only and statutory-review distinctions. Candidate and render comparisons disclose no lost operative qualification.
- **Chunk 10:** All 28 labeled operative rules survive normalized render comparison. Holdings preserves their substance, including Grokster's separately located liability and remedy rules. Gonzalez retains unanimous process classification and seven-Justice denial of extraordinary relief on the assumed account, rather than treating contested review efforts as absent. McCreary gives the repeal its actual prospective effect without declaring it an automatic cure; Van Orden distinguishes historical exposition from governmental adoption. Green Party keeps six merits joins separate from seven remedial joins. Halbert's actual-waiver analysis, Allapattah's enacted exceptions, Brand X's limited prior-circuit rule, Castle Rock's mandatory-duty assumption and Grokster's unresolved Sony application retain their proper scope.

Focused primary-source checks corroborated the disputed rehearing chronology in the [Gonzalez dissent](https://www.law.cornell.edu/supct/html/04-6432.ZD.html), including note 5, and the identifier-removal and postargument-repeal chronology in the [McCreary opinion](https://www.law.cornell.edu/supct/html/03-1693.ZO.html), notes 6 and 19. Those historical recitations verify factual limits; they do not replace the timeline's controlling law.

The deliberate absence of GitHub repository URLs in published trackers is not a defect. Preserved navigation in freeze and entering-law copies is not a close defect. Required original-decision labels and values are not correction notices. The remaining F4 targets actual editing narratives, not any of those permitted features.

## Operator disposition

F1–F3 are closed. F4 is the only unresolved discrepancy. Legal substance and the staged law are clean, but the explicit seamless-correction requirement must be satisfied before Close Commit. This pass changes only terms/OT2004/close/AUDIT.md, recording repair verification, completed checks, the fresh substantive conclusions and the exact remaining metadata fix. No repair, tracker publication, deletion of close candidates or Git mutation was performed.

READY FOR CLOSE COMMIT: NO
