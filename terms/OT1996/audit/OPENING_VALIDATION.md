# OT1996 opening validation

**Result: opening complete after revalidation on October 11, 2026.** Both recorded conflicts are resolved. The opening trackers and all four workspace files are validated, and the 153-item supplied inventory is fully covered. No unresolved opening discrepancy remains.

**Operator boundaries:** No git command; no access to the locked top-level directory. Writes are confined to `terms/OT1996/workspace/`, `terms/OT1996/audit/` and ignored `tmp/` scratch. No state, inventory, brief, other-term or foundation modification. Chunk briefs are expected later and are not an opening blocker.

## Opening baseline

All three opening trackers identify **Last completed October Term: 1995** and **Processed through: July 1, 1996, after all 116 completed OT1995 Court events and ten admitted source events.** Their common publication edition is **October 7, 2026**:

| Opening authority | Edition |
|---|---|
| [Holdings continuous view](../../../state/HOLDINGS.md), synchronized with the [doctrinal volumes](../../../state/holdings/INDEX.md) | October 7, 2026 |
| [Standards and Tests](../../../state/STANDARDS_AND_TESTS.md) | October 7, 2026 |
| [Standing State](../../../state/STANDING_STATE.md) | October 7, 2026 |

The divergence point is October 7, 1991, when Alex-Lamar Stone-Zsela replaces Rehnquist as Chief Justice. [Court Composition](../../../foundation/COURT_COMPOSITION.md) governs membership, seniority and circuit allotments.

## Resolved opening conflicts

1. **Publication synchronization — resolved:** Standing State has been restored to the October 7, 2026 edition. Re-reading all three headers confirms identical `Edition`, `Last completed October Term` and `Processed through` values. The eighteen Holdings volumes and continuous view are synchronized. No tracker was edited by this task.
2. **Prior-term pending docket — resolved:** The user's express instruction of October 11, 2026 removes the twelve matters below from the simulation docket and excludes them from OT1996. This is the user's inventory membership decision; it supplies no Court disposition and requires no OT1995 rewrite.

### Opening docket reconciliation

By the user's express inventory instruction of October 11, 2026, the following twelve matters listed as pending in the OT1995 final sources are removed from the simulation's docket and are not carried into OT1996. The supplied term list controls membership; the opening manifest therefore contains its 153 planned matters, including the 58 granted additions, and no prior-term carryover.

| Matter removed from the simulation docket | Docket |
|---|---|
| Wyoming v. Oklahoma | 112, Original |
| United States v. Louisiana, Alabama and Mississippi | 9, Original |
| Delaware v. New York | 111, Original |
| Nebraska v. Wyoming | 108, Original |
| Kansas v. Colorado | 105, Original |
| Wood v. Bartholomew | 94-1419 |
| Louisiana v. Mississippi | 121, Original |
| Jones v. ABC-TV | 95-7186 |
| United States v. Maine | 35, Original |
| Shieh petition | 95-7587 |
| Shieh petition | 95-7588 |
| Shieh petition | 95-7589 |

