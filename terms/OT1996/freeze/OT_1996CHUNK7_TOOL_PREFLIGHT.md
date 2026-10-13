# OT1996 chunk 7 tooling preflight

This is an internal tooling control, not adjudicative authority. The task's express constraints prohibit every Git command, access to the repository's top-level private Stone directory, and writes outside `terms/OT1996/` and `tmp/`. Governing infrastructure, approved briefs, term-opening state, and prior adjudications remain unchanged.

## Reviewed workflow and tools

AGENTS.md and Engine §§2–3, 8, 14–15 were reviewed for durable files, staged handoffs, ledger order, signed-opinion counting, and truthful validation status. A durable file handoff is not represented as a Git commit. Unperformed Git checks remain unverified.

| Tool | Finding | Permitted task execution |
|---|---|---|
| `tools/check_term.py` | Direct Git `cat-file` predicate in commit-reference loop; also invokes two reviewed Python checks | Do not execute directly; use the task-local adapter below |
| `tools/rebuild_ledger.py` | Direct per-record Git `log` invocation; would infer commitment order from it | Do not execute its main function; use the bounded append helper below |
| `tools/rebuild_manifest.py` | Standard-library only; no subprocess; writes only the chosen term manifest under ordinary OT1996 invocation | `python -B tools/rebuild_manifest.py OT1996`, adding explicit stopped/carried flags when required |
| `tools/build_render_input.py` | Standard-library only; no subprocess; writes the specified output from Record Public Projections | Use the chunk 7 output path and the exact completed chunk 7 Record list |
| `tools/holdings_volumes.py check` | Reads named state volumes and compatibility file; no writes in check mode; no subprocess | Allowed only in `check` mode; never `split` or `build` during this Run |
| `tools/split_chunk.py --check` | Reads the approved brief and corresponding three runtime splits, compares their full generated text; no writes in check mode; no subprocess | Allowed as the checker's reviewed helper; normal export writes only the explicit chunk 7 runtime files |

The tools have no local module dependencies beyond these reviewed helper invocations; remaining imports are Python standard library. `rg` is unavailable, so file searches used bounded PowerShell alternatives. No repository-root recursive search was used.

## No-Git checker

Command: `python -B tmp/chunk7_check_nogit.py`.

The adapter verifies SHA-256 identities of the reviewed checker and its two helper scripts. It executes an in-memory copy of the checker with the Git-reference loop omitted, prints the exact skipped check, and changes the final status to “non-Git checks only; Git provenance UNVERIFIED.” It never returns a fabricated successful Git predicate. Its subprocess allowlist permits only the reviewed read-only Holdings and split checks, adds `-B`, and rejects other commands. Original governing tools are untouched. Non-Git errors retain the checker's nonzero exit status.

`python -B tmp/chunk7_check_nogit.py --self-check` passed. This validates adapter source/hash expectations and compilation only. The full term check was not run by the tooling context and is not certified here.

## No-Git ledger update

Command form: `python -B tmp/chunk7_rebuild_ledger_nogit.py --append RECORD_FILENAME --append NEXT_RECORD_FILENAME`.

Supply every new Record in actual durable write order. Use `--dry-run` first. The helper preserves existing ledger rows and first-record identifiers byte-for-byte, appends each explicitly supplied new Record with “Git verification deferred,” and replaces only the ledger's introductory explanation. It refuses duplicate, already indexed, missing, or unlisted Records, malformed existing rows, an unexpected footer, and concurrent ledger changes. It uses only the original tool's fixed-label parser after checking that tool's SHA-256 identity; it never invokes the original main function or Git predicate. It does not invent Git order or first-record commit identifiers.

`python -B tmp/chunk7_rebuild_ledger_nogit.py --self-check` passed. No ledger update was performed by this preflight.

## Preservation baseline

`tmp/chunk7_preservation_baseline.json` contains SHA-256 hashes for 1,469 pre-existing OT1996 files captured before chunk 7 assembly. The traversal root was explicitly `terms/OT1996/`. Case-insensitive chunk 7 paths and the four mutable workspace projections were excluded; approved earlier briefs, existing Records, prior Render Inputs, outputs, freezes, and other existing term files were included. Hashing does not expose their substantive contents to the tooling context.

Command: `python -B tmp/chunk7_preservation.py check`.

The check passed after creation of the helpers and assignment-source handoff: all 1,469 protected files remained byte-identical. The baseline refuses overwrite. Re-run at final integration to verify preservation across the whole Run.

## Assignment evidence and recount

`freeze/OT_1996CHUNK7_ASSIGNMENT_SOURCES.md` copies case/date identifiers, public Opinion Topology blocks, and bounded assignment paragraphs from all 73 current-term Records present at preflight. Combined reconciliation/assignment sections were narrowed to actual assignment paragraphs; adjacent reconciliation and compatibility discussion was excluded. No current chunk 7 brief, Stone supplement, comparator, or neutral text was substantively supplied to this tooling context.

Command form: `python -B tmp/chunk7_assignment_recount.py --event-date YYYY-MM-DD --case-name 'Case caption' --output tmp/RECEIPT.json`.

The recount parses delivering authors freshly from actual public topology. It deduplicates multiple part rows belonging to the same signed lead and Justice. It does not use historical assignment tallies. The helper records 13 explicit procedural/source exclusions and treats the 60 other reviewed baseline Records as one signed plenary lead each, including argued LAVAS and the signed Lynce threshold opinion. A newly written Record relevant before the target requires explicit `--include FILENAME` for one signed plenary lead or `--exclude FILENAME=REASON`. A multi-opinion event requires a reviewed extension, not the one-lead flag.

Same-day ordering is mandatory: before Kadic and Metropolitan on April 21, 1997, Blessing counts and New Mexico does not. New Mexico enters counts for later alphabetical same-day events and later dates. Existing New Mexico authorship and its prior assignment statement remain unchanged. The target is never counted as its own predecessor. Counts are recomputed before each new assignment after earlier newly written Records are available.

The pre-Kadic receipt, `tmp/chunk7_recount_before_kadic.json`, counted 59 leads and produced Stone-Zsela 6, Stevens 7, O'Connor 9, Scalia 6, Kennedy 6, Souter 8, Thomas 5, Ginsburg 6, Breyer 6. Last counted: Blessing, April 21, 1997. New Mexico was explicitly excluded by same-day order. This is a clerical census, not a choice of eligible author or coalition.

## Remaining integration work

The operator must perform the actual non-Git term check after assembly, rebuild the ledger with the exact new-Record write order, rebuild the manifest with any exact blockers, update continuity and neutral projection, generate the Render Input from the completed Records, and rerun protected-file preservation. Git object existence, Git history order, Git commitment, and any checks not actually performed remain unverified. This preflight claims no completion of those future steps and creates no public render.
