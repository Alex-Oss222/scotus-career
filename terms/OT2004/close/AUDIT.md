# October Term 2004 close audit

**Audit date:** November 23, 2026.
**Disposition:** Not ready for Close Commit. Three unresolved projection discrepancies are listed below. The deterministic prerequisite has not passed, so the fresh substantive legal audit has not begun.

## Scope and authority

This audit follows AGENTS.md, Close protocol pass 4, and the Engine's source hierarchy and coordinated-close requirements. The deterministic review covers the OT2004 inventory, 105 Court Records, one Admitted Source Record, ten Render Inputs, ten public renders, runtime freshness, four workspace projections, three staged replacement trackers, close-pass notes, and the opening trackers and institutional sources needed for these checks. Records control over their projections.

The first operation was `python tools/check_term.py OT2004`. It exited successfully with `OK: OT2004; 0 warning(s)`. Its checks include opening Holdings-volume synchronization, runtime-split freshness, Record/Public Projection structure, exact Public Projection/Render Input body identity, manifest-to-input coverage, and recognized commit-reference existence. Its success does not certify the additional checks below or legal substance.

The operator authorized that checker, including its read-only Git object lookups. No other Git command was run. Only this audit file was written. No prohibited directory or prohibited jurisprudence filename was accessed. Sources and adjudications were not edited.

## Unresolved discrepancies

### F1 ? Medium ? Manifest summary contradicts the completed event rows

**File and line:** [terms/OT2004/workspace/manifest.md](../workspace/manifest.md), line 3.

**Evidence and effect:** The summary reports 103 completed scheduled events and two stopped matters. All 105 scheduled rows, lines 15?119, are marked Completed and identify existing Records. Gonzalez at line 108 and McCreary at line 117 have Records and rendered decisions. There is no stopped scheduled row. This is a status projection error, not an unfinished adjudication.

**Exact fix:** Replace line 3 with the following line, derived from its existing text by changing only the completed and stopped counts:

**Status:** Open; 105 scheduled events completed, 0 open, 0 stopped and 0 carried forward. **Scheduled events:** 105 in ten chunks. **Separate unscheduled carryovers:** 3.

Keep the three separate unscheduled carryovers and their operative stages. Change no inventory item, Record, vote, or disposition.

### F2 ? Medium ? Ledger contradicts its declared effective-date ordering

**File and lines:** [terms/OT2004/workspace/ledger.md](../workspace/ledger.md), lines 112?117; ordering declaration at line 3.

**Evidence and effect:** The main eight-column table ends at entry 104, Van Orden, dated June 27, 2005. A separate seven-column Additional completed events table then places Gonzalez, dated June 23, after that June 27 entry, followed by McCreary. Those two rows lack the Effective-date order column. All 106 Records are represented, but the structure and sequence contradict the ledger's declared effective-date/case-name index.

**Exact fix:** Consolidate the two additional rows into the existing table, preserving every Record-derived cell and the history-verification disclosure. Sort all 106 entries by effective date and case name, and renumber the Effective-date order column 1?106. Gonzalez becomes entry 95, between Exxon Mobil v. Allapattah Services and Green Party, in the June 23 group. McCreary becomes entry 102, between Bell v. Thompson and Metro-Goldwyn-Mayer v. Grokster, in the June 27 group. Remove the Additional completed events heading and separate table. This repairs the declared index without claiming repository commitment order was verified. The standard rebuild script invokes additional Git commands and was not run under this task's restriction.

### F3 ? Low ? Continuation projections misstate the current close stage

**Files and lines:** [terms/OT2004/workspace/continuity.md](../workspace/continuity.md), line 7; [terms/OT2004/workspace/neutral-projection.md](../workspace/neutral-projection.md), line 7.

**Evidence and effect:** Both current projection paragraphs state that no term-close pass has occurred. Four Holdings-pass notes, the Standards and Tests pass note, the Standing State pass note, and all three candidate trackers now exist. This is administrative status drift; it changes no judicial chronology or law.

**Exact fix:** In each line 7, replace only the sentence about no term-close pass having occurred with: `The close candidates are staged; completion of the full-term audit and coordinated publication remain pending.` Preserve all other text, including event dates, assignment disclosures, and retained-proceeding statements.

## Deterministic checks completed

