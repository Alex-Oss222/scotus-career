# OT1993 correction handoff — September 28, 2026

This is the implementation receipt for the user's authorized F01–F08 corrections, not a replacement Audit. The September 28 FAIL report and Appendices A–F were read in full before work. `close/AUDIT.md` remains byte-identical. No Audit, `check_term.py`, fresh substantive audit, Git command, commit or state publication was run. F09 was intentionally left untouched. All writes are under `terms/OT1993/` or ignored `tmp/`.

| Finding | Work completed | Status |
|---|---|---|
| F01 | Beecham/Jones now states “ship, transport, possess, or receive” in the internal holding and Public Projection. Its corrected controlling proposition and May 16, 1994 effective date are incorporated under Criminal Procedure in the Holdings candidate; its independently derived selector rule is incorporated in the Standards and Tests candidate. Dated follow-ups resolve the pass notes' earlier deferrals. | Fixed. |
| F02 | Granderson's date is March 22, 1994 in the Beecham Record, chunk 4 Render Input and public entry, and every Appendix B entering-law copy. The corrected qualification is also propagated through the listed reading and workspace copies. | Fixed. |
| F03 | Recovered all outstanding Appendix C1 files from Library of Congress U.S. Reports PDFs and the Caselaw Access Project Howell source. All 23 distinct cited targets now resolve. | Fixed; retrieval details and the 15-new/8-existing file accounting are in the [source receipt](../sources/RECOVERY_2026-09-28.md). |
| F04 | Repointed 392 local-link occurrences in 66 derived files to existing canonical files, including the Stone-method, validation and source-supplement targets. Recovered the complete Callins PDF/text at the already-cited path. Added the single [external-preparation note](../EXTERNAL_REFERENCES.md); briefs and foundation remain unchanged. | Artifact paths fixed; generic splitter integration remains an operator tooling decision, described below. |
| F05 | Moved whole entries and chronology-table rows in output and Render Inputs for chunks 1, 2, 3, 4, 6, 7 and 8. All 17 listed groups now follow inventory order. Chunk 5 is unchanged. | Fixed. |
| F06 | Chunk 3–5 Run-control notes now accurately distinguish authorization to use current content from byte identity. Standards and Tests and Composition match b83e0fd; Holdings and Standing State do not. | Fixed. |
| F07 | Regenerated the 96-row ledger with `tools/rebuild_ledger.py`, substituting only its history callback with read-only Git-object traversal. Every first-record field now identifies the actual first main-line integration commit and agrees with Appendix E. | Fixed; no Git executable was called. |
| F08 | Replaced the nonexistent load-manifest/inherited-law instruction with the four current workspace projections and relevant entering-law slices, respecting stage-specific access. | Fixed. |
| F09 | No external-access finding was rechecked or resolved. | Intentionally left for the operator, as directed. |

## Record correction and preservation

[Beecham/Jones version 1.1](../records/Beecham_and_Jones_v_United_States_merits_1994-05-16.md) identifies both corrections and the superseded Record at `fb57000d774520e983932c9c73ec33fedd2110df`. That object was read and compared with the starting Record; its text matches under newline normalization. Existing repository history preserves the earlier text. The correction itself remains uncommitted for the operator. Its vote, reasoning, topology and remedy were not re-adjudicated.

Targeted preservation checks against task-opening byte snapshots established that the other 95 Record files, every approved brief, all foundation/state/tool files, and the existing Audit were unchanged. All 94 non-Beecham public event blocks remain byte-identical, including the eleven other entries in chunk 4. Render Input event bodies likewise retain their bytes except for the authorized Beecham corrections; wrapper separators follow the relocated entries. Chronology rows were relocated as whole rows. Removing the one new entry from either candidate restores that candidate's starting bytes.

The same-day dependencies retained are Day before Sassower (1→2), McDermott before Boca Grande (36→37), Landgraf before Rivers (39→40), Staples before Posters ’N’ Things (50→54), and Holder before De Grandy (91→92). Event dates never cross a day boundary. Each Render Input remains a copy of its Record's Public Projection under the builder's newline/outer-whitespace convention.

## Reproduction limits of the unchanged generic tools

`tools/split_chunk.py` copies brief-relative link destinations literally into a sibling directory. Its raw `--check` therefore considers the eight corrected `_STONE.md` files stale solely because their Stone-method links now point to `../briefs/OT_1993_STONE_METHOD.md`. All Stone words, section text and external preparation references are preserved. Changing the approved briefs or repository-wide tools was outside the authorized write scope.

The term-local [rebase_split_links.py](../runtime/rebase_split_links.py) uses the existing splitter's parsing functions and applies exactly that one link-destination rebase. For example, `python -B terms/OT1993/runtime/rebase_split_links.py 4 --check` verifies chunk 4; `--write` regenerates its three normal split files from the approved brief with the correction. All 24 normal split files matched this derivation in targeted checks. It does not override the generic checker or claim that its literal-byte test passes. The operator must account for this documented relocation when running the later Audit, or separately authorize a repository-wide splitter update.

`tools/build_render_input.py` still sorts same-day events by caption. A future regeneration with that unmodified generic tool must reapply `case-list.md` inventory-number tie order to whole event blocks; otherwise it reintroduces F05. No public render content should be regenerated merely to move entries.

The ledger's history provider traversed the actual HEAD (`31f9d6df6e3a64709b55f16f4b3940d55e9ac4e0`) and its first-parent trees using read-only loose/packed object access. It recorded when each existing Record first appeared on that integration history. Records integrated in the same commit are ordered by filename because history supplies no finer order. First-integration hashes do not certify that current correction bytes have been committed.

## Targeted receipts

Ignored scratch under `tmp/ot1993_fixes/` retains the initial hashes and Markdown byte copies, exact link-change map, same-day movement receipt, 96-record history map, source-download receipts, correction scripts, and targeted `verification.json`. These checks establish the changes described here; they do not substitute for the operator's independent Audit or certify the remaining legal substance. The original pass-note counts and hashes remain historical, with dated correction follow-ups rather than silent retrospective rewrites.
