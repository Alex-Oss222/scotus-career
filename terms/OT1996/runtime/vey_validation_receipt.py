"""Write the operator receipt from completed check artifacts; no repository commands."""
from pathlib import Path
import hashlib
import json

term = Path(__file__).resolve().parents[1]
freeze = term / 'freeze'
prefix = 'OT_1996CHUNK6_68_RESUMPTION'
checks = json.loads((freeze / (prefix + '_CHECK.json')).read_text(encoding='utf-8'))
integrity = json.loads((freeze / (prefix + '_INTEGRITY.json')).read_text(encoding='utf-8'))
assert checks['non_git_exit_code'] == 0 and not integrity['errors']
assert integrity['chunk6_events'] == 12 and integrity['total_records'] == 73
assert len(integrity['changed_existing_files']) == 8
record = term / 'records/In_re_Vey_financial_leave_1997-04-14.md'
record_hash = hashlib.sha256(record.read_bytes()).hexdigest()
receipt = f'''# In re Vey — resumption and integration validation

**Scope and authorization:** October 13, 2026 completion of OT1996 matter 68, No. 96-8005, in its existing April 14, 1997 chronological slot. No event was added or redated. The [preparation receipt](OT_1996CHUNK6_68_PREPARATION_RECEIPT.md) records the user's Engine §14(5) financial premise as an adopted simulation premise, never recovered history. It establishes only current inability to pay through a compliant Rule 39.1 motion and proper affidavit or declaration. No merits, jurisdictional, exceptional-circumstances, custody, exhaustion or other factual premise follows from it.

**Completed result:** Present financial leave granted, 9–0 internally; new prospective extraordinary-writ fee-and-form condition declined, 9–0 internally. All nine Justices join the per curiam opinion in full. There is no separate writing and no counted signed plenary assignment under Engine §8. No stopped chunk 6 matter remains. The underlying habeas and alternative mandamus/prohibition requests remain pending and unvoted; no writ, certificate ruling, hearing, return, cure deadline, default, existing-restriction rescission or terminal event was supplied. The public projection contains the published joins but no private procedural tally.

## Physically separated stages

The distinct preparation context carried the premise into the [financial neutral handoff](OT_1996CHUNK6_68_FINANCIAL_NEUTRAL.md) and an operator-selected entering-law slice. A fresh modeling context saw the permitted neutral inputs, without comparator or Stone material, and froze [financial commitments](OT_1996CHUNK6_68_FINANCIAL_COMMITMENTS.md). A separate reconciliation context then received those commitments and the historical comparator, without Stone, and froze [financial reconciliation](OT_1996CHUNK6_68_FINANCIAL_RECONCILED.md). Only the subsequent assembly context received Stone's unchanged Section II. The [assembly validation](OT_1996CHUNK6_68_ASSEMBLY_VALIDATION.md) records the compatibility and joins. Stone's approved conditional position applies without fallback.

Only the old financial-input reservation was superseded. The old neutral, commitment and reconciliation freezes remain unchanged; the arguable-current-claim conclusion, declined prospective condition and other unaffected commitments were reused. The original stopped receipt remains as preparation history, with its financial gap resolved by this completion. No old freeze was rewritten to claim knowledge of the later adopted premise.

## Downstream and projection review

The [independent dependency review](OT_1996CHUNK6_68_DEPENDENCY_REVIEW.md) read all four Records dated on or after April 14, including Vey. No later result, reasoning, remedy, participation, procedure or assignment materially depends on a contrary Vey result. Only one stale internal entering-law sentence in each of Chandler, Blessing and Joseph A. was replaced. Raw comparisons confirm those exact replacements and no other byte changes in the three Records; their Public Projections remain unchanged. Every other preexisting Record is unchanged.

Manifest, ledger, continuity and neutral projection now account for 71 Court events and two Admitted Source Records. Vey's public coalition, controlling holdings, precedent treatment, resulting law and procedure are copied from the Record into both relevant projections. The manifest preserves the reserved underlying requests without scheduling another event. All 153 inventory slots retain their dates; all twelve chunk 6 slots are complete. The regenerated [chunk 6 Render Input](../render-inputs/OT_1996CHUNK6.md) includes all twelve Records in effective-date order, with no stopped-matter metadata. All eleven other events retain their Public Projection substance. No public output file was edited.

## Tool and integrity results

- `tools/rebuild_manifest.py OT1996` ran using its original implementation and updated the existing Vey row.
- `tools/rebuild_ledger.py OT1996` ran through the scoped wrapper, using its original main with only the Git lookup replaced by the previous ledger's order and provenance fields. The new Vey Record is marked uncommitted. Existing identifiers were preserved, not independently verified. See the [ledger receipt](OT_1996CHUNK6_68_RESUMPTION_LEDGER_RECEIPT.json).
- `tools/build_render_input.py` regenerated the chunk input from all twelve Records, with no separately authored substantive handoff.
- `tools/check_term.py OT1996` ran through the scoped wrapper. All non-Git checks passed with zero warnings; Git-object checks were explicitly deferred and subprocess Git execution was forbidden. This is not a passed provenance check. See the [checker output](OT_1996CHUNK6_68_RESUMPTION_CHECK.txt) and [machine receipt](OT_1996CHUNK6_68_RESUMPTION_CHECK.json).
- The [integrity comparison](OT_1996CHUNK6_68_RESUMPTION_INTEGRITY.json) checks {integrity['protected_file_count']} baseline files, the exact three note-only replacements, unchanged later Public Projections, seven frozen-handoff hashes, freeze/runtime identity, both copied public coalition declarations, protected brief/output file inventories, 153 manifest events, twelve completed chunk 6 events and twelve unique Render Input sources. It reports no errors. Exactly eight preexisting baseline files changed: three entering-law notes, four workspace files and the chunk 6 Render Input. Exactly one new Record was created, for Vey on April 14.

The initial assembly used one extra heading level in its Public Projection. Root mechanically normalized those headings to the eleven-block tool interface before generation and validation; no substantive prose, holding, join or disposition changed. The assembly-stage check had not enforced that exact heading-level requirement. The dependency reviewer verified the normalization by reversing it and reproducing the original assembly hash. Root subsequently replaced only the internal pending-integration paragraph with completed integration status. Assembly and dependency hashes remain truthful stage hashes. The final integrated Record SHA-256 is `{record_hash}`.

All writes were confined to `terms/OT1996/`. The case list, briefs, outputs, foundation and state were protected; the locked top-level private-position directory was never read, listed, searched or modified. No Git command was run. The user-supplied prior-stop identifier `ef97686` and authorized prospective Engine §8/AGENTS revision identifier `e0abdfd` remain unverified through Git. The identified opening-hash differences for those two authorized infrastructure revisions are expected, not adjudicative conflicts. Repository verification and commitment remain for the operator. There is no unresolved substantive blocker for this Run.
'''
(freeze / (prefix + '_VALIDATION.md')).write_text(receipt, encoding='utf-8')
print('Wrote final validation receipt; integrated Vey Record SHA-256: ' + record_hash)
