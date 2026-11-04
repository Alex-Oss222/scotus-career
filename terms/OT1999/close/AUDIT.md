# October Term 1999 - Close Audit

Audit date: November 3, 2026. Scope: the staged close through June 29, 2000, covering 104 Court events and five Admitted Source Records in nine chunks.

**Result: not ready for Close Commit.** Two unresolved projection discrepancies are identified below. This audit changes no adjudication, tracker candidate, public render or workspace projection.

## Audit sequence and limits

The permitted `python tools/check_term.py OT1999` ran first and exited successfully with one warning. The warning concerns the CaseMine source URL in the Mixon Record at lines 168 and 284: its hexadecimal document identifier was mistaken for a commit reference. It is not a missing provenance commit and requires no Record change. No Git command was run independently of the expressly permitted checker. Repository-history verification and commitment remain with the operator.

The remaining deterministic checks were completed before any fresh legal-substance audit. They found F1 and F2. Under AGENTS.md's Close protocol, pass 4, the fresh AI review of votes' legal support, coalition feasibility, holdings, precedent treatment, remedies, continuity and Justice-specific historical departures begins only after the deterministic checks pass. That stage has therefore **not been reached**; this document does not certify legal substance. Correcting F1 and F2 alone will not substitute for that required review.

The absence of GitHub repository URLs in the published trackers is intentional. Unresolved relative navigation inside frozen and entering-law copies is excluded from close defects as directed. No forbidden directory or file was opened. Only this audit is written.

## Unresolved discrepancies

### F1 - Medium - Completed cases remain in the current pending-grant lists

**Files and lines:** `terms/OT1999/workspace/continuity.md:6082` and `terms/OT1999/workspace/neutral-projection.md:6082`; affected subsection: lines 6082-6100 in each file. The erroneous pending stages occur at lines 6088-6093 and 6095-6100.

Both current-procedure projections describe twelve completed matters as granted and awaiting merits review: Reform Party, Gillespie, Doe v. Rosenberg, North Carolina Right to Life, National Mining Association, Saenz, Barrett, Eisenberg, Mixon, Bradley, Hawkins and Henerey. Their dated Records, final manifest and completed-event sections establish that review has occurred. This is not an archival opening list: line 6084 expressly says completed merits matters leave the pending list. McIver is marked completed at line 6094 but also remains in that list.

**Exact fix:** In each file, replace the entire subsection at lines 6082-6100 with the heading `### Opening grants and direct appeal completed` and this paragraph:

All opening grants and the Rayphand/Torres direct appeal scheduled for October Term 1999 have completed review. No opening grant remains awaiting merits review. The separate unresolved matters retain the stages listed below.

Preserve the following pending-matters subsection and all controlling Records. This is projection cleanup, not a new disposition. Then reconcile the resulting list against the final manifest and Standing State candidate.

### F2 - Low - Alaska's current decree stage cites only the 1997 authority

**Files and lines:** `terms/OT1999/workspace/continuity.md:6110` and `terms/OT1999/workspace/neutral-projection.md:6110`.

The Alaska row correctly states that the implementing decree was entered June 29 and that limited implementation jurisdiction remains, but its authority cell cites only the June 19, 1997 decision. The present stage is established by the June 29, 2000 decree Record. The Standing State candidate already uses that current authority.

**Exact fix:** Replace the authority cell in each row with `[Implementing-decree Record, June 29, 2000](../records/united-states-v-alaska_decree_2000-06-29.md)`. The 1997 decision may also be retained if expressly identified as the opening authority. Keep the entered-decree stage and limited retained jurisdiction unchanged. Recheck both links after editing.

## Deterministic verification

| Check | Result |
| --- | --- |
| Repository checker | Passed with the resolved CaseMine false positive described above; opening Holdings volumes synchronized. |
| Inventory, Records and renders | 104 inventory events reconcile to 104 Court Records, generated event blocks and public entries. The nine chunk counts are 12, 12, 12, 12, 12, 12, 12, 12 and 8. The ledger covers all 109 Records once. |
| Effective-date order | Inventory and event dates agree; Render Inputs follow effective-date order. Ledger recording order is not mistaken for effective-date order. |
| Participation, quorum and vote arithmetic | 102 events identify nine participants; Free identifies eight and publishes an undisclosed 4-4 division; Alaska publishes no tally. All 126 parsed judgment-roster comparisons reconcile, with seven special-format or undisclosed cases reviewed separately. |
| Argument/submission chronology | 103 explicit date mentions across 100 events precede or coincide with decision. Three summary dispositions have no dated argument; Alaska is an implementing decree. |
| Render structural fidelity | Published judgment rosters, counts, authorship, full/partial joins and judgment-only relationships agree with the Public Projections. This does not certify every paraphrased sentence's legal meaning. |
| Runtime split freshness | Passed for all nine rendered chunks through the permitted checker. |
| Public Projection identity | All generated event blocks match their source Records' bounded Public Projections. |
| Assignment receipt arithmetic | 33 receipts with source lists were recounted; 97 distinct referenced author/date combinations matched the Records. This checks arithmetic and attribution, not substantive eligibility or coalition grounds. |
| Local links and anchors | All 1,853 checked local links across 140 scoped files resolve, including candidate links mapped to their intended publication targets. External URLs were not broadly crawled. Frozen/entering-law navigation exemptions were honored. |
| Commit references | The sole checker warning is a source-URL identifier. No actual unresolved commit reference was identified. No independent Git inspection was performed. |
| Holdings candidate coverage | 121 additions cover 103 Court events; Free's equal-division affirmance properly supplies no controlling holding entry. The 1,199 opening entries become 1,320 candidate entries; three existing entries change and 1,196 retain their bodies. The three passes contain 256 question blocks. |
| Holdings mechanical fidelity | Of 250 explicitly labeled holding paragraphs compared with mapped Records, 247 match exactly. Three have bounded presentation changes concerning Locke, Weeks and Mobil. This is not a substantive-law certification. |
| Standards candidate coverage | Its pass receipt accounts for all 109 Records once. The 800 opening entries become 869: 69 additions, 22 substantive updates and one navigation update. All 92 new or modified entries have their mandatory fields, with unique rule titles. |
| Standing State and carry-forward | All 109 Procedure After Action blocks were checked for retained Court matters. The candidate correctly carries sixteen matters: thirteen unchanged inherited matters, Fiore, Arizona, and Alaska's limited retained implementation jurisdiction. No completed lower-court remand is promoted to a new pending Court request. |
| Roster and institutional setting | Nine occupied seats and seniority reconcile to the OT2000 Composition. Thirteen circuit allotments and the standing referral practice agree with the opening setting. |
| Candidate headers and cleanup | The three common publication headers match. Their retained OT1998 cutoff is expressly staged for coordinated advancement at Commit. Three candidates and five pass notes are appropriate before Commit; their deletion and final dossier/index generation belong to Commit. |
| Current workspace consistency | Failed: F1 and F2. |

## Required continuation

Resolve F1 and F2 in an authorized workspace-cleanup task without changing the adjudications or frozen source copies. Rerun the deterministic checks, then conduct the required fresh legal-substance audit against the opening trackers, all Records, final manifest and continuity projections, candidates and public renders. Replace this audit with the resulting findings before any Close Commit. At Commit, advance the three synchronized publication headers together and perform the prescribed publication, volume checks and cleanup.

Only `terms/OT1999/close/AUDIT.md` was created by this audit task.

READY FOR CLOSE COMMIT: NO
