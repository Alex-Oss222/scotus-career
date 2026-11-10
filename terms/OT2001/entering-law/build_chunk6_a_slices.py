from pathlib import Path
import importlib.util,re
root=Path('.')
spec=importlib.util.spec_from_file_location('slice_tool','tools/build_entering_law.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
out=Path('terms/OT2001/entering-law/OT_2001CHUNK6_A_AUTHORITIES.md')
selections={
 'business-and-commercial-law':["United States v. O'Hagan",'Central Bank of Denver, N.A. v. First Interstate Bank of Denver, N.A., 511 U.S. 164'],
 'criminal-procedure':['Austin v. United States, 509 U.S. 602 (1993)','United States v. Bajakajian, 524 U.S. 321','Hudson v. United States'],
 'federal-courts':['Rivet v. Regions Bank of Louisiana','Caterpillar Inc. v. Lewis',"California Public Employees' Retirement System and Florida State Board of Administration v. Paul Felzen et al."],
 'civil-rights':['Sandin v. Conner','Bragdon v. Abbott','Murphy v. United Parcel Service, Inc.','Sutton v. United Air Lines, Inc.'],
 'criminal-procedure-investigations':['Mitchell v. United States'],
 'administrative-law':['United States v. Haggar Apparel Co.','United States v. Mead Corp., 533 U.S. 218'],
 'federal-courts-immunities-and-remedies':['Vermont Agency of Natural Resources v. United States ex rel. Stevens, 529 U.S. 765 (2000)','Board of Trustees of the University of Alabama v. Garrett, 531 U.S. 356']
}
parts=['# OT2001 chunk 6 A — exact opening authority selections','Derived reading copy; source authorities control. The supplied future-matter historical decisions are excluded.']
for slug,titles in selections.items():
 source=Path('state/holdings')/(slug+'.md');text=source.read_text(encoding='utf-8')
 for title in titles:parts += ['Source: '+source.as_posix(),mod.take_heading(text,title)]
out.write_text('\n\n'.join(parts)+'\n',encoding='utf-8')
parts=['# OT2001 chunk 6 A — effective current-term public law','Compaq uses the baseline immediately before May 28, 2002: exclude the Festo and Prudential sections below. June 3 and June 10 matters include earlier effective May 28 law. No current-chunk proposal supplies entering law.']
public=[(1,'toyota-motor-manufacturing-kentucky-inc-v-williams-merits-2002-01-08'),(2,'riley-v-st-lukes-episcopal-hospital-merits-2002-01-09'),(2,'eeoc-v-waffle-house-inc-merits-2002-01-15'),(2,'barnhart-v-sigmon-coal-co-merits-2002-02-19'),(2,'winn-dixie-stores-inc-v-commissioner-merits-2002-02-20'),(4,'barnhart-v-walton-merits-2002-03-27'),(5,'Festo-v-Shoketsu'),(5,'In-re-Prudential')]
for chunk,key in public:
 source=Path(f'terms/OT2001/entering-law/OT_2001CHUNK{chunk}_PUBLIC_LAW.md'); text=source.read_text(encoding='utf-8')
 matches=list(re.finditer(r'<a id="([^"]+)"></a>',text)); found=[(i,m) for i,m in enumerate(matches) if key.casefold() in m.group(1).casefold()]
 if not found and key=='Festo-v-Shoketsu':found=[(i,m) for i,m in enumerate(matches) if 'Festo' in m.group(1)]
 if len(found)!=1:raise ValueError((source,key,len(found)))
 i,m=found[0];end=matches[i+1].start() if i+1<len(matches) else len(text)
 parts+=['Source: '+source.as_posix(),text[m.start():end].strip()]
source=Path('terms/OT2001/workspace/neutral-projection.md');text=source.read_text(encoding='utf-8')
a=text.index('### US Airways, Inc. v. Barnett');b=text.index('### City of Los Angeles',a)
parts+=['Source: '+source.as_posix(),text[a:b].strip()]
Path('terms/OT2001/entering-law/OT_2001CHUNK6_A_CURRENT.md').write_text('\n\n'.join(parts)+'\n',encoding='utf-8')
print('Copied opening holdings and effective public-law selections.')
