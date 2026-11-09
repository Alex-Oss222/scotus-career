# October Term 2000 - Close Audit

Audit date: November 9, 2026.

**Disposition:** Three unresolved deterministic discrepancies remain, F1-F3 below. The term is not ready for Close Commit. The required fresh legal-substance review has not begun: the Close protocol permits that stage only after the deterministic checks pass. This report does not certify the adjudications or candidate trackers as substantively audited.

## Scope and restrictions

The review covers the 114 completed events through June 28, 2001, eight chunks, final workspace, generated handoffs and public renders, and the three staged tracker candidates. Records control over projections. All finding locations are repository-relative, with one-based line numbers in the files reviewed.

Only this audit is written in the repository's substantive files. No adjudication, candidate, workspace projection, frozen handoff, or public render is repaired in this task. No direct Git command was executed. The expressly permitted `python tools/check_term.py OT2000` supplied its read-only commit-object checks; repository-history verification and commitment remain with the operator. Forbidden directories and filenames were not accessed.

The absence of GitHub repository URLs in the published trackers is intentional and is not a finding. Unresolved relative navigation inside preserved `freeze/` and `entering-law/` copies is also excluded as directed. Candidate navigation is checked against its intended publication destination; a staged Holdings destination is resolved against `HOLDINGS.candidate.md` where appropriate.

## Deterministic results

- **Term checker:** Passed with two warnings. Both are false commit-reference matches in public-source URLs: `records/Alabama_v_Bozeman_merits_2001-06-11.md:188` identifies a Library of Congress Code document, and `records/Sterling_v_Borough_of_Minersville_merits_2001-04-24.md:247` identifies a Third Circuit amendment. Neither is a Git lineage claim. No Record's opening lineage field contains a commit hash requiring an additional existence check.
- **Inventory, Records, ledger, and renders:** All 114 inventory entries reconcile to 114 manifest completions, 114 Records, and 114 ledger entries, without an omitted or duplicate event. Ledger identity, event, result, and lineage fields match their Records. The eight chunk totals are 12, 15, 14, 15, 14, 15, 14, and 15. Render case coverage, closing markers, and chronology match the generated inputs.
- **Effective dates:** Record headers, filenames, inventory, and manifest agree, allowing the disclosed organizational scheduling annotations. The effective-order review does not equate chronological order with repository commitment order.
- **Freshness and identity:** The term checker verified runtime splits and Record Public Projection/Render Input identity. All eight runtime/frozen commitment pairs and all eight reconciled pairs match byte-for-byte. Additional verification covered 45 chunk-2 handoff hashes, 17 chunk-3 index hashes, and 15 current chunk-8 Record digests. Documented neutral-aggregate role differences are not stale splits.
- **Participation and arithmetic:** All 114 Records were screened, including 87 compact numerical judgment blocks, 55 numerical component rows across 22 table-based decisions, and five actions that appropriately withhold a numerical division. Render checks covered 85 compact divisions and 65 component rows. Named coalitions and stated counts agree; Bush's three-way division is preserved. The inconsistent workspace participation summaries are F1.
- **Assignments:** The opinion-table census yields 103 counted signed plenary lead opinions and 11 excluded events. Final counts are Stone-Zsela 10, Stevens 12, O'Connor 12, Scalia 11, Kennedy 11, Souter 12, Thomas 12, Ginsburg 11, and Breyer 12. Declared eligible sets, balance pools, chosen authors, and opinion tables are internally arithmetically consistent. This does not certify the legal eligibility of a proposed author or historical availability of every prior Record. Actual repository commitment order is expressly unverified at `workspace/ledger.md:3`; operator verification must preserve the rule that a later-added earlier-effective Record does not reopen an earlier committed assignment.
- **Navigation:** The local scan checked 2,049 references across 164 files. Four links fail, all at the single location in F3. All other checked local paths and anchors resolve. The 709 external URL occurrences were distinguished from local references; external availability was not network-tested. No reference-style link or HTML-href gap was found in the checked set.
- **Candidates and carryovers:** The three common publication fields match. Their retained opening cutoff is expressly staged for coordinated advancement at Commit, not represented as an OT2000 publication. The Standing State candidate has nine occupied seats in OT2001 seniority order, thirteen circuit allotments, the carried referral practice, and both Arizona and Kansas. Its Kansas docket row is at line 61. The incomplete workspace summaries are F2. Current candidates and pass notes properly remain until successful Commit; they are not premature-cleanup defects. The opening Holdings' Holding-field text is retained, and the Standards candidate has 940 distinct canonical titles with required core fields in the changed or added sections inspected.

## Unresolved discrepancies

