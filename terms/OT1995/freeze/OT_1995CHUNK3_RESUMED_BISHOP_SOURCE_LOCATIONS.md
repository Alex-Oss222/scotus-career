# Bishop and Stokes: source locations and neutral-preflight exposure receipt

Prepared October 3, 2026. Substantive cutoff: February 5, 1996. This is a source-search receipt, not a validated Neutral Modeling Packet, entering-law snapshot, commitment, or disposition. The requested `OT_1995CHUNK3_RESUMED_BISHOP_NEUTRAL_VALIDATED.md` was not authored.

## Exposure and completion boundary

A general web search for the lower-court matter unexpectedly displayed a same-matter historical Supreme Court disposition in a search-result snippet. Its substance is intentionally absent from this receipt. Under Engine §3A, the exposed context stopped affected neutral framing and did not model any commitments. A fresh neutral preflight context must independently validate framing and completeness, followed by fresh independent modeling. No account of the excluded disposition should be supplied to either context.

The authorized earlier supplemental source-check receipt was inspected. It contained source-location results and later references to prior component labels and workflow status. Those prior workflow conclusions were not adopted. No previous commitment, reconciliation, comparator, Stone supplement, raw Decision Record, private workspace projection, or top-level Stone material was opened. No Git command was run.

The Archive searches below were independently completed and all returned title/identifier/year rows were inspected before the Supreme Court exposure. Full lower-opinion verification and the requested neutral supplement were not completed. This receipt makes no judgment about lawful disposition, sufficiency of record, or whether a missing source prevents adjudication.

## Independently completed Archive catalog searches

The Archive's own `advancedsearch.php` endpoint was queried with a browser User-Agent, selecting only identifier, title and year; `rows=200`, page 1. Each result set fit on the requested page. All returned metadata rows were inspected. No matching Bishop/Stokes criminal record was found. No unrelated item was opened. No conclusion is drawn about availability outside this indexed collection.

| Collection query | Results inspected | Matching record |
|---|---:|---|
| `collection:us-supreme-court AND "95-6678"` | 0 | None |
| `collection:us-supreme-court AND "95-6958"` | 0 | None |
| `collection:us-supreme-court AND Bishop` | 76 | None |
| `collection:us-supreme-court AND Stokes` | 25 | None |
| `collection:us-supreme-court AND "Kevin Bishop"` | 0 | None |
| `collection:us-supreme-court AND "Edward Stokes"` | 2 | Both unrelated nineteenth-century items |
| `collection:us-supreme-court AND "94-5321"` | 0 | None |
| `collection:us-supreme-court AND "94-5387"` | 0 | None |
| `collection:us-supreme-court AND 6678` | 5 | None |
| `collection:us-supreme-court AND 6958` | 6 | None |
| `collection:us-supreme-court AND "95 6678"` | 0 | None |
| `collection:us-supreme-court AND "95 6958"` | 0 | None |

The two Supreme Court docket strings were supplied solely as historical retrieval identifiers. This receipt assigns no Supreme Court docket to the in-world event.

Exact query URLs and unmodified selected metadata are in the following local receipts, in the table's order:

- `tmp/bishop_neutral_sources/archive_00.json` through `archive_11.json`.
- Retrieval script: `tmp/bishop_neutral_fetch.py`, executed with `python -B`.

Direct catalog URLs for repeatable checks:

1. <https://archive.org/advancedsearch.php?q=collection%3Aus-supreme-court+AND+%2295-6678%22&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=200&page=1&output=json>
2. <https://archive.org/advancedsearch.php?q=collection%3Aus-supreme-court+AND+%2295-6958%22&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=200&page=1&output=json>
3. <https://archive.org/advancedsearch.php?q=collection%3Aus-supreme-court+AND+Bishop&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=200&page=1&output=json>
4. <https://archive.org/advancedsearch.php?q=collection%3Aus-supreme-court+AND+Stokes&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=200&page=1&output=json>
5. <https://archive.org/advancedsearch.php?q=collection%3Aus-supreme-court+AND+%22Kevin+Bishop%22&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=200&page=1&output=json>
6. <https://archive.org/advancedsearch.php?q=collection%3Aus-supreme-court+AND+%22Edward+Stokes%22&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=200&page=1&output=json>
7. <https://archive.org/advancedsearch.php?q=collection%3Aus-supreme-court+AND+%2294-5321%22&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=200&page=1&output=json>
8. <https://archive.org/advancedsearch.php?q=collection%3Aus-supreme-court+AND+%2294-5387%22&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=200&page=1&output=json>
9. <https://archive.org/advancedsearch.php?q=collection%3Aus-supreme-court+AND+6678&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=200&page=1&output=json>
10. <https://archive.org/advancedsearch.php?q=collection%3Aus-supreme-court+AND+6958&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=200&page=1&output=json>
11. <https://archive.org/advancedsearch.php?q=collection%3Aus-supreme-court+AND+%2295+6678%22&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=200&page=1&output=json>
12. <https://archive.org/advancedsearch.php?q=collection%3Aus-supreme-court+AND+%2295+6958%22&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=200&page=1&output=json>

## Lower-opinion source locations

These are retrieval locations, not a claim of completed verification:

- [OpenJurist, 66 F.3d 569](https://openjurist.org/66/f3d/569). The page was fetched successfully; only part of its opinion text was read before the stop. Raw fetched HTML and a basic text extraction are at `tmp/bishop_neutral_sources/openjurist.html` and `openjurist.txt`. Neither file has been validated as a bounded neutral handoff; the fresh preflight should use the direct opinion URL and distinguish opinion text from site material.
- [Justia, lower appellate opinion](https://law.justia.com/cases/federal/appellate-courts/F3/66/569/488093/). This is the authorized neutral input's existing lower-opinion URL. No automated HTTP fetch of Justia was made. If used for a cross-check, it must be opened in an actual rendering browser under AGENTS.md.
- [Midpage, lower appellate opinion](https://app.midpage.ai/document/united-states-v-kevin-bishop-705084). A search-result location for the lower opinion was returned; the complete page was not opened or validated.

A CAP volume-index request and a CourtListener search request returned saved responses, but those responses were not inspected or verified. They are not certified source material and should not be treated as additional support. No petition, merits brief, appendix, suppression transcript, video, trial transcript, or trial objection/ruling was located or read in this preflight.

## Write and validation scope

Only this receipt and retrieval scratch files under `tmp/` were written. All Python invocations used `-B`; no Python subprocess was created. The completed validation is limited to the catalog searches and source locations stated above. No substantive neutral framing, commitment, legal conclusion, or final remedy is supplied.
