# October Term 1996 - Confirming Close Audit

Audit date: October 21, 2026. Confirming re-audit after the six F9 evidence files were restored in `a22486a7`.

**Result:** F1-F8 remain resolved, and F9 is resolved. The deterministic gate passes. The required fresh legal-substance audit is complete and identifies two remaining Medium discrepancies, F10 and F11, in the proposed Standards and Tests replacement. The term is not ready for the Close Commit.

## Scope and method

The audit applies AGENTS.md Close protocol pass 4 and Engine sections 2, 8, 13-15. It compares the three opening trackers, all 153 Canonical Decision Records and three Admitted Source Records, the final four-file workspace, all three candidate trackers, and all thirteen renders. Records supply authority; renders and candidate trackers are checked against them. Unaffected opening material was checked for preservation, and the earlier law implicated by current-term decisions was reviewed at its actual simulated scope.

The required `python tools/check_term.py OT1996` ran successfully before the fresh substantive review. Additional read-only checks covered the restored evidence, inventory and chronology, vote and join arithmetic, assignment census, local references, commit existence, candidate staging and carry-forwards. Git access was limited to the permitted checker lookups and read-only `git cat-file` operations. No Git mutation was performed.

Fresh legal review was divided into complete event ranges: chunks 1-5 (59 Court events and the three admitted sources), chunks 6-9 (47 Court events), chunks 10-11 (24 Court events), and chunks 12-13 (23 Court events). Each range covered controlling rules and qualifications, proposition-level authority, judgment and opinion coalitions, separate writings, remedies, Justice-specific reconciliation and departures, and the corresponding workspace, candidate and render content. Integration review checked cross-range dependencies and the final Court setting. F10 and F11 received an additional independent challenge and were confirmed.

This review uses the Records' documented source support and reconstruction limits; it does not certify a new full reading of every original petition, trial transcript, joint appendix or administrative record. A targeted primary-opinion check of the historical [Vacco syllabus](https://www.law.cornell.edu/supct/html/95-1858.ZS.html), [Souter concurrence](https://www.law.cornell.edu/supct/html/95-1858.ZC2.html) and [Ginsburg concurrence](https://www.law.cornell.edu/supct/html/95-1858.ZC3.html) confirmed the distinction between the unanimous judgment and the four judgment-only concurrences. Historical material was used for audit comparison, not as replacement simulated law.

Reads were confined to permitted materials. No private `stone/` directory or file named with `MASTER_JURISPRUDENCE` was opened. The deliberate absence of GitHub repository URLs from the published-form trackers is not a defect. No adjudication, candidate, render, workspace projection or published tracker was repaired during this task.

## Prior findings and F9 restoration

F1-F8 remain resolved. The Gaydos holdings and Foreman placement are present; the restored chunk-1, chunk-2, Faragher, Printz and medical-case support artifacts and their operative references resolve; the five corrected durable Record paths remain correct. The current core comparison against the restoration commit found no substantive change reopening those repairs.

F9 is resolved by restoration of all six files at the paths cited by the chunk-1 validation summary:

| Summary line | Restored file under `terms/OT1996/audit/` | Verification |
|---:|---|---|
| 5 | `RESUME_INPUT_HASHES.json` | Present; byte-identical to its `a22486a7` blob. |
| 60 | `CHUNK1_RECORD_CHECKS.json` | Present; byte-identical to its `a22486a7` blob. |
| 61 | `CHUNK1_FINAL_QA.json` | Present; byte-identical to its `a22486a7` blob. |
| 63 | `CHUNK1_CHECK_TERM.txt` | Present; byte-identical to its `a22486a7` blob, including its original encoding. |
| 65 | `CHUNK1_OPERATOR_SUMMARY_CHECK.md` | Present; byte-identical to its `a22486a7` blob. |
| 65 | `CHUNK1_FINAL_ARTIFACT_HASHES.json` | Present; byte-identical to its `a22486a7` blob. |

The restoration commit exists and describes recovery of preserved bytes. The input receipt contains 45 paths: 43 hashes match the current files, while the two entering-law differences are the later Morgan Stanley/Plaut paragraph changes; their historical hashes match the earlier `b1dc4ab` blobs. The final-artifact receipt's seventeen durable Record, freeze and Render Input hashes match current files. Its four workspace hashes identify the historical chunk-1 snapshot, not the completed term's later projections. The restored historical checker log reports success with six warnings and agrees with the summary's source-identifier explanation. These historical receipts were assessed as dated evidence, without rewriting them to claim present-day checks. All six formerly missing references now resolve.

## Deterministic checks

