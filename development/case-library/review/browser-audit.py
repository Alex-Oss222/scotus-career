"""Read-only real-browser audit; see review/README.md for the loopback server command."""
import importlib.util
import json
import sys
import time
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit
from playwright.sync_api import sync_playwright

root=Path(__file__).resolve().parents[3]
html_path=Path(sys.argv[1]).resolve()
catalogue=json.loads((html_path.parent/'catalogue.json').read_text())
records=catalogue['records']
report={'snapshot':str(html_path.parent.relative_to(root)),'records':len(records),'terms':dict(Counter(r['term'] for r in records))}
class Links(HTMLParser):
    def __init__(self): super().__init__();self.links=[];self.ids=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=='a':self.links.append(attrs['href'])
        if 'id' in attrs:self.ids.append(attrs['id'])
parser=Links();parser.feed(html_path.read_text())
assert len(set(parser.ids))==len(parser.ids),'duplicate HTML IDs'
local=0;external=0;fragments=0
for href in parser.links:
    parsed=urlsplit(href)
    if parsed.scheme:
        assert parsed.scheme in ('http','https') and parsed.hostname and not parsed.username and not parsed.password,href
        external+=1
    elif href.startswith('#'):
        assert unquote(href[1:]) in parser.ids,href
        fragments+=1
    else:
        resolved=(html_path.parent/unquote(parsed.path)).resolve()
        assert resolved.is_relative_to(root),href
        assert resolved.is_file(),href
        local+=1
report.update(local_links=local,external_pointers=external,fragment_links=fragments)
terms=['']+sorted(set(r['term'] for r in records))
chunks=['']+sorted({str(c) for r in records for c in r['chunks']},key=int)
kinds=['','court_event','admitted_source']
cases=[]
for term in terms:
    for chunk in chunks:
        for kind in kinds:
            expected=sorted(r['record_id'] for r in records if (not term or term==r['term']) and (not chunk or int(chunk) in r['chunks']) and (not kind or kind==r['kind']))
            cases.append({'term':term,'chunk':chunk,'kind':kind,'expected':expected})
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium')
    page=browser.new_page(viewport={'width':1280,'height':1000})
    errors=[];requests=[]
    page.on('pageerror',lambda error:errors.append(str(error)))
    page.on('request',lambda request:requests.append(request.url))
    start=time.perf_counter();page.goto('http://127.0.0.1:8765/'+html_path.relative_to(root).as_posix());page.wait_for_function("!document.getElementById('search').disabled")
    report['load_seconds']=round(time.perf_counter()-start,3)
    assert page.locator('.record:visible').count()==len(records)
    start=time.perf_counter()
    outcome=page.evaluate('''cases => {
      const term=document.getElementById('term-filter'), chunk=document.getElementById('chunk-filter'), kind=document.getElementById('kind-filter');
      for (let i=0;i<cases.length;i++) {
        const c=cases[i];term.value=c.term;chunk.value=c.chunk;kind.value=c.kind;
        kind.dispatchEvent(new Event('change'));
        const actual=Array.from(document.querySelectorAll('.record:not([hidden])')).map(x=>x.id).sort();
        if (JSON.stringify(actual)!==JSON.stringify(c.expected)) return {index:i,actual,expected:c.expected};
      }
      return null;
    }''',cases)
    assert outcome is None,outcome
    report['filter_combinations']=len(cases);report['filter_seconds']=round(time.perf_counter()-start,3)
    page.locator('#clear-filters').click()
    search_cases=[('nonexistent-case-library-probe-zzzz',0)]
    for query in ['410 U.S. 113','Casey','94-1941','OT1995']:
        import unicodedata
        words=unicodedata.normalize('NFKC',query).lower().split()
        # Browser data-search is the declared search surface; assert user-visible
        # results match every query token rather than merely testing counts change.
        expected=page.locator('.record').evaluate_all('nodes => nodes.map(node => ({id:node.id,text:node.dataset.search}))')
        count=sum(all(w in unicodedata.normalize('NFKC',r['text']).lower() for w in words) for r in expected)
        search_cases.append((query,count))
    for query,count in search_cases:
        page.locator('#search').fill(query)
        assert page.locator('.record:visible').count()==count,(query,count)
    report['search_cases']=len(search_cases)
    page.locator('#clear-filters').click()
    page.locator('#term-filter').select_option('OT1995')
    report['ot1995_visible']=page.locator('.record:visible').count()
    assert report['ot1995_visible']==sum(r['term']=='OT1995' for r in records)
    page.screenshot(path='/tmp/case-library-real-desktop.png')
    # Open all record detail blocks before checking mobile overflow so long URLs,
    # provenance labels, hashes and metadata participate in layout.
    page.locator('#clear-filters').click()
    page.locator('details').evaluate_all('nodes => nodes.forEach(node => node.open=true)')
    report['mobile_widths']=[]
    for width in (320,375,768,1280):
        page.set_viewport_size({'width':width,'height':1000})
        assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'),width
        report['mobile_widths'].append(width)
    page.locator('details').evaluate_all('nodes => nodes.forEach(node => node.open=false)')
    page.set_viewport_size({'width':375,'height':1000})
    page.screenshot(path='/tmp/case-library-real-mobile.png')
    nojs=browser.new_context(java_script_enabled=False)
    plain=nojs.new_page();plain.goto('http://127.0.0.1:8765/'+html_path.relative_to(root).as_posix())
    assert plain.locator('.record:visible').count()==len(records)
    assert plain.locator('noscript').is_visible()
    report['no_javascript_visible']=plain.locator('.record:visible').count()
    assert not errors,errors
    assert all(not url.startswith(('http:','https:')) or url.startswith('http://127.0.0.1:8765/') for url in requests),requests
    report['browser_errors']=errors;report['automatic_external_requests']=0
    nojs.close();browser.close()
Path('/tmp/case-library-browser-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
