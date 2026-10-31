# OT1999 opening validation

**Task:** Open October Term 1999.  
**Validation date:** October 31, 2026.  
**Result:** Opening baseline and four-file workspace validated; no current-term adjudication entered.  
**Source priority:** The current repository trackers govern. Supplied case-index introductory and closing descriptions do not replace them.

## Baseline

The three published trackers share last completed term OT1998, the cutoff June 23, 1999 after 130 completed Court events and one admitted source event, and edition October 29, 2026. Standing State expressly describes the opening of OT1999. The divergence point remains October 7, 1991.

`python -B tools/holdings_volumes.py check` passed: all eighteen doctrinal volumes and the continuous Holdings register are synchronized. Holdings and Standards and Tests match the publication hashes in the OT1998 Term-Close Dossier. Standing State differs from that older publication hash and now expressly includes the OT1999 additions identified in the opening instruction. Its current section 4 is the directed opening source; the old hash is not substituted for it. The roster, allotments and fourteen pending stages were separately reconciled.

The [OT1998 final audit](../../OT1998/close/AUDIT.md) reports no unresolved discrepancy. Its four retained notes are nonblocking. This was a term-opening baseline review, not another close audit. The [continuity note](../workspace/continuity.md) identifies the final completed event or same-day group for each earlier term, OT1991 through OT1998, from the corresponding Term-Close Dossier.

All nine seats and institutional seniority match Court Composition. All thirteen circuit allotments match the August 3, 1994 order. No vacancy or new-oath condition applies, and no additional case-specific nonparticipation is established by the opening setting. Event-specific participation remains for Run validation. The standing referral, signed-explanation and certification practice is carried accurately.

## Inventory and procedure

| Check | Result |
|---|---|
| Supplied scheduled inventory | 104 consecutive rows; no duplicate captions, blank fields or date reversals. |
| Chunk coverage | Chunks 1–8: twelve matters each; chunk 9: eight. |
| Categories | 101 MERITS, one DIRECT APPEAL, two ORIGINAL. |
| Supplemental matters | All 23 grants and Rayphand / Torres, No. 99-475, match Standing State section 4. No grant date, vote or rationale invented. |
| Prior pending matters | All fourteen retained. Alaska is scheduled once as row 104; thirteen others are separately unscheduled. |
| Distinct open matters | 117: 104 scheduled plus thirteen additional pending carryovers. |
| Same-day chronology | Date grouping retained for every scheduled row. Six groups span chunks: January 12, March 6, May 1, May 22, June 12 and June 26, 2000. Common entering-law requirements stated. |
| Current-term completed events | Zero Court events and zero admitted sources; no planned action marked complete. |
| Additional institutional or noncase-law change | None supplied for this opening. |
| Brief structure | All nine briefs pass the splitter's read-only `--parse-only` mode: 104 matters total. No brief substance was exposed to the opening operator by these mechanical checks. |
| Runtime handoffs | Not generated; absence is expected before Run. |
| Neutral boundary | Contains the opening law, Court setting, public docket stages and chronology; excludes private positions and current-matter historical outcomes, commitments, reconciliation and audit substance. |

Historical event descriptions in the control manifest remain planning metadata. They do not import Free's historical division, decide Fiore's proposed certification, enter Alaska's decree or settle any other Court action. The neutral projection omits those historical outcomes. Unscheduled matters remain pending without inferred default, execution, mootness, deadline or terminal event. The two Arteaga submissions and two Paraguay dockets remain distinct.

## Tool compatibility and verification

The direct `python -B tools/open_term.py OT1999` invocation parsed zero rows and stopped before writing. Its accepted format requires a bare ISO date and does not accept the supplied date-basis text plus Position status column. The source case index was preserved byte for byte.

A script copied all 104 saved inventory rows to `tmp/ot1999_open/seed-root/terms/OT1999/case-list.md`, extracting only the ISO date and omitting the approval column for the tool-input copy. `python -B tools/open_term.py OT1999 --root tmp/ot1999_open/seed-root` then generated the required four-file scaffold. The scaffold was copied into the authorized workspace; the original date bases, supplied event descriptions, categories, identifiers and areas of law were restored directly from the saved index, and the Standing State carryovers and completed opening projections were added. No source index, tool or governing file was modified.

The repository checker passed after writing the workspace: `python -B tools/check_term.py OT1999` reported zero warnings. Its inventory regex has the same bare-date limitation, so that pass alone does not establish inventory coverage. An independent structured comparison checked every original row against the manifest's caption, date, chunk, citation or docket, category, event description, date basis and area of law. All 104 matched. The thirteen additional pending rows and single scheduled Alaska entry also passed. Future manifest rebuilding needs a compatible input adapter while the richer source-index format remains in place; no tool revision is authorized by this Open.

All four projection stubs were replaced. Relative links resolve. Protected-file hashes before and after writing match for all fifty checked files: the published state and volumes, case index, nine briefs, governing Markdown files and existing tools. New workspace and audit text contains no repository web URLs or local-machine paths. File operations were confined to the authorized OT1999 workspace and audit directories and ignored scratch. No Git command was run, and the locked top-level directory was not accessed.

Independent read-only reviews checked the baseline and prior-term final events, inventory reconciliation, and the completed workspace's procedural framing and neutral boundary. They found no unresolved opening discrepancy. Operator verification and committing remain separate; no repository commit is claimed.

## Files written and remaining limits

- [Manifest](../workspace/manifest.md): all scheduled items, additional pending matters, stages, dates, dependencies and same-day groups.
- [Ledger](../workspace/ledger.md): empty current-term Record sequence and opening cursor.
- [Continuity](../workspace/continuity.md): governing baseline, Court setting, prior-term final events and current pending procedure.
- [Neutral projection](../workspace/neutral-projection.md): sanitized opening law, public procedure and chronology.
- This validation report.

No identified inventory item is missing and no substantive opening conflict remains. The index's eight unnamed legacy entries lack identifying information and are not additional docket instructions; no case was invented. Its references to calendar-audit, unresolved-items and preserved-source filenames are supplied background descriptions, not opening authorities. The parser limitation is disclosed above and does not prevent this independently validated opening.
