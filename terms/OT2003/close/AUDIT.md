# October Term 2003 — Term-Close Audit

**Audit date:** November 22, 2026.
**Disposition:** Not ready for Close Commit. Five unresolved findings remain: one high-severity reconciliation/authority-support gap and four low-severity documentation or candidate defects. They are identified individually below. This audit does not change an adjudication, frozen handoff, projection, render, candidate or published tracker.

## Scope, sequence and restrictions

The permitted `python tools/check_term.py OT2003` was run first and returned `OK: OT2003; 0 warning(s)`. The remaining required deterministic checks were completed before fresh substantive review. Their authoritative-file integrity checks passed; the additional pass-note counting discrepancy in F1 does not alter the candidate text or prevent substantive review of the Records.

Fresh audit contexts reviewed all 119 Court events and the December 1, 2003 Rule 53 Admitted Source Record. Coverage comprised chunks 1–3 excluding McConnell (38 Court events plus the source admission), chunks 4–6 excluding Vieth and Martinez (46), chunks 7–8 (32), and a separate review of McConnell, Vieth and Martinez (3). The review compared operative Records, relevant opening law, the final manifest and continuity, the three candidates, and public renders as cross-checks. It assessed controlling authority, material partial joins, remedies, present force, chronology dependencies and Justice-specific historical departures. Repeated kernel/Public Projection text was deduplicated computationally where appropriate.

Source verification was targeted to concrete uncertainties, including the historical Fellers and Kaupp opinions and Souter's Engine Manufacturers dissent. This audit does not claim independent reacquisition of every petition, brief, appendix or historical opinion, or a new adjudication of all inherited prior-term law. Repository-history truth beyond the permitted check remains for the operator: no other Git command was run, and no replacement of a completed adjudication is represented as history-verified here. Prohibited directories and filenames were not accessed.

## Deterministic results

- **Inventory, Records and ledger:** All 119 inventory matters match the manifest by inventory identity, chunk, caption and effective date. There are 120 authoritative Records and 120 ledger links: 119 judicial events and the Rule 53 source admission. The scheduled Court events extend from October 14, 2003 through June 30, 2004. No inventory item or source admission is lost or duplicated.
- **Chronology and coverage:** The effective-order manifest, chunk date ranges and event sequences reconcile. The eight Render Inputs and outputs contain 7, 16, 16, 16, 16, 16, 16 and 16 events respectively. The judicial Public Projections match all 119 generated source-record blocks after ordinary newline normalization. The Rule 53 source is separately accounted for rather than invented as another rendered Court decision.
- **Participation, votes and joins:** All 187 explicit numeric judgment components reconcile to their named supporters and opponents; common-coalition and written-number cases were also checked. Raytheon has seven participants; Olympic Airways, Newdow, Empagran and Intel each have eight. Those exceptions and their named absences reconcile. Record/output judgment and topology numbers agree in substance. In 107 nine-Justice eligibility/pool tables with explicit numeric counts and Yes/No fields, the declared pool matches the eligible minimum-plus-one calculation. Legal eligibility and the task-specific assignment directions were reviewed separately from this arithmetic.
- **Freshness and interfaces:** The permitted checker passes runtime-split freshness, the four-file workspace requirements, Record interfaces, source-record coverage, public-voice checks, and term-opening Holdings volume synchronization. No cited commit-object warning was returned. No commit-like reference occurs in the current-term Records or close files; the result is not a claim to have independently inspected Git history.
- **Candidate integrity:** The opening Holdings content survives in order as an exact byte-line subsequence of the candidate. Its 23 doctrinal areas retain their names and order. The four Holdings passes add 301 primary question blocks, and their coverage reconciles to all 120 Records. The independent Standards review table likewise accounts for 120 unique Records, with 40 classified as adding no reusable instruction. Standards grows from 1,059 to 1,113 entries; the accurate retained/modified counts are stated in F1. Holdings and Standards preserve CRLF; Standing State preserves LF.
- **Navigation:** The structural review checked 2,126 local links across 592 authorized OT2003 Markdown files; canonical and candidate destinations and anchors resolve. Candidate navigation was evaluated at its intended state publication location, substituting the staged Holdings candidate for the future published Holdings destination. External URLs were classified, not universally network-tested. The absence of GitHub repository URLs from published trackers is intentional and is not a finding. Source-relative navigation preserved in freeze/ and entering-law/ copies is exempt as directed. Nine comparable links in byte-identical runtime aggregates resolve from their identified authoritative freeze location and are likewise copied-handoff navigation, not a broken canonical dependency.
- **Carry-forward:** The final manifest and Standing State candidate agree on four pending original actions: Arizona v. California (Fort Yuma proceedings); Kansas v. Colorado (damages calculation and preparation of judgment); Nebraska v. Wyoming (litigation-cost allocation); and Kansas v. Nebraska, with Colorado (model-completion and certification condition). Review of 546 Record headers across OT2000–OT2003 found no later terminal event superseding those pending stages. Demore's remand and Virginia v. Maryland's completed decree do not create additional pending Supreme Court matters. Nine seats, seniority, thirteen circuit allotments and the standing referral practice reconcile.
- **Staging and cleanup:** The three candidates and current pass notes are proper pre-Commit artifacts. Their common publication fields deliberately remain synchronized to OT2002, as the pass notes expressly document. At coordinated publication, all three must advance together to OT2003, processed through June 30, 2004 after all 119 completed Court events, with the Rule 53 admission included in coverage and a common edition. The dossier, generated close indexes, tracker publication and deletion of candidates/pass notes belong to Commit; their present absence or presence is not a premature-cleanup finding.

