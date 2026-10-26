# October Term 1997 ? Confirming Close Audit

Audit date: October 26, 2026. This replaces the previous audit and includes the fresh legal-substance review that the previous audit did not reach. The repair commit examined is `05903335`.

F-01 through F-04 are resolved. Four discrepancies remain, F-05 through F-08 below. The term is not ready for Close Commit. The structural checker passes, but that result does not cure the candidate, assignment and workspace discrepancies found by substantive review.

Paths and line numbers below refer to the audited files as they stood before this audit was replaced. Unless stated otherwise, paths are relative to `terms/OT1997/`.

## Scope and governing directions

The audit applied the Close protocol, Engine, Render Contract, tracker instructions, Court Composition, approved corrections and the user's October 25?26 close rulings. It reviewed the opening Holdings volumes and continuous view, opening Standards and Tests and Standing State, all 163 current-term Records, the final four workspace projections, all three candidates, and all 13 Render Inputs and renders. Relevant approved Stone positions, frozen commitments and reconciliations were checked against the Records. Records controlled over projections and renders.

The fresh legal review covered every Court action, not a sample: 37 Records in chunks 1?3; 13 in chunk 4; 49 in chunks 5?8; 12 in chunk 9; 36 in chunks 10?12; and 15 in chunk 13, totaling 162 Court-action Records. The admitted PLRA source was reviewed separately. Each review considered jurisdiction and posture, participation, component judgments, proposition-level joins, Stone's approved position and fallback limits, separate writings, effective entering law, precedent treatment, controlling rules and qualifications, remedies, continuity and Justice-specific historical departures. The candidates were compared independently with the opening registers and controlling Records; render and workspace comparisons included both exact projections and substantively rewritten passages.

Only `close/AUDIT.md` was changed. Ignored `tmp/` was used for scratch. No prohibited directory or file was read, listed or searched. No Git command was used except the permitted checker and read-only `git cat-file` lookups. Existing CRLF line endings and UTF-8 encoding without a byte-order mark were preserved. No tracker, adjudication, frozen handoff or render was changed by this audit.

## Verification of the previous findings

| Finding | Verification | Status |
|---|---|---|
| F-01 ? inventory classification and totals | `case-list.md:9` totals 160 scheduled items, with the corrected 151 merits and four dismissal classifications. Ricci is MERITS at `case-list.md:116` and `workspace/manifest.md:98`. The repaired index and manifest agree with the Records and the permitted inspection of repair commit `05903335`. | Resolved |
| F-02 ? W.P. reviewed docket | `case-list.md:85` and `workspace/manifest.md:73` identify Third Circuit No. 96-5416 and preserve the exclusion of the consolidated E.B. component, No. 96-5132. The current Record and repaired inventory agree. | Resolved |
| F-03 ? five designated artifact digests | Every recorded digest for `entering-law/OT_1997CHUNK1_REVALIDATED.md`, `entering-law/OT_1997CHUNK1_B.md`, `entering-law/OT_1997CHUNK1_RYBAR_EFFECTIVE.md`, `freeze/OT_1997CHUNK1_COMMITMENTS_RYBAR.md` and `freeze/OT_1997CHUNK1_COMMITMENTS_B.md` matches that file's current bytes. Matching digests resolve this finding under ruling (1). | Resolved |
| F-04 ? inherited navigation in frozen/derived copies | Applied ruling (2): relative source navigation preserved inside `freeze/` and `entering-law/` is not a close defect. Working navigation in Records, Render Inputs, renders and trackers was checked separately. No link-resolution file is required or created. | Resolved |

The deliberate absence of GitHub repository URLs from the published trackers is not a defect. Ruling (3) was applied: none of the remaining findings requires adding a repository file.

## Deterministic checks

