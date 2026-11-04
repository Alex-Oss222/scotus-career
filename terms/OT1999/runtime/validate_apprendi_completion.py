from pathlib import Path
import hashlib
import json
import re

term = Path(__file__).resolve().parents[1]
path = term / 'records/apprendi-v-new-jersey_merits_2000-06-26.md'
text = path.read_text(encoding='utf-8')
internal, public = text.split('## Public Projection\n\n', 1)
expected = ['Event', 'Participation', 'Public Action', 'Judgment & Remedy', 'Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision', 'Separate Writings', 'Procedure After Action', 'Source Notes']
actual = re.findall(r'^## (.+)$', public, re.M)
assert actual == expected, actual
labels = ['**Case and dockets:**', '**Event and date:**', '**Result:**', '**Version / lineage:**']
assert all(line.startswith(label) for line, label in zip(text.splitlines()[:4], labels))
assert '**Version / lineage:** Original decision.' in text
assert not re.search(r'2026|stopped|revision|correction|renewed Stone|user.direct', text, re.I)
assert not re.search(r'OneDrive|github\.com|file://|[A-Z]:[/\\]', text)
for link in re.findall(r'\]\(([^)]+)\)', text):
    if not re.match(r'https?://', link):
        assert (path.parent / link.split('#')[0]).exists(), link
parts = dict((m[1], m[2].strip()) for m in re.finditer(r'^## ([^\n]+)\n\n(.*?)(?=^## |\Z)', public, re.M | re.S))
for pub, internal_heading in [('Holdings', 'Controlling holdings'), ('Precedent Treatment', 'Precedent treatment'), ('Law After Decision', 'Law after decision'), ('Separate Writings', 'Published separate writings')]:
    substantive = re.search(r'^## '+re.escape(internal_heading)+r'\n\n(.*?)(?=^## |\Z)', internal, re.M | re.S)[1].strip()
    assert parts[pub] == substantive, pub
explanation = parts['Holdings'].split('**Controlling explanation:**', 1)[1].split('**Application and remedial limit:**', 1)[0]
assert len(explanation.split()) <= 350
counts = json.loads((term / 'freeze/OT_1999CHUNK8_APPRENDI_COUNTS.json').read_text(encoding='utf-8'))
assert sum(counts['counts'].values()) == counts['total'] == 89
assert any(e['record'] == 'ramdass-v-angelone_merits_2000-06-12.md' and e['authors'] == ['Stevens'] for e in counts['counted_events'])
assert not any(e['record'] in ['apprendi-v-new-jersey_merits_2000-06-26.md','dickerson-v-united-states_merits_2000-06-26.md'] for e in counts['counted_events'])
support = ['Stone-Zsela', 'Stevens', 'Scalia', 'Souter', 'Thomas', 'Ginsburg']
opposition = ["O'Connor", 'Kennedy', 'Breyer']
assert len(set(support + opposition)) == 9
assert 'It must be admitted as an element or proved to a jury beyond a reasonable doubt' in parts['Holdings']
assert 'Facts of prior conviction are not decided' in parts['Holdings']
assert "Fifth Amendment's grand-jury clause is not applied to the States" in parts['Holdings']
assert 'No Associate judgment or sufficient rationale is changed in assembly.' in internal
report = {
    'record': path.name,
    'record_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
    'public_projection_sha256': hashlib.sha256(public.encode()).hexdigest(),
    'eleven_blocks_in_order': True,
    'substantive_projection_identity': True,
    'controlling_explanation_words': len(explanation.split()),
    'all_relative_links_resolve': True,
    'original_action_language_check': True,
    'legal_review': 'Frozen commitments, renewed approved Stone scope and bounded final joins compared in assembly; no new independent modeling claimed.',
    'judgment_support': support,
    'judgment_opposition': opposition,
    'counted_author_credits': counts['total'],
    'earlier_ramdass_lead_counted': True,
    'same_date_later_dickerson_excluded': True,
    'author': 'Stone-Zsela',
    'no_git_command_used': True
}
(term / 'freeze/OT_1999CHUNK8_APPRENDI_ASSEMBLY_VALIDATION.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
print(json.dumps(report, indent=2))
