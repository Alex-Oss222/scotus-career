from pathlib import Path
import hashlib

base = Path('terms/OT1998/sources/chunk7-control')
majority = (base / 'lasalle-ZO.txt').read_text(encoding='utf-8')
separate = (base / 'lasalle-ZD.txt').read_text(encoding='utf-8')

def sentence(text, start, end):
    first = text.index(start)
    last = text.index(end, first) + len(end)
    return text[first:last]

items = [
    ('Exclusivity ruling; published procedural recitation', sentence(majority, 'The Bankruptcy Court rejected the Bank’s motion', 'under §1121(d).5')),
    ('Preservation of exclusivity ruling; published note 5', sentence(majority, '5. The Bank neither appealed', 'as an issue in this appeal.')),
    ('New capital and eligibility; published plan recitation', sentence(majority, '(4) Certain former partners', 'the old equity holders were the only ones who could contribute new capital.11')),
    ('Valuation and other confirmation findings; published recitation at 526 U.S. 467', sentence(separate, 'petitioner does not challenge the Bankruptcy Judge’s valuation', '(other than the plan’s compliance with §1129(b)(2)(B)(ii)).')),
    ('Classification issue; published note 7', sentence(majority, 'The Bank sought no review of that issue', 'which is thus not before us.')),
]
out = ['# LaSalle — objective source extraction for fresh neutral validation', '',
       'Preparation only. The sentences below are mechanically copied from saved primary opinion text. They establish published recitations, not independent review of original briefs or findings. They contain no Supreme Court result, Justice position or reasoning. The classification sentence refers to the separate classification of the bank’s unsecured deficiency from other general unsecured claims. The exclusivity note refers to denial of the bank’s request to end the debtor’s exclusive proposal period.', '',
       'Fresh neutral validation and affected independent modelling are required before use. The prior frozen packet and commitments are preserved. Research cutoff: May 3, 1999.', '']
for label, quote in items:
    out += ['## ' + label, '', '> ' + quote.replace('\n', '\n> '), '']
out += ['## Public-source locations', '',
        '- https://www.law.cornell.edu/supct/html/97-1418.ZO.html — objective plan and procedural recitations and notes 5 and 7.',
        '- https://www.law.cornell.edu/supct/html/97-1418.ZD.html — objective preservation sentence, 526 U.S. 467. A neutral successor must use this extraction rather than open the surrounding historical analysis.', '',
        'The source receipts do not establish an independent appellate dispute over dollar valuation, an appeal of the exclusivity refusal, or a grant on separate classification. They do not determine whether the plan satisfies section 1129(b)(2)(B)(ii).', '']
target = Path('terms/OT1998/entering-law/OT_1998CHUNK7_LASALLE_SOURCE_EXTRACT.md')
target.write_text('\n'.join(out), encoding='utf-8', newline='\n')
print(target.as_posix())
print(hashlib.sha256(target.read_bytes()).hexdigest())
