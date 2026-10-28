from urllib.request import Request, urlopen
from pathlib import Path
from pypdf import PdfReader
from concurrent.futures import ThreadPoolExecutor
ROOT=Path(__file__).resolve().parent
def fetch(spec):
    name,url=spec
    try:
        data=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=90).read()
        p=ROOT/(name+'.pdf'); p.write_bytes(data)
        reader=PdfReader(p)
        (ROOT/(name+'.txt')).write_text('\n'.join('PAGE '+str(i+1)+'\n'+page.extract_text() for i,page in enumerate(reader.pages)),encoding='utf-8')
        return name,len(reader.pages)
    except Exception as e: return name,str(e)
if __name__=='__main__':
    specs=[('official-526','https://www.supremecourt.gov/opinions/boundvolumes/526bv.pdf'),('russell-official','https://ecf.ca8.uscourts.gov/opndir/98/06/973922P.pdf'),('cfr1998-part10','https://www.govinfo.gov/content/pkg/CFR-1998-title19-vol1/pdf/CFR-1998-title19-vol1-part10.pdf')]
    for r in ThreadPoolExecutor(max_workers=3).map(fetch,specs): print(r)
