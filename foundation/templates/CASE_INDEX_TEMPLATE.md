# OT[year] case index

[Save this file as `terms/OT[year]/case-list.md`, beside the term's `briefs/` folder (`briefs/OT_[year]CHUNK[n].md`). It is the user's term-wide inventory of cases and Court actions. `tools/open_term.py` builds the workspace manifest from its table, and `tools/rebuild_manifest.py` and `tools/check_term.py` check the manifest against it, so the table must keep the exact seven-column form below. The model is `terms/OT1994/case-list.md`.]

Bracketed text is instruction or placeholder text and does not appear in a completed case index.

**+ = one of the [number] expressly listed simulated grants.** For those entries, the docket shown is simulation-assigned under the user’s instruction; it is not a historical Supreme Court identifier. Stone approval status is stated separately in Section II.

[Omit the paragraph above if the term has no simulated grants.]

[Total] matters: [count] MERITS[, [count] ORIGINAL][, [count] CERTIORARI][, [count] APPLICATION]; [number] chunks ([size] each in chunks 1–[n], [size] in chunk [last]). Listed applications and petition-stage events: [list them, or none]. [Membership notes only: a matter excluded, reconstructed, or added, with a link to the chunk brief that explains it.] Consolidated companions count once.

| No. | Chunk | Caption | Docket(s) | Event date | Event type | Category |
|---:|---:|---|---|---|---|---|
| 1 | 1 | [Caption] | [Docket] | [YYYY-MM-DD] | [Event type] | [Category] |
| 2 | 1 | [Caption] / [Companion caption] | [Docket]; [Docket] | [YYYY-MM-DD] | [Event type] | [Category] |
| 3 | 1 | [Caption] + | [Simulation-assigned docket] | [YYYY-MM-DD] | Merits decision | MERITS |
| 4 | 1 | [State] v. [State] | [Number], Original | [YYYY-MM-DD] | Original proceeding: exceptions to Special Master report | ORIGINAL |

[One row per matter, in chronological order by event date; rows for the same date appear in the order the Court takes them, because the tools keep the list's own order for same-day ties. Each row stays on one line, and no cell contains a pipe character.

- **No.:** running number from 1, in table order.
- **Chunk:** the chunk number alone (1, 2, …), matching `briefs/OT_[year]CHUNK[n].md`.
- **Caption:** the case name, without italics. Consolidated companions share one row, their captions separated by " / ". A simulated grant ends with " +".
- **Docket(s):** the Supreme Court docket number or numbers, separated by "; ". An original action reads "[number], Original"; an application reads "A-[number]". For a simulated grant, give the simulation-assigned docket or, if none has been assigned, the lower-court citation; never invent a Supreme Court docket.
- **Event date:** YYYY-MM-DD.
- **Event type:** what the Court does that day, e.g. "Merits decision", "Per curiam decision after merits submission", "Original proceeding: exceptions to Special Master report".
- **Category:** MERITS, ORIGINAL, CERTIORARI or APPLICATION. A simulated grant is MERITS.]

[Docket notes, only where needed: historical captions or dockets that are preserved, how simulation-assigned dockets were given, and that lower-court docket numbers remain separate.] Stone approval status and remaining scope limits are stated in each chunk brief’s own Section II and neutral packet. The entering baseline is the completed OT[prior year] [Holdings](../../state/HOLDINGS.md), [Standards and Tests](../../state/STANDARDS_AND_TESTS.md), and [Standing State](../../state/STANDING_STATE.md), incorporating all [number] matters through [last decision date of the prior term], with the Court’s setting governed by [Court Composition](../../foundation/COURT_COMPOSITION.md). OT[year] is open; see the [validated workspace manifest](workspace/manifest.md). No prepared position or prospective same-term dependency is a Court decision.
