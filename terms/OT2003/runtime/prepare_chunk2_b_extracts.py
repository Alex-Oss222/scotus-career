from pathlib import Path

root=Path(__file__).resolve().parents[3]
base=root/'terms/OT2003/sources/chunk2_b'
out=root/'terms/OT2003/runtime/OT_2003CHUNK2_B_SOURCE_EXTRACTS.md'
parts=['# OT2003 chunk 2 B — mechanically copied instrument excerpts\n\nThese selections preserve source text, including extraction artifacts. They are reading copies, not independently authored legal text.']

def between(text,start,end):
    a=text.index(start); b=text.index(end,a)
    return text[a:b].rstrip()

p=(base/'virginia_historical_instruments.txt').read_text(encoding='utf-8')
parts.extend(['## Compact of 1785: Article Seventh\n\nSource: `sources/chunk2_b/virginia_historical_instruments.txt`, Appendix A.',between(p,'Seventh, The citizens','Eighth, All laws')])
parts.extend(['## Compact of 1785: Article Eighth',between(p,'Eighth, All laws','Ninth,')])
parts.extend(['## Compact of 1785: Article Thirteenth',between(p,'Thirteenth, These articles','And whereas')])
parts.extend(['## Congressional approval of the Black-Jenkins Award\n\nSource: the same saved historical instruments, Appendix D. This selection includes the congressional approval and the award, including its fourth paragraph.',p[78030:86258].rstrip()])
p=(base/'potomac_1958_congressional_consent.txt').read_text(encoding='utf-8')
parts.extend(['## Potomac River Compact of 1958: enacted consent and savings\n\nSource: `sources/chunk2_b/potomac_1958_congressional_consent.txt`; Public Law 87-783, 76 Stat. 797 (October 10, 1962). The enacted version controls over the earlier draft in the historical appendix.',between(p,'Resolved hy the Senate','"POTOMAC RIVER COMPACT')])
parts.extend(['## Potomac River Compact of 1958: Articles VII–IX and federal reservations',between(p,'"ARTICLE VII','October 10, 1962 \n[S. 3089]')])
out.write_text('\n\n'.join(parts).rstrip()+'\n',encoding='utf-8')
print(out.relative_to(root))
