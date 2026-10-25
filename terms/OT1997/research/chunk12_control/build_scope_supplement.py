from pathlib import Path
import re

base = Path(__file__).resolve().parent
bragdon = (base / 'USREPORTS-524-624.txt').read_text(encoding='utf-8')
clinton = (base / 'USREPORTS-524-417.txt').read_text(encoding='utf-8')
chapter81 = (base / 'USCODE-1997-title28-chap81.txt').read_text(encoding='utf-8')
chapter133 = (base / 'USCODE-1997-title28-chap133.txt').read_text(encoding='utf-8')
rules = (base / 'Rules_1995.txt').read_text(encoding='utf-8')

def between(text, start, end, offset=0):
    i = text.index(start, offset)
    return text[i:text.index(end, i)]

grant = between(bragdon, '   The petition for certiorari presented three other questions', 'The\nquestion is phrased')
filing = between(clinton, 'In their com-', 'In light of the Government', 89000)
intent_start = clinton.index('that it desires', 89000)
intent_end = clinton.index('I would deem', intent_start)
government_request = clinton[intent_start:intent_end]

i1254 = chapter81.rindex('1254.') - 1
sec1254 = chapter81[i1254:chapter81.index('(June 25, 1948', i1254)].strip()
i2101 = chapter133.rindex('2101.')
sec2101e = between(chapter133, '(e) An application', '(f) In any case', i2101).strip()
i2103 = chapter133.rindex('2103.') - 2
sec2103 = chapter133[i2103:chapter133.index(chr(167) + '2104.', i2103)].strip()
rule11 = between(rules, 'Rule 11. Certiorari to a United States Court of Appeals', 'Rule 12. Review on Certiorari', 15000).strip()
rule18 = between(rules, '12. After considering the documents distributed under', '13. If the Clerk', 39000).strip()

out = '''# Neutral source supplement: Bragdon review scope and Clinton review channels

**Purpose and source status:** Objective procedural facts and date-eligible legal texts for independent neutral validation and affected modeling. This extraction contains no historical final judgment, vote, opinion coalition, model proposal or private position. The raw historical case texts remain control/reconciliation-only. The event cutoff is June 25, 1998. No new Supreme Court action or procedural compliance is assumed.

## Bragdon v. Abbott, No. 97-156: granted questions

Source: official report, 524 U.S. 624, 648, 654, https://www.govinfo.gov/content/pkg/USREPORTS-524/pdf/USREPORTS-524-624.pdf . Local source: `USREPORTS-524-624.txt`.

The reported grant included the federal disability issue. For the direct-threat branch, the report reproduces three proposed questions and states that only Question 3 was granted. The following passage is mechanically copied; question numbers are the petition's numbers, and the last sentence identifies grant scope only.

```text
'''+grant+'''
```

The report at page 654 states that Question 5, whether the petitioner raised a genuine issue for trial, was not granted, and describes the resulting briefs and arguments as not concentrated on whole-record sufficiency in light of every summary-judgment submission. This is a published characterization of the briefing's scope, not independent review of the original briefs. It does not establish that any exhibit was absent, that any party defaulted, that evidentiary sufficiency was resolved, or that no legal consequence can follow from the granted question. The original petition, briefing, and joint appendix were not separately recovered for this supplement.

## Clinton v. City of New York, No. 97-1374: existing filings

Source: official report, 524 U.S. 417, 425 n.9 and 455, https://www.govinfo.gov/content/pkg/USREPORTS-524/pdf/USREPORTS-524-417.pdf . Local source: `USREPORTS-524-417.txt`.

The complaints invoked both the special review provision and ordinary federal-question/declaratory-judgment bases. The Government filed a direct appeal and a protective court-of-appeals notice. The following is the factual filing account, mechanically copied without the source writing's proposed jurisdictional disposition:

```text
'''+filing+'''
```

The same page attributes to the Government a representation

```text
'''+government_request+'''
```

That excerpt supplies the attributed litigation request only. It does not establish that a separate certiorari petition was filed or granted, that all Rule 11 requirements were met, or that the direct appeal could proceed under the special statute. The original jurisdictional statement, complaints, protective notice and reply brief were not separately recovered. No circuit judgment is supplied. Any route selected must distinguish statutory authorization, the Court's discretionary action, and Article III standing for each consolidated action.

## Date-eligible jurisdiction and rule texts

The following texts were mechanically copied from official historical sources. The 1997 Code and the rules adopted July 26, 1995, effective October 2, 1995, are used; no later text supplies the rule. The saved full sources permit verification of surrounding qualifications.

### 28 U.S.C. 1254 (1997)

Source: https://www.govinfo.gov/content/pkg/USCODE-1997-title28/html/USCODE-1997-title28-partIV-chap81.htm ; local `USCODE-1997-title28-chap81.html` and `.txt`.

```text
'''+sec1254+'''
```

### 28 U.S.C. 2101(e) (1997)

Source: https://www.govinfo.gov/content/pkg/USCODE-1997-title28/html/USCODE-1997-title28-partV-chap133.htm ; local `USCODE-1997-title28-chap133.html` and `.txt`.

```text
'''+sec2101e+'''
```

### Section 2103: repeal entry in the 1997 Code

The former conversion provision is not operative in 1998; its repeal and transition are reproduced below rather than supplying the repealed rule as current authority.

```text
'''+sec2103+'''
```

### Supreme Court Rule 11 (1995 rules)

Source: https://www.supremecourt.gov/ctrules/rules/Rules_1995.pdf ; local `Rules_1995.pdf` and `Rules_1995.txt`. The official PDF title page supplies adoption/effective dates.

```text
'''+rule11+'''
```

### Supreme Court Rule 18.12 (1995 rules)

The direct-appeal rule separately addresses disposition and consideration of appellate jurisdiction:

```text
'''+rule18+'''
```

**Scope of this preparation:** These sources identify available legal channels and actual reported filings, not satisfaction of every channel or a new grant. Section 692's distinct special direct-review terms remain in the existing neutral packet. No proposed model vote, historical merits rationale or selected procedural outcome appears in this supplement. Neutral validation and affected modeling must precede any use to change a frozen commitment.
'''

target = base / 'FACTS_SCOPE_BRAGDON_CLINTON.md'
target.write_text(out, encoding='utf-8')
print(target, len(out.encode('utf-8')))
