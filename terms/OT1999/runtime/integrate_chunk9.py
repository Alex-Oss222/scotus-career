from pathlib import Path
import re
import json

TERM = Path(__file__).resolve().parents[1]
# The saved ledger, rather than repository history, identifies the prior record set.
ledger = (TERM / 'runtime/OT_1999CHUNK9_OPENING_ledger.md').read_text(encoding='utf-8')
opening_names = set(re.findall(r'\[record\]\(../records/([^)]*)\)', ledger))
records = []
for path in (TERM / 'records').glob('*.md'):
    if path.name in opening_names:
        continue
    text = path.read_text(encoding='utf-8')
    labels = {}
    for label in ['Case and dockets', 'Event and date', 'Result']:
        labels[label] = re.search(r'^\*\*' + label + r':\*\*\s*(.*)$', text, re.M)[1]
    case = labels['Case and dockets'].split(';')[0].rstrip('.')
    date = re.search(r'\d{4}-\d{2}-\d{2}', labels['Event and date'])[0]
    projection = text.split('## Public Projection', 1)[1].strip()
    parts = re.split(r'^## ([^\n]+)\n', projection, flags=re.M)
    blocks = {parts[i]: parts[i+1].strip() for i in range(1, len(parts), 2)}
    records.append(dict(path=path, case=case, date=date, labels=labels, blocks=blocks,
                        source='admitted-source' in path.name))
records.sort(key=lambda r: (r['date'], r['case']))
court = sum(not r['source'] for r in records)
sources = sum(r['source'] for r in records)
alaska_done = any(r['case']=='United States v. Alaska' and not r['source'] for r in records)
alaska_stage = ('The June 29 implementing decree has been entered; jurisdiction remains retained only to effectuate and supplement the decree and the parties\' rights.' if alaska_done else 'The parties\' June 7 joint motion and proposed implementing decree are pending for consideration; no decree has yet been entered.')
cursor = max(['2000-06-26'] + [r['date'] for r in records if not r['source']])
stops_path = TERM / 'runtime/OT_1999CHUNK9_STOPS.json'
stops = json.loads(stops_path.read_text(encoding='utf-8')) if stops_path.exists() else {}

def nested(text):
    return re.sub(r'^(#{1,4}) ', lambda m: m[1]+'## ', text, flags=re.M)

def additions(keys):
    out = []
    for r in records:
        body = []
        for key in keys:
            val = r['blocks'].get(key, '')
            if not val or val in ['None.', 'None', 'Not applicable.']:
                continue
            body.append('#### '+key+'\n\n'+nested(val))
        if body:
            out.append('### '+r['case']+' - '+r['date']+'\n\n[Record](../records/'+r['path'].name+')\n\n'+'\n\n'.join(body))
    return '\n\n'.join(out)

rows = ['| '+r['date']+' | ['+r['case']+'](../records/'+r['path'].name+') | '+r['labels']['Result']+' |' for r in records]
status = f'{96+court} Court events and {4+sources} admitted nonjudicial sources are covered.'
chronology = (f'{96+court} Court events are completed: 72 through chunk 6, 12 in chunk 7, 12 in chunk 8 and {court} in chunk 9. '
              f'{4+sources} admitted nonjudicial sources retain their exact scope and effective dates. The chronology cursor is {cursor}. '
              'Uncoordinated same-day decisions share entering law and operate together only prospectively. No institutional change is entered.')
next_stage = ('All eight scheduled chunk 9 Court events are completed; their bounded remands and retained jurisdiction remain as recorded. '
              'No scheduled inventory event remains unprocessed. Fiore and the other opening carryovers retain their actual stages; '
              'Alaska now has its implementing decree, with jurisdiction retained to effectuate and supplement it. Term close is a separate task.') if court == 8 else (
              f'Chunk 9 is in progress: {court} Court events have been entered. Unprocessed inventory matters remain open. '
              'The June 7 Alaska joint motion is an admitted party filing and creates no judicial deadline before decree entry. '
              'Every completed earlier event retains its actual mandate and scope limits.')
if stops:
    next_stage += ' Stopped matters: '+'; '.join(k+': '+v for k,v in stops.items())+'.'