Prior-source references: [OT1995 final manifest](../../OT1995/workspace/manifest.md), [final continuity](../../OT1995/workspace/continuity.md), and [Term-Close Dossier, Final manifest, continuity and carry-forward](../../OT1995/close/TERM_CLOSE_DOSSIER.md#final-manifest-continuity-and-carry-forward). Their pending descriptions remain an unchanged account of OT1995; the express opening inventory decision resolves which matters continue in the simulation. The three Shieh petitions are distinct removals.

This is an inventory reconciliation, not a Court disposition or a terminal continuity closure. No terminal action, decision date, vote or holding is attributed to any removed matter. October 11, 2026 identifies the user's instruction, not an in-world Court event. No filing default, deadline or resolution of pending relief is inferred. Completed adjudications, the OT1995 files and the July 1, 1996 chronology cursor remain unchanged. The removed matters supply no OT1996 pending-docket blocker.

Both resolutions are carried in continuity.md and neutral-projection.md. The manifest's 153 event rows remain unchanged and the ledger remains empty. No git provenance verification or commit is claimed; the operator handles those steps.

## Inventory and institutional validation

| Check | Result |
|---|---|
| `python -B tools/holdings_volumes.py check` | PASS, exit 0: all eighteen doctrinal volumes and compatibility view synchronized |
| Common last-completed term and processed-through statement | PASS: OT1995; July 1, 1996, after 116 Court events and ten admitted sources |
| Common edition | PASS: October 7, 2026 in all three trackers |
| Roster and seniority versus Composition | PASS: Chief Stone; Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer; all nine seats occupied |
| Circuit allotments | PASS: all thirteen circuits match August 3, 1994 order |
| Standing practices | Preserved with October 7, 1991 referral and October 2, 1995 signed-explanation/certification terms |
| Inventory shape and numbering | PASS: 153 unique sequential rows, eight populated columns, including Area of law |
| Categories | PASS: 149 MERITS, 3 APPLICATION, 1 ORIGINAL; specific event type governs posture |
| Chunks | PASS: 13, counts 12 / 12 / 11 / 12 / 12 / 12 / 12 / 12 / 11 / 12 / 12 / 12 / 11 |
| Date order and duplicates | PASS: 1996-10-21 through 1997-09-15; no inversion or duplicate event |
| Same-day groups | PASS: 48 dates, 28 multi-matter groups; eleven crossing chunks explicitly retained |
| Sim-granted cases | PASS: all 58 match Standing State §4 captions, docket designations, index references and question-block chunks |
| New inventory coverage | PASS: 153 manifest rows exactly preserve caption, docket, event type, category, chunk and date; zero new planned carryover rows |
| Prior-term carryover reconciliation | PASS: twelve pending matters removed by the user's October 11, 2026 inventory decision; no OT1996 carryover or Court disposition |
| New events and source admissions | Zero; current ledger empty; opening does not advance the July 1, 1996 cursor |
| Brief availability | Expected absence; not a blocker and no brief contents read |

The introductory applications/petition-stage summary in `case-list.md` omits Lords Landing, although its No. 104 row explicitly supplies petition-stage possible GVR. The manifest preserves that row and posture. This is a summary omission, not a missing inventory event. The index's “not yet opened” note now reflects the earlier preparation stage; this audit and the four validated workspace projections establish the completed opening. That administrative note does not change inventory membership or block opening. The protected index was not edited.

The fifty-eight granted cases are represented once, not duplicated as new grant orders. Assigned preparation dates are not treated as Court decisions. Listed historical dates adopt no historical outcome or lineup. No unknown source admission or Court action has been invented to fill the interval after July 1, 1996.

## Prior-term final-event continuity

| Earlier term | Final effective date | Latest completed event or complete same-day group |
|---|---|---|
| OT1991 | 1992-07-17 | [Benten v. Kessler, A-40](../../OT1991/records/Benten_v_Kessler_A-40_application_to_vacate_stay_1992-07-17.md) |
| OT1992 | 1993-07-26 | [DeBoer v. DeBoer, A-64](../../OT1992/records/DeBoer_v_DeBoer_A-64_application_1993-07-26.md) |
| OT1993 | 1994-06-30 | [McFarland v. Scott](../../OT1993/records/McFarland_v_Scott_merits_1994-06-30.md); [Holder v. Hall](../../OT1993/records/Holder_v_Hall_merits_1994-06-30.md); [Johnson v. De Grandy](../../OT1993/records/Johnson_v_De_Grandy_merits_1994-06-30.md); [Madsen v. Women's Health Center](../../OT1993/records/Madsen_v_Womens_Health_Center_Inc_merits_1994-06-30.md); [United Mine Workers v. Bagwell](../../OT1993/records/International_Union_United_Mine_Workers_of_America_v_Bagwell_merits_1994-06-30.md); [Tuilaepa / Proctor v. California](../../OT1993/records/Tuilaepa_v_California_and_Proctor_v_California_merits_1994-06-30.md) |
| OT1994 | 1995-06-29 | [Rosenberger](../../OT1994/records/Rosenberger_v_Rector_and_Visitors_of_the_University_of_Virginia_merits_1995-06-29.md); [Babbitt v. Sweet Home](../../OT1994/records/Babbitt_v_Sweet_Home_Chapter_of_Communities_for_a_Great_Oregon_merits_1995-06-29.md); [Miller and consolidated matters](../../OT1994/records/Miller_and_consolidated_merits_1995-06-29.md); [Pinette](../../OT1994/records/Pinette_merits_1995-06-29.md); [Chabad Lubavitch v. Miller](../../OT1994/records/Chabad_Lubavitch_v_Miller_merits_1995-06-29.md) |
| OT1995 | 1996-07-01 | [United States v. Winstar](../../OT1995/records/United_States_v_Winstar_Corp_merits_1996-07-01.md); [Pennsylvania v. Labron and Kilgore](../../OT1995/records/Pennsylvania_v_Labron_and_Kilgore_summary_review_1996-07-01.md) |

The complete final-day groups are retained. OT1994 records sequence Pinette before Chabad; table order creates no other dependency. The OT1995 July 1 pair shares entering law and closes the carried legal cutoff.

These final events were checked against each term's close dossier and existing Record paths in an independent read-only review. The earlier review identified the pending-docket conflict, now resolved by the express opening inventory decision above. It did not re-adjudicate earlier cases or use Git to verify lineage.

## Scope of legal validation

This opening task checks publication integrity, continuity, institutional setting and inventory completeness. It does not repeat the completed OT1995 substantive close audit or adjudicate any OT1996 question. No material new disagreement between Holdings and Standards was resolved or silently synthesized. Existing law remains at its exact sources. Opening baseline validation is complete within this scope; no legal disagreement has been repaired by inference.

The ten admitted OT1995 source events remain part of the baseline with their own temporal limits. No post-cutoff external research or source admission was undertaken. Later neutral preflight must verify any material intervening law, especially for the first inventory item. Prior published Justice positions are consulted from public renders when implicated; this opening imports no private positions or historical comparator.

## Files written and verification receipt

- [manifest.md](../workspace/manifest.md): completed-opening status and reconciliation link; all 153 planned event rows, date bases, stages, dependencies and cross-chunk same-day groups preserved.
- [ledger.md](../workspace/ledger.md): completed-opening status; zero current-term entries.
- [continuity.md](../workspace/continuity.md): all seven Engine blocks, exact opening sources, prior final events, institutional state and resolved opening conflicts.
- [neutral-projection.md](../workspace/neutral-projection.md): sanitized current law, procedure, chronology and material dependencies; no private or comparator input.
- This audit and [OPENING_INPUT_HASHES.json](OPENING_INPUT_HASHES.json): exact SHA-256 values for thirty explicitly scoped read-only governing/baseline/inventory inputs.

During initial preparation, `python -B tools/open_term.py OT1996` completed successfully and seeded 153 events. Both generated stubs were replaced with substantive projections. This completion task preserves that scaffold and revalidates it rather than reseeding the workspace. A separate validation receipt below records the checks actually completed after writing. No Git validation or commit is claimed.


### Input-hash refresh

The pre-edit hash comparison found exactly one changed input: `state/STANDING_STATE.md`, matching its restored publication edition. Its SHA-256 changed from `26fe0f06f49f5b4a13c90f23bf105d20bf8304f652def1553402277251fc5929` to `cfc33f6ac276f23d4ee7152b718c6c7494f8892dc06492b4bc6d3586d5eddaf1`. The other twenty-nine input hashes match the earlier receipt. `OPENING_INPUT_HASHES.json` has been refreshed from the current inputs; all thirty are checked again after the workspace edits.

## Final deterministic receipt

- PASS — 153 manifest rows preserve all inventory fields, order, categories and chunk counts; all remain open.
- PASS — Date bases and all eleven cross-chunk same-day groups are explicit; no date or outcome adopted as a completed action.
- PASS — All 58 granted cases match Standing State by natural caption, docket and index reference; none duplicated.
- PASS — Nine-person roster, seniority and all thirteen August 3, 1994 circuit allotments match the opening setting.
- PASS — Four nonempty workspace files exist, both projection stubs are replaced, and continuity has all seven required blocks.
- PASS — All thirty refreshed input hashes match current read-only inputs and the pre-edit snapshot; only Standing State changed from the earlier audit receipt.
- PASS — All 71 generated local link occurrences and explicit heading anchors resolve.
- PASS — Repository check_term.py OT1996 passes with 0 warnings; guarded execution invokes only the read-only Holdings checker, no git.
- PASS — All three tracker headers match exactly: OT1995, July 1, 1996 after 116 Court events and ten admitted sources, edition October 7, 2026.
- PASS — All twelve exclusions match the express October 11 inventory decision in continuity, neutral projection and audit; no Court action, date, vote, holding, default or terminal closure is attributed.
- PASS — All manifest and same-day table rows are byte-for-byte unchanged; ledger remains empty, all four opening-status statements agree, and the chronology cursor remains July 1, 1996.

An independent read-only review also confirmed exact inventory coverage, all 58 grant mappings, the roster and seniority, all thirteen circuit allotments, and unchanged standing practice in both projections.

`check_term.py` was executed unchanged through `tmp/revalidate_ot1996_opening.py`, a scratch wrapper that rejects git and every unexpected subprocess. Its only child command was the read-only Holdings check, which passed with exit 0. Output: `OK: OT1996; 0 warning(s)`. Header equality and the twelve-matter inventory reconciliation were checked separately above; they are not supplied by the repository checker.

**Final opening status: complete.** Both opening conflicts are resolved and all revalidation checks pass. No unresolved opening discrepancy, missing inventory row or missing-brief blocker remains. Git verification and commitment are left to the operator; no git command was run.
