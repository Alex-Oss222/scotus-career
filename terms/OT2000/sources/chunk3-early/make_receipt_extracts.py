from pathlib import Path
import hashlib
import re

base = Path('terms/OT2000')
source = base / 'sources/chunk3-early/garrett_09..txt'
t = source.read_text(encoding='utf-8')
parts = [
    '# Garrett: mechanically copied predecision source passages',
    'Source: United States merits brief, No. 99-1240, August 2000; Internet Archive item micro_IA40386004_0922, document 09. Full OCR and PDF are preserved beside this extract. These are the advocate’s statements and quoted materials, not judicial findings. No contemporary Supreme Court decision is included. Current repository law controls over the brief’s descriptions of earlier decisions.',
    'The original document was fully read before the later search exposure reported separately to control. This file was copied mechanically afterward and carries no new neutral framing or validation.',
]
sections = [
    ('Printed pages 9–20: investigation, record descriptions, and employment examples', t.index('1. Congress exhaustively studied the problem', 32000), t.index('\n21 \n', 32000)),
    ('Printed pages 31–50: competing state-law, constitutional-power, and fit arguments', t.index('\n31 \n', 64000), t.index('\nCONCLUSION', 128000)),
    ('Appendix 2a–23a: congressional findings and Title I provisions', t.index('THE AMERICANS WITH DISABILITIES ACT OF 1990', 128000), t.index('\n24a \n', 128000)),
    ('Appendix 28a: express State-immunity provision', t.index('§ 12202. State immunity', 160000), t.index('\n29a \n', 160000)),
]
for label, start, end in sections:
    parts.extend(['## ' + label, t[start:end]])
(base / 'freeze/OT_2000CHUNK3_GARRETT_SOURCE_EXTRACT.md').write_text('\n\n'.join(parts) + '\n', encoding='utf-8')

# Remove a non-source closing-tag fragment left by the HTML boundary extraction.
for name in ['james_1986', 'langnes_1931', 'lake_tankers_1957']:
    p = base / ('sources/chunk3-early/' + name + '.txt')
    p.write_text(p.read_text(encoding='utf-8').replace('\n<div class="tab-pane"\n', '\n'), encoding='utf-8')

paths = [
    base / 'freeze/OT_2000CHUNK3_NEUTRAL_EARLY.md',
    base / 'entering-law/OT_2000CHUNK3_EARLY.md',
    base / 'entering-law/OT_2000CHUNK3_EARLY_SUPPLEMENT.md',
    base / 'entering-law/OT_2000CHUNK3_GARRETT_EQUAL_PROTECTION.md',
    base / 'sources/chunk3-early/prior_public_renders.md',
    source,
    base / 'sources/chunk3-early/garrett_united_states_merits.pdf',
    base / 'freeze/OT_2000CHUNK3_GARRETT_SOURCE_EXTRACT.md',
]
lines = ['# Early preflight selection receipt', '', 'SHA-256 identifies the preserved handoff bytes; it certifies copying, not legal sufficiency.', '']
for p in paths:
    lines.append('`' + p.as_posix() + '` — `' + hashlib.sha256(p.read_bytes()).hexdigest() + '`')
lines.extend(['', 'The initial early-neutral file is the exact first-five-case substring of the regenerated neutral runtime, ending immediately before Semtek. The entering-law builder was run with constitutional-structure, federal-courts and criminal-procedure volumes and eight selected Standards headings plus Current Court. The resulting selection was tightened mechanically by exact headings, then supplemented by the identified maritime/federal-court holdings, current-term SWANCC public fields, and later the separate Garrett equality selection. No source tracker was changed.', '', 'Government-brief discovery: Archive collection listing queried by docket and by case name; the name query identified micro_IA40386004_0922. Separate document 09 is the United States merits brief. Its full OCR, including all 50 printed pages and the 36-page statutory appendix, was read. Document 08 (employees’ brief) was downloaded as OCR and its cover identified, but its substantive text was not reviewed. The combined item, docket, same-matter Supreme Court opinion, and excluded local handoffs were not opened. A later search-result exposure is documented separately for control.', ''])
(base / 'freeze/OT_2000CHUNK3_EARLY_LAW_SELECTIONS.md').write_text('\n'.join(lines), encoding='utf-8')
print('Mechanical extracts and selection receipt written.')
