from pathlib import Path
import urllib.request,pymupdf
p=Path('terms/OT1999/preparation/chunk2-control-sources/PLAW-106publ69.pdf')
url='https://www.govinfo.gov/content/pkg/PLAW-106publ69/pdf/PLAW-106publ69.pdf'
p.write_bytes(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})).read())
doc=pymupdf.open(p); s='\n'.join(x.get_text() for x in doc); p.with_suffix('.txt').write_text(s,encoding='utf-8')
a=s.index('SEC. 350.'); b=s.index('SEC. 351.',a); t=s[a:b]
Path('terms/OT1999/preparation/OT_1999CHUNK2_DPPA_SECTION350.txt').write_text(t,encoding='utf-8')
print(t)