| Check | Result and boundary |
|---|---|
| Inventory to manifest | All 105 rows reconcile by original row number, chunk, caption after grant-marker removal, identifier, date, event type, category, and area of law. F1 concerns only the summary. |
| Record and render coverage | 106 Records: 105 judicial events plus the section 703 admitted source. The ten Render Inputs contain exactly the 105 judicial Records, without duplicates, omissions, or extras. The outputs contain 105 corresponding entries in the supplied order, with closing boundaries. Counts by chunk: 13, 11, 5, 7, 11, 9, 8, 11, 15, 15. |
| Effective dates | Render Inputs are ordered within each chunk. The continuity event table contains all 106 Records in effective-date order. Cross-chunk same-day groups remain identified. F2 concerns the ledger. Substantive entering-law use remains unaudited. |
| Judgment arithmetic | 146 numerical Record comparisons and 156 output margin/roster comparisons, supplemented by manual treatment of differently structured components and unpublished tallies, disclosed no additional discrepancy. Devenpeck's reversal/vacatur distinction, Bates's separate warranty instruction, Gonzalez's unanimous classification, and the public dismissals in Howell and Medellin remain distinct. Legal sufficiency of joins and proposition-level authority requires substantive review. |
| Runtime and projection identity | Runtime-split freshness and generated Render Input identity with Record Public Projections passed in the required checker. |
| Local navigation | A bounded scan of 444 Markdown files checked 2,901 local links/fragments. All tested targets in Records, Render Inputs, outputs, workspace, inventory, close candidates/pass notes, and published trackers resolve. External source URL availability was not tested. Copy-navigation exceptions are explained below. |
| Tracker structure | Holdings retains all opening case headings and the same 23 doctrinal-area headings, with 158 added case-area entries. Standards and Tests has 1,149 entries against 1,113 at opening, preserves broad areas, and its pass coverage accounts for all 106 Records. These structural checks do not approve legal content or admission decisions. |
| Standing State and carry-forward | Nine OT2005 opening seats, seniority, thirteen circuit allotments, and the referral practice match governing institutional sources. Five pending original actions are carried: Arizona v. California, Kansas v. Colorado, Nebraska v. Wyoming, Kansas v. Nebraska, and Alaska v. United States. The three unscheduled carryovers and two retained current-term original proceedings are accounted for. Ordinary lower-court remands were not added as pending Supreme Court matters. |
| Staging and cleanup | Three candidates and six pass notes are properly retained before Commit. The dossier, synchronized final publication headers, generated indexes, and post-publication cleanup belong to Commit. Their present absence or provisional status is not a defect. |
| Commit references | The checker recognizes zero commit-reference tokens in the 106 Records and nine pre-existing close Markdown files. Its zero warnings therefore reflects an empty existence-check set, not verification of lineage against history. No missing referenced commit was established. |

## Navigation exceptions and provenance limits

The deliberate absence of GitHub repository URLs from published trackers is not a defect. Unresolved relative links inside preserved freeze and entering-law copies are excluded as directed. Eighty location-relative misses in eleven runtime commitment/reconciliation copies were traced separately: each affected runtime file is byte-identical to its authoritative same-named freeze file, and every target exists relative to that canonical frozen location. The required inputs exist. Two case-index template example links are placeholders, not OT2004 navigation defects.

The no-Git instruction prevents independent repository-history review of lineage content and commitment order. That verification remains with the operator. This audit does not convert an empty commit-token check into provenance certification. No additional approval or Git access was requested.

## Required continuation

Repair F1?F3 in a task authorized to edit the named workspace files, preserving CRLF and all adjudications. Then rerun the deterministic checks and continue the fresh legal audit. AGENTS.md, Close protocol pass 4, states: ?Only after those pass does a fresh AI audit review legal substance.? Accordingly, this pass does not certify legally supported votes, coalition sufficiency, holdings, precedent treatment, remedies, substantive continuity, or Justice-specific historical departures. Prior close-pass reviews do not substitute for the remaining fresh audit.

Only `terms/OT2004/close/AUDIT.md` changed: it records the discrepancies, completed checks, limitations, and remaining prerequisites. No repair, publication, candidate deletion, or repository commit was performed.

READY FOR CLOSE COMMIT: NO
