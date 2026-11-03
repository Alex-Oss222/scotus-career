from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, urllib.request
from pypdf import PdfReader

root = Path('terms/OT1999/sources/chunk7/reconciliation-a-official')
root.mkdir(parents=True, exist_ok=True)
items = [('98-9828',529,753),('98-1828',529,765),('99-409',530,1),('99-387',530,15)]

def fetch(item):
    docket, volume, page = item
    package = f'USREPORTS-{volume}-{page}'
    url = f'https://www.govinfo.gov/content/pkg/USREPORTS-{volume}/pdf/{package}.pdf'
    request = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
    data = urllib.request.urlopen(request, timeout=50).read()
    if not data.startswith(b'%PDF'):
        raise ValueError(f'Non-PDF response for {url}')
    dest = root / f'{docket}.pdf'
    dest.write_bytes(data)
    reader = PdfReader(dest)
    text = '\n\n'.join(f'--- PDF page {n+1} ---\n{p.extract_text()}' for n,p in enumerate(reader.pages))
    (root / f'{docket}.txt').write_text(text, encoding='utf-8')
    return {'docket':docket,'url':url,'pdf':dest.name,'text':f'{docket}.txt','pages':len(reader.pages),'sha256':hashlib.sha256(data).hexdigest()}

with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(fetch,items))
(root/'sources.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print(json.dumps(results,indent=2))
