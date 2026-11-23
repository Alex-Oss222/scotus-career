from pathlib import Path
from urllib.request import Request, urlopen
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, io
import logging
from pypdf import PdfReader
logging.getLogger('pypdf').setLevel(logging.ERROR)

BASE = Path(__file__).resolve().parent
SOURCES = {
 'smith-syllabus': 'https://www.law.cornell.edu/supct/html/03-8661.ZS.html',
 'smith-court': 'https://www.law.cornell.edu/supct/html/03-8661.ZO.html',
 'smith-dissent': 'https://www.law.cornell.edu/supct/html/03-8661.ZD.html',
 'stewart-syllabus': 'https://www.law.cornell.edu/supct/html/03-814.ZS.html',
 'stewart-court': 'https://www.law.cornell.edu/supct/html/03-814.ZO.html',
 'smith-official': 'https://tile.loc.gov/storage-services/service/ll/usrep/usrep543/usrep543462/usrep543462.pdf',
 'stewart-official': 'https://tile.loc.gov/storage-services/service/ll/usrep/usrep543/usrep543481/usrep543481.pdf',
 'gdf-panel-official': 'https://www.ca5.uscourts.gov/opinions/pub/01/01-51099.cv0.wpd.pdf',
 'gdf-rehearing-official': 'https://www.ca5.uscourts.gov/opinions/pub/01/01-51099-CV1.wpd.pdf',
 'taft-official': 'https://www.opn.ca6.uscourts.gov/opinions.pdf/03a0446p-06.pdf',
 'karaha-official': 'https://www.ca5.uscourts.gov/opinions/pub/02/02-20042-CV0.wpd.pdf',
}

class Text(HTMLParser):
 def __init__(self):
  super().__init__(); self.parts=[]; self.skip=0
 def handle_starttag(self, tag, attrs):
  if tag in ('script','style'): self.skip += 1
  if tag in ('p','br','div','h1','h2','h3','h4','li','tr','hr'): self.parts.append('\n')
 def handle_endtag(self, tag):
  if tag in ('script','style'): self.skip=max(0,self.skip-1)
  if tag in ('p','div','h1','h2','h3','h4','li','tr'): self.parts.append('\n')
 def handle_data(self, data):
  if not self.skip: self.parts.append(data)

def acquire(item):
 name,url=item
 try:
  body=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read()
  if body.startswith(b'%PDF'):
   reader=PdfReader(io.BytesIO(body))
   text='\n\n'.join(f'--- PDF page {i+1} ---\n'+page.extract_text() for i,page in enumerate(reader.pages))
   (BASE/(name+'.pdf')).write_bytes(body)
   pages=len(reader.pages)
  else:
   parser=Text(); parser.feed(body.decode('utf-8',errors='replace'))
   text='\n'.join(line.strip() for line in ''.join(parser.parts).splitlines() if line.strip())
   if name in ('smith-syllabus','smith-court','smith-dissent','stewart-syllabus','stewart-court'):
    text=text[text.index('SUPREME COURT OF THE UNITED'):]
   pages=None
  (BASE/(name+'.txt')).write_text(text,encoding='utf-8')
  return {'name':name,'url':url,'download_sha256':hashlib.sha256(body).hexdigest(),'text_sha256':hashlib.sha256(text.encode()).hexdigest(),'pages':pages,'characters':len(text),'status':'saved'}
 except Exception as e:
  return {'name':name,'url':url,'status':'error','detail':str(e)}

if __name__=='__main__':
 BASE.mkdir(parents=True,exist_ok=True)
 with ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(acquire,SOURCES.items()))
 (BASE/'source-manifest.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
 for result in results: print(result['name'],result['status'],result.get('pages'),result.get('characters'),result.get('detail',''))
