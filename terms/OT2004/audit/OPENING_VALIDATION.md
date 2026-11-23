# OT2004 Opening Validation

**Task:** Open October Term 2004.  
**Opening state:** Before Leocal v. Ashcroft, No. 03-583, scheduled for 2004-11-09.  
**Adjudicative effect:** None. All 105 scheduled events remain open; three unscheduled originals remain open separately.

## Published opening baseline

The published Holdings, Standards and Tests, and Standing State identify OT2003 as the last completed term. Their identical processed-through statement is June 30, 2004, after all 119 completed OT2003 Court events and the admitted Rule 53 amendment effective December 1, 2003. Their common edition is November 22, 2026. The doctrinal index and all 23 volume headers match that publication triplet.

`python tools/holdings_volumes.py check` passed: the 23 doctrinal volumes and continuous compatibility view are synchronized. Standing State identifies OT2004 as the opening term. The case index's June 30, 2004 legal baseline agrees. The repository trackers control any supplied descriptive reference to a different source copy.

The Composition register and Standing State agree on nine occupied seats and seniority: Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. No vacancy or oath-date condition applies. The August 3, 1994 circuit allotments agree in both sources, and the standing referral practice is carried into the workspace from the saved Standing State text.

## Inventory, intake and carryover checks

The source index has 105 distinct rows, numbered 1–105, in ten chunks. All eight source fields are nonempty. Dates are valid and nondecreasing from 2004-11-09 through 2005-06-27. The direct manifest check compares every row's number, chunk, caption, docket or citation, event date, unchanged event type, category and area of law, preserving source order. Only the trailing caption convention ` +` is removed; its granted-matter meaning is recorded separately.

| Chunk | Inventory rows | Matters | Parse-only result |
|---|---|---:|---|
| OT_2004CHUNK1 | 1–13 | 13 | Pass |
| OT_2004CHUNK2 | 14–24 | 11 | Pass |
| OT_2004CHUNK3 | 25–29 | 5 | Pass |
| OT_2004CHUNK4 | 30–36 | 7 | Pass |
| OT_2004CHUNK5 | 37–47 | 11 | Pass |
| OT_2004CHUNK6 | 48–56 | 9 | Pass |
| OT_2004CHUNK7 | 57–64 | 8 | Pass |
| OT_2004CHUNK8 | 65–75 | 11 | Pass |
| OT_2004CHUNK9 | 76–90 | 15 | Pass |
| OT_2004CHUNK10 | 91–105 | 15 | Pass |

All ten briefs passed `tools/split_chunk.py --parse-only`; no runtime splits were generated. All 105 neutral caption, term and event-date fields match the inventory. Every inventory docket or reporter token appears in the corresponding neutral identifier field. All 105 neutral Participation Matter fields report no identified case-specific nonparticipation: 77 state “None identified.” and 28 state “No case-specific recusal or nonparticipation identified.” Historical nonparticipation reported later remains a Run verification flag.

The user's opening instruction establishes that all 105 Section II positions are approved. Their substantive contents were not exposed to the opening contexts or copied into the workspace. Brief extraction was limited to the neutral scheduling, posture, dependency and participation fields. Approval is accepted from the supplied instruction; this is not an assembly-stage revalidation of private positions.

The manifest retains exactly 103 `Merits decision` values and two `Original proceeding: exceptions to report` values, at rows 8 and 76. All 105 categories remain `MERITS`. Those labels prescribe no form or result. Neutral Entry Stage and Event and Unresolved Same-Term Dependencies fields are copied mechanically from the saved briefs, preserving their qualifications. The user's direction that every inventory matter is properly before the Court at its scheduled event governs opening acceptance; neutral finality cautions remain Run checks, not opening conflicts.

All 27 Standing State grants match exactly one inventory row each: 3, 5, 7, 14, 16, 20, 25, 26, 29, 31, 34, 36, 40, 44, 47, 51, 54, 56, 59, 62, 64, 70, 74, 78, 85, 92 and 99. None becomes a separate carryover or grant event. Kansas v. Colorado, No. 105, Original, is matched to row 8, chunk 1, 2004-12-07, and retains its carried opening stage there.

Arizona v. California, No. 8, Original; Nebraska v. Wyoming, No. 108, Original; and Kansas v. Nebraska, No. 126, Original, with Colorado, appear once each in the separate unscheduled manifest table. Their stages and sources are copied from Standing State. No OT2004 event date is scheduled for them. They do not increase the scheduled-event count, and no new report, filing, deadline or disposition is supplied.

## Chronology and conditional dependencies

Every event uses the law effective before its scheduled event date. Intervening effective Records supplement the opening trackers. The common pre-date baseline is preserved across each shared-date boundary: 2004-12-13, chunks 1–2, rows 10–14; 2005-01-24, chunks 2–3, rows 21–26; 2005-06-06, chunks 8–9, rows 75–78; and 2005-06-20, chunks 9–10, rows 86–92. All other uncoordinated same-date groups follow the same rule.

Conditional checks in the neutral intake are preserved in the manifest, including checks involving earlier scheduled sentencing, immunity, statutory enforcement, standing, jurisdiction, property and habeas matters. They supply no holding and assume no outcome. Same-day companion cautions preserve a common pre-date baseline. No coordinated same-day sequence is established at opening. Entering-law slices are refreshed for the actual event at Run.

## Prior-term completion cursors

An independent read-only review compared each earlier term's close dossier with the opening identity and date metadata of its final Court Records. Each row below lists the complete group on that term's latest effective Court-event date. This is a cursor check, not a new legal audit of prior adjudications.