| Check | Result |
|---|---|
| Required checker and opening Holdings synchronization | Pass. Exit 0; all 27 hash-like warnings were inspected and classified as source identifiers, dates, statutory-reference substrings, memorandum numbers or ordinary text, rather than missing actual commits. The checker also validates the synchronized opening Holdings volumes. |
| Inventory, manifest and Records | Pass. 153 inventory Court-event rows reconcile by case, docket, chunk and date with the manifest and 153 Court-event Records. Three legislative source Records bring the total to 156. |
| Render coverage and effective order | Pass. Thirteen renders contain the expected 153 events in the correct effective-date sequences. Same-day processing and assignment order supply no otherwise unestablished substantive dependency. |
| Participation, votes and joins | Pass. 178 directly parsed numeric/named judgment rows reconcile; 41 events with shorthand, conditional, split or differently formatted components received separate review. Quorum, nonparticipation, judgment-only support and proposition-level joins remain distinct. |
| Assignment census | Pass. An independent recount yields 136 signed plenary lead events and 137 author credits: Stone-Zsela 15, Stevens 15, O'Connor 16, Scalia 14, Kennedy 15, Souter 16, Thomas 15, Ginsburg 15 and Breyer 16. Kinman's two delivering authors receive separate credits; Roy's signed summary is excluded; Lynce's signed argued threshold opinion counts. The final Harrison preassignment figures reconcile. Eligibility, coalition membership and fit were reviewed qualitatively, separately from the census. |
| Runtime and public interfaces | Pass. The required runtime splits are fresh; each generated Render Input matches its Record's bounded Public Projection. Event coverage has no missing or duplicate entry. |
| Links, anchors and restoration references | Pass. 2,349 local Markdown links and nine fragments resolve across 195 core files. The supporting-artifact reference review also passes, including the F9 targets. |
| Commit existence and preservation | Pass. Actual cited commit objects resolve. The 195 core files compared with `a22486a7` have no content difference after line-ending normalization. Each of the six restored F9 files matches its committed bytes without normalization. |
| Opening material and candidate accounting | Pass. Opening Holdings material remains preserved in order. The Standards candidate accounts for all 483 opening titles through 442 unchanged entries and 41 replacements, with 99 additions; the accounting covers all 156 Records. F10 and F11 concern the substance of that projection, not missing source-accounting rows. |
| Coordinated candidates and Court setting | Pass for the staged phase. The three common publication header fields match. The nine-Justice OT1997 roster, thirteen circuit allotments and referral practice agree with the governing sources. Standing State contains the authorized setting and docket sections. |
| Open matters | Pass. The manifest and Standing State candidate retain the separate Gaydos certiorari submission, In re Vey, Bryan County/Brown reargument, Vey v. Clinton certiorari, and Alaska's implementing-decree process. No expired deadline alone establishes default or a terminal disposition. |
| Candidate cleanup and publication | Pass for this pre-Commit audit. The three candidates and five pass notes remain staged. Publication, synchronized header advancement, the dossier, generated indexes and subsequent candidate/pass-note removal belong to Close Commit. |

## Fresh legal-substance results

The review found no additional supported discrepancy in the adjudications, proposition-level coalitions, opinion assignments, remedies, historical-departure grounds, final workspace, Holdings candidate, Standing State candidate or public renders. This conclusion follows review of the complete event set, rather than treating the prior deterministic-only audit as a substantive certification.

Material continuity and authority checks included:

- The actual Casey framework remains the governing reproductive-liberty rule in Fargo/Mazurek and is not displaced by the assisted-death decisions. Vacco and Glucksberg preserve five-Justice rationales and four judgment-only concurrences.
- The altered Shaw/Miller/Vera territorial-design rule is applied at its established scope in Lawyer. The remand concerns existing preserved claims and lawful decree authority; neither new injury nor renewed endorsement of the earlier rule is attributed to dissenting Justices.
- The Reyes-Hernandez, Hincapie-Nieto, Salazar-Haro and Kolster sequence preserves provision-specific temporal analysis, the distinction between ordinary review and independent habeas, and the difference between a substantial legal eligibility objection and discretionary reweighing. Lindh's propagation across ten register entries preserves separately timed provisions, capital questions, successive applications and unresolved federal-prisoner questions.
- Plyler retains the original PLRA current-or-ongoing safeguard and distinguishes prospective relief from the actual bounded Morgan Stanley/Plaut reinstatement holdings. Boerne's later treatment limits future State and local RFRA applications without reopening completed judgments or deciding federal RFRA.
- The Andrade, Oncale, Faragher and Harrison sequence preserves actual authority materially aiding harassment, separate discriminatory-causation and environment predicates, record-specific proof and remedy, and the unresolved general preventive-care/nonuse defense. Historical doctrine was not substituted for those holdings.
- Printz's five direct joins in Part I remain distinct from the different five-Justice remand coalition. Souter's fiscal rationale is not converted into majority law or a Marks holding, and ultimate validity and compensation questions remain unresolved.
- The special-consideration Clinton record preserves its component joins, case-specific accommodation, official-function boundary, separate Breyer position and substantive explanations. Its missing downstream stay burden is isolated in F11. The Turner record and render likewise preserve the controlling full-power disposition and both reserved classifications; F10 concerns the register's stale reservation.
- Candidate and render review retained independent alternative holdings, permission-versus-obligation distinctions, statutory exceptions, limiting conditions and operative remedies. Separate positions were not counted as controlling merely because their authors supported a judgment. Documented source gaps and reconstruction premises were not treated as litigant default or new merits findings.

