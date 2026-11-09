# October Term 2000 - Confirming Close Re-audit

Audit date: November 9, 2026.
Repair reviewed: `343910da` (parent `9a68a2a85ae0275fb7116dfd41058a1def6e14e7`).

**Disposition:** F1-F5 are resolved. No discrepancy remains unresolved. October Term 2000 is ready for the Close Commit.

## Scope and method

This confirming review covers the repairs, repeats the deterministic close checks for all 114 events and eight chunks, and reopens the legal substance affected by the repairs. The preceding audit's full-term substantive review remains the baseline for unchanged adjudications; this report does not claim a second independent rereading of every historical source or every duplicated annex. Records control over projections. File locations below are repository-relative, with one-based line numbers.

The term checker ran first. The remaining deterministic checks passed before the focused legal-substance review began. Read-only `git cat-file` lookups verify the repair and parent objects and the relevant term trees. Before replacing this report, all 1,608 inspected direct files in the term's root, briefs, runtime, entering-law, freeze, records, render-inputs, output, workspace and close directories matched their repair-commit blobs. Comparison with the parent identifies eight changed OT2000 files, confined to the F4/F5 repairs and their required projections and pass-note updates. Other event entries are unchanged. Each repaired file retains its previous line endings: the public chunk-4 output uses LF; the other seven use CRLF.

The user's standing directions control: published trackers need no GitHub repository URLs; unresolved relative navigation within preserved freeze and entering-law copies is exempt; seamless repairs require no correction-specific version, lineage, receipt or narrative in Records or public copies. No missing correction provenance is treated as a defect, and no such provenance was added. No prohibited directory or filename was accessed. Git use was limited to the permitted term checker and read-only `cat-file` lookups. Repository commitment-order verification remains with the operator, as the ledger discloses; effective-date order was independently checked here.

## Repair verification

| Finding | Confirming result |
|---|---|
| F1 - Oakland participation | Resolved and retained. Breyer's nonparticipation appears in `terms/OT2000/workspace/manifest.md:147`, `workspace/continuity.md:5804,5823`, and `workspace/neutral-projection.md:4599,4643`. These agree with the Oakland Record and its eight participating Justices. The Hatter, New Hampshire and Pollard exceptions remain accurate. |
| F2 - Kansas carryover | Resolved and retained. Kansas remains pending before the Special Master in `terms/OT2000/workspace/manifest.md:3,142`, `workspace/continuity.md:9,5798,5960`, `workspace/neutral-projection.md:9,4636,5881`, and `close/STANDING_STATE.candidate.md:61`. The completed June 11 decision is distinguished from the remaining damages calculation and preparation of judgment. Arizona/Fort Yuma remains carried; Fiore's lower-court habeas work is not converted into an open Supreme Court event. |
| F3 - Kansas navigation | Resolved and retained. All four links in `terms/OT2000/records/Kansas_v_Colorado_merits_2001-06-11.md:227` use `../freeze/` and resolve to the intended files. No adjudicative text changed. |
| F4 - Children's Healthcare institutional conditions | Resolved. The missing nonmedical-care, religious-reliance, medical-services, ownership and affiliation requirements are now stated in their own terms. Their exceptions retain their separate scopes. The repaired paragraph agrees across the Record and all affected public and tracker projections listed below. |
| F5 - Rogers possessive | Resolved. `terms/OT2000/close/STANDARDS_AND_TESTS.candidate.md:7133` now reads `law's`. Comparison with the parent shows only the apostrophe repair at this rule; doctrine and authority are unchanged. |

F4's verified propagation locations are:

| File | Line(s) |
|---|---|
| `terms/OT2000/records/Childrens_Healthcare_Is_a_Legal_Duty_v_Min_De_Parle_merits_2001-04-23.md` | 128, 297 |
| `terms/OT2000/render-inputs/OT_2000CHUNK4.md` | 1137 |
| `terms/OT2000/output/OT_2000CHUNK4.md` | 1130 |
| `terms/OT2000/workspace/continuity.md` | 2041 |
| `terms/OT2000/workspace/neutral-projection.md` | 1902 |
| `terms/OT2000/close/HOLDINGS.candidate.md` | 36606 |
| `terms/OT2000/close/STANDARDS_AND_TESTS.candidate.md` | 8690 |

The Standards pass note now describes the completed conditions at `terms/OT2000/close/STANDARDS_AND_TESTS_PASS.md:23,104`. Its candidate digest at line 35 matches the actual SHA-256, `3510075d3c274872c7d63de6ef3abe5e5f8573f96a65d52849ebe95553ea3b24`. The stale limitation statements are gone. The candidate scan finds no remaining word-internal question-mark or replacement-character defect.

## Deterministic checks

