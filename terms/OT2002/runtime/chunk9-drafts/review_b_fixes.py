from pathlib import Path
import hashlib,json,re
root=Path('terms/OT2002/runtime/chunk9-drafts')
changes={
'Herring-v-Keenan_merits_2003-04-29.md':[
('No common narrower immunity rationale is established under Marks.','The immunity rationale remains fractured under Marks.'),
('Their agreement in rejecting this dismissal does not establish a shared rule for deciding other cases. The Court\'s existing objective immunity law remains the general governing law, while this case proceeds under the binding judgment.','The existing objective immunity framework remains the general governing law, while this case proceeds under the binding judgment supported by those distinct grounds.'),
('Marks supplies no basis to turn these different grounds into a single immunity rationale.','Under Marks, these distinct predicates leave the immunity rationale fractured.'),
('The governing objective immunity framework continues for other cases, and the four-Justice notice application here supplies no broader controlling immunity rule.','The governing objective immunity framework continues for other cases; Part II states four Justices\' application to this pleaded account.')],
'Roell-v-Withrow_merits_2003-04-29.md':[
('Section 636(c)(2) and Rule 73 require clerk notice when the action is filed,','Section 636(c)(2) and Rule 73 require written clerk notice when the action is filed,'),
('neither supplies a consent missing from this record.','the present statutory inquiry requires the actual civil consent established by this record.')],
'United-States-v-Miami-University_merits_2003-04-29.md':[
('Written consent must identify the records, reasons and recipients; under §1232g(d), the required consent and parental rights transfer to a student who is eighteen or attends a postsecondary institution.','Written consent must identify the records, reasons and recipients, with a copy furnished to the parents and student if the parents request it; under §1232g(d), the required consent and parental rights transfer to a student who is eighteen or attends a postsecondary institution.'),
('Section (h) separately permits inclusion of appropriate disciplinary information about conduct posing a significant safety or well-being risk to the student or school community,','Section (h) separately permits inclusion of appropriate information about disciplinary action taken for conduct that posed a significant safety or well-being risk to the student or school community,'),
('Section (i) separately permits disclosure to a parent or legal guardian of an under-21 student\'s alcohol or controlled-substance law, rule or policy violation when the institution determines a disciplinary violation; its express saving of state-law prohibitions remains.','Section (i) separately permits disclosure to a parent or legal guardian of an under-21 student\'s violation of a law, institutional rule or policy governing use or possession of alcohol or a controlled substance, whether or not the information is in education records, when the institution determines a disciplinary violation with respect to that use or possession; its express saving of state-law prohibitions remains.'),
('These are proved predicates for relief, not an injury presumption inferred from statutory coverage.','Those findings independently establish the ordinary equitable predicates.')]
}
results=[]
for filename, pairs in changes.items():
 p=root/filename
 original=p.read_text(encoding='utf-8')
 pre,sep,rest=original.partition('### Frozen non-Stone commitments and historical reconciliation — exact source copy')
 annex,projection_sep,pub=rest.partition('## Public Projection')
 assert sep and projection_sep
 before=hashlib.sha256(annex.encode()).hexdigest()
 for old,new in pairs:
  count=pre.count(old)+pub.count(old)
  assert count, (filename,old)
  pre=pre.replace(old,new); pub=pub.replace(old,new)
 pre=pre.replace('## Continuity and published noncontrolling positions','## Published noncontrolling positions')
 revised=pre+sep+annex+projection_sep+pub
 assert hashlib.sha256(revised.split(sep,1)[1].split(projection_sep,1)[0].encode()).hexdigest()==before
 p.write_text(revised,encoding='utf-8',newline='\n')
 headings=re.findall(r'^## (.+)$',pub,re.M)
 expected=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
 assert headings==expected,(filename,headings)
 internal=re.search(r'^## Controlling holdings\n(.*?)(?=^## )',pre,re.M|re.S).group(1).strip()
 public=re.search(r'^## Holdings\n(.*?)(?=^## )',pub,re.M|re.S).group(1).strip()
 assert internal==public,filename
 explanations=[]
 for m in re.finditer(r'\*\*(Controlling explanation|Explanation of authority):\*\* (.*?)(?=\n\*\*|\n### |\Z)',internal,re.S):
  count=len(m.group(2).split()); assert count<=350,(filename,count)
  explanations.append(count)
 results.append({'file':filename,'public_blocks':len(headings),'holdings_identical':True,'explanation_words':explanations,'copied_annex_sha256':before,'annex_unchanged':True})
(root/'B_review_checks.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print(json.dumps(results,indent=2))