### F1 - Medium - Oakland participation omitted from workspace summaries

**Files and lines:**

| File | Line(s) |
|---|---|
| `terms/OT2000/workspace/manifest.md` | 146 |
| `terms/OT2000/workspace/continuity.md` | 5803, 5822 |
| `terms/OT2000/workspace/neutral-projection.md` | 4599, 4642 |

**Discrepancy:** The participation-exception lists omit Breyer's nonparticipation in United States v. Oakland Cannabis Buyers' Cooperative. The two completed-event summary paragraphs consequently say that all nine participated except in Hatter, New Hampshire, and Pollard. The Oakland Record expressly establishes eight participants and an 8-0 judgment; see `terms/OT2000/records/United_States_v_Oakland_Cannabis_Buyers_Cooperative_merits_2001-05-14.md:8`, `:18`, and `:116`.

**Exact fix:** At each of the three enumerated participation lists, add Breyer's nonparticipation in Oakland Cannabis. At continuity line 5822 and neutral-projection line 4642, add Oakland Cannabis to the exceptions to universal participation. Preserve the existing Hatter, New Hampshire, and Pollard exceptions and the absence of any stated reason. The decision, its eight-person coalition, and the next-term roster require no change.

### F2 - Medium - Kansas omitted from closing open-matter summaries

**Files and lines:**

| File | Line(s) |
|---|---|
| `terms/OT2000/workspace/manifest.md` | 3; carryover table at 137-142 |
| `terms/OT2000/workspace/continuity.md` | 9; open-docket table at 5793-5797; 5959 |
| `terms/OT2000/workspace/neutral-projection.md` | 9; current-public-procedure table at 4631-4636; 5880 |

**Discrepancy:** These closing summaries identify the retained Arizona/Fort Yuma proceeding but omit the still-pending Kansas original action. Kansas's case-specific manifest and procedure rows correctly preserve it, as does `terms/OT2000/close/STANDING_STATE.candidate.md:61`. The controlling Record expressly recommits calculation and preparation of judgment to the Special Master and leaves the action pending at `terms/OT2000/records/Kansas_v_Colorado_merits_2001-06-11.md:437`. The Standing State pass already called attention to this projection omission.

**Exact fix:** Add Kansas alongside Arizona in the current-posture and final open-matter paragraphs at the listed locations. Add a Kansas row to each listed summary table, distinguishing the completed June 11 decision on exceptions from the pending calculation and preparation of judgment before the Special Master under that decision. If the manifest table remains limited by its title to opening Standing State carryovers, broaden the title to include closing open matters. Preserve the count of zero uncompleted scheduled inventory events; a completed event does not close the underlying original action. Retain Arizona's unresolved Fort Yuma work and Fiore's distinction between completed Supreme Court review and lower-court habeas implementation. Invent no deadline, later filing, final award, or new event. The Standing State candidate's two carryovers already require no correction.

### F3 - Low - Four Kansas Record links resolve in the wrong directory

**File and line:** `terms/OT2000/records/Kansas_v_Colorado_merits_2001-06-11.md:227`.

**Discrepancy:** Four relative hrefs point to nonexistent files beside the Record, although their named targets exist in the term's `freeze/` directory. This location is inside `records/`, so the exemption for preserved navigation inside `freeze/` and `entering-law/` does not apply.

**Exact fix:** Prefix each of these four existing hrefs with `../freeze/`, retaining its filename and link label:

- `OT_2000CHUNK7_COMMITMENTS_kansas_colorado_refresh.md`
- `OT_2000CHUNK7_NEUTRAL_KANSAS_REFRESH_RECEIPT.md`
- `OT_2000CHUNK7_NEUTRAL_KANSAS_TYPE_SOURCE.md`
- `OT_2000CHUNK7_NEUTRAL_KANSAS_DATE_SOURCE.md`

Change only the Record's navigation; preserve the frozen targets byte-for-byte. No public projection or adjudicative proposition changes.

## Required continuation

Repair F1-F3 in an authorized task, rerun the deterministic checks, and then perform the fresh legal-substance audit required by the Close protocol. That review remains responsible for the votes' legal support, coalitions, holdings, precedent treatment, remedies, continuity, historical departures, and independent candidate derivation. The source-completeness limitation expressly carried in `close/STANDARDS_AND_TESTS_PASS.md` concerning Children's Healthcare also remains for that substantive review; this gated structural audit neither clears nor adjudicates it.

The operator's repository-history verification remains separately reserved under the no-Git instruction. No tracker publication, candidate cleanup, or Close Commit is authorized by this report.

READY FOR CLOSE COMMIT: NO
