from pathlib import Path
d=Path('terms/OT1999/sources/chunk6-comparator')
for key in ['fischer-99-116','johnson-99-5153','public-lands-98-1991','morrison-99-5','geier-98-1811','jones-99-5739','playboy-98-1682']:
 print(key)
 for i,line in enumerate((d/(key+'.ZO.txt')).read_text(encoding='utf-8').splitlines()):
  if line.strip().startswith(('“','"')) or 'provides' in line[:180] or 'providing' in line[:180]:print(i+1,line[:160])
