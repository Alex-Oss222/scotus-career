#!/usr/bin/env python3
"""Retrieve complete archival primary sources; no substantive analysis."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
CASES={'oconnor':{'case':"O'Connor v. Consolidated Coin Caterers Corp.",'docket':'95-354','page':308},'lonchar':{'case':'Lonchar v. Thomas','docket':'95-5015','page':314}}
def now(): return datetime.now(timezone.utc).isoformat()
def hashfile(p): return sha256(p.read_bytes()).hexdigest()
class TextParser(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True); self.hidden=0; self.parts=[]; self.links=[]
 def handle_starttag(self,tag,attrs):
  if tag in ('script','style'): self.hidden+=1
  if tag=='a':
   href=dict(attrs).get('href')
   if href:self.links.append(href)
  if tag in ('p','div','br','h1','h2','h3','h4','li','tr','hr'):self.parts.append('\n')
 def handle_endtag(self,tag):
  if tag in ('script','style'):self.hidden=max(0,self.hidden-1)
  if tag in ('p','div','h1','h2','h3','h4','li','tr'):self.parts.append('\n')
 def handle_data(self,data):
  if not self.hidden:self.parts.append(data)
 def text(self):return '\n'.join(re.sub(r'[ \t\r\f\v]+',' ',s).strip() for s in ''.join(self.parts).splitlines()).strip()+'\n'
def fetch(case,suffix):
 cfg=CASES[case];d=ROOT/f'chunk5_{case}_historical_primary';ispdf=suffix=='pdf'
 base=f'usreports-517-{cfg["page"]}' if ispdf else f'cornell-{cfg["docket"]}.{suffix}'
 url=f'https://www.govinfo.gov/content/pkg/USREPORTS-517/pdf/USREPORTS-517-{cfg["page"]}.pdf' if ispdf else f'https://www.law.cornell.edu/supct/html/{cfg["docket"]}.{suffix}.html'
 tmp=d/f'{base}.download';headers=d/f'{base}.headers.txt';started=now()
 result=subprocess.run(['curl','--silent','--show-error','--location','--max-time','90','--user-agent','Mozilla/5.0 (compatible; primary-source archival research)','--dump-header',str(headers),'--output',str(tmp),'--write-out','%{http_code}\n%{url_effective}\n%{content_type}\n',url],capture_output=True,text=True)
 fields=result.stdout.splitlines()
 m={'case':cfg['case'],'citation':f'517 U.S. {cfg["page"]}','docket':cfg['docket'],'purpose':'Historical comparator-only archive; no modeling or reconciliation','requested_url':url,'effective_url':fields[1] if len(fields)>1 else None,'http_status':int(fields[0]) if fields and fields[0].isdigit() else None,'content_type':fields[2] if len(fields)>2 else None,'retrieval_started_utc':started,'retrieval_completed_utc':now(),'curl_exit_code':result.returncode,'curl_stderr':result.stderr,'response_headers_file':headers.name,'source_kind':'pdf' if ispdf else 'html','full_substantive_reading_claimed':False}
 if tmp.exists():m.update({'response_bytes':tmp.stat().st_size,'response_sha256':hashfile(tmp)})
 success=result.returncode==0 and m['http_status']==200 and tmp.exists()
 if ispdf:
  m['pdf_magic_valid']=tmp.exists() and tmp.read_bytes().startswith(b'%PDF-')
  if success and m['pdf_magic_valid']:
   pdf=d/f'{base}.pdf';tmp.rename(pdf);txt=d/f'{base}.layout.txt'
   result=subprocess.run(['pdftotext','-layout','-enc','UTF-8','-eol','unix',str(pdf),str(txt)],capture_output=True,text=True)
   info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True)
   (d/f'{base}.pdfinfo.txt').write_text(info.stdout+info.stderr)
   pagecount=re.search(r'^Pages:\s*(\d+)',info.stdout,re.M)
   content=txt.read_text() if txt.exists() else ''
   m.update({'source_file':pdf.name,'source_sha256':hashfile(pdf),'pdfinfo_exit_code':info.returncode,'pdfinfo_file':f'{base}.pdfinfo.txt','page_count':int(pagecount.group(1)) if pagecount else None,'extraction':{'file':txt.name,'method':'pdftotext -layout -enc UTF-8 -eol unix; all pages; no filtering','exit_code':result.returncode,'stderr':result.stderr,'bytes':txt.stat().st_size if txt.exists() else None,'sha256':hashfile(txt) if txt.exists() else None,'form_feed_count':content.count('\f'),'nonempty_page_count':sum(bool(p.strip()) for p in content.split('\f')),'tool_version':subprocess.run(['pdftotext','-v'],capture_output=True,text=True).stderr.strip()}})
  else:
   if tmp.exists():tmp.rename(d/f'{base}.response')
   m['error']='Request or PDF magic validation failed; no .pdf artifact created.'
 elif success:
  html=d/f'{base}.html';tmp.rename(html);parser=TextParser();parser.feed(html.read_text(errors='replace'));txt=d/f'{base}.txt';txt.write_text(parser.text())
  m.update({'source_file':html.name,'source_sha256':hashfile(html),'links':parser.links,'page_count':None,'page_count_note':'Unpaginated HTML source; original reporter markers retained where supplied.','extraction':{'file':txt.name,'method':'Python html.parser; all visible text retained, script/style omitted, whitespace normalized; raw HTML is authoritative','sha256':hashfile(txt),'bytes':txt.stat().st_size}})
 else:
  if tmp.exists():tmp.rename(d/f'{base}.response')
  m['error']='HTTP retrieval failed.'
 (d/f'{base}.metadata.json').write_text(json.dumps(m,indent=2)+'\n')
 return {k:m.get(k) for k in ('case','requested_url','effective_url','http_status','response_bytes','page_count','error')}|({'opinion_links':[u for u in m['links'] if re.search(r'\.Z[A-Z]\d?\.html',u)]} if 'links' in m else {})
if __name__=='__main__':
 jobs=[(c,s) for c in CASES for s in ('pdf','ZS')] if sys.argv[1]=='initial' else [(sys.argv[1],s) for s in sys.argv[2:]]
 with ThreadPoolExecutor(max_workers=4) as pool:
  for result in pool.map(lambda v:fetch(*v),jobs):print(json.dumps(result))
