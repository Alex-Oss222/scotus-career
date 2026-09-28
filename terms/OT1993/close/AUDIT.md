# October Term 1993 — Sixth Re-audit

**Audit date:** September 28, 2026.  
**Result:** FAIL — one low-severity render-boundary discrepancy.  
**Current findings:** 0 critical, 0 high, 0 medium, 1 low.  
**Publication status:** Staged close; Commit is not authorized while R15 remains open.  
**Observed repository HEAD:** `0504fd80508025397c8fb6eac6e2d0df281137bc`, verified by direct reference and object reads.

**R14 is RESOLVED.** Chunk 4's Render Input and output contain neither a Stopped-matters section nor a Workflow Blockers section, including the obsolete references to Day, Sassower and Cavanaugh. The repair also deleted the horizontal divider required after the final output entry, *Security Services, Inc. v. Kmart Corp.* That additional deletion is R15. All twelve Render Input event blocks and all twelve output accounts through their closing lines are byte-identical to the Fifth Re-audit baseline; the final entry's complete required boundary is not.

The Fifth Re-audit's completed substantive legal conclusions remain applicable. This pass found no contradictory legal evidence and does not reopen that review. The standalone checker returns OK, but the complete deterministic gate fails on R15.

## Scope and basis for reliance

This report replaces the Fifth Re-audit at the user's direction. The prior report is preserved in repository history at the observed HEAD above, at `terms/OT1993/close/AUDIT.md`; its contents were compared directly with the report present at intake. The Fifth Re-audit recorded a complete fresh substantive review of all 95 Court matters, the Act 184 Admitted Source Record, both Holdings pass contributions, the complete Standards and Tests candidate, and the Standing State candidate. It found zero substantive defects and only R14. It separately verified resolution of R08–R13 and removal of the Stone Method/outside-brief provenance.

The user expressly limited this pass to the narrow repair, continued preservation and the deterministic gate. Accordingly, this pass does not claim another fresh legal review of all 95 matters. It relies on the Fifth Re-audit's conclusions after confirming that every reviewed Record, brief, runtime file, freeze, entering-law slice, workspace projection, candidate and opening tracker remains unchanged.

The Fifth Re-audit's 2,128-file protected snapshot supplies the byte comparison. Exactly two files differ: chunk 4's Render Input and output. The other 2,126 files are byte-identical; there is no protected-file addition or deletion. In particular, the other seven chunks' fourteen Render Input/output files are byte-identical. Prior bytes for the two changed files were recovered from the Fifth Re-audit's observed commit, `615985227dc8dc501e7a7826da6ff271cfa5d2c9`. Their original newline forms were verified against the prior raw-file SHA-256 digests before comparing them with the current files. The preservation conclusion therefore does not rest on normalized prose or on the operator's description of the repair.

## Deterministic checks

