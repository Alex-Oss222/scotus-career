# OT2000 Opening Validation

**Task:** Open October Term 2000.  
**Validation date:** November 7, 2026.  
**Result:** Opening workspace validated; no conflict or missing inventory item.

## Baseline

The three published trackers agree on last completed October Term 1999, the June 29, 2000 cutoff after 104 completed Court events and five admitted source events, and edition November 3, 2026. Standing State identifies the opening of OT2000 before its first supplied event. The edition date does not extend the substantive cutoff. The opening divergence remains October 7, 1991.

The nine seated Justices, their seniority and the 13 circuit allotments match the Composition register. The August 3, 1994 allotment order remains effective. No vacancy or new oath-date participation condition applies. The standing referral practice, including temporary Circuit Justice action, signed explanations and certification, is preserved with its effective dates and qualifications.

`python tools/holdings_volumes.py check` passed: all 18 canonical doctrinal volumes and the continuous Holdings view are synchronized. The final completed event group from each earlier term is identified in the continuity note, ending with the June 29, 2000 United States v. Alaska implementing decree for OT1999. This Open accepts the published legal baseline; it does not reopen completed adjudications or independently rederive the entire law register.

## Inventory and chronology

The supplied case index contains 114 unique, consecutively numbered, chronologically ordered matters. The eight chunk counts are 12, 15, 14, 15, 14, 15, 14 and 15. All are categorized MERITS: 111 ordinary merits events and three original-proceeding merits events. There are no listed application or petition-stage events. Consolidated companions remain one inventory event.

All 29 Standing State docket entries match the inventory once: Arizona v. California and Fiore v. White, plus 27 expressly granted lower-court cases. The grant entries reconcile by their reporter citations even where captions are abbreviated. The two carryovers retain their published procedural states and occupy their existing scheduled rows. No duplicate event was added.

Dates retain their supplied basis: 87 historical event dates used for scheduling and 27 organizationally assigned dates. The scheduled range is October 10, 2000 through June 28, 2001. The first eligible scheduled matter is Arizona v. California, subject to validation of the required implementing provisions. The current legal cursor remains June 29, 2000.

Same-day groups cross chunks on March 20, May 21, June 4 and June 18, 2001. Both projections preserve their common pre-date entering-law baseline. The expressly related Daniels/Coss and Calcano-Martinez/St. Cyr matters require coordination; conditional same-day references do not create an adopted holding or effective sequence. Later-calendar references in the neutral scheduling fields are marked unavailable as entering law on the present schedule.

## Seed and format adaptation

The required direct opener invocation could not parse the supplied table: it accepts numeric chunk cells and bare ISO dates, while this index uses labeled chunk cells and parenthetical date annotations. No inventory row was changed.

A scratch-only adapter copied all 114 rows to the opener's supported numeric-chunk form and preserved the date annotations separately. `python tools/open_term.py OT2000 --root tmp/ot2000_open/seed` then generated the four seed files. Those seeds were copied to the authorized workspace and populated with the validated opening baseline, full scheduling metadata and carryovers. The repository tools and supplied inventory remained unchanged.

The stock manifest rebuilder uses the same unsupported input grammar. Subsequent regeneration must use an equivalently bounded adapter unless a separately authorized tool update supplies support. The stock term check also does not recognize these inventory rows for its coverage check. Accordingly, its successful result is supplemented here by an independent, exact comparison of all 114 source rows against the manifest, including caption, docket, date, event type, category, date basis, stage and dependency fields. This format limitation leaves no unresolved opening coverage gap.

## Checks and source limits

- `python tools/check_term.py OT2000`: passed with zero warnings. Its potential repository-history lookup had no applicable records or close artifacts; no git command was executed.
- All eight briefs passed the splitter's read-only parse check. Their caption sequences and counts match the inventory. No runtime split was generated; runtime generation belongs to Run.
- The manifest includes all 114 events with status Open, same-day group, current stage and material dependencies. The working ledger has no current-term entry.
- Continuity contains all seven Engine blocks. Its opening law, Court, practices and carryovers agree with the neutral projection and manifest.
- Local links resolve. Workspace files contain no seed placeholders, absolute machine paths or excluded publication tokens.
- Byte-integrity checks confirm that the state publications, governing infrastructure, tools, case index, briefs, and existing OT2000 record, close, render-input and output directories are unchanged.
- Independent read-only reviews covered inventory completeness, chronology, baseline synchronization, roster, allotments and carryover procedure.

Only neutral scheduling and participation fields from the briefs were used to populate the workspace. No private position, historical comparator, provisional commitment or audit annex entered the neutral projection. No external-event research was conducted and no later filing was admitted.

Run must validate Arizona's implementing provisions and preserve the separate Fort Yuma proceedings; validate Fiore's state-court answer before federal adjudication; establish the flagged participation facts for Hatter, New Hampshire v. Maine and Pollard; and establish any coordinated same-day sequence before relying on it. These remain event-stage checks, not completed events or opening inventory defects.

## Files written

- [Full-Term Event Manifest](../workspace/manifest.md)
- [Term Working Ledger](../workspace/ledger.md)
- [Term Continuity Note](../workspace/continuity.md)
- [Current-Term Neutral Projection](../workspace/neutral-projection.md)
- This validation summary.

Scratch preparation and validation files remain under `tmp/ot2000_open/`. All durable task writes are within the OT2000 workspace and audit directories. Operator review and repository commitment follow this task.
