"""Project operator-reviewed canonical records into the four-file workspace.

No legal conclusion is computed here. The reviewable companion metadata must
be checked against each preserved Record before this script is run.
"""
from pathlib import Path
import json
import re

term = Path(__file__).resolve().parents[1]
snapshot = term / 'freeze/CHUNK1_OPENING_WORKSPACE'
items = []
for path in (term / 'runtime/assembly').glob('*.json'):
    item = json.loads(path.read_text(encoding='utf-8-sig'))
    if (isinstance(item, dict) and 'record' in item
            and path.stem + '.md' == item['record']
            and (term / 'records' / item['record']).is_file()):
        for field in ('law_summary', 'published_positions', 'next_stage'):
            assert field in item, (path.name, field)
        items.append(item)
items.sort(key=lambda x: (x['date'], x['case']))
assert items, 'No canonical records to project'
assert len({x['record'] for x in items}) == len(items)
for item in items:
    canonical = (term / 'records' / item['record']).read_text(encoding='utf-8')
    assert canonical.count('## Public Projection') == 1
    public = canonical.split('## Public Projection', 1)[1].strip() + '\n'
    copy = term / 'entering-law' / ('PUBLIC_' + item['record'])
    copy.write_text('# Bounded current-term public reading copy\n\n'
                    f"Authority: canonical event {item['case']}, {item['date']}; natural-key Record {item['record']}. "
                    'The following Public Projection is copied unchanged; no audit or private material is included.\n\n' + public,
                    encoding='utf-8')
blocker_path = term / 'runtime/assembly/BLOCKERS.json'
blockers = json.loads(blocker_path.read_text(encoding='utf-8')) if blocker_path.is_file() else []
end = max(x['date'] for x in items)
count = len(items)

def plain(value):
    assert isinstance(value, str), type(value)
    return value.replace('|', '&#124;').replace('\n', ' ')

def link(item, anchor=''):
    return f"[Record](../records/{item['record']}{anchor})"

def table(field):
    title = {'law_summary': 'Controlling law and limits', 'next_stage': 'Disposition and procedure'}[field]
    rows = [f'| Effective date | Matter | {title} | Authority |', '|---|---|---|---|']
    for item in items:
        rows.append(f"| {item['date']} | {plain(item['case'])} | {plain(item[field])} | {link(item)} |")
    return '\n'.join(rows)

position_rows = []
for item in items:
    for position in item['published_positions']:
        position_rows.append(f"- **{item['case']} ({item['date']}):** {plain(position)} {link(item, '#separate-writings')}")
positions = '\n'.join(position_rows) if position_rows else 'No material published separate position is added by these Records.'
positions += '\n\nEarlier public positions remain available in the prior terms’ output files. Preserve each writing’s author, date, proposition, joins and noncontrolling status; a successor does not inherit a retired Justice’s position.'

def section(text, title, body):
    pattern = rf'(?ms)(^## {re.escape(title)}\n).*?(?=^## |\Z)'
    result, changed = re.subn(pattern, lambda m: m.group(1) + '\n' + body.strip() + '\n\n', text, count=1)
    assert changed == 1, title
    return result

cursor = (f'Chunk 1 has {count} completed Court events through **{end}**. '
          f'{len(blockers)} matter(s) remain stopped as identified below; no event or law is inferred for them. '
          'The next scheduled inventory event after this processed range is Louisiana v. Mississippi’s December 4, 1995 decree in chunk 2. '
          'The five undated inherited carryovers remain open on their existing terms. Same-day events retain their common entering-law baseline.')

def common(text):
    text = re.sub(r'(?m)^The next dated inventory event is .*?$', cursor, text)
    text = text.replace('Dates are supplied planning dates, confirmed against the neutral intake metadata and Section I, not completed Court actions.',
                        'Dates for completed entries are established by their Records; dates for remaining entries are supplied planning dates, not completed Court actions.')
    text = text.replace('No supplied inventory event was removed, added, rescheduled or decided.',
                        'No supplied inventory event was removed, added or rescheduled; completed actions are listed below.')
    text = text.replace('The [manifest](manifest.md) is the initial Full-Term Event Manifest.',
                        'The [manifest](manifest.md) is the current Full-Term Event Manifest.')
    text = text.replace('No review of Stone\'s supplement, approval, compatibility or vote is performed at opening. All substantive Run stages remain separate tasks.',
                        'The opening validation did not review Stone\'s supplement, approval, compatibility or vote. Current Run validation is recorded separately in the chunk control and validation artifacts.')
    text = text.replace('Sources used: governing foundation files;', 'Opening-stage sources: governing foundation files;')
    text = text.replace('No Section II or III content was opened into this context.',
                        'The opening-stage receipt records that no Section II or III content was opened there.')
    text = text.replace(
        'Original action; prospective decree after the still-unprocessed October 31 exceptions event; boundary schedule requires authentication.',
        'Original jurisdiction retained after the completed October 31 exceptions decision. Before the precise decree, authenticate Point 3: Appendix A gives 32°48′47″N and Appendix E gives 32°49′47″N, both at 91°09′37″W. No disputed coordinate is operative.')
    text = text.replace(
        'Process the exceptions event first. Refresh from its actual judgment and authenticate the boundary schedule before implementation; adoption of the report, a particular boundary and cancellation of private titles are not assumed.',
        'The [October 31 Record](../records/Louisiana_v_Mississippi_original_exceptions_1995-10-31.md) overrules the exceptions and adopts the former-channel recommendation at its stated merits scope, denies another hearing, leaves private-title cancellation rejected, and retains jurisdiction. The precise decree requires resolution of Point 3: Appendix A 32°48′47″N versus Appendix E 32°49′47″N, both 91°09′37″W; obtain the cited surveys or an authenticated correction.')
    text = text.replace(
        "Louisiana's December 4 implementation depends on its actual October 31 judgment and an authenticated survey schedule.",
        "Louisiana's October 31 exceptions judgment is completed. December 4 implementation still requires an authenticated resolution of the Point 3 latitude conflict (Appendix A 32°48′47″N; Appendix E 32°49′47″N; both 91°09′37″W), using P-32D, LA-1A, P-32E, counterclaim paragraph 5 or an authenticated correction; no numerical decree has issued.")
    return text