| Check | Result and evidence |
|---|---|
| Required term checker | `python tools/check_term.py OT1997` was run at the start and rerun after the review; exit 0, `OK: OT1997`. Its 16 warnings were examined: they are source identifiers or text fragments matched by the commit heuristic, not missing recorded Git objects. |
| Opening Holdings synchronization | `python tools/holdings_volumes.py check` passed; the doctrinal volumes and continuous compatibility view match. |
| Inventory ? manifest ? Records ? ledger ? render | All 160 scheduled items are completed. There are 163 Records and corresponding ledger entries: 162 Court actions plus the admitted statutory source. All 162 Court actions appear in the 13 chunk render handoffs and renders. The additional Court events and admitted source are not silently counted as new scheduled cases. |
| Effective dates and dependency order | Records were checked by effective date, with lawful treatment of same-day peers, dated statutory change, approved corrections and later-written earlier-effective events. No unsupported same-day merits dependency or automatic reopening of a completed assignment was found. The separate global workspace cursor defect is F-08. |
| Participation, judgments and joins | The nine-Justice roster and applicable participation were checked; 148 numeric judgment rows and 411 topology rows were reconciled, including partial joins, judgment-only agreement, direct cross-writing majorities and noncontrolling separate positions. The complete legal review also checked counts at the proposition level. No vote or join arithmetic discrepancy remains. |
| Runtime freshness | All 13 chunk splits were checked against their approved inputs, including scoped updates and approval records. Superseded position evidence was not substituted for the operative approved position. |
| Public Projection ? Render Input | All bounded Public Projections match their generated handoffs. Chunk coverage, dates, eleven-block order and supplied substantive content reconcile. Render differences were reviewed for preserved legal meaning rather than treated as automatically identical. |
| Working links and anchors | 2,306 working local references across 202 files, including 172 anchor references, were checked; every working target and anchor resolves. The ruling (2) copies were excluded from this defect test. No navigation file was created. |
| Digests and recorded Git objects | Recorded dependency digests and lineage objects were checked. The broad digest review covered 2,406 references to 1,127 targets; differences outside F-03 were evaluated against their actual bounded snapshots, documented updates and resolved stages rather than assuming every historical snapshot must equal the latest file. Required recorded Git objects exist. |
| Assignment counts and pools | Substantive classification review found the Aktepe error in F-06. Mechanical reconciliation alone did not detect the contradiction between its express uncounted threshold status and two later censuses. |
| Candidate preservation and cleanup | All three candidates remain staged. Opening law is preserved except for supported current-term amendments. Candidate headers awaiting synchronized publication and temporary pass notes awaiting Commit cleanup are proper at this stage; deleting them now would be premature. |
| Open matters and next-term setting | The 160 scheduled entries are complete. The 14 separately pending Court stages retain their conditions and are carried forward; completion of their underlying review does not invent a later compliance event. The two reserved OT1998 intake matters are preserved separately. Candidate Standing State contains the next-opening roster, seniority, circuit allotments, standing referral practice and permitted docket entries, without a positions/history register. Its roster and allotments agree with Court Composition. |

## Fresh legal-substance review

The review found no unsupported judgment, controlling coalition, adopted legal rule, merits remedy or Stone-position substitution requiring correction. It checked the actual opening law and earlier effective current-term law rather than treating historical outcomes as governing. Historical departures were assessed for concrete changed premises and the affected Justice's own commitments; differences in authorship or a narrower common opinion were not themselves treated as a changed legal vote.

The review specifically preserved distinctions that are easy to lose in consolidation: threshold decisions versus merits decisions; discretion versus commands; different statutory exclusions; judgment-only fallback versus rationale joins; independent alternative holdings versus a nonexistent narrowest-ground synthesis; and remand permission versus an adjudicated entitlement. The fractured decisions and their separate writings reconcile to the controlling propositions. The PLRA source's effective date and application to pending proceedings were checked against the enacted source without inventing a judicial disposition. Approved corrections, including the final Waste Management position and the updated chunk-13 positions, are reflected in the controlling Records and their substantive projections.

The remaining defects concern the exact publication of candidate qualifications and text, the accuracy and completeness of internal assignment accounting, and the final workspace's global completion description. They are set out below for correction in existing files.

## Remaining discrepancies

### F-05 ? Low ? Two corrupted characters in the Standards and Tests candidate

**Files and lines:** `close/STANDARDS_AND_TESTS.candidate.md:6966` and `:11098`.

**Discrepancy:** Line 6966 contains `Endangered Species Act?s harm prohibition`; the question mark corrupts the possessive in the named related rule. Line 11098 starts the Bestfoods rule with `For ?107(a)(2)`, corrupting the statutory section sign. The controlling source text is unambiguous.

**Exact fix:** At line 6966 replace `Act?s` with `Act?s`. At line 11098 replace `?107(a)(2)` with `?107(a)(2)`. Preserve the surrounding rule, qualifications and line endings. No adjudication or new file is needed.

### F-06 ? Moderate ? Aktepe incorrectly counted, inflating Kennedy's totals and narrowing eligible pools

**Controlling classification:** `records/aktepe_v_united_states_merits_1998-03-10.md:71` expressly classifies its signed nonjusticiability opinion as an uncounted threshold opinion under Engine ?8. Plenary review does not make it a merits lead. The permitted `git cat-file` inspection of the same Record at `23fe5916ecd2` confirms that this classification was already present; this is not an omission explained by a later-written earlier-effective Record.

