from urllib.parse import urlencode
from urllib.request import Request,urlopen
from pathlib import Path
import json
from fetch_sources import fetch
ROOT=Path(__file__).resolve().parent
for term in ['97-1868','UNUM Ward','97-2044','Haggar','Russell Burris']:
    url='https://archive.org/advancedsearch.php?'+urlencode({'q':'collection:us-supreme-court AND ('+term+')','output':'json','rows':'50','fl[]':'identifier,title'})
    try:
        data=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read()
        (ROOT/('archive-search-'+term.replace(' ','_')+'.json')).write_bytes(data)
        print(term,json.loads(data).get('response',{}))
    except Exception as e: print(term,str(e))
print(fetch(('unum-us-amicus','https://www.justice.gov/osg/brief/unum-life-insurance-v-ward-amicus-merits')))
