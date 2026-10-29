from pathlib import Path
import json,re
W=Path(__file__).resolve().parent
entries=json.loads((W/'draft_entries_345.json').read_text())
for e in entries:
    if 'text' not in e:continue
    t=e['text'];f=e['file']
    t=t.replace('the eight direct joins identified in Opinion Topology',"eight direct joins: Stone-Zsela, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer")
    t=t.replace('the seven direct Associate joins identified in Opinion Topology',"seven direct Associate joins: O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer")
    t=t.replace("the eight Associates' direct joins identified in Opinion Topology","the direct joins of all eight Associate Justices")
    t=t.replace('Part IV has the distinct eight-Justice coalition in the opinion table.','Part IV is joined by Thomas, Stevens, O\'Connor, Scalia, Kennedy, Souter, Ginsburg and Breyer; Stone-Zsela does not join that part.')
    if f.startswith('wright_v_ernst'):
        t=t.replace('All three holdings are adopted in the complete Opinion of the Court by the nine Justices identified in Opinion Topology. Each has direct majority authority; no combination of separate rationales is required.',"**Proposition-level authority:** Thomas's unanimous opinion of the Court controls all three holdings.")
    if f.startswith('boring_'):
        t=t.replace('The complete Opinion of the Court, joined by',"Stone-Zsela's complete opinion of the Court, joined by")
    if f.startswith('minns_'):
        t=t.replace('Five Justices affirm the whole dismissal, but only four adopt',"**Authority of the judgment:** Stone-Zsela, O'Connor, Kennedy, Thomas and Breyer affirm the whole dismissal, 5–4, but only four adopt")
    if f.startswith('stewart_v_lagrand_application'):
        key='##### II. General unavailability does not excuse the earlier omission of the gas claim'
        a,b=t.split(key,1)
        b=b.replace('**Holding:**','**Independent alternative holding:**',1).replace('**Proposition-level authority:**','**Proposition-level authority for alternative holding:**',1)
        t=a+key+b
    if f.startswith('your_home_'):
        extra="""##### Reopening jurisdiction and review of an actual revised reimbursement determination

**Holding:** Section 405.1885(c) gives reopening jurisdiction exclusively to the body that last decided the matter; §405.1889 separately recognizes review when actual reopening produces a revision in the reimbursement amount. The Secretary's fair, considered reading consistent with those provisions receives regulatory deference, while the regulation's mandatory reopening commands remain intact and an agency's jurisdictional label is not conclusive.

**Proposition-level authority:** Kennedy's Part I-B, joined by Stevens, O'Connor, Scalia, Souter, Thomas, Ginsburg and Breyer; eight Justices. Stone-Zsela does not join this additional regulatory ground.

"""
        t=t.replace('##### II. The claim cannot proceed directly under federal-question jurisdiction',extra+'##### II. The claim cannot proceed directly under federal-question jurisdiction')
    # The register keeps operative relief and material coalitions, not advocacy
    # about dispositions that the Court did not adopt.
    t=re.sub(r'The dissent would reverse the status dismissal.*?fee relief\.','',t)
    t=re.sub(r'The dissent would vacate rejection of the common policy claim.*?examination\.','',t)
    t=re.sub(r'Stone-Zsela would vacate the appellate eligibility determination.*?infringement\.','',t)
    t=t.replace('**Opposing:** Justices Kennedy and Thomas, who would reject the federal construction and remand for the unresolved Iowa-law ground.','**Opposing:** Justices Kennedy and Thomas.')
    t=t.replace('Any still-pending collateral matter retains its actual procedural posture.','')
    t=re.sub(r'\n{3,}','\n\n',t)
    e['text']=t
(W/'entries_345.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2))
