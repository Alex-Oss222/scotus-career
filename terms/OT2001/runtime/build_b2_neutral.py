from pathlib import Path
import re

root = Path('terms/OT2001')
text = (root / 'runtime/OT_2001CHUNK7_NEUTRAL.md').read_text(encoding='utf-8')
parts = re.split(r'(?=^## \d+\. )', text, flags=re.M)
selected = [p for p in parts if re.match(r'^## (125|126)\. ', p)]
assert len(selected) == 2
balderas = (root / 'entering-law/OT_2001CHUNK7_BALDERAS_PUBLIC.md').read_text(encoding='utf-8')
page = (root / 'runtime/research_june20/page_lower.txt').read_text(encoding='utf-8')
robertson = (root / 'runtime/research_june20/robertson_lower.txt').read_text(encoding='utf-8')

def between(source, start, end):
    i = source.index(start)
    j = source.index(end, i)
    return source[i:j]

excerpts = [
    ('Page: actual findings, 144 F. Supp. 2d at 361-362', between(page, 'C. Findings of Fact', 'III.')),
    ('Page: district projections and primary evidence, 144 F. Supp. 2d at 365-366', between(page, 'Using the data he had gathered to project', 'Once again, we feel')),
    ('Robertson: pleaded counts and different parties, 148 F. Supp. 2d at 446', between(robertson, 'Then, on April 27, 2001', 'On May 2, 2001')),
    ('Robertson: evidentiary agreement and review posture, 148 F. Supp. 2d at 447', between(robertson, 'Subsequently, the parties in this case agreed', 'We heard oral argument')),
    ('Robertson: racial and other criteria, 148 F. Supp. 2d at 455-457', between(robertson, 'The plaintiffs point to two paragraphs', 'In sum, Bartels')),
    ('Robertson: incumbent-treatment ground, 148 F. Supp. 2d at 459', between(robertson, 'Count II of the plaintiffs', 'D. Constitutionality of Residency Requirement')),
]

header = '''# OT2001 chunk 7 — Page and Robertson frozen neutral handoff

The two approved neutral sections below are copied mechanically without alteration. Their provisional cutoff statements are superseded by the effective current-law refresh and Balderas public handoff reproduced below. Both direct-review events are properly before the Court on June 20, 2002; no filing, grant or jurisdictional-statement verification condition is imposed. No oral argument is invented, no case-specific nonparticipation is established, and all nine Justices are seated. Research cutoff: immediately before June 20, 2002. The two same-day matters share that baseline and do not supply one another with new Supreme Court precedent.

The complete published lower opinions were read independently. The earlier procedural Page appeal is not the judgment under review, and the Robertson residency count remains separate. Lower-opinion descriptions of post-divergence Supreme Court doctrine are historical descriptions, not controlling simulated law. Governing propositions come from the entering-law slice and actual dated public opinions. Published recitations establish the reported pleadings, evidence and findings under Engine section 14; possession of original transcripts or exhibits is not claimed. No research gap is treated as litigant default.

'''
receipt = '''
# Current-law and framing validation

The entering-law sources are OT_2001CHUNK7_B.md, OT_2001CHUNK7_B_SUPPLEMENT.md and OT_2001CHUNK7_B_CURRENT.md. Balderas is now an effective June 17 event. Its summary affirmance supplies no common majority application rationale; it preserves Valdespino and adds no automatic independent-ground, compactness, numerical, geographic or totality rule for these New Jersey cases. The complete public handoff is copied below. Easley's April 18, 2001 public opinion and Valdespino's June 17, 1999 public opinion were also read for actual non-Stone joins and separate positions. Neither current matter's historical Supreme Court disposition was researched.

Page's findings permit consideration of an independent third-Gingles failure, local opportunity and primary access, rather than inference from minority percentages or statewide gain alone. Adverse expert proof was received and assessed; it was not absent. The rejected chilling theory remains distinct from electoral-success analysis, and discriminatory purpose was separately rejected. The lower court's predominance language does not replace the governing independent-injury analysis. Robertson's political association, strategic timing and common remedial objectives do not establish representative authority under Richards. Agreed testimony is admissible evidence, not consent to Page's factual inferences or preclusion. The incumbent claim concerns electoral prospects created through district boundaries, with no separate racial candidate qualification. The actual summary-judgment evidence supports competing arguments about the relative role of race; the existence of other factors alone does not logically prove race could not predominate. Easley governs the legal significance of predominance; its four dissenters' proposed rule remains noncontrolling.

No independent merits due-process theory is invented from Page's complaint label. No distinct Section 2 count is invented in Robertson. No new election date, later election result, replacement map or trial finding is assumed. Original 2001 calendar descriptions do not become new 2002 procedural orders.

# Effective Balderas public handoff — script copy

'''
extra = '''
# Primary lower-opinion record excerpts — script copies

Full sources: https://static.case.law/f-supp-2d/144/html/0346-01.html and https://static.case.law/f-supp-2d/148/html/0443-01.html. Saved HTML and extracted text are in runtime/research_june20/. Extraction artifacts remain source artifacts; no quotation is silently corrected.

'''
for title, body in excerpts:
    extra += '## ' + title + '\n\n' + body.strip() + '\n\n'
output = header + '\n'.join(selected) + receipt + balderas + extra
target = root / 'freeze/OT_2001CHUNK7_B_2_NEUTRAL.md'
assert not target.exists(), 'Do not replace an existing frozen handoff.'
target.write_text(output, encoding='utf-8')
print(target)
