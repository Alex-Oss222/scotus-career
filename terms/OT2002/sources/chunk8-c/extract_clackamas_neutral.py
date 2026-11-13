from pathlib import Path

root = Path(__file__).resolve().parent
source = root.parent / 'chunk8-comparators'
texts = {suffix: (source / ('01-1435.' + suffix + '.html.txt')).read_text(encoding='utf-8') for suffix in ('ZO', 'ZD')}

def clip(suffix, start, end):
    text = texts[suffix]
    left = text.index(start)
    right = text.index(end, left) + len(end)
    return text[left:right]

items = [
    ('Reported control and financial incidents', clip('ZO', 'For example, they apparently control the operation of their clinic', 'personally liable for malpractice claims.')),
    ('Work, agreements, premises and organizational standards', clip('ZD', 'The doctors provide services on behalf of the corporation', 'App. 66;')),
    ('Other statutory classifications acknowledged in the published record', clip('ZD', 'The Employee Retirement Income Security Act of 1974', 'Ore. Rev. Stat. Ann. §656.005(30) (1996 Supp.).')),
    ('Weekly headcount recitation', clip('ZD', 'In 1996, Clackamas had 4 physician-shareholders', 'current or preceding calendar year”).')),
    ('Additional record evidence', clip('ZO', '11.  For example, the record indicates', 'Ibid.')),
]
lines = ['# Clackamas: source-only factual excerpts for clean neutral review', '',
         'Source: Clackamas Gastroenterology Associates, P. C. v. Wells, 538 U.S. 440 (2003), published judicial record recitations. These excerpts establish what the published opinion reports about the record; they do not represent independent review of the underlying appendix, contracts or argument transcript. They contain no disposition, alignment or current-position recommendation. Existing entering-law and neutral materials remain separately applicable.', '',
         'The text below was extracted by script from the saved complete primary text. Original citations and source ellipses are retained. The first excerpt ends at its record citation and does not include the ensuing legal argument. These passages require fresh neutral validation before any new modeling input.', '']
for title, excerpt in items:
    lines += ['## ' + title, '', *('> ' + line for line in excerpt.splitlines()), '']
target = root / 'Clackamas-neutral-source-excerpts.md'
target.write_text('\n'.join(lines), encoding='utf-8')
print(target.relative_to(root.parents[2]))
