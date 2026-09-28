# October Term 1993 — Seventh Re-audit

**Audit date:** September 28, 2026.  
**Result:** PASS — the complete deterministic gate is clean; the Fifth Re-audit's completed substantive conclusions remain applicable.  
**Current findings:** 0 critical, 0 high, 0 medium, 0 low.  
**Publication status:** Staged close. **Commit October Term 1993 close is authorized.** This Audit does not itself publish the trackers or complete the Commit pass.  
**Observed repository HEAD:** `414f02748bd7a4ff0b8fb460e297153ecbc74439`, verified through direct reference and object reads.

**R15 is RESOLVED.** The [chunk-4 output](../output/OT_1993CHUNK4.md) now has the required horizontal divider at line 859, after the *Security Services, Inc. v. Kmart Corp.* closing line at line 857. The exact change from the Sixth Re-audit baseline is an appended blank line and `---` line: raw bytes `\n---\n`. Every preexisting byte is preserved. All twelve event accounts, from their headings through their bold closing lines, remain byte-identical. All twelve entries now have complete required boundaries.

**R14 remains RESOLVED.** Neither chunk 4's [Render Input](../render-inputs/OT_1993CHUNK4.md) nor its output contains the obsolete Stopped-matters or Workflow Blockers section. No new content or boundary discrepancy was found.

## Scope, baseline and substantive reliance

This report replaces the Sixth Re-audit at the user's direction. That report is preserved at the observed HEAD, at `terms/OT1993/close/AUDIT.md`; direct object reads confirm it matches the report present at intake, allowing for repository newline storage. The exact Sixth-pass output bytes were recovered from commit `1fa9ee208f15808c24f5f826b9edb7ffe520d5f6` and verified against the Sixth Re-audit's stored raw-file SHA-256 digest before comparison. The repair conclusion therefore rests on byte evidence, not normalized prose or the operator's description.

The Sixth Re-audit's protected snapshot contains 2,128 files outside repository metadata and ignored root scratch, excluding the replaceable Audit. Exactly one differs: `terms/OT1993/output/OT_1993CHUNK4.md`. The other 2,127 are byte-identical, with no protected addition or deletion. This includes every Record, source, approved brief, runtime split, freeze, entering-law slice, workspace projection, candidate, opening tracker and infrastructure file, all eight Render Inputs, and the other seven outputs. Apart from the replacement Audit and ignored checking evidence, no other file was affected.

As expressly authorized, this pass does not claim another fresh substantive review of all 95 matters. The Fifth Re-audit completed that review across all 95 Court matters, the Act 184 Admitted Source Record, both Holdings pass contributions, the complete Standards and Tests candidate and the Standing State candidate, finding zero substantive defects. The Sixth Re-audit verified continued applicability. This pass verified preservation again and found nothing in its deterministic checks that contradicts those conclusions. Their substantive findings remain the basis for this clean close audit.

## Deterministic checks

| Check | Result and evidence |
|---|---|
| Required initial checker | PASS: `python tools/check_term.py OT1993` ran first and returned exit 0, OK, with 14 accepted lexical warnings. Its internal Git execution is disclosed below. A guarded rerun of the unchanged main routine, using direct object reads for commit existence, also returned exit 0 with 14 warnings. |
| Inventory → manifest → Records → Render Inputs → renders | PASS: all 95 Court matters have one current Record and one public entry. There are 96 Records including the separate Act 184 source. Chunk counts are 12, 12, 12, 12, 12, 12, 12 and 11. All 96 Records occur once in the ledger; no Court event was added, removed or duplicated. |
| Effective-date order | PASS: inventory and manifest dates, Record dates, input order, output chronology, separate event-and-date lines and closing dates reconcile. Court-event dates are nondecreasing. Act 184 remains separately scheduled for January 1, 1994. All five expressly sequenced same-day pairs and their reviewed entering-law materials are preserved. |
| Participation, vote and join arithmetic | PASS: repeated mechanical checks of 136 named judgment rows and 273 named writing rows identify no tally mismatch, opposing-side overlap or new participation inconsistency. All 95 public participation, judgment and topology fields exactly match the Fifth Re-audit's reviewed fields. Its component-specific participation, partial-join and eight prose-judgment checks remain applicable; no vote or join changed. |
| Runtime-split freshness | PASS: all eight approved briefs pass the splitter's check mode through the checker. No runtime split was regenerated or edited. |
| Public Projection → Render Input identity | PASS for all 95 Court-event blocks. Internal controlling-proposition, explanation and authority comparisons also show no drift. All Render Inputs are byte-identical to the Sixth baseline. |
| Render coverage, forms and boundaries | PASS: 95 headings, 95 separate event-and-date lines, 95 matching bold closing lines and 95 following dividers. An independent check verifies each complete boundary, including every final entry, the repeated caption/event/date, interior heading levels, and the absence of event prose after the closing line. All supplied full forms retain their tables. The same sixteen compact table-to-prose diagnostics remain covered by the prior substantive review; no new diagnostic appears. |
| Link and anchor resolution | PASS: 6,426 local/same-repository link occurrences across 813 term Markdown files, excluding this replacement Audit. All 525 inherited-alias diagnostics resolve under the documented convention. Every checked local target and anchor resolves. This Audit's links receive a separate final check. |
| Commit-hash existence and concise lineage | PASS: all 126 genuine commit-reference occurrences resolve to commit objects by direct reads. The 333 other lexical candidates are unchanged non-commit tokens. Record lineage and previously verified provenance materials remain byte-identical; their qualified claims are preserved. No narrative commit archaeology was required. |
| Opening Holdings volumes | PASS through the checker's invocation of `tools/holdings_volumes.py check`. The opening canonical volumes and continuous compatibility view remain synchronized. |
| Candidate staging and cleanup | PASS for pre-Commit staging: three candidates, two Holdings pass notes, one Standards pass note, one current Audit and `.gitkeep`. No competing candidate or premature final dossier exists. The common retained fields agree: completed OT1992, processed through July 26, 1993 after DeBoer, edition September 17, 2026. These remain expressly staged fields; synchronized publication and candidate/pass-note cleanup belong to the authorized Commit pass. |
| Open-matter carry-forward | PASS: seven inherited matters and Anderson's underlying writ remain expressly carried open. Fifteen user-added OT1994 matters are included, yielding 23 docket rows. Day and Sassower's fee components remain expressly scope-closed without Court adjudication; Cavanaugh remains completed. None of those three appears as open in the candidate docket or as a live chunk-4 blocker. |
| Preservation since the Sixth Re-audit | PASS: only the exact divider restoration changed among 2,128 protected paths. All twelve chunk-4 accounts are byte-identical through their closing lines; the other 2,127 protected files are byte-identical, with no addition or deletion. |

