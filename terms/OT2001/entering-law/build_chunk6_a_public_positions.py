from pathlib import Path
import importlib.util,re
spec=importlib.util.spec_from_file_location('slice_tool','tools/build_entering_law.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
parts=['# OT2001 chunk 6 A — exact supplementary law and prior public positions']
holdings=[('business-and-commercial-law','Wharf (Holdings) Ltd. v. United International Holdings, Inc., 532 U.S. 588'),('federal-courts','Cardinal Chemical Co. v. Morton International, Inc., 508 U.S. 83 (1993)'),('administrative-law','Thomas Jefferson University v. Shalala, 512 U.S. 504'),('criminal-procedure-sentencing-and-capital','Ohio Adult Parole Authority v. Woodard')]
for slug,key in holdings:
 p=Path('state/holdings')/(slug+'.md');parts+=['Source: '+p.as_posix(),mod.take_heading(p.read_text(encoding='utf-8'),key)]
standards=Path('state/STANDARDS_AND_TESTS.md').read_text(encoding='utf-8')
for key in ['Live patent-invalidity counterclaims after noninfringement affirmance',"Controlling weight for a responsible agency's fair regulatory interpretation"]:parts+=['Source: state/STANDARDS_AND_TESTS.md',mod.take_heading(standards,key)]
public=[(1992,6,'### Cardinal Chemical'),(1993,7,'### Thomas Jefferson'),(1994,8,'### Sandin'),(1996,12,"### United States v. O'Hagan"),(1997,6,'### Ohio Adult Parole'),(1998,3,"### California Public Employees'"),(1998,6,'### Mitchell'),(2000,3,'### Board of Trustees'),(2000,6,'### Wharf'),(2000,7,'### United States v. Mead')]
for year,chunk,key in public:
 p=Path(f'terms/OT{year}/output/OT_{year}CHUNK{chunk}.md');t=p.read_text(encoding='utf-8');a=t.index(key);m=re.search(r'^### [^\n]+',t[a+len(key):],re.M);end=a+len(key)+m.start() if m else len(t);parts+=['Source: '+p.as_posix(),t[a:end].strip()]
Path('terms/OT2001/entering-law/OT_2001CHUNK6_A_PUBLIC_POSITIONS.md').write_text('\n\n'.join(parts)+'\n',encoding='utf-8')
print('Copied exact relevant prior public case sections.')
