# OT1998 chunk 7 deterministic-control preparation

No Git command was run. No Git metadata was read. The locked top-level directory was not read, listed, searched, or modified. This support context did not open the chunk 7 brief or its Stone/comparator runtime files. Writes were confined to new files in this audit directory. No Record or workspace projection was edited.

## Assignment inputs

[The assignment baseline](OT_1998CHUNK7_ASSIGNMENT_BASELINE.md), [bounded exact excerpts](OT_1998CHUNK7_ASSIGNMENT_EXCERPTS.md), and [source-digest receipt](OT_1998CHUNK7_ASSIGNMENT_BASELINE.json) were generated from the current 75 Records before April 13, 1999. There are 65 counted signed leads and 10 exclusions. Stone-Zsela, Stevens, Scalia, Kennedy, Souter, Thomas, and Ginsburg have seven each; O'Connor and Breyer have eight each. Barnes, April 7, 1999, by Breyer, is the last counted event. All 75 source digests and every baseline link/anchor passed a fresh read-only verification. Counts agree with a separate fresh run of the existing chunk 6 recount tool; no earlier reported tally supplied either recount.

This is a baseline, not a substitute for the fresh preceding-opinion-table count Engine section 8 requires before every assignment. Form and proposition support are fixed before author selection. Eligibility and fit remain substantive assembly decisions.

## Git-free commands

The new adapter runs the existing checker's non-Git checks unchanged, executes the two Python helpers in-process, blocks every subprocess, and prohibits access to the locked directory and Git metadata. It explicitly reports commit-reference existence as deferred. The ledger command preserves existing local order and first-record cells, appends new Records in effective-date/case-name order, and does not claim Git commitment order or verified commitment status.

```powershell
python -B terms/OT1998/audit/ot1998_chunk7_no_git.py ledger
python -B terms/OT1998/audit/ot1998_chunk7_no_git.py check
```

The adapter's command-line load/help check passed. Full `check` was reserved to root control because the original checker mechanically reads all available briefs and runtime sections, including chunk 7's excluded sections. The ledger command was not executed during this support task. Do not run raw `tools/check_term.py` or `tools/rebuild_ledger.py` under the prohibition: both invoke Git.

`tools/rebuild_manifest.py`, `tools/build_render_input.py`, `tools/split_chunk.py`, and `tools/holdings_volumes.py check` contain no Git invocation. The checker covers Holdings synchronization, runtime freshness/parseability, workspace presence, inventory coverage, fixed Record interface, exact eleven public blocks and ordering, Record-to-Render-Input identity/coverage, selected public-voice leaks, the Standing State publication-link restriction, and close-candidate cleanup. It does not perform a full legal, vote/join, link/anchor, source, or assignment audit; those still need separate validation. Commit existence and Git commitment order remain unverified.

## Germany original-leave preservation

The general manifest rebuilder matches Germany's existing completed component Record and would otherwise mark the entire original-leave matter completed. The prior Run supplied this exact explicit pending flag:

```powershell
python -B tools/rebuild_manifest.py OT1998 --stopped 'Federal Republic of Germany, et al. v. United States, et al.=Original leave remains under consideration; a supported dated further action is required. No return date or terminal disposition is established.'
```

Its integrator then restored the original pending row exactly. Chunk 7 integration must likewise preserve the existing row, including its completed-component link and legal status `Open; original leave remains under consideration`; the temporary command-line `Stopped:` label is an accounting guard, not a new adjudication or an original-leave disposition. Pass any other actually stopped/carried matters explicitly. No pending-row change was made here.

The current row is:

```text
| 1999-03-03 | OT_1998CHUNK5 | Federal Republic of Germany, et al. v. United States, et al. | 127, Original; A-736 | ORIGINAL | Original leave motion and emergency injunction | Open; original leave remains under consideration | Printing dispensation and both present restraint requests resolved; original leave pending. No return date or later disposition established. | 1999-03-03; common pre-group law | Supplied reported date; prospective task only | The original leave request requires a supported dated further action. No execution, mootness, deadline or terminal disposition is inferred. | federal_republic_of_germany_original_leave_and_interim_order_1999-03-03.md |
```

Generate chunk 7 Render Input only after its Records are complete, with explicit Record paths (and `--stopped` descriptions for actual stopped matters) supplied to the existing `tools/build_render_input.py`. That generator copies bounded Public Projections without authoring them. Render remains a separate task.
