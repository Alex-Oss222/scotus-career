from pathlib import Path

base = Path(__file__).resolve().parent
validation = (base / 'OT_1999CHUNK3_NEUTRAL_VALIDATION.md').read_text(encoding='utf-8').splitlines()
later = (base.parent / 'entering-law/OT_1999CHUNK3_LATER.md').read_text(encoding='utf-8').splitlines()

def section(lines, title, maximum):
    start = lines.index(title)
    end = start + 1
    while end < len(lines):
        line = lines[end]
        level = len(line) - len(line.lstrip('#'))
        if 0 < level <= maximum and line[level:level + 1] == ' ':
            break
        end += 1
    return lines[start:end]

out = '''# OT1999 chunk 3 — EARLY neutral readiness receipt

Status: READY for independent modeling of Weisgram, Hunt-Wesson, Baral, Rotella, Rice and Roe v. Flores-Ortega, subject to the record limits stated below. No current-matter outcomes, votes, authors or commitments are supplied. The approved brief and mechanical runtime remain unchanged.

Authorized read set: the mechanical neutral packet; frozen entering neutral state through February 14, 2000; EARLY entering-law slice; this receipt; EARLY_SOURCE_FACTS and EARLY_PREEXISTING_TEXT. The extra Lindh material below is copied verbatim from the authorized LATER slice solely to complete the applicable pre-AEDPA law. Source control alone read current-matter historical opinions and originals. This validator read only the sanitized products and did not open their raw source links.

The source-facts and preexisting-text companions were read in full. They contain objective chronology, attributed lower-court judgments, statutory/rule text and bounded source limits; no current Supreme Court disposition, reasoning, lineup or authorship was detected. Published recitations and affirmative original-record passages support the stated predicates. Located original files were not certified as fully read. No missing research document establishes litigant default or failure of proof.

The packet's obsolete June 23, 1999/no-same-term-decision placeholders are superseded by the frozen state through February 14, 2000. Smith v. Robbins and Weeks v. Angelone are effective January 19, 2000. Same-day uncoordinated events share entering law; later dependent events require an ordinary refresh. The nine-member OT1999 Court is seated at both milestones; no case-specific nonparticipation is identified.

## Precise current-law map
'''.splitlines()
start = validation.index('| Matter | Exact operative entry and present-operation date | Material boundary |')
out += [''] + validation[start:start + 2]
names = ['Weisgram', 'Hunt-Wesson', 'Baral', 'Rotella', 'Rice', 'Flores-Ortega']
out += [line for line in validation if any(line.startswith('| ' + name + ' |') for name in names)]
out += '''
Current-term Hill (January 11, 2000) concerns authorized scheduling, not appeal waiver. Rayphand/Torres (December 13, 1999) concerns a confined territorial constitutional accommodation, not a state ancestry franchise. Gutierrez (January 19, 2000) construes a statutory vote denominator. Steamfitters (January 10, 2000) supplies direct-causation boundaries, not a RICO accrual trigger.

## Validated neutral supplements and competing paths

Each path is an analytical possibility, not an unverified attribution to a party. Prior Justice names below identify published date-eligible sources; none predicts a present commitment.
'''.splitlines()
for title in ['### Weisgram v. Marley Co.', '### Hunt-Wesson, Inc. v. Franchise Tax Board', '### Baral v. United States', '### Rotella v. Wood', '### Rice v. Cayetano', '### Roe v. Flores-Ortega']:
    out += section(validation, title, 3)
out += '''
## Verbatim additional entering law

Source: [LATER law slice](../entering-law/OT_1999CHUNK3_LATER.md). Source authorities, not this copy, control.
'''.splitlines()
out += section(later, '## Standards and Tests selection: Temporal reach of ordinary AEDPA habeas amendments', 2)
out += section(later, '#### Lindh v. Murphy', 4)
out += '''
## Final readiness and source limits

All six matters have a bounded question, supported procedural posture, applicable entering law and at least two legal paths tested without a present commitment. No unresolved source question prevents modeling those bounded questions. An expanded ruling about a new proffer, exact refund, disputed counsel conversation, later RICO injury, independent tolling entitlement, tribal status or program validity would require its own supported record and permitted scope; those matters are not supplied by assumption. The existing record may support a legal standard and a bounded remand without invented factual findings.

Research cutoff: February 22, 2000 for Weisgram, Hunt-Wesson and Baral; February 23, 2000 for Rotella, Rice and Flores-Ortega. No later law enters.

Source companions: [EARLY source facts](OT_1999CHUNK3_EARLY_SOURCE_FACTS.md) and [EARLY preexisting text](OT_1999CHUNK3_EARLY_PREEXISTING_TEXT.md).
'''.splitlines()
(base / 'OT_1999CHUNK3_EARLY_NEUTRAL_READY.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('Created EARLY receipt with six neutral supplements and exact Lindh selections.')
