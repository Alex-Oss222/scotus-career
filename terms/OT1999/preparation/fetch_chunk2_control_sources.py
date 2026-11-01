from pathlib import Path
import urllib.request, concurrent.futures, pymupdf, json
out=Path('terms/OT1999/preparation/chunk2-control-sources'); out.mkdir(parents=True,exist_ok=True)
pages=[141,152,216,225,250,259,304,320,377]
def get(p):
 url=f'https://www.govinfo.gov/content/pkg/USREPORTS-528/pdf/USREPORTS-528-{p}.pdf'
 req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
 b=urllib.request.urlopen(req,timeout=60).read(); path=out/f'USREPORTS-528-{p}.pdf'; path.write_bytes(b)
 doc=pymupdf.open(path); texts=[f'\n--- PDF PAGE {i+1} ---\n'+page.get_text() for i,page in enumerate(doc)]
 (out/f'USREPORTS-528-{p}.txt').write_text(''.join(texts),encoding='utf-8')
 return {'page':p,'url':url,'pdf':str(path).replace('\\','/'),'text':str(path.with_suffix('.txt')).replace('\\','/'),'pages':len(doc),'chars':sum(map(len,texts))}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: results=list(ex.map(get,pages))
(out/'sources.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