| Term | Latest Court-event date | Court events on that date | Cutoff source |
|---|---|---|---|
| OT1991 | 1992-07-17 | Benten v. Kessler, A-40; application to vacate stay. | [Close dossier](../../OT1991/close/TERM_CLOSE_DOSSIER.md) |
| OT1992 | 1993-07-26 | DeBoer v. DeBoer, A-64; stay application. | [Close dossier](../../OT1992/close/TERM_CLOSE_DOSSIER.md) |
| OT1993 | 1994-06-30 | Holder v. Hall; International Union, United Mine Workers of America v. Bagwell; consolidated Johnson v. De Grandy / De Grandy v. Johnson / United States v. Florida; Madsen v. Women's Health Center; McFarland v. Scott; consolidated Tuilaepa / Proctor v. California. | [Close dossier](../../OT1993/close/TERM_CLOSE_DOSSIER.md) |
| OT1994 | 1995-06-29 | Babbitt v. Sweet Home Chapter; Chabad-Lubavitch of Georgia v. Miller; consolidated Miller / Abrams / United States v. Johnson; Capitol Square Review and Advisory Board v. Pinette; Rosenberger v. Rector and Visitors of the University of Virginia. | [Close dossier](../../OT1994/close/TERM_CLOSE_DOSSIER.md) |
| OT1995 | 1996-07-01 | Pennsylvania v. Labron / Kilgore, grants and reasoned summary merits decisions in one Record; United States v. Winstar Corp., merits. | [Close dossier](../../OT1995/close/TERM_CLOSE_DOSSIER.md) |
| OT1996 | 1997-09-15 | Harrison v. Eddy Potash, Inc. | [Close dossier](../../OT1996/close/TERM_CLOSE_DOSSIER.md) |
| OT1997 | 1998-09-28 | Ino Ino, Inc. v. City of Bellevue; Lucas v. Johnson; Newton County Wildlife Association v. Rogers; SEC v. First Jersey Securities, Inc.; United States ex rel. McKenzie v. BellSouth Telecommunications, Inc. | [Close dossier](../../OT1997/close/TERM_CLOSE_DOSSIER.md) |
| OT1998 | 1999-06-23 | Alden v. Maine; College Savings Bank v. Florida Prepaid; Florida Prepaid v. College Savings Bank; Ortiz v. Fibreboard Corp. | [Close dossier](../../OT1998/close/TERM_CLOSE_DOSSIER.md) |
| OT1999 | 2000-06-29 | United States v. Alaska, No. 84, Original; implementing decree. | [Close dossier](../../OT1999/close/TERM_CLOSE_DOSSIER.md) |
| OT2000 | 2001-06-28 | Lorillard Tobacco Co. / Altadis U.S.A. Inc. v. Reilly; Palazzolo v. Rhode Island; Tyler v. Cain; consolidated Zadvydas v. Davis / Ashcroft v. Ma. | [Close dossier](../../OT2000/close/TERM_CLOSE_DOSSIER.md) |
| OT2001 | 2002-06-28 | Stewart v. Smith; United States v. Bass. | [Close dossier](../../OT2001/close/TERM_CLOSE_DOSSIER.md) |
| OT2002 | 2003-06-30 | Amazon.com, Inc. v. Barnesandnoble.com, Inc.; Bragg v. West Virginia Coal Association; Burdine v. Johnson (Cockrell v. Burdine); Eichorn v. AT&T Corp.; Holland ex rel. Overdorff v. Harrington; United States v. Gatewood. | [Close dossier](../../OT2002/close/TERM_CLOSE_DOSSIER.md) |
| OT2003 | 2004-06-30 | Roeder v. Islamic Republic of Iran, No. 03-1147. | [Close dossier](../../OT2003/close/TERM_CLOSE_DOSSIER.md) |

The OT2003 manifest contains 119 scheduled rows, all Completed, referencing 119 distinct existing Court Records. There is no unmatched Court Record. The additional Rule 53 amendment source is separately classified as an Admitted Source Record and excluded from the 119 Court events. The final Roeder event and the 119-event completion count agree with the close dossier and the opening trackers.

## Adapter and validation scope

The scratch adapter at `tmp/ot2004_open_adapter.py` invokes `tools/open_term.py` with an in-memory inventory-reader replacement for this index's textual Chunk column, then populates the four projections. The original index, briefs and tools remain unchanged. It copies exact neutral field and Standing State text from the saved sources, rather than retyping it.

`tools/check_term.py OT2004` passed with zero warnings, invoked under a command guard preventing any prohibited version-control invocation. Because its inventory regex does not recognize this supplied layout, its success alone does not establish inventory coverage. The adapter's independent field-by-field comparison supplies that coverage. No current-term Records or close artifacts required object-history checks.

The final workspace check passed for all four populated files, the seven required continuity blocks, relative-link targets, preserved inventory order and values, copied neutral stage and dependency fields, exactly three undated carryover rows, and the absence of prohibited publication tokens and machine-specific paths. The pre-write content snapshot comparison passed: protected opening inputs remain byte-identical. The scratch files remain under `tmp/`.

Independent final review also passed: the carryover rows and shared-date tables are identical across the manifest, continuity note and neutral projection; all scheduled events remain Open; and no private position, proposed vote, historical-comparator substance or placeholder enters those projections. The opening workspace is validated.

**Conflict or missing inventory item:** None found. Routine event-specific research, runtime splitting, entering-law refresh and participation verification remain Run work. No adjudication was performed during Open.
