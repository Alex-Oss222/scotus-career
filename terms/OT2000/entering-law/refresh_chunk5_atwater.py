from pathlib import Path
base=Path(__file__).resolve().parents[1]
source=(base/'entering-law/OT_2000CHUNK5_NEUTRAL_SOURCE_ADDENDUM_ATWATER.md').read_text(encoding='utf-8')
facts=source[source.index('## Record recitations to add'):source.index('## Source support and limits')]
limits=source[source.index('The cited underlying Record pages'):]
text='''# Atwater: refreshed neutral record

## Scope and validation

This addendum supplements `OT_2000CHUNK5_NEUTRAL.md` and the prior Atwater preparation receipt; all prior freezes remain preserved. It corrects an incomplete factual premise concerning identification, prior acquaintance, the earlier stop and practical processing. It supplies no merits vote, outcome or present historical rationale. Only the sanitized objective-source addendum, the original neutral packet and the existing entering-law slice were read for this refresh. No current Supreme Court opinion, comparator, private supplement or reconciliation artifact was opened.

The new facts are material to any actual-function analysis of station-house custody. Lack of physical papers cannot be treated as lack of identifying information: Atwater supplied her license number and address, and Turek knew her as a local resident from an earlier encounter. The earlier encounter ended in a warning after he discovered that the child was belted, not a finding of a prior unbelted-child offense. The additional plaintiff-favorable recitations concerning slow daytime driving, no other traffic, her old traffic citation, acknowledgment and apology must retain that summary-judgment source status. They do not erase the conceded present violation, prove subjective motive or resolve danger, future appearance, verification or processing necessity by themselves.

Ricci's controlling actual-enforcement requirement, its civil-offense limit and its nonexclusive possible justifications remain the same entering law. Its dissent's supported processing account was a different record, not authority to presume processing needs here. Likewise the four-Justice Ricci application reservation creates no automatic requirement to leave every record unresolved. If modeling applies or extends functional review, it must assess the actual additional custody using both the missing physical papers and the supplied identification/local familiarity, not a hypothetical unidentified driver. The difference between Texas's fine-only criminal offense and Ricci's civil violation remains an express legal question. The current McArthur and Wallis rules retain their actual scopes.

The City's identified safety and appearance rationales are litigation positions. The published recitation does not establish that no other argument was preserved, that an additional ground was waived, that roadside verification was impossible or that station processing was compulsory. A proposed ground needing such a fact must identify its support; absence of the original paper from research proves no litigant omission. Any remand must state the real unresolved predicate without manufacturing a new evidentiary hearing or inviting an unsupported justification.

Conduct-date immunity remains measured in March 1997. This factual correction changes neither the effective dates of Ricci and Knowles nor the independent municipal policy, fault, causation and injury requirements. No factual supplementation supplies a missing legal choice.

## Mechanically copied objective recitations

'''+facts+'''
## Source precision

Official source: https://www.govinfo.gov/content/pkg/USREPORTS-532/pdf/USREPORTS-532-318.pdf. Reporter page 324 and footnote 1 supply the missing-papers account and earlier encounter; page 346 supplies local familiarity; pages 369–371 contain the other record recitations and the identified litigating justifications. These references locate only objective recitations and their underlying record citations; no current-case judicial evaluation is incorporated.

'''+limits+'''

## Affected-stage instruction

This is a material neutral-source completion. Any independent commitment relying on inability to identify Atwater, unknown local residence, a prior seatbelt conviction or an unsupported necessary-processing premise must be replaced through clean modeling on this corrected packet and then reconciled afresh. This addendum itself changes no vote, adjudication or public output.
'''
(base/'freeze/OT_2000CHUNK5_NEUTRAL_REFRESH_ATWATER.md').write_text(text.rstrip()+'\n',encoding='utf-8')
print('Atwater neutral refresh saved; prior freezes preserved.')
