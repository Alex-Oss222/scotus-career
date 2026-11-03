import json
import urllib.request
from pathlib import Path

folder=Path('terms/OT1999/sources/chunk6-neutral')
for name,volume,page in [('ncrl','168','0705'),('mining','177','0001'),('saenz','183','0389'),('mciver','186','1119')]:
    url=f'https://static.case.law/f3d/{volume}/cases/{page}-01.json'
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as response:
        raw=response.read()
    data=json.loads(raw)
    folder.joinpath(name+'-cap.json').write_bytes(raw)
    body=data['casebody'].get('data',data['casebody'])
    if isinstance(body,str): text=body
    else: text='\n\n'.join([body.get('head_matter','')]+[op.get('text','') for op in body.get('opinions',[])])
    folder.joinpath(name+'-cap.txt').write_text(text,encoding='utf-8')
    folder.joinpath(name+'-cap.source.json').write_text(json.dumps({'url':url,'name':data.get('name'),'date':data.get('decision_date'),'source':'Caselaw Access Project reporter primary text'},indent=2)+'\n',encoding='utf-8')
    print(name,data.get('name'),data.get('decision_date'),len(text))
