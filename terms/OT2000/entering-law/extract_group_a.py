from pathlib import Path
import importlib.util, re, urllib.request
spec=importlib.util.spec_from_file_location('slice','tools/build_entering_law.py')
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
selections={
 'business-and-commercial-law':['Central Bank of Denver, N.A. v. First Interstate Bank of Denver, N.A., 511 U.S. 164',"United States v. O'Hagan"],
 'election-law':['United States Department of Commerce v. Montana, 503 U.S. 442 (1992)','Voinovich v. Quilter, 507 U.S. 146 (1993)'],
 'federal-indian-law':['Strate v. A-1 Contractors'],
 'criminal-procedure':['Whren v. United States, 517 U.S. 806','Ricci v. Village of Arlington Heights','Knowles v. Iowa, 525 U.S. 113'],
 'administrative-law':['Bennett v. Spear','Christensen v. Harris County, 529 U.S. 576 (2000)','Thomas Jefferson University v. Shalala, 512 U.S. 504']
}
out=[]
for slug,qs in selections.items():
 for q in qs:
  out.append('Source: state/holdings/'+slug+'.md\n\n'+m.take_heading(Path('state/holdings/'+slug+'.md').read_text(encoding='utf-8'),q))
Path('terms/OT2000/entering-law/OT_2000CHUNK6_A_FOCUS.md').write_text('# Scripted focused extracts from selected Holdings volumes\n\n'+'\n\n'.join(out),encoding='utf-8')
for name,url in [
 ('Chen_lower','https://law.resource.org/pub/us/case/reporter/F3/206/206.F3d.502.98-20440.html'),
 ('Appalachian_lower','https://law.resource.org/pub/us/case/reporter/F3/208/208.F3d.1015.98-1540.98-1542.98-1538.98-1537.98-1536.html')]:
 data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})).read().decode('utf-8')
 p=Path('terms/OT2000/sources/CHUNK6_A'); p.mkdir(parents=True,exist_ok=True)
 (p/(name+'.html')).write_text(data,encoding='utf-8')
 from html import unescape
 text=unescape(re.sub('<[^>]+>', '\n', data))
 text=re.sub(r'\n\s*\n+', '\n\n', text)
 (p/(name+'.txt')).write_text(text,encoding='utf-8')
print('Focused slice and two date-eligible lower opinions saved.')
