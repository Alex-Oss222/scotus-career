from pathlib import Path
import re
import json
import hashlib

term = Path('terms/OT1999')
p = term / 'records/dickerson-v-united-states_merits_2000-06-26.md'
s = p.read_text(encoding='utf-8')
public = s.split('\n## Public Projection\n', 1)[1]
expected = ['Event', 'Participation', 'Public Action', 'Judgment & Remedy', 'Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision', 'Separate Writings', 'Procedure After Action', 'Source Notes']
found = [x for x in re.findall(r'^## (.+)$', public, re.M) if x in expected]
assert found == expected, found
assert s.count('\n## Public Projection\n') == 1
for line, label in zip(s.splitlines()[:4], ['Case and dockets', 'Event and date', 'Result', 'Version / lineage']):
    assert line.startswith(f'**{label}:**'), line
assert '2000-06-26' in s.splitlines()[1]
assert 'October Term 1999, chunk 8' in s.splitlines()[1]
internal_h = s.split('## Controlling holdings\n\n', 1)[1].split('\n\n## Precedent treatment and resulting law', 1)[0]
public_h = public.split('## Holdings\n\n', 1)[1].split('\n\n## Precedent Treatment', 1)[0]
assert internal_h == public_h
r = (term / 'freeze/OT_1999CHUNK8_C_RECONCILED.md').read_text(encoding='utf-8-sig')
frozen = r.split('## Dickerson — reconciliation of all eight Associates\n', 1)[1].split('\n## Reconciliation result and assembly conditions', 1)[0].strip()
actual = s.split('### Frozen non-Stone reconciliation and grounds — mechanically copied\n', 1)[1]
actual = actual.split('\n\n### Historical comparison and departures', 1)[0]
assert actual.endswith(frozen)
explanations = re.findall(r'\*\*Controlling explanation:\*\* (.*?)(?=\n\n\*\*Statutory qualifications:|\Z)', public_h, re.S)
# Separate the genuinely distinct holdings before applying the explanation cap.
word_counts = []
for h in public_h.split('\n### '):
    if '**Controlling explanation:** ' not in h:
        continue
    body = h.split('**Controlling explanation:** ', 1)[1].split('\n\n**Statutory qualifications:', 1)[0]
    word_counts.append(len(body.split()))
assert len(word_counts) == 2 and all(n <= 350 for n in word_counts), word_counts
roster = {'Stone-Zsela', 'Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer'}
support = {'Stone-Zsela', 'Stevens', "O'Connor", 'Kennedy', 'Souter', 'Ginsburg', 'Breyer'}
oppose = {'Scalia', 'Thomas'}
part2 = support - {'Stone-Zsela'}
assert support | oppose == roster and not support & oppose
assert (len(support), len(oppose), len(part2)) == (7, 2, 6)
assert '| Opinion of the Court, Part I | Stevens | Stone-Zsela, O\'Connor, Kennedy, Souter, Ginsburg and Breyer |' in public
assert '| Opinion of the Court, Part II | Stevens | O\'Connor, Kennedy, Souter, Ginsburg and Breyer |' in public
assert '| Dissent | Scalia | Thomas |' in public
counts = json.loads((term / 'freeze/OT_1999CHUNK8_DICKERSON_COUNTS.json').read_text(encoding='utf-8-sig'))
eligible = part2
minimum = min(counts['counts'][j] for j in eligible)
pool = {j for j in eligible if counts['counts'][j] <= minimum + 1}
assert pool == eligible and 'Stevens' in pool and counts['total'] == 88
assert counts['last_event']['case'] == 'Santa Fe Independent School District v. Doe'
assert counts['counts']['Stevens'] == 9 and counts['counts']['Souter'] == 10
assert not (term / 'records/apprendi-v-new-jersey_merits_2000-06-26.md').exists()
for target in re.findall(r'\]\(([^)]+)\)', s):
    if target.startswith('https://'):
        assert 'github' not in target.lower() and 'onedrive' not in target.lower()
    else:
        assert not re.match(r'(?:[A-Za-z]:|file:|/)', target), target
        assert (p.parent / target.split('#')[0]).resolve().exists(), target
