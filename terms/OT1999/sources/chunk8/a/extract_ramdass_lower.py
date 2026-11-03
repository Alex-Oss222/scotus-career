from pathlib import Path
base=Path(__file__).resolve().parent
text=(base/'ramdass/07. Joint Appendix_djvu.txt').read_text(encoding='utf-8')
pairs=[('Even were we persuaded by Ramdass\u2019 theory','\n\n\nCc'),('Having determined that Simmons applies only to a','Even if we were not so constrained')]
parts=['# Ramdass: bounded lower-court legal grounds','', 'Exact extracts from the saved joint appendix, printed pages 399-401, reproducing 187 F.3d 396. These are the Fourth Circuit\u2019s reasons, not governing Supreme Court law. The current simulated statutory construction and constitutional holdings control their assessment. Current-matter Supreme Court action, outcome and lineup are absent.']
for start,end in pairs:
    i=text.index(start);j=text.index(end,i)
    parts+=['','```text',text[i:j].strip(),'```']
(base/'ramdass-lower-grounds-safe.md').write_text('\n'.join(parts)+'\n',encoding='utf-8')
print('Copied bounded appellate alternative grounds.')
