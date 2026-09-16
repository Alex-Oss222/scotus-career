# October Term 1991 — Fresh term-close audit

**Audit date:** September 15, 2026.  
**Result:** Unresolved discrepancies remain. The coordinated close is not ready for Commit.  
**Proposed common cutoff:** July 17, 1992, after Benten v. Kessler.  
**Action:** Report only; no repairs, adjudication, or tracker replacement.

This report preserves [AUDIT.md](AUDIT.md), [the first reaudit](AUDIT.reaudit-2026-09-15.md), and [the second reaudit](AUDIT.reaudit-2026-09-15-2.md). It uses a new filename because [AGENTS.md](../../../AGENTS.md) prohibits modifying previously written close files. Earlier findings were independently checked against the current files; an earlier report is not evidence that its discrepancy remains unresolved.

## Scope and method

The audit compares the three opening trackers, all 125 current record files (124 Court events and the October 23 institutional source), the case inventory, final manifest and commitment ledger, Term Continuity Note and Current-Term Neutral Projection, the three closing candidates, and all fourteen public chunk renders. Effective Render Inputs and correction receipts identify the appropriate public projections and distinguish current authority from superseded material. Three parallel reviews cover chunks 1–5, 6–10, and 11–14; the principal review covers the institutional source, term-level reconciliation, carry-forwards, candidate structure and navigation, and Casey's current workspace.

The governing sources are [AGENTS.md](../../../AGENTS.md), the [Engine](../../../foundation/ENGINE.md), [Render Contract](../../../foundation/RENDER_CONTRACT.md), [Court Composition](../../../foundation/COURT_COMPOSITION.md), and the [Holdings](../../../foundation/templates/HOLDINGS_TEMPLATE.md), [Standards and Tests](../../../foundation/templates/STANDARDS_AND_TESTS_TEMPLATE.md), and [Standing State](../../../foundation/templates/STANDING_STATE_TEMPLATE.md) instructions. Records control; renders are cross-checks.

The audit accepts the expressly authorized Casey version 1.5 result: Stone, Blackmun, Stevens, O'Connor, and Souter adopt the complete six-step framework. Preserved earlier objections do not undo that result. The older separate-file correction convention for Holmes, Suter/Montana, Alaska, and Harris is also respected. No new votes are modeled, no historical outcome is substituted, and no legal issue is adjudicated. This is a comparison of the repository's authoritative records and projections, not a new authentication of every external source. Coverage concentrates on each record's operative propositions, authority, limits, remedy and continuity, with judgment, topology and annex passages examined as needed; it is not an uninterrupted reread of every embedded source or superseded modeling table. Mechanical checks establish identity, ordering, field completeness, and references; they do not establish legal meaning.

## Checks that passed

| Check | Result |
|---|---|
| Opening baseline | Holdings and Standards begin empty. All three opening trackers identify no completed simulated term, the October 7, 1991 opening baseline, and the September 14, 2026 edition. No prior registered substantive proposition requires rollover. |
| Required candidate headers | All three have exactly `Last completed October Term: 1991`; `Processed through: July 17, 1992, after Benten v. Kessler.`; `Edition: September 15, 2026`. |
| Inventory, manifest, and ledger | All 124 inventory Court events have records. The manifest has 125 dated completed events/sources, in effective-date order, plus the undated pending Coleman petition: 126 rows. The numbered ledger runs from 1 through 125 and identifies 125 distinct existing records. Correction receipts create no extra Court event. |
| Natural anchors and required fields | All 150 primary Holdings case/area blocks supply docket and decision date; holding and current-force field counts reconcile. All 98 Standards entries have their required core fields. Candidate links and prospective Holdings heading references resolve. |
| Holding coverage and authority | No omitted controlling holding, duplicate substantive holding, or promotion of noncontrolling reasoning into the closing candidates was identified. Cross-area references, independent alternatives, fractures, equal divisions, and orders retain their authority boundaries. An ordinary application of unchanged law does not require a separate Standards entry. The source and workspace defects below remain independently material. |
| Public event accounting | The fourteen outputs contain 124 event entries and 124 closing boundaries. Older correction insertions appear in their authorized public locations without duplicate events. The Zatko closing caption now matches its heading. Public blocker sections contain no cleared-blocker history. |
| Roster and allotments | The proposed OT1992 roster, service dates, seniority, and thirteen circuit allotments match the Composition and October 23 admitted source. The opening referral practice is retained. |
| Standing State boundary and carry-forward | Only the permitted header, current Court, allotments, standing practices, and four docket lines appear. Zatko's unresolved paid-docketing condition, Wyoming's retained implementation jurisdiction, Coleman petition No. 91-8336, and Reynolds's interim trials protection are all carried forward at their recorded stages. No positions register, dependency/history section, or future institutional transition is added. Ordinary lower-court remands are not treated as open Supreme Court matters. |

