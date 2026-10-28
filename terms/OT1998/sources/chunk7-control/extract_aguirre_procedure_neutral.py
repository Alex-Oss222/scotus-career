from pathlib import Path
import hashlib

src = Path('terms/OT1998/sources/chunk7-control/aguirre-ZO.txt')
body = src.read_text(encoding='utf-8')

def span(start, end):
    first = body.index(start)
    last = body.index(end, first) + len(end)
    return body[first:last]

extracts = [
    ('Claim of translation/transcription error', span('respondent contends the record of his testimony', 'Brief for Respondent 11—22.')),
    ('Published preservation recitation', span('Respondent advanced this argument for the first time', 'before either the BIA or the Court of Appeals.')),
    ('Pending agency motion', span('Respondent has filed a motion in the BIA', 'App. to Brief for Respondent 1a—6a.')),
    ('BIA briefing recitation', span('Respondent did not file a brief with the BIA', 'Record 13—15.')),
    ('Evidence-triggered burden provision as quoted in the source', span('“If the evidence indicates that one or more of the grounds for denial of withholding of deportation', 'such grounds do not apply”')),
    ('Ninth Circuit reliance on international guidance', span('In reaching the contrary conclusion and ruling that the risk of persecution should be balanced', '(U. N. Handbook).')),
    ('Paragraph 156 passage quoted by the source', span('Paragraph 156 of the U. N. Handbook, the portion relied upon by the Court of Appeals', 'the degree of persecution feared … .”')),
    ('Paragraph 152 language and Ninth Circuit comparison argument', span('Also relying on the U. N. Handbook, the Court of Appeals held', 'atrocities attributed to McMullen and his associates.” 121 F.3d, at 524.')),
]
out = [
    '# Aguirre-Aguirre — source-only procedural extraction for clean validation', '',
    'Preparation only. These bounded sentences and regulatory text are mechanically copied from the saved primary opinion. They are published recitations, not independent inspection of every original filing or proof that alleged translation errors occurred. No Supreme Court result, Justice position or legal evaluation is included.', '',
    'Research cutoff: May 3, 1999. The regulatory quotation is identified in the source as 8 C.F.R. §208.16(c)(3) (1995); the quoted clause is a condition-triggered preponderance burden, not a universal default rule. The absence of a BIA brief supplies no merits default or adverse factual inference. The agency motion is a reported existing procedure, not an instruction to invent a new hearing or a prediction of its outcome.', '',
    'The Handbook passages below identify the Ninth Circuit’s argument and the excerpts of paragraphs 156 and 152 reproduced in the primary source. They are not a complete independent reproduction of either paragraph and do not decide the guidance’s legal force, interpretive weight, or effect on any selected rule.', '',
]
for title, text in extracts:
    out += ['## ' + title, '', '> ' + text.replace('\n', '\n> '), '']
out += [
    '## Scope of fresh review', '',
    'The pending-motion and preservation recitations require source classification and procedural treatment in the affected remedy handoff. Separately test whether the conditional burden matters to any selected merits ground. Do not introduce a factual default merely because a paper was not filed. This extraction selects no merits or remedy position.', '',
    'Public source location: https://www.law.cornell.edu/supct/html/97-1754.ZO.html. The clean successor should use this bounded extract rather than open the surrounding historical analysis.', '',
]
target = Path('terms/OT1998/entering-law/OT_1998CHUNK7_AGUIRRE_PROCEDURE_SOURCE_EXTRACT.md')
target.write_text('\n'.join(out), encoding='utf-8', newline='\n')
print(target.as_posix())
print(hashlib.sha256(target.read_bytes()).hexdigest())
