# October Term 1992 — Second close re-audit

**Audit date:** September 17, 2026.  
**Result:** **Not ready for Commit.** Findings 7, 12 and 14 are resolved. Findings 4, 8, 11 and 13 remain partly resolved. Newly identified finding 15 concerns the neutral projection.  
**Scope:** Report only. No adjudication, candidate, workspace, input, render or opening tracker was changed.

This report supplements the preserved [original audit](AUDIT.md) and [first re-audit](AUDIT.reaudit.md). It retains their finding numbers. It examines the hand-applied changes in `563cb7b` and `ac3ebda`, against first-re-audit revision `7dbc6c2`. The examined HEAD is `ac3ebda11d5e23e9ebfb2a384f1c47b38f49302d`; the working tree was clean at intake. These are read-only history references, not commits made by this pass.

## Verification of the seven requested findings

| Finding | Result | What is repaired and what remains |
|---|---|---|
| 4. Hartford qualification | **Partly resolved** | The entering-law paragraph now supplies the export alternative, its claim connection and export-only injury limitation, while reserving applicability. The completed record still identifies itself as the initial v1.0 with no superseded decision; neither its audit annex nor the workspace identifies this correction. |
| 7. Moreau alternative | **Resolved** | Standards now expressly permits individual subsection (ii) “agreements or understandings” for later hires. The earlier-hire transition route, actual-consent condition and legally capable representative reservation remain distinct. |
| 8. Explanations and unchanged handoff | **Partly resolved** | All four source explanations now enter the inputs verbatim, and the public explanations preserve their substance. Moreau's earlier-hire operative rule is still rewritten in the input; Demos's holding-specific precedent treatment is still omitted from Holdings and condensed in a separate block. |
| 11. Correction lineage and metadata | **Partly resolved** | Demos and Moreau now identify version 1.1; Blair identifies version 2.1. Their lineage paragraphs name corrective commits, and workspace version references were updated. The three input metadata sections are unchanged; Blair still points to version 2.0. The audit annexes still describe the earlier corrections rather than the latest completed-record repairs. |
| 12. Blair input form and interface | **Resolved** | The Event selects full form; the sixth block is again `Holdings`, with an express no-controlling-holding statement. The input retains the eleven required blocks in order. The public entry already has both tables and accurately reports a nonprecedential equal division. |
| 13. Ledger and cumulative law | **Partly resolved** | Both records are now in the actual ledger, and their controlling rules and limits appear in cumulative Current Law, which the neutral interface incorporates. The new ledger rows identify the wrong completion commit and were inserted in effective-date positions despite the ledger's append-only commitment-order requirement. |
| 14. Demos public particulars | **Resolved** | The public entry now supplies no oral argument, 507 U.S. 290, the Ninth Circuit's 962 F.2d 13 and May 11, 1992 date, petition/lower-disposition source links, and the supplied public-source qualification. It publishes no certiorari poll or correction lineage. |

Findings 1, 2, 3, 5, 6, 9 and 10 retain their previously resolved status. The new repairs do not disturb their relevant content. Finding 6's restored reservations, Denton treatment and full-form tables remain present; that does not itself satisfy finding 8's distinct unchanged-handoff requirement.

## Remaining discrepancies

### 4. Hartford's completed-record correction still lacks provenance

**Locations:** [Hartford record](../records/Hartford_Fire_Insurance_v_California_merits_1993-06-28.md), lines 5 and 29, Adaptive audit annex and Validation and durable status; [workspace](../workspace.md), Hartford ledger row at line 294.

The defective “specified U.S. export effect” shorthand is gone. The new paragraph states the direct, substantial and reasonably foreseeable effect on the export trade or commerce of a person engaged in that trade or commerce in the United States, the paragraph (2) claim connection, and the export-only injury limitation. The applicability reservation remains. No foreign-effects holding, vote, remedy or public projection changed.

However, `563cb7b` changes an already completed record while its lineage still says “initial record v1.0; no completed decision superseded.” The audit annex and durable-status account contain no identification of this repair, and the workspace still calls it an initial v1.0 event. The first re-audit expressly required correction provenance as well as completion of the statutory account. Preserve the existing adjudication and identify the superseded record, correction version, actual history references and scope of this authorized change. Do not invent a commit for work not yet committed. The supplied source map remains the official report and judgment below; this pass does not certify a new retrieval or a new admitted source.

### 8. Correct explanations do not yet make the entire holding handoff unchanged

