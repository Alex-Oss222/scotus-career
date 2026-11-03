from pathlib import Path
import urllib.request, urllib.parse, json, re
p=Path(__file__).parent
items={'castillo':('micro_IA40385014_0343','08. Respondents Brief'),'sims':('micro_IA40385014_0311','Respondents Brief'),'hubbell':('micro_IA40385014_0327','07. Petitioners Brief'),'harris':('micro_IA40385014_0341','09. Respondents Brief')}
manifest=[]
for case,(ident,part) in items.items():
 d=json.load(urllib.request.urlopen('https://archive.org/metadata/'+ident))
 fs=[f['name'] for f in d['files'] if f['name'].endswith('_djvu.txt') and part in f['name']]
 if not fs: print(case,'NOT FOUND');continue
 f=fs[0];u='https://archive.org/download/'+ident+'/'+urllib.parse.quote(f)
 t=urllib.request.urlopen(u).read().decode();(p/(case+'-opposing-merits.txt')).write_text(t,encoding='utf-8')
 manifest.append({'case':case,'source':u,'file':case+'-opposing-merits.txt','full_text_bytes':len(t)})
 print(case,len(t))
 matches=list(re.finditer('SUMMARY OF (?:THE )?ARGUMENT',t,re.I))
 print('summary positions',[m.start() for m in matches])
 if matches: print(t[matches[-1].start():matches[-1].start()+6500])
(p/'opposing-source-map.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
