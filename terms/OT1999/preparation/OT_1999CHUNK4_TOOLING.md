# OT1999 chunk 4 tooling

The existing scratch adapter `tmp/ot1999_chunk3_no_git.py` is reused without changing infrastructure. Its ledger operation executes the stock rebuild logic with Git lookup replaced by preserved existing ledger order/provenance plus an explicit new-Record sequence. Its manifest operation retains the supplied nine-column index and annotated dates. Its check operation executes stock non-Git checks while detecting and expressly deferring commit-reference existence checks. Unexpected subprocesses are blocked before invocation; only the read-only Holdings synchronization and runtime-split checks may run.

`tools/split_chunk.py`, `tools/build_entering_law.py` and `tools/build_render_input.py` are Git-free. Every invocation selects an output within the permitted term or scratch directories. All Python runs disable bytecode writes. The entering-law tool does not itself include effective current-term Records; scoped public-law copies must supply those.

`tmp/ot1999_chunk4_count.py` freshly reads actual lead authors from the public opinion topology of each eligible earlier Record. It never uses numbers from assignment statements. It counts a split lead once per author, excludes per curiam/summary/procedural events, and filters by effective date and alphabetical case name before each assignment. Eligibility, form, pool choice and legal fit remain qualitative assembly decisions.

Baseline check receipt: `../freeze/OT_1999CHUNK4_BASELINE_VALIDATION.txt`. Exit status 0 with zero non-Git warnings; Git verification is deferred, not passed. Existing adjudications, briefs and governing infrastructure were preserved before this Run for a later unchanged-content check.
