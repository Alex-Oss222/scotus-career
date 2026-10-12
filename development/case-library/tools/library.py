#!/usr/bin/env python3
"""Case library: find matters, keep the Court's own Records apart from historical
sources, and trace where each of the Court's decisions is mentioned later.

Read-only. It reads the live repository on every run, so it is never stale and
nothing generated is stored. It reads only terms/ and state/, never opens anything
under stone/, and withholds text that points there. It is a research aid, not
authority; no Court stage uses it.

    python development/case-library/tools/library.py find Casey
    python development/case-library/tools/library.py show OT1991-121
    python development/case-library/tools/library.py cited-by OT1991-121
    python development/case-library/tools/library.py text "undue burden" --term OT1994
    python development/case-library/tools/library.py citator --term OT1995 --md
    python development/case-library/tools/library.py check

In Windows PowerShell, run [Console]::OutputEncoding = [Text.Encoding]::UTF8 before
piping or redirecting the output.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from bisect import bisect_left
from dataclasses import dataclass, field
from fnmatch import fnmatch
from functools import lru_cache
from pathlib import Path
from urllib.parse import unquote, urlsplit

TOOLS = Path(__file__).resolve().parent
ALIASES = TOOLS.parent / "aliases.json"

# Words that never identify a case on their own: government and institutional
# terms, places, ordinals, months and connectors.
GENERIC = set("""
a an the of for and in on at to by with re ex rel parte et al v vs de la le du von van der
united states america american national international federal state commonwealth people nation
city county town township village parish borough district municipal metropolitan regional
board department dept commission commissioner director secretary attorney general governor mayor
office agency authority administration bureau council committee court courts judge clerk sheriff
warden superintendent treasurer comptroller collector registrar justice justices chief president
congress senate house government counsel police officer officers prison prisons navy army air force
marine coast guard veterans affairs interior agriculture commerce treasury defense housing urban
development welfare human social security internal revenue customs immigration naturalization
environmental protection reserve trade securities exchange labor tribe nations capitol harbor square
school schools university college education educational
inc incorporated co cos company corp corporation ltd llc lp na plc partnership partners association
associates assn union local brotherhood workers employees laborers trust trustees fund plan estate
services service systems industries industrial group holdings enterprises products productions
bank insurance mutual life financial savings loan church society foundation center clinic hospital
medical health railroad railway transportation transit airlines lines communications television
broadcasting telephone telegraph network energy power electric gas oil water
north south east west northern southern eastern western new great central saint st paul louis
alabama alaska arizona arkansas california colorado connecticut delaware florida georgia hawaii
idaho illinois indiana iowa kansas kentucky louisiana maine maryland massachusetts michigan
minnesota mississippi missouri montana nebraska nevada hampshire jersey mexico york carolina dakota
ohio oklahoma oregon pennsylvania rhode island tennessee texas utah vermont virginia washington
wisconsin wyoming columbia puerto rico guam
boston chicago philadelphia detroit atlanta houston dallas miami denver seattle portland cleveland
baltimore pittsburgh cincinnati milwaukee minneapolis albuquerque phoenix angeles francisco diego
richmond hialeah buffalo newark memphis nashville orleans tampa omaha tulsa sacramento honolulu
january february march april may june july august september october november december
""".split())

# The Justices and the era's officials: their names never identify one case.
JUSTICES = set("white blackmun stevens oconnor scalia kennedy souter thomas ginsburg breyer rehnquist "
               "stone zsela marshall brennan powell burger".split())
OFFICIALS = set("""
reno barr thornburgh meese babbitt lujan shalala cisneros kemp pena glickman espy yeutter madigan
riley rubin bentsen brady aspin cheney christopher oleary watkins mosbacher kantor reich dole
skinner slater derwinski gober lyng clinton bush reagan sullivan bowen heckler
""".split())
# Common surnames and given names: they identify a case only where the same
# document also names that case in full, cites it, or calls it simulated or historical.
SURNAMES = set("""
smith johnson williams brown jones miller davis garcia rodriguez wilson martinez anderson taylor
moore jackson martin lee perez thompson harris sanchez clark ramirez lewis robinson walker young
allen king wright scott torres nguyen hill flores green adams nelson baker hall rivera campbell
mitchell carter roberts gomez phillips evans turner diaz parker cruz edwards collins reyes
stewart morris morales murphy cook rogers gutierrez ortiz morgan cooper peterson bailey reed kelly
howard ramos kim cox ward richardson watson brooks chavez wood james bennett gray mendoza ruiz
hughes price alvarez castillo sanders patel myers long ross foster jimenez jenkins perry
russell bell coleman butler henderson barnes gonzales fisher vasquez simmons romero
jordan patterson alexander hamilton graham reynolds griffin wallace west cole hayes bryant
herrera gibson ellis tran medina aguilar stephens murray ford castro owens harrison
fernandez mcdonald woods wells vargas henry chen freeman webb tucker guzman
burns crawford olson simpson porter hunter gordon mendez silva shaw snyder mason dixon munoz hunt
hicks holmes palmer wagner black robertson boyd rose salazar fox warren mills meyer rice
schmidt garza daniels ferguson nichols soto weaver ryan gardner payne grant dunn kelley
spencer hawkins arnold pierce vazquez hansen peters santos hart bradley knight elliott cunningham
duncan armstrong hudson carroll lane andrews alvarado ray delgado berry perkins hoffman
johnston matthews pena richards contreras willis carpenter lawrence sandoval
""".split())
# Given names and placeholder parties never identify a case on their own.
GIVEN = set("""
john james robert michael william david richard joseph charles mary patricia linda barbara paul
elizabeth jennifer susan margaret dorothy lisa nancy karen betty helen sandra donna carol george
doe roe baby minor child children
""".split())
COMMON = JUSTICES | OFFICIALS | SURNAMES | GIVEN
# U.S. Reports volumes for each term's decisions, to tell a same-named older case apart.
TERM_VOLUMES = {"OT1991": (502, 505), "OT1992": (506, 509), "OT1993": (510, 512), "OT1994": (513, 515),
                "OT1995": (516, 518), "OT1996": (519, 521)}
SUFFIXES = {"inc", "co", "cos", "corp", "ltd", "llc", "lp", "na", "plc"}
ORG = re.compile(r"\b(?:Inc|Co|Cos|Corp|Ltd|Company|Corporation|Association|Assn|Union|Council|Board|Church|"
                 r"Tribe|Bank|Trust|Fund|Society|Foundation|Center|Hospital|League|Party|Club|Coalition|"
                 r"Committee|Group|Products|Industries|Services|Systems)\b\.?")

# A qualifier directly before a name says which decision is meant. The Records
# write "actual", "effective" and "entered" for the Court's own decisions.
HISTORICAL = {"historical", "historically", "history"}
SIMULATED = {"simulated", "simulation", "entered", "actual", "effective", "operative", "received",
             "current", "present", "governing", "binding"}
# Process bookkeeping names matters without relying on them.
BOOKKEEPING = re.compile(r"processed through|chronology cursor|close cursor|comparator material|neutral-source search|"
                         r"merits-brief review|source-validation|full-read receipt|run log", re.I)

# A full caption: party A, "v.", and the whole of party B (masked together so no
# word inside another case's caption is read as a short name).
CAPTION = re.compile(r"([A-Z][\w'.&-]*(?:\s+(?:of|for|and|the|de|ex rel\.|&|[A-Z][\w'.&-]*))*"
                     r"(?:,?\s+(?:Inc|Co|Cos|Corp|Ltd|L\.P|N\.\s?A)\.?)?)\s+v\.\s*"
                     r"([A-Z0-9][\w'.&-]*(?:\s+(?:of|for|and|the|de|&|[A-Z0-9][\w'.&-]*))*"
                     r"(?:,?\s+(?:Inc|Co|Cos|Corp|Ltd|L\.P|N\.\s?A)\.?)?)")
AFTER_CAPTION = re.compile(r"^,?\s*(\d{1,4})\s+(U\.\s*S\.|F\.\s*(?:2d|3d)|F\.\s*Supp\.)\s*(\d{1,4})")
PAIR = re.compile(r"(?=\b([A-Z][A-Za-z'.-]*[A-Za-z]|[A-Z])\s([A-Z][A-Za-z0-9'.-]*[A-Za-z0-9]|[A-Z])\b)")
CAPWORD = re.compile(r"\b[A-Z]\.(?:\s?[A-Z]\.)+|\b[A-Z][A-Za-z'.-]*[A-Za-z]\b")
US_CITE = re.compile(r"\b(\d{3})\s+U\.\s*S\.\s*(\d{1,4})\b")
US_PIN = re.compile(r"\b(\d{3})\s+U\.\s*S\.,?\s*at\s+(\d{1,4})\b")
LOWER_CITE = re.compile(r"\b\d{1,4}\s+F\.\s*(?:2d|3d)\s+\d{1,4}\b|\b\d{1,4}\s+F\.\s*Supp\.(?:\s*2d)?\s+\d{1,4}\b")
CASE_LINE = re.compile(r"^\s*(?:[-*]\s*)?\*\*(?:Case|Case and dockets|Natural (?:event )?key)[^*]*:\*\*", re.I)
FILENAME = re.compile(r"[A-Za-z0-9_.'()-]+\.md")
MD_LINK = re.compile(r"\]\(\s*<?([^)\s>]+)>?\s*\)")
URL = re.compile(r"https?://[^\s<>)\]`\"]+")
GITHUB = re.compile(r"^https?://(?:(?:www\.)?github\.com/[^/]+/scotus-career/(?:blob|tree|raw)/[^/]+|"
                    r"raw\.githubusercontent\.com/[^/]+/scotus-career/[^/]+)/(.*)$", re.I)
STONE_PATH = re.compile(r"(?:\.\.[/\\])+stone(?:[/\\]\S*)?|(?<![\w-])stone[/\\][\w./\\#-]+")
CONNECTORS = {"v", "of", "the", "and", "in", "re", "ex", "rel", "et", "al", "for"}


def plain(text: str) -> str:
    """Normalize typography and drop Markdown emphasis for matching."""
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"[*_`]", "", text)


def fold(text: str) -> str:
    """Lowercase ASCII: accents dropped, so 'Peña' and 'Pena' agree."""
    return unicodedata.normalize("NFKD", plain(text)).encode("ascii", "ignore").decode().casefold()


@lru_cache(maxsize=None)
def tok(word: str) -> str:
    return re.sub(r"[^a-z0-9]", "", fold(re.sub(r"'s?$", "", plain(word))))


def norm(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", fold(text)))


def us_cites(text: str) -> set[str]:
    return {f"{v} U.S. {p}" for v, p in US_CITE.findall(text)}


def docket_ids(text: str) -> set[str]:
    """Docket, application and original-action numbers."""
    ids = {d.upper() for d in re.findall(r"\b(?:\d{2}-\d{1,5}|A-\d{1,5})\b", text)}
    ids |= {"ORIG" + n for n in re.findall(r"\b(\d{1,3}),?\s+Orig(?:inal)?\b", text, re.I)}
    return ids


def date_of(path: Path | str) -> str | None:
    m = re.search(r"(\d{4}-\d{2}-\d{2})\.md$", str(path))
    return m[1] if m else None


def is_stone(rel: str) -> bool:
    return any(part.casefold() == "stone" for part in unquote(rel).replace("\\", "/").split("/"))


def resolve(doc: str, target: str) -> str | None:
    """A Markdown link target as a repository path, or None for outside links."""
    m = GITHUB.match(target)
    if m:
        target = "/" + unquote(m[1])
    elif target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    target = unquote(target.split("#")[0])
    base = [] if target.startswith("/") else doc.split("/")[:-1]
    parts = list(base)
    for p in target.strip("/").split("/"):
        if p == "..":
            parts = parts[:-1]
        elif p not in ("", "."):
            parts.append(p)
    return "/".join(parts)


def stone_spans(text: str, doc: str = "") -> list[tuple[int, int]]:
    """Spans of links or paths into stone/, judged by path parts (so a Record named
    Stone_v_INS or the words "Stone/Breyer" are left alone)."""
    spans = []
    for m in MD_LINK.finditer(text):
        rel = resolve(doc, m[1]) if doc else None
        if is_stone(m[1]) or (rel and is_stone(rel)):
            spans.append(m.span())
    spans += [m.span() for m in URL.finditer(text) if is_stone(urlsplit(m[0]).path)]
    spans += [m.span() for m in STONE_PATH.finditer(text)]
    merged: list[tuple[int, int]] = []
    for s, e in sorted(spans):  # overlapping matches become one span
        if merged and s <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
        else:
            merged.append((s, e))
    return merged


def excerpt(text: str, start: int, end: int, doc: str = "") -> str:
    """A slice of a line with every stone/ link or path replaced; a span that
    crosses the slice's edge widens it, so no fragment of a path is shown."""
    spans = stone_spans(text, doc)
    for s, e in spans:
        if s < end and e > start:
            start, end = min(start, s), max(end, e)
    piece = text[start:end]
    for s, e in sorted({sp for sp in spans if sp[0] >= start and sp[1] <= end}, reverse=True):
        piece = piece[:s - start] + "[stone/ link withheld]" + piece[e - start:]
    return " ".join(piece.split())


