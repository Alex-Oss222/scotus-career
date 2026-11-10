from pathlib import Path
import urllib.request
from html.parser import HTMLParser
class Text(HTMLParser):
    def __init__(self):super().__init__();self.parts=[];self.skip=0
    def handle_starttag(self,t,a):
        if t in ['script','style']:self.skip+=1
        if t in ['p','div','br','h1','h2','h3','h4','li','pre']:self.parts.append('\n')
    def handle_endtag(self,t):
        if t in ['script','style']:self.skip=max(0,self.skip-1)
    def handle_data(self,d):
        if not self.skip:self.parts.append(d)
out=Path('terms/OT2001/sources/chunk6-a')
for sec in ['12111','12112','12113','12116']:
    url=f'https://www.govinfo.gov/content/pkg/USCODE-2000-title42/html/USCODE-2000-title42-chap126-subchapI-sec{sec}.htm'
    try:
        data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read().decode('utf-8');p=Text();p.feed(data);text='\n'.join(s.strip() for s in ''.join(p.parts).splitlines() if s.strip());(out/f'ada-2000-{sec}.txt').write_text('Source: '+url+'\n\n'+text,encoding='utf-8');print(sec,len(text),flush=True)
    except Exception as e:print(sec,str(e),flush=True)
