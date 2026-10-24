from pathlib import Path
import json,re,subprocess,sys

root=Path(__file__).resolve().parents[3]
dst=Path(__file__).parent
areas=['constitutional-structure','civil-rights','criminal-procedure','federal-courts','administrative-law','business-and-commercial-law','federal-indian-law','federal-taxation','first-amendment','property-and-economic-rights']
queries=['Commerce connection, mechanism','State-created liberty in prison discipline','Revocation of existing parole-like','Effective prisoner court access','Circumstantial proof of unconstitutional motive','Political retaliation in existing','Backward-looking relief for unconstitutional taxes','Factual frivolousness','Statutory temporal reach','Medicare corrective adjustments','Medicare educational costs','Medicare accounting records','Controlling weight for a responsible agency','Recognition of state representative','Constitutional authority to bind','Diversity cured before trial','Ancillary enforcement','Concrete personal interests','Endangered Species Act citizen-suit','APA review of completed species','Limited modification authority','National-bank annuity','Prosecutorial investigation','Qualified-immunity legal appeals','Relevant precedent in appellate','Public-employee speech','Prospective restrictions on employees','Military statement-based','Continuing individual controversy','Habeas custody in a continuous','Conviction-negating damages','Ministerial court reporting','Qualified-immunity eligibility','Presidential civil immunity']
standards=(root/'state/STANDARDS_AND_TESTS.md').read_text(encoding='utf-8')
titles=re.findall(r'^### (.+)$',standards,re.M)
headings=[]
for q in queries:
    matches=[t for t in titles if q in t]
    assert len(matches)==1,(q,matches)
    headings.append(matches[0])
args=[sys.executable,str(root/'tools/build_entering_law.py'),str(dst/'OT_1997CHUNK4.md')]
for a in areas:args+=['--holdings-area',a]
for h in headings:args+=['--standard-heading',h]
args+=['--standing-heading','1. Current Court','--standing-heading','3. Standing Practices']
subprocess.run(args,check=True)
names=['United States v. Lopez','United States v. Hale','Sandin v. Conner','Young v. Harper','Lewis v. Casey','Board of County Commissioners, Wabaunsee County v. Umbehr','Crawford-El v. Britton','Reich v. Collins','Fulton Corp. v. Faulkner','Camps Newfound/Owatonna','Zatko v. California','Martin v. District','Demos v. Storrie','Day v. Day','In re Sassower','In re Anderson','Landgraf v. USI','Shalala v. Guernsey','Thomas Jefferson University','Brown v. Gardner','Matsushita Electric','Richards v. Jefferson','Caterpillar Inc. v. Lewis','Peacock v. Thomas','Bennett v. Spear','Lujan v. Defenders','MCI Telecommunications','NationsBank of North Carolina','Hagen v. Utah','Fletcher v. Kalina','United States v. Lanier','Johnson v. Jones','Behrens v. Pelletier','Elder v. Holloway','Buckley v. Fitzsimmons','Walmer v. Department','Thomasson v. Perry','Romer v. Evans','Waters v. Churchill','United States v. National Treasury','Heck v. Humphrey','Arizonans for Official English','Garlotte v. Fordice','Edwards v. Balisok','United States v. James Daniel','Antoine v. Byers','Richardson v. McKnight','Clinton v. Jones']
parts=['# OT1997 chunk 4 — Compact entering-law selections','','Exact selected complete case blocks copied from current canonical Holdings volumes. Full selected-volume tool copy: [OT_1997CHUNK4.md](OT_1997CHUNK4.md). This reading aid is not authority. Effective current-term law follows below; uncoordinated same-day peers share one pre-group baseline.','']
receipt=[]
for area in areas:
    p=root/'state/holdings'/f'{area}.md'; lines=p.read_text(encoding='utf-8').splitlines()
    starts=[i for i,l in enumerate(lines) if re.match(r'^#{1,4} ',l)]
    for idx,start in enumerate(starts):
        title=lines[start]
        if not title.startswith('#### ') or not any(n in title for n in names):continue
        if 'United States v. Hale' in title and area!='constitutional-structure':continue
        end=starts[idx+1] if idx+1<len(starts) else len(lines)
        parts += [f'## Source: [state/holdings/{area}.md](../../../state/holdings/{area}.md)','', '\n'.join(lines[start:end]).strip(),'']
        receipt.append({'source':str(p.relative_to(root)),'title':title,'line_start':start+1,'line_end':end})
