import urllib.request
from pathlib import Path
out=Path('terms/OT1998/sources/chunk8-comparator')
urls=['https://media.ca1.uscourts.gov/pdf.opinions/98-1309.01A','https://media.ca1.uscourts.gov/pdf.opinions/98-1309.01A.pdf','https://www.ca1.uscourts.gov/sites/ca1/files/opnfiles/98-1309.01A','https://law.resource.org/pub/us/case/reporter/F3/129/129.F3d.505.96-35835.html']
for i,u in enumerate(urls):
 try:
  b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=10).read()
  print(i,len(b),b[:60]);(out/('primary_attempt_'+str(i)+('.pdf' if b.startswith(b'%PDF') else '.txt'))).write_bytes(b)
 except Exception as e:print(i,str(e))
