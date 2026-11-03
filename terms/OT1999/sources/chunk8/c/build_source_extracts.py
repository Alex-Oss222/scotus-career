from pathlib import Path
import re
from html import unescape

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent

def write(name, text):
    (HERE / name).write_text(text, encoding='utf-8')

def excerpt(source, start, end, name):
    text = (HERE / source).read_text(encoding='utf-8')
    write(name, f'Source file: {source}\nCharacter interval: [{start}, {end})\nVerbatim downloaded OCR; no transcription correction.\n\n' + text[start:end])

excerpt('apprendi_04._Joint_Appendix.txt', 3200, 16300, 'apprendi_indictment_extract.txt')
excerpt('apprendi_04._Joint_Appendix.txt', 19000, 29500, 'apprendi_plea_extract.txt')
excerpt('apprendi_02._Petition_for_Writ_of_Certiorari.txt', 41800, 48400, 'apprendi_lower_facts_extract.txt')
excerpt('apprendi_05._Petitioners_Brief.txt', 9000, 32000, 'apprendi_petitioner_record_extract.txt')
excerpt('apprendi_06._Respondents_Brief.txt', 9700, 30000, 'apprendi_respondent_record_extract.txt')
excerpt('dickerson_08._Respondents_Brief.txt', 9251, 23500, 'dickerson_us_record_extract.txt')
excerpt('dickerson_20._Amicus_Curiae_Brief.txt', 10880, 18500, 'dickerson_defense_arguments_extract.txt')

# Exact statutory text is obtained from the government HTML, not retyped.
statute = (HERE / '3501_1994.html').read_text(encoding='utf-8')
statute = statute.split('<!-- field-start:statute -->', 1)[1].split('<!-- field-end:statute -->', 1)[0]
statute = unescape(re.sub('<[^>]+>', '', statute))
write('3501_1994_statute.txt', 'Source: https://www.govinfo.gov/content/pkg/USCODE-1994-title18/html/USCODE-1994-title18-partII-chap223-sec3501.htm\nGovernment HTML statutory body, mechanically stripped of tags.\n\n' + statute.strip() + '\n')

public = [
    ('terms/OT1997/output/OT_1997CHUNK6.md', 'Almendarez-Torres'),
    ('terms/OT1998/output/OT_1998CHUNK6.md', 'Jones v. United States'),
    ('terms/OT1992/output/OT_1992CHUNK5.md', 'Withrow v. Williams'),
    ('terms/OT1993/output/OT_1993CHUNK7.md', 'Davis v. United States'),
    ('terms/OT1995/output/OT_1995CHUNK1.md', 'Thompson v. Keohane'),
    ('terms/OT1998/output/OT_1998CHUNK9.md', 'Neder v. United States'),
]
parts = ['# Date-eligible prior public positions — exact extracts\n\nThese are published prior-term decisions, not current-matter outcomes or private commitments. The root entering-law slice remains the reading copy for controlling law.\n']
for file, term in public:
    text = (ROOT / file).read_text(encoding='utf-8')
    heads = list(re.finditer(r'^(#{1,6}) (.+)$', text, re.M))
    first = next(m for m in heads if term in m.group())
    start = first.start()
    level = len(first.group(1))
    end = next((m.start() for m in heads if m.start() > start and len(m.group(1)) <= level), len(text))
    section = text[start:end]
    sep = re.search(r'^#{1,6} Separate Positions Relevant to the Decision\s*$', section, re.M)
    if sep:
        nexthead = re.search(r'^#{1,6} ', section[sep.end():], re.M)
        stop = sep.end() + nexthead.start() if nexthead else len(section)
        section = section[sep.start():stop]
    parts.append('\n## ' + term + '\n\nSource: `' + file + '`\n\n' + section.strip() + '\n')
write('prior_public_positions.md', '\n'.join(parts))

for source, start, end, name in [
    ('roberson_486us675.txt', 30471, 48694, 'roberson_kennedy_source_extract.txt'),
    ('quarles_467us649.txt', 25624, 50999, 'quarles_oconnor_source_extract.txt'),
    ('elstad_470us298.txt', 10920, 44590, 'elstad_oconnor_source_extract.txt'),
]:
    excerpt(source, start, end, name)

print('Wrote 12 source excerpts/statutory or prior-public extracts.')
