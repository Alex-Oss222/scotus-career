# OT2001 chunk 2 tool safety protocol

Read-only inspection covered the five requested tools and the two child check tools. Governing tools were not modified. No repository command was run. The task adapter is [scratch-only](../../../tmp/ot2001_chunk2_tools.py).

## Execution boundaries

- `rebuild_ledger.py` invokes a repository history command once per Record. Do not execute its main function directly. The adapter imports its fixed-label parser only, preserves each existing first-record provenance cell by Record filename, and marks new entries pending operator verification. It uses effective-date and case-caption order without claiming commitment order.
- `check_term.py` invokes a repository object check for detected commit references. The adapter retains reference detection for a disclosed skipped-reference count, suppresses only that prohibited validation, and installs an execution guard that permits only the two inspected Python check tools. All other subprocesses fail before execution.
- The checker also invokes `holdings_volumes.py check` and `split_chunk.py --check` or `--parse-only`. These modes are read-only and contain no subprocess invocation. The Holdings `split` and `build` modes write outside this task's scope and must not be used.
- The stock manifest parser does not recognize this term's nine-column inventory or its `Event type` header. The adapter supplies the exact inventory parser and header in memory, then uses the existing status-refresh function. An independent comparison verifies all 124 inventory rows and all nine source fields. Stopped and carried arguments retain their ordinary explicit format.
- `build_render_input.py` and `build_entering_law.py` invoke no subprocess and read only explicit input paths or selected state paths. Constrain their output arguments to this term. The entering-law tool copies opening-state selections only: effective current-term authority still requires a separate bounded mechanical public-law extraction under the date barrier.
- There is no root-wide search in the inspected tools. The checker recursively enumerates Markdown under the selected term only and reads named state files. Other glob operations stay within the term's named subdirectories. No inspected tool contacts an external service.
- Use `python -B` when running the adapter. Imports disable bytecode writes. The adapter validates publication text before its own writes and confines those writes to the current term or scratch directory.

## Commands after assembly

Run `python -B tmp/ot2001_chunk2_tools.py ledger`, then `python -B tmp/ot2001_chunk2_tools.py manifest`, supplying any exact stopped or carried reasons. Generate the Render Input with the ordinary tool and explicit current-chunk Record paths. Run `python -B tmp/ot2001_chunk2_tools.py check` after the four workspace projections are coordinated. The checker has not been executed for chunk 2 by this inspection task. A passing result excludes repository-object existence validation and must be reported with that limit.

## Entering status

The manifest contains 124 scheduled inventory rows: 16 completed, 108 open, and none stopped. Chunk 2 consists of rows 17–32, all open, from 2002-01-09 through 2002-02-20. The latest completed event is Chao on 2002-01-09. Kelly and Riley share that date and must use the common baseline immediately before January 9; Chao supplies no entering law or prior published position to them. Its signed lead still counts for the separate assignment-balance inquiry.

The opening validation records a synchronized 2001-06-28 tracker baseline, nine occupied seats, all four populated workspace files, 124 matched inventory entries, and two unscheduled original-action carryovers. Arizona v. California and Kansas v. Colorado remain separately open. No new event is scheduled for either.

Chunk 1 validation reports fourteen counted signed leads across sixteen Records: Stone-Zsela 1; Stevens 1; O'Connor 2; Scalia 2; Kennedy 2; Souter 1; Thomas 2; Ginsburg 2; Breyer 1. This is cross-check information; the mechanically extracted prior opinion tables and assignment statements control the assembly recount.

## Execution result

The Run used these adapters for the ledger and manifest, the original Render Input builder, and the actual term checker with the described object-check exclusion. The final checker passed with zero warnings; two detected object references remain unverified. Caption matching additionally normalizes straight and typographic apostrophes in memory without changing inventory cells. The Windows execution guard validates the structured command first and accepts its exact active serialized representation; it still permits only the two named read-only Python checks. The [final validation receipt](CHUNK2_VALIDATION.md) records complete results.
