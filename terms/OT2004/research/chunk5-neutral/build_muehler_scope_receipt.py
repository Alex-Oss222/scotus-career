from pathlib import Path

root = Path('terms/OT2004')
parts = ['''# Muehler: neutral question-scope source addendum

This source-control receipt identifies a dispute in the predecision filings about whether qualified immunity is within the two questions presented. It makes no Justice commitment, adopts no side's construction, and states no present-matter Supreme Court outcome or rationale. The supplied scheduled review remains properly before the Court; this is the scope of relief within that review, not verification of a grant or filing event.

The petition's questions address whether questioning and handcuff detention violated the Fourth Amendment. Petitioners' merits brief argues that the related immunity issues are fairly included; respondent's merits brief disputes that scope and gives an alternative merits response. The frozen neutral packet's description of requested immunity relief is not itself adjudication of that dispute. A clean context should decide whether any reachability addition materially affects the existing conditional merits and remedial commitments.

The excerpts below are mechanically copied from the saved predecision source texts, with their OCR retained. They are bounded extracts, not certification that the complete underlying documents were re-read for this receipt. Existing full-record retrieval receipts remain unchanged.
''']
items = [
('Petition questions', 'muehler_02-petition-for-writ-of-certiorari.txt', 62, 96),
('Petitioners: questioning-immunity argument and scope footnote', 'muehler_08-petitioners-brief.txt', 1499, 1533),
('Petitioners: handcuff-immunity argument and scope footnote', 'muehler_08-petitioners-brief.txt', 1968, 1998),
('Respondent: contrary scope footnote and alternative argument', 'muehler_09-respondents-brief.txt', 1991, 2026),
]
for title, filename, start, end in items:
    path = root / 'research/chunk5-record' / filename
    lines = path.read_text(encoding='utf-8').splitlines()
    parts += [f'\n## {title}\n\nSource file: research/chunk5-record/{filename}; copied lines {start + 1}–{end}.\n\n```text\n', '\n'.join(lines[start:end]), '\n```\n']
(root / 'research/chunk5-neutral/Muehler-scope-source-facts.md').write_text(''.join(parts), encoding='utf-8')
