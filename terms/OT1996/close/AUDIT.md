# October Term 1996 - Close Audit

Audit date: October 21, 2026. This is the pre-Commit audit of the current staged candidates.

**Result:** Eight unresolved findings remain, F1-F8. The term is not ready for the Close Commit. This audit reports defects and makes no adjudicative or tracker repair.

## Scope and audit gate

The required `python tools/check_term.py OT1996` ran first and exited 0 with 27 warnings. Every warning was checked in context: each is a source identifier, date, or substring falsely recognized as a commit hash. None is a missing actual commit reference. The command's read-only Git object lookups were the sole authorized Git use; no separate Git command was run.

The additional deterministic checks did not pass as a set because F1-F8 remain. Under AGENTS.md, Close protocol pass 4, the fresh legal-substance audit starts only after those checks pass. That stage was therefore not begun. This report does not certify the merits, Justice-specific historical departures, legal sufficiency of coalition grounds, opinion-author eligibility or assignment fit, precedent treatment, or remedies. Candidate source-coverage checks below compare existing controlling labels with projections; they do not reconsider an adjudication.

The allowed checker establishes existence of actual cited commit objects, not the truth of lineage content or ancestry. The seven Records carrying specific lineage hashes describe operator-supplied/deferred provenance; this audit adds no claim of independent content verification. Operator provenance verification remains outside the permitted command scope. External source URLs were not refetched. No restricted directory or restricted filename was opened, and no repository file other than this Audit was written.

## Deterministic checks completed

| Check | Result and limits |
|---|---|
| Required checker | Exit 0; 27 false-positive hash warnings classified. Opening Holdings volumes remain synchronized. Canonical naming/interfaces, runtime split freshness, and generated Public Projection identity checks passed. |
| Inventory, manifest and Records | 153 inventory Court-event rows match 153 manifest rows by caption, docket, chunk and date, with 153 distinct Decision Records. Three separately manifested Admitted Source Records bring the total to 156. |
| Render coverage and chronology | All 13 chunk renders and Render Inputs cover the 153 Court events. Event dates agree with Records and manifest; inventory, manifest and render dates are ordered. A completed procedural event was not treated as termination of an underlying pending matter. |
| Participation, judgment and joins | Published numerical judgment rosters reconcile with participation. Record/render topology names and partial-join displays agree. Amchem's nonparticipation and Greene's distinct formal disposition are preserved. These are arithmetic checks, not a legal endorsement of the votes. |
| Assignment arithmetic | Recounted 136 signed plenary lead events and 137 author credits, including the two delivering Justices in Kinman; checked 113 post-revision count statements. Apparent differences are accounted for by later-written, earlier-effective Records and preserved prior assignments. The June 16 refreshed counts have a retained reconciliation receipt. Legal eligibility and fit remain for the gated substantive audit. |
| Frozen interfaces and cutoff fields | All 26 ordinary chunk commitment/reconciliation files exist. Every Decision Record supplies a source/research cutoff. Supporting-artifact losses are separately listed in F3-F7. |
| Links and anchors | Checked 2,345 local Markdown links across 194 core files; all nine explicit fragments resolve. Core render-input, output, workspace and close links resolve. Record links and essential native freeze references expose the missing artifacts in F3-F7; five inaccurate durable-location strings are in F8. |
| Candidate baseline and coverage | All 23,974 opening Holdings lines remain in order in the candidate. Standards contains 442 unchanged, 41 replaced and 99 new entries, with no dropped opening title. Its source accounting covers all 156 Records. The specific Holdings coverage and placement defects are F1-F2. This is not a full doctrinal comparison. |
| Candidate synchronization and setting | The three common draft-header fields match. The next-term nine-Justice roster, all thirteen circuit allotments and unchanged referral practice agree with their governing sources. All three candidates retain CRLF. |
| Open-matter carry-forward | The manifest and Standing State candidate both retain exactly five matters: the separate Gaydos certiorari submission; In re Vey; Bryan County/Brown reargument; Vey v. Clinton certiorari; and Alaska's implementing-decree process. No default or terminal event was inferred. |
| Cleanup and publication stage | Three candidates and five pass notes properly remain before Commit. Their removal, coordinated header advancement, dossier and generated close indexes belong to the later Commit pass. Their present existence and retained synchronized draft cursor are not defects. |

