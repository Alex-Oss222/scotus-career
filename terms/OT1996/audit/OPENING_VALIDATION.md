# OT1996 opening validation

**Result: prepared; opening validation incomplete.** The four workspace files are populated, and the 153-item supplied inventory is fully covered. Two source conflicts remain; neither is repaired by altering protected inputs. The term is not certified open merely because a manifest now exists.

**Operator boundaries:** No git command; no access to the locked top-level directory. Writes are confined to `terms/OT1996/workspace/`, `terms/OT1996/audit/` and ignored `tmp/` scratch. No state, inventory, brief, other-term or foundation modification. Chunk briefs are expected later and are not an opening blocker.

## Opening baseline

All three opening trackers identify **Last completed October Term: 1995** and **Processed through: July 1, 1996, after all 116 completed OT1995 Court events and ten admitted source events.** Their exact editions differ:

| Opening authority | Edition |
|---|---|
| [Holdings continuous view](../../../state/HOLDINGS.md), synchronized with the [doctrinal volumes](../../../state/holdings/INDEX.md) | October 7, 2026 |
| [Standards and Tests](../../../state/STANDARDS_AND_TESTS.md) | October 7, 2026 |
| [Standing State](../../../state/STANDING_STATE.md) | October 11, 2026 |

The divergence point is October 7, 1991, when Alex-Lamar Stone-Zsela replaces Rehnquist as Chief Justice. [Court Composition](../../../foundation/COURT_COMPOSITION.md) governs membership, seniority and circuit allotments.

## Unresolved conflicts

1. **Publication synchronization:** Standing State is dated October 11, 2026; Holdings and Standards and Tests are dated October 7, 2026. The three publication templates and Engine §13 require identical editions. The legal cutoff matches, but the opening set cannot be certified synchronized. No source header has been normalized or replaced.
2. **Prior-term pending docket:** The current opening instruction and Standing State §4 supply 58 sim-granted cases and no carried-over matter. The OT1995 final manifest, continuity note and close dossier explicitly retain twelve pending matters. The opening calendar follows the supplied 153-item inventory and adds no carryover; that does not enter a terminal action or resolve the prior sources. Reconcile this conflict before the first adjudication. The natural matters and source locations appear below.

| Prior source's pending matter | Docket |
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

Sources: [OT1995 final manifest](../../OT1995/workspace/manifest.md), [final continuity](../../OT1995/workspace/continuity.md), and [Term-Close Dossier, Final manifest, continuity and carry-forward](../../OT1995/close/TERM_CLOSE_DOSSIER.md#final-manifest-continuity-and-carry-forward). These are a conflict register, not twelve scheduled OT1996 events. No date, Court disposition or continuity closure is supplied here.

Wood retains a plenary grant; the three Shieh petitions remain separate. In [Jones's February 26, 1996 Record](../../OT1995/records/Jones_v_ABC_TV_filing_order_1996-02-26.md), financial leave and certiorari remain pending. Its exact blocker is authentication of the prescribed Rule 39.1 motion and notarized Form 4 affidavit or a declaration under 28 U.S.C. §1746 establishing the required financial particulars, or a supported applicable alternative basis, including an established qualifying appointed-counsel exception. Missing research support establishes neither nonfiling nor default. No refiling duty, payment deadline, decision date or terminal disposition is established.

Required next resolution: establish a coordinated opening publication edition and reconcile the prior final pending docket with the current no-carryover setting. This task neither amends state nor treats the operator's description of Standing State as an adjudicative closure. It preserves all completed decisions. No new terminal event, deadline or default is invented. Git provenance verification and any authorized source repair remain with the operator.

## Inventory and institutional validation

| Check | Result |
|---|---|
| `python -B tools/holdings_volumes.py check` | PASS, exit 0: all eighteen doctrinal volumes and compatibility view synchronized |
| Common last-completed term and processed-through statement | PASS: OT1995; July 1, 1996, after 116 Court events and ten admitted sources |
| Common edition | FAIL: October 7 versus October 11, 2026 |
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
| Prior-term carryover reconciliation | UNRESOLVED: twelve pending matters in prior final sources; no carryover in current supplied setting |
| New events and source admissions | Zero; current ledger empty; opening does not advance the July 1, 1996 cursor |
| Brief availability | Expected absence; not a blocker and no brief contents read |

The introductory applications/petition-stage summary in `case-list.md` omits Lords Landing, although its No. 104 row explicitly supplies petition-stage possible GVR. The manifest preserves that row and posture. This is a summary omission, not a missing inventory event. The index's “not yet opened” note remains accurate while opening validation is incomplete. The protected index was not edited.

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

These final events were checked against each term's close dossier and existing Record paths in an independent read-only review. The review also identified the pending-docket conflict. It did not re-adjudicate earlier cases or use Git to verify lineage.

## Scope of legal validation

This opening task checks publication integrity, continuity, institutional setting and inventory completeness. It does not repeat the completed OT1995 substantive close audit or adjudicate any OT1996 question. No material new disagreement between Holdings and Standards was resolved or silently synthesized. Existing law remains at its exact sources, and the full legal baseline is not certified while the opening conflicts remain.

The ten admitted OT1995 source events remain part of the baseline with their own temporal limits. No post-cutoff external research or source admission was undertaken. Later neutral preflight must verify any material intervening law, especially for the first inventory item. Prior published Justice positions are consulted from public renders when implicated; this opening imports no private positions or historical comparator.

## Files written and verification receipt

- [manifest.md](../workspace/manifest.md): 153 planned events, date bases, stages, dependencies and cross-chunk same-day groups.
- [ledger.md](../workspace/ledger.md): zero current-term entries.
- [continuity.md](../workspace/continuity.md): all seven Engine blocks, exact opening sources, prior final events, institutional state and unresolved conflicts.
- [neutral-projection.md](../workspace/neutral-projection.md): sanitized current law, procedure, chronology and material dependencies; no private or comparator input.
- This audit and [OPENING_INPUT_HASHES.json](OPENING_INPUT_HASHES.json): exact SHA-256 values for thirty explicitly scoped read-only governing/baseline/inventory inputs.

`python -B tools/open_term.py OT1996` completed successfully and seeded 153 events. Both generated stubs were replaced with substantive projections. A separate validation receipt below records the checks actually completed after writing. No Git validation or commit is claimed.

## Final deterministic receipt

- PASS — 153 manifest rows preserve all inventory fields, order, categories and chunk counts; all remain open.
- PASS — Date bases and all eleven cross-chunk same-day groups are explicit; no date or outcome adopted as a completed action.
- PASS — All 58 granted cases match Standing State by natural caption, docket and index reference; none duplicated.
- PASS — Nine-person roster, seniority and all thirteen August 3, 1994 circuit allotments match the opening setting.
- PASS — Four nonempty workspace files exist, both projection stubs are replaced, and continuity has all seven required blocks.
- PASS — All thirty explicitly scoped read-only input hashes are unchanged.
- PASS — All 74 generated local link occurrences and explicit heading anchors resolve.
- PASS — Repository check_term.py OT1996 passes with 0 warnings; guarded execution invokes only the read-only Holdings checker, no git.

`check_term.py` was executed unchanged through a scratch Python wrapper that rejects git or any unexpected subprocess. Its only child command was the read-only Holdings check. Output: `OK: OT1996; 0 warning(s)`. The checker does not validate publication-edition equality or reconcile prior-term pending matters; its success does not clear the two conflicts above.

**Final opening status: incomplete.** The workspace and inventory checks pass; the synchronized-baseline and carryover checks do not. No missing OT1996 inventory row or missing-brief blocker was found. No Git command or provenance verification was performed.
