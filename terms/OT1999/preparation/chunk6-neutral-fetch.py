"""Fetch expressly selected neutral sources; no repository discovery."""
import json
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.ignore=0
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.ignore+=1
        if tag in ('p','div','br','h1','h2','h3','li','article','section'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style') and self.ignore: self.ignore-=1
        if tag in ('p','div','li','article','section'): self.parts.append('\n')
    def handle_data(self, data):
        if not self.ignore: self.parts.append(data)

folder=Path('terms/OT1999/sources/chunk6-neutral')
folder.mkdir(parents=True,exist_ok=True)
name,url=sys.argv[1:3]
req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req,timeout=45) as response:
        data=response.read(); status=response.status
    raw=data.decode('utf-8',errors='replace')
    folder.joinpath(name+'.html').write_text(raw,encoding='utf-8')
    parser=Text(); parser.feed(raw)
    folder.joinpath(name+'.txt').write_text('\n'.join(line.strip() for line in ''.join(parser.parts).splitlines() if line.strip()),encoding='utf-8')
    folder.joinpath(name+'.source.json').write_text(json.dumps({'url':url,'status':status,'bytes':len(data)},indent=2)+'\n',encoding='utf-8')
    print(name,status,len(data))
except Exception as exc:
    print(name,type(exc).__name__,str(exc)); sys.exit(1)
