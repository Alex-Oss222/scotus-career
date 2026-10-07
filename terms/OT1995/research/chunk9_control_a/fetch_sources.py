from pathlib import Path
import urllib.request
import re,html,subprocess
import concurrent.futures

BASE=Path(__file__).parent
SOURCES={
 'lane_syllabus':'https://www.law.cornell.edu/supct/html/95-365.ZS.html',
 'lane_court':'https://www.law.cornell.edu/supct/html/95-365.ZO.html',
 'lane_stevens':'https://www.law.cornell.edu/supct/html/95-365.ZD.html',
 'cfi_syllabus':'https://www.law.cornell.edu/supct/html/95-325.ZS.html',
 'cfi_court':'https://www.law.cornell.edu/supct/html/95-325.ZO.html',
 'cfi_thomas':'https://www.law.cornell.edu/supct/html/95-325.ZX.html',
 'brown_syllabus':'https://www.law.cornell.edu/supct/html/95-388.ZS.html',
 'brown_court':'https://www.law.cornell.edu/supct/html/95-388.ZO.html',
 'brown_stevens':'https://www.law.cornell.edu/supct/html/95-388.ZD.html',
 'cfi_below':'https://law.resource.org/pub/us/case/reporter/F3/053/53.F3d.1155.94-4036.94-4034.html',
 'brown_below':'https://openjurist.org/50/f3d/1041',
 'lane_794':'https://www.govinfo.gov/content/pkg/USCODE-1994-title29/html/USCODE-1994-title29-chap16-subchapV-sec794.htm',
 'lane_794a':'https://www.govinfo.gov/content/pkg/USCODE-1994-title29/html/USCODE-1994-title29-chap16-subchapV-sec794a.htm',
 'cfi_507_1993':'https://uscode.house.gov/view.xhtml?req=granuleid:USC-1993-title11-section507&num=0&edition=1993',
 'cfi_510_1993':'https://uscode.house.gov/view.xhtml?req=granuleid:USC-1993-title11-section510&num=0&edition=1993',
 'cfi_4971_1993':'https://uscode.house.gov/view.xhtml?req=granuleid:USC-1993-title26-section4971&num=0&edition=1993',
 'lane_loc':'https://tile.loc.gov/storage-services/service/ll/usrep/usrep518/usrep518187/usrep518187.pdf',
 'cfi_loc':'https://tile.loc.gov/storage-services/service/ll/usrep/usrep518/usrep518213/usrep518213.pdf',
 'brown_loc':'https://tile.loc.gov/storage-services/service/ll/usrep/usrep518/usrep518231/usrep518231.pdf',
}
def fetch(item):
 name,url=item
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (source research)'}),timeout=40) as r: data=r.read(); typ=r.headers.get('Content-Type','')
  if 'pdf' in typ or url.endswith('.pdf'):
   (BASE/(name+'.pdf')).write_bytes(data)
   import fitz
   doc=fitz.open(stream=data,filetype='pdf'); s='\n'.join(p.get_text() for p in doc)
  else:
   raw=data.decode('utf-8','replace'); (BASE/(name+'.html')).write_text(raw,encoding='utf-8')
   raw=re.sub(r'<(script|style)\b[^>]*>.*?</\1>','',raw,flags=re.S|re.I)
   s=html.unescape(re.sub(r'<[^>]+>',' ',raw)); s=re.sub(r'\s+',' ',s)
  (BASE/(name+'.txt')).write_text(url+'\n\n'+s,encoding='utf-8')
  return f'{name}: {len(s)} chars'
 except Exception as e: return f'{name}: ERROR {e}'
if __name__=='__main__':
 for result in concurrent.futures.ThreadPoolExecutor(max_workers=8).map(fetch,SOURCES.items()): print(result)