def withhold(text: str, doc: str = "") -> str:
    return excerpt(text, 0, len(text), doc)


def typo(text: str) -> str:
    """Typography normalized, characters otherwise kept (for showing text)."""
    text = unicodedata.normalize("NFKC", text)
    return text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')


def strip_marks(text: str) -> tuple[str, list[int]]:
    """Drop Markdown emphasis for matching, keeping each kept character's original index."""
    kept = [(ch, i) for i, ch in enumerate(text) if ch not in "*_`"]
    return "".join(ch for ch, _ in kept), [i for _, i in kept] + [len(text)]


@dataclass
class Matter:
    key: str
    term: str
    no: int
    chunk: int
    caption: str
    dockets: str
    date: str
    event_type: str
    category: str
    area: str
    line: int
    sim: bool
    records: list[str] = field(default_factory=list)
    cites: set[str] = field(default_factory=set)
    below: set[str] = field(default_factory=set)
    parties: list[tuple[list[str], list[str], bool, bool]] = field(default_factory=list)
    party_sets: list[tuple[set[str], set[str]]] = field(default_factory=list)
    aliases: set[str] = field(default_factory=set)
    anchored: set[str] = field(default_factory=set)
    phrases: set[str] = field(default_factory=set)
    holdings: list[str] = field(default_factory=list)

    def summary(self) -> dict:
        return {"key": self.key, "term": self.term, "chunk": self.chunk, "date": self.date,
                "caption": self.caption + (" +" if self.sim else ""), "dockets": self.dockets,
                "event_type": self.event_type, "category": self.category, "area_of_law": self.area,
                "citations": sorted(self.cites), "judgment_below": sorted(self.below),
                "records": self.records, "holdings": self.holdings}


