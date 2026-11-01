from pathlib import Path
base=Path('terms/OT1999/preparation/chunk2-control-sources')
out=Path('terms/OT1999/preparation/OT_1999CHUNK2_CONTROL_NEUTRAL_FACTS.md')
def read(p): return (base/f'USREPORTS-528-{p}.txt').read_text(encoding='utf-8')
def between(s,a,b):
 i=s.index(a); j=s.index(b,i); return s[i:j]
sections=['# OT1999 chunk 2: control-extracted neutral facts\n\nThis handoff contains source-copied record and statutory passages only. It contains no target Supreme Court disposition, lineup, or legal rationale. Excerpts are exact substrings of saved text; page furniture and source typography remain. The full sources are control-only because they also contain historical outcomes. A fresh neutral context must validate these extracts before modeling.\n']
sections+=['## Reno v. Condon\n\nSource: https://www.govinfo.gov/content/pkg/USREPORTS-528/pdf/USREPORTS-528-141.pdf, pp. 143–148. Saved original: `terms/OT1999/preparation/chunk2-control-sources/USREPORTS-528-141.txt`. This statutory recitation describes the October 9, 1999 opt-in amendment and distinguishes mandatory disclosures from permitted disclosures.\n\n```text\n'+between(read(141),'The DPPA regulates the disclosure and resale','We granted')+'```\n']
sections+=['### Condon: scope of government argument\n\nSource: same, p. 148 n.2.\n\n```text\n'+between(read(141),'2 In the lower courts,','\n--- PDF PAGE 9 ---')+'```\n']
s=read(225)
sections+=['## Weeks v. Angelone\n\nSource: https://www.govinfo.gov/content/pkg/USREPORTS-528/pdf/USREPORTS-528-225.pdf, pp. 227–231. Saved original: `terms/OT1999/preparation/chunk2-control-sources/USREPORTS-528-225.txt`. The charge, jury question, judicial response, defense objection, verdict, polling, and prior procedural route appear below. No inference about the jury\'s understanding is adopted.\n\n```text\n'+between(s,'Petitioner Lonnie Weeks, Jr.,','We granted\ncertiorari')+'```\n']
sections+=['### Separate mitigation instruction\n\nSource: same, p. 232 n.2.\n\n```text\n'+between(s,'2 That instruction was titled','\n--- PDF PAGE 9 ---')+'```\n']
sections+=['### Additional mitigation evidence recited in the source\n\nSource: same, p. 248 n.9. These are the source\'s factual recitations; its assessment of the evidence is excluded.\n\n```text\n'+between(s,'9 The evidence showed,','\n--- PDF PAGE 25 ---')+'```\n']
sections+=['### AEDPA posture verification required\n\nThis was a federal habeas challenge to a state judgment. The historical source expressly applies 28 U.S.C. § 2254(d)(1). The neutral packet should separately state the filing date, statutory applicability, and governing entering-law test; the source\'s target resolution is withheld.\n']
out.write_text('\n'.join(sections),encoding='utf-8')
print(str(out))
