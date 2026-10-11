# Source library and citation index

An isolated, working catalogue of all closed terms OT1991–OT1995. It links the repository's simulation Records, their recorded source locations, and citation occurrences. **Production integration remains disabled.** Nothing here is authority or a restricted-stage handoff.

This is a new version-2 rebuild. The original uncommitted development workspace was unavailable; recovered older documentation, schemas, tests and patches are preserved under [recovery/retained-text](recovery/retained-text/). The original stable case IDs, reviewed source mappings and retained builds were not recovered. New Record IDs derive from canonical paths and survive in-place corrections; renames require explicit review. No lossless migration or original feature parity is claimed.

[Open the current browser](builds/94795938180682ff581c7ddeca4921514fd4b8a90365224ea0d5bb4bcf09d0fb/index.html) · [See a preview](review/browser-desktop.png)

## Use

From the repository root:

```sh
python -B development/case-library/tools/library.py build
python -B development/case-library/tools/library.py check
python -B development/case-library/tools/library.py search 'Bowersox' --term OT1995
python -B development/case-library/tools/library.py search '' --term OT1995 --chunk 10
python -B development/case-library/tools/library.py citations '505 U.S. 833'
```

`build` prints the snapshot directory. Open its `index.html` for the browser, which supports term, chunk, Record-kind and text filters. Every card and pointer remains available with JavaScript disabled. The `citations` command returns observed citation strings and their source Record/line/section; these are mentions, not legal-treatment determinations. CLI reads verify freshness. An already-open static browser cannot do that: run `check` before relying on its navigation.

Python 3.10+ and `jsonschema` 4.18+ are required; the cloud environment already provides them. A different environment can install the bounded dependency with `python -m pip install -r development/case-library/requirements.txt`.

## Coverage and limits

All 575 canonical Records and 556 inventory rows are accounted for: 558 Court events and 17 admitted sources. The final 1995 carryover table retains twelve pending matters; completion of an earlier event does not close its underlying matter. Bowersox's interim and final actions are separate Records. Coleman's supplemental post-close petition remains outside the scheduled inventory, with a null ledger effective date because no explicit ledger entry was found.

The index preserves observed metadata, 6,070 recorded reference occurrences and 8,154 recognized citation mentions. These counts do not represent distinct verified historical documents. No PDF corpus was copied or downloaded, no remote URLs were checked, and no missing source was invented. Unsupported or absent locations remain visible. Full Records are mixed public/internal material. No stage-specific retrieval or automatic legal-force analysis is implemented.

Exact inventory matching and six explicitly evidenced OT1991 exceptions bind the inventory to Records. These are new clerical mappings, not restoration of the lost original case-identity catalogue. The new index does not merge case identities across terms or infer consolidation from matching names/dockets.

## Update and recover

Run `build` after an independently completed development catch-up. It checks all selected terms, preserves operator annotations and retains prior snapshots. An identical build reuses the validated snapshot. Ordinary source edits produce a fresh snapshot; CLI reads refuse an older one.

If the pointer or a generated snapshot is damaged, inspect it and use:

```sh
python -B development/case-library/tools/library.py build --recover
```

Recovery preserves damaged pointer bytes and existing build directories. It does not repair authoritative source files or guess missing inputs. Concurrent writers fail with a retry message. An interrupted process releases its OS lock; do not delete the lock file to bypass an active writer.

Operator-owned aliases, notes and named extension objects belong in `inputs/annotations.json`, keyed by the new Record IDs. Generation never edits that file. Unknown IDs, malformed JSON, invalid dates, extra core fields, symlinks and path escapes fail validation. Schema version changes describe structural changes; a routine data refresh does not increment it.

## Validate

```sh
python -B -m unittest discover -s development/case-library/tests -v
CASE_LIBRARY_BROWSER_TESTS=1 python -B -m unittest discover -s development/case-library/tests -v
```

Browser tests additionally require Playwright and Chromium; the current environment provides both. Test failures and file mutations are confined to disposable fixtures. Recovered historical tests are archived evidence and are deliberately excluded from this suite.

See [STATUS.md](STATUS.md), [DESIGN.md](DESIGN.md), and [SAFEGUARDS.md](SAFEGUARDS.md). Integration still requires a separate readiness review and later user authorization. Proposed maintenance remains a refresh after completed chunks and a full reconciliation after term close.