**Erroneous census locations:**

| Existing file | Lines | Exact correction |
|---|---|---|
| `freeze/OT_1997CHUNK8_ASSIGNMENT_BASELINE.md` | 74; Kennedy total at 15 | Exclude Aktepe from counted merits leads; Kennedy 8 ? 7. |
| `freeze/OT_1997CHUNK8_ASSIGNMENT_CURRENT.md` | 74; Kennedy total at 15 | Exclude Aktepe from counted merits leads; Kennedy 9 ? 8. |
| `freeze/OT_1997CHUNK11_PRIOR_ASSIGNMENTS.md` | 84; Kennedy total at 17 | Replace its counted-merits classification with uncounted threshold status; Kennedy 12 ? 11. |
| `freeze/OT_1997CHUNK11_PRIOR_ASSIGNMENTS.json` | 2516?2517; Kennedy total at 7 | Correct classification and set `counted` to false; Kennedy 12 ? 11. The copied source at line 2511 already expressly says uncounted and should remain accurate to that source. |

**Affected Record annotations:** Every row below requires the stated Kennedy count correction. Where indicated, add Kennedy to the eligible balance pool at the specified line; do not alter the other eligible names merely because this one count changes.

| Record | Count line | Kennedy count: recorded ? correct | Pool correction |
|---|---:|---|---|
| `records/benjamin_v_jacobson_merits_1998-05-07.md` | 49 | 8 ? 7 | No membership change. |
| `records/bronx_household_of_faith_v_community_school_district_no_10_merits_1998-05-11.md` | 49 | 8 ? 7 | No membership change. |
| `records/rice_v_paladin_enterprises_inc_merits_1998-05-14.md` | 47 | 8 ? 7 | No membership change. |
| `records/arkansas_educational_television_commission_v_forbes_merits_1998-05-18.md` | 47 | 9 ? 8 | Add Kennedy at line 57. |
| `records/bousley_v_united_states_merits_1998-05-18.md` | 37 | 9 ? 8 | No membership change. |
| `records/montana_v_crow_tribe_of_indians_merits_1998-05-18.md` | 39 | 9 ? 8 | Add Kennedy at line 39. |
| `records/ohio_forestry_association_inc_v_sierra_club_threshold_1998-05-18.md` | 26 | 9 ? 8 | Add Kennedy at line 26. |
| `records/stewart_v_martinez_villareal_threshold_1998-05-18.md` | 26 | 9 ? 8 | No membership change. |
| `records/textron_lycoming_reciprocating_engine_division_v_united_automobile_workers_threshold_1998-05-18.md` | 28 | 9 ? 8 | Add Kennedy at line 28. |
| `records/gavin_v_branstad_merits_1998-05-21.md` | 47 | 9 ? 8 | Add Kennedy at line 47. |
| `records/united_states_v_thompson_merits_1998-05-21.md` | 49 | 9 ? 8 | Add Kennedy at line 49. |
| `records/forney_v_apfel_threshold_1998-06-15.md` | 26 | 12 ? 11 | Add Kennedy at line 26. |
| `records/hohn_v_united_states_threshold_1998-06-15.md` | 28 | 12 ? 11 | Add Kennedy at line 28. |
| `records/pennsylvania_department_of_corrections_v_yeskey_merits_1998-06-15.md` | 26 | 12 ? 11 | Add Kennedy at line 26. |
| `records/phillips_v_washington_legal_foundation_merits_1998-06-15.md` | 26 | 12 ? 11 | Add Kennedy at line 26. |
| `records/zeran_v_america_online_inc_merits_1998-06-15.md` | 150 | 12 ? 11 | No membership change. |
| `records/caron_v_united_states_merits_1998-06-22.md` | 141 | 12 ? 11 | Add Kennedy at line 143. |
| `records/gebser_v_lago_vista_independent_school_district_merits_1998-06-22.md` | 259 | 12 ? 11 | No membership change. |
| `records/pearson_v_hines_merits_1998-06-22.md` | 26 | 12 ? 11 | No membership change. |
| `records/pennsylvania_board_of_probation_parole_v_scott_merits_1998-06-22.md` | 26 | 12 ? 11 | No membership change. |
| `records/united_states_v_bajakajian_merits_1998-06-22.md` | 28 | 12 ? 11 | No membership change. |
| `records/wisconsin_department_of_corrections_v_schacht_threshold_1998-06-22.md` | 26 | 12 ? 11 | No membership change. |
| `records/swidler_berlin_v_united_states_merits_1998-06-25.md` | 26 | 12 ? 11 | No membership change. |

