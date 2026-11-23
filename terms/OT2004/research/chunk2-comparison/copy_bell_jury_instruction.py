from pathlib import Path
base=Path('terms/OT2004/research/chunk2-comparison')
s=(base/'bell_full.txt').read_text(encoding='utf-8')
a=s.index('The jury was instructed with respect to this aggravated circumstance as follows:')
b=s.index('359 F. 3d, at 794.',a)+len('359 F. 3d, at 794.')
p=base/'BELL_NEUTRAL_RULE_APPLICATION.md'
p.write_text(p.read_text(encoding='utf-8')+'\n## 6. The jury definitions reported below\n\nThe following instruction is reported in the Sixth Circuit opinion at 359 F.3d 794 and reproduced at 543 U.S. 452 n.4. It is included to permit comparison of the actual jury language and the authoritative state construction without assuming that their contents were identical. Its constitutional effect remains an independent legal question.\n\n'+s[a:b]+'\n',encoding='utf-8')
print(s[a:b])
