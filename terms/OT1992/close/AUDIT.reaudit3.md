# October Term 1992 — Third close re-audit

**Audit date:** September 17, 2026.  
**Result:** **Not ready for Commit.** Findings **4, 8, 13 and 15 are resolved**. Finding **11 remains partly resolved**, solely because the revised provenance still misstates parts of the actual correction history. No additional substantive discrepancy was identified.  
**Scope:** Report only. No candidate, adjudication, workspace, input, render or opening tracker was changed.

This report supplements the [second re-audit](AUDIT.reaudit2.md), [first re-audit](AUDIT.reaudit.md) and [original audit](AUDIT.md), preserving their finding numbers. It examines the complete repair diff from `09e1b21` to `f47a06ab8b33490724b493eaf1216fdfd85f242d`, the examined HEAD. The working tree was clean at intake. Commit identifiers in this report are read-only historical references; this pass made no commit.

## Verification of the five requested findings

| Finding | Result | Verification |
|---|---|---|
| 4. Hartford qualification and provenance | **Resolved** | The complete export alternative, claim connection and export-only injury limit remain in the entering-law paragraph, with applicability reserved. The record now identifies version 1.1, the superseded initial version, corrective commit `563cb7b`, correction scope and conservation of the adjudication. The annex, durable-status section and workspace ledger identify the repair consistently. |
| 8. Unchanged holding handoff | **Resolved** | Both Demos holdings now carry their separate precedent-treatment lines into the input's Holdings block. Moreau's earlier-hire operative rule now reproduces both source sentences exactly. All four operative rules, authority statements and controlling explanations, and each holding's precedent treatment, are present unchanged in their respective Holdings blocks. |
| 11. Correction lineage and metadata | **Partly resolved** | The three input metadata sections now match Demos and Moreau version 1.1 and Blair version 2.1; Blair's Event reference is also synchronized. The annexes now distinguish later corrections from initial completion. Demos and Moreau nevertheless contain false statements about which commits changed their records and what those record changes did. Their durable-status text also retains an inaccurate contemporaneous ledger-append claim. See the remaining discrepancy below. |
| 13. Ledger and cumulative law | **Resolved** | The ledger identifies `b17e334` as position approval and `e147769` as initial completed-record publication. Demos and Moreau now appear at the end as explicitly retrospective recoveries of omitted entries, rather than pretending to have been appended at their effective-date positions. All 126 records occur once in the actual ledger. Their cumulative law, limits and neutral-law incorporation remain intact; neither effective date nor the July 26 cursor changes. |
| 15. Historical comparator in neutral projection | **Resolved** | The offending historical Blair disposition and execution comparison is removed. The neutral paragraph retains the simulated continuing stay, further proceedings below and unrecovered-source limits without supplying that historical outcome. |

Findings 1, 2, 3, 5, 6, 7, 9, 10, 12 and 14 retain their previously resolved status. The repairs do not disturb their relevant content.

## Remaining discrepancy

### 11. Demos and Moreau still misdescribe their correction history

