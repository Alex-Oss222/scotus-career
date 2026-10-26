# October Term 1997 - Close Audit

**Audit date:** October 25, 2026.
**Status:** Not ready for Close Commit. Four unresolved deterministic findings remain: F-01 through F-04. The required fresh legal-substance review has not begun.
**Authority and scope:** AGENTS.md Close protocol, foundation/ENGINE.md, the applicable tracker instructions and Render Contract. Records control; renders are cross-checks. This audit changes no adjudication, handoff, projection, candidate or published tracker.

## Unresolved findings

### F-01 - Medium - Ricci is incorrectly classified as a dismissal

**Files and lines:** `terms/OT1997/case-list.md:116`; `terms/OT1997/workspace/manifest.md:98`; inventory totals at `terms/OT1997/case-list.md:9`.

Both inventory rows describe a dismissal as improvidently granted. The controlling `terms/OT1997/records/ricci_v_village_of_arlington_heights_merits_1998-05-04.md:2-3,95-106` and the corresponding public entry instead record a substantive 5-4 targeted reversal and remand. This is an inventory/projection discrepancy, not a proposed change to the judgment.

**Exact fix:** In both rows replace the event description with `Merits decision` and the category/matter type with `MERITS`. Retain the caption, No. 97-501, May 4, 1998 date, question and completed-Record reference. At case-list line 9 change the totals to `151 MERITS` and `4 DISMISSAL`; the total of 160 matters and chunk counts stay the same. Do not revise the Record or render to match the erroneous dismissal label.

### F-02 - Medium - W.P. retains E.B.'s docket in the case index

**File and line:** `terms/OT1997/case-list.md:85`.

The index gives W.P. No. 96-5132. The controlling `terms/OT1997/records/wp_v_verniero_merits_1998-03-16.md:1,8,10` identifies W.P. as Third Circuit No. 96-5416 and expressly excludes the separate E.B. jurisdictional proceeding, No. 96-5132. `terms/OT1997/workspace/manifest.md:73` already reflects that distinction.

**Exact fix:** Replace the docket cell with `Third Circuit 96-5416 (W.P.; consolidated E.B. 96-5132 outside review)`, matching the manifest. Preserve the caption, date, reviewed questions and immutable brief. This repairs the index without enlarging review.

### F-03 - High - Five chunk-1 frozen artifact identities are unreconciled

**File and lines:** `terms/OT1997/freeze/OT_1997CHUNK1_FREEZE_RECEIPTS.json:31,91,101,131,186`. The affected files and byte digests are listed below; the table was generated directly from the receipt and current file bytes.

| Target relative to terms/OT1997/ | Receipt line | Recorded SHA-256 | Current SHA-256 |
|---|---:|---|---|
| `entering-law/OT_1997CHUNK1_REVALIDATED.md` | 31 | `922ea4214fabb45f2aebf14571241876babec074c9b946976c9a55b78a68cd5c` | `6bd54fbdf40f78eee04d370aa1ba7ee37f63e331e8f82d1e427dbbe24a25664d` |
| `freeze/OT_1997CHUNK1_COMMITMENTS_RYBAR.md` | 91 | `79b263e047c1b2399e0fc8a44892af1182a49a9f6d9034bbd46169621309345c` | `fa5172a7a8de59ba16a6d9905f6bbd20d6bba31170b182a2a5f7d30e0f5459a4` |
| `entering-law/OT_1997CHUNK1_B.md` | 101 | `81fc2b90c24cbc21e0704c5336566bc5d84126b18e97d17fc9586babc23d6c29` | `50219d444a1483cd309ad876ce9e8906ff168a49c778829ab06b7f8374850c43` |
| `freeze/OT_1997CHUNK1_COMMITMENTS_B.md` | 131 | `933b6a92feacedb1e5198f3741d69e2495ef274f997da00605e940bf1b020a82` | `b0a94fb5f6cb79ce62af1fb4d18477b146974f94a2d66c9e5588f4c34ac2f7d6` |
| `entering-law/OT_1997CHUNK1_RYBAR_EFFECTIVE.md` | 186 | `7fb858229308d73e7d6461fef85e6073d5c5d218332bcbb758c610c3b0c42197` | `d2caa2463f5044b57721aec7e8b2acb7560f7ba1389fccef5f110d1a794d1b2a` |


The mismatches persist after testing LF/CRLF normalization. They affect three entering-law artifacts and two frozen commitment files. The original digests are corroborated by `terms/OT1997/freeze/OT_1997CHUNK3_AFTER_INTERIM_STARTING_HASHES.json:471,575,1243,1251,1259`; the different current digests already appear in `terms/OT1997/freeze/OT_1997CHUNK5_RESUMPTION_STARTING_HASHES.json:76,83,833,837,838`.

