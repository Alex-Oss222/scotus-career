# OT1997 chunk 8 — completion and validation receipt

**Result:** All twelve scheduled matters are complete through May 21, 1998. No matter is stopped and no chunk-specific workflow blocker remains. The twelve Canonical Decision Records and generated Render Input are ready for operator verification and repository commit. No Git command was run; no repository commit is claimed.

## Authoritative outputs and current state

- [Release order and Record digests](OT_1997CHUNK8_RECORD_ORDER.json): twelve Records, released in effective-date order and alphabetical case order within independent same-day groups. Released bytes were rechecked against their recorded SHA-256 digests.
- [Independent assembly audit](OT_1997CHUNK8_ASSEMBLY_AUDIT.md): all twelve Records pass; no unresolved substantive discrepancy. It reviews Stone's actual positions, frozen non-Stone grounds, votes, partial joins, remedies, source limits, and assignments.
- [Generated Render Input](../render-inputs/OT_1997CHUNK8.md): twelve events, May 7–21, with the eleven Public Projection blocks copied from each Record. No public render was authored in this Run.
- [Manifest](../workspace/manifest.md): 97 completed scheduled matters and 63 open, out of 160. The next scheduled matter is Calderon v. Ashmus, May 26, 1998, chunk 9.
- [Ledger](../workspace/ledger.md): 100 Records, comprising 99 Court actions and one admitted source. The five opening carryovers and separately pending Brown, Arteaga, Glendora and Breard stages remain at their recorded stages.
- [Continuity](../workspace/continuity.md) and [neutral projection](../workspace/neutral-projection.md): cumulative public-law projections through this chunk, preserving earlier public entries and adding mechanically copied new Public Projections. No private positions or internal reconciliation supply public law.

## Stage separation and source limits

Neutral modeling, historical reconciliation and assembly used separate scoped contexts. The original frozen handoffs remain intact. Normal consolidated COMMITMENTS and RECONCILED handoffs are mechanical collections of the separately frozen materials, not new decisions; their runtime copies are identical. All same-named chunk-8 freeze/runtime pairs present were compared without a mismatch. The approved brief and the base runtime split remain unchanged and fresh.

Ohio required isolation recovery. The initial neutral module exposed controlled-position fields and was stopped without an operative commitment. A subsequent reviewer encountered a historical-result banner while retrieving the lower opinion and also stopped without an operative commitment. A fresh clean context then used a mechanically sanitized packet and complete lower-opinion text; its scoped pleading/preservation refresh preceded final reconciliation. The operative Ohio commitments therefore come from that clean work, not either exposed review. The [control receipt](OT_1997CHUNK8_CONTROL_EXPOSURE.md), [clean preflight](OT_1997CHUNK8_OHIO_PREFLIGHT.md), [scope refresh](OT_1997CHUNK8_OHIO_PREFLIGHT_SCOPE_REFRESH.md), and final reconciliation preserve the boundaries.

Montana's objective correction returned through neutral refresh and historical reconciliation. Reconciliation rejected provisional full-recovery affirmances because the recovered facts were already present in the historical record, while preserving the supported partial-restitution positions. Bousley's narrow preservation supplement likewise passed clean validation and a separate reconciliation receipt before release. Its draft Stevens-join mismatch was repaired before release and independently rechecked. No completed earlier adjudication was altered.

Published recitations are used only at their identified scope. Original pleadings, agreements, reports or transcripts are not claimed recovered where the Records identify their absence. No research gap supplies litigant default, consent, compliance or a merits finding. Each Record states its own event-date cutoff; this is not a claim of an exhaustive external-event sweep.

## Assignment and publication checks

The form and supported grounds were settled before each assignment. Actual current-term opinion tables were recounted sequentially, including earlier Records in this Run. The audit explains the term's actual threshold-event classifications without treating every opinion about procedural law as excluded. All Chief assignments satisfy full-rationale eligibility and the minimum-plus-one pool; Bronx's component assignments are Associate assignments. No prior assignment was reopened.

Final counted signed plenary leads: **77** — Stone-Zsela 8; Stevens 9; O'Connor 9; Scalia 9; Kennedy 9; Souter 8; Thomas 8; Ginsburg 9; Breyer 8. Lewis is a Clerk's dismissal without a judicial vote or authorship credit. Ohio, Stewart and Textron are threshold actions without merits-lead credit.

Every Public Projection contains exactly eleven ordered blocks. The assembly audit checks every judgment and proposition-level coalition, the Bousley remedial difference, Stone's specified partial joins and fallback components, and the substantive separate-writing summaries. All controlling explanations meet the ordinary ceiling; the longest is 270 words. The generated Render Input contains no author placeholder, private approval marker, modern approval date or internal historical-departure annotation.

## Deterministic validation and no-Git boundary

The following completed successfully:

- `python -B tools/split_chunk.py terms/OT1997/briefs/OT_1997CHUNK8.md --check`: twelve matters; split current.
- `python -B tools/holdings_volumes.py check`: canonical volumes and compatibility view synchronized.
- `python -B tools/rebuild_manifest.py OT1997`: twelve completed rows added to the existing manifest; counts and chronology metadata then updated from the Records.
- `python -B tools/build_render_input.py` with the twelve released Records: generated the chunk handoff without separately authoring its substantive content.
- `python -B tmp/chunk8_no_git.py check`: all non-Git portions of `tools/check_term.py` passed, with zero warnings, including inventory/projection checks. Commit-reference existence validation was explicitly skipped.
- Release-date/case order, all present freeze/runtime byte pairs, ledger count, twelve chunk-8 manifest rows, complete ordinary handoff set, and absence of stale current-cursor metadata were checked separately.

The ordinary ledger tool invokes Git, so the bounded `tmp/chunk8_no_git.py ledger` adapter rebuilt it from the canonical labels while preserving existing ledger order and hash strings without verification. New rows explicitly state that they are uncommitted. The check adapter executes the existing checker with only the Git-object check replaced by an explicit skipped notice; its subprocess guard rejects any Git invocation. No hash was represented as a verified repository commit.

A scoped start-to-finish file comparison found no change to the existing foundation, state, tools, brief, Record or output files included in that snapshot. Among pre-existing term files, only the four authorized workspace projections changed. New task files are confined to `terms/OT1997/` and scratch `tmp/`. The locked top-level private directory was not accessed. Git object verification and all committing remain for the operator.
