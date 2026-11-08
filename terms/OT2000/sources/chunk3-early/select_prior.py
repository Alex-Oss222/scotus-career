from pathlib import Path
import runpy

take = runpy.run_path('tools/build_entering_law.py')['take_heading']
selections = [
    ('terms/OT1999/output/OT_1999CHUNK1.md', 'Kimel v. Florida Board of Regents; United States v. Florida Board of Regents, Nos. 98-791 and 98-796'),
    ('terms/OT1999/output/OT_1999CHUNK6.md', 'Geier v. American Honda Motor Co., No. 98-1811'),
    ('terms/OT1998/output/OT_1998CHUNK11.md', 'Florida Prepaid Postsecondary Education Expense Board v. College Savings Bank, No. 98-531'),
    ('terms/OT1995/output/OT_1995CHUNK9.md', 'Medtronic, Inc. v. Lohr; Lohr v. Medtronic, Inc., Nos. 95-754 and 95-886'),
]
parts = []
for filename, query in selections:
    section = take(Path(filename).read_text(encoding='utf-8'), query)
    print(filename, len(section))
    print('\n'.join(line for line in section.splitlines() if line.startswith('#') or (line.startswith('**') and len(line) < 110)))
    parts.extend(['## Source: ' + filename, section])
Path('terms/OT2000/sources/chunk3-early/prior_public_renders.md').write_text('\n\n'.join(parts) + '\n', encoding='utf-8')

out = Path('terms/OT2000/entering-law/OT_2000CHUNK3_EARLY_SUPPLEMENT.md')
selections = {
    'maritime-law': ['American Dredging Co. v. Miller, 510 U.S. 443', 'Yamaha Motor Corp., U.S.A. v. Calhoun, 516 U.S. 199'],
    'federal-courts': ['FDIC v. Meyer, 510 U.S. 471', 'Lane v. Peña, 518 U.S. 187 (1996)'],
}
parts = ['# Early matters: supplementary prior law', 'Copied mechanically from the identified holdings volumes.']
for area, queries in selections.items():
    filename = 'state/holdings/' + area + '.md'
    for query in queries:
        parts.extend(['## Source: ' + filename, take(Path(filename).read_text(encoding='utf-8'), query)])
out.write_text('\n\n'.join(parts) + '\n', encoding='utf-8')
print(out, out.stat().st_size)
