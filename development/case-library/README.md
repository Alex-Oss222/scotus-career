# Case library

A research aid for the simulated Court. It finds matters, keeps your Court's own Records apart from the historical sources they link to, and traces where each of your Court's decisions is mentioned later. It is not authority, and it is not part of Open, Run, Render or Close.

It reads the repository fresh on every run, so it is always current and nothing generated is stored. It reads only `terms/` and `state/`, never opens anything under `stone/`, and withholds links that point there. Python 3.10 or later, standard library only; it runs the same on Windows, macOS, Linux and Codex cloud.

## Use

From the repository root:

```sh
python development/case-library/tools/library.py find Casey
python development/case-library/tools/library.py find --term OT1995 --chunk 10
python development/case-library/tools/library.py show OT1991-121
python development/case-library/tools/library.py cited-by OT1991-121
python development/case-library/tools/library.py text "undue burden" --term OT1994
python development/case-library/tools/library.py citator --term OT1995 --md
python development/case-library/tools/library.py check
```

A matter is named by its term and case-list number: `OT1991-121` is No. 121 in the OT1991 case index. `find`, `show`, `cited-by` and `text` also take `--json` for research agents.

| Command | What it does |
|---|---|
| `find` | Matches case names, dockets, citations, area of law and event type; `--term` and `--chunk` narrow it. With no words it lists a term or chunk. |
| `show` | One matter: its Record, the chunk's brief, render input and render, its Holdings entries, then separately the historical sources the Record links to (outside sites) and the repository files it links to. |
| `cited-by` | Every later document that mentions the decision, with file, line and a snippet, in the groups described below. |
| `text` | Full-text search of the Records (`--scope all` adds renders and `state/`), with file and line. |
| `citator` | For each decision in a term, how many later documents mention it; `--md` prints a "Cited by" page. |
| `check` | Confirms every case-list row of a run term is tied to its Record. |

## How mentions are traced

Your Records mostly refer to the Court's own decisions by name ("simulated Casey", "the entered R.A.V. holding"), so the tracer looks for:

- **Full captions** such as "Shaw v. Reno" or "Stone v. INS". A caption of some other case, such as "West Virginia University Hospitals v. Casey", is set aside and never credited to your decision.
- **Citations** such as "505 U.S. 833" or "505 U.S., at 846", where the repository records the decision's citation (Holdings headings, workspace tables, Record headers).
- **Docket numbers** such as "A-766", and **links** to the decision's Record.
- **Short names** such as "Casey", "Casey's", "R.A.V.", "Adarand" or "Two Pesos": a person's surname or an organization's distinctive words. Justices' names, officials, places, ordinary words, and parties named in three or more captions (wardens, agencies) never count alone. A common surname such as "Shaw" counts only in a document that also names or cites the decision, or where it is called simulated or historical.

Each mention is tagged from the word just before it: **simulated** ("simulated", "entered", "actual", "effective", "current"), **historical** ("historical", "history") or **unmarked**. A document can only cite decisions dated before it, so mentions are grouped:

- **Mentioned in**: later documents that name your Court's decision.
- **Historical**: the name is expressly the historical opinion ("historical Casey language"), not your Court's decision.
- **Ambiguous**: the name also fits another of your decisions, a different case named in the same document, or the document's own case.
- **Bookkeeping only**: process notes such as "processed through ... after Benten v. Kessler".
- **Same-day**: documents decided the same day, which are not entering law for each other.
- **Before this decision existed**: an earlier document using the name (history or coincidence).

A document naming its own case does not count. These are mentions, not legal treatment: the tool never decides whether a later decision followed, limited or departed from an earlier one.

## Hand-kept names

`aliases.json` adjusts short names by matter. `add` makes a word or two-word name count even when the tool would not choose it; `remove` stops a name the tool chose:

```json
{"OT1991-88": {"add": ["Lujan"]}, "OT1994-55": {"add": ["Travelers"]}}
```

A name that also belongs to another of your decisions does not belong here: "Amtrak", for example, fits both National Railroad Passenger Corp. v. Boston & Maine and Lebron v. National Railroad Passenger Corp.

Known limits: a name shared with a case outside the simulation (a 1987 Fifth Circuit "Lopez", a defendant named Madsen) can still be credited when nothing in the document tells them apart, and a decision referred to only by a state's name ("Wyoming") is not traced. `show` lists a Record's outside links as historical sources and its links into this repository (including GitHub addresses of repository files) as repository files.

## Tests

```sh
python -m unittest discover -s development/case-library/tests
```

The tests build a small fixture repository; two further checks run against this repository's terms when they are present.