manifest_path = term / 'workspace/manifest.md'
manifest = common(manifest_path.read_text(encoding='utf-8'))
manifest = re.sub(r'(?m)^\*\*Opening status:\*\*.*$',
                  f'**Current status:** Open; chunk 1 has {count} completed events and {len(blockers)} stopped matter(s). Records control; operator Git verification and commitment remain pending.', manifest)
by_name = {x['record']: x for x in items}
lines = manifest.splitlines()
for i, line in enumerate(lines):
    if not line.startswith('| 1995-') or '| OT_1995CHUNK1 |' not in line:
        continue
    cells = [x.strip() for x in line.strip().strip('|').split('|')]
    if len(cells) != 8:
        raise ValueError('Unexpected manifest row width')
    matches = [item for name, item in by_name.items() if name in cells[6]]
    if matches:
        assert len(matches) == 1
        cells[7] = plain(matches[0]['next_stage'])
    elif cells[6].startswith('Stopped:'):
        cells[7] = 'Pending; no completed Court action or current-term holding.'
    lines[i] = '| ' + ' | '.join(cells) + ' |'
manifest_path.write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')

continuity = common((snapshot / 'continuity.md').read_text(encoding='utf-8'))
continuity = re.sub(r'(?m)^\*\*Posture:\*\*.*$', '**Posture:** ' + cursor + ' **Opening adjudicative cutoff:** 1995-06-29.', continuity)
continuity = re.sub(r'(?m)^No OT1995 Court event or source admission has been completed\..*$',
                    f'{count} current-term Court events are now preserved in canonical Records. The opening trackers remain unchanged; those trackers plus effective Records supply current law. Public separate writings remain noncontrolling at their stated scope.', continuity)
continuity = section(continuity, '2. Completed Events and Admitted Sources', table('next_stage') + '\n\nThe ledger indexes these Records. No separate Admitted Source Record is created by this chunk. Git commitment history remains for the operator to verify.')
continuity = section(continuity, '3. Current Law', 'The opening Holdings and Standards and Tests remain the baseline. The following summaries navigate the effective Records; they do not replace their complete rules, coalitions, reasoning, limits or remedies.\n\n' + table('law_summary'))
continuity = section(continuity, '4. Material Published Noncontrolling Positions', positions)
internal_blockers = '\n'.join(f"- **{b['case']}:** {b['blocker']}" for b in blockers)
continuity = continuity.replace('## 6. Blockers and Revalidation Needs\n', '## 6. Blockers and Revalidation Needs\n\n' + (internal_blockers or 'No chunk 1 matter is stopped.') + '\n\nThe remaining opening intake limits are retained below.\n')
continuity = continuity.replace('## 7. Source and Research Cutoff\n', f'## 7. Source and Research Cutoff\n\nCurrent-term adjudicative cutoff: **{end}**, subject to the expressly stopped earlier matter(s). Each Record states its own cutoff and reading limits. No proposed commitment or later planning date is current law.\n')
(term / 'workspace/continuity.md').write_text(continuity.rstrip() + '\n', encoding='utf-8')

neutral = common((snapshot / 'neutral-projection.md').read_text(encoding='utf-8'))
neutral = re.sub(r'(?m)^\*\*(?:Opening posture|Posture):\*\*.*$', '**Posture:** ' + cursor, neutral)
neutral = re.sub(r'(?m)^No OT1995 Court event or source admission has been completed\..*$',
                 f'{count} current-term Court events are effective as listed below. The opening trackers plus those effective Records supply law; proposed or stopped matters supply none.', neutral)
neutral = neutral.replace('## Court and public procedure\n', '## Completed events and current law\n\n' + table('law_summary') + '\n\n' + table('next_stage') + '\n\n## Court and public procedure\n', 1)
neutral = section(neutral, 'Published noncontrolling positions', positions)
neutral_blockers = '\n'.join(f"- **{b['case']}:** {b['neutral_blocker']}" for b in blockers)
neutral = neutral.replace('## Public source limits and unresolved procedural inputs\n', '## Public source limits and unresolved procedural inputs\n\n' + neutral_blockers + '\n', 1)
neutral = neutral.replace('## Source cutoff\n', f'## Source cutoff\n\nEffective current-term Court law extends through **{end}** only for completed Records. The unresolved earlier matter(s) remain open and supply no holding. Case-specific source limits remain as stated in those Records.\n', 1)
for item in items:
    neutral = neutral.replace('../records/' + item['record'], '../entering-law/PUBLIC_' + item['record'])
(term / 'workspace/neutral-projection.md').write_text(neutral.rstrip() + '\n', encoding='utf-8')
print(f'Projected {count} reviewed Records and {len(blockers)} exact blockers; inherited roster, practices, five carryovers and future intake limits retained. Ledger must be rebuilt separately with the no-Git adapter.')