Dependent reconciliations still identify the original commitment digests: `terms/OT1997/freeze/OT_1997CHUNK1_RECONCILED_RYBAR.md:7`, `OT_1997CHUNK1_RECONCILED_FOSTER.md:5`, `OT_1997CHUNK1_RECONCILED_PARKER.md:5`, and `OT_1997CHUNK1_RECONCILED_SALINAS.md:5` in the same directory. No later receipt reconciling these five changes was found in the inspected freeze, workspace and Record files.

**Exact fix:** The operator must recover the versions matching the recorded digests and compare each with the current file. Restore the immutable commitment handoffs to their verified original bytes unless a specifically authorized correction establishes another governing version. If such authorization exists, retain the original handoff, identify the corrected version and authority explicitly, and validate the affected reconciliation and downstream dependencies. Add a bounded integrity receipt accounting for all five differences, the exact governing versions and the result of that dependency review. Preserve truthful historical receipts; merely replacing their old hashes with current hashes is not a fix. Any demonstrated substantive change must return through the Engine's authorized correction process.

This finding establishes an unresolved identity/provenance discrepancy. It does not establish that a vote, holding or remedy changed. The permitted commit-object check cannot establish the content or authorization of these intervening edits.

### F-04 - Low - Frozen and derived copies contain unresolved relative navigation

**Files and lines:** The complete location inventory for this finding appears in the F-04 appendix below: 593 unresolved local-link occurrences in 39 top-level freeze Markdown files, and three occurrences in `terms/OT1997/entering-law/OT_1997CHUNK8.md:25646,32700,32720`.

Concrete verified examples:

| File and line, relative to terms/OT1997/ | Original target | Located target or source |
|---|---|---|
| `freeze/OT_1997CHUNK1_OPENING_NEUTRAL.md:13` | `manifest.md` | `../workspace/manifest.md`, with the opening snapshot's effective scope preserved |
| `freeze/OT_1997CHUNK5_ENTERING_ASSIGNMENTS.md:665` | `united_states_v_fields_merits_1998-02-09.md` | `../records/united_states_v_fields_merits_1998-02-09.md`; copied from `records/danahy_v_buscaglia_merits_1998-02-12.md:137` |
| `entering-law/OT_1997CHUNK8.md:25646,32700,32720` | `manifest.md` | `../workspace/manifest.md`, with each copied section's effective scope preserved |

The freeze occurrences comprise 119 `law/`, 193 `research/`, one `position_evidence/`, and 280 copied bare relative targets. Some are inherited source-bundle citations or superseded inputs. Broken navigation alone does not establish missing material evidence, litigant default or an adjudicative defect. It also cannot be reported as a successful literal link-resolution check.

**Exact fix:** Preserve immutable briefs and frozen bytes. Add a durable `terms/OT1997/freeze/OT_1997_LINK_RESOLUTION.md` that accounts for every appendix location, mapping the original artifact, line and target to the original source location, available canonical target and effective snapshot scope. For an obsolete bundle reference, identify the actual operative replacement or explicit supersession; do not manufacture a missing source. Rebase links in mutable reading copies only where permitted, preserving their substance and effective date. Verify every mapped target and anchor. Where a material source cannot be located or shown superseded, state the exact unresolved source and affected event for the subsequent legal audit rather than declaring the link repaired.

## Deterministic checks completed

The first operation was the expressly permitted `python tools/check_term.py OT1997`. It exited 0 with 16 warnings and no errors. The warnings are false matches by the checker's broad hexadecimal pattern: archive/catalogue identifiers, official-document identifiers, an IRS technical-advice number and substrings of ordinary prose. No genuine missing cited commit was identified. This result does not cover the additional mismatches above.

