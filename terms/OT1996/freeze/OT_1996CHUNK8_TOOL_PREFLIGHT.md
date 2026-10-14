# OT1996 chunk 8 tooling and control preflight

No Git command was executed. The protected top-level private directory was not listed, searched, read or changed. All writes in this context were confined to terms/OT1996 and tmp. Approved briefs, governing tools and foundation files were not edited.

## Safe workflow

split_chunk.py and build_entering_law.py have no subprocess dependencies and write only their configured outputs. rebuild_manifest.py writes only the selected term manifest. build_render_input.py writes only its configured output. holdings_volumes.py check is read-only; its build and split modes are not authorized during this Run. Use python -B to suppress bytecode writes.

Do not invoke rebuild_ledger.py or check_term.py directly: their Git operations violate the task instruction. The task-local adapters tmp/chunk8_check_nogit.py and tmp/chunk8_rebuild_ledger_nogit.py leave governing tools untouched. Each verifies reviewed source hashes. The checker removes the Git-only loop in memory, explicitly reports that provenance is UNVERIFIED, and allowlists only reviewed read-only Python dependencies. It never substitutes a fabricated successful Git predicate. The full non-Git term check passed with zero warnings at preflight; this does not verify Git objects or term legal substance.

The ledger adapter preserves every existing ledger row and first-record identifier byte-for-byte. Supply --append RECORD_FILENAME once for each new Record in actual durable write order, and run --dry-run first. New rows are labeled operator-commit-pending. The helper rejects duplicate, omitted, missing or already indexed Records and concurrent ledger edits. The self-check passed; this control context has not changed the ledger.

## Opening input hashes

The receipt OT_1996CHUNK8_OPENING_HASH_CHECK.json compares all 30 saved opening inputs against actual SHA-256 hashes. Twenty-seven match. AGENTS.md and foundation/ENGINE.md differ as expected under the prospective October 13 revision. case-list.md also differs from the opening hash, but its current SHA-256 matches tmp/chunk7_preservation_baseline.json exactly. This is an inherited difference, not a change made in chunk 8. Root verified the twelve current chunk-8 inventory rows against the approved neutral lineup and dates and found no content conflict. No administrative blocker remains from this hash delta; Git lineage was not verified. Current hashes were separately saved as tmp/chunk8_governing_baseline.json for later change detection.

## Approved controlled input

The mechanical split contains exactly one Section II for each of twelve matters. No. 92 explicitly carries the user's October 13, 2026 Version 2 approval and says it replaces the October 11 position in full. The other supplements carry approval language and supplied dispositions, grounds and limits. Event-specific revalidation against entering law remains assembly work. This control context read the Stone supplement and cannot serve as a neutral, modeling or historical-reconciliation context. No Stone substance was forwarded to neutral workers or root.

## Assignment-only handoff

runtime/OT_1996CHUNK8_ASSIGNMENT_BASELINE.md mechanically extracts each prior Record's case and date identifiers, public Opinion Topology block and bounded assignment statements. The receipt OT_1996CHUNK8_ASSIGNMENT_BASELINE_RECEIPT.json hashes the extract and all 86 source Records and checks equal case/date/topology coverage. Three admitted-source Records have no assignment statement. Recount actual delivering authors from topology, never historical assignment tallies, with date and same-day alphabetical ordering. All prior assignments stand.

The reviewed tmp/chunk7_assignment_recount.py is safe and reusable, with explicit --include or --exclude for post-baseline Records. It uses its chunk7 preservation baseline; it cannot simply classify all current Records automatically. Multi-opinion events need a reviewed extension. No recount was performed in this control context.

## Comparator scope

All twelve comparators are present. A historical-only correction and verification limit are saved in OT_1996CHUNK8_COMPARATOR_CONTROL.md for a clean reconciliation context. The approved brief and runtime comparator were not edited. Further full-opinion review remains the reconciliation context's responsibility.
