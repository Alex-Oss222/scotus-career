# OT1999 chunk 3 prior-opinion count cross-check

Engine §8 counts each signed plenary merits lead once for each Justice who delivers any part, including a lead that announces a judgment without a majority rationale. Separate writings, per curiam opinions, summary dispositions and procedural actions do not count.

Independent classification of the 24 prior-event opinion tables in `OT_1999CHUNK3_PRIOR_ASSIGNMENT_TABLES.md` produces **20 counted leads through February 14, 2000**:

| Justice | Count | Raw opinion-table evidence |
|---|---:|---|
| Stone-Zsela | 1 | Wardlow |
| Stevens | 2 | Hill; Smith |
| O'Connor | 3 | Laidlaw; Fraternal Order of Police; Shrink |
| Scalia | 3 | Condon; Martinez-Salazar; Richards |
| Kennedy | 2 | Paul P.; Rayphand/Torres |
| Souter | 2 | Drye; Gutierrez |
| Thomas | 2 | Steamfitters; Martinez v. Court of Appeal |
| Ginsburg | 2 | Kimel; U.S. West |
| Breyer | 3 | United Reporting; Weeks; Bossier Parish |

The last counted event is **Richards v. United States, February 14, 2000, Scalia**. These counts come from the actual author rows or prose topology, not historical assignment-statement tallies.

The `source_record` parser in `tmp/ot1999_chunk3_counts.py` was executed against bounded in-memory copies containing only each prior event's identity/date headers and opinion table or prose topology. Its result matched the independent classification for all 24 events. No parser edit was necessary for this baseline.

- Fraternal Order of Police's prose expressly identifies O'Connor as delivering the Court's opinion; the parser's prose branch counts her once.
- Paul P.'s three Court-part rows all identify Kennedy; they count once. Bossier Parish's two Breyer rows and U.S. West's two Ginsburg rows likewise count once each.
- Weeks's four lead-part rows identify Breyer. His four-Justice Part IV rationale still announces the majority judgment; the signed plenary lead counts once. Its separate writings do not count.
- United Reporting's majority/plurality lead counts once for Breyer.
- Fiore's signed certification opinion is a procedural action and contributes zero. Flippo, Lesage and Adarand are the three per curiam summary dispositions and contribute zero.
- Admitted-source events are excluded by the helper before any opinion-row counting; they are outside these 24 judicial-event tables.

This is baseline arithmetic and parser quality assurance only. It selects no form, eligible pool or author for a chunk 3 matter. No current brief, runtime, freeze, Stone supplement or comparator was opened; no Record or workspace file was changed; no Git command was run. The full `count_before` directory traversal was not invoked during this scoped check. This verifies the supplied prior-event forms, not every possible future table form.
