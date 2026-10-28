from pathlib import Path
import urllib.request, re, json, hashlib
from concurrent.futures import ThreadPoolExecutor
from html import unescape
base = Path('terms/OT1998/runtime/chunk9-control')
sources = base / 'historical-sources'
sources.mkdir(exist_ok=True)
cases = {'97-2048':('osullivan',526,838),'98-830':('amoco',526,865),'97-1121':('morales',527,41),'98-5881':('lilly',527,116),'98-377':('zurko',527,150),'98-387':('greater-new-orleans',527,173),'98-727':('cunningham',527,198)}
def fetch(url,path):
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (source verification)'})
    with urllib.request.urlopen(req,timeout=60) as r: data=r.read()
    path.write_bytes(data)
    return data
manifest=[]
def one(item):
    docket,(name,vol,page)=item
    found=[]
    url=f'https://www.law.cornell.edu/supct/html/{docket}.ZS.html'
    path=sources/f'{docket}.ZS.html'
    raw=fetch(url,path)
    links=sorted(set(re.findall(rf'{docket}\.Z[A-Z0-9]*\.html',raw.decode('utf-8',errors='replace'))))
    for fn in links:
        u=f'https://www.law.cornell.edu/supct/html/{fn}'
        p=sources/fn
        data=raw if fn==path.name else fetch(u,p)
        txt=unescape(re.sub(r'<[^>]+>', '\n', data.decode('utf-8', errors='replace')))
        txt=re.sub(r'\n\s*\n+', '\n\n', txt).strip()
        (sources/f'{fn}.txt').write_text(txt,encoding='utf-8')
        found.append({'docket':docket,'url':u,'file':p.as_posix(),'sha256':hashlib.sha256(data).hexdigest(),'text_chars':len(txt)})
    pdfurl=f'https://tile.loc.gov/storage-services/service/ll/usrep/usrep{vol}/usrep{vol}{page:03d}/usrep{vol}{page:03d}.pdf'
    pdf=sources/f'usrep{vol}{page:03d}.pdf'
    try:
        data=fetch(pdfurl,pdf)
        import fitz
        with fitz.open(pdf) as doc:
            txt='\n\n'.join(f'PDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc))
        pdf.with_suffix('.txt').write_text(txt,encoding='utf-8')
        found.append({'docket':docket,'url':pdfurl,'file':pdf.as_posix(),'sha256':hashlib.sha256(data).hexdigest(),'text_chars':len(txt)})
    except Exception as e: found.append({'docket':docket,'pdf_error':str(e),'url':pdfurl})
    return found
with ThreadPoolExecutor(max_workers=7) as pool:
    for rows in pool.map(one,cases.items()): manifest.extend(rows)
(sources/'source-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps(manifest,indent=2))