full=(dst/'OT_1997CHUNK4.md').read_text(encoding='utf-8')
parts += ['## Selected current standards and Court setting','',full[full.index('## Standards and Tests selection:'):].strip(),'']
projection=root/'terms/OT1997/workspace/neutral-projection.md';lines=projection.read_text(encoding='utf-8').splitlines()
starts=[i for i,l in enumerate(lines) if re.match(r'^#{1,3} ',l)]
keys=['Brown v. Williams','Jeffries v. Harleston','United States v. Rybar','United States v. Parker','Richenberg v. Cohen','City of Chicago','Clanton','Valot','Smith v. Mattox','Baker v. General Motors','Lunding v. New York','Allentown Mack','South Dakota v. Yankton','McCardle','Danahy','J. Roderick MacArthur']
positionkeys=['Jeffries','Rybar','Richenberg','City of Chicago','Clanton','Valot','Smith','Baker']
public=[]
for idx,start in enumerate(starts):
    title=lines[start]
    if not title.startswith('### ') or not (any(n in title for n in keys) or any(title.startswith('### '+n+' — ') for n in positionkeys)):continue
    end=starts[idx+1] if idx+1<len(starts) else len(lines)
    public += ['\n'.join(lines[start:end]).strip(),'']
    receipt.append({'source':str(projection.relative_to(root)),'title':title,'line_start':start+1,'line_end':end})
