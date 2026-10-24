from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[4]
TERM = ROOT / 'terms/OT1997'
BASE = TERM / 'entering-law/OT_1997CHUNK7_A_VOLUME_SLICE.md'

def sections(text, level):
    heads = list(re.finditer(r'^(#{2,5}) (.+)$', text, re.M))
    for i, m in enumerate(heads):
        if len(m.group(1)) == level:
            end = next((n.start() for n in heads[i+1:] if len(n.group(1)) <= level), len(text))
            yield m.group(2), text[m.start():end].strip()

def state_case(slug, query, child=None):
    text = (ROOT / 'state/holdings' / (slug + '.md')).read_text(encoding='utf-8-sig')
    found = [body for title, body in sections(text, 4) if query in title and (child is None or child in body)]
    if not found:
        raise ValueError((slug, query, child))
    return '\n\n'.join(found)

def standard(query):
    text = (ROOT / 'state/STANDARDS_AND_TESTS.md').read_text(encoding='utf-8-sig')
    found = [body for title, body in sections(text, 3) if query in title]
    if len(found) != 1:
        raise ValueError((query, len(found)))
    return found[0]

def current(query):
    text = (TERM / 'workspace/neutral-projection.md').read_text(encoding='utf-8-sig')
    found = [body for title, body in sections(text, 3) if query in title]
    if len(found) != 1:
        raise ValueError((query, len(found)))
    return found[0]

select = {
 'women': [
  ('civil-rights','Planned Parenthood of Southeastern','The framework retaining protected choice'),
  ('civil-rights','Planned Parenthood of Southeastern','Medical emergency and the protective construction'),
  ('civil-rights','Fargo Women'),('federal-courts','Fargo Women'),('federal-courts','Leavitt v.')],
 'atlantic': [('federal-taxation','United States v. Hill'),('environmental-law','Babbitt v. Sweet'),('administrative-law','Auer v. Robbins'),('business-and-commercial-law','Smiley v.')],
 'beach': [('federal-taxation','Reich v. Collins'),('federal-taxation','United States v. Brockamp'),('administrative-law','Reiter v. Cooper')],
 'campbell': [('civil-rights','J.E.B.'),('criminal-procedure','Georgia v. McCollum'),('federal-courts','Georgia v. McCollum')],
 'miller': [('civil-rights','United States v. Virginia'),('civil-rights','Kelley v.'),('civil-rights','Klinger v.'),('federal-courts','Lujan v. Defenders')],
 'deep_sea': [('federal-courts','Idaho v. Coeur'),('federal-courts','Seminole Tribe')]
}
standards = {
 'women':['Protected choice and the six-step','Medical emergency and the separate disclosure-health'],
 'atlantic':['Mineral-depletion basis','Habitat injury within the Endangered Species','Controlling weight for a responsible agency'],
 'beach':['Unreasonable-rate counterclaims','Tax-refund filing and payment limits'],
 'campbell':['Purposeful sex discrimination in state peremptory','Purposeful racial peremptory strikes'],
 'miller':['Effective correction of sex-based educational','Program-wide athletic opportunity','Program-specific prison comparisons','Concrete personal interests'],
 'deep_sea':['Prospective officer relief for ongoing federal property','Prospective officer enforcement of IGRA']
}
currents = {
 'women':[],
 'atlantic':['1998-02-24 — Regions Hospital'],
 'beach':['December 15, 1997 — Bay Area Laundry'],
 'campbell':[],
 'miller':[],
 'deep_sea':[]
}
for case, entries in select.items():
    parts=[f'# OT1997 chunk 7 entering law: {case}', '',
     'Derived exact-text reading copy. Selection follows tools/build_entering_law.py volume generation. The identified state holdings and Standards and Tests, supplemented by earlier effective public law in the Current-Term Neutral Projection, control. No current-matter result is selected here.', '']
    for entry in entries:
        parts += ['## Source: state/holdings/' + entry[0] + '.md', '', state_case(*entry), '']
    for query in standards[case]:
        parts += ['## Source: state/STANDARDS_AND_TESTS.md', '', standard(query), '']
    for query in currents[case]:
        parts += ['## Source: terms/OT1997/workspace/neutral-projection.md', '', current(query), '']
    dest=TERM/'entering-law'/('OT_1997CHUNK7_A_'+case.upper()+'.md')
    dest.write_text('\n'.join(parts).rstrip()+'\n',encoding='utf-8')
    print(dest.relative_to(ROOT), dest.stat().st_size)

