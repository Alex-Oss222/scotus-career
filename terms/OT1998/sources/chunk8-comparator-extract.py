from pathlib import Path
import pymupdf,hashlib,json
src=Path('terms/OT1998/sources/chunk7-control/official-526.pdf')
out=Path('terms/OT1998/sources/chunk8-comparator');out.mkdir(exist_ok=True)
doc=pymupdf.open(src)
cases={'goldsmith':(529,540),'cromartie':(541,558),'white':(559,573),'ruhrgas':(574,588),'new-jersey-decree':(589,601),'wilson':(603,628),'davis':(629,686),'monterey':(687,755),'california-dental':(756,794),'cleveland':(795,807),'hanlon':(808,810)}
manifest=[]
for name,(start,end) in cases.items():
 pages=[]
 for p in range(start,end+1):
  ix=p+110 if p<555 else p+111
  pages.append(doc[ix].get_text())
 dest=out/(name+'-official.txt');dest.write_text('\n\f\n'.join(pages),encoding='utf-8')
 manifest.append({'case':name,'printed_pages':[start,end],'source':'https://www.supremecourt.gov/opinions/boundvolumes/526bv.pdf','file':dest.as_posix(),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
# Boundary map is the printed page 601; preserve the complete official visual.
doc[713].get_pixmap(matrix=pymupdf.Matrix(2,2)).save(out/'new-jersey-decree-map.png')
(out/'extraction-manifest.json').write_text(json.dumps({'source_file':src.as_posix(),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'items':manifest},indent=2),encoding='utf-8')
for name in cases:
 text=(out/(name+'-official.txt')).read_text(encoding='utf-8')
 print(name,len(text),text[:40].replace('\n',' '),text[-120:].replace('\n',' '))

