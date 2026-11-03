from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
import fitz
import json
base=Path(__file__).resolve().parent
items={'apprendi':466,'dickerson':428}
def fetch(item):
    name,page=item;url=f'https://www.govinfo.gov/content/pkg/USREPORTS-530/pdf/USREPORTS-530-{page}.pdf'
    pdf=base/(name+'-official-control-only.pdf')
    if not pdf.exists():
        req=Request(url,headers={'User-Agent':'Mozilla/5.0'})
        with urlopen(req,timeout=90) as response:pdf.write_bytes(response.read())
    reader=fitz.open(pdf)
    text='\n\n'.join(p.get_text() for p in reader)
    (base/(name+'-official-control-only.txt')).write_text(text,encoding='utf-8')
    return {'name':name,'source':url,'pages':len(reader),'characters':len(text)}
with ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(fetch,items.items()))
(base/'official-comparator-source-map.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
for r in results:print(r['name'],r['pages'],'pages saved; full reading remains for reconciliation')
