# Recovered library files from guard92_snapshots conversation

Recovered on October 11, 2026, into this quarantine directory only. These files
were transcribed from complete tool outputs or complete patches retained in
this agent's earlier conversation. No missing implementation was invented, and
no active `development/case-library/` directory was created or edited.

## Complete files retained

| Original relative path | Source and vintage |
|---|---|
| `development/case-library/schemas/case.schema.json` | Complete JSON schema printed by a read-only tool during the October 3, 2026 OT1992 safeguards task; draft schema version 1. |
| `development/case-library/tests/test_snapshot.py` | Complete file printed by a read-only tool at the beginning of that safeguards task; eight existing snapshot tests. |
| `development/case-library/tests/test_ot1992.py` | Complete file printed by a read-only tool at the beginning of that safeguards task; eleven existing OT1992 tests. |
| `development/case-library/tests/test_live_snapshot_guards.py` | Complete file from this agent's successful creation patch during that safeguards task; nine new live-profile tests. |

`development/case-library/tools/pilot.py.guard92.patch` preserves the exact
patch this agent applied to `pilot.py` in that task. It is an `apply_patch`
format patch with its original absolute target path, not a complete Python
file. It must not be applied blindly to an unrelated or differently versioned
file. It adds live-entry, provenance, observation, and cross-term validation
checks to an existing implementation.

## Completeness and verification limits

- The complete `pilot.py`, `term_catalogue.py`, `pilot_views.py`, `pilot_inputs.py`,
  `source_checks.py`, input-selection schemas, operator manifests and generated
  catalogue snapshots are not recoverable from this agent's retained context.
  Partial printed portions of tools were not presented as complete files.
- Other agents may retain additional files or later versions. These recovered
  versions are not asserted to be the final lost-workspace versions.
- The earlier task's nine new tests passed in 9.204 seconds, and eleven then
  existing snapshots passed structural validation with `check_sources=False`.
  Those are historical results, not a test of this incomplete recovery.
- Original source-file hashes were not retained for these complete files.
  The files were transcribed from visible conversation text; no claim of an
  independently proven byte-for-byte match to the lost filesystem is made.
- Syntax-only checks may be performed on this recovered subset. The test suite
  cannot run from this subset because its implementation, fixture module and
  reviewed catalogue manifests are missing.

Production integration remains disabled. Recovery does not authorize changes
to Court records or the adjudication workflow.
