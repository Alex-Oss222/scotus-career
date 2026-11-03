import json,urllib.request,urllib.parse,concurrent.futures
from pathlib import Path
OUT=Path('terms/OT1999/sources/chunk6-records')
def get(url):
 return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (legal research)'}),timeout=60).read()
for name,item in [('carmell','micro_IA40385014_0295'),('geier','micro_IA40385014_0277')]:
 data=get('https://archive.org/metadata/'+item)
 (OUT/(name+'-metadata.json')).write_bytes(data)
 obj=json.loads(data)
 jobs=[]
 for f in obj['files']:
  fname=f['name']
  if fname.endswith(('_djvu.txt','.pdf')):
   print(name,fname,f.get('size'))
   if 'Opinion' not in fname and 'Docket' not in fname:
    jobs.append((fname,OUT/(name+'-'+fname.split(' ',1)[-1])))
 def save(job):
  fname,target=job
  try:
   target.write_bytes(get('https://archive.org/download/'+item+'/'+urllib.parse.quote(fname)))
   return target.name+' saved'
  except Exception as e: return fname+': '+str(e)
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  for result in pool.map(save,jobs): print(result)