The previously accepted checker heuristic and external URL reachability remain tool/documentation limitations, not content findings. This pass does not claim fresh retrieval of the 532 distinct external links. Neither limitation is re-flagged.

## R15 repair and boundary verification

The Sixth baseline output digest is `4fc747643f82431ca43e924d64990d4fb26350b3f1a7a751f1ab18019b475d96`. The repaired output digest is `219c0d9c8ca99c511a50cd62906ef88d98180c6b66cd0419cf6d50053f114aa1`. The current file begins with the entire baseline byte sequence and adds only `\n---\n`. Its line delta inserts lines 858–859, removes nothing and alters no existing line.

All twelve output entries were separately extracted and compared as raw bytes from their level-three headings through their bold closing lines. Every comparison passes. The restored final divider completes the boundary required by [Render Contract §3](../../../foundation/RENDER_CONTRACT.md#3-chunk-presentation); all eight outputs also pass the independent boundary check under [§8](../../../foundation/RENDER_CONTRACT.md#8-projection-check). Each closing line has exactly one following divider and no intervening substantive account. The added divider does not restore the removed Workflow Blockers footer or change any procedural status.

The [manifest's completed-status resolution](../workspace/manifest.md#status-after-resolving-the-three-chunk-1-matters), the affected Records and the candidate docket remain unchanged. R14's correction and R15's formatting repair are both complete.

## Retained legal and candidate conclusions

The Fifth Re-audit's full legal conclusions remain applicable, including resolution of R08–R13 and removal of the Stone Method/outside-brief provenance. The Posters, Carter and Irvine qualifications, active Good/Powell/Reed propagation, removal of the four obsolete scratch files, and all 28 corrected entering-law/frozen projection targets remain preserved. No affected authority or candidate changed.

Both Holdings contributions remain substantively verified: 234 current-term controlling propositions, including nine independently sufficient alternatives. The complete Standards and Tests candidate remains verified across all 289 entries against opening law and the Records. Standing State's OT1994 roster, seniority, allotments, referral practice and 23-row docket remain verified. The Act 184 source retains its effective date, transition and savings limits and does not become a Court adjudication. No fresh substantive defect was found or inferred from the formatting repair.

## Execution disclosure and preservation

The required initial direct checker invocation internally launched read-only `git cat-file` subprocesses before its implementation was inspected. This violated the user's prohibition on every Git command and was disclosed during the task. No explicit Git command, staging, commit, checkout or push followed. Subsequent provenance checks read `.git` references and objects directly. Later checker execution used its unchanged main routine with an equivalent direct-object existence callback and a guard rejecting Git subprocesses. The repository checker was not edited. This execution deviation is separate from the repository-content audit result.

Only this Audit and ignored scratch under `tmp/ot1993_reaudit7/` were written. No finding was repaired during this pass. Scratch evidence contains the intake Sixth report, protected-file snapshots, exact repair diff and per-entry digests, repeated deterministic results, arithmetic, links, direct-object checks and guarded checker transcripts. Repository history preserves prior reports and file versions.

**Final verification:** After replacement, the guarded checker returned exit 0. Every link and supplied anchor in this Audit resolves. All 2,128 protected intake files remain byte-identical during this pass, with no protected addition or deletion; repository HEAD is unchanged. The only changed durable artifact is this Audit.

**Operator conclusion:** **PASS — Commit October Term 1993 close is authorized.** Findings: 0 critical, 0 high, 0 medium, 0 low.
