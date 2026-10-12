# Officer substitution rules: source-validation receipt

**Legal cutoff:** 1996-11-04.  
**Scope:** Federal Rule of Appellate Procedure 43(c) and Federal Rule of Civil Procedure 25(d), including the complete surrounding rules and the relevant historical notes. This is a legal-source receipt, not a case-specific application, vote, reconciliation, or decision.  
**Status:** Source validation complete. Files are saved; no Git command was run and no commit is claimed. Any repository freeze remains pending the operator's authorized process.

## Verified official sources and dates

1. [United States Code, 1994 Edition, Supplement I (1995), Title 28 appendix](https://www.govinfo.gov/content/pkg/USCODE-1995-title28/pdf/.pdf), Government Publishing Office / Office of the Law Revision Counsel. This is GovInfo's working legacy PDF URL, including the literal filename `.pdf`. Its appellate and civil rule headings, printed pages 3 and 47, state that the text is amended through January 16, 1996. [Official package metadata](https://www.govinfo.gov/metadata/pkg/USCODE-1995-title28/mods.xml) confirms base edition 1994, supplement 1, edition 1995, and laws-in-effect date 1996-01-16. The archived PDF's later digital creation/modification dates are retrieval-format metadata, not legal amendment dates.
2. FRAP 43 is on printed/PDF page 42. The rule's own source-credit line identifies the March 10, 1986 amendment, effective July 1, 1986. The 1986 note describes its changes to subdivisions (a) and (c) as technical, without intended substantive change. The 1967 note expressly identifies FRCP 25(d) and the then-Supreme Court Rule 48 as sources of subdivision (c).
3. FRCP 25 and its full notes are on printed/PDF pages 115-116. The last amendment shown for Rule 25 is March 2, 1987, effective August 1, 1987. The 1987 note calls the amendments technical. The 1961 amendment, effective July 19, 1961, supplies the explanatory notes concerning automatic public-officer substitution and designation by official title.
4. [Supreme Court order of April 23, 1996, 517 U.S. 1257, with the complete accompanying appellate amendments](https://www.govinfo.gov/content/pkg/USREPORTS-517/pdf/USREPORTS-517-BackMatter-3.pdf), printed pages 1255-1262: the order changes Appellate Rules 21, 25, and 26, not Rule 43. Those changes take effect December 1, 1996, after this receipt's cutoff, governing later-commenced cases and pending proceedings insofar as just and practicable.
5. [Supreme Court order of April 23, 1996, 517 U.S. 1281, with the complete accompanying civil amendments](https://tile.loc.gov/storage-services/service/ll/usrep/usrep517/usrep5171277/usrep5171277.pdf), printed pages 1279-1283: the order changes Civil Rules 5 and 43, not Rule 25. The same December 1, 1996 effective date and pending-proceeding qualification apply. The LOC identifier and saved filename end in `1277`; the actual source pages begin at 1279 and the order is printed at 1281.

The operative rule wording copied here is the January 16, 1996 historical text, applicable at the November 4, 1996 cutoff. No wording from the later restyled rules has been substituted. The expected 1994 and 1996 GovInfo appendix paths did not resolve; the date-eligible 1994 Edition, Supplement I supplies the authenticated historical text.

## What the texts establish

- **FRAP 43(c)(1):** Its trigger is a public officer already a party in an official capacity to an appeal or other proceeding in the court of appeals, who dies, resigns, or otherwise ceases to hold office during its pendency. The proceeding does not abate; the successor is automatically substituted. Later proceedings must use the substituted party's name, but a misnomer that does not affect the parties' substantial rights must be disregarded. A substitution order may be entered at any time; omitting one does not defeat substitution.
- **FRAP 43(c)(2):** An official-capacity public-officer party may be identified by official title instead of personal name. The court retains authority to require the name. This is permission to use a title, not an obligation to omit the name.
- **FRCP 25(d)(1)-(2):** The corresponding district-court provisions use an officer who is a party to an action in an official capacity and leaves office during the action's pendency as their trigger. They likewise provide automatic substitution, disregard of harmless misnomer, an optional substitution order, and permission to identify the officer by title subject to the court's power to require the name. A change of officeholder before an appeal must therefore be examined at the procedural stage when it occurred, rather than assuming that FRAP 43(c)(1)'s appellate-pendency condition is met.
- **Scope and limits:** By their terms, these provisions continue an existing official-capacity party through succession or identify that party by title. Neither provision, by itself, makes an unrelated nonparty an original party or supplies the factual predicate that an official-capacity party existed. Whether a disputed designation identifies an existing party or instead seeks to add someone requires examination of the governing case record and any other applicable authority; this receipt does not answer that question.
- **1961 FRCP note:** The note explains that official capacity includes actions formally naming an officer but intrinsically directed against the government, office, or continuing incumbent. It distinguishes claims seeking recovery from the named officer's personal assets. Automatic substitution is procedural and leaves substantive issues, including immunity defenses, unchanged. A successor may still seek dismissal for mootness or take other appropriate steps if the challenged policy will not continue. These are explanations in the advisory note, distinct from the rule's operative commands.

## Exact-copy provenance and verification

All source files and extracts are in `terms/OT1996/sources/roy-procedure/`. The official downloaded PDF/XML bytes were preserved. `copy_officer_rule_sources.py`, run with `python -B`, copies text directly from the specified PDF pages using PyMuPDF `page.get_text()` and literal substring boundaries. It does not retype, dehyphenate, or normalize the copied text. Editorial page-boundary markers are identified as such. Full-rule-and-notes extracts preserve the surrounding subdivisions; the two short exact extracts isolate all of FRAP 43(c) and FRCP 25(d). The complete 1996 amendment documents were read, not just their first pages.

The rule pages 42, 115, and 116 and the two amendment-order pages were rendered and visually inspected against the extracted text. The complete relevant rule text, qualifications, numbering, amendment lines, and effective dates agree. `OFFICER_RULES_SOURCE_MANIFEST.json` contains exact URLs, file sizes, all source hashes, all extract hashes, and the extraction-script hash. The manifest's recorded hashes were recomputed against the saved bytes before this receipt was delivered.

| File | SHA-256 |
|---|---|
| `USCODE-1995-title28-appendix.pdf` | `d9fb41c43579b1647d26b5381940d274dffa11b19ed96f4dec47cf1c66ffb2f4` |
| `USCODE-1995-title28-mods.xml` | `ec55206fae90ddc5c5204e0a73dbfb5dbabf04fbfc57ad88075444c02fe1ecb7` |
| `FRAP-1996-amendments-517US1255.pdf` | `ed55c56cb75fe6565f2ee550632f457c840fc2b021b012b71f37cd650e3d1a60` |
| `FRCP-1996-amendments-517US1277.pdf` | `6deb7764be708a586aae198a1adaa02af974b3ac44b4de3e52570bc51671da72` |
| `FRAP43c-1996-operative-exact-extract.txt` | `6b5121255cb9ac47eadb72a5613311875812a3699a9b65d535fc24cf35f20eea` |
| `FRCP25d-1996-operative-exact-extract.txt` | `e6a7e20b3f8932584dfd17327fd66f8cd68728e3901ca4f07a6465731603ae20` |

No case brief, commitment, comparator, reconciliation handoff, Record, assembly material, or top-level `stone/` path was opened, listed, or searched for this source-validation task. No case-specific legal conclusion is included.
