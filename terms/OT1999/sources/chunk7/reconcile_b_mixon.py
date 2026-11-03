from pathlib import Path
import urllib.request
from html.parser import HTMLParser
class Extract(HTMLParser):
    def __init__(self): super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'): self.skip+=1
    def handle_endtag(self,tag):
        if tag in ('script','style'): self.skip=max(0,self.skip-1)
    def handle_data(self,data):
        if not self.skip and data.strip(): self.parts.append(data.strip())
base=Path('terms/OT1999/sources/chunk7/reconciliation-b-official')
for name,url in [('mixon-ca6','https://openjurist.org/193/f3d/389/tanya-mixon-v-the-state-of-ohio-and-michael-white'),('spivey-district','https://www.casemine.com/judgement/us/59148102add7b0493447ce95')]:
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
    data=urllib.request.urlopen(req,timeout=45).read()
    (base/(name+'.html')).write_bytes(data)
    parser=Extract(); parser.feed(data.decode('utf-8')); text='\n'.join(parser.parts)
    (base/(name+'.txt')).write_text(text,encoding='utf-8')
    print(name,len(text),url)
