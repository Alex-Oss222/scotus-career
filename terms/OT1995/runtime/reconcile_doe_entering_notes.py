"""Apply only reviewed, internal entering-law note corrections after Doe completion."""
from pathlib import Path
import re

BASE = Path(__file__).resolve().parents[1]
RECORDS = BASE / 'records'
NEW = RECORDS / 'Doe_v_Kirchner_review_dismissal_1996-06-21.md'
LINK = '[Doe completion addendum](../entering-law/OT_1995CHUNK9_DOE_COMPLETION_LAW_ADDENDUM.md)'

REPLACEMENTS = {
    'Baby_Richard_v_Kirchner_merits_1996-06-21.md': (
        'The separate Doe matter, Illinois No. 76063, is not adjudicated here and supplies no same-day precedent. No result, vote or final procedural event is attributed to that stopped matter.',
        'The separate Doe matter, Illinois No. 76063, is not adjudicated here and supplies no same-day entering precedent. Its separately completed June 21 threshold dismissal leaves the adoption judgment undisturbed and reaches no adult-custody merits. Both decisions retain the common pre-June21 baseline; this Record derives neither its jurisdiction nor its implementation holding from Doe.'),
    'United_States_v_Ursery_and_United_States_Currency_merits_1996-06-24.md': (
        'Gray and all four earlier-effective chunk 9 decisions are included; June 24 peers are excluded.',
        'Gray and the four chunk 9 decisions completed before this original reading are included in the preserved snapshot; June 24 peers are excluded. The subsequently completed Doe threshold dismissal is also effective June 21 and is accounted for by supplemental entering-law review. It creates no forfeiture, punishment, attachment or property rule and changes no ground of this decision. ' + LINK + ' preserves its exact public action and limits.'),
    'Lewis_v_United_States_merits_1996-06-24.md': (
        'No same-day peer supplies precedent, and the stopped Doe matter supplies none.',
        'No same-day peer supplies entering precedent. The preserved snapshot predates completion of Doe; supplemental entering-law review accounts for its June 21 threshold dismissal, which reaches no adult-custody merits and creates no jury, aggregation or cap rule material here. ' + LINK + ' preserves its exact public action and limits.'),
    'Gasperini_v_Center_for_Humanities_Inc_merits_1996-06-24.md': (
        'No June 24 peer supplies precedent through completion or file order; the stopped Doe matter supplies none.',
        'No June 24 peer supplies entering precedent through completion or file order. The preserved snapshot predates completion of Doe; supplemental entering-law review accounts for its June 21 threshold dismissal, which creates no Erie, compensation or reexamination rule material here. ' + LINK + ' preserves its exact public action and limits.'),
}

ADDITIONS = {
    'Lewis_v_Casey_merits_1996-06-24.md': (
        'The common PRE_19960624 projection and ACCESS_LAW slice govern.',
        'It creates no Article III or prison-access rule and decides no family-status merits.'),
    'Settle_v_Dickson_County_School_Board_merits_1996-06-25.md': (
        'The common PRE_19960625 neutral projection and JUNE25_SETTLE_LAW supply the entering baseline',
        'It decides no school-speech, causation, proof, qualified-immunity or remedial question material here.'),
    'Medtronic_Inc_v_Lohr_and_Lohr_v_Medtronic_Inc_merits_1996-06-26.md': (
        'Research and law cutoff: June 26, 1996',
        'It changes no federal-court review, preemption, actual-duty or agency-interpretation premise of these cross-petitions.'),
    'United_States_v_Virginia_and_Virginia_v_United_States_merits_1996-06-26.md': (
        'The material entering law is the coordinated OT1994 close',
        'It changes no jurisdiction, equal-protection, educational-opportunity or remedial premise of these federal cross-petitions.'),
}


def main():
    if not NEW.exists():
        raise SystemExit('Doe must be assembled and reviewed before notes are changed')
    if not (BASE / 'entering-law' / 'OT_1995CHUNK9_DOE_COMPLETION_LAW_ADDENDUM.md').exists():
        raise SystemExit('Create the exact public entering-law addendum first')
    targets = {}
    for filename in list(REPLACEMENTS) + list(ADDITIONS):
        path = RECORDS / filename
        original = path.read_text(encoding='utf-8')
        internal, public = original.split('## Public Projection', 1)
        if filename in REPLACEMENTS:
            old, new = REPLACEMENTS[filename]
            assert internal.count(old) == 1, filename
            internal = internal.replace(old, new, 1)
        else:
            start, explanation = ADDITIONS[filename]
            paragraphs = internal.split('\n\n')
            indexes = [i for i, p in enumerate(paragraphs) if p.startswith(start)]
            assert len(indexes) == 1, (filename, indexes)
            note = ('**Doe completion entering-law note:** The identified snapshot remains the preserved original reading set '
                    'and predates completion of Doe. Supplemental entering-law review accounts for its June 21 threshold '
                    'dismissal without importing its unresolved adult-right merits or another same-day peer. ' + explanation + ' ' + LINK +
                    ' supplies the exact public action and limits; the original snapshot and its recorded hash remain unchanged.')
            paragraphs.insert(indexes[0] + 1, note)
            internal = '\n\n'.join(paragraphs)
        changed = internal + '## Public Projection' + public
        for label in ['Case and dockets', 'Event and date', 'Result', 'Version / lineage']:
            pattern = rf'^\*\*{re.escape(label)}:\*\*.*$'
            assert re.search(pattern, original, re.M)[0] == re.search(pattern, changed, re.M)[0]
        assert changed.split('## Public Projection', 1)[1] == public
        targets[path] = changed
    # Validate every replacement before writing any of them.
    for path, text in targets.items():
        path.write_text(text, encoding='utf-8')
    print('Corrected only entering-law notes in eight existing Records; opening labels and Public Projections unchanged.')


if __name__ == '__main__':
    main()
