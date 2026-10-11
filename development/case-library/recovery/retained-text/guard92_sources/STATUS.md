# Case-library development status

**Current state: full OT1991 and OT1992 catalogues. Production integration: disabled.**

Updated October 3, 2026. This is clerical source/identity review, not a Court audit or new adjudication.

| Term | Record files at observed baseline | Court-event Records indexed | Case/matter entries |
|---|---:|---:|---:|
| OT1991 | 126 | 125 | 124 |
| OT1992 | 126 | 123 | 123 |
| OT1993 | 96 | 0 | 0 |
| OT1994 | 101 | 0 | 0 |
| OT1995 | 36 | 0 | 0 |
| OT1996 | 0 | 0 | 0 |

The source baseline remains `1ded4b1cae6c8d1634365f0ef45f43270d4a88f4`: 485 Record files and 230 PDFs observed under `terms/`. These are file counts, not unique cases or verified packets. Exact consumed-source hashes are saved with each catalogue. Global caught-up status remains unset.

## Completed coverage

- [OT1991](catalogues/OT1991/README.md): 124 case entries, 125 Court events across 14 chunks, 375 recorded historical-source pointers. Coleman has two events under one identity; the Thomas institutional source accounts for the remaining Record. All earlier identity/source qualifications remain visible.
- [OT1992](catalogues/OT1992/README.md): 123 entries/events across 11 chunks, 401 recorded historical documents (397 URL pointers, 393 distinct URLs, four location gaps). Two statutory admissions and White's retirement account for the other three Records. There is no supplemental Court event.
- The [original 24-matter pilot](pilot/OT1991-chunks-1-3/README.md) remains independently usable and overlaps OT1991; it is not counted again in the totals.

Together the full-term catalogues contain 247 distinct selected case IDs and 248 Court-event Records. No PDF or remote source was newly downloaded or verified. OT1992's independent audit reconciles all inventory, Record, ledger and presentation mappings, with 1,279 exact quotations and 155 source hashes.

The case-entry schema remains draft version 1. OT1991 uses selection version 3 with version 2 retained for history; OT1992 uses version 4 for explicit term scope and repeated-heading locators. The pilot's version-1 manifests remain unchanged. Normal Open, Run, Render and Close remain independent of this development work.

## Validation

All **116 development tests passed** against the final code: the existing 105 plus 11 OT1992 tests. They cover strict input/source checks, event identity, stale-source detection, view consistency, staged publication, interrupted-build reuse, rollback, writer contention and non-destructive recovery. The new tests add full OT1992 coverage, cross-term rejection, separate Smith identities, original dockets, correction nonduplication and repeated-section binding. Mutations use temporary repositories or synthetic fixtures.

All three catalogue profiles pass command-line validation. OT1992 repeated build reuses its active snapshot. Chromium/Playwright checked OT1992's 123 entries and eleven filters, the two Smith results, companion search, twelve repeated-section links, source gaps and the no-results state. The OT1991 browser checks also passed after the shared-tool refresh. Local links resolve: OT1992 616 HTML / 742 Markdown, OT1991 625 / 750, retained pilot 121 / 146. Earlier OT1991 version-2/version-3 and pilot snapshots remain structurally readable during recovery.

All 1,216 prior snapshot files and all four earlier mapping manifests were preserved byte-for-byte. All 205 OT1992 source files and the 163 previously audited OT1991 term sources remain unchanged. Shared-tool changes required fresh older-profile snapshots, without changing their reviewed mappings. See [SAFEGUARDS.md](SAFEGUARDS.md) for tested behavior and limits.

## Qualifications and remaining work

- Coverage is clerical; remote packet completeness, legal force and later treatment remain unaudited. Empty treatment lists establish no absence.
- Full Record links expose mixed public/internal material. Stage-specific retrieval remains unimplemented; these catalogues are not authorized Court-stage inputs.
- OT1992's old workspace count of 124, Coleman withdrawal and Martin continuity reconciliation remain explicit source history. Demos, Moreau and Delo corrections remain single dated events; presentation order is not an inferred legal sequence.
- Dobbs, Herrera, Graham and Delo v. Blair have recorded lower-court documents without recorded locations. Historical date/source qualifications and later-dated material remain visible.
- OT1991 retains its qualified Harris/Alvarez-Machain attribution and unknown historical dates; no authoritative source was edited to remove disagreements.

Next: backfill OT1993–OT1994, then catch up to completed OT1995/OT1996 artifacts in separate development tasks. Review research gaps, explicit treatment links, chronology and restricted-stage retrieval before proposing integration. Catch-up never activates the library automatically; a readiness review and the user's later authorization are still required.

Changes remain local, uncommitted and unpushed. Update this status and `progress.json` together after later development work.