- **Term checker and opening Holdings:** `python tools/check_term.py OT2000` passes. Its two warnings are source-identifier false positives: the Library of Congress identifier at `terms/OT2000/records/Alabama_v_Bozeman_merits_2001-06-11.md:188`, and the Third Circuit amendment filename at `records/Sterling_v_Borough_of_Minersville_merits_2001-04-24.md:247`. Neither is a Git reference. Actual cited commit objects resolve. `python tools/holdings_volumes.py check` also passes.
- **Coverage and chronology:** All 114 inventory entries reconcile to 114 unique Records, 114 manifest completions and 114 matching ledger rows. Case/docket identities, dates, results and ledger fields agree. Inventory scheduling annotations were included explicitly. The effective range is October 10, 2000-June 28, 2001; event order and closing boundaries agree across the eight chunks, whose totals are 12, 15, 14, 15, 14, 15, 14 and 15. Same-date grouping and the disclosed coordinated sequence remain intact.
- **Splits, freezes and public identity:** Runtime-split freshness passes. All eight commitment pairs and eight reconciliation pairs match their frozen counterparts byte-for-byte. All 114 generated Render Input entries match their Records' bounded Public Projections. Public outputs preserve event coverage and chronology; the repair changes only Children's Healthcare's affected paragraph within chunk 4.
- **Durable digests:** All 128 selected current digest comparisons pass: the chunk-2 handoff index and aggregates, chunk-3 stage index, chunk-8 final selected handoffs and aggregates, Lorillard final neutral handoff, and the fifteen chunk-8 Records in each of the two final Record receipts. Historical stage snapshots were not misclassified as assertions about subsequently replaced working files.
- **Participation and arithmetic:** Computational checks reconcile 84 compact judgment statements and 51 component rows with their named coalitions. The remaining complex forms were checked directly, including Bush, Hicks, KDM, Garvey, Kentucky River and Wallis. The five entries without a disclosed numerical tally preserve that limit. Oakland has eight participants, Hatter seven, New Hampshire eight and Pollard eight. Judgment votes remain distinct from rationale joins.
- **Assignments:** An independent census from the opinion tables reproduces 103 counted signed plenary lead opinions and eleven excluded events: Stone-Zsela 10, Stevens 12, O'Connor 12, Scalia 11, Kennedy 11, Souter 12, Thomas 12, Ginsburg 11 and Breyer 12. The repairs change no assignment or eligibility premise. This census does not claim to reconstruct repository commitment order.
- **Navigation and presentation:** Across 144 active Markdown files, all 1,830 local href occurrences resolve, including anchors. Candidate navigation was evaluated at its intended publication destination with staged Holdings substituted where appropriate. The 705 external href occurrences were distinguished from local references; their availability was not comprehensively retested. No reference-definition or HTML-href omission was found. The 236 labeled controlling explanations in each of the Record public, Render Input and output layers satisfy the ordinary 350-word ceiling; the maximum is 212 words.
- **Candidates and carry-forward:** All 2,740 opening Holding fields remain intact. Standards has 940 unique entries, with required fields in all 109 additions/replacements and substantive preservation of the 831 unreplaced entries, including three documented title-reference updates. Its coverage accounts for all 114 Records. The three candidates' publication fields agree and intentionally await coordinated advancement at Commit. Standing State preserves the nine-seat OT2001 roster, thirteen circuit allotments, unchanged referral practice, and Arizona and Kansas carryovers. No scheduled inventory event remains uncompleted. Candidates and pass notes correctly remain until successful Commit; no premature publication or cleanup occurred.

## Confirming legal-substance review

F4 was checked against the enacted text of [Public Law 105-33, section 4454, 111 Stat. 427-429](https://www.govinfo.gov/content/pkg/PLAW-105publ33/html/PLAW-105publ33.htm), including Social Security Act sections 1861(ss)(1)(C), (F), (G), 1861(ss)(4), and 1821, and against the preserved statutory source. The ownership threshold, affiliation exceptions and election exceptions remain distinct. The completed conditions limit constitutional permission without establishing actual eligibility, compliance or entitlement.

Children's Healthcare retains its three controlling grounds, component-specific authority and 5-4, 9-0 and 6-3 dispositions. The five direct joins to the operational-remand rationale remain distinct from Stone-Zsela's additional judgment vote. The repair adds no finding of financed prayer or ineffective public review and no new remedial command. Its changed text supplies the previously omitted terms of existing limits; it does not change a coalition, historical-departure premise or assignment. The Holdings and Standards candidates preserve that distinction. The subsequent Freiler and KDM uses retain their bounded accommodation and actual-function analysis and acquire no changed decisional premise.

The Rogers repair was checked against its Record's rule and authority. It leaves the five-Justice framework coalition distinct from the judgment coalition and changes only typography. F1-F3 remain accurate participation, procedural-continuity and navigation repairs, without any change to Oakland's merits or Kansas's component dispositions and recommittal.

The prior full-term legal-substance conclusion remains clean after review of every affected part and the identified downstream uses. This confirming review finds no new defect in votes, joins, holdings, precedent treatment, remedy, continuity or Justice-specific historical departures.

## Remaining discrepancies and handoff

No discrepancy remains unresolved. F1-F5 are closed, and the term is ready for the Close Commit. This audit does not perform that Commit: the operator must publish the synchronized trackers, advance their common metadata, generate the close dossier and indexes, verify publication and complete the prescribed candidate/pass-note cleanup.

Only `terms/OT2000/close/AUDIT.md` is changed as a repository deliverable, preserving its CRLF endings. No adjudication, public copy, tracker or frozen artifact was modified by this review.

READY FOR CLOSE COMMIT: YES
