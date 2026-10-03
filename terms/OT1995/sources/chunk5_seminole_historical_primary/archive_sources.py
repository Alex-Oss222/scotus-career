#!/usr/bin/env python3
"""Archive raw public opinion sources and unabridged extraction products only."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import subprocess
import sys

BASE = Path(__file__).resolve().parents[1]
CASES = {
    'seminole': {'case': 'Seminole Tribe of Florida v. Florida', 'docket': '94-12', 'citation': '517 U.S. 44', 'page': 44},
    'morse': {'case': 'Morse v. Republican Party of Virginia', 'docket': '94-203', 'citation': '517 U.S. 186', 'page': 186},
}
class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hidden = 0
        self.parts = []
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.hidden += 1
        if tag == 'a':
            href = dict(attrs).get('href')
            if href: self.links.append(href)
        if tag in ('p','div','br','h1','h2','h3','h4','li','tr','hr'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.hidden = max(0,self.hidden-1)
        if tag in ('p','div','h1','h2','h3','h4','li','tr'): self.parts.append('\n')
    def handle_data(self, data):
        if not self.hidden: self.parts.append(data)
    def text(self):
        value = ''.join(self.parts)
        return '\n'.join(re.sub(r'[ \t\r\f\v]+',' ',line).strip() for line in value.splitlines()).strip()+'\n'

def digest(path): return sha256(path.read_bytes()).hexdigest()
def stamp(): return datetime.now(timezone.utc).isoformat()

def fetch(case, kind, suffix=None):
    info=CASES[case]
    out=BASE/f'chunk5_{case}_historical_primary'
    out.mkdir(parents=True,exist_ok=True)
    name=f'usreports-517-{info["page"]}' if kind=='pdf' else f'cornell-{info["docket"]}.{suffix}'
    url=(f'https://www.govinfo.gov/content/pkg/USREPORTS-517/pdf/USREPORTS-517-{info["page"]}.pdf' if kind=='pdf' else f'https://www.law.cornell.edu/supct/html/{info["docket"]}.{suffix}.html')
    tmp=out/f'{name}.download'
    headers=out/f'{name}.headers.txt'
    cmd=['curl','--silent','--show-error','--location','--max-time','90','--user-agent','Mozilla/5.0 (compatible; primary-source archival research)','--dump-header',str(headers),'--output',str(tmp),'--write-out','%{http_code}\n%{url_effective}\n%{content_type}\n',url]
    started=stamp()
    result=subprocess.run(cmd,capture_output=True,text=True)
    fields=result.stdout.splitlines()
    meta={'case':info['case'],'citation':info['citation'],'docket':info['docket'],'purpose':'historical comparator-only archival source; not a model or reconciliation artifact','requested_url':url,'effective_url':fields[1] if len(fields)>1 else None,'http_status':int(fields[0]) if fields and fields[0].isdigit() else None,'content_type':fields[2] if len(fields)>2 else None,'retrieval_started_utc':started,'retrieval_completed_utc':stamp(),'curl_exit_code':result.returncode,'curl_stderr':result.stderr,'response_headers_file':headers.name,'source_kind':kind,'full_substantive_reading_claimed':False}
    if tmp.exists(): meta.update({'response_bytes':tmp.stat().st_size,'response_sha256':digest(tmp)})
    successful=result.returncode==0 and meta['http_status']==200 and tmp.exists()
    if kind=='pdf':
        magic=tmp.read_bytes()[:5] if tmp.exists() else b''
        meta['pdf_magic_valid']=magic==b'%PDF-'
        if successful and meta['pdf_magic_valid']:
            pdf=out/f'{name}.pdf'; tmp.rename(pdf)
            target=out/f'{name}.layout.txt'
            extraction=['pdftotext','-layout','-enc','UTF-8','-eol','unix',str(pdf),str(target)]
            extracted=subprocess.run(extraction,capture_output=True,text=True)
            pinfo=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True)
            (out/f'{name}.pdfinfo.txt').write_text(pinfo.stdout+pinfo.stderr)
            text=target.read_text() if target.exists() else ''
            count=re.search(r'^Pages:\s*(\d+)',pinfo.stdout,re.M)
            meta.update({'source_file':pdf.name,'source_sha256':digest(pdf),'pdfinfo_exit_code':pinfo.returncode,'pdfinfo_file':f'{name}.pdfinfo.txt','page_count':int(count.group(1)) if count else None,'extraction':{'file':target.name,'method':'pdftotext -layout -enc UTF-8 -eol unix; no page limits or content filtering','exit_code':extracted.returncode,'stderr':extracted.stderr,'bytes':target.stat().st_size if target.exists() else None,'sha256':digest(target) if target.exists() else None,'form_feed_count':text.count('\f'),'text_nonempty':bool(text.strip()),'tool_version':subprocess.run(['pdftotext','-v'],capture_output=True,text=True).stderr.strip()}})
        else:
            if tmp.exists(): tmp.rename(out/f'{name}.response')
            meta['error']='HTTP request or PDF magic validation failed; no PDF artifact created.'
    elif successful:
        html=out/f'{name}.html'; tmp.rename(html)
        parser=VisibleText(); parser.feed(html.read_text(errors='replace'))
        target=out/f'{name}.txt'; target.write_text(parser.text())
        meta.update({'source_file':html.name,'source_sha256':digest(html),'links':parser.links,'page_count':None,'page_count_note':'HTML source is unpaginated; printed reporter page markers are retained where supplied.','extraction':{'file':target.name,'method':'Python html.parser; all visible document data retained, script/style omitted, whitespace normalized; raw HTML authoritative','sha256':digest(target),'bytes':target.stat().st_size}})
    else:
        if tmp.exists(): tmp.rename(out/f'{name}.response')
        meta['error']='HTTP request failed.'
    (out/f'{name}.metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
    return {'case':case,'name':name,'status':meta['http_status'],'error':meta.get('error'),'page_count':meta.get('page_count'),'bytes':meta.get('response_bytes'),'links':meta.get('links',[])}

if __name__=='__main__':
    if sys.argv[1]=='initial':
        jobs=[(case,kind,suffix) for case in CASES for kind,suffix in [('pdf',None),('html','ZS')]]
    else:
        jobs=[(sys.argv[1],'html',suffix) for suffix in sys.argv[2:]]
    with ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(lambda args:fetch(*args),jobs): print(json.dumps(result))