**Locations:** Lineage, Adaptive audit annex and Validation and durable commitment in the [Demos record](../records/Demos_v_Storrie_fee_motion_1993-03-08.md) and [Moreau record](../records/Moreau_v_Klevenhagen_merits_1993-05-03.md). Cross-check: the two retrospective recovery rows in the [workspace ledger](../workspace.md#term-working-ledger-index).

The required metadata synchronization is now complete. Blair's new annex note also identifies the later labeling/interface repairs and preserves its 4–4 disposition. Those portions of finding 11 need no further repair.

Three provenance statements in Demos and Moreau remain inaccurate:

1. Both lineage paragraphs say that commits `563cb7b` and `ac3ebda` carried the record's content into downstream projections **“without further change to this record file.”** That is true of `563cb7b`, but false of `ac3ebda`: its actual diff changes the lineage paragraph in each record, identifying version 1.1 and the preceding correction set. It also changes Blair's record and the workspace. It does not edit the input or public-render files. Distinguish unchanged adjudicative substance from an unchanged record file, and identify each commit's actual role.
2. The descriptions of `3cc14e4` continue to mix record corrections with projection corrections. Demos's lineage says **both** controlling explanations were expanded within the record; the diff expands only the prospective-restriction explanation, changes the record's render-form selection and adds that holding's Denton precedent line. The current-filing explanation was already present. Moreau's lineage and new annex say the alternatives and no-presumed-consent limit were restored within the record, culminating in **“All are corrected within this record.”** Its record diff changes only the two controlling explanations. The operative “agreements or understandings” alternative and the no-presumed-consent limit were already in the source record; their restoration was a downstream projection repair. The annex itself recognizes a downstream omission but then inaccurately describes its repair as a record correction.
3. Both durable-publication lines still attach **“ledger appended”** to the September 16 version 1.0 publication. The September 16 `e147769` publication added the records, inputs and workspace references but omitted the actual ledger rows, as finding 13 established. The rows first appeared in `ac3ebda`; the present `f47a06a` repair relocates and expressly labels them as retrospective recoveries. The durable account must distinguish record publication from that later ledger recovery, consistently with the now-correct workspace.

The read-only history establishes the following allocation:

| Existing commit | Relevant actual change |
|---|---|
| `b17e334` | Approved Stone supplements in the two briefs; not completed-record publication. |
| `e147769` | First publication of Demos and Moreau records, their input projections and associated workspace changes; no actual ledger rows for these events. |
| `3cc14e4` | Demos record: full-form selection, prospective explanation expansion and added prospective Denton treatment. Moreau record: two explanation expansions. The same commit also repaired downstream inputs and renders. |
| `563cb7b` | Further Demos/Moreau projection repairs; neither of those record files changed. Separately completed Hartford's statutory account and repaired Blair's input interface. |
| `ac3ebda` | Demos/Moreau lineage edits, Blair lineage/durable-status edits, and workspace version, ledger and cumulative-law changes. No input or public-render edit. |
| `f47a06a` | The currently examined provenance, handoff and workspace repairs, including new annex notes, metadata synchronization, retrospective ledger placement and neutral-comparator removal. No public render changed. |

These are correction-account errors, not grounds to alter a rule, vote, coalition, disposition, remedy or separate writing. Correct the existing provenance statements to match the actual history and the retrospective ledger account. No further explanation expansion or re-adjudication is required by this finding. Preserve the completed handoff and metadata repairs.

## Term-wide checks and conservation

This pass reviewed every changed line against the second-re-audit revision, checked the affected record/input fields directly, examined the cited correction commits, and repeated the term-wide coverage, candidate-header, link, duplicate and baseline-preservation checks. Unchanged substantive material uses the preceding audits as its review baseline; this is not a new historical reconstruction of all 123 adjudications or a certification of new external-source retrieval.

- Exactly eight artifacts changed in the repair: four records, three inputs and the workspace. All three candidates, all eleven public renders, the other 122 records, the other eight inputs, the inventory and opening trackers are unchanged from the second re-audit.
- All 126 records remain present: 123 Court-event records and three admissions. The actual ledger contains 126 distinct record links, with no missing or duplicate record. The public chunks contain 123 entries and 123 matching closing lines.
- Only the Demos, Moreau and Blair input event blocks changed. Other event blocks in the affected chunks are identical after line-ending normalization. The repaired handoffs preserve the eleven-block interface. No repair changes a vote, author, named coalition, disposition or remedy.
- The four source/input explanation word counts remain 171 and 199 for Demos, and 185 and 175 for Moreau. The public explanations remain 171/200 and 185/175. Demos's public “before the Court” for “before it,” and Moreau's faithful public paraphrase of the earlier-hire rule, remain permissible render wording; the expressly unchanged input handoff now passes independently.
- Candidate header values agree: **Last completed October Term: 1992**; **Processed through: July 26, 1993, after DeBoer v. DeBoer, No. A-64.**; **Edition: September 17, 2026**. Trailing Markdown whitespace does not change those values.
- Local candidate file links and heading anchors resolve both in `close/` and under a prospective unchanged copy into `state/`. This confirms the existing workspace paths, not portability to another host.
- No exact duplicate holding text or Standards title was found. The opening Holdings substance remains present. The prior Crosby spacing mismatch and opening-header replacement are the same already-reviewed mechanical comparison exceptions, not new legal omissions. The candidate set is byte-unchanged from the second re-audit.
- Standing State retains the correct OT1993 roster and seniority, thirteen August 10 circuit assignments, the referral practice and eight supported carried matters: Zatko and companions, Wyoming, Reynolds, Grubbs, Martin No. 92-5618, Louisiana, Delaware and Nebraska. Blair remains complete at this Court; further proceedings below are not promoted to a pending Supreme Court matter. No noncontrolling proposal or equal-division rationale is added to current law.

Working evidence is under `tmp/reaudit1992-third/`: the intake hashes, checking scripts, `checks.json`, `delta.json`, `final-checks.json`, saved read-only correction diffs and final integrity results. String comparisons were checked against their legal and documentary purpose; an unchanged public paraphrase is not treated as a failed verbatim input handoff.

## Commit condition and boundaries

**Finding 11 alone remains open.** Commit must await an accurate correction-history account and verification of that limited repair. No new separately numbered discrepancy is added. Findings 4, 8, 13 and 15 should not be reopened merely because finding 11 remains unresolved.

The only durable file written by this pass is `terms/OT1992/close/AUDIT.reaudit3.md`. Earlier audits, candidates and close notes remain unchanged. Scratch files were written only under `tmp/`. No file under foundation, stone, state, or OT1992 briefs, runtime, records, render-inputs or output was modified; the workspace was not modified. No git commit, checkout, branch or push command was run. No Term-Close Dossier or tracker replacement was performed.