| Check | Result and evidence |
|---|---|
| Required initial checker | PASS: `python tools/check_term.py OT1993` returned exit 0, OK, with 14 accepted lexical warnings. Its internal Git execution is disclosed below. A subsequent guarded run of the unchanged checker, with direct object reads for commit existence, also returned exit 0 and 14 lexical warnings. |
| Inventory → manifest → Records → Render Inputs → renders | PASS for coverage: 95 Court matters, 95 current public entries and 96 Records including the separate Act 184 source. Chunk counts remain 12, 12, 12, 12, 12, 12, 12 and 11. All 96 Records appear once in the ledger. No event was added, removed or duplicated. |
| Effective-date order | PASS: inventory, manifest, Record dates, input order, render chronology and closing dates reconcile. Court-event dates are nondecreasing. Act 184 remains separately scheduled for January 1, 1994. The five expressly sequenced same-day pairs and all other chronology materials are unchanged from the reviewed baseline. |
| Participation, votes and joins | PASS: repeated mechanical checks find no count mismatch, opposing-side overlap or new participation discrepancy in 136 named judgment rows and 273 named writing rows. All 95 participation, judgment and topology fields equal the Fifth Re-audit's reviewed fields. Its component-specific participation, partial-join and eight prose-judgment checks remain applicable; no judgment or join changed. |
| Runtime-split freshness | PASS: the checker ran the splitter's check mode for all eight approved briefs. No runtime split was regenerated or edited. |
| Public Projection → Render Input identity | PASS for all 95 Court-event blocks. Internal controlling-proposition, explanation and authority comparisons also show no drift. The metadata deletion changed no event block. |
| Render completeness and boundaries | Coverage, chronology, supplied forms and substantive preservation PASS. The same sixteen compact table-to-prose diagnostics remain covered by the prior substantive review. Boundary check FAIL: 95 headings and closing lines remain, but only 94 entries have the required following divider. R15 identifies the single missing boundary. |
| Link and anchor resolution | PASS: 6,426 local/same-repository link occurrences across 813 term Markdown files, excluding this replacement Audit. All 525 inherited-alias diagnostics resolve under the documented convention. Every checked local target and anchor resolves. The replacement Audit's links are checked separately. |
| Commit existence and concise lineage | PASS: all 126 genuine commit-reference occurrences resolve to commit objects through direct reads. The 333 other lexical candidates are unchanged non-commit tokens; the only location shift is caused by the removed input lines. Record lineage text and the previously verified provenance materials are byte-identical. No narrative commit archaeology was required. |
| Opening Holdings volumes | PASS through the checker's invocation of `tools/holdings_volumes.py check`; the opening Holdings volumes and continuous compatibility view remain synchronized. |
| Candidate staging and cleanup | PASS for pre-Commit staging: three candidates, two Holdings pass notes, one Standards pass note, this Audit and `.gitkeep`. No competing candidate or premature final dossier exists. All three retained publication headers agree: completed OT1992, processed through July 26, 1993 after DeBoer, edition September 17, 2026. These remain expressly staged fields; synchronized publication and candidate/pass-note cleanup belong to Commit. |
| Open-matter carry-forward | PASS: seven inherited matters and Anderson's underlying writ remain carried open; fifteen user-added OT1994 matters are included, for 23 docket rows. Day and Sassower's fee components remain expressly scope-closed without Court adjudication; Cavanaugh remains completed. None of those three appears as open in the candidate docket. |
| Preservation since the Fifth Re-audit | PASS except the R15 boundary deletion: only the two identified chunk-4 files changed among 2,128 protected paths. All Records, candidates, workspace projections and prior R08–R13/provenance-removal corrections are unchanged. |

The previously accepted checker heuristic and external URL reachability remain tool/documentation limitations, not content findings. This pass does not claim fresh retrieval of the 532 distinct external links. Neither limitation is re-flagged.

## R14 resolution and exact repair delta

The [chunk-4 Render Input](../render-inputs/OT_1993CHUNK4.md) differs only by deletion of the prior blank line and Stopped matters block, old lines 4–8. All twelve generated event blocks remain byte-identical. No Stopped-matters or Workflow Blockers reference remains anywhere in that file.

The [chunk-4 output](../output/OT_1993CHUNK4.md) differs only by deletion of old lines 858–867. That span contains the obsolete Workflow Blockers footer, but also the final event's preceding horizontal divider. Every word, table, citation and closing line in the twelve event accounts is unchanged. No Stopped-matters or Workflow Blockers reference remains anywhere in the output.

