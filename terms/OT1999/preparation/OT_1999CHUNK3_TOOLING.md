# OT1999 chunk 3 tooling under the no-Git instruction

The temporary adapter is `tmp/ot1999_chunk3_no_git.py`. It loads the existing tool implementations without changing `tools/`. No Git command is permitted. Unexpected subprocesses are rejected before invocation; the only permitted subprocesses are the stock checker's read-only `holdings_volumes.py check` and `split_chunk.py --check` or `--parse-only` calls. Python bytecode writes are disabled.

Run the following from the repository root when assembly is ready:

```powershell
python -B tmp/ot1999_chunk3_no_git.py ledger --new-record FIRST_NEW_RECORD.md --new-record SECOND_NEW_RECORD.md
python -B tmp/ot1999_chunk3_no_git.py manifest
python -B tools/build_render_input.py terms/OT1999/render-inputs/OT_1999CHUNK3.md RECORD_PATH_1 RECORD_PATH_2
python -B tmp/ot1999_chunk3_no_git.py check
```

The uppercase filenames and paths above are placeholders. Repeat `--new-record` once for every Record absent from the existing ledger, in actual durable assembly order. Include new admitted-source Records as well as decisions. The adapter refuses to proceed if a new Record is omitted, duplicated, or extra, or an existing ledger Record is missing. Existing ledger order and provenance cells are retained; new provenance cells say `Uncommitted / operator commit pending; Git not queried`. A subsequent ledger rebuild with no new Records needs no `--new-record` arguments. This adapter writes only `terms/OT1999/workspace/ledger.md`; its `check` command is read-only.

Pass each stopped matter explicitly to the `manifest` adapter command with `--stopped "CASE=exact blocker"`, or a carried matter with `--carried "CASE=carry-forward reason"`. Pass stopped identities and blockers to `build_render_input.py` with `--stopped "natural identity: exact blocker"`. Render Input generation needs the complete set of completed chunk 3 Records in its arguments; do not include unrelated current-term Records.

The other inspected tools can run directly with `python -B`: `split_chunk.py` writes only the selected runtime output directory; `build_entering_law.py` writes only its selected output file; the manifest adapter executes the stock `rebuild_manifest.py` with its parser extended for the supplied nine-column index and annotated date cells, writing only the term manifest; and `build_render_input.py` writes only its selected Render Input. Select output paths within `terms/OT1999/` or `tmp/`. The entering-law builder copies selected opening-state material but does not automatically add effective current-term Records; the operator must supply the required current-term authority separately.

## Exactly what is skipped

- The ledger's Git log lookup, Git-derived first-record order, and first-record commit discovery. Durable order comes from the existing ledger plus the explicit new-Record sequence. Existing provenance is retained without reverification.
- The term checker's Git commit-hash existence test. Commit-like references are still detected; the adapter reports the number of unique references whose existence check was skipped. A passing result is expressly limited to non-Git deterministic checks.

No other stock validation is disabled. The adapter does not claim a repository commit or a successful commit-hash audit.

## Checks retained and schema required

The checker retains Holdings volume synchronization; Render Input/brief/output presence; runtime split freshness and unrun-brief parseability; the four workspace files; case-list coverage in the manifest; exact completed-Record coverage in each Render Input; exact Public Projection copying; Record filenames and fixed labels; public block order; public workflow-language screening; the Standing State self-link check; and candidate cleanup after an audit declaring no unresolved discrepancy. Its subprocess checks are read-only.

Every modern Record filename must end in an event component and `YYYY-MM-DD.md`. Its opening twelve lines must contain `**Case and dockets:**`, `**Event and date:**`, `**Result:**`, and `**Version / lineage:**`. The stronger governing rule requires those four exact labels first, each on its own line; the adapter does not weaken that rule. The Event label must supply the effective ISO date for ledger, manifest, and Render Input generation.

The bounded `## Public Projection` must contain these eleven level-two blocks in order: Event; Participation; Public Action; Judgment & Remedy; Opinion Topology; Holdings; Precedent Treatment; Law After Decision; Separate Writings; Procedure After Action; Source Notes. Render Inputs retain generated `source-record` markers and exactly matching projection text. The manifest's completed statuses and any completed-component column determine expected Render Input coverage.

The stock deterministic checker does not substantively verify vote arithmetic, joinder compatibility, legal holdings, historical departures, assignment balance, source adequacy, or freeze integrity. Those remain required stage and substantive checks. A non-Git checker pass is not a substitute for them.

Preparation note: the adapter's baseline `check` command passed with exit status 0 and zero warnings; its output is preserved in `terms/OT1999/freeze/OT_1999CHUNK3_BASELINE_VALIDATION.txt`. No ledger regeneration or Git command was run. No adjudication was changed.

## Manifest parser compatibility

The supplied case index has nine columns and date-basis annotations that the stock parser does not accept. The scratch adapter now exposes a `manifest` command with the previously validated bounded parser extension for that exact form; it runs the stock matching, status and preservation logic without editing the tool or index. Stopped and carried arguments remain explicit. This parsing adjustment changes no case, date, stage or adjudication by itself.
