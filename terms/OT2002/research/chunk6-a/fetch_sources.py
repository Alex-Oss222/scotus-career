from pathlib import Path
from urllib.request import Request, urlopen
from pypdf import PdfReader
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser

base = Path(__file__).resolve().parent
sources = {
 'wheat-circuit.pdf': 'https://media.ca8.uscourts.gov/opndir/01/12/003457P.pdf',
 'section-841-1994.pdf': 'https://www.govinfo.gov/content/pkg/USCODE-1994-title21/pdf/USCODE-1994-title21-chap13-subchapI-partD-sec841.pdf',
 'buckland-circuit.html': 'https://openjurist.org/289/f3d/558/united-states-v-buckland',
}
class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.skip += 1
        if tag in ('p','div','h1','h2','h3','br'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.skip -= 1
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)
def get(item):
    name,url=item
    try:
        data=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35).read()
        path=base/name; path.write_bytes(data)
        if name.endswith('.pdf'):
            reader=PdfReader(path); text='\n'.join(p.extract_text() or '' for p in reader.pages)
        else:
            parser=Text(); parser.feed(data.decode('utf-8')); text=''.join(parser.parts)
        path.with_suffix('.txt').write_text(text,encoding='utf-8')
        return f'{name}: saved {len(data)} bytes, {len(text)} text characters; {url}'
    except Exception as exc: return f'{name}: {exc}; {url}'
with ThreadPoolExecutor(max_workers=3) as pool:
    results=list(pool.map(get,sources.items()))
(base/'retrieval.txt').write_text('\n'.join(results)+'\n',encoding='utf-8')
print('\n'.join(results))