The authoritative [manifest resolution](../workspace/manifest.md#status-after-resolving-the-three-chunk-1-matters), [Day Record](../records/Day_v_Day_prospective_filing_control_1993-10-12.md), [Sassower Record](../records/In_re_Sassower_prospective_filing_control_1993-10-12.md) and [Cavanaugh Record](../records/Cavanaugh_v_Roller_merits_1993-11-30.md) remain unchanged. The removed status claims were obsolete. R14 is therefore resolved, independently of the new boundary defect.

## Current finding

### R15 — Low — The R14 repair removed the final chunk-4 entry divider

**Location:** [chunk-4 output](../output/OT_1993CHUNK4.md), immediately after line 857, the closing line for *Security Services, Inc. v. Kmart Corp.*, merits decision, May 16, 1994. The file now ends at that closing line. The old horizontal divider was at line 859 and was deleted together with the footer.

**Requirement:** [Render Contract §3](../../../foundation/RENDER_CONTRACT.md#3-chunk-presentation) requires every event entry to end with its bold closing line followed by a horizontal divider. It expressly applies that boundary to every event, including the last or only entry. [Section 8](../../../foundation/RENDER_CONTRACT.md#8-projection-check) requires verification of the heading, event-and-date line, matching closing line and divider. The divider belongs to the event boundary, not to the Workflow Blockers footer.

**Evidence:** The original output's bytes reproduce the Fifth Re-audit's stored file digest. The raw comparison shows one deletion spanning old lines 858–867, including `---` before the Workflow Blockers heading. All twelve event accounts through their bold closing lines compare identically, but the complete-boundary count falls from twelve to eleven in chunk 4. The independent all-chunk entry check identifies this same entry as the only missing closing boundary.

**Effect and severity:** Low; presentation only. No disposition, date, vote, join, controlling law, remedy, source or procedural status changed. Nevertheless, the output violates an express Render Contract requirement and does not preserve all twelve complete entry boundaries as requested.

**Required resolution:** Restore the horizontal divider after the final Security Services closing line while leaving the removed Workflow Blockers footer absent. Preserve every existing event byte, then recheck all twelve boundaries and the bounded file delta. No repair was made in this pass. Commit remains unauthorized until this finding is resolved and verified.

## Retained substantive conclusions

R08–R13 and the Stone Method/outside-brief provenance removal remain resolved on the Fifth Re-audit's completed review and this pass's exact preservation evidence. This includes the Posters, Carter and Irvine qualifications, the active Good/Powell/Reed propagation, removal of the four obsolete scratch files, and all 28 corrected entering-law/frozen projection targets. No affected authority or candidate changed.

The Fifth Re-audit's complete candidate conclusions also remain in force: both Holdings contributions were reviewed, including 234 current-term propositions and nine independently sufficient alternatives; all 289 Standards and Tests entries were examined against opening law and Records; and Standing State's roster, allotments, practice and docket were verified. This pass found no reason to withdraw any of those conclusions. The single remaining finding concerns only the final render divider.

## Execution disclosure and preservation

The required initial direct checker invocation internally launched read-only `git cat-file` subprocesses before its implementation was inspected. That violated the user's prohibition on every Git command and was disclosed during the task. No explicit Git command, staging, commit, checkout or push followed. Subsequent provenance checks read `.git` references and objects directly. The later checker run used its unchanged main routine, substituted only the equivalent direct-object existence callback, and guarded subprocess execution against Git. The repository checker was not edited. This execution deviation is disclosed separately from the repository-content finding.

Only this Audit and ignored scratch under `tmp/ot1993_reaudit6/` were written. No Record, input, output, tracker, candidate, workspace, source or infrastructure file was repaired. Scratch evidence includes the intake Fifth report, protected-file snapshots, exact R14 diff, per-entry digests, inventory/arithmetic results, links, direct-object checks and the guarded checker transcript. Repository history remains the durable provenance source.

**Final verification:** The guarded checker returned exit 0 after report replacement. All nine report-link occurrences and their supplied anchors resolve. All 2,128 protected intake files remain byte-identical during this pass, with no protected addition or deletion; the repository HEAD is unchanged. Only this Audit and root scratch evidence changed.

**Operator conclusion:** FAIL — R14 resolved; R15 remains open. Commit is not authorized. **Findings: 0 critical, 0 high, 0 medium, 1 low.**
