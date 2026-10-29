# Murphy and Kolstad raw-source receipt — control use

Status: substantive neutral preflight stopped after historical Supreme Court petition-treatment statements unexpectedly appeared in predecision merits briefs. Neither target Supreme Court merits result, rationale nor vote lineup was read. No commitments or final neutral packets were produced. Fresh neutral contexts must validate sanitized facts and framing. This receipt is for control; do not pass the exposure-location discussion to fresh contexts.

## Verified source inventory

All paths below are relative to `terms/OT1998/runtime/chunk11-scoped/`.

| Matter | Safe original lower-opinion text | Source and extraction |
|---|---|---|
| Murphy | `murphy_lower_opinion.txt` | https://openjurist.org/141/f3d/1185/murphy-v-united-parcel-service ; only `<article class="opinion-body">` extracted with Python HTMLParser. Complete extracted opinion read. |
| Kolstad | `kolstad_lower_opinion.txt` | https://openjurist.org/139/f3d/958/kolstad-v-american-dental-association ; only `<article class="opinion-body">` extracted. Relevant portions read; not certified complete reading. |

Do not expose `murphy_lower_raw.html` or `kolstad_lower_raw.html`: these saved landing pages contain modern answer boxes and citation-history material. Only HTML tag names/class metadata were printed to locate the original-opinion article; the modern prose was not read.

The Internet Archive's own collection search returned Murphy item `micro_IA40385014_0185` and Kolstad item `micro_IA40385014_0217`. Metadata confirmed separately numbered predecision filings. The files below are IA OCR text, downloaded from their individual item files, not the aggregate or docket. PDFs were not downloaded or read; OCR accuracy should be checked against PDF for any quotation whose exact wording becomes decisive.

| Local suffix (prefix `murphy_` or `kolstad_`) | Separate IA document |
|---|---|
| `02_source.txt` | `02. Petition for Writ of Certiorari_djvu.txt` |
| `06_source.txt` | `06. Joint Appendix_djvu.txt` |
| `07_source.txt` | `07. Petitioners Brief_djvu.txt` |
| `08_source.txt` | `08. Respondents Brief_djvu.txt` |
| `09_source.txt` | `09. Reply Brief_djvu.txt` |

URL template: `https://archive.org/download/<item>/<item>%20<number>.%20<URL-encoded document name>_djvu.txt`.

Read scope: Murphy original lower opinion in full; selected questions, fact statement, statutory/regulatory excerpts and pertinent argument portions of 07/08/09. Kolstad pertinent lower-opinion portions, questions, statement-of-case, and one respondent argument passage; limited keyword-location checks in JA. No claim that every filing was read in full, and no claim that a proposition is absent merely because not located.

## Exact control redaction needs

- Kolstad 07, lines 533–580: statement of case contains a historical Supreme Court petition-treatment statement concerning a related cross-petition. Control should remove that statement before any fresh neutral exposure. Its disposition is deliberately not repeated here.
- Murphy 08, footnote 28 at approximately lines 2689–2707: preservation argument contains historical target Supreme Court grant-scope/petition-treatment language. Control should replace it with a sanitized, objectively verified review-scope statement only if supported by the operative simulated posture, preserving the respondent's distinct waiver argument as an allegation.
- Murphy 08, proceedings-below portion around lines 665–676 also contains a historical Sutton grant citation; it establishes no effective June 22 merits law. Remove Supreme Court procedural citations from fresh excerpts.
- Other petition/brief/JA portions were not certified free of historical Supreme Court docket or grant statements. Do not pass the entire documents blindly; control should extract necessary source facts. Preserve lower-court holdings, party arguments and record references distinctly. Do not redact lower reasoning simply because it disagrees with a party.

## Already verified objective source facts (not a new neutral framing)

