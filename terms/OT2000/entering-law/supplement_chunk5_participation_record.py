from pathlib import Path

base=Path(__file__).resolve().parents[1]
participation=(base/'sources/chunk5-control/Oakland-participation-neutral.txt').read_text(encoding='utf-8')
valentine=(base/'sources/chunk5-control/Valentine.txt').read_text(encoding='utf-8')

def excerpt(start,end):
    return valentine[valentine.index(start):valentine.index(end,valentine.index(start))].strip()

text='''# OT2000 chunk 5: neutral participation and record supplement

## Status and scope

This supplements the prior neutral freeze and preparation receipts; it does not overwrite them. The Oakland participation correction supersedes the original neutral entry's statement that no case-specific nonparticipation was identified. The Valentine clarification narrows any implication that a supported factual dispute or a new evidentiary hearing has already been established. No current Supreme Court outcome, merits rationale or lineup was supplied or opened. The Oakland source is an isolated participation extract; the complete official lower-court Valentine opinion was read.

## Oakland participation correction

Breyer did not participate in consideration or decision. Model the participating Court as eight Justices: Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas and Ginsburg. The seven participating non-Stone Justices are modeled; Breyer supplies no commitment, vote, join or assignment. Six qualified Justices constitute a quorum, and this eight-member Court satisfies it. No reason for the absence, separate recusal order or physical-presence detail is inferred. The report's consideration-and-decision statement supplies the participation limit; it does not introduce the historical merits disposition.

### Exact sanitized source copy

'''+participation+'''

## Valentine: actual support for the alleged pause and name

The official Third Circuit opinion does not identify a district-court historical finding that Valentine stopped and gave his name before charging, and it does not report a trial credibility determination accepting that account. It reports the district court's legal determination that reasonable-suspicion analysis should stop at the officer's command. Those propositions are different.

The appellate court recounts the officer's sequence as a response followed by a charge toward the officer, an attempt to push aside his arms, physical restraint and discovery of the gun during the struggle. On the asserted earlier compliance, the appellate court says that its record review found no supporting evidence and that the police report appeared to rebut the theory. It nevertheless expressly declines factual determination because it regards even the assumed pause and name as legally insufficient submission. The published source does not reproduce the police report or identify supporting testimony for the asserted pause.

Accordingly, neither a found interval of submission nor a genuine evidentiary dispute requiring a new hearing is established by this source. The Court may assess the categorical legal rule and the lawfully supported alternative record ground separately. A remand need not compel a new hearing, reopen proofs or erase an established continuous-charge account; it can require only appropriate treatment of the existing record under the governing legal rule if that is the supported disposition. Conversely, the appellate court's assumption for legal analysis cannot become an affirmative historical finding of no earlier submission. A final factual resolution requiring more than the published recitation would need the actual suppression findings, relevant hearing testimony and Woodard's police report; no such original is claimed read here.

The lower court's additional assertion that charging necessarily supplies suspicion by analogy to its historical Wardlow account is not entering law. Apply the actual simulated Wardlow holding to the supported pre-seizure conduct. The seizure-time issue and the content/reliability of the initial tip remain distinct, as does the unadjudicated New Jersey permit theory.

Source: https://www2.ca3.uscourts.gov/opinarch/001425.txt, pages 3, 11–15. The following source passages are copied mechanically without alteration; linebreak and extraction artifacts are retained.

### Reported encounter sequence

'''+excerpt('The officers, who were in uniform and in a marked car,','We have jurisdiction under 18 U.S.C.')+'''

### District court's stated legal boundary

'''+excerpt('The District Court expressly held that inquiry about','While it is true that the')+'''

### Record-support and assumed-facts distinction

'''+excerpt('We conclude that as in Johnson and Moorefield,','Under some circumstances we have held')+'''

## Validation

The Oakland correction is material to participation and must enter before its commitments are frozen. Any already prepared Oakland commitment naming Breyer requires removal and review of affected arithmetic or opinion possibilities in the clean modeling context. The remaining neutral record, four-part lower injunction conditions and merits alternatives are unchanged.

The Valentine clarification supplies source status rather than an adjudicated credibility choice. It does not prescribe a judgment. No Court action, new factual finding or historical Supreme Court disposition is imported by this supplement.
'''
(base/'freeze/OT_2000CHUNK5_NEUTRAL_SUPPLEMENT_OAKLAND_VALENTINE.md').write_text(text.rstrip()+'\n',encoding='utf-8')
print('Participation correction and Valentine source clarification saved as separate neutral supplement.')
