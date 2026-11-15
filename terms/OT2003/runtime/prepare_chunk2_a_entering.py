"""Mechanical bounded copies for the first eight chunk-two neutral matters."""
from pathlib import Path
import importlib.util
import subprocess
import sys
import re

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location('entering_builder', ROOT / 'tools/build_entering_law.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
OUT = ROOT / 'terms/OT2003/entering-law/OT_2003CHUNK2_A.md'
STANDARDS = [
    'State-court merits decisions and factual development under amended §2254',
    'Temporal reach of ordinary AEDPA habeas amendments',
    'Sequencing nonretroactivity and procedural default on habeas review',
    'Preserved protected-silence and personal-intent errors on federal habeas review',
    'A vitiated jury reasonable-doubt standard is structural error',
    'Jury determination of elements and qualified omitted-element review',
    'Protected choice and the six-step standard for previability regulation',
    'Accurate abortion-consent information, optional materials and receipt certification',
    'Confidential abortion reporting and distinct medical predicates',
    'Official disclosure and compelled surrender of intimate information',
    'S corporation debt-discharge income and attribute-reduction sequence',
    'Delegated Customs interpretation and independent tariff review',
    'Duration and trial-work conditions in initial disability entitlement',
    'Complete deprivation of economically beneficial land use',
    'Definitive land-use restrictions and unnecessary further applications',
    'Postregulation acquisition and the contextual takings inquiry',
    'Commerce connection, mechanism, and class-wide effects',
    'Common substantial-justification standard for governmental racial classifications',
    'Selective racial restructuring of access to lawful remedies',
]
HOLDINGS = [
    ('federal-courts-habeas', 'Williams v. Taylor (Terry Williams), 529 U.S. 362 (2000)'),
    ('federal-courts-habeas', 'Bell v. Cone, 535 U.S. 685'),
    ('federal-courts-habeas', 'Woodford v. Visciotti, 537 U.S. 19'),
    ('federal-courts-habeas', 'Lockyer v. Andrade, 538 U.S. 63'),
    ('criminal-procedure', 'Brecht v. Abrahamson, 507 U.S. 619 (1993)'),
    ('criminal-procedure', 'Sullivan v. Louisiana, 508 U.S. 275 (1993)'),
    ('criminal-procedure', 'Neder v. United States'),
    ('criminal-procedure-sentencing-and-capital', 'Ring v. Arizona, 536 U.S. 584'),
    ('civil-rights', 'Reproductive liberty and constitutional precedent'),
    ('civil-rights', 'Abortion reporting and public disclosure'),
    ('civil-rights', 'Doe v. Southeastern Pennsylvania Transportation Authority'),
    ('civil-rights', 'Herring v. Keenan — intimate medical information'),
    ('first-amendment', 'Abortion information and compelled speech'),
    ('first-amendment', 'Commack Self-Service Kosher Meats, Inc. v. Weiss'),
    ('federal-taxation', 'Gitlitz v. Commissioner, 531 U.S. 206'),
    ('administrative-law', 'United States v. Mead Corp., 533 U.S. 218'),
    ('administrative-law', 'Barnhart v. Walton, 535 U.S. 212'),
    ('administrative-law', 'Heimmermann v. First Union Mortgage Corp. — official HUD interpretations of mortgage-broker compensation'),
    ('property-and-economic-rights', 'Palazzolo v. Rhode Island'),
    ('property-and-economic-rights', 'Tahoe-Sierra Preservation Council, Inc. v. Tahoe Regional Planning Agency, 535 U.S. 302'),
    ('constitutional-structure', 'United States v. Lopez'),
    ('constitutional-structure', 'National Association of Home Builders v. Babbitt'),
    ('civil-rights', 'Adarand Constructors, Inc. v. Peña'),
    ('civil-rights', 'Romer v. Evans, 517 U.S. 620'),
    ('civil-rights', 'Coalition for Economic Equity v. Wilson'),
]
PUBLIC = [
    ('OT1999',5,'Williams v. Taylor (Terry Williams), No. 98-8384'),
    ('OT2001',5,'Bell v. Cone, No. 01-400'),
    ('OT2002',1,'Woodford v. Visciotti, No. 02-137'),
    ('OT2002',5,'Lockyer v. Andrade, No. 01-1127'),
    ('OT1992',5,'Brecht v. Abrahamson, No. 91-7358'),
    ('OT1992',7,'Sullivan v. Louisiana, No. 92-5129'),
    ('OT1998',9,'Neder v. United States, No. 97-1985'),
    ('OT2001',8,'Ring v. Arizona, No. 01-488'),
    ('OT1991',14,'Planned Parenthood of Southeastern Pennsylvania v. Casey, Nos. 91-744 and 91-902'),
    ('OT1996',7,'Doe v. Southeastern Pennsylvania Transportation Authority, Third Circuit No. 95-1559'),
    ('OT2002',1,'Commack Self-Service Kosher Meats, Inc. v. Weiss'),
    ('OT2000',2,'Gitlitz v. Commissioner, No. 99-1295'),
    ('OT2000',7,'United States v. Mead Corp., No. 99-1434'),
    ('OT2001',4,'Barnhart v. Walton, No. 00-1937'),
    ('OT2002',13,'Heimmermann v. First Union Mortgage Corp.'),
    ('OT2000',8,'Palazzolo v. Rhode Island, No. 99-2047'),
    ('OT2001',4,'Tahoe-Sierra Preservation Council, Inc. v. Tahoe Regional Planning Agency, No. 00-1167'),
    ('OT1994',5,'United States v. Lopez, No. 93-1260'),
    ('OT1997',10,'National Association of Home Builders v. Babbitt, D.C. Circuit No. 96-5354'),
    ('OT1994',7,'Adarand Constructors, Inc. v. Peña, No. 93-1841'),
    ('OT1995',6,'Romer v. Evans, No. 94-1039'),
    ('OT1998',1,'Coalition for Economic Equity v. Wilson, Ninth Circuit Nos. 97-15030 and 97-15031'),
]

def case_section(text, title):
    # One old public output repeats a case heading in source notes. Select the
    # bounded substantive entry, never its short source-note duplicate.
    lines=text.splitlines(); found=[]
    for i,line in enumerate(lines):
        if re.sub(r'^#+\s*','',line).strip()!=title: continue
        level=len(line)-len(line.lstrip('#')); end=len(lines)
        for j in range(i+1,len(lines)):
            if re.match(r'^#{1,'+str(level)+r'}\s',lines[j]): end=j; break
        found.append('\n'.join(lines[i:end]))
    if not found: raise ValueError(title)
    return max(found,key=len)

def main():
    args=[sys.executable,'-B',str(ROOT/'tools/build_entering_law.py'),str(OUT)]
    for h in STANDARDS: args+=['--standard-heading',h]
    args+=['--standing-heading','1. Current Court']
    subprocess.run(args,cwd=ROOT,check=True,capture_output=True,text=True)
    parts=[OUT.read_text(encoding='utf-8')]
    for volume,title in HOLDINGS:
        source='state/holdings/'+volume+'.md'
        copied=builder.take_heading((ROOT/source).read_text(encoding='utf-8'),title)
        parts+=['\n## Verbatim Holdings selection\n\nSource: `'+source+'`; heading: '+title+'\n',copied]
    for term,chunk,title in PUBLIC:
        source=f'terms/{term}/output/OT_{term[2:]}CHUNK{chunk}.md'
        case=case_section((ROOT/source).read_text(encoding='utf-8'),title)
        parts+=['\n## Prior public positions\n\nSource: `'+source+'`; case: '+title+'\n']
        for section in ['Opinion Topology','Separate Writings','Selected Separate Positions','Selected Separate Writings','Separate Positions Relevant to the Decision']:
            try: copied=builder.take_heading(case,section)
            except ValueError: continue
            parts.append(copied)
    projection=(ROOT/'terms/OT2003/workspace/neutral-projection.md').read_text(encoding='utf-8')
    holston=builder.take_heading(projection,'United States v. Holston; Second Circuit No. 02-1292; judgment below reported at 343 F.3d 83.')
    parts+=['\n## Effective current-term authority for Ho only\n\nSource: `terms/OT2003/workspace/neutral-projection.md`. Effective October 30, 2003; excludes this authority from Gentry and Greenville. The other selected cases present different fields.\n',holston]
    OUT.write_text('\n\n'.join(parts).rstrip()+'\n',encoding='utf-8')
    print(str(OUT.relative_to(ROOT))+': '+str(len(OUT.read_text(encoding='utf-8').split()))+' words')

if __name__=='__main__': main()