## Substantive review results

The review did not promote judgment agreement into an opinion join or combine incompatible grounds to create controlling law. In particular, Demore's four-Justice general risk-burden rationale remains distinct from its controlling entitlement and party-specific remedy; McConnell retains provision-specific coalitions and separate payroll, reporting and source rules; Vieth's five direct framework joins remain distinct from Kennedy's noncategorical position; and Martinez preserves the separate Senate proof concession and racial statutory claims. The additional conditional Martinez proposal does not enter current law.

The middle-term review covered the component coalitions and remedies in Banks, Dretke, Groh, Yates, Hood, Benjamin, Till and Thornton, and the relevant chronology and prior-law treatment in Crawford, Locke and McCallum. The late-term review checked all 32 decisions, including Pliler's split remedial rationales, Hamdi's unresolved complete proof allocation, Seibert's direct five-Justice objective rule, and Cheney's five-Justice reconsideration mandate. Candidate text generally preserves these distinctions. The specific exceptions established by this audit are F1–F5 below.

The Rule 53 candidate preserves the December 2003 appointment and review provisions, the twenty-day objection period, and the just-and-practicable transition for pending matters. It does not automatically convert existing appointments or apply district-court rules to Supreme Court original-action masters.

## Unresolved discrepancies

### F1 — Low — Standards pass-note verification counts are inaccurate

**File and line:** `terms/OT2003/close/STANDARDS_PASS.md:9`.

The note reports changes to 46 existing entries, including navigation clarifications, and says 1,013 entries retain their source text. Exact comparison instead yields 1,010 unchanged entries, 47 modified entries retaining the same title, and two renamed/modified entries: 49 changed existing entries in total. There are 54 genuinely new entries, producing the stated final total of 1,113.

The three overlooked navigation-only updates are in Recall reopening completed state-prisoner habeas merits, Invalid aggravators in capital weighing and correction of sentencing error, and Crime innocence as a gateway to otherwise barred habeas claims. Each updates the reference to the renamed punishment-eligibility entry. No missing rule or corrupted candidate entry follows from this count error.

**Exact fix:** On line 9, replace `46 existing entries` with `49 existing entries`, and replace `1,013 unrelated entries` with `1,010 unrelated entries`. Preserve the remaining text and CRLF endings.

### F2 — High — Fellers lacks the required Justice-specific support for its greater doctrinal reach

**Primary file and line:** `terms/OT2003/records/fellers_v_united_states_merits_2004-01-26.md:97`.
**Related locations:** The same Record, lines 91–95, 113–120 and 128; the adopted rule at lines 58 and 228; `terms/OT2003/briefs/OT_2003CHUNK3.md:1723`.

The Record adopts a generally controlling Sixth Amendment causal-independence rule through Stone-Zsela and Stevens, O'Connor, Kennedy, Souter, Ginsburg and Breyer. The Government bears preponderance proof under that rule. The [historical Fellers opinion](https://www.law.cornell.edu/supct/html/02-6320.ZO.html) unanimously left the Elstad-extension question for the court of appeals in the first instance. The reconciliation recognizes the unchanged material record and explains that Cobb's expanded offense boundary does not affect this charged-offense case. It then treats history's failure to decide the competing merits rules as a sufficient reason to retain the six Associates' new rule joins.