# Copy only public separate positions into the relevant scoped law handoffs.
priors = {'women':['Fargo'], 'campbell':['JEB'], 'deep_sea':['Coeur','Seminole']}
for case, names in priors.items():
    path=TERM/'entering-law'/('OT_1997CHUNK7_A_'+case.upper()+'.md')
    append=[]
    for name in names:
        p=TERM/'research/chunk7-neutral-a'/ (name+'_public_prior.md')
        text=p.read_text(encoding='utf-8')
        blocks=[body for title,body in sections(text,4) if 'Separate' in title or 'Noncontrolling' in title or 'Other Opinions' in title]
        if not blocks:
            # Some public outputs use an adaptive opinion heading.
            for title,body in sections(text,4):
                if ('O\'Connor, joined by Scalia' in body or 'Justice Kennedy, concurring in part' in body) and ('holding' not in title.casefold()):
                    blocks.append(body)
        if not blocks:
            raise ValueError(('separate positions not found',name))
        append+=['## Earlier public positions: '+name,'', '\n\n'.join(blocks),'']
    with path.open('a',encoding='utf-8') as f:f.write('\n'+'\n'.join(append))

# Freeze one case-scoped handoff per event. The input brief and generated runtime
# split remain untouched. Stale source-pointer/entering-law prose is not copied.
runtime=(TERM/'runtime/OT_1997CHUNK7_NEUTRAL.md').read_text(encoding='utf-8-sig')
caseheads=list(re.finditer(r'^# (?!SECTION|OT_)(.+)$',runtime,re.M))
runtime_by={m.group(1):runtime[m.start():caseheads[i+1].start() if i+1<len(caseheads) else len(runtime)] for i,m in enumerate(caseheads)}
supp=(TERM/'research/chunk7-neutral-a/NEUTRAL_SUPPLEMENT.md').read_text(encoding='utf-8')
supp_sections=dict(sections(supp,2))
common=supp_sections['Common chronology, participation, and source limits']
lookup={'women':'Women','atlantic':'Atlantic Mutual','beach':'Beach v.','campbell':'Campbell v.','miller':'Miller v.','deep_sea':'California v.'}
source_add={
 'atlantic':['atlantic.md','ATLANTIC_REGULATION_EXCEPTIONS.md'],
 'beach':['beach.md'],
 'campbell':['campbell.md','CAMPBELL_SELECTION_AND_PRESERVATION.md'],
 'miller':['miller.md','MILLER_STATUTE_AND_PROCEDURE.md'],
 'deep_sea':['deep_sea.md','DEEP_SEA_ASA_2105_2106.md'],
 'women':[]}
prior_urls={
 'campbell':['https://www.law.cornell.edu/supremecourt/text/499/400','https://www.law.cornell.edu/supremecourt/text/468/339'],
 'miller':['https://www.law.cornell.edu/supremecourt/text/430/787','https://www.law.cornell.edu/supremecourt/text/486/875','https://www.law.cornell.edu/supremecourt/text/465/728','https://www.law.cornell.edu/supremecourt/text/443/76'],
 'deep_sea':['https://www.law.cornell.edu/supremecourt/text/77/15','https://www.law.cornell.edu/supremecourt/text/256/503']}
index=['# OT1997 chunk 7 A: validated frozen neutral handoff index','',
 'The six case-scoped handoffs below are the authorized neutral inputs. Their paired entering-law slices are exact-text selections from current state and the current-term public projection, with relevant earlier published separate positions. No commitments or results were created by this preflight. Do not provide other current-chunk stage files to an independent model.','']
