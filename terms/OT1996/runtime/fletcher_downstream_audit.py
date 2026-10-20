from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
RECORDS = ROOT / 'terms/OT1996/records'
FREEZE = ROOT / 'terms/OT1996/freeze'
NAMES = ['Stone-Zsela', 'Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer']
TARGET = 'Fletcher_v_Kalina_merits_1997-06-16.md'


def normalized(text):
    return text.translate({0x2019: 0x27})


def census():
    rows = []
    for p in RECORDS.glob('*.md'):
        raw = p.read_bytes()
        text = raw.decode('utf-8-sig')
        ev = next((line for line in text.splitlines()[:5] if line.startswith('**Event and date:**')), '')
        match = re.search(r'\d{4}-\d{2}-\d{2}', ev)
        if not match:
            raise RuntimeError('Event date absent: ' + p.name)
        case = text.splitlines()[0].split('**Case and dockets:**')[-1].strip().split(';')[0]
        public = text.split('## Public Projection')[-1]
        top = next((b for b in re.split(r'(?m)^## ', public) if b.startswith('Opinion Topology')), '')
        authors = []
        for line in normalized(top).splitlines():
            if not line.startswith('|'):
                continue
            cells = [c.strip() for c in line.strip('|').split('|')]
            if re.search(r'(?i)^opinion of the court|^court opinion|^same opinion|^lead opinion|^opinion announcing', cells[0]) and cells[1] in NAMES:
                authors.append(cells[1])
        if not authors:
            lead = re.search(r"(Stone-Zsela|Stevens|O'Connor|Scalia|Kennedy|Souter|Thomas|Ginsburg|Breyer) (?:delivers|writes) (?:the )?(?:unanimous )?[Oo]pinion of the Court", normalized(top))
            if lead:
                authors.append(lead.group(1))
        authors = list(dict.fromkeys(authors))
        counted = bool(authors) and ('merits' in p.name or p.name.startswith('Lynce_') or p.name.startswith('Department_of_State_'))
        if 'merits' in p.name and not authors:
            raise RuntimeError('Unresolved merits form: ' + p.name)
        rows.append({'date': match.group(), 'case': case, 'file': p.name, 'authors': authors, 'counted': counted,
                     'topology_sha256': hashlib.sha256(top.encode()).hexdigest(),
                     'opinion_topology': top,
                     'event': ev})
    rows.sort(key=lambda r: (r['date'], normalized(r['case']).casefold()))
    counts = dict.fromkeys(NAMES, 0)
    last = None
    opinions = 0
    for row in rows:
        row['counts_before'] = counts.copy()
        row['last_counted'] = last
        row['opinions_before'] = opinions
        if row['counted']:
            for author in row['authors']:
                counts[author] += 1
            opinions += 1
            last = row['case']
    return rows, counts


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def replace_once(text, before, after):
    if text.count(before) != 1:
        raise RuntimeError('Expected one occurrence: ' + repr(before))
    return text.replace(before, after, 1)


def assignment_segment(text):
    match = re.search(r'(?m)^#{2,3} Assignment(?: countability)?\r?$', text)
    if not match:
        raise RuntimeError('Assignment heading absent')
    end = re.search(r'(?m)^#{2,3} ', text[match.end():])
    stop = match.end() + end.start() if end else len(text)
    return match.start(), stop, text[match.start():stop]