assert not re.search(r'https?://[^\s)]*(?:github|onedrive)|file://|[A-Za-z]:\\', s, re.I)
for forbidden in ['Version / lineage', 'reconciled', 'freeze/', 'runtime/', 'approved', 'fallback', 'simulated', 'Git ', '2026', 'modeling', 'assignment', 'workflow']:
    assert forbidden.lower() not in public.lower(), forbidden
for required in ['subject to a properly preserved exception', 'six hours', 'transportation', 'need not be conclusive', 'without interrogation', 'not under arrest or detention', 'oral or written', 'The United States supports Dickerson', 'Paul Cassell', 'no fresh finding', 'judicially reject', 'instruct it to give the confession the weight it deserves in light of all the circumstances']:
    if required == 'no fresh finding':
        assert 'not a fresh finding' in public
    else:
        assert required in public, required
summary = f'''# Dickerson v. United States — assembly validation

**Record:** `records/{p.name}`; SHA-256 `{hashlib.sha256(p.read_bytes()).hexdigest().upper()}`.

**Result:** Assembly self-validation passed. Natural-key identity, exact four opening labels, event/argument dates, October Term 1999 chunk 8 placement, one bounded Public Projection and eleven-block order passed.

**Final pre-integration formatting QA:** The eleven Public Projection block headings use level two and the two holding subheadings retain level three. The formatting normalization changed no substantive Holdings text, judgment, join, ground or remedy. Internal/public Holdings identity was checked again after normalization.

**Final statutory-completeness QA:** Saved official section 3501(a) was checked again. The identical internal/public statutory-qualifications text now expressly states the mandatory jury instruction about the confession's weight under all circumstances, as well as the duty to permit relevant voluntariness evidence. This completes the statutory account without changing the holding, authority, judgment or remedy. Identity and the express instruction clause were checked after this addition.

**Mechanical checks actually performed:** Internal/public Holdings are byte-identical as text; the complete Dickerson frozen-reconciliation section is preserved by programmatic copy; ordinary controlling explanations contain {word_counts[0]} and {word_counts[1]} whitespace-delimited words, each within 350. Judgment arithmetic is seven supporting and two opposing; Part I has seven direct rationale votes and Part II six. The exact authors and joins match those sets. The fresh count contains 88 earlier lead-author counts, ends with Santa Fe on June 19 and places Stevens at nine and the five other eligible Associates at ten; all six are in the balance pool. Apprendi has no Record or count. All relative links resolve, public URLs contain no prohibited service link, and no local-machine/OneDrive/GitHub link occurs. Public text contains none of the tested internal provenance or workflow terms.

**Substantive self-review actually performed:** The two final clean law-review receipts were read, followed by the scoped Stone supplements in order. Apprendi was stopped for the material existing-law/new-constitutional-ground conflict. Dickerson's approved fixed core fits Part I and the restored suppression remedy; its fallback is confined to rejection of the independent judicial-abandonment request and supplies no Part II rationale. Every Associate's result, ground, reservation and remedy remain compatible with the frozen reconciliation. The prosecution's position and the defending amicus's argument are separate; the circuit's voluntariness inference and the district court's custody/warning findings remain separate. The statutory mandatory considerations, nonconclusive-factor permission, six-hour rule and transportation proviso, subsection-(d) alternatives, subsection-(e) definition, independent coercion inquiry and existing exceptions are preserved. The ungranted search, reopening and circuit-issue-raising questions receive no new disposition. Suppression is restored at the case-in-chief scope, subject to a properly preserved exception; no hearing, conviction, acquittal, dismissal or release is invented. Scalia and Thomas's contrary rule requires their own judicial reconsideration and does not claim congressional override of a concededly binding constitutional rule.

**Limits:** This receipt does not certify a new full reread of every historical filing or final shared-workspace integration. The source map and frozen neutral/reconciliation source verification are relied upon for their stated scope. The root must rebuild the shared projections, generate Render Input mechanically and run the term check. No Render, workspace, opening tracker, foundation or earlier Record was edited. No Git command was run or Git hash claimed.
'''
receipt = term / 'freeze/OT_1999CHUNK8_DICKERSON_ASSEMBLY_VALIDATION.md'
receipt.write_text(summary, encoding='utf-8', newline='\n')
print(json.dumps({'record': p.as_posix(), 'validation': receipt.as_posix(), 'explanation_words': word_counts, 'judgment': '7-2', 'part_I': 7, 'part_II': 6, 'author': 'Stevens', 'status': 'passed'}, indent=2))
