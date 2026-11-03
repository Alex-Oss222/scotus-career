from pathlib import Path
import re
folder=Path('terms/OT1999/sources/chunk6-comparator')
out=Path('terms/OT1999/entering-law/OT_1999CHUNK6_STATUTORY_EXTRACTS.md')
parts=['# Neutral statutory reading extracts','Exact quotation blocks mechanically copied from saved source text. These blocks reproduce provisions, not a historical Supreme Court ruling. Original source files are held by control and are not authorized independent-model inputs. Ellipses in source quotations remain ellipses; the separately saved official historical Code and CFR pages supply fuller provisions. No legal inference is supplied here.']
selected=[
('18 U.S.C. 666(a)–(c)','fischer-99-116',77,97),
('Offense-date 18 U.S.C. 3583(e)(1)–(3), as quoted (source ellipses retained)','johnson-99-5153',90,94),
('Former grazing preference definition','public-lands-98-1991',106,106),
('1995 grazing preference definition','public-lands-98-1991',110,110),
('1995 permitted-use definition','public-lands-98-1991',114,114),
('Safety Act original express-preemption clause','geier-98-1811',63,63),
('Cable section 505','playboy-98-1682',174,186),
('Cable section 504','playboy-98-1682',188,196),
]
for title,key,start,end in selected:
 lines=(folder/(key+'.ZO.txt')).read_text(encoding='utf-8').splitlines()
 excerpt='\n'.join(lines[start-1:end]).strip()
 docket=re.search(r'\d{2}-\d+',key).group()
 parts += ['## '+title,'Source: https://www.law.cornell.edu/supct/html/'+docket+'.ZO.html ; only copied provision text below is an authorized neutral input.',excerpt]
geier=(folder/'geier-98-1811.ZO.txt').read_text(encoding='utf-8')
paragraph=geier.splitlines()[66]
quotes=re.findall('“([^”]+)”',paragraph)
fragments=[q for q in quotes if q.startswith('[c]ompliance') or q.startswith('does not exempt')]
assert len(fragments)==2
parts+=['## Safety Act original saving-clause quotation fragments','Source: https://www.law.cornell.edu/supct/html/98-1811.ZO.html . These two fragments are separated in the source; this is not a complete clause. The complete 1994 recodified provision is in code1994-30103.txt.', '\n\n'.join(fragments)]
out.write_text('\n\n'.join(parts)+'\n',encoding='utf-8');print(out.as_posix())