**Locations:** Demos's Law of the decision in its [record](../records/Demos_v_Storrie_fee_motion_1993-03-08.md), and Holdings at lines 658–675 of the [chunk 4 input](../render-inputs/OT_1992CHUNK4.md); Moreau's earlier-hire rule in its [record](../records/Moreau_v_Klevenhagen_merits_1993-05-03.md) and line 796 of the [chunk 6 input](../render-inputs/OT_1992CHUNK6.md).

The explanation repair succeeds:

| Explanation | Record words | Input words | Public words | Assessment |
|---|---:|---:|---:|---|
| Demos, current filing | 171 | 171 | 171 | Exact explanation in both projections. |
| Demos, prospective restriction | 199 | 199 | 200 | Exact input; public “before the Court” replaces “before it,” without substantive change. |
| Moreau, earlier hires | 185 | 185 | 185 | Exact explanation in both projections. |
| Moreau, later hires | 175 | 175 | 175 | Exact explanation in both projections. |

The source/input counts use whitespace-delimited words. All satisfy the applicable range. Moreau's later-hire operative rule and its precedent line now also match the source, including the limitation to the two routes presented. No further explanation expansion is needed.

Two outstanding differences remain:

- Moreau's source ends the earlier-hire rule with a separate sentence: “This transition rule operates independently of, and does not require, a further individual or collective agreement for that cohort.” The input substitutes a participial phrase, “operating independently of any further individual or collective agreement for that cohort.” This is substantively compatible, but it does not satisfy the express instruction to carry the record's controlling-holding content into Holdings unchanged. Restore the supplied rule there; the renderer may use faithful public prose.
- Neither Demos holding carries its source precedent-treatment content into the input's Holdings block. The separate Precedent Treatment block still merges and rewrites it. In particular, the source separately distinguishes Sindram's extraordinary-writ setting and preserves its force; the projection combines Sindram with McDonald as preserved authority. The source's In re Demos line expressly says the earlier restriction does not itself resolve this civil-certiorari fee question; the projection substitutes a statement that the earlier restriction remains in force. These formulations are related but are not the unchanged holding-specific treatment the previous finding required.

Carry the existing source holding content, including its precedent treatment, into the required handoff. Preserve the eleven-block interface and render without needless repetition. These are projection corrections, not grounds for new reasoning or altered dispositions.

### 11. New lineage labels are not synchronized through the correction record and handoff

**Locations:** Lineage and Adaptive audit annex sections of the [Demos](../records/Demos_v_Storrie_fee_motion_1993-03-08.md), [Moreau](../records/Moreau_v_Klevenhagen_merits_1993-05-03.md) and [Blair](../records/Delo_v_Blair_application_to_vacate_stay_1993-07-21.md) records; metadata in inputs [4](../render-inputs/OT_1992CHUNK4.md), [6](../render-inputs/OT_1992CHUNK6.md) and [11](../render-inputs/OT_1992CHUNK11.md).

The new lineage paragraphs are real improvements: they identify corrective versions and the actual correction commits. Blair's durable-commitment line also now names version 2.1. But comparison with `7dbc6c2` confirms that all three chunk metadata sections are unchanged. Chunk 11's metadata and Blair Event still describe the linked record as version 2.0. Chunks 4 and 6 still describe only completion of the former stopped matters, without the subsequent correction metadata required by AGENTS.md.

Demos's and Moreau's annexes still say that only a stopped-matter placeholder is replaced. Their durable-publication lines still describe September 16 completion without distinguishing the September 17 completed-record repair. Blair's annex still accounts only for the version 1.0 reasoning defect, not the later labeling and input-form repairs. The current versions should distinguish the initial completion from subsequent corrections and record the scope and conservation checks for those corrections. The input metadata must agree with the current record versions. Keep this provenance out of the public renders.

The historical references in the new lineage paragraphs describe a correction set spanning records and projections; `563cb7b` did not itself edit the Demos, Moreau or Blair record files. A corrected account should preserve that distinction rather than imply that every cited commit changed each record.

### 13. Missing entries are restored, but the new ledger provenance and order need correction

**Locations:** [Workspace](../workspace.md), ledger rows 213 and 238; Current Law entries at lines 1681 and 2436; Current-Term Neutral Projection.

The principal completeness defect is repaired. All 126 record filenames now occur in the actual ledger, not merely somewhere in the workspace. Demos's two rules, reservations and precedent treatments appear in Current Law. Moreau's two statutory routes, actual-consent limit and reserved questions also appear. The neutral interface's instruction to supply cumulative Current Law now includes both cases.

The new ledger rows nevertheless say each case was “completed by correction at commit b17e334.” Read-only history establishes:

- `b17e3343459858e9fee1b405ec71db1cd4e48e95` changes only the two briefs and supplies the approved Stone supplements.
- `e147769e90d3219925fd56f2fcf476f1beb375d2` first adds both completed Decision Records, their input projections and corresponding workspace changes.

The completion attribution to `b17e334` is therefore a new factual error introduced by the attempted repair. Identify approval and completed-record publication separately.

The two rows were also inserted among the original chunk 4 and chunk 6 entries in effective-date order. Both records were completed after the original chunk 6 Run; the ledger expressly claims append-only commitment order, as Engine §2 requires. The first re-audit likewise requested commitment order with effective dates. Preserve the actual commitment sequence, recording any retrospective recovery of an omitted ledger entry explicitly; use the manifest and neutral effective-order view for legal chronology. Do not change either decision date or the July 26 cursor. The later correction history must remain distinguishable from the original publication.

## Newly identified discrepancy

### 15. The Current-Term Neutral Projection contains historical-comparator material

**Location:** [Workspace, Current-Term Neutral Projection](../workspace.md#current-term-neutral-projection), Material continuation limits, line 5331.

The supposedly sanitized projection says: “Unlike the historical record, in which a differently composed Court vacated the stay and the execution proceeded July 21, 1993,” before describing the simulated outcome. This supplies the historical Blair disposition and its aftermath directly to a neutral continuation interface. Engine §§2–3 expressly exclude comparators and reconciliation from that interface; its own preceding paragraph says the same.

This text predates the latest repairs and is newly identified here, rather than attributed to `563cb7b` or `ac3ebda`. Keep the simulated public action, continuing lower-court stay and source limitations in the neutral projection. Keep the historical comparison in the appropriate comparator/audit material. No change to Blair's vote, disposition, separate statements or controlling law is called for.

## Term-wide checks and conservation

The re-audit examined the complete correction diff and changed event blocks, compared source holding fields with the affected projections, and repeated coverage, header, link, duplicate and baseline-preservation checks across the term. Unchanged substantive material uses the prior audits as its review baseline; this is not a fresh historical reconstruction of 123 adjudications.

- Exactly eleven examined artifacts changed since the first re-audit: four records, three inputs, two renders, Standards and the workspace. The other 122 records, nine renders, eight inputs, Holdings and Standing State are unchanged. The opening trackers and inventory are unchanged.
- All 126 records remain present: 123 Court-event records and three admissions. The eleven public chunks retain 123 entries and matching closing lines. All 126 files are now referenced in the actual working ledger.
- Only Demos and Moreau public entries changed. Only Demos, Moreau and Blair input event blocks changed. Other blocks in the affected chunks are identical after line-ending normalization; chunk 11's public render is unchanged. No repaired block changes a vote, author, named coalition, disposition or remedy.
- All candidate header values agree: last completed term **1992**; processed through **July 26, 1993, after DeBoer v. DeBoer, No. A-64.**; edition **September 17, 2026**.
- Local candidate links and heading anchors resolve both in `close/` and under a prospective unchanged copy to `state/`. This validates the existing absolute-path links in this workspace, not portability to another host.
- No exact duplicate holding text or Standards title was found. The opening Holdings substance survives. The already-reviewed Crosby spacing mismatch is harmless; the unchanged prior source-comparison exceptions are not reopened as substantive defects. The only new candidate change is Moreau's restored “or understandings.”
- Standing State still has the proper OT1993 roster and seniority, thirteen August 10 circuit assignments, the unchanged referral practice and eight supported carried matters. Blair remains closed at this Court; ordinary remands remain proceedings below. No separate-writing proposal or equal-division rationale is promoted to law by the repairs.

Working evidence is under `tmp/reaudit1992-second/`: `before.json`, `checks.json`, `delta.json`, the checking scripts and final integrity results. String mismatches were reviewed for meaning: the public “before the Court” wording is harmless, while the expressly required unchanged input handoff remains incomplete. No external historical-source recovery or re-adjudication is certified.

## Commit condition and boundaries

Do not perform the Commit pass while findings **4, 8, 11, 13 and 15** remain unresolved. The needed work is limited to the identified provenance, handoff and workspace defects, followed by verification of the resulting set. Findings 7, 12 and 14 require no further repair unless later changes disturb them.

The only durable file written by this pass is `terms/OT1992/close/AUDIT.reaudit2.md`. Earlier audits, close candidates and notes remain unchanged. Scratch files were written only under `tmp/`. No file under foundation, stone, state, or OT1992 briefs, runtime, records, render-inputs or output was modified; the workspace was not modified. No git commit, checkout, branch or push command was run. No Term-Close Dossier or tracker replacement was performed.
