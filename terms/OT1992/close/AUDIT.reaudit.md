# October Term 1992 — Close re-audit

**Audit date:** September 17, 2026.  
**Result:** **Not ready for Commit.** Seven original findings are resolved; findings 4, 7 and 8 are only partly resolved. Four additional discrepancies are reported below.  
**Scope:** Report only. No candidate, adjudication, workspace, Render Input, public render or opening tracker was changed.

This report supplements the preserved [original audit](AUDIT.md). Its finding numbers retain that audit's numbering; new findings start at 11. It is the current assessment of the attempted repairs, not a replacement adjudication. Existing close files remain unchanged.

The examined repository revision was `0a0313c` (candidate rewrite), following `3cc14e4` (Demos/Moreau corrections) and `f032ef1` (Blair corrections). The original audit is preserved at `956602f`. These are existing history references, not commits made by this pass.

## Verification of all ten original findings

| Finding | Result | Evidence and remaining issue |
|---|---|---|
| 1. Schaefer | **Resolved** | Both damaged Holdings sentences now include “entered.” Standards states both sentence-six routes: the Secretary's pre-answer good-cause motion, and new material evidence with good cause for its earlier omission. Proper entry, the then-effective appeal period, retained jurisdiction and the Hudson limits remain distinct. |
| 2. Forfeiture enactment | **Resolved** | Standards now identifies Pub. L. 102-550, §1521, matching the October 28 Admitted Source Record. The effective date, protective-order obligation on motion and unresolved application to earlier events are unchanged. |
| 3. Dunnigan | **Resolved** | Standards separately states constitutional permission and the applicable Guideline's mandatory adjustment after independent perjury findings. It no longer calls the adjustment constitutionally required. |
| 4. Hartford qualification | **Partly resolved** | Standards now supplies the export alternative, claim connection and export-only injury limit while reserving applicability. The record's entering-law account still uses the incomplete “specified U.S. export effect.” See the remaining scope below. |
| 5. Blair carryover | **Resolved** | Blair is removed from Standing State. The eight supported carried matters remain: Zatko and companions, Wyoming, Reynolds, Grubbs, Martin No. 92-5618, Louisiana, Delaware and Nebraska. Blair's completed application is not confused with continuing proceedings below. |
| 6. Demos reservations, precedent and form | **Resolved as originally specified** | Record and input select full form; the public entry has both required tables. Input and render now expressly reserve both a universal prior-warning requirement and categorical invalidity of prospective restrictions, and include Denton's limited treatment without importing its statutory screening framework wholesale. The fee/restriction votes remain unanimous; the certiorari poll is not published. Additional projection omissions are identified in finding 14. |
| 7. Moreau alternative | **Partly resolved** | The input and render now preserve individual “agreements or understandings.” The Standards current rule still says only individual subsection (ii) “agreements.” |
| 8. Explanations and handoff | **Partly resolved** | The three previously short record explanations now meet the 120–200-word requirement, and Moreau's no-presumed-consent statement is restored downstream. The input Holdings blocks still do not carry the record's controlling-holding content unchanged. |
| 9. Blair authority and public source note | **Resolved as originally specified** | The record and public entry now label the tie's legal effect and individual positions as nonholdings; both workspace assertions that Blair adds a holding are removed. The public Source Notes no longer describe historical-vote reconciliation. No stay, vote or Herrera rule changes. The separate new input-interface defect is finding 12. |
| 10. Publication navigation | **Resolved for this workspace** | All local candidate file targets and heading anchors resolve both from `close/` and under a prospective unchanged copy into `state/`. Absolute workspace paths avoid the earlier relative-path failures. This validates the specified local publication, not portability to another checkout or host. |

## Original findings still open

### 4. Hartford: the candidate is complete, but its controlling source still contains the identified omission

