# OT2003 Opening Validation

**Result:** Open. No conflict or missing inventory item was identified.

The four coordinated projections are populated: [manifest](../workspace/manifest.md), [ledger](../workspace/ledger.md), [continuity](../workspace/continuity.md), and [neutral projection](../workspace/neutral-projection.md). No current-term adjudication or source admission was made.

## Baseline

All three tracker headers identify OT2002 as the last completed term and June 30, 2003 as the processed-through date after 185 completed events, edition November 14, 2026. The legal baseline in the case index agrees. The 23-volume Holdings index is complete, and `python -B tools/holdings_volumes.py check` passes. The current Standing State supplies the roster, allotments, referral practice, five carried matters and 38 scheduled lower-court additions. All nine seats are occupied; no vacancy or oath-date condition applies.

The latest effective event or same-day group from each term OT1991–OT2002 was checked from Record opening metadata and dated natural keys and is retained in the continuity note. OT2002 ends with six events on June 30, 2003; no order among them is invented. The Owens documentation limitation remains a limitation for any later dependent use.

## Inventory and neutral scheduling

- Direct row-by-row comparison passes for all 119 rows: number, presentation order, chunk, caption, docket or citation, event date, exact event type, category and area of law.
- Chunk counts are 7, 16, 16, 16, 16, 16, 16 and 16. All eight `split_chunk.py --parse-only` checks pass. Runtime handoffs were not generated; they are due at Run.
- All 119 neutral case names and event dates match. Neutral scheduling stages and Participation Matter values were copied mechanically; no private position or comparator was copied.
- Event types remain exactly 117 `Merits decision`, one `Merits decision in original proceeding` for Virginia v. Maryland and one `Merits decision on reargument` for Demore v. Kim. These labels supply no form or result.
- All 38 addition-marker captions match Standing State's scheduled lower-court entries. The marker is excluded from the caption. These entries are not extra carryovers.
- Demore, No. 01-1491, is matched once to inventory row 1 on October 14, 2003, the first scheduled event. The four original actions appear once each in a separate undated carryover table, with their Standing State stages, outside the 119-event count.
- The final scheduled event is Roeder on June 30, 2004. Presentation order does not change legal chronology. Every row identifies a pre-event-date entering-law baseline. All shared-date groups retain the common pre-date baseline for uncoordinated matters, including December 15, 2003 across chunks 2–3 and June 21, 2004 across chunks 7–8.
- All neutral participation fields report no case-specific nonparticipation. Any later historical nonparticipation report remains a Run verification flag unless established; participation is checked at argument or submission and at decision.

## Method and boundaries

The scratch-only adapter `tmp/ot2003_open_adapter.py` supplied the existing opener with the parsed rows in presentation order, then populated all four workspace projections. The original opener, manifest rebuilder and general coverage parser were not changed. Direct comparison supplies the coverage evidence because the supplied index layout is outside those parsers' supported formats; no generic coverage success is claimed.

Protected-input byte checks passed for 55 files under the explicitly scoped tracker, infrastructure, tool and brief inputs and the case index. Workspace relative links resolve. No current-term Record, Render Input or output was created. The only durable task outputs are the four workspace files and this validation note; helper scripts and their result are under `tmp/`.

The opening projection contains the published baseline and neutral scheduling information only. Event-specific legal research, entering-law slices, participation findings and isolated Run handoffs remain future work under their own task boundaries.

Independent review confirmed all 119 mapped rows, the 38 unique additions, the single Demore entry and the four unscheduled carryovers. The resulting projections also preserve Demore's continuing judgment below and bond release and the complete Kansas v. Nebraska conditional-dismissal scope from the prior-term close dossier.
