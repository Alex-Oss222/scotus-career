from pathlib import Path
import urllib.request,concurrent.futures,json,fitz
out=Path('terms/OT1999/sources/chunk6-neutral')
items=[('medicare-41360','CFR-1999-title42-vol2','413-60'),('medicare-41364','CFR-1999-title42-vol2','413-64'),('grazing-definitions','CFR-1995-title43-vol2','4100-0-5'),('grazing-qualifications','CFR-1995-title43-vol2','4110-1'),('grazing-improvements','CFR-1995-title43-vol2','4120-3-2'),('grazing-permits','CFR-1995-title43-vol2','4130-2'),('grazing-nonuse','CFR-1995-title43-vol2','4130-4')]
def fetch(it):
 name,pkg,sec=it;url=f'https://www.govinfo.gov/content/pkg/{pkg}/pdf/{pkg}-sec{sec}.pdf'
 try:
  data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read()
  if not data.startswith(b'%PDF-'):raise ValueError('Server returned non-PDF; not a recovered provision')
  doc=fitz.open(stream=data,filetype='pdf')
  (out/(name+'.pdf')).write_bytes(data);(out/(name+'.txt')).write_text('\n'.join(p.get_text() for p in doc),encoding='utf-8');(out/(name+'-source.json')).write_text(json.dumps({'source':url,'pages':len(doc)},indent=2)+'\n',encoding='utf-8')
  return name,len(doc)
 except Exception as e:return name,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
 for result in pool.map(fetch,items):print(result)
