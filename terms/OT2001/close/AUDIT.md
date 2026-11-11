# October Term 2001 - Term-Close Audit

**Audit date:** November 11, 2026.
**Adjudicative cutoff:** June 28, 2002; 127 completed scheduled events in eight chunks.
**Result:** One unresolved discrepancy, F1. The term is not ready for Close Commit.

## Unresolved discrepancy

### F1 - Medium (P2): BE&K's reserved liability question is narrowed to sole purpose

**File:** `terms/OT2001/close/STANDARDS_AND_TESTS.candidate.md`
**Line:** 12581, "Exceptions and limits" under "Reasonably based employer litigation and retaliation."

The candidate uses "brought only" where the controlling opinion uses a but-for retaliatory-purpose condition. A lawsuit can have another motive and still satisfy a but-for condition; the candidate therefore understates the category whose legal treatment remains open. The unsuccessful-suit and protected-activity context elsewhere in the entry does not cure this causal change.

**Controlling source:** `terms/OT2001/records/bek-construction-co-v-nlrb_merits_2002-06-24.md`, line 60, repeated in its Public Projection at line 230. Part II has five direct joins. The Holdings candidate at line 49579 and the chunk 8 render at line 192 preserve the controlling reservation. The narrower shorthand in the four-Justice separate-writing summary is not a substitute for Part II's rule.

**Exact fix:** In line 12581, replace only:

> a reasonably based suit brought only to impose litigation costs regardless of outcome

with:

> an unsuccessful, reasonably based suit that would not have been brought but for a purpose to impose litigation costs regardless of outcome in retaliation for protected activity

Retain the rest of the paragraph. The replacement above was copied mechanically from the controlling Record. The affected artifact is the staged Standards candidate; the Record, Holdings candidate, Render Input and render already supply the correct controlling reservation. After the candidate correction, verify that reservation and refresh this audit's finding and readiness result.

No additional unresolved discrepancy was identified in the completed review.

## Deterministic checks

These checks preceded the fresh legal-substance reviews.

| Check | Result |
|---|---|
| Required checker | `python tools/check_term.py OT2001` exited 0: OK, with the two false-positive warnings explained below. It also validated opening Holdings-volume synchronization, runtime-split freshness and Record/Public Projection interfaces. |
| Inventory, Records and public coverage | All 127 scheduled events map one-to-one to Records, generated Render Inputs and public entries. Chunk counts are 16, 16, 16, 16, 15, 15, 18 and 15. |
| Chronology | Manifest and public events are in effective-date order. The final cursor is June 28, 2002; uncoordinated same-day matters preserve the common entering-law baseline. |
| Participation and arithmetic | Checked 153 explicit judgment components across 118 Records and manually reconciled the remaining judgment forms, including procedural disclosure limits. Counts, named coalitions and partial joins reconcile; Rucker preserves Breyer's nonparticipation and its eight-member judgment. |
| Assignment | Recounted 114 signed plenary lead opinions. All 44 frozen assignment receipts reconcile their enumerated credits to their count vectors and canonical opinion tables. Documented later-written earlier-date Records explain the apparent recount differences under Engine section 8. |
| Frozen handoffs | Overlapping frozen/runtime commitment and reconciliation copies match. Eight neutral-copy differences are scoped, augmented or index handoffs; they do not override frozen authority or invalidate the separately checked mechanical runtime splits. |
| Public Projection identity | Generated Render Input blocks match their source Records; no event is dropped or duplicated. |
| Navigation | All 2,182 local Markdown file/anchor references among the 155 audited Record, Render Input, output, workspace and close files resolve. External URLs were outside this local-link check. |
| Candidate integrity | Common publication headers agree. The Standards candidate has 990 distinct rule headings, with required core fields on new entries. Candidate line endings remain unchanged. |
| Open matters and cleanup | Arizona v. California, Kansas v. Colorado and Nebraska v. Wyoming's continuing decree/cost proceedings are carried in Standing State. No scheduled event is stopped or omitted. Three candidates and five pass notes are proper pre-Commit artifacts; their cleanup belongs to Commit. |

The checker's warnings at `records/schrader-v-blackwell_merits_2001-12-10.md:115` and `records/searles-v-van-bebber_merits_2002-01-08.md:142` concern reporter-derived tokens in existing source filenames, not commit references. Both named source files exist. These warnings are not unresolved findings.

## Fresh legal-substance review

Fresh scoped reviews covered all 127 events: chunks 1-3 (48), chunks 4-6 (46), and chunks 7-8 (33). Each reviewed controlling propositions and independent alternatives, proposition-level authority, judgment and remedy, material qualifications, precedent treatment, selected separate writings, continuity, and Justice-specific grounds for historical departures. The reviews compared the relevant new and modified Holdings and Standards entries with the authoritative Records and used public renders as cross-checks. F1 is the only supported discrepancy found.

Material continuity checks included the changed Hendricks, Sutton/Murphy, Circuit City, Shafer and Bennis premises; the Erie/Playboy, sovereign-immunity and Sandin lines; and Angle's effect on Harris and Ring. Distinct formal dispositions, reasoning coalitions and remedial limits remain separate. No historical outcome was substituted for an adjudicated result.

The nine nonexact matches among 280 labeled operative-rule paragraphs in Holdings preserve their substance through subject placement, remedy fields or faithful restatement. Balderas's exclusions and remedy remain intact. Nebraska's complete operative decree is preserved in the Holdings candidate, and its rendered text differs only in typography, reflow and table presentation. The institutional review confirmed the OT2002 roster, seniority, circuit allotments, unchanged standing practice and three original-action docket lines.

This review used the existing local Records, relevant opening law, handoffs, workspace projections, candidates and renders. It did not independently retrieve every historical filing or re-create every original source investigation. The only Git subprocesses were the read-only `cat-file` lookups made by the expressly permitted checker. Repository-history comparison and first-record commitment chronology beyond that permitted check remain for the operator; this audit makes no claim that they were independently verified.

## Commit handoff and file scope

The candidates intentionally retain the synchronized OT2000 publication header while staged. After F1 is resolved, coordinated Commit must advance all three together to last completed October Term 2001, processed through June 28, 2002 after all 127 completed OT2001 Court events, with one common edition date. Commit also performs publication, volume synchronization, index generation and candidate/pass-note cleanup under the governing protocol. These future Commit operations are not present audit defects.

The absence of GitHub repository URLs in published trackers is intentional. Unresolved source-relative navigation inside copied `freeze/` and `entering-law/` material was excluded from close findings as directed.

**Repository file written:** `terms/OT2001/close/AUDIT.md`, to record the completed audit, F1 and the Close Commit decision. No adjudication, render, candidate, published tracker or governing file was changed. The new audit uses CRLF, matching the close pass notes. Existing files retain their line endings.

**Ignored scratch written:** `tmp/ot2001_audit_assignment_parse.json`, containing mechanically extracted assignment/count data. No prohibited directory or filename was inspected. No Git command was issued directly, and no staging, commit, checkout or push was performed.

READY FOR CLOSE COMMIT: NO
