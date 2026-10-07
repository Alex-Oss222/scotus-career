from pathlib import Path

p=Path(__file__).parent
tax=p.joinpath('tax1982.txt').read_text(encoding='utf-8')
a=tax.index('§ 4371.'); b=tax.index('CHAPTER 35',a)
p.joinpath('IBM_1982_STATUTORY_EXTRACT.txt').write_text(tax[a:b],encoding='utf-8')
er=p.joinpath('erisa1994.txt').read_text(encoding='utf-8')
parts=['# ERISA statutory source extracts\n\nVerbatim extraction from the 1994 United States Code, title 29, https://www.govinfo.gov/content/pkg/USCODE-1994-title29/html/USCODE-1994-title29.htm . Source extraction, not construction.']
defs=er[er.index('§1002. Definitions'):]
a=defs.index('(21)(A)'); b=defs.index('(22)',a)
parts += ['## Section 3(21), 29 USC 1002(21)\n\n'+defs[a:b]]
for start,end in [('§1103. Establishment of trust','§1104.'),('§1104. Fiduciary duties','§1105.'),('§1106. Prohibited transactions','§1107.')]:
 a=er.index(start); b=er.index(end,a); parts += ['## '+start+'\n\n'+er[a:b]]
ob=p.joinpath('obra1986.txt').read_text(encoding='utf-8')
a=ob.index('SEC. 9204. EFFECTIVE'); b=ob.index('Subtitle D—',a)
parts+=['## OBRA section 9204\n\nVerbatim OCR extraction from Public Law 99-509, 100 Stat. 1979–1980, official PDF pages 106–107. Typographic OCR noise must not be treated as statutory wording.\n\n'+ob[a:b]]
p.joinpath('SPINK_STATUTORY_EXTRACT.md').write_text('\n\n'.join(parts)+'\n',encoding='utf-8')

law=Path('terms/OT1995/entering-law')
links={
'IBM': '''## Current-term reading references and chronology\n\nUse [the complete June 3 projection](OT_1995CHUNK7_PRE_JUNE10_NEUTRAL_PROJECTION.md) with [the chronology note](OT_1995CHUNK7_PRE_JUNE10_CHRONOLOGY_NOTE.md). No June 10 peer supplies entering law. [Fulton, February 21](PUBLIC_Fulton_Corp_v_Faulkner_merits_1996-02-21.md), Holdings and Precedent Treatment, supplies the actual current Commerce Clause/compensatory-tax law if a Commerce analogy is used. It is not an Export Clause holding. The tax volume contains no intervening Export Clause displacement identified in this selection.\n''',
'SPINK': '''## Current-term reading references and chronology\n\nUse [the complete June 3 projection](OT_1995CHUNK7_PRE_JUNE10_NEUTRAL_PROJECTION.md) with [the chronology note](OT_1995CHUNK7_PRE_JUNE10_CHRONOLOGY_NOTE.md). No June 10 peer supplies entering law. Read [Varity, March 19](PUBLIC_Varity_Corp_v_Howe_merits_1996-03-19.md), Holdings I–IV, Precedent Treatment and Separate Writings; and [Peacock, February 21](PUBLIC_Peacock_v_Thomas_merits_1996-02-21.md), Holdings and Law After Decision. In the copied tax volume the precise relevant heading is Pension property transfers and prohibited exchanges (Keystone); in the labor volume use ERISA plan amendment and corporate authority, Insured employee-benefit assets, and ERISA equitable relief against nonfiduciaries. The copied Landgraf standard is the temporal authority.\n''',
'MYERS': '''## Current-term reading references and chronology\n\nFor June 11 use the [current public projection](../workspace/neutral-projection.md), including completed June 10 actions. Read [Ornelas, May 28](PUBLIC_Ornelas_v_United_States_merits_1996-05-28.md), Holdings and Law After Decision, and [Whren, June 10](PUBLIC_Whren_v_United_States_merits_1996-06-10.md), Holdings and Precedent Treatment. In the copied opening volume read Thermal examination of a closed home (Pinson), Court-employee warrant-record errors (Evans), Personal Fourth Amendment rights, Conditional pleas, and Forfeited error on criminal appeal. The June 10 IBM and Spink decisions, when completed, must be checked for any actual effect before final modeling; this source extraction does not presume their results.\n''',
'VERA': '''## Current-term reading references and chronology\n\nFor June 13 use the [current public projection](../workspace/neutral-projection.md) and every subsequently completed earlier-effective current-chunk public action. Read the copied election-law heading Territorial racial design and constitutional deprivation in full, including Miller's separate standing and merits holdings. [Wisconsin, March 20](PUBLIC_Wisconsin_v_City_of_New_York_merits_1996-03-20.md), Holdings, supplies the actual earlier census standing/sufficiency distinctions if invoked. [Romer, May 20](PUBLIC_Romer_v_Evans_merits_1996-05-20.md), Holdings, retains its distinct actual legal-disadvantage setting. Neither creates the missing predicates of a different claim. The operative allegations and judgment are the expressly adopted reconstruction in the neutral packet; no historical Supreme Court racial-predominance judgment supplies law.\n'''
}
for name,addition in links.items():
 q=law.joinpath('OT_1995CHUNK8_A_'+name+'.md')
 s=q.read_text(encoding='utf-8')
 q.write_text(s.rstrip()+'\n\n'+addition,encoding='utf-8')
print('Statutory extracts and current-term reading links written.')
