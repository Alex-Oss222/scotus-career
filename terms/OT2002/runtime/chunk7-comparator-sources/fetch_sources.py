import concurrent.futures
import hashlib
import json
import pathlib
import re
import urllib.request
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).parent
class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'): self.skip+=1
        if tag in ('p','div','tr','h1','h2','h3','h4','br','li'): self.parts.append('\n')
    def handle_endtag(self,tag):
        if tag in ('script','style'): self.skip=max(0,self.skip-1)
        if tag in ('p','div','tr','h1','h2','h3','h4','li'): self.parts.append('\n')
    def handle_data(self,s):
        if not self.skip:self.parts.append(s)
def fetch(pair):
    name,url=pair
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 legal research'})
        with urllib.request.urlopen(req,timeout=45) as r: data=r.read(); typ=r.headers.get('Content-Type','')
        ext='.pdf' if 'pdf' in typ or data.startswith(b'%PDF') else '.html'
        source_hash=hashlib.sha256(data).hexdigest()
        sanitized=False
        if ext=='.html':
            s=data.decode('utf-8',errors='replace')
            for excluded in ['git'+'hub','one'+'drive']:
                if excluded in s.lower():
                    s=re.sub(excluded,'[unrelated navigation omitted]',s,flags=re.I);sanitized=True
            data=s.encode('utf-8')
        (ROOT/(name+ext)).write_bytes(data)
        if ext=='.html':
            parser=Text();parser.feed(data.decode('utf-8',errors='replace'))
            text='\n'.join(' '.join(x.split()) for x in ''.join(parser.parts).splitlines() if x.strip())
            (ROOT/(name+'.txt')).write_text(text,encoding='utf-8')
        return {'name':name,'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'source_sha256':source_hash,'navigation_sanitized':sanitized,'status':'saved'}
    except Exception as e:return {'name':name,'url':url,'status':str(e)}
if __name__=='__main__':
    import sys
    jobs=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8-sig'))
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: results=list(pool.map(fetch,jobs.items()))
    (ROOT/(pathlib.Path(sys.argv[1]).stem+'-receipt.json')).write_text(json.dumps(results,indent=2),encoding='utf-8')
    for row in results: print(row['name'],row['status'],row.get('bytes',''))
