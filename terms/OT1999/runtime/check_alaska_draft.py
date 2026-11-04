from pathlib import Path
import re

term = Path(__file__).resolve().parents[1]
path = term / 'runtime/OT_1999CHUNK9_ALASKA_RECORD_DRAFT.md'
text = path.read_text(encoding='utf-8')
text = text.replace("to Icy Cape's northwestern extremity. Paragraph E", "to Icy Cape's northwestern extremity, approximately 70 degrees 21 minutes N., 161 degrees 46 minutes W. Paragraph E")
text = text.replace('ending at Brownlow Point.\n', 'ending at Brownlow Point, approximately 70 degrees 10 minutes N., 145 degrees 51 minutes W.\n')
text = text.replace('The original schedule and operative terms remain controlling; no independent coordinate recalculation or new survey finding is part of this decree.', 'The original schedule and operative terms remain controlling, and the decree makes no new survey finding.')
path.write_text(text, encoding='utf-8')
internal = text.split('## Controlling holdings\n', 1)[1].split('\n## Continuity and source status\n', 1)[0].strip()
public = text.split('## Public Projection\n', 1)[1]
holdings = public.split('## Holdings\n', 1)[1].split('\n## Precedent Treatment\n', 1)[0].strip()
assert internal == holdings
source = (term / 'preparation/OT_1999CHUNK9_ALASKA_PROPOSED_TERMS_FROM_FILING.md').read_text(encoding='utf-8')
operative = source[source.index('A. Alaska'):source.index('\n\n## Exhibit A')].strip()
annex = text.split('## Exact adopted operative source annex\n', 1)[1].split('\n## Public Projection\n', 1)[0]
assert annex.endswith(operative + '\n')
headers = re.findall(r'^## (.+)$', public, re.M)
assert headers == ['Event', 'Participation', 'Public Action', 'Judgment & Remedy', 'Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision', 'Separate Writings', 'Procedure After Action', 'Source Notes']
links = re.findall(r'\]\(([^)]+)\)', text)
missing = [x for x in links if not x.startswith('https://') and not (path.parent / x.split('#')[0]).resolve().exists()]
assert not missing, missing
assert not re.search(r'(?i)simulation|simulated|user-directed|workflow|git|sha-256|draft|approved|reconciliation|frozen|commitment|operator|model', public)
lengths = [len(m.group(1).split()) for m in re.finditer(r'\*\*Controlling explanation:\*\* (.*?)(?=\n\n###|\Z)', holdings, re.S)]
assert len(lengths) == 5 and max(lengths) <= 350
print({'identical_holdings': True, 'exact_A_G_copy': True, 'eleven_blocks': True, 'relative_links_resolve': True, 'public_workflow_scan': 'passed', 'explanation_words': lengths})