def update_assignment(filename, segment, counts):
    # Only numeral tokens attached to Justice names within this bounded section.
    for name in NAMES:
        variants = [name]
        if name == "O'Connor":
            variants.append('O\u2019Connor')
        for variant in variants:
            segment = re.sub(r'(?<![A-Za-z])' + re.escape(variant) + r'(\s+)(\d+)\b', lambda m: variant + m.group(1) + str(counts[name]), segment)
            segment = re.sub(re.escape(variant) + r' \(\d+\)', variant + ' (' + str(counts[name]) + ')', segment)

    if filename.startswith('Hughes_Aircraft'):
        segment = replace_once(segment, 'Last counted: Crawford-El v. Britton, June 16, 1997.', 'Last counted: Fletcher v. Kalina, June 16, 1997.')
        segment = replace_once(segment, 'The lowest count is 11; all eight form the pool at counts 11, 11, 11, 11, 12, 11, 12 and 11 respectively.', "The lowest count is 11; the complete-opinion pool is O'Connor (12), Scalia (11), Kennedy (11), Souter (12), Thomas (11), Ginsburg (12) and Breyer (11). Stevens (13) is eligible but outside that pool.")
    elif filename.startswith('Piscataway_'):
        segment = replace_once(segment, "the pool is O'Connor (12), Scalia (11) and Thomas (11). Kennedy (12) is outside the pool.", "the pool is O'Connor (12), Scalia (11), Kennedy (12) and Thomas (11).")
    elif filename.startswith('Salazar_Haro'):
        segment = replace_once(segment, "The pool is Stevens (13), Souter (12), Ginsburg (12) and Breyer (11); O'Connor (13) is outside it.", "The pool is Souter (12), Ginsburg (12) and Breyer (11); Stevens (13) and O'Connor (13) are outside it.")
    elif filename.startswith('Metropolitan_Stevedore'):
        segment = replace_once(segment, 'Souter offers the necessary risk/proof formulation at the lower count', 'Souter offers the necessary risk/proof formulation at the same count')
    elif filename.startswith('ODell_'):
        segment = replace_once(segment, 'Stevens can carry the same exact boundaries at the lower count.', 'Stevens can carry the same exact boundaries at the same count.')
    elif filename.startswith('United_States_v_Alaska'):
        segment = replace_once(segment, 'The minimum eligible count is 12; all seven eligible authors are in the minimum-plus-one pool.', "The minimum eligible count is 12; the minimum-plus-one pool is Stone-Zsela (12), O'Connor (13), Kennedy (12), Souter (13), Ginsburg (12) and Breyer (13). Stevens (14) remains eligible but is outside the pool.")
    elif filename.startswith('Agostini_'):
        segment = replace_once(segment, '**Balance pool:** Stone-Zsela, Stevens, Souter, Ginsburg and Breyer.', '**Balance pool:** Stone-Zsela, Souter, Ginsburg and Breyer.')
        segment = replace_once(segment, 'Souter, Stevens and Breyer at13 remain eligible and in the pool;', 'Souter and Breyer at 13 remain eligible and in the pool; Stevens is eligible at 14 and outside it;')
    elif filename.startswith('Cohen_'):
        segment = replace_once(segment, '**Balance pool:** Stone-Zsela, Scalia and Thomas.', '**Balance pool:** Stone-Zsela, Scalia, Kennedy and Thomas.')
    elif filename.startswith('Idaho_'):
        segment = replace_once(segment, '**Balance pool:** Stone-Zsela, Stevens, Souter, Ginsburg and Breyer.', '**Balance pool:** Stone-Zsela, Souter, Ginsburg and Breyer.')
        segment = replace_once(segment, 'Stevens, Ginsburg and Breyer also support the entire lead at 13 and can deliver it;', 'Ginsburg and Breyer also support the entire lead at 13 and can deliver it; Stevens supports the entire lead at 14 but is outside the pool;')
    return segment