The link to the former standalone Casey version 1.2 record at workspace line 290 is in a preserved historical correction receipt. Subsequent receipts identify its in-place successor and lineage. It is not a missing current authority and is not reported as an unresolved reference defect.

## Unresolved discrepancies

### 1. Three incompatible Casey statements remain in the current workspace

**Classification:** Current-state projection error; the authorized decision itself is not reopened.

The [Casey record](../records/Planned_Parenthood_of_Southeastern_Pennsylvania_v_Casey_merits_1992-06-29.md) supplies the complete framework and proof allocation at lines 220–313, the five-Justice integrated timetable replacement and nine-Justice timetable result at lines 344–354, and Kennedy's distinct retained-core position at line 354. Much of the [workspace](../workspace.md) now agrees, including its expanded standard at line 3963, current-law limits at lines 4439–4441, and Neutral Projection at lines 5284–5288. Three live passages still conflict:

| Workspace location | Discrepancy against the current record |
|---|---|
| Line 3959, governing-standard authority | Calls the separate timetable result a six-vote result, naming Stone, White, O'Connor, Scalia, Kennedy, and Thomas. The current record gives that result all nine votes; five directly join the integrated replacement rationale. This also contradicts workspace lines 3969 and 4439. |
| Line 3969, governing-standard explanation | Includes Kennedy in the four Justices described as rejecting the replacement because they would reject Roe's underlying entitlement, then distinguishes his retained-core position later in the same paragraph. Record line 354 assigns the rejection-of-entitlement ground only to White, Scalia, and Thomas; Kennedy separately rejects the timetable while retaining the protected core. His lack of a framework join cannot become rejection of that core. |
| Line 3971, governing-standard explanation | Says no majority creates a universal burden shift **after meaningful interference**. Record lines 274 and 282 expressly place substantiation of justification and fit on the State after challengers establish the duty, population, causation, and triggering interference. The corrected limitation elsewhere concerns an automatic shift for every regulation **regardless of** that threshold. Line 3971 does not preserve that distinction and contradicts workspace lines 3963, 4441, and 5286. |

Engine §§1, 2, and 12 require the current projection to state the record faithfully. An accurate passage elsewhere, or a general statement that the record controls, does not cure contradictory current instructions. The Neutral Projection also uses the Continuity Note's current-law sections as part of its cumulative baseline (lines 5274 and 5282).

**Required resolution:** Reconcile these passages to the existing version 1.5 tally, Kennedy's actual ground, and the conditional proof allocation. Preserve the five direct framework joins and the nine-vote timetable result; do not invent a new coalition or burden. No later-event adjudicative change is established by this finding.

### 2. Gade invokes an unnamed statutory savings boundary

**Classification:** Record and public-projection completeness gap; no new construction of the savings clause is adopted here.

The [Gade record](../records/Gade_v_National_Solid_Wastes_Management_Association_merits_1992-06-18.md) cites OSH Act §4(b)(4), 29 U.S.C. §653(b)(4), at line 21 and says its “specified savings remain operative” at lines 23 and 70. It never states what that provision saves. The [effective Render Input](../render-inputs/OT_1991CHUNK12.md), line 428, repeats the unnamed qualification. The [public render](../output/OT_1991CHUNK12.md), line 379, likewise says that the specified savings remain operative without supplying their terms elsewhere in the entry.

This is an expressly retained statutory boundary in the account of the law after decision. AGENTS.md's completeness rule requires material exceptions and qualifications to be stated in the same entry and specifically forbids relying on an unnamed “specified exception.” A section citation alone does not provide the invoked boundary's operative terms. The Court's shared negative holding rejecting automatic occupational-overlap preemption remains identifiable; the omission does not establish that the Court construed §4(b)(4), adopted a broader positive conflict test, or changed any vote.

**Required resolution:** Supply the event-eligible text or supported formulation of the invoked §4(b)(4) savings from the authoritative statutory source, accurately distinguish preservation from a newly adjudicated construction, and project the supported boundary into the effective input and public entry. If its intended scope cannot be established, identify that source gap explicitly instead of leaving the unnamed qualification. Do not infer a new holding during close.

