from pathlib import Path
import re,hashlib
b=Path('terms/OT2004/research/chunk3-control')
s=(b/'ohio-2919.151-2000.txt').read_text(encoding='utf-8')
stat=s[s.index('(A) As used in this section:'):s.index('Available Versions of this Section')].strip()
t=(b/'taft-official.txt').read_text(encoding='utf-8');p=re.split(r'--- PDF page \d+ ---',t)
def take(page,a,z):
    x=p[page]; i=x.index(a); j=x.index(z,i)+len(z); return x[i:j]
extracts=[
('Divisions (B) and (C), composite quotation; printed p. 7 / PDF p. 4',take(4,'When the fetus','function.')),
('Division (A)(3), procedure definition and sequential elements; printed p. 8 / PDF p. 4',take(4,'“the medical','(d) Completion of the vaginal delivery of the fetus.')),
('Division (A)(5), definition; printed p. 9 / PDF p. 5',take(5,'“an y','function.”')),
('Division (A)(1), exclusion of extraction from evacuation definition; printed p. 9 / PDF p. 5',take(5,'“‘[d]ilation','extraction procedure of abortion.”')),
('Division (G), prior act causing death; printed p. 9 / PDF p. 5',take(5,'“does\nnot apply','after it is partially born.”')),
('Division (A)(4), partially born; printed p. 9 / PDF p. 5',take(5,'“that the portion','from the body of the mother.”')),
('Division (A)(2), body boundary; printed p. 9 / PDF p. 5',take(5,'“‘[f]rom','vaginal delivery .”')),
('Division (F), explicit method exclusions; printed p. 27 / PDF p. 14',take(14,'“This\nsection does not prohibit','dilation and evacuation procedure of abortion.”')),
]
head='''# Ohio statute: mechanically copied source extracts

This preparation artifact contains statutory text only. It supplies no judicial outcome, reasoning, vote, or proposed disposition. Section 1 copies the complete historically applicable provision from the official Ohio Laws August 18, 2000 version. Section 2 preserves the quotations as extracted from the saved official Sixth Circuit opinion, including its spacing artifacts and bracketed composite of (B) and (C). No long quotation was manually retyped.

## 1. Complete official historical provision

Source: https://codes.ohio.gov/ohio-revised-code/section-2919.151/8-18-2000 . Saved source: `ohio-2919.151-2000.html`; deterministic text extraction: `ohio-2919.151-2000.txt`. The official page identifies August 18, 2000 and House Bill 351, 123rd General Assembly. Paragraph identifiers below are the enacted identifiers. Its (A)(6) cross-reference is retained; it is not silently expanded using current statutory text.

```text
'''
out=head+stat+'\n```\n\n## 2. Quotations appearing in the official Taft opinion\n\nSource: https://www.opn.ca6.uscourts.gov/opinions.pdf/03a0446p-06.pdf . Saved source: `taft-official.pdf` and `taft-official.txt`. The PDF prints two opinion pages on each PDF page. The opinion uses the citation form 2919.15.1; the official code uses 2919.151. Only quoted statutory words are copied below; the surrounding judicial construction is omitted.\n\n'
for name,x in extracts:out+='### '+name+'\n\n```text\n'+x+'\n```\n\n'
out+='## Reproduction receipt\n\nThe complete provision is an exact substring of the saved official text; each opinion quotation is an exact substring of its indicated saved PDF-page text. Extraction is reproducible with `build_ohio_extract.py`. The opinion does not quote every paragraph of the statute; the official historical provision supplies (A)(6), (D), and (E), as well as separate unmerged (B) and (C).\n'
(b/'OHIO_STATUTE_EXTRACT.md').write_text(out,encoding='utf-8')
print('OHIO_STATUTE_EXTRACT.md written;',len(stat),'official statutory characters;',len(extracts),'exact opinion excerpts.')
