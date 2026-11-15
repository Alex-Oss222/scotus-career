from pathlib import Path
from html.parser import HTMLParser
import urllib.request
import urllib.parse
import json

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'terms/OT2003/sources/chunk2_b'
OUT.mkdir(parents=True,exist_ok=True)
class Plain(HTMLParser):
    def __init__(self): super().__init__(); self.parts=[]
    def handle_data(self,data): self.parts.append(data)
    def handle_starttag(self,tag,attrs):
        if tag in ('p','h4','h3','h2','aside','section','article'): self.parts.append('\n\n')
def read(url):
    return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read().decode()
for name,vol,page in [('van_susteren','331','1024'),('deaton','332','0698'),('banks','282','0699'),('hernandez','298','1030'),('castro','290','1270')]:
    url=f'https://static.case.law/f3d/{vol}/html/{page}-01.html'
    parser=Plain(); parser.feed(read(url))
    body='\n'.join(line.strip() for line in ''.join(parser.parts).splitlines() if line.strip())
    (OUT/(name+'_lower.txt')).write_text('Source: '+url+'\n\n'+body+'\n',encoding='utf-8')
    print(name,len(body),'characters')
queries=['collection:us-supreme-court AND (identifier:*02-473* OR title:(Banks))','collection:us-supreme-court AND (identifier:*02-749* OR title:(Hernandez))','collection:us-supreme-court AND (identifier:*02-809* OR title:(Pringle))','collection:us-supreme-court AND (identifier:*02-6683* OR title:(Castro))','collection:us-supreme-court AND title:(Virginia Maryland)']
results=[]
for q in queries:
    url='https://archive.org/advancedsearch.php?'+urllib.parse.urlencode({'q':q,'fl[]':['identifier','title'],'rows':100,'output':'json'},doseq=True)
    try:
        result=json.loads(read(url)); docs=result.get('response',{}).get('docs',[])
        results.append({'query':q,'matches':docs,'count':result.get('response',{}).get('numFound')})
    except Exception as exc: results.append({'query':q,'error':str(exc)})
(OUT/'archive_search.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
