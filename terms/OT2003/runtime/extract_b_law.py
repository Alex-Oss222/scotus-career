from pathlib import Path
import sys
sys.path.insert(0, str(Path('tools').resolve()))
from build_entering_law import take_heading

root=Path('.')
out=Path('terms/OT2003/entering-law')
selections={
61:{'administrative-law':['Arkansas v. Oklahoma, 503 U.S. 91 (1992)','National Railroad Passenger Corp. v. Boston & Maine Corp., 503 U.S. 407 (1992)']},
62:{'criminal-procedure-investigations':['United States v. Ramirez','Soldal v. Cook County, 506 U.S. 56 (1992)']},
63:{'administrative-law':['United States Department of State v. Ray, 502 U.S. 164 (1991)','Bibles v. Oregon Natural Desert Association','Department of Defense v. Federal Labor Relations Authority, 510 U.S. 487']},
64:{'federal-indian-law':['Amoco Production Co. v. Southern Ute Indian Tribe']},
65:{'election-law':['Rice v. Cayetano, 528 U.S. 495'],'civil-rights':['Adarand Constructors, Inc. v. Peña']},
66:{'federal-indian-law':['Strate v. A-1 Contractors','Kiowa Tribe of Oklahoma v. Manufacturing Technologies, Inc.','Atkinson Trading Co. v. Shirley, 532 U.S. 645','Nevada v. Hicks']}
}
for num,vols in selections.items():
    parts=[f'# Case {num} entering-law selection','Derived verbatim reading copy; each cited state volume remains authority.']
    for vol,heads in vols.items():
        t=Path(f'state/holdings/{vol}.md').read_text(encoding='utf-8')
        for h in heads:
            parts += [f'Source: state/holdings/{vol}.md',take_heading(t,h)]
    (out/f'OT_2003CHUNK5_CASE{num}.md').write_text('\n\n'.join(parts)+'\n',encoding='utf-8')