def main():
    rows, final_counts = census()
    target = next(r for r in rows if r['file'] == TARGET)
    if target['authors'] != ['Stevens']:
        raise RuntimeError('Fletcher signed lead is not yet Stevens; no records written')
    affected = [r for r in rows if r['date'] >= '1997-06-16']
    planned = []
    for row in affected:
        if row['file'] == TARGET:
            continue
        p = RECORDS / row['file']
        raw = p.read_bytes()
        text = raw.decode('utf-8')
        start, end, before = assignment_segment(text)
        after = update_assignment(p.name, before, row['counts_before'])
        new = text[:start] + after + text[end:]
        assert new.split('## Public Projection')[1] == text.split('## Public Projection')[1]
        assert new[:start] == text[:start] and new[start+len(after):] == text[end:]
        old_paras = re.split(r'(?:\r?\n){2}', before)
        new_paras = re.split(r'(?:\r?\n){2}', after)
        assert len(old_paras) == len(new_paras)
        changed_paras = [{'paragraph_index': i, 'before_sha256': sha(a), 'after_sha256': sha(b)}
                         for i, (a, b) in enumerate(zip(old_paras, new_paras)) if a != b]
        planned.append((p, raw, new.encode('utf-8'), {
            'file': row['file'], 'before_sha256': hashlib.sha256(raw).hexdigest(),
            'after_sha256': hashlib.sha256(new.encode('utf-8')).hexdigest(),
            'assignment_line': text[:start].count('\n')+1,
            'assignment_before_sha256': sha(before), 'assignment_after_sha256': sha(after),
            'public_projection_sha256': sha(text.split('## Public Projection')[1]),
            'changed_paragraphs': changed_paras,
            'outside_assignment_identical': True, 'public_projection_identical': True,
        }))
    # Validate every planned edit before the first write.
    for p, raw, new, receipt in planned:
        if p.read_bytes() != raw:
            raise RuntimeError('Concurrent Record change: ' + p.name)
    for p, raw, new, receipt in planned:
        if raw != new:
            p.write_bytes(new)
    result = {
        'scope': 'Every OT1996 Record dated 1997-06-16 or later; current substantive dependencies and chronological signed-plenary assignment census.',
        'rules': 'Engine sections 2, 8 and 9. Dates then alphabetical case names; signed plenary leads once per delivering author; Kinman has two credits; Department of State follows argument; Lynce follows plenary briefing and argument; summary, unsigned and per curiam actions excluded.',
        'fletcher_lead_author': 'Stevens',
        'substantive_dependency_result': 'No material effect on another judgment, adopted rationale, remedy, participation or published writing.',
        'assignment_result': 'Every other assigned author remains in the applicable pool; existing recorded qualitative fit supports every selection without a new author rationale.',
        'count_matrix': affected,
        'final_counts': final_counts,
        'paragraph_checks': [entry[3] for entry in planned],
        'record_edits': sum(1 for p, raw, new, receipt in planned if raw != new),
        'source_topology_hashes': [{k:r[k] for k in ['file','date','authors','counted','topology_sha256']} for r in rows],
        'counted_census': [{k:r[k] for k in ['file','case','date','authors','event','topology_sha256','opinion_topology']} for r in rows if r['counted']],
    }
    out = FREEZE / 'OT_1996CHUNK11_FLETCHER_DEPENDENCY_CHECKS.json'
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    audit = [
        '# Fletcher v. Kalina — dependency and assignment audit',
        '',
        'Fletcher affirms denial of absolute immunity for the personal factual certification and leaves constitutional liability and personal defenses unresolved. Ordinary conduct-date qualified immunity remains available. Stevens delivers the signed plenary lead.',
        '',
        'The fifteen Records dated June 16, June 19 and June 23 have been reviewed under Engine sections 2, 8 and 9. No other judgment, adopted rationale, remedy, participation or published writing depends on a different Fletcher rule. Every assigned author remains within the applicable balance pool and is supported by the qualitative fit already stated in that Record. There is no material downstream adjudicative or assignment effect.',
        '',
        '| Record | Substantive dependency assessment |',
        '|---|---|',
        '| Associates Commercial Corp. v. Rash | Adjusted Chapter 13 replacement valuation; no prosecutorial or personal-immunity question. Same-day substantive baseline. |',
        '| Crawford-El v. Britton | Ordinary motive proof, tailored discovery and actual causation preserve the existing Harlow/Anderson defense. Same-day substantive baseline; no contrary immunity rule. |',
        '| Del Monte Dunes v. City of Monterey | Municipal takings damages and jury allocation. Imbler supplies the tort character of section 1983; its immunity rules are not adjudicated. Same-day substantive baseline. |',
        '| Fletcher v. Kalina | Personal oath distinguished from advocacy; liability and available personal defenses remain unresolved. |',
        '| Hughes Aircraft v. United States ex rel. Schumer | Statutory temporal application of the former government-possession bar; no personal-immunity premise. Same-day substantive baseline. |',
        '| Mazurek v. Armstrong | Casey and preliminary-relief requirements; no personal-immunity issue. Per curiam summary form adds no count. |',
        '| Piscataway Township v. Taxman | Independent Title VII grounds and source-specific relief; no prosecutorial or personal-immunity premise. Same-day substantive baseline. |',
        '| Salazar-Haro v. INS | Immigration review jurisdiction and unfiled collateral claims; no personal-immunity premise. Same-day substantive baseline. |',
        '| Klehr v. A. O. Smith | RICO accrual, new injury and concealment diligence; no immunity premise. |',
        '| Metropolitan Stevedore v. Rambo | Longshore nominal compensation, proof allocation and administrative application; no immunity premise. |',
        "| O'Dell v. Netherland | Teague and Simmons, with claim-specific habeas predicates and remedy; no civil personal-immunity premise. |",
        '| United States v. Alaska | Baselines, island status and federal retention of submerged lands; no prosecutorial or personal-immunity premise. |',
        '| Agostini v. Felton | Rule 60 and Establishment Clause treatment of public instruction; no immunity premise. |',
        '| Cohen v. Brown University | Prospective athletics accommodation, independent sex-classification scrutiny and institution-specific relief; no personal damages immunity. |',
        "| Idaho v. Coeur d'Alene Tribe | Prospective officer relief and the immune State's remedial limits; no personal-capacity damages or qualified-immunity determination. |",
        '',
        'The June 19 Records identify the June 16 public-law refresh at entering-law/OT_1996CHUNK11_BEFORE_1997-06-19.md, and the June 23 Records identify entering-law/OT_1996CHUNK11_BEFORE_1997-06-23.md. Both reading copies contain Fletcher under its natural authority heading. Their role remains a linked copy of the Record. The Records\' stated absence of a material governing dependency is accurate. Uncoordinated June 16 actions retain the common pre-June-16 substantive baseline; alphabetical sequencing applies only to assignment counts.',
        '',
        'The census reads actual Opinion Topology author cells or explicit delivering-author sentences. It counts each signed plenary lead once per delivering Justice; Kinman supplies one credit each to Stone-Zsela and Ginsburg. The signed Department of State opinion follows argument, and Lynce follows plenary briefing and argument. Summary, unsigned and per curiam dispositions supply no count. An opinion with several parts and one author supplies one credit.',
        '',
        '| Event | Stone | Stevens | O\'Connor | Scalia | Kennedy | Souter | Thomas | Ginsburg | Breyer | Author |',
        '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|',
    ]
    for row in affected:
        audit.append('| ' + row['case'] + ' | ' + ' | '.join(str(row['counts_before'][n]) for n in NAMES) + ' | ' + (', '.join(row['authors']) if row['counted'] else 'Per curiam; excluded') + ' |')
    audit += [
        '',
        'Counts are immediately before each event in date and alphabetical order. The source table, complete counted-event census, final counts, and paragraph and Public Projection hashes are in OT_1996CHUNK11_FLETCHER_DEPENDENCY_CHECKS.json.',
        '',
        '| Assignment | Current pool and selection assessment |',
        '|---|---|',
        '| Rash; Crawford-El; Del Monte Dunes | Ginsburg, Stone-Zsela and Stevens respectively remain in their complete-lead pools. The existing qualitative fit is unaffected. |',
        "| Hughes Aircraft | Complete-lead pool: O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer. Stevens is eligible at 13 but outside the pool; Stone joins the substantive-part pool at 12. Kennedy remains at 11 and the recorded Landgraf/Rivers fit controls. |",
        "| Taxman | O'Connor, Scalia, Kennedy and Thomas form the pool. O'Connor's recorded Johnson/Hopwood formulation supports selection at 12. |",
        "| Salazar-Haro | Souter, Ginsburg and Breyer form the pool; Stevens and O'Connor are eligible at 13 but outside it. Breyer remains the lowest-count pool member at 11. |",
        "| Klehr | Stevens assigns as senior Associate. All six complete-lead eligible Justices remain available; the Chief's balance rule does not bind the assignment. Breyer's recorded coordination of the limitations questions supports selection. |",
        '| Rambo | Stevens, Kennedy, Souter, Ginsburg and Breyer form the pool. Souter and Kennedy are both at 12; the recorded distinction between proof of significant risk and probability of future loss supports Souter without count superiority. |',
        "| O'Dell | Stevens, Souter, Ginsburg and Breyer form the complete-lead pool; the component pools remain as stated. Stevens and Souter are both at 13. The recorded Gardner/Lambrix fit, including the express comparison with Ginsburg at 12, supports Stevens. |",
        "| Alaska | Stone-Zsela, O'Connor, Kennedy, Souter, Ginsburg and Breyer form the pool. Stevens is eligible at 14 but outside it. O'Connor remains at 13 with the recorded paired title-inquiry fit. |",
        '| Agostini | Stone-Zsela, Souter, Ginsburg and Breyer form the pool. Stevens is eligible at 14 but outside it. Ginsburg remains at 12 and the recorded separation of controlling and additional grounds supports selection. |',
        '| Cohen | Stone-Zsela, Scalia, Kennedy and Thomas form the pool. Scalia remains at 11 with the recorded statutory-text/deference fit; Thomas is the equal-count alternative. |',
        '| Coeur | Stone-Zsela, Souter, Ginsburg and Breyer form the pool. Stevens is eligible at 14 but outside it. Stone-Zsela remains the lowest-count eligible author at 12 and the recorded officer/remedy fit supports selection. |',
        '',
        'Edits are confined to assignment-section counts, pool descriptions and count comparisons. Every other byte in these Records, including every Public Projection, is preserved. No substantive entering-law amendment is necessary.',
    ]
    (FREEZE / 'OT_1996CHUNK11_FLETCHER_DEPENDENCY_AUDIT.md').write_text('\n'.join(audit)+'\n', encoding='utf-8')
    # This scratch is generated directly from actual topology, never assignment tallies.
    (ROOT / 'terms/OT1996/runtime/FLETCHER_ASSIGNMENT_TABLE_CENSUS.json').write_text(json.dumps({'rules': result['rules'], 'records': rows}, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps({'record_edits': result['record_edits'], 'checks': str(out), 'final_counts': final_counts}))
    for row in affected:
        print(row['case'], row['counts_before'])


if __name__ == '__main__':
    main()