| Check | Result and scope |
|---|---|
| Inventory, manifest and ledger coverage | All 160 scheduled captions, chunks and dates reconcile. The manifest covers 162 Court-action Records; the admitted November 26, 1997 PLRA source accounts for Record 163. Every Record appears once in the ledger with its effective date. F-01 and F-02 are the remaining inventory-field discrepancies. |
| Record-to-Render-Input identity and runtime freshness | Required checker passed the generated Public Projection comparisons, completed-event coverage and approved-brief runtime split checks for all 13 chunks. All 163 Records have the four opening labels. |
| Public event coverage and boundaries | All 13 renders match their Render Inputs' event counts: 162 events total. Each displayed event has one closing line and divider. No Workflow Blockers section remains in the public outputs. |
| Chronology | Scheduled rows are in effective order. All 167 extracted argument/reargument date occurrences precede their decisions. This is date consistency, not a determination that every legal dependency is sound. |
| Participation, judgment and join arithmetic | 144 numeric component-table rows, 107 supporting and 56 opposing prose-roster statements reconcile after applying their explicit common-coalition and nonreach qualifications. Review of 411 topology rows found no absent-participant join or actual double counting. AT&T correctly excludes O'Connor. Legal support for the joins remains outside this arithmetic check. |
| Canonical local links and anchors | 2,299 local Markdown references across 202 current Record, Render Input, render, workspace, close and case-index files resolved; 172 anchor-target files were examined. This does not waive F-04 in the auxiliary copies. External URLs were not live-probed. |
| Frozen identity evidence | 131 references to 117 distinct targets were checked; 121 matched current bytes exactly. F-03 accounts for the unexplained chunk-1 discrepancies. Earlier chunk-6 assembly hashes are explained by the subsequent matching integration receipt at `freeze/OT_1997CHUNK6_RESUMED_INTEGRATION_CHECKS.json:3-5`. A changed chunk-12 temporary formatting scratch file is not an authoritative frozen input. All 14 chunk-13 commitment/reconciliation index hash rows match. |
| Holdings candidate structure and coverage | All 836 opening case blocks survive. The 207 new area blocks cover 158 Court-action events, excluding the Rogers DIG, Hetzel's separate grant, and the Caterpillar and Lewis/Brunswick Rule 46.1 dismissals. Existing-entry maintenance is confined to Lewis, Plyler and Kinman fields. The admitted PLRA amendment is maintenance, not a fabricated case holding. This is structural coverage, not approval of legal incorporation. |
| Standards candidate structure | All 584 opening entries survive: 559 unchanged and 25 amended, plus 113 additions. The 697 current-rule titles are unique and required core fields are present. Whether every rule faithfully states controlling law awaits the gated legal review. |
| Standing State and carry-forward | Court/practice sections match the opening tracker with the prospective term advanced; nine Justices and thirteen allotments match Composition. All five opening carryovers and nine current-term pending stages appear among fourteen pending docket lines. Davenport and Jean are two additional OT1998 reservations with their intake gaps expressly retained. |
| Publication metadata and cleanup | All three candidates intentionally retain identical opening publication metadata pending coordinated Commit; all use CRLF. Candidate files and pass notes must remain until successful Commit. Their current presence is not a defect. The deliberate omission of GitHub repository URLs from published trackers is not a defect. |

## Required next validation and operator boundary

AGENTS.md:144 permits fresh legal-substance review only after the deterministic checks pass. F-01 through F-04 prevent that gate from passing. Accordingly, this audit does not certify votes' legal grounds, coalition feasibility, controlling holdings, precedent treatment, remedies, continuity or Justice-specific historical departures. After the findings are resolved, rerun the deterministic checks and conduct the required fresh review against the opening trackers, all Records, final workspace, approved corrections, candidates and renders before replacing this audit's readiness conclusion.

No Git command was run directly. Git access was limited to the explicitly authorized check_term.py commit-object lookups. Truthful lineage verification against historical content remains reserved to the operator; object existence alone does not verify a lineage claim. No prohibited directory or prohibited filename was accessed. Only this audit is written by the audit task. No finding is silently repaired outside its write boundary.

## F-04 location appendix

The following file/line inventory is generated mechanically from the retained freeze and entering-law Markdown files. Each row requires the resolution or explicit source-context/supersession mapping specified in F-04; it does not assert that every referenced document remains legally necessary. Multiple unresolved targets on one line are represented by that line once. Original briefs and byte-identical runtime exports are not to be rewritten to repair their inherited bundle citations.

