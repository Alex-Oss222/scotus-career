from pathlib import Path
base=Path('terms/OT1998/runtime/chunk9-control')
src=base/'historical-sources'
selections={
'Cunningham v. Hamilton County':('98-727', ['Petitioner, an attorney, represented', 'A Magistrate Judge oversaw discovery.', 'Petitioner failed to heed', 'At a July 19 hearing,', 'The District Court affirmed the Magistrate', 'Although proceedings in the District Court were ongoing,', '1. Starcher died','2. He also ordered petitioner']),
'Dickinson v. Zurko':('98-377',['The case before us tests these two competing legal views.']),
'Lilly v. Virginia':('98-5881',['On December 4, 1995,','After taking them into custody,','A tape recording of Mark','The police told Mark','The Commonwealth of Virginia charged','The Supreme Court of Virginia affirmed','“[A]dmissiblity into evidence','“That Mark Lilly’s statements']),
'City of Chicago v. Morales':('97-1121',['Before the ordinance was adopted,','The council found that','The ordinance creates a criminal offense','Two months after the ordinance','During the three years of its enforcement,','The Illinois Supreme Court affirmed.','In support of its vagueness holding,','2. The ordinance states in pertinent part:','6. The city began enforcing']),
'Greater New Orleans Broadcasting Association v. United States':('98-387',['Petitioners are an association of Louisiana broadcasters','Petitioners brought this action against the United States','On remand, the Fifth Circuit majority adhered'])}
out=['# Sanitized objective factual extracts — group B','', 'Scope: excerpts copied programmatically from saved primary-opinion reproductions. They supply published recitations of record facts and lower-court procedure only. They are not the original briefs or appendix. Judicial characterizations are attributed recitations, not independent findings. No current-case Supreme Court merits result, rationale, votes, or separate writing is included. A fresh neutral context must validate this selection before use.','']
for name,(docket,prefixes) in selections.items():
    lines=(src/f'{docket}.ZO.compact.txt').read_text(encoding='utf-8').splitlines()
    out += [f'## {name}',f'Public source: https://www.law.cornell.edu/supct/html/{docket}.ZO.html','']
    for pre in prefixes:
        found=[x for x in lines if x.startswith(pre)]
        assert len(found)==1,(docket,pre,len(found))
        s=found[0]
        if docket=='98-377':s=s.replace('The case before us tests these two competing legal views. ','')
        if docket=='98-387' and pre.startswith('On remand,'):s=s.split(' Because the Court of Appeals')[0]
        out += ['> '+s,'']
(base/'SANITIZED_GROUP_B_FACT_EXTRACTS.md').write_text('\n'.join(out),encoding='utf-8')
print('Wrote sanitized factual extracts.')
