from pathlib import Path
import importlib.util
import subprocess
import sys
import re

ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('entering_builder',ROOT/'tools/build_entering_law.py')
builder=importlib.util.module_from_spec(spec); spec.loader.exec_module(builder)
standards=[
 'Announcement before dwelling entry',
 'Statutory announcement and supported danger under §3109',
 'Independent appellate review of suspicion and nonwarrant probable cause',
 'Informant reports of gun possession and individualized suspicion',
 'Brief actual submission to a police command',
 'Rejected employment explanations and circumstantial discrimination proof',
 'Whole-record review of a jury verdict under Rule 50',
 'Age motivation, pension tenure and willfulness',
 'Write-in voting within the complete ballot-access system',
 'Compulsory outsider selection of official party nominees',
 'Exclusive congressional qualifications and ballot restrictions',
 'Exclusive interstate jurisdiction and private boundary-related claims',
 'Enforcement and modification of interstate water decrees',
 'Commerce connection, mechanism, and class-wide effects',
 'Migratory-bird use and isolated-water jurisdiction',
 "Controlling weight for a responsible agency's fair regulatory interpretation",
 'Delegated Customs interpretation and independent tariff review',
 'Persuasive weight of a nonbinding agency advisory interpretation',
 'No delay-based substitute for statutory habeas dismissal',
 'Federal-prisoner limitation and successive-motion certification',
 'Second or successive state-custody habeas applications',
 'Supreme Court original habeas after an authorization-review bar',
]
holdings={
 'criminal-procedure-investigations':['Wilson v. Arkansas','Richards v. Wisconsin','United States v. Ramirez','Ornelas v. United States, 517 U.S. 690','Illinois v. Wardlow, 528 U.S. 119 (2000)','United States v. Valentine'],
 'labor-and-employment':['Hazen Paper Co. v. Biggins, 507 U.S. 604 (1993)',"St. Mary's Honor Center v. Hicks, 509 U.S. 502 (1993)",'Reeves v. Sanderson Plumbing Products, Inc., 530 U.S. 133 (2000)'],
 'election-law':['Burdick v. Takushi, 504 U.S. 428 (1992)','Timmons v. Twin Cities Area New Party','California Democratic Party v. Jones, 530 U.S. 567 (2000)'],
 'constitutional-structure':['U.S. Term Limits, Inc. v. Thornton / Bryant v. Hill','United States v. Lopez','National Association of Home Builders v. Babbitt'],
 'property-and-economic-rights':['New Jersey v. New York'],
 'federal-courts':['Arizona v. California, 530 U.S. 392 (2000)'],
 'environmental-law':['Solid Waste Agency of Northern Cook County v. U.S. Army Corps of Engineers, 531 U.S. 159'],
 'administrative-law':['Auer v. Robbins','United States v. Mead Corp., 533 U.S. 218'],
 'federal-courts-habeas':['Lonchar v. Thomas, 517 U.S. 314','Felker v. Turpin, 518 U.S. 651 (1996)','Stewart v. Martinez-Villareal'],
}
public=[
 ('OT1991','10','Burdick v. Takushi, No. 91-535'),
 ('OT1992','10',"St. Mary's Honor Center v. Hicks, No. 92-602"),
 ('OT1992','5','Hazen Paper Co. v. Biggins, No. 91-1600'),
 ('OT1994','5','United States v. Lopez, No. 93-1260'),
 ('OT1994','6','U.S. Term Limits, Inc. v. Thornton / Bryant v. Hill, Nos. 93-1456, 93-1828'),
 ('OT1994','6','Wilson v. Arkansas, No. 94-5707'),
 ('OT1995','10','Felker v. Turpin, No. 95-8836; associated application A-890'),
 ('OT1995','5','Lonchar v. Thomas, No. 95-5015'),
 ('OT1995','7','Ornelas v. United States, No. 95-5257'),
 ('OT1996','4','Auer v. Robbins, No. 95-897'),
 ('OT1996','7','Richards v. Wisconsin, No. 96-5955'),
 ('OT1996','7','Timmons v. Twin Cities Area New Party, No. 95-1608'),
 ('OT1997','10','National Association of Home Builders v. Babbitt, D.C. Circuit No. 96-5354'),
 ('OT1997','5','United States v. Ramirez, No. 96-1469'),
 ('OT1997','8','Stewart v. Martinez-Villareal, No. 97-300'),
 ('OT1997','9','New Jersey v. New York, No. 120, Original'),
 ('OT1999','1','Illinois v. Wardlow, No. 98-1036'),
 ('OT1999','8','Reeves v. Sanderson Plumbing Products, Inc., No. 99-536'),
 ('OT1999','8','Arizona v. California, No. 8, Original'),
 ('OT1999','9','California Democratic Party v. Jones, No. 99-401'),
 ('OT2000','2','Solid Waste Agency of Northern Cook County v. U.S. Army Corps of Engineers, No. 99-1178'),
 ('OT2000','5','United States v. Valentine, Third Circuit No. 00-1425; judgment below at 232 F.3d 350'),
 ('OT2000','7','United States v. Mead Corp., No. 99-1434'),
]
out=ROOT/'terms/OT2003/entering-law/OT_2003CHUNK2_B.md'
args=[sys.executable,'-B',str(ROOT/'tools/build_entering_law.py'),str(out)]
for title in standards: args.extend(['--standard-heading',title])
args.extend(['--standing-heading','1. Current Court'])
subprocess.run(args,cwd=ROOT,check=True,capture_output=True,text=True)
parts=[out.read_text(encoding='utf-8')]
for volume,titles in holdings.items():
 source='state/holdings/'+volume+'.md'
 for title in titles:
  copied=builder.take_heading((ROOT/source).read_text(encoding='utf-8'),title)
  parts.extend(['\n## Verbatim Holdings selection\n\nSource: `'+source+'`; heading: '+title+'\n',copied])
for term,chunk,title in public:
 source=f'terms/{term}/output/OT_{term[2:]}CHUNK{chunk}.md'
 case=builder.take_heading((ROOT/source).read_text(encoding='utf-8'),title)
 parts.append('\n## Prior public positions\n\nSource: `'+source+'`; case: '+title+'\n')
 for heading in ['Opinion Topology','Separate Writings','Selected Separate Positions','Selected Separate Writings','Separate Positions Relevant to the Decision']:
  try: copied=builder.take_heading(case,heading)
  except ValueError: continue
  parts.append(copied)
source='terms/OT2003/workspace/neutral-projection.md'
parts.extend(['\n## Effective current-term law: Holston\n\nSource: `'+source+'`; effective October 30, 2003. Applies before every assigned December event. Later 2004 events are excluded.\n',builder.take_heading((ROOT/source).read_text(encoding='utf-8'),'United States v. Holston; Second Circuit No. 02-1292; judgment below reported at 343 F.3d 83.')])
out.write_text('\n\n'.join(parts).rstrip()+'\n',encoding='utf-8')
print(str(out.relative_to(ROOT)),len(out.read_text(encoding='utf-8').split()),'words')