for name in ['continuity', 'neutral-projection']:
    text = (TERM / ('runtime/OT_1999CHUNK9_OPENING_'+name+'.md')).read_text(encoding='utf-8')
    text = text.replace('96 Court events and 4 admitted nonjudicial sources are covered;', status.rstrip('.')+';')
    text = text.replace('after 96 Court events and 4 admitted nonjudicial sources.', f'after {96+court} Court events and {4+sources} admitted nonjudicial sources.')
    text = re.sub(r'96 Court events are completed:.*?(?=\n\n)', chronology, text, count=1, flags=re.S)
    text = re.sub(r'Chunk 8 has twelve completed events;.*?(?=\n\n)', next_stage, text, count=1, flags=re.S)
    heading = '## Completed Events and Admitted Sources' if name == 'continuity' else '## Completed public events and admitted sources'
    start = text.index(heading)
    end = text.index('\n## ', start+1)
    section = text[start:end]
    oldrows = [line for line in section.splitlines() if re.match(r'^\| \d{4}-', line)]
    if oldrows:
        first = section.index(oldrows[0])
        last = section.index(oldrows[-1])+len(oldrows[-1])
        allrows = sorted(oldrows+rows, key=lambda line:(line.split('|')[1].strip(), line.split('|')[2].strip()))
        section = section[:first]+'\n'.join(allrows)+section[last:]
        text = text[:start]+section+text[end:]
    mapping = ([('## Current Law', ['Public Action', 'Judgment & Remedy', 'Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision', 'Source Notes']),
                ('## Material Published Noncontrolling Positions', ['Separate Writings']),
                ('## Current Procedure and Institution', ['Procedure After Action'])] if name == 'continuity' else
               [('## Current-term law', ['Public Action', 'Judgment & Remedy', 'Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision', 'Source Notes']),
                ('## Published noncontrolling positions', ['Separate Writings']),
                ('## Current public procedure and institution', ['Procedure After Action'])])
    for heading, keys in mapping:
        start = text.index(heading)
        end = text.find('\n## ', start+1)
        if end == -1: end = len(text)
        text = text[:end].rstrip()+'\n\n'+additions(keys)+'\n\n'+text[end:].lstrip()
    if name == 'continuity':
        text = text.replace('Court-event research cutoffs are event-specific, from October 18, 1999 through 2000-05-01, as stated in the Records. The four admitted nonjudicial sources preserve their own release, publication, enactment and conditional effective dates.', 'Court-event research cutoffs are event-specific, from October 18, 1999 through '+cursor+', as stated in the Records. The '+str(4+sources)+' admitted nonjudicial sources preserve their own filing, release, publication, enactment and conditional effective dates.')
        end = text.index('\n## Source and Research Cutoff')
        note = '\n\nChunk 9: '+('No adjudicative blocker remains.' if court==8 and not stops else 'Work remains on unprocessed or stopped inventory matters.')
        if stops: note += ' '+'; '.join(k+': '+v for k,v in stops.items())+'.'
        note += ' Git-reference existence and repository commitment remain with the operator; no Git command has been run.\n'
        text = text[:end].rstrip()+note+text[end:]
        text += ('\nChunk 9 uses event-specific research cutoffs through '+cursor+'. The June 7 Alaska filing is admitted at its own date with a late-intake chronology review; '
                 'no earlier completed adjudication is reopened. New Records and frozen handoffs retain precise source limits. The generated chunk Render Input is separate from a public Render.\n')
    text = text.replace('Proposed implementing decree awaited; jurisdiction retained.', 'Implementing decree entered June 29; limited implementation jurisdiction retained.' if alaska_done else 'June 7 joint motion and proposed decree pending; jurisdiction retained.')
    old = 'Alaska overlaps the 104 scheduled matters; the other thirteen are additional unscheduled pending matters. All fourteen stay open at the stated stage. The scheduled date for Alaska does not establish that a proposed decree has been submitted or entered.'
    text = text.replace(old, 'Alaska overlaps the 104 scheduled matters; the other thirteen remain additional unscheduled pending matters at their recorded stages. '+alaska_stage+' The June 7 filing and June 29 action, when entered, rest on their own Records rather than the scheduled date.')
    (TERM / ('workspace/'+name+'.md')).write_text(text, encoding='utf-8', newline='\n')

manifest_path = TERM / 'workspace/manifest.md'
manifest = manifest_path.read_text(encoding='utf-8')
manifest = re.sub(r'^\*\*Current status:\*\*.*$', f'**Current status:** Open after {court} completed chunk 9 events; {96+court} completed Court events in all. Term close has not been performed.', manifest, count=1, flags=re.M)
manifest = re.sub(r'^\*\*Completed OT1999 events:\*\*.*$', f'**Completed OT1999 events:** {96+court} Court events and {4+sources} admitted noncase-law sources. Fiore\'s certification is completed, but the underlying case remains open.', manifest, count=1, flags=re.M)
if alaska_done:
    manifest = re.sub(r'^\*\*Carryovers:\*\*.*$', '**Carryovers:** The 14 opening carryovers remain accounted for. Alaska\'s scheduled implementing decree is completed, with limited retained jurisdiction; the other 13 remain unscheduled at their recorded stages.', manifest, count=1, flags=re.M)
manifest = re.sub(r"Alaska's fourteenth(?: opening)? carryover appears once in the scheduled inventory\..*?(?= No additional effective|\n\n)", "Alaska's fourteenth opening carryover appears once in the scheduled inventory. "+alaska_stage, manifest, flags=re.S)
if not alaska_done:
    manifest = manifest.replace('Proposed implementing decree awaited; jurisdiction retained.', 'June 7 joint motion and proposed decree pending; jurisdiction retained.')
marker = '\n## Chunk 9 current changes\n'
if marker in manifest: manifest = manifest.split(marker)[0].rstrip()+'\n'
manifest += marker+'\n'+next_stage+'\n\n'+alaska_stage+' The [June 7 filing source](../records/united-states-v-alaska-joint-decree-motion_admitted-source_2000-06-07.md) is admitted at its own date, without reopening an earlier adjudication.\n'
manifest_path.write_text(manifest, encoding='utf-8', newline='\n')
print(f'Projected {court} new Court events and {sources} admitted sources; cursor {cursor}.')
