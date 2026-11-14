from pathlib import Path
import json,re

base=Path(__file__).resolve().parent/'chunk13-drafts'
p=base/'C_specs.json'
specs=json.loads(p.read_text(encoding='utf-8'))
s=next(x for x in specs if x['case']=='Gratz v. Bollinger')
s['assignment_authority_text']="The Chief assigns the actual separately reviewed disposition rejecting the intervenors' alternative defense of the 1995–1998 mechanism, which he supports in disposition only under his standing fallback. O'Connor, as senior Justice of the five-Justice coalition, assigns current-program constitutional and statutory invalidity. Standing agreement and preservation of unreviewed immunity rulings supply no assignment authority. One shared eligible author can carry the whole lead, and the Chief-assigned-part balance restriction applies to the common five-Justice pool."
p.write_text(json.dumps(specs,indent=2)+'\n',encoding='utf-8')
p=base/'Gratz-v-Bollinger_merits_2003-06-23.md'
t=p.read_text(encoding='utf-8')
if '| Individual-capacity' in t:
    a=t.index('| Individual-capacity')
    b=t.index('\n\nThe requested admission',a)
    t=t[:a]+t[b:]
    t=t.replace('The requested admission and monetary relief remain for claim-specific adjudication under Part VII. Surviving earlier claims are preserved independently of the current-program disposition.',"The unreviewed qualified-immunity dismissal of the individual-capacity §1983 claims against Bollinger and Duderstadt remains intact, as does the unreviewed denial of the Regents' Eleventh Amendment defense to Title VI. All nine preserve these scope boundaries; Stone supports the dispositions only. The remand cannot reopen the dismissed personal claims or revive the rejected Title VI defense. The requested admission and monetary relief remain for claim-specific adjudication under Part VII. Surviving earlier claims are preserved independently of the current-program disposition.")
    t=t.replace('__ASSIGNMENT_BLOCK__',"The Chief's assignment authority rests on the actual separately reviewed 1995–1998 alternative-defense disposition, supported through his disposition-only fallback; it does not rest on standing agreement or the immunity scope boundaries. O'Connor assigns the current-program invalidity portions.\n\n__ASSIGNMENT_BLOCK__")
    p.write_text(t,encoding='utf-8')

# Repair only obvious character-encoding artifacts in the mechanically copied
# Gratz annex; the authoritative freeze remains unchanged.
t=p.read_text(encoding='utf-8')
for old,new in [('66a?94a','66a–94a'),('Pe?a','Peña'),('IV-D?V','IV-D–V'),('Hopwood I?II','Hopwood I–II'),('Adarand?Hopwood','Adarand–Hopwood'),('1995?1998','1995–1998'),('1999?2000','1999–2000'),('University?s',"University's")]:
    t=t.replace(old,new)
t=re.sub(r'\?(?=(?:601|602|1981|1983)\b)','§',t)
p.write_text(t,encoding='utf-8')

blocks=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
results=[]
for s in specs:
    p=base/s['file']; t=p.read_text(encoding='utf-8'); public=t.split('## Public Projection\n',1)[1]
    hs=re.findall(r'^## (.+)$',public,re.M)
    row={'case':s['case'],'blocks_match':hs==blocks,'assignment_placeholders':t.count('__ASSIGNMENT_BLOCK__'),'publication_placeholders':t.count('__PUBLICATION_STATUS__'),'explanation_word_counts':[]}
    holding=public.split('## Holdings\n',1)[1].split('## Precedent Treatment\n',1)[0]
    for q in re.split(r'(?m)(?=^### )',holding):
        if '**Controlling explanation:**' in q:
            exp=q.split('**Controlling explanation:**',1)[1]
            row['explanation_word_counts'].append({'holding':q.splitlines()[0],'words':len(exp.split())})
    row['word_question_mark_anomalies']=len(re.findall(r'[A-Za-z]\?[A-Za-z]',t))
    assert row['blocks_match']
    assert row['assignment_placeholders']==1
    assert row['publication_placeholders']==1
    assert all(x['words']<=350 for x in row['explanation_word_counts'])
    results.append(row)
(base/'C_draft_validation.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print(json.dumps(results,indent=2))