| File relative to terms/OT1997/ | Lines containing unresolved local targets |
|---|---|
| `entering-law/OT_1997CHUNK8.md` | 25646, 32700, 32720 |
| `freeze/OT_1997CHUNK10_NEUTRAL.md` | 45, 46, 65, 109, 110, 129, 173, 174, 193, 237, 238, 257, 303, 304, 323, 368, 387, 430, 456, 496, 497, 523, 567, 568, 594, 634, 635, 654, 698, 699, 718, 763, 782 |
| `freeze/OT_1997CHUNK10_PRIOR_ASSIGNMENTS.md` | 1010, 1055, 1100, 1136, 1202, 1241 |
| `freeze/OT_1997CHUNK11_ASSIGNMENT_READING.md` | 834, 876, 916, 945, 969, 1025, 1054 |
| `freeze/OT_1997CHUNK11_COMPARATOR_A.md` | 19, 55, 77, 115 |
| `freeze/OT_1997CHUNK11_COMPARATOR_B.md` | 23, 55, 97 |
| `freeze/OT_1997CHUNK11_COMPARATOR_C.md` | 27, 65, 97, 121, 145 |
| `freeze/OT_1997CHUNK11_NEUTRAL.md` | 45, 46, 65, 107, 108, 134, 176, 177, 203, 245, 246, 270, 314, 315, 346, 390, 391, 410, 452, 453, 479, 521, 522, 548, 590, 591, 617, 659, 660, 686, 730, 731, 757, 799, 800, 826 |
| `freeze/OT_1997CHUNK11_NEUTRAL_A.md` | 39, 40, 59, 94, 95, 121, 156, 157, 183, 218, 219, 243 |
| `freeze/OT_1997CHUNK11_NEUTRAL_B.md` | 39, 40, 71, 108, 109, 128, 163, 164, 190, 225, 226, 252 |
| `freeze/OT_1997CHUNK11_NEUTRAL_C.md` | 37, 38, 64, 101, 102, 128, 163, 164, 190 |
| `freeze/OT_1997CHUNK11_PRIOR_ASSIGNMENTS.md` | 900, 939, 976, 1002, 1025, 1077, 1107 |
| `freeze/OT_1997CHUNK12_COMPARATOR_BAUCHMAN.md` | 29 |
| `freeze/OT_1997CHUNK12_COMPARATOR_BERRYMAN.md` | 25 |
| `freeze/OT_1997CHUNK12_COMPARATOR_BREWSTER.md` | 25 |
| `freeze/OT_1997CHUNK12_COMPARATOR_CAMILO.md` | 21 |
| `freeze/OT_1997CHUNK12_COMPARATOR_CLEAN.md` | 43, 92, 129, 174, 217, 250, 289, 332, 369, 398, 431, 464 |
| `freeze/OT_1997CHUNK12_COMPARATOR_ELLERTH.md` | 35 |
| `freeze/OT_1997CHUNK12_COMPARATOR_MONGE.md` | 31 |
| `freeze/OT_1997CHUNK12_STONE_BALSYS.md` | 29 |
| `freeze/OT_1997CHUNK13_ASSIGNMENT_SOURCE.md` | 551, 580, 628, 665, 702, 773, 829 |
| `freeze/OT_1997CHUNK13_COMPARATOR_146.md` | 13 |
| `freeze/OT_1997CHUNK13_NEUTRAL_HADIX.md` | 44, 45, 64 |
| `freeze/OT_1997CHUNK1_OPENING_NEUTRAL.md` | 13 |
| `freeze/OT_1997CHUNK2_NEUTRAL_ROGERS_SEED.md` | 39, 40, 59 |
| `freeze/OT_1997CHUNK2_OPENING_NEUTRAL.md` | 11, 269 |
| `freeze/OT_1997CHUNK3_OPENING_NEUTRAL.md` | 11, 485 |
| `freeze/OT_1997CHUNK4_ENTERING_ASSIGNMENTS.md` | 622, 648, 695, 733, 771, 842, 901 |
| `freeze/OT_1997CHUNK4_KIRK_SHAHAR_NEUTRAL_REVIEW.md` | 154, 155, 181 |
| `freeze/OT_1997CHUNK4_MODEL_A_NEUTRAL.md` | 131, 202, 336, 412 |
| `freeze/OT_1997CHUNK4_MODEL_B_NEUTRAL.md` | 73, 149, 216, 347, 423, 499 |
| `freeze/OT_1997CHUNK4_NEUTRAL.md` | 134, 204, 337, 412, 494, 569, 635, 764, 839, 914 |
| `freeze/OT_1997CHUNK5_ENTERING_ASSIGNMENTS.md` | 509, 561, 577, 591, 626, 665 |
| `freeze/OT_1997CHUNK8_ASSIGNMENT_BASELINE.md` | 807, 836, 884, 925, 964, 1039, 1097 |
| `freeze/OT_1997CHUNK8_ASSIGNMENT_CURRENT.md` | 819, 848, 896, 937, 976, 1051, 1109 |
| `freeze/OT_1997CHUNK8_NEUTRAL.md` | 42, 43, 62, 120, 121, 147, 192, 218, 261, 262, 281, 325, 326, 345, 389, 390, 409, 451, 452, 478, 520, 521, 552, 594, 595, 621, 663, 664, 690, 735, 766, 807, 808, 827 |
| `freeze/OT_1997CHUNK8_NEUTRAL_A.md` | 38, 39, 58, 116, 117, 143, 188, 214, 257, 258, 277, 322, 353, 394, 395, 414 |
| `freeze/OT_1997CHUNK8_NEUTRAL_B.md` | 41, 42, 61, 105, 106, 125, 167, 168, 194, 236, 237, 268, 310, 311, 337, 379, 380, 406 |
| `freeze/OT_1997CHUNK8_OHIO_NEUTRAL_CLEAN.md` | 36, 37, 62 |
| `freeze/OT_1997CHUNK9_ENTERING_NEUTRAL_PROJECTION.md` | 11, 8231, 8255 |


READY FOR CLOSE COMMIT: NO
