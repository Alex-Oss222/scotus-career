# OT1995 chunk 8 ? completed three-matter revision validation

Status: Run complete in the working files. All twelve chunk 8 inventory slots are completed; no stopped matter remains. Operator review and commit remain pending. No Git command was performed.

| Inventory matter | Canonical Record and disposition | Final SHA-256 |
|---|---|---|
| OT1995-077 | [Vera_and_consolidated_merits_1996-06-13.md](../records/Vera_and_consolidated_merits_1996-06-13.md) ? Standing retained 9?0; all three appeals reversed on the merits 5?4. | `ad84885fc495f2f009308d04e57df1982ba8687de7d96f6d994b10a322fe4f6f` |
| OT1995-079 | [Montana_v_Egelhoff_merits_1996-06-13.md](../records/Montana_v_Egelhoff_merits_1996-06-13.md) ? Affirmed 5?4; the state judgment granting a new trial on both counts remains in force. | `1e5d42fe9e9f6fff0c24f77cd5b49f9cc95d9940cb3d5ece9b527ec29850fd78` |
| OT1995-082 | [Leavitt_v_Jane_L_summary_merits_1996-06-17.md](../records/Leavitt_v_Jane_L_summary_merits_1996-06-17.md) ? Summary partial vacatur and remand 5?4; limited severability grant, otherwise denied; necessary independently supported protection preserved. | `2f82dce2ef738610d8b835e00a72ccc326b9561adcd869ff4bed2fa200023851` |

## Stage and chronology validation

The approved brief was not changed. The normal runtime split was regenerated with tools/split_chunk.py. Operator-selected entering-law slices were built with tools/build_entering_law.py using term-opening selections and all actually effective earlier Records: 97 before June13 for Vera and Egelhoff, 102 before June17 for Leavitt. Linked copies contain the complete actual Public Projections. Same-day peers remain excluded. Leavitt received the completed Vera and Egelhoff public decisions before its independent revalidation and reconciliation.

The [current handoff index](OT_1995CHUNK8_REVISION_HANDOFFS.md) identifies each separate frozen independent and reconciled product. Egelhoff and Leavitt use their authorized unchanged neutral packets and concretely revalidated commitments; Vera adds independently modeled merits commitments. The assembly receipts record the final component joins, assignments and source limits. The Vera/Egelhoff assembly context previously received task-summary exposure, disclosed in both receipts; it did not perform independent modeling or reconciliation. Leavitt used a fresh assembly-only context. The operator is not claimed to be blind. File freezes are durable handoffs, not Git commits.

The [completed dependency review](OT_1995CHUNK8_REVISION_DEPENDENCY_REVIEW.md) clears all six same-day/later peers, including Jaffee. Only Rise, Melendez, Calderon and Gray receive internal entering-law-note changes. Their public text is unchanged; no peer result, ground, opinion join, remedy or assignment is changed. The revised common pre-June14/17/20 neutral baselines include every earlier-effective Record and exclude their same-day groups. The current workspace expressly points upcoming June20 peers to the revised common baseline, excluding Gray.

## Mechanical validation

- Original rebuild_ledger.py main ran through the scoped no-Git adapter: 106 Records; preexisting first-record metadata preserved and the new Egelhoff Record marked operator commit pending.
- Original rebuild_manifest.py ran: 115 inventory events, with the three matters retained in their existing slots and dates.
- Original build_render_input.py generated [chunk 8 Render Input](../render-inputs/OT_1995CHUNK8.md) from exactly twelve Records, without stopped metadata. All changed Records are in chunk8; no other chunk Render Input requires regeneration.
- Original check_term.py main ran through the scoped no-Git adapter: **OK, zero warnings**. Its 201 referenced commit hashes were explicitly not checked. The [tool log](OT_1995CHUNK8_REVISION_TOOL_VALIDATION.md) records the actual output.
- [Scope check](OT_1995CHUNK8_REVISION_SCOPE_CHECK.json): **PASS**. Initial hashes confirm IBM, every other untargeted/nonpeer Record, the approved brief, case-list and all eight existing output files are unchanged. Both superseded Record names are absent. Peer identity/date/result and complete Public Projection preservation pass; [byte hashes](OT_1995CHUNK8_REVISION_PEER_NOTE_RECEIPT.json) record the four internal-note updates.
- [Link check](OT_1995CHUNK8_REVISION_LINK_CHECK.json): 35 local file targets in the three Records and assembly receipts checked, none missing. A separate scoped scan finds zero Markdown links to the old Record or public-copy names. Live workspace/Render Input source references use current names; former names in internal lineage, old snapshot identifiers and preservation hashes remain truthful historical identifiers.
- [Navigation receipt](OT_1995CHUNK8_REVISION_NAVIGATION.json) documents renamed link targets and explanatory historical annotations in affected old handoffs. No old frozen vote, ground or historical process assertion was silently rewritten. Earlier input hashes refer to the original bytes identified by this receipt.
- [Assignment reference](OT_1995CHUNK8_REVISION_ASSIGNMENT_REFERENCE.md) coordinates the current named-opinion count of 84, retaining all untargeted assignments and distinguishing their original historical sequence statements.

## Deliberate limits and remaining operator work

No public Render was performed; every output file remains unchanged under the express instruction. The generated Render Input is ready for a separate Render task. No foundation, state, tools, case-list or brief edit was made. Work and source artifacts stay under existing OT1995 subfolders, with ignored tmp scratch; no research directory was created. The locked top-level private directory was never read, listed, searched or modified.

Only operator verification of repository history/commit existence and the operator commit remain. These are deferred by the explicit no-Git instruction, not certified as passed. There is no adjudicative, coalition, source or dependency blocker for the three completed matters.
