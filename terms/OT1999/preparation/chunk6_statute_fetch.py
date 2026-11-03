from pathlib import Path
import urllib.request,concurrent.futures,json,fitz
out=Path('terms/OT1999/sources/chunk6-neutral');out.mkdir(exist_ok=True,parents=True)
packages=[
('code1994-666','USCODE-1994-title18','USCODE-1994-title18-partI-chap31-sec666'),
('code1994-3583','USCODE-1994-title18','USCODE-1994-title18-partII-chap227-subchapD-sec3583'),
('code1994-13981','USCODE-1994-title42','USCODE-1994-title42-chap136-subchapIII-partC-sec13981'),
('code1994-844','USCODE-1994-title18','USCODE-1994-title18-partI-chap40-sec844'),
('code1994-315','USCODE-1994-title43','USCODE-1994-title43-chap8A-subchapI-sec315'),
('code1994-315a','USCODE-1994-title43','USCODE-1994-title43-chap8A-subchapI-sec315a'),
('code1994-315b','USCODE-1994-title43','USCODE-1994-title43-chap8A-subchapI-sec315b'),
('code1994-30103','USCODE-1994-title49','USCODE-1994-title49-subtitleVI-partA-chap301-subchapI-sec30103'),
]
def fetch(it):
 name,pkg,key=it;url=f'https://www.govinfo.gov/content/pkg/{pkg}/pdf/{key}.pdf'
 try:
  data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read()
  if not data.startswith(b'%PDF-'):raise ValueError('Server returned non-PDF; not a recovered statute')
  (out/(name+'.pdf')).write_bytes(data);doc=fitz.open(stream=data,filetype='pdf')
  (out/(name+'.txt')).write_text('\n'.join(p.get_text() for p in doc),encoding='utf-8')
  (out/(name+'-source.json')).write_text(json.dumps({'source':url,'pages':len(doc),'edition':'1994 historical edition; annotations distinguish later amendments'},indent=2)+'\n',encoding='utf-8')
  return name,len(doc)
 except Exception as e:return name,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
 for result in pool.map(fetch,packages):print(result)
