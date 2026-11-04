from pathlib import Path
import hashlib

term = Path(__file__).resolve().parents[1]
original = term / 'freeze' / 'OT_1999CHUNK9_JONES_NEUTRAL.md'
correction = term / 'preparation' / 'OT_1999CHUNK9_JONES_TASHJIAN_CORRECTION.md'
original_text = original.read_text(encoding='utf-8')
source_text = correction.read_text(encoding='utf-8-sig')
old = "The surviving pre-divergence Tashjian opinions also matter: O'Connor joined the party-autonomy majority; Scalia's dissent and Stevens's joined portion raise distinct public-election/qualification objections."
new = "The surviving pre-divergence Tashjian opinions also matter. O'Connor joined Scalia's separate dissent; Scalia joined Stevens's separate dissent, which concerns federal/state legislative voter qualifications. The exact attribution, grounds and qualifications appear in the sanitized source correction copied below."
assert original_text.count(old) == 1
revised = original_text.replace(old, new)
revised = revised.replace('# Frozen neutral packet — California Democratic Party v. Jones', '# Revised frozen neutral packet — California Democratic Party v. Jones', 1)
note = '''\n## Neutral-handoff lineage and source correction\n\nThis revised neutral freeze supersedes the original Jones neutral freeze solely for the corrected pre-divergence Tashjian attribution and related source qualifications. The original freeze remains preserved. This is a preparation correction before provisional commitments, not a change to an adjudication. The prior neutral receipt's assertion that all supplied attribution was ready is qualified by this identified error. No Jones outcome, vote or Stone position is supplied by the correction.\n\n'''
copied = source_text[source_text.index('## Tashjian attribution and grounds'):source_text.index('## Required next step')].rstrip()
revised += note + copied + '\n'
out = term / 'freeze' / 'OT_1999CHUNK9_JONES_NEUTRAL_REVISED.md'
receipt = term / 'freeze' / 'OT_1999CHUNK9_JONES_NEUTRAL_REVISED_VALIDATION.md'
if out.exists() or receipt.exists():
    raise RuntimeError('Refusing to replace existing revised freezes')
out.write_text(revised, encoding='utf-8', newline='\n')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
body = '''# Jones — revised fresh-neutral validation receipt

Status: READY. The independent neutral context revalidated the sanitized pre-divergence attribution correction without reading any modeled commitment, historical Jones result, comparator, Stone supplement, raw Record or exposure receipt.

The original packet and receipt remain preserved. The revised packet changes the erroneous Tashjian source-map passage and adds the exact saved sanitized correction. O'Connor joined Scalia's dissent, not the majority; Scalia joined Stevens's distinct qualifications dissent. Stevens did not thereby join Scalia's separate associational reasoning. The copied correction preserves the majority's footnotes 6 and 13 qualifications and the distinct scope of Stevens's Eu concurrence. None of these facts supplies a vote in Jones.

All other facts, entering law, the Reform Party addition, chronology, lawful paths and scope limits remain byte-identical within the original packet. The original unresolved source limits remain applicable. Read this revised packet rather than the superseded original packet for modeling.

Additional allowed source read: `preparation/OT_1999CHUNK9_JONES_TASHJIAN_CORRECTION.md`. Previously authorized sources are listed in the original validation receipt. The validator has not opened the linked external opinions itself; it validates the supplied source correction's framing and scope. It makes no broader source-reading claim.

Snapshot integrity:

'''
for p in [original, correction, out]:
    body += f'- `{p.relative_to(term).as_posix()}`: SHA-256 `{sha(p)}`.\n'
receipt.write_text(body, encoding='utf-8', newline='\n')
assert copied in out.read_text(encoding='utf-8')
assert old not in out.read_text(encoding='utf-8')
print('Jones revised neutral packet and validation receipt created; exact correction copied and stale attribution removed.')
