from pathlib import Path
import re
base=Path(__file__).resolve().parent
source=(base/'idea-1997.txt').read_text(encoding='utf-8')
packet=base/'NEUTRAL_EXACT_EXCERPTS.md'
text=packet.read_text(encoding='utf-8')
def statute(number,next_number):
    starts=list(re.finditer(r'SEC\. '+str(number)+r'\.',source))
    assert len(starts)==1,(number,len(starts))
    start=source.rfind('\n',0,starts[0].start())+1
    end_match=re.search(r'SEC\. '+str(next_number)+r'\.',source[starts[0].end():])
    assert end_match
    end_offset=starts[0].end()+end_match.start()
    end=source.rfind('\n',0,end_offset)+1
    return source[start:end].rstrip()
block='## IDEA section 604; 20 U.S.C. 1403; Public Law 105-17\n\nSource: idea-1997.txt; exact section-marker extraction from SEC. 604 through the beginning of SEC. 605. Includes all three subsections.\n\n```text\n'+statute(604,605)+'\n```\n\n'
block+='## IDEA section 615; complete procedural safeguards provision\n\nSource: idea-1997.txt; exact section-marker extraction from SEC. 615 through the beginning of SEC. 616. Includes receipt-linked procedures, hearing and civil action provisions, remedies and limitations, and the separate-rights/exhaustion clause. Page furniture is retained as in the saved official source.\n\n```text\n'+statute(615,616)+'\n```\n\n'
start=text.index('## IDEA section 604;')
end=text.index('## Carter indictment',start)
packet.write_text(text[:start]+block+text[end:],encoding='utf-8')
print('Copied full sections 604 and 615 by markers; removed incomplete or mislabelled extracts.')
