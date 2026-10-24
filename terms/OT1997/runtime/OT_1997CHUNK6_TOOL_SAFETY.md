# OT1997 chunk 6 restricted tool invocation

Inspected tools: check_term.py, split_chunk.py, build_entering_law.py, build_render_input.py, rebuild_ledger.py, rebuild_manifest.py and holdings_volumes.py. No repository tool was altered. No Git command was run and the top-level locked directory was not accessed.

## Safe ordinary invocations

Use `python -B` and set `PYTHONDONTWRITEBYTECODE=1` for inherited Python subprocesses. These tools import only Python standard-library modules; this avoids local bytecode writes if their imports later change.

- `split_chunk.py`: its ordinary mode writes the three split files to the brief's term runtime directory, or the explicit `--outdir`; both `--check` and `--parse-only` write nothing. Set or verify the output directory remains within terms/OT1997.
- `build_entering_law.py`: reads explicit state holdings volumes and the two named state registers; writes only its explicit output. It does not itself include current-term Record deltas, so any needed delta remains a separately script-copied task.
- `build_render_input.py`: reads only supplied Record paths, and writes only the named output. All stopped matters must be passed explicitly. It expects at least one completed Record.
- `rebuild_manifest.py OT1997`: reads the case list, current-term Records and existing manifest; writes only the current-term workspace manifest. Pass stopped/carried matters explicitly.
- `holdings_volumes.py check`: read-only. Do not use its `split` or `build` modes under the current write restriction because those write state/.

No inspected Run tool accesses the top-level locked directory. The split tool's variable and output suffix for the approved position refer to the authorized runtime handoff, not that directory.

## Git-dependent tools

Unmodified `check_term.py OT1997` invokes Git through `git_object_exists` for every apparent commit reference in records/ and close/. Its remaining checks are read-only; its subprocesses call `holdings_volumes.py check` and `split_chunk.py --check` or `--parse-only`.

The ready-to-run wrapper `tmp/run_ot1997_checks_without_git.py` loads the unchanged check tool in memory, replaces only that Git callback, and reports the skipped provenance check before and after the structural checks. Invoke `python -B tmp/run_ot1997_checks_without_git.py`. Treat its result as structural validation with commit-existence verification skipped, never as verified Git provenance. The wrapper is not yet executed by the tooling-support agent.

Unmodified `rebuild_ledger.py OT1997` invokes `git log` once per Record. Do not call it directly. A compliant integration can load that unchanged tool in memory and replace `git_added` with a function that reads the existing ledger's saved row order and First-record commit value, returns those values for existing Records, and assigns new Records a later deterministic order and an explicit `uncommitted; Git disabled by user` marker. Run its unchanged `main`, then replace the generated introductory sentence's Git-order assertion with a truthful statement that existing order and commit metadata were preserved without revalidation and new rows were appended. Alternatively, rebuild the same columns directly while preserving that metadata. Either choice must explicitly record that new Git commit chronology could not be derived and no commit was made. This is a user-imposed provenance limitation, not a judicial blocker.

The allowed helper and all generated results stay within tmp/ or terms/OT1997/. The root operator remains responsible for public-projection validation, physical context separation and the final assembly's chronological recount after every new signed lead.