The published-form trackers deliberately omit GitHub repository URLs at the user's standing direction. Their absence is not a finding.

## F1 - Gaydos controlling holdings omitted from candidate Holdings

**Severity:** High. The replacement Holdings would omit law expressly identified as controlling in the canonical Record.

**Files and lines:** `terms/OT1996/close/HOLDINGS.candidate.md:5530` is the fee-relief/filing-control destination, and `:2559` is the extraordinary-writ destination; the missing entry itself has no line. The exclusion is explicit in `terms/OT1996/close/HOLDINGS_PASS1.md:21`. The unresolved coverage question is preserved at `terms/OT1996/close/HOLDINGS_PASS2.md:39` and `terms/OT1996/close/HOLDINGS_PASS3.md:27`.

The controlling source is `terms/OT1996/records/In_re_Gaydos_filing_and_writ_disposition_1996-12-02.md:39`: three labeled holdings begin at lines 41, 51 and 61, with authority at lines 45, 55 and 65 and precedent treatment at lines 71-78. Candidate lines 5635 and 5647 merely cite Gaydos inside later Vey treatment; they do not preserve its own holdings. The pass-1 reason that the event adds no new general rule does not satisfy the Holdings admission instruction: `foundation/templates/HOLDINGS_TEMPLATE.md:31` expressly includes case-specific holdings without a new reusable test.

**Exact fix:** Add the Record's three controlling question blocks to candidate Holdings: financial leave/current-paper review and prospective filing conditions under the existing fee-relief topic, and extraordinary/original relief under the existing extraordinary-writ topic, with natural cross-references between the two Gaydos entries. Preserve the nine-Justice financial and extraordinary-writ-condition coalitions, the eight-Justice writ-reasons and noncriminal-certiorari-condition coalitions, the Chief's disposition-only limits, every operative qualification, the relief actually ordered, and precedent treatment. Derive the text by copying the authoritative passages with a script and adapting only to the Holdings entry form. Do not convert the pending separate petition into a Holdings docket entry or invent a reusable test. Replace pass 1's exclusion with admission and update its coverage totals; resolve the carried coverage question in the pass notes. No change to the adjudication is required.

## F2 - Foreman is filed beneath the wrong Election Law topic

**Severity:** Low. The doctrinal location contradicts the entry's subject and its navigation references.

**File and lines:** `terms/OT1996/close/HOLDINGS.candidate.md:21765` begins the substantive Election Law Foreman entry, inside the political-committee topic beginning at line 21733. Its Federal Courts cross-reference at line 9207 instead identifies Voting Rights Act preclearance. The existing preclearance topic begins at line 21555. The issue is already noted at `terms/OT1996/close/STANDARDS_AND_TESTS_PASS.md:19`.

**Exact fix:** Script-move the complete Foreman block at lines 21765-21803, including its surrounding separator spacing, to the end of the Voting Rights Act preclearance topic immediately before the next topic at line 21697. Preserve the block's bytes and both case cross-references. Keep the separate Federal Courts entry at line 9201. Do not change any holding, coalition, remedy or Standards rule.


## F3 - Chunk 1 validation and stage-support artifacts are absent

**Severity:** Medium. Required durable audit support is missing.

The Records and frozen handoffs point to absent final-validation, source-exposure, repair and resumption evidence. The normal commitment/reconciliation files survive, but these cited support artifacts do not. No retained file was established as an equivalent replacement.

