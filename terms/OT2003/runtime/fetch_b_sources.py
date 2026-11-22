from pathlib import Path
from urllib.request import Request,urlopen
from pypdf import PdfReader
import io
dest=Path('terms/OT2003/runtime/neutral-sources-b'); dest.mkdir(parents=True,exist_ok=True)
sources={
'duro-1990':'https://www.govinfo.gov/content/pkg/USREPORTS-495/pdf/USREPORTS-495-676.pdf',
'wheeler-1978':'https://www.govinfo.gov/content/pkg/USREPORTS-435/pdf/USREPORTS-435-313.pdf',
'title25-2000-1301':'https://www.govinfo.gov/content/pkg/USCODE-2000-title25/pdf/USCODE-2000-title25-chap15-subchapI-sec1301.pdf',
'fpa203-2000':'https://www.govinfo.gov/content/pkg/USCODE-2000-title16/pdf/USCODE-2000-title16-chap12-subchapII-sec824b.pdf',
}
for name,url in sources.items():
    try:
        data=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read()
        (dest/(name+'.pdf')).write_bytes(data)
        reader=PdfReader(io.BytesIO(data))
        text='\n'.join(f'\nPAGE {n+1}\n'+page.extract_text() for n,page in enumerate(reader.pages))
        (dest/(name+'.txt')).write_text(text,encoding='utf-8')
        print(name,len(reader.pages),len(text))
    except Exception as exc: print(name,type(exc).__name__,str(exc))