**Additional relative-count explanations:** In `records/benjamin_v_jacobson_merits_1998-05-07.md:61`, Kennedy has the same seven-count total as Scalia, Breyer and Thomas, not one more. In `records/bronx_household_of_faith_v_community_school_district_no_10_merits_1998-05-11.md:61`, Breyer and Kennedy both have seven, so Breyer does not have one fewer. In `records/rice_v_paladin_enterprises_inc_merits_1998-05-14.md:59`, Stone-Zsela and Thomas are equal-count alternatives to Kennedy at seven, not lower-count alternatives.

**Exact fix and effect:** Correct the four existing census artifacts, the 23 Record count annotations, the 11 omitted pool memberships and the three false comparative statements. Reconcile any dependent aggregate total and recorded digest of an edited artifact through the existing files. Reassess the affected assignment explanations against the complete corrected pools and Engine ?8's concrete-fit rule, preserving the frozen grounds and joins. Every chosen author remains eligible and within the corrected pool; the eligible minima do not change. The error therefore does not itself establish that any author must change, and it supplies no basis to rewrite a judgment or holding. Existing fit grounds must be evaluated with the corrected counts rather than preserved on a false arithmetic premise. Any actual change to a completed adjudication would require the ordinary authorized-correction procedure; this audit makes none. No additional repository file is needed to correct the identified accounting and explanation defects.

### F-07 ? Moderate ? U.S. Shoe candidate exclusions lack their operative predicates

**Files and lines:** `close/HOLDINGS.candidate.md:10693` and `close/STANDARDS_AND_TESTS.candidate.md:1957`.

**Discrepancy:** Both entries refer to ?specified? antidumping/countervailing exclusions without supplying which determinations are excluded. They also abbreviate the distinct Tariff Act ?305 exclusion. The source Record provides the terms at `records/united_states_v_united_states_shoe_corp_merits_1998-03-31.md:30`, repeated in its Public Projection at line 131. The abbreviated candidates do not meet the express completeness rule and can be read as excluding those fields categorically.

**Exact fix:** In each existing candidate paragraph, state the ?1581(i) exclusion for antidumping/countervailing determinations reviewable by the Court of International Trade or designated binational panels, and separately identify ?1581(j)'s exclusion for actions under Tariff Act ?305. Preserve that neither exclusion covers this levy claim and that residual jurisdiction does not cure a missed protest deadline where the protest channel actually governs. Keep the two statutory provisions and their predicates distinct, using the controlling Record's complete formulation. This is a candidate-completeness correction; no new holding, adjudication or file is required.

### F-08 ? Moderate ? Final workspace global scope and continuation cursor remain at chunk 12

**Files and lines:**

| Existing file | Stale global count/scope | Stale latest date | Stale continuation cursor |
|---|---:|---:|---:|
| `workspace/continuity.md` | 15370 | 15372 | 15374 |
| `workspace/neutral-projection.md` | 15582 | 15584 | 15586 |

**Discrepancy:** These global source-boundary paragraphs still say 147 Court-action Records, identify chunk 12 as the latest completed group, give August 17, 1998 as the latest covered event, and identify Clifton/OT_1997CHUNK13 as unresolved and next for processing. They conflict with the final manifest and with the chunk-13 material actually present in both projections. These are current global statements, not bounded historical chunk summaries. No chunk-13 holding was lost: the substantive projections are present.

**Exact fix:** Update the two global scope paragraphs to 162 Court-action Records, including the 15 completed chunk-13 events, and describe the copied substantive coverage through all 13 chunks rather than singling out chunk 9 as the apparent completed projection. Preserve the admitted statutory source separately. Change the latest covered Court event date to September 28, 1998. Replace the Clifton/next-chunk/next-eligible continuation statements with completion of all 160 scheduled items and no remaining scheduled item or unprocessed OT1997 chunk. Preserve the separately pending stages, their conditions, the opening public state, record-specific cutoffs and the limitation that the projection is not an independent external-event sweep. Do not erase legitimately bounded earlier status summaries or close a pending stage merely because its scheduled review is complete. Only the existing two projection files need correction.

## Disposition

F-01 through F-04 are resolved. F-05 through F-08 remain open. All identified repairs can be made within existing files; no new remediation file is proposed. Close Commit must wait for those corrections and confirmation of their consistency. This audit changes no adjudication and publishes no candidate to `state/`.

READY FOR CLOSE COMMIT: NO