addition='\n'.join(['## Current-term public-law selections','','Source: [Current-Term Neutral Projection](../workspace/neutral-projection.md); linked Public Projections identify authority. Copied verbatim from the authorized sanitized projection; no raw Record was read.','']+public)
(dst/'OT_1997CHUNK4.md').write_text(full.rstrip()+'\n\n'+addition+'\n',encoding='utf-8')
parts += [addition]
(dst/'OT_1997CHUNK4_COMPACT.md').write_text('\n'.join(parts).rstrip()+'\n',encoding='utf-8')
(dst/'OT_1997CHUNK4_SELECTIONS.json').write_text(json.dumps({'areas':areas,'standards':headings,'selections':receipt},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Compact bytes:',(dst/'OT_1997CHUNK4_COMPACT.md').stat().st_size,'Selections:',len(receipt))

cases=[
('01_KIRK','1998-02-14','United States v. Kirk',['United States v. Lopez','United States v. Hale'],['Commerce connection'],['United States v. Rybar','United States v. Parker']),
('02_JOHNSON','1998-02-17','Johnson v. Rodriguez',['Sandin','Young v. Harper','Lewis v. Casey','Crawford-El','Umbehr'],['State-created liberty','Revocation of existing','Effective prisoner','Circumstantial proof','Political retaliation'],['Jeffries v. Harleston','Clanton v. Cooper','Valot']),
('03_NEWSWEEK','1998-02-23','Newsweek v. Florida Department of Revenue',['Reich v. Collins','Fulton Corp.','Camps Newfound'],['Backward-looking relief'],['Lunding v. New York']),
('04_ARTEAGA','1998-02-23','Arteaga and Arteaga v. Wilson',['Zatko','Martin v. District','Demos v. Storrie','Day v. Day','In re Sassower','In re Anderson'],['Factual frivolousness'],['Brown v. Williams']),
('05_REGIONS','1998-02-24','Regions Hospital v. Shalala',['Landgraf','Shalala v. Guernsey','Thomas Jefferson University','Brown v. Gardner'],['Statutory temporal reach','Medicare corrective','Medicare educational','Medicare accounting','Controlling weight'],['Allentown Mack']),
('06_RIVET','1998-02-24','Rivet v. Regions Bank',['Matsushita','Richards v. Jefferson','Caterpillar Inc.','Peacock v. Thomas'],['Recognition of state','Constitutional authority to bind','Diversity cured','Ancillary enforcement'],['City of Chicago','Baker v. General Motors']),
('07_NCUA','1998-02-25','NCUA / AT&T Family Federal Credit Union',['Bennett v. Spear','Lujan v. Defenders','MCI Telecommunications','NationsBank'],['Concrete personal','Endangered Species Act citizen','APA review of completed','Limited modification','National-bank annuity'],['Allentown Mack','J. Roderick MacArthur']),
('08_VENETIE','1998-02-25','Alaska v. Native Village of Venetie',['Hagen v. Utah'],[],['South Dakota v. Yankton']),
('09_APONTE','1998-02-26','Aponte Matos v. Toledo Davila',['Crawford-El','Fletcher v. Kalina','United States v. Lanier','Johnson v. Jones','Behrens v. Pelletier','Elder v. Holloway','Buckley v. Fitzsimmons'],['Circumstantial proof','Prosecutorial investigation','Qualified-immunity legal','Relevant precedent'],['Clanton','Smith v. Mattox','McCardle']),
('10_SHAHAR','1998-03-02','Shahar v. Bowers',['Walmer','Thomasson','Romer','Waters','National Treasury','Umbehr'],['Public-employee speech','Prospective restrictions','Military statement','Political retaliation'],['Jeffries','Richenberg','Valot','Danahy']),
('11_SPENCER','1998-03-03','Spencer v. Kemna',['Lujan','Heck v. Humphrey','Arizonans','Garlotte','Edwards v. Balisok'],['Continuing individual','Habeas custody','Conviction-negating','Concrete personal'],['J. Roderick MacArthur']),
('12_LEXECON','1998-03-03','Lexecon v. Milberg Weiss',['Caterpillar Inc.','United States v. James Daniel'],['Diversity cured'],['City of Chicago']),
('13_BOGAN','1998-03-03','Bogan v. Scott-Harris',['Antoine','Buckley v. Fitzsimmons','Fletcher v. Kalina','Richardson v. McKnight','Clinton v. Jones'],['Ministerial court','Prosecutorial investigation','Qualified-immunity eligibility','Presidential civil immunity'],['Danahy','Valot']),
]

def section(text,title,level):
    lines=text.splitlines();start=lines.index('#'*level+' '+title);end=len(lines)
    for i in range(start+1,len(lines)):
        match=re.match(r'^(#+) ',lines[i])
        if match and len(match[1])<=level:end=i;break
    return '\n'.join(lines[start:end]).strip()

index=['# OT1997 chunk 4 entering-law navigation','','These per-case files copy selected authority verbatim. Read the named case slice with the neutral packet. The full tool-built volume copy remains OT_1997CHUNK4.md; no reading copy supplies authority independently.','', '| Order | Event | Case | Reading slice |','|---:|---|---|---|']
for rank,(ident,date,label,needhold,needstd,needpublic) in enumerate(sorted(cases,key=lambda c:(c[1],c[2])),1):
    pparts=[f'# {label} — entering law', '', f'**Event date:** {date}. Baseline: completed public law through February 13, 1998, plus any actually completed material earlier chunk-4 event after the refresh gates in the preflight report. Uncoordinated same-day peers do not enter one another.','']
    for r in receipt:
        title=r['title']
        ishold=r['source'].startswith('state')
        if ishold and not any(n in title for n in needhold):continue
        if not ishold and not any(n in title for n in needpublic):continue
        p= root/r['source']; ls=p.read_text(encoding='utf-8').splitlines()
        pparts += [f"## Source: [{r['source']}](../../../{r['source']})",'', '\n'.join(ls[r['line_start']-1:r['line_end']]).strip(),'']
    for title in headings:
        if any(n in title for n in needstd):pparts += [f'## Standards source: [current register](../../../state/STANDARDS_AND_TESTS.md)','',section(standards,title,3),'']
    pparts += ['## Participation baseline','','All nine Justices are seated throughout the chunk. No case-specific new-run recusal is established. Argument or submission and decision participation require separate confirmation; no historical absence or reason is inferred. [Current Court](../../../state/STANDING_STATE.md#1-current-court).','']
    name=f'OT_1997CHUNK4_{ident}.md'; (dst/name).write_text('\n'.join(pparts).rstrip()+'\n',encoding='utf-8')
    index.append(f'| {rank} | {date} | {label} | [{ident}]({name}) |')
index+=['','## Refresh gates','','- Kirk is first, after the February 13 cursor. Its Commerce ruling has no identified direct dependent merits question in this chunk.','- Johnson precedes Shahar and Spencer. Check any actually adopted general retaliation, liberty or justiciability rule; prisoner-specific application alone does not decide either later case.','- Regions precedes NCUA. Check any actually adopted general statutory-interpretation or agency-review rule; Medicare-specific authority alone does not decide credit-union membership.','- Rivet precedes Spencer and Lexecon. Check any actually adopted general jurisdiction or judgment-remedy rule without equating preclusion, mootness and MDL venue.','- Aponte precedes Bogan. A qualified-immunity disposition does not decide legislative absolute immunity; refresh only if an actually adopted general functional rule matters.','- February 23 (Newsweek/Arteaga), February 24 (Regions/Rivet), February 25 (NCUA/Venetie), and March 3 (Spencer/Lexecon/Bogan) are uncoordinated same-day groups and use a common entering baseline.','- Any material change requires clean affected neutral validation, refreezing and affected modeling/reconciliation before assembly; planned dispositions supply no law.','']
(dst/'OT_1997CHUNK4_INDEX.md').write_text('\n'.join(index),encoding='utf-8')
