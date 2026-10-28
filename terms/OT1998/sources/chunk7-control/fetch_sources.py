from urllib.request import Request, urlopen
from html.parser import HTMLParser
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json

ROOT = Path(__file__).resolve().parent
class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.out=[]; self.skip=0
    def handle_starttag(self, tag, attrs):
        if tag in ('style','script'): self.skip += 1
        if tag in ('p','div','br','hr','h1','h2','h3','h4','li','tr'): self.out.append('\n')
    def handle_endtag(self, tag):
        if tag in ('style','script'): self.skip -= 1
        if tag in ('p','div','li','tr'): self.out.append('\n')
    def handle_data(self, data):
        if not self.skip: self.out.append(data)
def fetch(spec):
    name,url=spec
    try:
        data=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 (source verification)'}),timeout=45).read()
        (ROOT/(name+'.html')).write_bytes(data)
        parser=Text(); parser.feed(data.decode('utf-8',errors='replace'))
        lines=[' '.join(l.split()) for l in ''.join(parser.out).splitlines()]
        text='\n'.join(l for l in lines if l)+'\n'
        (ROOT/(name+'.txt')).write_text(text,encoding='utf-8')
        return {'name':name,'url':url,'characters':len(text)}
    except Exception as e: return {'name':name,'url':url,'error':str(e)}
if __name__ == '__main__':
    specs=[]
    for name,docket,writings in [
        ('unum','97-1868',['ZS','ZO']),
        ('haggar','97-2044',['ZS','ZO','ZC']),
        ('sun-diamond','98-131',['ZS','ZO']),
        ('aguirre','97-1754',['ZS','ZO']),
        ('lasalle','97-1418',['ZS','ZO','ZC','ZD']),
        ('el-paso','98-6',['ZS','ZO']),
        ('saenz','98-97',['ZS','ZO','ZD','ZD1']),
        ('rubin','98-93',['ZD'])]:
        for suffix in writings: specs.append((name+'-'+suffix,'https://www.law.cornell.edu/supct/html/'+docket+'.'+suffix+'.html'))
    specs += [('russell','https://openjurist.org/146/f3d/563/russell-v-burris-pac-russell-r'),('sealed','https://openjurist.org/148/f3d/1073')]
    results=list(ThreadPoolExecutor(max_workers=8).map(fetch,specs))
    (ROOT/'source-manifest.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
    for r in results: print(r)
