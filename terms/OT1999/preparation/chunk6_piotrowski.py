from pathlib import Path
import urllib.request,json
folder=Path('terms/OT1999/sources/chunk6-neutral');url='https://static.case.law/f3d/51/cases/0512-01.json'
data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45).read();obj=json.loads(data)
body=obj['casebody'].get('data',obj['casebody'])
folder.joinpath('piotrowski-preconduct-cap.json').write_bytes(data)
folder.joinpath('piotrowski-preconduct-cap.txt').write_text('\n\n'.join([obj['name'],obj['decision_date']]+[o['text'] for o in body['opinions']]),encoding='utf-8')
folder.joinpath('piotrowski-preconduct-source.json').write_text(json.dumps({'source':url,'name':obj['name'],'date':obj['decision_date']},indent=2)+'\n',encoding='utf-8')
print(obj['name'],obj['decision_date'])
