"""Refresh public-only common baselines; all effective Records, no same-day law."""
from pathlib import Path
import hashlib
import re
import json

TERM = Path(__file__).resolve().parents[1]
ENTERING = TERM / 'entering-law'
rows = []
for path in (TERM / 'records').glob('*.md'):
    text = path.read_text(encoding='utf-8')
    identity = re.search(r'^\*\*Case and dockets:\*\* (.+)$', text, re.M).group(1)
    event = re.search(r'^\*\*Event and date:\*\* (.+)$', text, re.M).group(1)
    date = re.search(r'\d{4}-\d{2}-\d{2}', event).group()
    public = text.split('## Public Projection', 1)[1].strip() + '\n'
    rows.append((date, path.name, identity, public))
rows.sort()
receipts = []
for label, cutoff in [('JUNE14','1996-06-14'), ('JUNE17','1996-06-17'), ('JUNE20','1996-06-20')]:
    earlier = [r for r in rows if r[0] < cutoff]
    lines = [f'# OT1995 revised common neutral baseline before {cutoff}', '',
        'Derived reading copy only. Term-opening authority and each effective Canonical Record control. This baseline incorporates every actual earlier-effective Record; all same-day peers are excluded. It replaces the original chunk 8 snapshot for current work while the original remains a historical stage handoff.', '',
        'Opening trackers: [Holdings volumes](../../../state/holdings/INDEX.md), [Standards and Tests](../../../state/STANDARDS_AND_TESTS.md), [Standing State](../../../state/STANDING_STATE.md), through the completed June 29, 1995 group. The event-date Court is Stone-Zsela, Stevens, O\'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer; no case-specific participation fact is inferred.', '',
        'Only public projections appear in the linked copies. Their Holdings and Law After Decision establish controlling doctrine; published separate positions retain their stated noncontrolling scope. The earlier-case date and the statutory application qualifications control, not link order.', '',
        f'**Earlier Records:** {len(earlier)}. **Same-day Records excluded:** {sum(r[0] == cutoff for r in rows)}.', '',
        '| Effective date | Authority and complete public reading copy | Public Projection SHA256 |', '|---|---|---|']
    for date, name, identity, public in earlier:
        copy = ENTERING / ('PUBLIC_' + name)
        if not copy.exists() or public.strip() not in copy.read_text(encoding='utf-8'):
            copy.write_text('# Bounded current-term public reading copy\n\n' + public, encoding='utf-8')
        digest = hashlib.sha256(public.encode()).hexdigest()
        lines.append(f'| {date} | [{identity.replace("|", "&#124;")}](PUBLIC_{name}) | `{digest}` |')
    lines += ['', '## Excluded same-day peers', '']
    lines.extend('- ' + identity for date, name, identity, public in rows if date == cutoff)
    path = ENTERING / f'OT_1995CHUNK8_REVISION_PRE_{label}_NEUTRAL_PROJECTION.md'
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    receipts.append({'path': str(path.relative_to(TERM)), 'strict_before': cutoff, 'earlier_record_count': len(earlier), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
(TERM / 'freeze/OT_1995CHUNK8_REVISION_NEUTRAL_BASELINES.json').write_text(json.dumps(receipts, indent=2)+'\n', encoding='utf-8')
print(json.dumps(receipts, indent=2))