def split_parties(caption: str) -> list[tuple[list[str], list[str], bool, bool]]:
    """Each companion caption becomes (party A words, party B words, A is an organization, B is)."""
    out = []
    for part in re.split(r"\s+/\s+|;\s+", caption):
        part = re.sub(r"\([^)]*\)", " ", part)                # parenthetical descriptors
        part = re.sub(r",\s+(?:\d.*|[a-z].*)$", "", part)       # ", 507 U.S. 197", ", supplemental decree"
        part = re.sub(r"\bet al\.?", " ", part)
        sides = re.split(r"\s+v\.\s+", part, maxsplit=1)
        a_raw = re.sub(r"^In re\s+|^Ex parte\s+", "", sides[0].strip())
        b_raw = sides[1] if len(sides) > 1 else ""
        out.append((name_words(a_raw), name_words(b_raw), bool(ORG.search(a_raw)), bool(ORG.search(b_raw))))
    return out


def name_words(side: str) -> list[str]:
    """A party's name words: comma segments that are part of the name ("Planned
    Parenthood, Sioux Falls Clinic"), not descriptors or corporate suffixes."""
    keep = [s for s in re.split(r",\s+", side.strip().rstrip(","))
            if s[:1].isupper() and not re.fullmatch(r"(?:Inc|Co|Cos|Corp|Ltd|L\.P|N\.\s?A)\.?", s)]
    return " ".join(keep).split()


def clean_caption(text: str) -> str:
    """A caption without its trailing citation, lowercase descriptor or parenthetical."""
    text = re.sub(r",\s+(?:\d.*|[a-z].*)$", "", text.strip())
    return re.sub(r"\s*\([^)]*\)\s*$", "", text)


def party_tokens(words: list[str]) -> set[str]:
    """Every way a party can appear in a caption: words, hyphen parts, initials, acronym."""
    toks = {tok(w) for w in words} - {""}
    for w in words:
        if "-" in w:
            toks |= {tok(p) for p in w.split("-")} - {""}
    singles = [tok(w) for w in words if len(tok(w)) == 1]
    if len(singles) > 1:
        toks.add("".join(singles))
    caps = [w[0].lower() for w in words if w[:1].isupper()]
    if len(caps) > 1:
        toks.add("".join(caps))
    return toks


def party_alias(words: list[str], org: bool, allow: set[str] = frozenset()) -> str | None:
    """A party's usual short name: a person's surname, an organization's first distinctive word."""
    toks = [tok(w) for w in words if tok(w)]
    if len(toks) > 1 and all(len(t) == 1 for t in toks):  # initials such as R. A. V.
        return "".join(toks)
    blocked = GENERIC | (COMMON - allow)
    distinctive = [t for t in toks if t not in blocked and len(t) >= 3 and not t.isdigit()]
    if not distinctive:
        return None
    if org or len(toks) > 3 or any(t in GENERIC for t in toks):
        return distinctive[0]
    return toks[-1] if toks[-1] in distinctive else None


@dataclass
class Mention:
    path: str
    line: int
    how: str            # caption, citation, docket, link, or name: <word>
    tag: str            # simulated, historical, unmarked, same-day, before-decision
    ambiguous: list[str]
    snippet: str
    bookkeeping: bool = False

    @property
    def group(self) -> str:
        if self.tag in ("same-day", "before-decision", "historical"):
            return self.tag
        if self.ambiguous:
            return "ambiguous"
        return "bookkeeping" if self.bookkeeping else "mentions"


