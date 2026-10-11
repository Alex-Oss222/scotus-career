# OT1995 catch-up preparation

This directory is **preparation only**. It is not the recovered development library, a replacement schema, or a completed import. No production repository files are modified. The original library and schema are absent from the current repository checkout; their stable case, event, source and document IDs cannot be restored safely until the original copy is available.

`source-inventory.json` captures repository HEAD, raw-byte SHA256 fingerprints, all 126 canonical Record paths and their four opening metadata lines, the 115 scheduled manifest rows referencing 116 Court events, the ten remaining admitted noncase source Records, and the twelve final carried-matter rows from Standing State. Table rows and metadata lines are retained verbatim without their line terminators. Classification follows explicit manifest membership and its published totals; it does not decide legal meaning or index historical URLs.

`extract_source_inventory.py` reads `/workspace/scotus-career` and writes the JSON beside this README. Run it with `python -B extract_source_inventory.py` to refresh this preparation. It validates counts, references, metadata labels, source hashes and a stable HEAD before writing. It reads but never modifies repository files. Successful validation establishes the integrity of this extraction, not readiness of a recovered library or correctness of adjudications.

## Recovery and import order

1. Recover the original library, its schema, stable IDs, build/validation tools and retained snapshots. Do not derive replacement IDs from inventory row numbers or captions.
2. Compare the recovered snapshot fingerprints with this inventory. Refresh existing OT1995 entries as well as adding the remaining chunks: earlier Records contain in-place corrections, audit repairs and completions of previously stopped events.
3. Use the recovered schema's existing mechanisms for separate historical documents, simulation Records, noncase sources, lifecycle status and provenance. This preparation does not prescribe a new schema or change those mechanisms.
4. Reconcile the imported totals and distinctions below, then run the recovered library's safeguards and freshness checks. Only a completed, validated import can be described as caught up.

## Import distinctions to preserve

- **115 scheduled rows, 116 Court events, ten admitted sources, 126 Records.** Bowersox has separate interim and final actions on April 9; the manifest lists the final filename first. Reference order must not become chronology.
- **Twelve final carried matters.** A completed event can leave the underlying matter pending. The manifest's five inherited *opening* carryovers are not the complete closing list; use the final Standing State rows captured here.
- **Stable identity matters.** Love's metadata still includes `OT1995-015`, whereas the current case list places it at row 18. Preserve recovered IDs and explicit aliases. Louisiana v. Mississippi has separate exceptions and decree events; the three Shieh petitions share a filing event; Baby Richard and Doe v. Kirchner remain distinct matters; the Vera Record covers consolidated captions.
- **Records control completed action metadata.** Ayers ended in dismissal of review before judgment, and Doe v. Kirchner in review dismissal, notwithstanding the original intake descriptions. Kilgore's authenticated docket is 95-1738; older intake 95-1692 is not the current identifier.
- **Noncase sources have varying dates and types.** They include state/federal statutes, a rule amendment and a regulation. Medicaid coverage, statutory enactment, publication, delayed effectiveness and conditional implementation must not be flattened into a single undifferentiated date. All ten source Records also have Public Projections; that heading does not make them Court decisions.
- **Current trackers are closing law.** `state/` now publishes the completed OT1995 baseline. Do not use those current bytes as the term-opening law for earlier OT1995 events.
- **Same-day groups cross chunks** on February 21, May 20, June 10, June 20 and June 26, 1996. Chunk and file order do not establish intervening law.
- **Historical preparation remains historical.** Ledger display order is not verified commitment order, and retained pending-commit or stopped-matter prose must be interpreted in its documented stage rather than overriding later authoritative Records and close publication.

The source inventory is intentionally limited to current repository metadata. It contains no newly researched historical URLs, no legal rereview, and no claim that the development library has been recovered or integrated.
