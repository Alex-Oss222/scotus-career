from pathlib import Path
import re,difflib,json,hashlib
base=Path('terms/OT1999/sources/chunk7')
items=[(120,'99-658',['ZS','ZO']),(103,'98-9537',['ZS','ZO','ZC','ZD']),(57,'99-138',['ZS','ZO','ZC','ZC1','ZD','ZD1','ZD2']),(27,'99-166',['ZS','ZO','ZC']),(238,'99-579',['ZS','ZO'])]
manifest=[]
for page,docket,suffixes in items:
    official=(base/'reconciliation-b-official'/f'USREPORTS-530-{page}.txt').read_text(encoding='utf-8')
    cornell='\n'.join((base/'control-opinions'/f'{docket}.{s}.txt').read_text(encoding='utf-8') for s in suffixes)
    def norm(s):
        s=re.sub(r'(?<=\w)[\-\u00ad]\s*\n\s*(?=\w)','',s)
        return re.findall(r'[\w]+',s.lower())
    a,b=norm(cornell),norm(official)
    matcher=difflib.SequenceMatcher(None,a,b,autojunk=False)
    chunks=[]
    for tag,i,j,k,l in matcher.get_opcodes():
        if tag!='equal' and l>k: chunks.append(' '.join(b[k:l]))
    diff=base/'reconciliation-b-official'/f'USREPORTS-530-{page}-collation.txt'
    diff.write_text('\n'.join(chunks),encoding='utf-8')
    manifest.append({'page':page,'docket':docket,'url':f'https://www.govinfo.gov/content/pkg/USREPORTS-530/pdf/USREPORTS-530-{page}.pdf','official_words':len(b),'collation_words':sum(len(x.split()) for x in chunks),'sha256':hashlib.sha256((base/'reconciliation-b-official'/f'USREPORTS-530-{page}.pdf').read_bytes()).hexdigest(),'cornell_suffixes':suffixes})
(base/'reconciliation-b-official'/'sources.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps(manifest,indent=2))