class Library:
    def __init__(self, root: Path):
        self.root = root.resolve()
        terms_dir = self.root / "terms"
        if not terms_dir.is_dir():
            raise SystemExit(f"No terms/ folder under {self.root}; pass --root with the repository root.")
        self.terms = sorted(p.name for p in terms_dir.iterdir()
                            if re.fullmatch(r"OT\d{4}", p.name) and self.safe(p) and (p / "case-list.md").is_file())
        self.matters: list[Matter] = []
        self.by_key: dict[str, Matter] = {}
        self.record_paths: dict[str, list[Path]] = {}
        self.record_owner: dict[str, list[str]] = {}
        self._text: dict[str, str] = {}
        self.unmatched_rows: list[Matter] = []
        self.conflicts: list[str] = []
        overrides = json.loads(ALIASES.read_text(encoding="utf-8")) if ALIASES.is_file() else {}
        self.overrides = {k: v for k, v in overrides.items() if not k.startswith("_")}
        for term in self.terms:
            self._load_term(term)
        self._load_holdings()
        self._build_indexes()

    # ---- reading -------------------------------------------------------
    def safe(self, path: Path) -> bool:
        """Never follow a link or junction, never leave the repository, never enter stone/."""
        try:
            rel = path.relative_to(self.root).as_posix()
        except ValueError:
            return False
        if is_stone(rel) or path.is_symlink():
            return False
        resolved = path.resolve()
        # Any link anywhere along the path shows up as a different resolved path.
        if os.path.normcase(str(resolved)) != os.path.normcase(str(path.absolute())):
            return False
        return resolved == self.root or self.root in resolved.parents

    def glob(self, folder: Path, pattern: str, recursive: bool = False) -> list[Path]:
        """Files under a folder, pruning stone/ and links before they are entered."""
        if not folder.is_dir() or not self.safe(folder):
            return []
        out = []
        for dirpath, dirnames, filenames in os.walk(folder, topdown=True, followlinks=False):
            dirnames[:] = sorted(d for d in dirnames if d.casefold() != "stone"
                                 and self.safe(Path(dirpath) / d))
            out += [Path(dirpath) / f for f in filenames if fnmatch(f, pattern) and self.safe(Path(dirpath) / f)]
            if not recursive:
                break
        return sorted(out, key=lambda p: p.as_posix())

    def rel(self, path: Path) -> str:
        return path.relative_to(self.root).as_posix()

    def read(self, rel: str) -> str:
        if is_stone(rel):
            raise ValueError("stone/ is never read")
        if rel not in self._text:
            self._text[rel] = (self.root / rel).read_text(encoding="utf-8", errors="replace")
        return self._text[rel]

    def _load_term(self, term: str):
        base = self.root / "terms" / term
        records = self.glob(base / "records", "*.md")
        self.record_paths[term] = records
        names = {p.name: p for p in records}
        rows = []
        for i, line in enumerate(self.read(f"terms/{term}/case-list.md").splitlines(), 1):
            m = re.match(r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|(.*)\|\s*$", line)
            if not m:
                continue
            cells = [c.strip() for c in m[3].split("|")]
            if len(cells) not in (5, 6) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", cells[2]):
                continue
            caption, sim = cells[0], cells[0].endswith(" +")
            caption = caption[:-2].rstrip() if sim else caption
            matter = Matter(f"{term}-{m[1]}", term, int(m[1]), int(m[2]), caption, cells[1], cells[2], cells[3],
                            cells[4], cells[5] if len(cells) == 6 else "", i, sim)
            matter.parties = split_parties(caption)
            rows.append(matter)
        # Explicit links: the workspace manifest names each row's Record file.
        explicit: dict[tuple[str, str], list[str]] = {}
        cites: dict[tuple[str, str], set[str]] = {}
        for ws in (base / "workspace" / "manifest.md", base / "workspace.md"):
            if not ws.is_file() or not self.safe(ws):
                continue
            for line in self.read(self.rel(ws)).splitlines():
                if not line.startswith("|"):
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                dates = [c for c in cells if re.fullmatch(r"\d{4}-\d{2}-\d{2}", c)]
                if not dates or len(cells) < 3:
                    continue
                files = [f for f in FILENAME.findall(line) if f in names]
                for cell in cells:
                    if " v. " in cell or cell.startswith("In re"):
                        k = (dates[0], norm(clean_caption(cell)))
                        if files:
                            explicit.setdefault(k, []).extend(files)
                        cites.setdefault(k, set()).update(us_cites(line))
                        cites[k].update(LOWER_CITE.findall(line))
        claimed: dict[str, str] = {}
        for matter in rows:
            k = (matter.date, norm(clean_caption(matter.caption)))
            files = sorted(set(explicit.get(k, [])))
            if not files:
                files = self._match(matter, records)
            for f in files:
                if f in claimed and claimed[f] != matter.key:
                    self.conflicts.append(f"{f} claimed by {claimed[f]} and {matter.key}")
                claimed[f] = matter.key
            matter.records = [f"terms/{term}/records/{f}" for f in files]
            for f in matter.records:
                self.record_owner.setdefault(f, []).append(matter.key)
            for kk, cs in cites.items():
                if kk[0] == matter.date and kk[1] == k[1]:
                    matter.cites |= {c for c in cs if "U.S." in c}
                    if matter.sim:
                        matter.below |= {c for c in cs if "U.S." not in c}
            for f in matter.records:
                for line in self.read(f).splitlines()[:30]:
                    if CASE_LINE.match(line):
                        matter.cites |= us_cites(line)
                        if matter.sim:
                            matter.below |= set(LOWER_CITE.findall(line))
            if not matter.records and records:  # a term not yet run has no Records
                self.unmatched_rows.append(matter)
            self.matters.append(matter)
            self.by_key[matter.key] = matter

    def _match(self, matter: Matter, records: list[Path]) -> list[str]:
        """Same-date Record whose opening names the caption or carries its docket."""
        wanted = docket_ids(matter.dockets)
        words = {tok(w) for a, b, _, _ in matter.parties for w in a + b} - CONNECTORS - {""}
        scored = []
        for path in records:
            if date_of(path) != matter.date:
                continue
            opening = self.read(self.rel(path))[:1500]
            have = docket_ids(opening)
            hay = set(norm(path.stem.replace("_", " ").replace("-", " ") + " " + opening[:400]).split())
            named = docket_ids(path.stem.replace("_", " "))
            score = 5 * len(wanted & named) + 3 * len(wanted & have) + len(words & hay)
            if score:
                scored.append((score, bool(wanted & have), path.name))
        if not scored:
            return []
        best = max(s for s, _, _ in scored)
        top = [name for s, _, name in scored if s == best]
        if len(top) > 1:  # several Records for one row only when each carries the row's docket
            top = [name for s, d, name in scored if s == best and d] or top[:1]
        return top

    def _load_holdings(self):
        index: dict[str, list[tuple[str, set[str]]]] = {}
        self.holding_heads: dict[str, list[tuple[int, int]]] = {}
        for path in self.glob(self.root / "state" / "holdings", "*.md"):
            rel = self.rel(path)
            for i, line in enumerate(self.read(rel).splitlines(), 1):
                m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
                if not m:
                    continue
                self.holding_heads.setdefault(rel, []).append((i, len(m[1])))
                if " v. " not in m[2] and not m[2].startswith("In re"):
                    continue
                name = re.split(r",\s+\d{3}\s+U\.", m[2])[0]
                year = re.search(r"\((\d{4})\)", m[2])
                index.setdefault(norm(name), []).append((f"{rel}:{i}", us_cites(m[2]), year[1] if year else None))

        def names_of(matter):
            return ({norm(clean_caption(matter.caption))}
                    | {norm(" ".join(a) + " v. " + " ".join(b)) for a, b, _, _ in matter.parties if b})

        sharing: dict[str, list[Matter]] = {}
        for matter in self.matters:
            for n in names_of(matter):
                sharing.setdefault(n, []).append(matter)
        for matter in self.matters:
            for n in names_of(matter):
                for loc, cs, year in index.get(n, []):
                    if len(sharing[n]) > 1:  # same caption, different events: the heading must say which
                        fits = (cs & matter.cites) if (cs and matter.cites) else (year == matter.date[:4] if year else False)
                        if not fits:
                            continue
                    matter.holdings.append(loc)
                    matter.cites |= cs
            matter.holdings = sorted(set(matter.holdings))

    def _build_indexes(self):
        self._alias_index: dict[str, list[Matter]] | None = None
        self.dropped_aliases: list[str] = []
        self.b_index: dict[str, list[Matter]] = {}
        self.volume_index: dict[str, list[tuple[int, Matter]]] = {}
        self.docket_index: dict[str, list[Matter]] = {}
        self.phrase_index: dict[str, list[Matter]] = {}
        for matter in self.matters:
            for a, b, a_org, b_org in matter.parties:
                for side, org in ((a, a_org), (b, b_org)):
                    alias = party_alias(side, org)
                    if alias:
                        matter.aliases.add(alias)
                    anchored = None if org else party_alias(side, org, allow=SURNAMES)
                    if anchored and anchored != alias and anchored not in GIVEN:
                        matter.anchored.add(anchored)
                    if len(side) >= 2 and side[1].lower() not in CONNECTORS and side[0][:1].isupper() and side[1][:1].isupper():
                        first_two = [tok(w) for w in side[:2]]
                        if not all(t in GENERIC | COMMON for t in first_two):
                            matter.phrases.add(" ".join(first_two))
            rule = self.overrides.get(matter.key, {})
            for word in rule.get("add", []):
                (matter.phrases if " " in word.strip() else matter.aliases).add(
                    " ".join(tok(w) for w in word.split()) if " " in word.strip() else tok(word))
            removed = {tok(x) for x in rule.get("remove", [])}
            matter.aliases -= removed
            matter.anchored -= removed
            matter.party_sets = [(party_tokens(a), party_tokens(b)) for a, b, _, _ in matter.parties]
            for _, b_set in matter.party_sets:
                for t in b_set:
                    self.b_index.setdefault(t, []).append(matter)
            for cite in matter.cites:
                m = re.match(r"(\d{3}) U\.S\. (\d+)", cite)
                if m:
                    self.volume_index.setdefault(m[1], []).append((int(m[2]), matter))
            for d in docket_ids(matter.dockets):
                self.docket_index.setdefault(d, []).append(matter)
            for p in matter.phrases:
                self.phrase_index.setdefault(p, []).append(matter)

    def alias_index(self) -> dict[str, list[Matter]]:
        """Short names that stand for a decision. A party word the Records often use
        as an ordinary lowercase word ("planned", "reliance") is not a name, and a
        party named in three or more captions (a warden, an agency) is not either."""
        if self._alias_index is not None:
            return self._alias_index
        words = {a for m in self.matters for a in m.aliases | m.anchored}
        lower: dict[str, int] = {}
        upper: dict[str, int] = {}
        for term in self.terms:
            for path in self.record_paths[term]:
                for w in re.findall(r"[A-Za-z][A-Za-z'.-]*", plain(self.read(self.rel(path)))):
                    k = tok(w)
                    if k in words:
                        counts = lower if w[0].islower() else upper
                        counts[k] = counts.get(k, 0) + 1
        forced = {tok(x) for rule in self.overrides.values() for x in rule.get("add", []) if " " not in x.strip()}
        share: dict[str, int] = {}
        for m in self.matters:
            for w in m.aliases | m.anchored:
                share[w] = share.get(w, 0) + 1
        ok = {w for w in words if w in forced or (lower.get(w, 0) <= max(2, 0.2 * upper.get(w, 0)) and share[w] < 3)}
        self.dropped_aliases = sorted(words - ok)
        self._alias_index = {}
        for m in self.matters:
            m.anchored &= ok
            for a in sorted(m.aliases & ok):
                self._alias_index.setdefault(a, []).append(m)
            for a in sorted(m.anchored):
                self._alias_index.setdefault(a, []).append(m)
        return self._alias_index

    # ---- finding -------------------------------------------------------
    def find(self, query: str, term: str | None = None, chunk: int | None = None) -> list[Matter]:
        q = norm(query)
        out = []
        for m in self.matters:
            if term and m.term != term or chunk and m.chunk != chunk:
                continue
            hay = norm(" ".join([m.key, m.caption, m.dockets, m.area, m.event_type, " ".join(m.cites),
                                 " ".join(Path(r).stem.replace("_", " ") for r in m.records)]))
            if not q or f" {q} " in f" {hay} " or m.key.casefold() == query.strip().casefold():
                out.append(m)
        return out

    def resolve(self, query: str) -> list[Matter]:
        query = query.strip()
        if query.upper() in self.by_key:
            return [self.by_key[query.upper()]]
        found = self.find(query)
        exact = [m for m in found if norm(m.caption) == norm(query)]
        return exact or found

    # ---- tracing -------------------------------------------------------
    def corpus(self, scope: str, term: str | None = None) -> list[tuple[str, str | None]]:
        """(path, date) of documents to scan. Records always; renders and state/ on request."""
        docs = []
        for t in self.terms:
            if term and t != term:
                continue
            docs += [(self.rel(p), date_of(p)) for p in self.record_paths[t]]
            if scope == "all":
                for p in self.glob(self.root / "terms" / t / "output", "*.md"):
                    m = re.search(r"CHUNK(\d+)\.md$", p.name)
                    dates = [x.date for x in self.matters if x.term == t and m and x.chunk == int(m[1])]
                    docs.append((self.rel(p), max(dates) if dates else None))
        if scope == "all" and not term:
            docs += [(self.rel(p), None) for p in self.glob(self.root / "state", "*.md", recursive=True)]
        return docs

    def _own(self, path: str) -> tuple[set[str], dict[int, set[str]]]:
        """Matters a document is itself about, for the whole document or by line."""
        own = set(self.record_owner.get(path, []))
        m = re.match(r"terms/(OT\d{4})/output/OT_\d{4}CHUNK(\d+)\.md$", path)
        if m:
            own |= {x.key for x in self.matters if x.term == m[1] and x.chunk == int(m[2])}
        by_line: dict[int, set[str]] = {}
        heads = self.holding_heads.get(path)
        if heads:
            owners: dict[int, set[str]] = {}
            for x in self.matters:
                for loc in x.holdings:
                    f, _, ln = loc.rpartition(":")
                    if f == path:
                        owners.setdefault(int(ln), set()).add(x.key)
            for start, level in heads:
                if start in owners:
                    last = len(self.read(path).splitlines()) + 1
                    end = next((ln for ln, lv in heads if ln > start and lv <= level), last)
                    for ln in range(start, end):
                        by_line.setdefault(ln, set()).update(owners[start])
        return own, by_line

    def mentions(self, path: str, doc_date: str | None) -> dict[str, list[Mention]]:
        """Every mention of the Court's decisions in one document, keyed by matter."""
        found: dict[str, list[Mention]] = {}
        seen: set[tuple[str, int]] = set()
        own_doc, own_line = self._own(path)
        aliases = self.alias_index()
        shown_lines = [typo(raw) for raw in self.read(path).splitlines()]
        stripped = [strip_marks(t) for t in shown_lines]
        lines = [s for s, _ in stripped]
        qualifier_words = HISTORICAL | SIMULATED

        def qualifier(line: str, start: int) -> str:
            before = re.split(r"[;:.|(\[]", line[:start])[-1]
            for word in reversed(re.findall(r"[A-Za-z-]+", before)[-2:]):
                if word.lower() in HISTORICAL:
                    return "historical"
                if word.lower() in SIMULATED:
                    return "simulated"
            return "unmarked"

        def add(cands: list[Matter], line_no: int, start: int, how: str, line: str, other: str | None = None):
            cands = [c for c in {c.key: c for c in cands}.values() if c.records]  # only decided matters
            own = own_doc | own_line.get(line_no, set())
            note = []
            if any(c.key in own for c in cands):
                cands = [c for c in cands if c.key not in own]
                note = ["this document's own case"]
            if not cands:
                return
            in_world = [c for c in cands if doc_date is None or c.date <= doc_date]
            chosen = in_world or cands
            tag = qualifier(line, start)
            index_map = stripped[line_no - 1][1]
            low, high = index_map[max(0, start - 90)], index_map[min(len(index_map) - 1, start + 110)]
            snippet = excerpt(shown_lines[line_no - 1], low, high, path)
            amb = [c.key for c in chosen] if len(chosen) > 1 else []
            for c in chosen:
                if (c.key, line_no) in seen:
                    continue
                seen.add((c.key, line_no))
                when = tag
                if doc_date is not None and c.date > doc_date:
                    when = "before-decision"
                elif doc_date is not None and c.date == doc_date:
                    when = "same-day"
                also = [a for a in amb if a != c.key] + note + ([f"{other} (named in this document)"] if other else [])
                found.setdefault(c.key, []).append(
                    Mention(path, line_no, how, when, also, snippet, bool(BOOKKEEPING.search(line))))

        def caption_hits(m, line: str) -> list[Matter]:
            words = [w for w in m[1].split() if tok(w) not in SUFFIXES and tok(w)]
            b_words = m[2].split()
            if not words or not b_words:
                return []
            x_last, y_first = tok(words[-1]), tok(b_words[0])
            hits = [c for c in self.b_index.get(y_first, [])
                    if any(x_last in a and y_first in b for a, b in c.party_sets)]
            after = AFTER_CAPTION.match(line[m.end():m.end() + 40])
            if after and hits:  # a reporter citation right after the caption must fit this decision
                volume, reporter, page = int(after[1]), " ".join(after[2].split()), after[3]
                keep = []
                for c in hits:
                    if reporter.startswith("U."):
                        if c.cites:
                            ok = f"{volume} U.S. {page}" in c.cites
                        else:
                            first, last = TERM_VOLUMES.get(c.term, (0, 10 ** 6))
                            ok = first <= volume <= last
                    else:  # a lower-court report: only a sim-granted case is known by its judgment below
                        ok = c.sim and (not c.below or any(x.startswith(f"{volume} ") and x.endswith(f" {page}")
                                                           for x in c.below))
                    if ok:
                        keep.append(c)
                hits = keep
            return hits

        # A different case named in full here ("Hancock v. Train") makes a bare
        # "Hancock" in this document ambiguous rather than the Court's decision.
        shadow: dict[str, str] = {}
        strong: set[str] = set()
        masked_lines = []
        for line_no, line in enumerate(lines, 1):
            masked = list(line)
            for m in CAPTION.finditer(line):
                hits = caption_hits(m, line)
                if hits:
                    # "Entered Shaw v. Reno": a leading qualifier is not part of the caption.
                    lead = re.match(r"(?:(?:" + "|".join(sorted(qualifier_words)) + r")\s+)+", m[1], re.I)
                    add(hits, line_no, m.start() + (lead.end() if lead else 0), "caption", line)
                    strong.update(c.key for c in hits)
                else:
                    name = " ".join(m[0].split()[-6:])
                    for w in (m[1].split()[-1], m[2].split()[0]):
                        shadow.setdefault(tok(w), name)
                masked[m.start():m.end()] = " " * (m.end() - m.start())
            for m in US_CITE.finditer(line):
                hits = [c for c in self.matters if f"{m[1]} U.S. {m[2]}" in c.cites]
                if hits:
                    add(hits, line_no, m.start(), "citation", line)
                    strong.update(c.key for c in hits)
                masked[m.start():m.end()] = " " * (m.end() - m.start())
            for m in US_PIN.finditer(line):
                page = int(m[2])
                cands = [(first, c) for first, c in self.volume_index.get(m[1], []) if first <= page <= first + 150]
                if cands:
                    best = max(f for f, _ in cands)
                    hits = [c for f, c in cands if f == best]
                    add(hits, line_no, m.start(), "citation", line)
                    strong.update(c.key for c in hits)
                masked[m.start():m.end()] = " " * (m.end() - m.start())
            for m in re.finditer(r"\b(?:\d{2}-\d{1,5}|A-\d{1,5})\b|\b\d{1,3},?\s+Orig(?:inal)?\b", line):
                hits = [c for d in docket_ids(m[0]) for c in self.docket_index.get(d, [])]
                if hits:
                    add(hits, line_no, m.start(), "docket", line)
                    strong.update(c.key for c in hits)
            index_map = stripped[line_no - 1][1]
            for m in MD_LINK.finditer(shown_lines[line_no - 1]):
                rel = resolve(path, m[1])
                if rel and rel in self.record_owner:
                    hits = [self.by_key[k] for k in self.record_owner[rel]]
                    add(hits, line_no, bisect_left(index_map, m.start()), "link", line)
                    strong.update(c.key for c in hits)
            masked_lines.append("".join(masked))

        for line_no, rest in enumerate(masked_lines, 1):
            line = lines[line_no - 1]
            # Two-word names ("Two Pesos", "Brown Group", "Baby K"): look up each pair
            # of adjacent capitalized words.
            for m in PAIR.finditer(rest):
                hits = self.phrase_index.get(f"{tok(m[1])} {tok(m[2])}")
                if hits:
                    add(hits, line_no, m.start(), f"name: {m[1]} {m[2]}", line)
                    end = m.start() + len(m[1]) + 1 + len(m[2])
                    rest = rest[:m.start()] + " " * (end - m.start()) + rest[end:]
            for m in CAPWORD.finditer(rest):
                t = tok(m[0])
                hits = aliases.get(t)
                if not hits:
                    continue
                # A common surname counts only where this document names or cites the
                # decision, or calls it simulated, entered, actual or effective.
                usable = [c for c in hits if t in c.aliases
                          or c.key in strong or qualifier(line, m.start()) == "simulated"]
                if usable:
                    add(usable, line_no, m.start(), f"name: {m[0]}", line, shadow.get(t))
        return found

    def cited_by(self, matter: Matter, scope: str) -> list[Mention]:
        out = []
        for path, date in self.corpus(scope):
            out += self.mentions(path, date).get(matter.key, [])
        return out

    def text(self, query: str, scope: str, term: str | None = None) -> list[tuple[str, int, str]]:
        words = norm(query).split()
        if not words:
            return []
        pattern = re.compile(r"\b" + r"\W+".join(re.escape(w) for w in words) + r"\b")
        out = []
        for path, _ in self.corpus(scope, term):
            for i, line in enumerate(self.read(path).splitlines(), 1):
                shown = withhold(line, path)
                if pattern.search(fold(shown)):
                    out.append((path, i, " ".join(shown.split())[:220]))
        return out

    def links(self, matter: Matter) -> tuple[dict[str, list[str]], list[str], int]:
        """Outside (historical) links by site, repository links, and stone/ links withheld."""
        outside: dict[str, list[str]] = {}
        inside, withheld = [], 0
        for rec in matter.records:
            text = self.read(rec)
            targets = MD_LINK.findall(text) + [u.rstrip(".,;:") for u in URL.findall(text)]
            for target in dict.fromkeys(targets):
                rel = resolve(rec, target)
                if rel is None:
                    if target.startswith(("http://", "https://")):
                        if is_stone(urlsplit(target).path):
                            withheld += 1
                        else:
                            outside.setdefault(urlsplit(target).hostname or "?", []).append(target)
                elif is_stone(rel) or is_stone(target):
                    withheld += 1
                else:
                    inside.append(rel)
        return {k: sorted(set(v)) for k, v in sorted(outside.items())}, sorted(set(inside)), withheld


# ---- command line ------------------------------------------------------------

def one(lib: Library, query: str) -> Matter:
    found = lib.resolve(query)
    if len(found) == 1:
        return found[0]
    if not found:
        raise SystemExit(f"No matter matches {query!r}. Try: find {query}")
    lines = "\n".join(f"  {m.key:12} {m.date}  {m.caption}" for m in found[:30])
    raise SystemExit(f"{len(found)} matters match {query!r}; name one by its key:\n{lines}")


def print_matter(m: Matter):
    print(f"{m.key:12} chunk {m.chunk:<3} {m.date}  {m.caption}{' +' if m.sim else ''}  [{m.dockets}]")
    for r in m.records:
        print(f"{'':14}Record: {r}")


def cmd_find(lib, args):
    found = lib.find(args.query, args.term, args.chunk)
    if args.json:
        return print(json.dumps([m.summary() for m in found], ensure_ascii=False, indent=2))
    for m in found:
        print_matter(m)
    print(f"{len(found)} matter(s)")


def cmd_show(lib, args):
    m = one(lib, args.case)
    outside, inside, withheld = lib.links(m)
    term_dir = f"terms/{m.term}"
    chunk_file = f"OT_{m.term[2:]}CHUNK{m.chunk}.md"
    files = {kind: f"{term_dir}/{kind}/{chunk_file}" for kind in ("briefs", "render-inputs", "output")}
    if args.json:
        data = m.summary() | {"chunk_files": {k: v for k, v in files.items() if (lib.root / v).is_file()},
                              "outside_links": outside, "repository_links": inside, "stone_links_withheld": withheld}
        return print(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"{m.key} | {m.caption}{' +' if m.sim else ''}")
    print(f"  Chunk {m.chunk} | {m.date} | {m.event_type} | {m.category}")
    print(f"  Area of law: {m.area}")
    print(f"  Dockets: {m.dockets}" + (f" | Citation: {', '.join(sorted(m.cites))}" if m.cites else "")
          + (f" | Judgment below: {', '.join(sorted(m.below))}" if m.below else ""))
    print("\nYour Court's own record")
    for r in m.records:
        print(f"  Record: {r}")
    names = {"briefs": "Brief", "render-inputs": "Render input", "output": "Render"}
    for kind, path in files.items():
        if (lib.root / path).is_file():
            print(f"  {names[kind]} (whole chunk): {path}")
    for h in m.holdings:
        print(f"  Holdings: {h}")
    print("\nHistorical sources linked from the Record (outside the simulation; not your Court's law)")
    if not outside:
        print("  none")
    for host, urls in outside.items():
        print(f"  {host}: {len(urls)}")
        for u in urls[:args.limit]:
            print(f"    {u}")
        if len(urls) > args.limit:
            print(f"    (first {args.limit} shown)")
    print(f"\nRepository files linked from the Record: {len(inside)}" + (f" (links into stone/ withheld: {withheld})" if withheld else ""))
    for p in inside[:args.limit]:
        print(f"  {p}")
    if len(inside) > args.limit:
        print(f"  (first {args.limit} shown)")


GROUPS = {"mentions": "Mentioned in",
          "ambiguous": "Ambiguous: the name also fits another decision or a different case in",
          "bookkeeping": "Named only in process bookkeeping in",
          "same-day": "Same-day documents (not entering law for each other):",
          "historical": "Named as the historical opinion (not your Court's decision) in",
          "before-decision": "Name appears before this decision existed (history or coincidence) in"}


def cmd_cited_by(lib, args):
    m = one(lib, args.case)
    hits = lib.cited_by(m, args.scope)
    groups = {g: [h for h in hits if h.group == g] for g in GROUPS}
    if args.json:
        return print(json.dumps({"matter": m.summary(), **{g: [h.__dict__ for h in v] for g, v in groups.items()}},
                                ensure_ascii=False, indent=2))
    names = sorted((m.aliases | m.anchored) & set(lib.alias_index()))
    print(f"{m.caption} ({m.key}, decided {m.date}) | names: {', '.join(names) or 'full caption only'}"
          + (f" | citation {', '.join(sorted(m.cites))}" if m.cites else ""))
    for group, items in groups.items():
        by_doc: dict[str, list[Mention]] = {}
        for h in items:
            by_doc.setdefault(h.path, []).append(h)
        if not by_doc and group != "mentions":
            continue
        title = GROUPS[group]
        print(f"\n{title}{'' if title.endswith(':') else ''} {len(by_doc)} document(s)")
        for path, hs in by_doc.items():
            tags = sorted({h.tag for h in hs})
            print(f"  {path}  ({len(hs)} mention(s); {', '.join(tags)})")
            for h in hs[:args.lines]:
                extra = f" also: {', '.join(h.ambiguous)}" if h.ambiguous else ""
                print(f"    line {h.line} [{h.tag}, {h.how}]{extra}: {h.snippet}")


def cmd_text(lib, args):
    hits = lib.text(args.query, args.scope, args.term)
    if args.json:
        return print(json.dumps([{"path": p, "line": i, "text": t} for p, i, t in hits], ensure_ascii=False, indent=2))
    for p, i, t in hits[:args.limit]:
        print(f"{p}:{i}: {t}")
    print(f"{len(hits)} line(s)" + (f"; first {args.limit} shown" if len(hits) > args.limit else ""))


def cmd_citator(lib, args):
    targets = [m for m in lib.matters if m.term == args.term and m.records]
    tally = {m.key: {g: set() for g in GROUPS} for m in targets}
    for path, date in lib.corpus(args.scope):
        for key, hs in lib.mentions(path, date).items():
            if key in tally:
                for h in hs:
                    tally[key][h.group].add(path)
    cols = ("mentions", "ambiguous", "bookkeeping")
    if args.md:
        print(f"# {args.term} cited by\n\nLater documents that mention each {args.term} decision by caption, citation, docket, "
              "link or name. Generated by `development/case-library/tools/library.py citator`; a research aid, not authority.\n")
        print("| No. | Decision | Decided | Mentioned in | Ambiguous | Bookkeeping only |\n|---:|---|---|---:|---:|---:|")
        for m in targets:
            t = tally[m.key]
            print(f"| {m.no} | {m.caption}{' +' if m.sim else ''} | {m.date} | " + " | ".join(str(len(t[c])) for c in cols) + " |")
        return
    for m in targets:
        t = tally[m.key]
        print(f"{m.key:12} {m.date}  mentioned {len(t['mentions']):>3}  ambiguous {len(t['ambiguous']):>3}  "
              f"bookkeeping {len(t['bookkeeping']):>3}  {m.caption}")


def cmd_check(lib, args):
    print(f"Terms: {', '.join(lib.terms)}")
    bad = 0
    for term in lib.terms:
        ms = [m for m in lib.matters if m.term == term]
        if not lib.record_paths[term]:
            print(f"{term}: {len(ms)} matters; no Records yet (term not run)")
            continue
        linked = {r for m in ms for r in m.records}
        others = [p.name for p in lib.record_paths[term] if lib.rel(p) not in linked]
        print(f"{term}: {len(ms)} matters, {sum(bool(m.records) for m in ms)} with Records, "
              f"{len(lib.record_paths[term])} Records ({len(others)} not tied to a case-list row), "
              f"{sum(bool(m.cites) for m in ms)} with a known citation")
        if args.verbose:
            for name in others:
                print(f"    other Record: {name}")
    for m in lib.unmatched_rows:
        bad += 1
        print(f"  no Record found: {m.key} {m.date} {m.caption}")
    for c in lib.conflicts:
        bad += 1
        print(f"  conflict: {c}")
    for k in lib.overrides:
        if k not in lib.by_key:
            bad += 1
            print(f"  aliases.json names an unknown matter: {k}")
    print("OK" if not bad else f"{bad} problem(s)")
    return 1 if bad else 0


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure") and not os.environ.get("PYTHONIOENCODING"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", type=Path, default=TOOLS.parents[2], help="repository root")
    sub = ap.add_subparsers(dest="command", required=True)
    p = sub.add_parser("find", help="find matters by name, docket, citation, area of law, term or chunk")
    p.add_argument("query", nargs="?", default="")
    p.add_argument("--term"); p.add_argument("--chunk", type=int); p.add_argument("--json", action="store_true")
    p = sub.add_parser("show", help="one matter: your Court's record, its files, and the historical sources it links")
    p.add_argument("case"); p.add_argument("--limit", type=int, default=8); p.add_argument("--json", action="store_true")
    p = sub.add_parser("cited-by", help="every later mention of one of your Court's decisions")
    p.add_argument("case"); p.add_argument("--scope", choices=("records", "all"), default="records")
    p.add_argument("--lines", type=int, default=2); p.add_argument("--json", action="store_true")
    p = sub.add_parser("text", help="full-text search with file and line")
    p.add_argument("query"); p.add_argument("--term"); p.add_argument("--scope", choices=("records", "all"), default="records")
    p.add_argument("--limit", type=int, default=60); p.add_argument("--json", action="store_true")
    p = sub.add_parser("citator", help="for each decision in a term, how many documents mention it")
    p.add_argument("--term", required=True); p.add_argument("--scope", choices=("records", "all"), default="records")
    p.add_argument("--md", action="store_true")
    p = sub.add_parser("check", help="coverage: every case-list row tied to its Record")
    p.add_argument("--verbose", action="store_true")
    args = ap.parse_args(argv)
    lib = Library(args.root)
    if getattr(args, "term", None) and args.term not in lib.terms:
        raise SystemExit(f"Unknown term {args.term}; known: {', '.join(lib.terms)}")
    handler = {"find": cmd_find, "show": cmd_show, "cited-by": cmd_cited_by, "text": cmd_text,
               "citator": cmd_citator, "check": cmd_check}[args.command]
    return handler(lib, args) or 0


if __name__ == "__main__":
    sys.exit(main())