### 3. Felix and Robertson authority fields count the author among those who “joined” the author

**Classification:** Clerical attribution error; the stated tallies and unique coalitions remain ascertainable.

| Affected proposition | Locations |
|---|---|
| Felix, Part I | [Record](../records/United_States_v_Felix_merits_1992-03-25.md), line 93; [Render Input](../render-inputs/OT_1991CHUNK7.md), line 60; [workspace](../workspace.md), line 1204. |
| Felix, Part II | Same record, line 106; same Render Input, line 73; workspace line 1211. |
| Robertson | [Record](../records/Robertson_v_Seattle_Audubon_Society_merits_1992-03-25.md), line 90; same chunk 7 Render Input, line 404; workspace line 1296. |

Felix identifies White as author and then includes White in the list “joined by”; Robertson does the same with Thomas. The listed unique supporters establish the stated nine/seven/nine support, but the wording confuses the author with the other Justices' joins. The Holdings candidate and public prose already express the support without this self-join wording; this is not a missing-vote or changed-coalition finding.

**Required resolution:** Correct the attribution wording while preserving the actual author, unique supporters, partial-join limits, and stated tally. No new vote or reconsideration is indicated.

### 4. Twelve early Render Inputs rewrite the controlling explanations

**Classification:** Record-to-Render-Input handoff fidelity; no substantive change in law, coalition, or remedy was identified.

AGENTS.md's Holdings writing standard requires the record's controlling-holding text to be carried into the Render Input's Holdings block **unchanged**. Twelve early events instead shorten or reword their controlling explanations. This finding concerns actual rewritten words, not whitespace, punctuation, or the separate permission to present a faithful public render in prose.

| Event | Record location | Effective Render Input location |
|---|---|---|
| Ibarra | [Record](../records/United_States_v_Ibarra_merits_1991-10-15.md), line 25 | [Chunk 1](../render-inputs/OT_1991CHUNK1.md), line 33 |
| Zatko | [Record](../records/Zatko_v_California_fee_motions_1991-11-04.md), line 23 | Chunk 1, line 167 |
| Hafer | [Record](../records/Hafer_v_Melo_merits_1991-11-05.md), line 24 | Chunk 1, line 210 |
| MCorp | [Record](../records/Board_of_Governors_v_MCorp_Financial_merits_1991-12-03.md), line 25 | Chunk 1, line 253 |
| Griffin | [Record](../records/Griffin_v_United_States_merits_1991-12-03.md), line 25 | Chunk 1, line 296 |
| Estelle | [Record](../records/Estelle_v_McGuire_merits_1991-12-04.md), line 48 | [Chunk 2](../render-inputs/OT_1991CHUNK2.md), line 46 |
| Gizoni | [Record](../records/Southwest_Marine_v_Gizoni_merits_1991-12-04.md), line 33 | Chunk 2, line 89 |
| Wooddell | [Record](../records/Wooddell_v_IBEW_Local_71_merits_1991-12-04.md), lines 35 and 41 | Chunk 2, lines 133 and 140 |
| Gibson | [Record](../records/Gibson_v_Florida_Bar_merits_1991-12-04.md), lines 41 and 47 | Chunk 2, lines 193 and 200 |
| Simon & Schuster | [Record](../records/Simon_and_Schuster_v_Crime_Victims_Board_merits_1991-12-10.md), line 33 | Chunk 2, line 243 |
| Ardestani | [Record](../records/Ardestani_v_INS_merits_1991-12-10.md), line 33 | Chunk 2, line 286 |
| Union Bank v. Wolas | [Record](../records/Union_Bank_v_Wolas_merits_1991-12-11.md), line 33 | Chunk 2, line 329 |

For example, Ibarra's record identifies the Government's reconsideration filing within thirty days **of suppression**, its appeal after denial, and its earlier abandonment **of consent** in a fuller controlling explanation. The input compresses those sentences, and its operative-rule paragraph also rephrases the record. The information remains consistent in substance; that does not satisfy the express unchanged-text handoff requirement. The corresponding public entries were checked without finding a changed holding, omitted material qualification, altered vote, or different remedy. The current explanations in chunks 3–5 are preserved.

**Required resolution:** Project the authoritative controlling-holding text unchanged into the affected Holdings blocks, preserving their event boundaries and the other events. Review the corresponding public entries for the required depth and substance from that corrected input. No new adjudication or change to the authoritative explanations is indicated by this finding, and no independent word-count failure is asserted.