The two unresolved findings below concern the Standards and Tests candidate. They require projection corrections and confirming audit verification before Close Commit; they do not require changing the underlying decisions.

## F10 - Turner reservation is stale in the current-law register

**Severity:** Medium.

**File and line:** `terms/OT1996/close/STANDARDS_AND_TESTS.candidate.md:4609`, within ?Cable-carriage rules and review of legislative predictions.? Related authority and navigation fields are at lines 4601-4611.

**Discrepancy:** The current `Open question` field still says the decision does not finally sustain the provisions. That accurately describes the 1994 disposition, but the March 31, 1997 Record sustains the reviewed general full-power core, 5-4. The later decision leaves the separate low-power eligibility and market-modification classifications unresolved. A current-law reservation cannot leave the full-power disposition open after that adjudication.

**Controlling support:** `terms/OT1996/records/Turner_Broadcasting_System_Inc_v_FCC_merits_1997-03-31.md:338` preserves both excluded classifications; lines 344 and 350 supply the five-Justice preservation/diversity and fit holdings; line 364 states the resulting law. The Standards template's lines 129 and 150 require the open-question field to identify what controlling law still leaves unresolved.

**Exact fix:** Replace line 4609 with:

> **Open question:** The separate low-power eligibility and market-modification classifications remain unresolved. Turner Broadcasting System, Inc. v. FCC, March 31, 1997, Part I, unanimously excludes those questions from its limited review; Parts II-III sustain the reviewed general full-power core, 5-4, on the common preservation-and-diversity rationale. The 1994 four-Justice record-insufficiency explanation remains noncontrolling.

Add the March 31, 1997 Part I authority for the surviving reservations to `Authority by component`, and its natural question-level reference to `Holdings navigation`. Preserve the existing intermediate-scrutiny rule and its 1994 operative date. No new routine-application entry, replacement of the 1994 holding, or adjudicative correction is required.

## F11 - Clinton stay rule omits its conditional applicant burden

**Severity:** Medium.

**File and line:** `terms/OT1996/close/STANDARDS_AND_TESTS.candidate.md:9445`, within ?Presidential civil immunity and case-specific litigation accommodation.?

**Discrepancy:** The current rule requires the applicant to identify a litigation demand and conflict or hardship, but omits the separately retained Landis condition: even a fair possibility that a requested stay will harm the opposing party triggers the applicant's clear-showing burden. No other candidate entry supplies that condition. General references to supported need and competing interests do not state its trigger or proof requirement.

**Controlling support:** `terms/OT1996/records/Clinton_v_Jones_merits_1997-05-27.md:84` states the conditional clear showing of hardship or inequity; lines 88, 94 and 100 expressly retain that rule in holdings IV-V. The corresponding Holdings candidate preserves it at lines 2114 and 8818. The Standards template's complete-current-rule and burden fields, together with AGENTS.md's completeness rule, require the condition to survive projection.

**Exact fix:** In line 9445, after the sentence ending with the plaintiff's timely-adjudication and evidence interests, insert:

> When even a fair possibility exists that a requested stay will harm the other party, the applicant must make a clear showing of hardship or inequity.

Keep that burden limited to a requested stay, retain the existing authority references to Clinton holdings IV-V, and preserve the separate ordinary accommodations for timing, sequence and manner. Do not turn the condition into a general heightened burden for every scheduling request or import Breyer's noncontrolling formulation.

## Operator handoff

Only `terms/OT1996/close/AUDIT.md` is changed as a repository deliverable. It replaces the superseded F9 blocker with restoration verification, completed deterministic and fresh legal-substance audit results, and the two exact candidate corrections still required. Existing CRLF line endings are preserved. Ignored `tmp/` files were used for audit calculations and review extracts. No repair or Close Commit was performed.

READY FOR CLOSE COMMIT: NO