**Missing file:** `terms/OT1996/audit/CHUNK1_FINAL_VALIDATION.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/records/California_v_Roy_summary_review_1996-11-04.md` | 179 |
| `terms/OT1996/records/Caterpillar_v_Lewis_merits_1996-12-10.md` | 126, 202 |
| `terms/OT1996/records/Hopwood_v_Texas_merits_1996-11-25.md` | 18, 177, 183 |
| `terms/OT1996/records/Humane_Society_v_Babbitt_merits_1996-12-09.md` | 120, 196 |
| `terms/OT1996/records/INS_v_Yueh_Shaio_Yang_merits_1996-11-13.md` | 133 |
| `terms/OT1996/records/In_re_Askin_merits_1996-12-09.md` | 191 |
| `terms/OT1996/records/In_re_Gaydos_filing_and_writ_disposition_1996-12-02.md` | 126, 208 |
| `terms/OT1996/records/Lopez_v_Monterey_County_merits_1996-11-06.md` | 108, 162 |
| `terms/OT1996/records/Ohio_v_Robinette_merits_1996-11-18.md` | 117, 169 |
| `terms/OT1996/records/Tyler_Murray_v_Montrose_County_School_District_merits_1996-12-02.md` | 115, 191 |
| `terms/OT1996/records/United_States_v_Jose_summary_review_1996-12-02.md` | 99, 171 |

**Missing file:** `terms/OT1996/audit/CHUNK1_RECONCILIATION_CONTEXT_REVIEW.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK1_COMMITMENTS.md` | 14 |
| `terms/OT1996/freeze/OT_1996CHUNK1_RECONCILED.md` | 12 |

**Missing file:** `terms/OT1996/audit/REPAIRS_ASSEMBLY.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/records/INS_v_Yueh_Shaio_Yang_merits_1996-11-13.md` | 127 |
| `terms/OT1996/records/In_re_Askin_merits_1996-12-09.md` | 185 |

**Missing file:** `terms/OT1996/audit/RESUME_NEUTRAL_A.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK1_COMMITMENTS_A.md` | 5 |

**Missing file:** `terms/OT1996/audit/RESUME_NEUTRAL_B.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK1_COMMITMENTS_B.md` | 7 |

**Missing file:** `terms/OT1996/audit/RESUME_NEUTRAL_HOPWOOD_SOURCE_CHECK.json`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK1_COMMITMENTS_HOPWOOD.md` | 11 |

**Missing file:** `terms/OT1996/audit/RESUME_REPAIRS_MODEL.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK1_COMMITMENTS_REPAIRS.md` | 8 |

**Missing file:** `terms/OT1996/audit/ROY_RECONCILIATION_REPAIR.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK1_RECONCILED_ROY_REPAIR.md` | 5 |

**Exact fix:** Restore each named original artifact at the exact path above from operator-verified preserved bytes, then verify that every listed reference resolves to the receipt or proposal it describes. Preserve the frozen handoffs and adjudications. A generic validation summary is not a substitute for the missing source-specific evidence. If original bytes cannot be recovered, retain this finding and explicitly document the provenance loss before commissioning newly dated replacement checks; do not fabricate or backdate a historical receipt.


## F4 - Chunk 2 validation and chronology support artifacts are absent

**Severity:** Medium. Required durable audit support is missing.

Twelve Records rely on the missing chronology/assignment receipt. The retained chunk-2 validation summary also links to missing identity, control, review, projection and scope results; the summary is not the cited results themselves.

**Missing file:** `terms/OT1996/audit/OT_1996CHUNK2_ASSEMBLY_REVIEW_RESOLUTIONS.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK2_VALIDATION.md` | 9 |

**Missing file:** `terms/OT1996/audit/OT_1996CHUNK2_CHECK_SCOPE.json`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK2_VALIDATION.md` | 23 |