for case, prefix in lookup.items():
    name=next(n for n in runtime_by if n.startswith(prefix))
    block=runtime_by[name]
    fields=[]
    for label in ['Case Name','Citation or Docket','Simulated Event Date','Question Presented','Question Granted','Relevant Dates']:
        m=re.search(r'^\* \*\*'+re.escape(label)+r':\*\*.*?(?=\n\s*\* \*\*|\n## |\n# |\Z)',block,re.M|re.S)
        if m:fields.append(m.group(0).strip())
    selected=next(body for title,body in supp_sections.items() if title.startswith(prefix))
    parts=[f'# Frozen neutral packet: {name}', '',
        '**Stage:** Neutral preflight complete; no independent model commitment or later-stage material included.',
        '**Research cutoff:** Sources and applicable law must predate or be effective at this event. Women: April 20, 1998; April 21 peers: April 21, 1998; April 22 peers: April 22, 1998. Modern retrieval supplies evidence only, not later law.', '',
        '## Mechanically retained event identity and question formulations','', '\n\n'.join(fields), '',
        common, '', selected, '', '## Required entering-law handoff', '',
        '../entering-law/OT_1997CHUNK7_A_'+case.upper()+'.md', '',
        'This paired file must be read in full. Its exact case holdings and complete Standards and Tests modules supply operative rules, authority, dates, qualifications and remedies. An older source formulation does not replace these rules.', '']
    for f in source_add[case]:
        p=TERM/'research/chunk7_neutral_facts'/f
        parts+=['## Exact control-sanitized source text: '+f,'',p.read_text(encoding='utf-8-sig').strip(),'']
    if case=='women':
        lower=(TERM/'research/chunk7-neutral-a/voinovich_lower.txt').read_text(encoding='utf-8')
        a=lower.index('2\nThe Act creates')
        b=lower.index('B. Procedural History',a)
        fa=lower.index('2\nThe Act defines "medical emergency"',lower.index('142\n'))
        fb=lower.index('\n3\nAppellants argued below',fa)
        sa=lower.index('56\nSeverability is a matter')
        sb=lower.index('\n61\n',sa)
        parts+=['## Exact statutory recitations from the full lower opinion','',
          'Source: https://law.resource.org/pub/us/case/reporter/F3/130/130.F3d.187.96-3159.96-3157.html . These are enacted words and judicial statutory recitations as identified in the lower opinion, not a newly authenticated full session-law transcription. Lower judicial interpretation remains reviewable.','',
          lower[a:b].strip(),'',lower[fa:fb].strip(),'',lower[sa:sb].strip(),'']
    if case in prior_urls:
        parts+=['## Surviving predivergence authority source map','',
            '\n'.join('- '+u for u in prior_urls[case]),'',
            'These primary opinion pages identify the prior authorities discussed above. The Davis and Ex parte New York (No. 2) opinions were read in full; the other source checks establish the stated bounded background propositions, not an exhaustive new audit of every writing. Earlier simulated treatment remains controlling wherever it changes the prior rule.','']
    parts += ['## Boundary and readiness', '',
      'No same-matter historical Supreme Court outcome, vote, or rationale is supplied. The model may use the paired entering-law text, this packet, and Engine rules needed for modeling. Source URLs for current-matter Supreme opinions are provenance only, not authorization to open those opinions. Earlier-day law must be added before a dependent event proceeds. No inference from unavailable original papers establishes litigant default or failure of proof.','']
    dest=TERM/'freeze'/('OT_1997CHUNK7_A_'+case.upper()+'_NEUTRAL.md')
    dest.parent.mkdir(parents=True,exist_ok=True)
    content='\n'.join(parts).rstrip()+'\n'
    for forbidden in ['SUPPLIED_juris','SUPPLIED_supp','sources/','_STONE','_COMPARATOR','None completed in this new run','No completed decisions in this new run']:
        if forbidden in content:raise ValueError(('unsafe source reference',case,forbidden))
    dest.write_text(content,encoding='utf-8')
    index += ['- ['+name+']('+dest.name+') — [entering law](../entering-law/OT_1997CHUNK7_A_'+case.upper()+'.md).']
    print('FROZEN',dest.relative_to(ROOT),len(content))
(TERM/'freeze/OT_1997CHUNK7_A_NEUTRAL.md').write_text('\n'.join(index)+'\n',encoding='utf-8')
