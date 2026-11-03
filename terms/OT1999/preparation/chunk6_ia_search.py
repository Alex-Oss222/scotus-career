import json, urllib.parse, urllib.request
from pathlib import Path
OUT=Path('terms/OT1999/sources/chunk6-records')
OUT.mkdir(parents=True,exist_ok=True)
queries={
 'carmell-docket':'collection:us-supreme-court AND ("98-7540")',
 'carmell-name':'collection:us-supreme-court AND (carmell)',
 'geier-docket':'collection:us-supreme-court AND ("98-1811")',
 'geier-name':'collection:us-supreme-court AND (geier)',
}
for name,q in queries.items():
 url='https://archive.org/advancedsearch.php?'+urllib.parse.urlencode({'q':q,'output':'json','rows':50,'fl[]':['identifier','title']},doseq=True)
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (legal research)'})
  data=urllib.request.urlopen(req,timeout=60).read()
  (OUT/(name+'-search.json')).write_bytes(data)
  obj=json.loads(data)
  print(name,obj.get('response',{}))
 except Exception as e: print(name,type(e).__name__,str(e))
