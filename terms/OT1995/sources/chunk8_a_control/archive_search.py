import json, urllib.request, urllib.parse
from pathlib import Path
q='collection:us-supreme-court AND (identifier:*95-591* OR title:("International Business Machines"))'
u='https://archive.org/advancedsearch.php?'+urllib.parse.urlencode({'q':q,'output':'json','rows':50,'fl[]':['identifier','title']},doseq=True)
req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})
data=urllib.request.urlopen(req,timeout=45).read()
Path(__file__).with_name('ibm_archive_search.json').write_bytes(data)
print(data.decode())
