from pathlib import Path
from html.parser import HTMLParser
import urllib.request
import hashlib
import re
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'terms/OT1996/sources/chunk6-neutral-b'
OUT.mkdir(parents=True,exist_ok=True)
class Text(HTMLParser):
    def __init__(self): super().__init__(); self.rows=[]; self.skip=0
    def handle_starttag(self,t,a):
        if t in ('style','script'): self.skip+=1
        if t in ('p','div','h1','h2','h3','h4','br','li'): self.rows.append('\n')
    def handle_endtag(self,t):
        if t in ('style','script'): self.skip=max(0,self.skip-1)
        if t in ('p','div','h1','h2','h3','h4','li'): self.rows.append('\n')
    def handle_data(self,d):
        if not self.skip:self.rows.append(d)
sources={
'1320a2_1996':'https://www.govinfo.gov/content/pkg/USCODE-1996-title42/html/USCODE-1996-title42-chap6-subchapXI_2-partA-sec1320a-2.htm',
'1320a10_1996':'https://www.govinfo.gov/content/pkg/USCODE-1996-title42/html/USCODE-1996-title42-chap6-subchapXI_2-partA-sec1320a-10.htm',
'654_1994':'https://www.govinfo.gov/content/pkg/USCODE-1994-title42/html/USCODE-1994-title42-chap6-subchapIV_2-partD-sec654.htm',
'654_1996':'https://www.govinfo.gov/content/pkg/USCODE-1996-title42/html/USCODE-1996-title42-chap6-subchapIV_2-partD-sec654.htm',
}
receipt=['# Neutral B primary-source retrieval receipt','']
for name,url in sources.items():
    try:
        data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45).read()
        if b'Page Not Found' in data:
            raise ValueError('GovInfo returned its error page; not statute text')
        (OUT/(name+'.html')).write_bytes(data)
        p=Text(); p.feed(data.decode('utf-8',errors='replace'))
        txt=re.sub(r'\n[ \t]*\n+', '\n\n',''.join(p.rows))
        (OUT/(name+'.txt')).write_text(txt,encoding='utf-8')
        receipt += [f'- {name}: {url}; {len(data)} bytes; SHA-256 `{hashlib.sha256(data).hexdigest()}`.']
        print(name,len(txt))
    except Exception as e:
        receipt += [f'- {name}: {url}; retrieval failed: {e}.']
        print(name,'ERROR',e)
(OUT/'RETRIEVAL.md').write_text('\n'.join(receipt)+'\n',encoding='utf-8')