- Murphy lower opinion ¶¶2–6: district summary judgment for UPS; unmedicated pressure approximately 250/160; August 1994 application; initial examination 186/124; health card issued; employment began mid-August; nurse review in September; October 5 termination. ¶¶8–9 describe the medicated-state coverage ground and treating doctor's everyday-function testimony. ¶¶13–14 state the lower regarded-as rationale and expressly leave qualification, reasonable accommodation and the DOT-defense contention unreached. ¶15 addresses the interview-inquiry contention separately.
- Murphy 07 printed pp.6–7 and 31–32: petitioner relies on testimony about severe effects when medication lowers pressure to normal, plus actual limitations in lifting, exertion and other functions; these are petitioner's assertions and cited testimony, not new findings. Initial 186/124 and later 160/102 and 164/104 readings are distinguished. 07 pp.35–38 and 09 pp.19–20 argue exclusion extends to DOT-required work and ancillary jobs; 08 pp.43–44 disputes that occupational breadth and invokes vocational evidence and other mechanic employment.
- Murphy 08 p.42 n.23 objects that medicated-state factual sufficiency falls outside the question presented; petitioner 07 pp.30–32 and 09 p.17 presses that alternative. This is an unresolved scope dispute for clean validation, not a preflight finding of waiver. The earlier neutral packet did not identify it.
- Murphy regulatory text quoted in 07 p.5: §391.41(b)(6) concerns high blood pressure likely to interfere with safe vehicle operation; §391.43(f) says consistent pressure above 160/90 may require further tests. The briefs separately discuss DOT medical advisory criteria and possible temporary certification. A court's or party's shorthand numerical statement is not automatically the regulation's command.
- Kolstad lower opinion ¶¶3–9: the disputed promotion arose in 1992; Wheat recommended Spangler and executive director Allen made the selection; the jury found sex discrimination and awarded $52,718 in backpay. The district judge withheld punitive damages; panel and en banc treatment of that issue are distinct. These sources do not establish a punitive award.
- Kolstad lower opinion ¶¶40–41 and ¶¶63–65: majority and dissent disagree about punitive attribution and legal awareness; dissent says the Association had not argued good-faith compliance and emphasizes executive-director decisionmaking. That statement is the dissent's procedural characterization, not an independently proved compliance fact. The initial neutral packet's formulation of disputed implementation requires fresh source validation.
- Kolstad 07 question: “In what circumstances may punitive damages be awarded under Title VII of the 1964 Civil Rights Act, as amended, for unlawful intentional discrimination?” 08 asks whether jury discretion is available absent egregious conduct. These are party formulations, not certified operative grant text.

## Previously located entering-law pointers

These were located before substantive work stopped and require fresh operator selection. No votes were modeled.

- `state/holdings/civil-rights.md`: Bragdon, beginning line 4365; Landgraf, beginning line 1694.
- `state/holdings/labor-and-employment.md`: Hazen Paper, beginning line 110; Faragher, line 1566; Ellerth, line 2221. Current simulated Ellerth preserves the general complete-defense question and distinct remedial limitations as open.
- `state/STANDARDS_AND_TESTS.md`: “Actual disability and substantial limitation of reproduction”; “Objective assessment of an ADA direct threat”; “The 1991 Civil Rights Act’s new liabilities and jury election”; “Meaningful review of punitive-damage amounts”; “Employer attribution of supervisor-created harassment.”
- Prior public writings: `terms/OT1997/output/OT_1997CHUNK12.md` Bragdon entry beginning line 22; Ellerth entry line 752. `terms/OT1996/output/OT_1996CHUNK13.md` Faragher line 883 and Harrison line 1004. `terms/OT1992/output/OT_1992CHUNK5.md` Hazen Paper line 400.
- Pre-June22 projection links current West v. Gibson public law at `terms/OT1998/entering-law/west_v_gibson_merits_1999-06-14.md`; that compensation authority does not itself settle punitive eligibility.

No Git commands were used. All writes were under terms/OT1998; Python used `-B`. No Stone directory, master-jurisprudence file, combined brief, comparator, raw Record, commitment, reconciliation or audit annex was opened.
