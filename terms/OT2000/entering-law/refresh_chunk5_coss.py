from pathlib import Path
base=Path(__file__).resolve().parents[1]
source=(base/'sources/chunk5-control/Coss-neutral-record-supplement.md').read_text(encoding='utf-8')
copied=source[source.index('## Underlying record and lower proceedings'):]
text='''# Coss: refreshed neutral record and preservation limits

## Scope and source validation

This addendum supplements the frozen Coss neutral entry, its entering-law slice and the April 24–25 preparation receipt. All earlier freezes remain preserved. The original entry incompletely described the surrounding criminal history, the sentencing court's stated considerations, the lower remedy and the source account of the prosecutor's lower appellate arguments. These details can matter to an actual-sentencing-effect ground and to the proper scope of appellate review. They supply no merits vote, present Supreme Court outcome, comparator rationale or private position.

The source is a sanitized extraction from the official report: https://www.govinfo.gov/content/pkg/USREPORTS-532/pdf/USREPORTS-532-394.pdf, pages 397–400 and the briefing-characterization footnote on page 409. The full current Supreme Court opinion and all comparator and reconciliation materials were not opened. The passages reproduced below were mechanically copied from the sanitized file. Underlying sentencing documents, the original state postconviction file and the appellate briefs have not been independently read in this refresh. The report establishes published recitations, not possession or authentication of every original paper.

## Neutral completeness update

### Other history and sentencing considerations

The source describes five juvenile adjudications before age sixteen and several adult convictions. The adult list includes the challenged assault, institutional-vandalism and criminal-mischief convictions; it must not be represented as wholly independent of those challenged convictions. The other adjudications and convictions are additional background relevant to the sentencing record at their supported scope. The listed arrests whose charges were dropped are not convictions or findings that Coss committed the alleged acts. The probation office's general characterization is that office's characterization, not an independently established finding that every listed arrest involved proven misconduct.

The resentencing court sustained the objection to counting the 1986 convictions separately and eliminated their effect on the numerical prior-record score and applicable range. It then identified several considerations in choosing a sentence within the range: the current crime, community protection, criminal disposition, prior record, rehabilitation and the testimony heard. It stated a perceived need for incarceration to prevent continued lawbreaking and reimposed six to twelve years. That fuller explanation must be considered alongside the reference to the prior record. Neither the presence of other serious history nor the removal of points establishes by itself that the challenged convictions had no adverse influence on the selected sentence. Conversely, mention or consideration of them is not by itself a finding of how much shorter a sentence would have been absent them.

### Existing findings and the actual lower remedy

The federal district court identified a current-sentence claim and found a reference to the challenged convictions sufficient for its jurisdiction analysis. After an evidentiary hearing it found deficient counsel performance but denied relief for lack of Strickland prejudice. The en banc Third Circuit agreed that the convictions had been considered, found a reasonable probability of a different result at the 1986 assault trial absent the deficient performance, and ordered a specific alternative remedy: the Commonwealth could retry the 1986 assault or resentence Coss for the 1990 assault without considering the 1986 conviction.

Those are existing lower determinations and remedial directions, not issues that can be described as never examined. Their existence does not itself establish that every legal predicate was satisfied, that the Supreme Court must adopt the remedy, or that the current sentence was necessarily lengthened. Identify which finding, legal inference, procedural ruling or remedy is being reviewed and apply the proper appellate treatment. The source supplies no authority for replacing an actual finding with a new contrary fact merely because another inference seems plausible. Nor does the presence of a lower finding prevent lawful review of its sufficiency or legal consequence when that review is properly available.

### Preservation and the source account of appellate briefing

The separately supplied footnote characterizes the prosecutor's panel brief and rehearing petition as not disputing the causal connection. It characterizes the en banc supplemental argument as addressing the numerical range, without challenging the district court's consideration finding concerning the maximum within that range. Preserve the difference between a range-only objection and a separately presented challenge to influence on selection within the range.

This account is an authenticated published judicial characterization, not an independently recovered set of briefs or a final holding about waiver. It therefore bears on preservation but must not automatically establish forfeiture, concession of every causal element or authority to decide an unpreserved merits issue. If a dispositive alternative depends on what the actual briefs disputed or on the scope of a particular finding, the missing precise sources are the cited panel/rehearing briefs, the en banc supplemental brief at pages 15–18, and the pertinent lower findings. No litigant default follows from their absence from this research packet. A supported narrower ruling or remand must still account for the existing findings and the preserved dispute rather than silently reopening every question.

### Remaining legal and factual boundaries

The September 1994 federal filing retains the former chapter 153 framework. Present custody, permissibility of indirect predicate review, applicable exhaustion or excuse, constitutional invalidity and adverse influence on current custody remain distinct. Custis's ACCA sentencing holding and express expired-custody and no-meaningful-review reservations are unchanged; Garlotte's continuous unexpired custody rule does not decide these independent completed sentences. Neither the fuller criminal history nor the existence of a current sentence resolves those channel questions.

The 1987 state petition was filed, counsel was appointed and the prosecutor answered, but the reason for the long absence of a ruling remains unexplained. The absence of a direct appeal does not itself establish abandonment of the later filed collateral petition, faultless delay, available meaningful adjudication or exhaustion of every required route. No new fact concerning responsibility for that lapse is supplied.

These additions require fresh consideration of the actual record-supported alternatives: a channel ruling, lawful treatment of the supported sentencing-effect issue, or a bounded remand where a necessary predicate remains unresolved. They do not prefer one, establish harmlessness, grant relief, require a new evidentiary hearing or supply a final sentence.

## Exact sanitized source passages

'''+copied+'''

## Affected-stage receipt

The independent modeling handoff must include this refresh because criminal-history completeness, sentencing explanation, prior findings and preservation can change the sufficiency or availability of an alternative ground. Every affected non-Stone determination must be remodeled on the corrected neutral record before a new reconciliation. This receipt itself changes no frozen commitment, adjudication or public output.
'''
(base/'freeze/OT_2000CHUNK5_NEUTRAL_REFRESH_COSS.md').write_text(text.rstrip()+'\n',encoding='utf-8')
print('Coss neutral refresh saved; prior freezes preserved.')
