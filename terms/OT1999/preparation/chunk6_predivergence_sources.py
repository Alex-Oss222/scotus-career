from pathlib import Path
import urllib.request,concurrent.futures,json,fitz,sys
out=Path('terms/OT1999/sources/chunk6-neutral');out.mkdir(exist_ok=True,parents=True)
items=[('collins',497,37),('hopt',110,574),('thompson-missouri',171,380),('calder',3,386),('civil-rights-cases',109,3),('harris1883',106,629)]
if len(sys.argv)>1:items=[item for item in items if item[0] in sys.argv[1:]]
def fetch(item):
 name,vol,page=item;stem=f'usrep{vol:03d}{page:03d}';url=f'https://tile.loc.gov/storage-services/service/ll/usrep/usrep{vol:03d}/{stem}/{stem}.pdf'
 try:
  data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read()
  if not data.startswith(b'%PDF-'):raise ValueError('Non-PDF response')
  (out/(name+'-official.pdf')).write_bytes(data)
  doc=fitz.open(stream=data,filetype='pdf');txt='\n'.join(p.get_text() for p in doc)
  (out/(name+'-official.txt')).write_text(txt,encoding='utf-8')
  (out/(name+'-official-source.json')).write_text(json.dumps({'source':url,'pages':len(doc),'status':'downloaded full official opinion; interpretation requires reading'},indent=2)+'\n',encoding='utf-8')
  return name,len(doc),len(txt)
 except Exception as e:return name,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for result in pool.map(fetch,items):print(result)