The individual rows provide legal arguments for attenuation, but do not establish the concrete changed premise explaining why each of those Justices would decide the historically reserved question now. The actual opening Dickerson, Cobb and Kaupp law, and the [historical Kaupp opinion](https://www.law.cornell.edu/supct/html/02-5636.ZPC.html), support the distinctions discussed in the Record without independently supplying that missing explanation. Engine §7 and the Records instructions require the changed-premise inquiry for a material departure in scope as well as a changed judgment.

The approved neutral brief at line 1723 provides a possible scope distinction: a remand for unadjudicated fruits or harmlessness facts must identify the governing rule. Engine §8's complete-resolution requirement is also relevant. Neither automatically chooses attenuation or establishes the six individual joins. The case index approves Stone's position, not a Fellers non-Stone outcome. This is an unresolved reconciliation and authority-support gap; it is not a finding that attenuation is legally wrong, that the seven-Justice result necessarily changes, or that the unanimous reversal must be disturbed.

**Exact required resolution:** Conduct fresh scoped reconciliation using the neutral packet, actual entering law, frozen non-Stone commitments and historical comparator, without private Stone material. Explicitly evaluate the brief's scope instruction and Engine §8 against each of the six Justices' historical first-instance-remand position and date-eligible commitments. Record the concrete supported changed premise and Justice-specific reason for deciding the rule now. Preserve existing frozen artifacts; any new handoff must truthfully identify its relationship to them. If that support cannot be established, obtain the required authorization for a correction and implement the supported doctrinal scope rather than treating historical silence as affirmative support.

Any authorized substantive correction must propagate through the Fellers Record, `render-inputs/OT_2003CHUNK3.md:912`, the corresponding output entry beginning at `output/OT_2003CHUNK3.md:922`, workspace projections, `close/HOLDINGS.candidate.md:32619`, and `close/STANDARDS_AND_TESTS.candidate.md:8515`. Screen later Fellers references, including Iowa v. Tovar, for actual dependency; do not presume their outcomes change. If fresh review validates the existing rule, the completed reconciliation must still supply the missing support before Close Commit. This audit supplies neither that reconciliation nor a replacement adjudication.

### F3 — Low — Fellers retains a stale placeholder sentence

**File and line:** `terms/OT2003/records/fellers_v_united_states_merits_2004-01-26.md:14`.

The sentence `Scalia and Thomas remain placeholders.` contradicts the completed individual commitments, final topology and published judgment concurrence elsewhere in the same Record.

**Exact fix:** Delete that sentence in the authorized Record cleanup, preserving the other sentences and the file's existing line endings. Do not replace it with a new vote or rationale. The finalized positions are already stated in the Record.

### F4 — Low — Banks Holdings entry corrupts the statutory section symbol

**File and line:** `terms/OT2003/close/HOLDINGS.candidate.md:14511`.

The independent alternative holding prints `?2254(e)(2)` where the cited statute is §2254(e)(2). Its substantive no-applicant-fault ground otherwise matches the controlling Record. A scan of all three candidates found no other comparable literal-question-mark corruption after excluding legitimate questions.

**Exact fix:** Replace `?2254(e)(2)` with `§2254(e)(2)` on line 14511, leaving the rest of the entry and its CRLF endings unchanged.

### F5 — Low — Standards mislabels Souter's Engine Manufacturers writing

**File and line:** `terms/OT2003/close/STANDARDS_AND_TESTS.candidate.md:12347`.

The authority field says `eight direct joins, Souter dissenting`. The canonical Record identifies Souter as concurring in the judgment at `terms/OT2003/records/engine_manufacturers_association_v_south_coast_air_quality_management_district_merits_2004-04-28.md:345`, with the substantive summary at line 378. The judgment is unanimous; eight Justices join the controlling rationale. `terms/OT2003/close/HOLDINGS.candidate.md:66025` correctly preserves that distinction.

**Exact fix:** Replace `Souter dissenting` with `Souter concurring in the judgment only` on line 12347. Retain the eight direct rationale joins, link destination, rule and CRLF endings. No Record or Court vote needs alteration for this candidate transcription correction.

## Disposition and operator boundary

F1–F5 remain unresolved because this task authorizes changes only to this audit. No other discrepancy was established within the completed review. Close Commit must wait for the stated fixes and resolution of F2, followed by verification of the affected projections and an updated audit. The deliberate tracker navigation policy, source-copy link exceptions, staged headers, legitimate pre-Commit candidate files, and operator-reserved Git verification are not additional findings.

Only `terms/OT2003/close/AUDIT.md` is delivered as a repository change. Existing adjudications and all three candidates remain untouched.

READY FOR CLOSE COMMIT: NO
