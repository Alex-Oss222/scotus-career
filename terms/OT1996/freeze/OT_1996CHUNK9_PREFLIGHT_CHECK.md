# OT1996 chunk 9 — initial deterministic check

The task-local no-Git adapter executed `tools/check_term.py`'s non-Git checks against OT1996 before new decisions were assembled. Result: `OK: OT1996; 0 warning(s)`.

The adapter omitted only the commit-object existence loop. Git provenance remains for operator verification; no Git command was executed. The current-task preservation baseline is `tmp/ot1996_c9_opening/preservation.json`, with the four opening workspace copies beside it. No completed adjudication was changed.
