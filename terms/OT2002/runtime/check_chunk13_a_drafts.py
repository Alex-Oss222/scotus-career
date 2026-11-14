from pathlib import Path
import json
import re

root = Path('terms/OT2002/runtime/chunk13-drafts')
specs = json.loads((root/'A_specs.json').read_text(encoding='utf-8'))
blocks = ['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
labels = ['**Case and dockets:**','**Event and date:**','**Result:**','**Version / lineage:**']
results = []
for spec in specs:
    p = root/spec['file']
    text = p.read_text(encoding='utf-8')
    for line,label in zip(text.splitlines()[:4], labels):
        assert line.startswith(label),(p.name,label)
    assert text.count('## Public Projection\n') == 1,p.name
    public = text.split('## Public Projection\n',1)[1]
    assert re.findall(r'^## (.+)$',public,re.M) == blocks,p.name
    assert text.count('__ASSIGNMENT_BLOCK__') == 1,p.name
    assert text.count('__PUBLICATION_STATUS__') == 1,p.name
    assert '| Writing | Author | Joined by | Relationship to judgment | Scope joined |' in public,p.name
    explanations = re.findall(r'\*\*Controlling explanation:\*\*\s*(.*?)(?=\n\n(?:\*\*|###|##)|\Z)',public,re.S)
    lengths = [len(x.split()) for x in explanations]
    assert all(length <= 350 for length in lengths),(p.name,lengths)
    assert set(spec['eligible_authors']) == set(spec['full_joiners']),p.name
    assert len(spec['eligible_authors']) == len(set(spec['eligible_authors'])),p.name
    assert 'HICKS_REFRESH_PENDING' not in public,p.name
    results.append(f"- {p.name}: exact four opening labels and eleven projection blocks; one assignment and publication placeholder; controlling explanations {', '.join(str(n) for n in lengths)} words; {len(spec['eligible_authors'])} full-support eligible authors.")

qa = '''# OT2002 chunk 13 A assembly-content QA

Scope: content drafts only. This pass performs no publication, assignment count, workspace mutation, render, or whole-term validation.

## Deterministic results

'''+ '\n'.join(results)+'''

## Substantive review

- Beaumont: six reverse and three oppose on actual contribution fit. Stone joins the cumulative source-and-channel rationale. Kennedy's changed historical result and Scalia/Thomas's changed doctrinal grounds remain recorded in the copied reconciliation annex. Unused solicitation-branch discussion was removed from the public holding; the source note states only established funding and fund-operation facts.
- Hicks: nine reverse on state-judgment review and insufficient whole-policy substantiality. The separate granted forum question has a sufficient-ground nonreach explanation. The actual-policy denominator, state-law severability, preserved claims, and prohibition on automatic conviction reinstatement remain intact.
- Overton: all nine reverse each facial component. Part I has seven direct joins; Part II has the eight Associates; Part III has nine. The six overlapping Associates can carry the full lead opinion. Stone's express Court-held facial-insufficiency condition activates; his primary remedy remains preserved internally rather than silently rewritten. Scalia and Thomas's alternative application joins do not recognize a general institutional-assistance entitlement.
- Library matter: all nine support the statutory construction; five directly support the bounded facial conclusion, with their broader grounds preserved separately. Stone's primary affirmance and dissent remain; disagreement with the same construction does not trigger his alternative remand. No Marks synthesis, general five-vote forum rule, or categorical subsidy rule is created.
- The five public blocks governed by the negative-statement rule were reviewed. Retained negatives state operative legal qualifications, genuine nonreach, or surviving lower-court judgments and do not list relief no party sought.

## Pending integration

The library draft is expressly provisional. The exact finalized June 16 Hicks Public Projection and clean materiality confirmation must be supplied before any June 23 publication. Its content cannot be treated as a completed adjudication. Serial author assignments, completed-record validation, and all term-level checks remain integration work. A_specs.json states the fixed forms' eligible full supporters and assignment authority; it supplies no counts or author selection. No source Record was edited by this content stage.
'''
(root/'A_QA.md').write_text(qa,encoding='utf-8')
print('\n'.join(results))
print('Wrote A_QA.md; library dependency remains pending.')
