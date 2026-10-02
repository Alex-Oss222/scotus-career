# Preflight C — source and verification log

Research cutoffs are the supplied event dates: 1995-11-20 (A. St. P. C.); 1995-11-28 (Field and Town & Country); 1995-11-29 (Thompson). Retrieval: 2026-10-02.

## Clean handoff

`C_FACTUAL_ADDENDUM.md` is ready for a fresh neutral validator. It is an objective source digest and does not replace neutral framing. The initial scope/gap inventory is `PREFLIGHT_C_INITIAL.md`. Current law must come from the entering slice/trackers and actual earlier effective decisions.

## Retrieval/reading record

- Internet Archive own advanced search API queried its `us-supreme-court` collection by exact docket and case name. Search responses and their exact URLs: `preflight_c_archive_search.json`; additional A. name/docket variants: `C_ac_archive_search_additional.json`. No matching A. No.94-7810 item located. No inference about unrecovered record contents follows.
- Field `micro_IA40385013_0573`: petition, both merits briefs and JA PDFs + OCR downloaded. Town `micro_IA40385013_0572`: petition, both respondent briefs, petitioner brief and JA PDFs + OCR downloaded. Thompson `micro_IA40385013_0614`: petition, both merits briefs and JA PDFs + OCR downloaded. `C_records/download_manifest.json` maps all exact URLs and local copies. Downloads are NOT full-reading certificates.
- A. Louisiana rehearing, 643 So.2d743: complete court text including footnotes and Dennis additional reasons read from CAP JSON, URL https://static.case.law/so2d/643/cases/0743-01.json. Original 643 So.2d719: posture/statutory text/proof/access/therapist-weight portions read; full opinion and separate writing NOT certified read. Both saved as C_ac files. CAP volume metadata authenticates date/docket/reporter location. Original official court copy/session-law scan not independently recovered.
- Santosky: full official U.S. Reports PDF https://tile.loc.gov/storage-services/service/ll/usrep/usrep455/usrep455745/usrep455745.pdf downloaded, extracted with pdftotext, and completely read, including majority, dissent and footnotes. `C_Santosky_LOC.*`. Cornell/official report metadata cross-checks identity. Stevens majority join and O'Connor dissent join verified; no extension vote inferred.
- Prior public outputs: DeBoer entire public entry; Reno v. Flores public separate-position and remedy section. No private record opened.
- Field direct archive spot-verification: JA printed pp.36–45 (bankruptcy court reasons) and October correspondence; respondent brief p.32–33 debt-nexus argument. No absence claim derived by search. Reproduced Code §523(a)(2)(A)/(B) checked against downloaded government 1994 Code.
- Town: full published judicial text checked; Eighth Circuit opinion opening/background/threshold disposition read through OpenJurist actual opinion, not later-citation summaries. NLRA §152(3) full definition including exclusions checked against official 1994 Code download.
- Thompson: complete published judicial texts checked; petitioner merits brief pp.41–43 and Appendix A pp.A-1–A-2 read directly. The latter supplies complete pre-AEDPA §2254(d). Attempted government PDF returned non-PDF; kept as C_FAILED_USCODE1994_2254_response.html, not statutory evidence.
- Ordinary-case full-opinion verification used Cornell separate-writing URLs after syllabus identification: Field 94-967.ZO, ZC, ZD; Town 94-947.ZO (no separate writing listed); Thompson 94-6615.ZO, ZD. Each entire writing, all footnotes, read. Official U.S. Reports 516 U.S.59/85/99 PDFs downloaded for primary-source support. These full same-case materials are NOT clean inputs and are quarantined under `freeze/C_historical_verification/`. The separate exposure log is internal only and may not be passed to neutral validator/model.
- Browser API was tried for required rendered Justia access. In-app browser unavailable and browser inventory empty. No Justia automated HTTP fetch performed. Search snippets were discovery only; no Justia AI opinion summary used.

## Outstanding bounded source work

No current merits vote or remedy is certified. Fresh validator decides whether the objective evidence suffices for each live path. A. further contact remedy or additional constitutional component requires the exact preserved issue and relevant operative orders; no new abuse finding may be made. Full Archive reading is available if a live path makes scope, preservation, factual conflict or remedy dependent on those materials. No claim that an unrecovered/missing proposition is absent from the Archive corpus is made. Full reading of large bundles is not otherwise necessary merely to certify ordinary dates and facts verified in judicial text.

No git command, Foundation/state edit, brief edit or access to top-level Stone materials was performed. No commitments were produced. No independent modeling by this context is authorized.
