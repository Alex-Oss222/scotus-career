import argparse
import html.parser
import urllib.request
from pathlib import Path

class Text(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.hide=0
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.hide+=1
        if tag in ('p','div','br','h1','h2','h3','h4','li'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.hide-=1
    def handle_data(self,data):
        if not self.hide: self.parts.append(data)

p=argparse.ArgumentParser(); p.add_argument('name'); p.add_argument('url'); a=p.parse_args()
dest=Path(__file__).parent
req=urllib.request.Request(a.url,headers={'User-Agent':'Mozilla/5.0'})
with urllib.request.urlopen(req,timeout=60) as r: data=r.read()
dest.joinpath(a.name+'.html').write_bytes(data)
t=Text(); t.feed(data.decode('utf-8',errors='replace'))
text='\n'.join(x.strip() for x in ''.join(t.parts).splitlines() if x.strip())
dest.joinpath(a.name+'.txt').write_text(text,encoding='utf-8')
print(a.name,len(data),len(text))