**Missing file:** `terms/OT1996/audit/OT_1996CHUNK2_CHRONOLOGY_ASSIGNMENTS.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK2_VALIDATION.md` | 18 |
| `terms/OT1996/records/Abebe_Jira_v_Negewo_merits_1997-01-14.md` | 159 |
| `terms/OT1996/records/Atherton_v_FDIC_merits_1997-01-14.md` | 121 |
| `terms/OT1996/records/DeAngelis_v_El_Paso_Association_merits_1997-01-06.md` | 163 |
| `terms/OT1996/records/Greene_v_Georgia_summary_review_1996-12-16.md` | 147 |
| `terms/OT1996/records/Grimmett_v_Brown_certiorari_dismissal_1997-01-14.md` | 69 |
| `terms/OT1996/records/MLB_v_SLJ_merits_1996-12-16.md` | 164 |
| `terms/OT1996/records/Ogilvie_v_United_States_merits_1996-12-10.md` | 185 |
| `terms/OT1996/records/Old_Chief_v_United_States_merits_1997-01-07.md` | 188 |
| `terms/OT1996/records/United_States_v_Sahhar_merits_1996-12-16.md` | 205 |
| `terms/OT1996/records/Walmer_v_Department_of_Defense_merits_1997-01-13.md` | 182 |
| `terms/OT1996/records/Walters_v_Metropolitan_Educational_Enterprises_merits_1997-01-14.md` | 155 |
| `terms/OT1996/records/Watts_and_Putra_summary_review_1997-01-06.md` | 180 |

**Missing file:** `terms/OT1996/audit/OT_1996CHUNK2_CONTROL_RECEIPT.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK2_VALIDATION.md` | 9 |

**Missing file:** `terms/OT1996/audit/OT_1996CHUNK2_FINAL_IDENTITIES.json`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK2_VALIDATION.md` | 7, 25 |

**Missing file:** `terms/OT1996/audit/OT_1996CHUNK2_PROJECTION_REVIEW.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK2_VALIDATION.md` | 21 |

**Missing file:** `terms/OT1996/audit/OT_1996CHUNK2_RECORD_CHECKS.json`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK2_VALIDATION.md` | 19 |

**Missing file:** `terms/OT1996/audit/OT_1996CHUNK2_REVIEW_A.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK2_VALIDATION.md` | 17 |

**Missing file:** `terms/OT1996/audit/OT_1996CHUNK2_REVIEW_B.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK2_VALIDATION.md` | 17 |

**Missing file:** `terms/OT1996/audit/OT_1996CHUNK2_REVIEW_C.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK2_VALIDATION.md` | 17 |

**Exact fix:** Restore each named original artifact at the exact path above from operator-verified preserved bytes, then verify that every listed reference resolves to the receipt or proposal it describes. Preserve the frozen handoffs and adjudications. A generic validation summary is not a substitute for the missing source-specific evidence. If original bytes cannot be recovered, retain this finding and explicitly document the provenance loss before commissioning newly dated replacement checks; do not fabricate or backdate a historical receipt.


## F5 - Faragher final-form support is absent

**Severity:** Medium. Required durable audit support is missing.

The assignment account cites a pre-count final-form artifact that is not present at its stated durable path.

**Missing file:** `terms/OT1996/preparation/OT_1996CHUNK13_FARAGHER_FINAL_FORM.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/records/Faragher_v_City_of_Boca_Raton_merits_1997-09-08.md` | 34 |

**Exact fix:** Restore each named original artifact at the exact path above from operator-verified preserved bytes, then verify that every listed reference resolves to the receipt or proposal it describes. Preserve the frozen handoffs and adjudications. A generic validation summary is not a substitute for the missing source-specific evidence. If original bytes cannot be recovered, retain this finding and explicitly document the provenance loss before commissioning newly dated replacement checks; do not fabricate or backdate a historical receipt.


## F6 - Printz final-form and reviewed-proposal support are absent

**Severity:** Medium. Required durable audit support is missing.

The Record cites an absent final-form artifact. Both the embedded and retained postfreeze join audit identify a separate absent proposal as the proposal actually reviewed. Preserve that distinction when restoring the evidence.

**Missing file:** `terms/OT1996/preparation/OT_1996CHUNK13_PRINTZ_FINAL_FORM.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/records/Printz_v_United_States_Mack_v_United_States_merits_1997-06-27.md` | 30 |

