# Chunk 5 tooling preflight

The current repository checker completed before new chunk-5 Records with zero warnings through tmp/ot1997_no_git_tools.py. The adapter executes tools/check_term.py with only its Git-object-existence predicate deferred, blocks every Git/external subprocess, and allows the reviewed read-only Holdings and split checks. One existing referenced hash requires operator Git verification. The first adapter invocation stopped before running a dependency because Windows supplies the process audit command line as a string; the adapter was corrected and the check then completed.

The ledger adapter executes tools/rebuild_ledger.py with existing ledger order/status retained and new Record order derived from dated durable files. No Git command has been issued. New decision Records and stage freezes are durable files for operator review; repository verification and commits remain with the operator.

All permitted writes are under terms/OT1997/ and tmp/. The protected top-level personal directory is excluded from all reads, listings and searches. Final chunk validation remains required after assembly.