## Earlier findings verified as cleared

- **Casey's current record supersession:** Lines 50–52 now expressly supersede the changed dispositions and authorship rather than reserving only the abstract framework join question; line 74 also covers the parental-attendance rationale and authorship. The earlier version 1.4 account can now be read as superseded history at those scopes.
- **Casey's Standards reporting qualification:** The current rule at Standards line 911 now states that individual reports are not public records, law-enforcement access requires a common pleas court order following an application showing good cause, and published statistics may not identify physician, facility, or patient. These remain the safeguards accepted in this litigation, not a new universal constitutional minimum.
- **Lujan's Standards elements:** Standards line 166 now states traceability to the defendant rather than independent third parties and likely, nonspeculative redressability, while preserving the distinction from the noncontrolling absent-agency application.
- **Gizoni's reserved issue:** Standards lines 1125–1133 remove the affirmative conclusive-record summary-judgment instruction and expressly preserve that question as unresolved. Its public explanation retains the substantial employment-related vessel connection.
- **Hunter's validation evidence:** The dated annex at record line 52 now identifies itself as the §8 sanitized reconciliation audit, states its input boundary and provenance/location, and supplies its result. This clears the previously unidentified-check finding; it does not independently authenticate unrecorded historical process.
- **Zatko's count and caption:** Workspace line 5294 now refers to the seventeen dockets' applicants rather than seventeen distinct petitioners. The public closing caption matches “companion matters.” All seventeen docket identities and the open compliance condition remain represented.
- **The rest of the previously identified Casey workspace repair:** The full framework, direct five-Justice authority, principal provision results, separate-writing summaries, accepted alternatives and evidentiary qualifications, clinical safeguards, and general Step 6/Ohio v. Akron treatment are now supplied. The Neutral Projection now states the correct framework and timetable result and the conditional burden allocation. Finding 1 identifies the three surviving contradictions rather than reviving the cleared omissions.
- **Earlier Wrigley, Estelle, and Presley items:** The independent-contractor and office qualifications remain supplied, Estelle's research cutoff is stated, and Presley's entering-law date for Campos is corrected. The Standards source-limitation note identifies Wrigley's earlier gap as resolved.

## Coverage and preservation

| Source group | Coverage |
|---|---|
| Chunks 1–5 | 41 Court-event records and the October 23 Admitted Source Record, with candidate and public-projection comparisons. |
| Chunks 6–10 | 46 Court-event records, including the older correction insertions, with candidate and effective public-projection comparisons. |
| Chunks 11–14 | 37 Court-event records, including the operative Casey version 1.5 adjudication, with candidate and public-projection comparisons. |
| Term-level material | Opening trackers, complete inventory, manifest, ledger and correction receipts, continuity and neutral projections, all three candidates, Standards limitation note, and fourteen public outputs. |

Working evidence is confined to `tmp/`: [mechanical checks](../../../tmp/audit-1991-r3-mechanical.json), [structural checks](../../../tmp/audit-1991-r3-structure.json), [record/workspace text comparisons](../../../tmp/audit-1991-r3-projection.json), [boundary checks](../../../tmp/audit-1991-r3-boundaries.json), and reviewer notes for [chunks 1–5](../../../tmp/audit-1991-chunks1-5.md), [chunks 6–10](../../../tmp/audit-1991-chunks6-10.md), and [chunks 11–14](../../../tmp/audit-1991-chunks11-14.md). Text-comparison nonmatches are review leads, not automatic findings. Permitted candidate/public-render compression and docket omission from an otherwise matching closing caption are not treated as discrepancies merely because they differ byte-for-byte; the separate express requirement for unchanged Holdings text at the Record-to-Render-Input handoff is addressed above.

The [preservation check](../../../tmp/audit-1991-r3-preservation.json) compared all **245 pre-existing files** in the [source baseline](../../../tmp/audit-1991-r3-source-hashes.json), covering foundation, state, every protected term directory, existing close documents, workspace, case inventory, and AGENTS.md. All remained byte-identical. Only this new close report and working files under `tmp/` were written. No Git command was run.

No discrepancy was repaired. The absent Term-Close Dossier and unchanged `state/` are expected in this staged Audit pass. No finding rests on the passes not being Git-committed. The unresolved items must be resolved through the authorized correction/projection process and the coordinated set audited again before Commit. This report creates no new holding, vote, Court event, or tracker cutoff.
