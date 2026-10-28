from pathlib import Path
ROOT=Path(__file__).resolve().parent
t=(ROOT/'cfr1998-part10.txt').read_text(encoding='utf-8')
a=t.index('§ 10.13 Statutory'); b=t.index('§ 10.14 Fabricated',a)
c=t.index('(b) Operations incidental to the assem-',b); d=t.index('(d) Joining of American-made',c)
op=(ROOT/'haggar-ZO.txt').read_text(encoding='utf-8')
clause='make its determinations upon the basis of the record made before the court'
assert clause in op
out='# Haggar neutral statutory source extracts\n\nMechanically copied from official 19 C.F.R. Part 10 (April 1, 1998), §§10.13 and 10.16(b)–(c). PDF line breaks and page furniture remain. No adjudicative source reasoning is included.\n\nSource: https://www.govinfo.gov/content/pkg/CFR-1998-title19-vol1/pdf/CFR-1998-title19-vol1-part10.pdf\n\n```text\n'+t[a:b]+'\n'+t[c:d]+'\n```\n\nThe relevant §2640(a) clause, mechanically copied from its contemporaneous judicial quotation, is: “'+clause+'”. The source excerpt does not quote subsection (a)(1) in full; the extraction does not certify omitted statutory text.\n'
dest=ROOT.parents[1]/'entering-law'/'OT_1998CHUNK7_HAGGAR_STATUTES_NEUTRAL.md'
dest.write_text(out,encoding='utf-8')
print(dest.name)
