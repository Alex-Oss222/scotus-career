from pathlib import Path
import urllib.request,json
out=Path('terms/OT1999/sources/chunk6-neutral')
for name,vol,page in [('ross-pre1995',910,1422),('salas-pre1995',980,299)]:
 url=f'https://static.case.law/f2d/{vol}/cases/{page:04d}-01.json'
 data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read()
 obj=json.loads(data);(out/(name+'-cap.json')).write_bytes(data)
 body=obj['casebody']['data'] if 'data' in obj['casebody'] else obj['casebody']
 text='\n\n'.join([obj['name'],obj['decision_date']]+[o.get('text','') for o in body.get('opinions',[])])
 (out/(name+'-cap.txt')).write_text(text,encoding='utf-8')
 (out/(name+'-source.json')).write_text(json.dumps({'source':url,'name':obj['name'],'date':obj['decision_date']},indent=2)+'\n',encoding='utf-8')
 print(name,obj['name'],len(text))