**Missing file:** `terms/OT1996/preparation/OT_1996CHUNK13_PRINTZ_NARROW_DISPOSITION_PROPOSAL.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/freeze/OT_1996CHUNK13_PRINTZ_POSTFREEZE_JOIN_AUDIT.md` | 3 |
| `terms/OT1996/records/Printz_v_United_States_Mack_v_United_States_merits_1997-06-27.md` | 427 |

**Exact fix:** Restore each named original artifact at the exact path above from operator-verified preserved bytes, then verify that every listed reference resolves to the receipt or proposal it describes. Preserve the frozen handoffs and adjudications. A generic validation summary is not a substitute for the missing source-specific evidence. If original bytes cannot be recovered, retain this finding and explicitly document the provenance loss before commissioning newly dated replacement checks; do not fabricate or backdate a historical receipt.


## F7 - The shared Vacco/Glucksberg form receipt is absent

**Severity:** Medium. Required durable audit support is missing.

Both Records cite the same absent form-selection artifact. Restoration must supply that original shared receipt, not a newly inferred explanation from the final outcomes.

**Missing file:** `terms/OT1996/preparation/OT_1996CHUNK13_MEDICAL_FORMS.md`.

| File | Line(s) |
|---|---|
| `terms/OT1996/records/Vacco_v_Quill_merits_1997-06-26.md` | 26 |
| `terms/OT1996/records/Washington_v_Glucksberg_merits_1997-06-26.md` | 26 |

**Exact fix:** Restore each named original artifact at the exact path above from operator-verified preserved bytes, then verify that every listed reference resolves to the receipt or proposal it describes. Preserve the frozen handoffs and adjudications. A generic validation summary is not a substitute for the missing source-specific evidence. If original bytes cannot be recovered, retain this finding and explicitly document the provenance loss before commissioning newly dated replacement checks; do not fabricate or backdate a historical receipt.


## F8 - Five Records name nonexistent durable self-paths

**Severity:** Low. Internal location strings disagree with the actual canonical filenames.

Replace only the `Durable location` value on each listed line with the exact repository path in the final column. These are internal clerical corrections; do not rename files or change any Public Projection.

| File | Line | Exact replacement value |
|---|---:|---|


| `terms/OT1996/records/Church_on_the_Rock_v_City_of_Albuquerque_merits_1997-05-27.md` | 115 | `terms/OT1996/records/Church_on_the_Rock_v_City_of_Albuquerque_merits_1997-05-27.md` |
| `terms/OT1996/records/Suitum_v_Tahoe_Regional_Planning_Agency_merits_1997-05-27.md` | 95 | `terms/OT1996/records/Suitum_v_Tahoe_Regional_Planning_Agency_merits_1997-05-27.md` |
| `terms/OT1996/records/United_States_v_Hyde_merits_1997-05-27.md` | 95 | `terms/OT1996/records/United_States_v_Hyde_merits_1997-05-27.md` |
| `terms/OT1996/records/United_States_v_LaBonte_merits_1997-05-27.md` | 111 | `terms/OT1996/records/United_States_v_LaBonte_merits_1997-05-27.md` |
| `terms/OT1996/records/United_States_v_Thomas_merits_1997-05-19.md` | 111 | `terms/OT1996/records/United_States_v_Thomas_merits_1997-05-19.md` |


## Completion requirements

F3-F7 identify 22 absent support artifacts at 58 verified reference locations. F8 identifies five additional inaccurate internal paths. Every source location above was checked against the present file; line numbers refer to this audit's input snapshot.

Resolve F1-F8 in the appropriate authorized repair task, preserve all adjudications and frozen commitments, and rerun the deterministic checks. Then commission the required fresh legal-substance audit across the opening trackers, all Records, final workspace, proposed replacement trackers and renders. Only a clean completed audit can authorize Close Commit; the successful basic checker alone cannot do so.

Operator handoff: the only repository file created by this task is `terms/OT1996/close/AUDIT.md`, to record the audit evidence, unresolved findings and required fixes. No state tracker, candidate, Record, render, freeze artifact, governing file or Git state was modified.

READY FOR CLOSE COMMIT: NO
