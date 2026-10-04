# Bowersox — additional control-only source receipt

This supplements the initial receipt and preserves `REPORTED_RECORD_FACTS.md` unchanged. **Do not expose this receipt or raw current-opinion sources to independent modeling.** The only new sanitized handoff is `RETROSPECTIVE_PRE_EVENT_FACTS.md`.

## Bounded search and source discovery

The first extraction correctly found no new locator in 517 U.S. 345–347. On control's subsequent instruction, the earlier receipts were checked for a targeted lower-opinion search beyond Archive. None was documented. A single bounded lower-opinion search pass was therefore performed, without repeating Archive searches.

- CourtListener's public web search and API search for `"Doyle" "Williams"`, bounded before April 10, 1996, each returned HTTP 403. These responses establish access failure, not absence of a lower opinion.
- OpenJurist's advertised search form was inspected and its actual `q` parameter used for `Williams Delo`. The resulting index supplied 49 F.3d 442, 82 F.3d 781, and 928 F.2d 284. Modern index text served only as navigation.
- The 49 F.3d 442 header and opening text identify **Darryl Williams**, a different prisoner; it was excluded without claiming complete reading.
- The short 928 F.2d 284 text was read through its complete nine numbered paragraphs. It concerns Doyle Williams but dates to March 19, 1991 and gives no contents of the January 1996 report/order. Its proceedings were not imported.
- The specific 82 F.3d 781 lead concerns Doyle Williams and appellate No. 96-1205. CAP's volume metadata independently confirms identity, docket, date, page range and case ID 7644389. Its original reporter transcription was then retrieved directly. The attempted case-specific CAP PDF URL returned 404; no reporter-image examination is claimed.
- The opinion cites the pre-event second-petition decision at 912 F.2d 924, retrieved through its specific CAP citation path. No broad search followed. The 1988 district citation surfaced there concerns the second petition; it was recorded as such and not confused with the unrecovered January 1996 order.

Exact requests, status codes and purposes are retained in `LOWER_LOCATOR_SEARCH.json`. The retained OpenJurist search text is navigation only. CAP's full volume metadata was narrowed to the matching case entry in `CAP_82_MATCHED_METADATA.json`; no claim is based on unrelated metadata.

## Complete personal reading and cross-check

**R2 — Williams v. Delo, 82 F.3d 781–785 (April 9, 1996):**

- https://openjurist.org/82/f3d/781/williams-v-k-delo — retained complete visible text `82f3d781.txt`.
- https://static.case.law/f3d/82/html/0781-01.html — retained `82f3d781_CAP.html` and complete plain-text extraction `82f3d781_CAP.txt`, with printed-page markers and paragraph IDs.
- Personally read the complete opinion, including caption/docket/date, counsel and panel, all eight numbered OpenJurist body paragraphs, final ordering language, and every CAP body paragraph on pp. 783–785. No footnotes or additional writings appear. CAP's casebody omits reporter headnotes; full source coverage means the complete judicial writing, not headnotes or unrecovered page images.
- The two transcriptions agree in substance; CAP has evident OCR artifacts such as `eases` for `cases`, `MeMILLIAN`, and split `habe-as`. The sanitized handoff uses paraphrase except expressly quoted source fragments. Modern citator assessments, analytics, and quoted passages selected by later-citation frequency were not used as authority.
- The opinion expressly follows the historical Supreme Court vacatur and a subsequent request for a reasoned stay or merits ruling. Its final paragraph also refers to a later merits brief. Those events and the opinion's own adjudication are excluded from the sanitized handoff. The relevant extracted petition contents, proposed amendment, older conduct, and district findings expressly concern already existing matters. Statements whose particular presentation time is uncertain are not certified as earlier submissions.
- No later ruling, new appellate finding, claim characterization as legally abusive/successive/meritless, legal-innocence assessment, or conclusion about substantial grounds enters the addendum. Prior-district findings are expressly labeled as such. The report's reference to expert opinions is not turned into invented expert testimony.

**R3 — Williams v. Armontrout, 912 F.2d 924–942 (1990):**

- https://static.case.law/f2d/912/html/0924-01.html — retained `912f2d924_CAP.html` and complete marked text `912f2d924_CAP.txt` (11,019 extracted words).
- Personally read the entire judicial casebody, in contiguous nontruncated text blocks: caption, docket No. 88-1342 and dates; complete en banc merits opinion, Parts I–VI (printed pp. 927–935); complete Bright opinion joined by McMillian (pp. 935–941), including **all eleven notes** retained later in CAP document order; October 12 rehearing/amicus order; complete Lay statement; complete Bright statement; and complete Arnold statement joined by John R. Gibson (through p. 942). Nothing was skipped after locating favorable excerpts. Reporter headnotes and original scanned images were not supplied by the retrieved casebody.
- Direct source corroboration establishes the earlier first-degree instruction claim and trial judge's quoted explanation, plus reported transcript citations. The strongest contrary record material was retained: both sides requested that instruction; the victim was transported alive, with intervening stops; the account of premeditated intent depended on an immunized accomplice whose credibility was impeached. Judicial inferences about the proper instruction and legal merits were not converted into objective facts.
- The earlier guilt-phase ineffective-assistance discussion is kept distinct from the later penalty-phase claim. No inference from the absence of discussion in an appellate opinion substitutes for full possession of the earlier petition.

Generated plain-text copies normalize trailing whitespace only; downloaded CAP HTML is retained byte-for-byte. Checksums for retained substantive source texts and sanitized handoff are recorded in `RETROSPECTIVE_SOURCE_SHA256.txt`. No original lower filing was recovered. No external communication, source request to a party, or simulated procedural event was performed.

## Scope and remaining gaps

The new source base materially improves the record: actual claim subjects, proposed amendment, confinement evidence and opposing district findings, and important prior-presentation facts are now supported. Initial statements about the limits of R1 are preserved as statements about that source alone. The sanitized addendum lists the remaining specific gaps without requiring possession of every original: penalty-phase omission/prejudice particulars, expert contents, disputed second-degree presentation history, names of newer Missouri authorities, and identities/relevance of alleged proportionality comparators. It also disclaims certification of an exhaustive petition inventory.

Fresh neutral validation must assess the addendum's retrospective source use, its dating limits, and whether any remaining gap affects an available ruling. This extractor makes no ruling or vote recommendation. Historical follow-on events are not assumed to have occurred merely because the later report supplied information about preexisting evidence.