**Locations:** [Standards, American-market effects and asserted foreign-law permission](STANDARDS_AND_TESTS.candidate.md#american-market-effects-and-asserted-foreign-law-permission); [Hartford record, Participation and entering law](../records/Hartford_Fire_Insurance_v_California_merits_1993-06-28.md), line 29.

The candidate now identifies the affected United States exporter, preserves paragraph (2)'s connection between the qualifying effect and the claim, and states the final export-only injury limitation. Its added [statutory citation](https://www.law.cornell.edu/uscode/text/15/6a) supplies those terms and identifies the 1982 enactment. The candidate does not decide the reserved applicability question or create a new comity rule.

However, the original finding expressly identified the same incomplete alternative in the record. That record is byte-identical to the previously audited version and still says “specified U.S. export effect” without supplying the specification. A downstream candidate rewrite does not repair that source entry under the completeness rule. Complete the record's existing statutory account, with event-eligible source support and correction provenance, or explicitly resolve the source omission. This is not a request to reconsider the foreign-effects holding or its coalition. The existing input and render state the reserved holding and its domestic-effects application; they do not themselves reproduce the defective export shorthand.

### 7. Moreau: Standards still drops “or understandings”

**Location:** [Standards, Public-sector compensatory time and legally capable representatives](STANDARDS_AND_TESTS.candidate.md#public-sector-compensatory-time-and-legally-capable-representatives), current rule, line 2186. **Source:** [Moreau record](../records/Moreau_v_Klevenhagen_merits_1993-05-03.md#the-later-hire-component-individual-agreements-where-no-representative-could-bind).

The later-hire sentence still permits individual subsection (ii) “agreements instead of losing compensatory time entirely.” It must retain the alternative “agreements or understandings.” The earlier-hire sentence's use of “agreement or understanding” does not state the separate later-hire route. The record, Holdings, corrected input and corrected public holding all preserve the alternative; the defect is confined to this Standards formulation.

### 8. Demos and Moreau: sufficient source length, but the required unchanged handoff is still missing

**Locations:** Both records' Law of the decision sections; Demos's Holdings block in [chunk 4 input](../render-inputs/OT_1992CHUNK4.md); Moreau's Holdings block in [chunk 6 input](../render-inputs/OT_1992CHUNK6.md). Cross-checks: [chunk 4 render](../output/OT_1992CHUNK4.md#demos-v-storrie-no-92-6846) and [chunk 6 render](../output/OT_1992CHUNK6.md#moreau-v-klevenhagen-no-92-1).

Whitespace-delimited counts of the controlling-explanation paragraphs are:

| Proposition | Record | Input | Public render |
|---|---:|---:|---:|
| Demos, current filing | 171 | 129 | 129 |
| Demos, prospective restriction | 199 | 129 | 129 |
| Moreau, earlier hires | 185 | 183 | 183 |
| Moreau, later hires | 175 | 175 | 175 |

All now satisfy the length range. Length alone does not satisfy AGENTS.md's instruction to carry the controlling-holding section into the input Holdings block unchanged. All four source explanations still differ from their input paragraphs. Equal word counts do not establish equality: the later-hire input substitutes “state law” for the record's “Texas law.” The earlier-hire paragraph also changes wording. Demos is materially abbreviated: its prospective explanation loses the closing reservation about future records that could support a different restriction, and its first explanation omits the express distinction between clearing the filing threshold and justifying relief or plenary review. Some limits survive elsewhere, but the handoff remains incomplete.

The source holding formulations and precedent-treatment content must likewise be preserved, rather than merely lengthening the input summaries. Moreau's later-hire precedent line, for example, drops the record's express limitation to the two routes presented. Repair the input from the corrected record, then project the public entry faithfully. No additional record padding or new judicial reasoning is needed to satisfy this remaining finding.

## Additional discrepancies

### 11. The latest corrections have no corresponding record lineage or handoff-metadata update

**Locations:** Lineage, audit annex and durable-commitment sections of [Demos](../records/Demos_v_Storrie_fee_motion_1993-03-08.md), [Moreau](../records/Moreau_v_Klevenhagen_merits_1993-05-03.md) and [Blair](../records/Delo_v_Blair_application_to_vacate_stay_1993-07-21.md); chunk 4, 6 and 11 input metadata; [workspace](../workspace.md).

Demos and Moreau still call themselves initial version 1.0 records and describe replacement of stopped placeholders, even though `3cc14e4` revised already completed records to answer this audit. Blair retains version 2.0 and describes only the earlier correction from version 1.0, not the later `f032ef1` correction to its authority labels. The latest corrections are absent from their lineage lines and audit annexes. Input chunk metadata is unchanged from the original audit revision. Workspace changes address two Blair authority sentences but do not record the new correction lineage.

Repository history preserves the earlier bytes, which is useful and verified; it does not replace the required in-record identification of what was corrected, versions and commit references. Add accurate provenance for these already-authorized corrections and synchronize the input metadata and workspace references. Existing historical versions and corrective commits are available; do not invent a commit for unpublished work, and do not publish workflow provenance in the public renders. This finding concerns traceability, not authorization to change votes.

### 12. Blair's Render Input violates both the form rule and the eleven-block interface

**Location:** [Chunk 11 input](../render-inputs/OT_1992CHUNK11.md), Blair Event at line 121 and the sixth block at line 146.

The Event still specifies “Render form: compact” because the Court is equally divided, with no majority opinion. Those are express grounds requiring **full** form under AGENTS.md. The public entry already has the Judgment and Opinion Topology tables; its existing structure does not cure the contradictory input instruction.

The recent correction also renamed the required sixth input block from `Holdings` to `Legal Effect (No Controlling Holding)`. Engine §13 requires the eleven exact block names for every completed event, including nonprecedential actions. Keep `Holdings` as the interface name and state within it that there is no controlling holding. The public render may retain its accurate Legal Effect heading. Neither repair should turn the tie into precedent or change the disposition.

### 13. Demos and Moreau are missing from the working ledger and cumulative Current Law

**Locations:** [Workspace, Term Working Ledger index](../workspace.md#term-working-ledger-index), lines 156–298; [Current Law](../workspace.md#3-current-law), lines 310–4366; [Current-Term Neutral Projection](../workspace.md#current-term-neutral-projection).

Both records appear in the manifest and later procedural-stage bullets, and the Continuity Note says they “remain corrected.” Neither record has an entry in the actual Term Working Ledger index. Their controlling propositions are also absent from cumulative Current Law: there is no Demos filing-specific application/reservation account and no Moreau §207(o) transition or later-hire rule. Searches for the captions, §207(o), compensatory time and official interference confirm the omission; this is not an alternative title hiding the entries. The neutral projection instructs continuation to use that incomplete cumulative section.

Engine §§2 and 12 require the durable records in the ledger and a complete cumulative law projection. Add the existing completed events in commitment order with their effective dates and correction provenance, and project their recorded rules and limits into the cumulative law section and neutral continuation interface. No new adjudication or chronology-cursor advance is required. The candidates already contain their holdings; this is a workspace-completeness defect, not a finding that the cases were never decided.

### 14. Demos's public entry still omits supplied event and source particulars

**Locations:** Demos Event and Source Notes in [chunk 4 input](../render-inputs/OT_1992CHUNK4.md), beginning line 630; corresponding [public entry](../output/OT_1992CHUNK4.md#demos-v-storrie-no-92-6846), beginning line 504.

The new tables cure finding 6's full-form defect. The public entry nevertheless omits the supplied statement that there was no oral argument, the reporter locator 507 U.S. 290, the Ninth Circuit locator 962 F.2d 13 and May 11, 1992 date, and the supplied petition/lower-disposition source support and public source qualification. These details are present in the input but not in that entry or its chunk chronology row. Restore the supplied public chronology and source information under the Contract's preservation rule; no new research or invented argument date is needed. This was not introduced by the latest correction, but remains a newly identified projection discrepancy.

## Term-wide checks and conservation

The re-audit compared the changed artifacts in full against the original-audit revision and repeated extraction, coverage, header, anchor, duplication and source-preservation checks across the term. SHA-256 comparison with the original audit's 161-file snapshot identified exactly thirteen changed files: three records, their three inputs and three renders, three candidates, and the workspace. The remaining recorded source/candidate files are unchanged. Prior substantive findings for those unchanged materials were used as the re-audit baseline, not represented as a new adjudication or fresh historical-source review.

- All 126 record files remain present: 123 Court-event records and three admissions. Every file is referenced somewhere in the final workspace; finding 13 distinguishes that weaker coverage check from actual ledger completeness.
- Eleven public chunks contain 123 case entries and 123 closing lines: twelve entries in each of chunks 1–10 and three in chunk 11. All record-to-public-entry mappings remain accounted for. The three admissions appropriately have no public decision entries.
- Only the Demos, Moreau and Blair event blocks changed in the affected input/render chunks. Other event blocks remain identical after line-ending normalization. No vote, disposition, author or named coalition changed in those repairs.
- The three candidate header values agree: last completed term **1992**; processed through **July 26, 1993, after DeBoer v. DeBoer, No. A-64.**; edition **September 17, 2026**.
- The opening trackers remain unchanged. Every substantive opening Holdings paragraph survives. There are 232 added Holding/Independent alternative holding fields and no exact duplicate holding text; Standards retains 206 distinct rule titles without duplicates. The source-comparison exceptions for Crosby's spacing and Parke's combined factual-review paragraph remain harmless and unchanged.
- The candidate rewrite's nonnavigation changes are limited to the two Schaefer Holding repairs, the four identified Standards repairs and Hartford source citation, and removal of the Blair docket row. It did not repair the Moreau Standards omission.
- Standing State contains the proper OT1993 roster and seniority, thirteen August 10 circuit allotments, unchanged referral practice and eight carried matters. White's retirement and Ginsburg's prospective accession remain distinct. Ordinary lower-court remands do not become retained Supreme Court proceedings.
- No additional controlling holding was lost or noncontrolling rule promoted by the corrections. The prior audit's reviewed fracture boundaries and independent alternative holdings remain unchanged. Blair remains a specially authorized nonprecedential disposition entry in Holdings and supplies no Standards rule.

Working evidence is in `tmp/reaudit1992/`: `before.json`, `changes.json`, `checks.json`, `bulk-checks.json`, `coverage.json`, `delta.json` and `final-integrity.json`. The checking scripts also reside under `tmp/`. Mechanical checks identify mismatches; the legal and procedural conclusions above do not follow from string comparison alone.

This pass consulted the candidate's Cornell statutory link to check what its cited page supplies. Attempts to retrieve separate official HTML corroboration did not succeed; no historical-source recovery or new admitted source is certified. Existing underlying-record limits, including Blair's unrecovered affidavits, remain disclosed. No historical vote or substantive legal rule was independently reconstructed.

## Commit condition and authorized boundaries

Do not perform the Commit pass while findings **4, 7, 8 and 11–14** remain unresolved. Correct the specified candidate, record/projection, provenance and workspace defects in authorized passes, then verify the resulting set together. Findings marked resolved above need not be reopened unless those later repairs affect them.

The only durable file written by this pass is `terms/OT1992/close/AUDIT.reaudit.md`; the original audit and all candidates are preserved. Scratch files were written only under `tmp/`. No file under foundation, stone, state, OT1992 briefs, runtime, records, render-inputs or output was modified, and the workspace was not modified. Git was used only for read-only status/history/diff inspection. No git commit, checkout, branch or push command was run. No Term-Close Dossier or tracker replacement was performed.
