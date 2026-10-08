import concurrent.futures
import urllib.parse
import urllib.request
from pathlib import Path
ROOT = Path('terms/OT1995/entering-law/CHUNK10_RESEARCH_A_SOURCES')
ROOT.mkdir(exist_ok=True)
items = {
 'COLORADO': ('micro_IA40385013_0654', ['02. Petition for Writ of Certiorari','05. Joint Appendix','06. Petitioners Brief','07. Respondents Brief','08. Reply Brief']),
 'UMBEHR': ('micro_IA40385013_0595', ['02. Petition for Writ of Certiorari','05. Joint Appendix','06. Petitioners Brief','07. Respondents Brief','08. Reply Brief']),
 'OHARE': ('micro_IA40385013_0638', ['02. Petition for Writ of Certiorari','05. Joint Appendix','06. Petitioners Brief','07. Respondents Brief','08. Reply Brief']),
 'DENVER': ('micro_IA40385013_0640', ['02. Petition for Writ of Certiorari','05. Joint Appendix','06. Petitioners Brief','07. Petitioners Brief','08. Respondents Brief','09. Respondents Brief','10. Reply Brief','11. Reply Brief','12. Supplemental Brief']),
}
def fetch(row):
 name, identifier, part = row
 remote = identifier + ' ' + part + '_djvu.txt'
 url = 'https://archive.org/download/' + identifier + '/' + urllib.parse.quote(remote)
 target = ROOT / (name + '_' + part + '.txt')
 target.write_bytes(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})).read())
 return name,part,target.stat().st_size
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
 for row in pool.map(fetch, [(n,i,p) for n,(i,ps) in items.items() for p in ps]):
  print(row)
