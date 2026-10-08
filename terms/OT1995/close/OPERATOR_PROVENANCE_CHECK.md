# OT1995 close — operator provenance check and audit-finding repairs

**Date:** October 7, 2026. **Operator:** the user's Claude Code session, under the user's instruction to resolve audit findings and complete the close. This is a temporary pass note; the Commit pass removes it with the other close pass notes.

## Commit references and lineage (Audit §2, "Commit references and lineage")

`python tools/check_term.py OT1995`, run by the operator with Git available, returns exit 0, no errors, and 85 warnings. Each warning is a hex-like token that is not a commit. All tokens fall into the classes the Audit already identified:

- Internet Archive item fragments: `A40385013`, `A40386012`, `A40385014`.
- Dates in preserved snapshot filenames: `19960621`, `19960624`, `19960625`, `19960626`.
- Supreme Court Library document identifiers: `1000370934`, `1000202729`.
- Statutory PDF path fragments: `ec21103`, `ec20302`.
- UNT `metadc` fragment: `adc30866`.
- vLex document number: `889392159`.
- Technical Advice Memorandum number: `8314011`.
- Reporter filename: `58F3d59`.
- Currency-amount anchor: `40508923`.

Every genuine commit hash cited in OT1995 Records, freezes and workspace lineage notes resolves in repository history. That covers the chunk Run, Render and Correction commits, including 6e9ce8f, 3f8cd91, 9f9df70, cd591c3 and 3815cd9. No lineage claim names a missing commit.

## Repairs made for Audit §3

1. **§3.1 Operative source links.** All 67 catalogued link occurrences in §8 were repointed on their stated lines to the listed working relative targets. The one additional runtime copy of the Settle timing-addendum link was repointed the same way. Only the link target path changed; no text, holding, commitment or provenance statement changed. All 67 working targets were verified to exist.
2. **§3.2 Workspace summaries.**
   - The present-tense source summaries in `workspace/manifest.md`, `workspace/continuity.md` and `workspace/neutral-projection.md` now state ten admitted noncase-law sources and include Utah H.B. 206 (effective April 29) and the chunk 10 Telecommunications Act cable admissions (effective February 8).
   - Each of the three files now carries a header note. It marks dated chunk-progress entries as historical snapshots, whose source counts and "latest admitted source" dates (for example "eight", "April 26") reflect the time they were written, and states the current figures.
   - Enactment and effective dates are not conflated.

No Record, Render Input, render, brief, case-list, candidate substance or `state/` file was changed by these repairs.
