from pathlib import Path

p = Path(__file__).parent
t = (p / 'grokster_ZO.txt').read_text(encoding='utf-8')
c = (p / 'grokster_ZC.txt').read_text(encoding='utf-8')

def cut(text, start, end):
    a = text.index(start)
    b = text.index(end, a)
    return text[a:b].strip()

parts = [
    '# Grokster neutral qualification request — reconciliation source extraction\n\n'
    'For control and a fresh neutral validator, then the independent model only after validation. '
    'This document contains objective lower-court posture and evidence descriptions, not a present vote, author, or proposed current disposition. '
    'The frozen baseline remains unchanged. Research cutoff: June 27, 2005.\n\n'
    'Validate the existing packet against these source recitations: the precise cross-motion and current-version scope; the uncontested direct-infringement conclusion below; the status of unreleased promotional drafts as evidence; the parties\' continuing disagreement over substantial lawful capability, and the inability to equate unknown files automatically with authorized downloads. '
    'Assess any required scope, remand, and alternative distribution-theory commitments without importing the historical outcome. '
    'Past conduct may be evidence relevant to then-current distribution; it should not be excluded solely because it preceded that software version. That last proposition is a legal argument to assess, not a new adjudicated historical fact.\n',
    '## Source recitation: current-version cross-motions and ruling below\n\n'
    'Source: https://www.law.cornell.edu/supct/html/04-480.ZO.html, Part I-B.\n\n'
    + cut(t, 'After discovery, the parties', 'The Court of Appeals affirmed.'),
    '## Source recitation: limits of the statistics\n\n'
    'Source: the same writing, Part I-A.\n\n'
    + cut(t, 'As for quantification,', 'Grokster and StreamCast are not,'),
    '## Source recitation: publicity of promotional drafts\n\n'
    'Source: the same writing, note 7.\n\n'
    + cut(t, 'The record makes clear that StreamCast', '8.'),
    '## Source recitation: respondents\' scope objection\n\n'
    'Source: the same writing, note 13; only the reported contention is copied.\n\n'
    + cut(t, 'Grokster and StreamCast contend that', 'This contention misapprehends'),
    '## Source recitation: statistics not classifying the residual files\n\n'
    'Source: https://www.law.cornell.edu/supct/html/04-480.ZC.html, note 3; the following reports the expert study, rather than adopting an inferential conclusion.\n\n'
    + cut(c, 'That survey identified 75%', 'Even assuming, as Justice'),
    '## Source recitation: no concession of the Sony issue\n\n'
    'Source: the same writing, note 4. The published characterization of the parties\' litigation positions is copied; its rhetoric is not an independent finding.\n\n'
    + cut(c, 'The District Court’s conclusion', '\n \n'),
]
(p / 'GROKSTER_NEUTRAL_QUALIFICATION_REQUEST.md').write_text('\n\n'.join(parts) + '\n', encoding='utf-8')
print('Wrote source-bounded request.')
