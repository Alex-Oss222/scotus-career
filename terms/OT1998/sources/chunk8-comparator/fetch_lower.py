from pathlib import Path
import urllib.request,re,html
out=Path('terms/OT1998/sources/chunk8-comparator')
for n,u in [('maine','https://law.resource.org/pub/us/case/reporter/F3/173/173.F3d.1.98-1309.html'),('berger','https://openjurist.org/129/f3d/505/berger-v-c-hanlon')]:
 try:
  b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read();(out/(n+'.html')).write_bytes(b)
  t=b.decode('utf-8',errors='replace');t=re.sub(r'<(script|style)\b.*?</\1>','',t,flags=re.S|re.I);t=html.unescape(re.sub('<[^>]+>','\n',t));t=re.sub(r'\n\s*\n+','\n\n',t)
  (out/(n+'.txt')).write_text(t,encoding='utf-8'); print(n,len(b))
 except Exception as e:print(n,type(e).__name__,str(e))
p=Path('terms/OT1998/sources/chunk8-comparator-extract.py');p.write_text(p.read_text(encoding='utf-8').replace('doc[712]','doc[713]'),encoding='utf-8')
