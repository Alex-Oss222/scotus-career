from pathlib import Path
import re

term = Path(__file__).resolve().parents[1]
draft_path = term / 'runtime/OT_1999CHUNK9_ALASKA_RECORD_DRAFT.md'
draft = draft_path.read_text(encoding='utf-8')
public = draft.split('## Public Projection\n', 1)[1]
holdings = public.split('## Holdings\n', 1)[1].split('\n## Precedent Treatment\n', 1)[0].strip()
source = (term / 'preparation/OT_1999CHUNK9_ALASKA_PROPOSED_TERMS_FROM_FILING.md').read_text(encoding='utf-8')
operative = source[source.index('A. Alaska'):source.index('\n\n## Exhibit A')].strip()
assert draft.count('{{COPY_PUBLIC_HOLDINGS}}') == 1
assert draft.count('{{COPY_OPERATIVE_TERMS}}') == 1
draft = draft.replace('{{COPY_PUBLIC_HOLDINGS}}', holdings)
draft = draft.replace('{{COPY_OPERATIVE_TERMS}}', operative)
draft = draft.replace('https://www.govinfo.gov/content/pkg/USCODE-1994-title43/pdf/USCODE-1994-title43-chap29-subchapIII.pdf', 'https://www.govinfo.gov/content/pkg/USCODE-1994-title43/pdf/USCODE-1994-title43.pdf')
draft_path.write_text(draft, encoding='utf-8')
internal = draft.split('## Controlling holdings\n', 1)[1].split('\n## Continuity and source status\n', 1)[0].strip()
assert internal == holdings
assert draft.split('## Exact adopted operative source annex\n', 1)[1].split('\n## Public Projection\n', 1)[0].endswith(operative + '\n')
blocks = re.findall(r'^## (.+)$', public, re.M)
assert blocks == ['Event', 'Participation', 'Public Action', 'Judgment & Remedy', 'Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision', 'Separate Writings', 'Procedure After Action', 'Source Notes'], blocks
lengths = [len(m.group(1).split()) for m in re.finditer(r'\*\*Controlling explanation:\*\* (.*?)(?=\n\n###|\Z)', holdings, re.S)]
assert len(lengths) == 5
assert max(lengths) <= 350
print({'eleven_blocks': True, 'identical_holdings': True, 'exact_operational_copy': True, 'explanation_words': lengths, 'draft_only': str(draft_path.relative_to(term))})
