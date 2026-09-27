# OT1993 Term Continuity Note

**Opened:** September 26, 2026, at repository revision 55fc623.  
**Chronology cursor:** October 4, 1993, the opening of October Term 1993, before the first supplied event.  
**Mode:** No adjudication has occurred. Run stages use the isolated-context mode described in `AGENTS.md`.

This Note is a replaceable cumulative projection. The Canonical Decision Records and Admitted Source Records control if it conflicts with them.

## 1. Scope and Chronology Cursor

- **Term:** October Term 1993. Divergence point October 7, 1991, when Stone replaced Rehnquist as Chief Justice.
- **Opening tracker versions:** `state/STANDING_STATE.md`, `state/STANDARDS_AND_TESTS.md`, and `state/HOLDINGS.md` with its doctrinal volumes `state/holdings/*.md`, each headed "Last completed October Term: 1992; Processed through: July 26, 1993, after DeBoer v. DeBoer, No. A-64; Edition: September 17, 2026." They were published by the OT1992 Commit pass (`terms/OT1992/close/TERM_CLOSE_DOSSIER.md`) and last changed at commit e53e54d (Holdings volume compression, no substantive change). Validated at opening: the three headers agree; `python tools/holdings_volumes.py check` reports the volumes and compatibility view synchronized; Standing State's roster and allotments match the Composition register's OT1993 roster row and its order effective August 10, 1993.
- **Manifest:** `workspace/manifest.md`, generated from `terms/OT1993/case-list.md` (95 entries in eight chunks) with the seven Standing State carryovers, the institutional calendar, and the manifest controls appended below the inventory table.
- **Changes covered:** none. No Court event or admitted source change has been processed.
- **Latest processed change:** the term-opening baseline.
- **Latest completed events of the earlier simulated terms:** OT1991, *Benten v. Kessler*, July 17, 1992; OT1992, *DeBoer v. DeBoer*, No. A-64, July 26, 1993.
- **Next eligible manifest item:** *Day v. Day*, Nos. 92-8788, 92-8792, 92-8888, 92-8905, 92-8906, 92-9018, 92-9101, and 93-5430, Rule 39 filing-relief application, October 12, 1993 (chunk 1), followed the same day by *In re Sassower* in the expressly established sequence.

## 2. Completed Events and Admitted Sources

None. The ledger is empty at opening.

## 3. Current Law

No current-term holding, reusable doctrine, or noncase-law change exists. The law entering the Term is stated in full by the opening trackers: controlling propositions in `state/HOLDINGS.md` (doctrinal volumes under `state/holdings/`) and reusable rules in `state/STANDARDS_AND_TESTS.md`, each with effective dates and limits, completed through July 26, 1993. Pre-divergence law remains available where those registers have not displaced it. A historical Supreme Court decision after October 7, 1991 supplies no in-world proposition unless a simulated decision adopted it. Each event's entering-law reading slice is built from these files and any effective current-term Record with `tools/build_entering_law.py`.

## 4. Material Published Noncontrolling Positions

None current-term. Each Justice's published separate positions from OT1991 and OT1992 are consulted from those terms' public renders, `terms/OT1991/output/` and `terms/OT1992/output/`, which is where the Engine reads a Justice's simulated prior positions. They are not restated here and they are not law.

## 5. Current Procedure and Institution

- **Roster and seniority:** Stone, Chief Justice; Associate Justices in seniority order Blackmun, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg. All nine seats are occupied. Ginsburg took the judicial oath on August 10, 1993 and is seated throughout the Term.
- **Participation:** Six Justices constitute a quorum. A majority of participating Justices controls a judgment; a referred application uses the participating-majority rule. Thomas and Ginsburg do not participate in No. 93-5252 (*Sassower v. Reno*). No other case-specific nonparticipation is established at opening; each event validates participation at argument or submission and again at decision.
- **Assignment:** Stone assigns when he is in the judgment majority. Otherwise the most senior participating Associate in that majority assigns, in the order Blackmun, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg. An equally divided Court affirms without precedential effect.
- **Allotments (order effective August 10, 1993, governing through August 2, 1994):** Stone, District of Columbia, Fourth, and Federal; Souter, First; Ginsburg, Second; Scalia, Third and Fifth; Stevens, Sixth and Seventh; Blackmun, Eighth; Kennedy, Ninth; O'Connor, Tenth; Thomas, Eleventh.
- **Standing practice:** Referral of applications, effective October 7, 1991. An application for interim relief in a matter on the Term's inventory is referred by the Circuit Justice to the full Court and decided by the participating Justices; the order issues in the Court's name, recites the presenting Justice, and ordinarily issues without opinion. The user designated Stone as administrative presenter for the Day and Sassower Rule 39 groups; Anderson is presented by Stone under the District of Columbia allotment.
- **Open matters:** the seven carried matters listed in the manifest (*Zatko v. California*; *Wyoming v. Oklahoma*; *Reynolds v. International Amateur Athletic Federation*; *Grubbs v. Delo*; *United States v. Louisiana*; *Delaware v. New York*; *Nebraska v. Wyoming*), each awaiting a verified dated event. *Martin v. McDermott*, No. 92-5618, and *Demos v. Storrie* are closed and not carried; *Coleman v. Thompson* is confined to OT1991.
- **Next nonroutine acts:** none scheduled. The first supplied events are the October 12, 1993 filing-relief applications.
- **Institutional dependencies:** none within the Term. Breyer's accession on August 3, 1994 falls after the last inventory event.

## 6. Blockers and Revalidation Needs

- No conflict exists among the three opening trackers or between Standing State and the Composition register.
- No inventory item is missing. The manifest carries all 95 supplied matters; no duplicate natural key or out-of-order date was found; the eight chunk briefs in `terms/OT1993/briefs/` contain the same 95 matters.
- Source limitation, recorded for the three Rule 39 applications: the pending petitions and financial affidavits were not recovered into the research sources. The neutral packets preserve that gap, and Stone's positions decide on the record as it stands.
- Every Stone Section II position is labeled a prepared position. Under Engine section 4 it is approved only when the user's Run task says so; each Run task must carry that approval.
- Each event's posture, questions, participation, and lower-court judgment come from its brief and must be validated at Run. The opening task validates none of them.
- The briefs cite the opening trackers as `inherited/HOLDINGS.md`, `inherited/STANDARDS_AND_TESTS.md`, `inherited/STANDING_STATE.md`, and `inherited/COURT_COMPOSITION.md`. Those are byte-identical snapshots of `state/` and `foundation/COURT_COMPOSITION.md` at commit b83e0fd, and every cited anchor resolves in the current files.

## 7. Source and Research Cutoff

The opening state relies on `state/`, `foundation/COURT_COMPOSITION.md`, `terms/OT1993/case-list.md`, `terms/OT1992/close/TERM_CLOSE_DOSSIER.md`, and `terms/OT1992/close/OPEN_MATTER_RECONCILIATION.md`. No external research was required or performed for term opening. Research cutoff: September 26, 2026.
