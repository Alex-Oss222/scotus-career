"""Clerical provenance checks for historical-document pointers.

These checks use only quoted local evidence. They neither fetch source documents
nor establish completeness, authenticity, legal effect, or stage authorization.
"""
from __future__ import annotations

from datetime import date
from pathlib import PurePosixPath
import posixpath
import re
import unicodedata
from urllib.parse import unquote, urlsplit


_URL = re.compile(r"https?://[^\s<>\"'`]+")
_CONTROL_ROOTS = {"foundation", "state", "development", ".git", ".agents", ".codex", "AGENTS.md", "README.md"}
_SIMULATION_DIRECTORIES = {
    "records", "runtime", "freeze", "output", "render-inputs", "workspace",
    "entering-law", "close",
}
_MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August",
           "September", "October", "November", "December")
_SUPREME_COURT_REPORTER = re.compile(
    r"(?<!\w)\d+\s*(?:U\W*S\W*|S\W*Ct\W*|L\W*Ed(?:\W*(?:2d|3d))?\W*)\d+", re.I)


def _url_tokens(text):
    """Extract literal URLs, retaining balanced parentheses in URL paths."""
    for match in _URL.finditer(text):
        token = match[0]
        depth = {"(": 0, "[": 0}
        for index, character in enumerate(token):
            if character in depth:
                depth[character] += 1
            elif character in ")]":
                opening = "(" if character == ")" else "["
                if depth[opening] == 0:
                    token = token[:index]
                    break
                depth[opening] -= 1
        # Markdown closing delimiters and sentence punctuation are not part of
        # the URL. Balanced URL parentheses/brackets (including IPv6) remain.
        changed = True
        while changed:
            old = token
            token = token.rstrip(".,;:!?")
            for opening, closing in (("(", ")"), ("[", "]")):
                while token.endswith(closing) and token.count(closing) > token.count(opening):
                    token = token[:-1]
            changed = token != old
        yield token


def _literal_path_present(path, quote):
    # Do not accept a prefix of another path or the same text embedded in a URL.
    for url in _url_tokens(quote):
        quote = quote.replace(url, "")
    return bool(re.search(r"(?<![\w/.:~-])" + re.escape(path) + r"(?![\w/.~-])", quote))


def _local_target_supported(path, evidence):
    for item in evidence:
        quote = item["quote"]
        if _literal_path_present(path, quote):
            return True
        # Relative Markdown links resolve against the evidence file, just as
        # they do when an operator opens the authoritative source file.
        for target in re.findall(r"\]\(([^\s)]+)\)", quote):
            target = target.strip("<>")
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            relative = unquote(parts.path)
            resolved = posixpath.normpath(posixpath.join(
                str(PurePosixPath(item["path"]).parent), relative))
            if resolved == path:
                return True
    return False


def _check_local_kind(path, label):
    parts = PurePosixPath(path).parts
    if not parts or parts[0] in _CONTROL_ROOTS:
        raise ValueError(f"{label}/repository_path: historical source cannot target a control/development file")
    if parts[0] == "terms" and len(parts) >= 3:
        if parts[2] in _SIMULATION_DIRECTORIES or parts[2] in {"workspace.md", "case-list.md"}:
            raise ValueError(f"{label}/repository_path: historical source cannot target a simulated or internal file")


def _date_supported(value, evidence):
    try:
        day = date.fromisoformat(value)
    except (TypeError, ValueError) as error:
        raise ValueError("Historical document_date must be a valid calendar date or null") from error
    month = _MONTHS[day.month - 1]
    # Accept compressed legacy typography, but not date-looking fragments of
    # file names, years, or other identifiers. A yearless month/day is not a
    # complete calendar-date assertion, even when another date supplies a year.
    numeric = (r"(?<![\w/.-])" + re.escape(value)
               + r"(?![\w/-]|\.[A-Za-z0-9])")
    written = (r"(?<!\w)(?:" + month + "|" + month[:3] + r"\.)\s*"
               + str(day.day) + r"\s*,?\s*" + str(day.year) + r"(?!\d)")
    # Abbreviations without periods are common in earlier source notes.
    abbreviated = (r"(?<!\w)" + month[:3] + r"\s+" + str(day.day)
                   + r"\s*,?\s*" + str(day.year) + r"(?!\d)")
    for item in evidence:
        quote = item["quote"]
        for url in _url_tokens(quote):
            quote = quote.replace(url, "")
        if any(re.search(pattern, quote, re.I) for pattern in (numeric, written, abbreviated)):
            return True
    return False


def _citation_supported(citation, evidence):
    """Require a whole quoted citation, tolerating recorded typography only.

    Removing URLs prevents reporter-looking URL paths from supplying otherwise
    unrecorded bibliographic metadata. Abbreviation punctuation and whitespace
    may differ, but digit runs, numeric separators and subsection parentheses
    stay intact. Token boundaries prevent a shorter page or volume from
    matching a longer one.
    Descriptive additions such as a publication year need their own literal
    support; a source pointer alone does not establish them.
    """
    def normalize(value):
        return unicodedata.normalize("NFKC", value).casefold().translate(
            str.maketrans({character: "-" for character in "‐‑‒–—−"}))

    citation = normalize(citation)
    tokens = list(re.finditer(r"\d+|[^\W\d_]", citation))
    if not tokens:
        return False
    # Ordinary typography may not swallow a subsection delimiter. Numbers are
    # matched as whole runs so 20.3 never supplies 203, nor 377 supplies 3-77.
    formatting = r"(?:[^\w()\[\]{}]|_)*"

    def delimiters(value):
        return formatting.join(re.escape(character) for character in value if character in "()[]{}")

    pieces = [r"(?<![^\W_])", delimiters(citation[:tokens[0].start()])]
    for index, token in enumerate(tokens):
        if index:
            previous = tokens[index - 1]
            gap = citation[previous.end():token.start()]
            if previous[0].isdigit() and token[0].isdigit():
                # A decimal, range, or compound instrument number has a real
                # separator; do not treat its punctuation as an abbreviation.
                # A semicolon between parallel citations may be a comma in
                # the source; both still separate the two complete numbers.
                if gap.strip() == ";":
                    pieces.append(r"\s*[,;]\s*")
                    pieces.append(r"(?<!\d)" + re.escape(token[0]) + r"(?!\d)")
                    continue
                numeric_separator = r"\s*".join(re.escape(character) for character in gap if not character.isspace())
                pieces.append(r"\s*" + numeric_separator if numeric_separator else r"\s+")
                pieces.append(r"\s*")
            else:
                structural = delimiters(gap)
                pieces.append(formatting + structural + formatting if structural else formatting)
        if token[0].isdigit():
            pieces.append(r"(?<!\d)" + re.escape(token[0]) + r"(?!\d)")
        else:
            pieces.append(re.escape(token[0]))
    suffix = delimiters(citation[tokens[-1].end():])
    pieces.extend((formatting + suffix if suffix else "", r"(?![^\W_])"))
    pattern = "".join(pieces)
    for item in evidence:
        quote = item["quote"]
        for url in _url_tokens(quote):
            quote = quote.replace(url, "")
        if re.search(pattern, normalize(quote)):
            return True
    return False


def check_historical_document(doc, sources):
    """Reject unsupported historical locations/dates/citations before generation.

    ``sources`` is the shared read-only Sources object. Its evidence method
    checks exact quotations against local files; no network operation occurs.
    Input manifest schemas remain responsible for overall field/type checking.
    """
    label = f"Historical document {doc['document_id']}"
    evidence = doc["evidence"]
    sources.evidence(evidence)
    citation = doc.get("citation")
    if citation is not None:
        if (doc.get("document_type") == "lower_court_opinion"
                and _SUPREME_COURT_REPORTER.search(citation)):
            raise ValueError(f"{label}/citation: a lower-court opinion cannot inherit a Supreme Court reporter citation")
        if not _citation_supported(citation, evidence):
            raise ValueError(f"{label}/citation: whole citation is absent from quoted evidence; "
                             "add verified local evidence or retain an unknown citation")
    url, basis = doc["url"], doc["url_basis"]
    if (url is None) != (basis == "not_recorded"):
        raise ValueError(f"{label}/url_basis: recorded URLs require their recorded evidence basis")
    if url is not None:
        if basis == "explicit_url":
            if not any(url in set(_url_tokens(item["quote"])) for item in evidence):
                raise ValueError(f"{label}/url: exact URL is absent from quoted evidence")
        elif basis == "recorded_archive_identifier":
            match = re.fullmatch(r"https://archive\.org/details/([A-Za-z0-9_.-]+)", url)
            if match is None or not any(re.search(
                r"(?<![A-Za-z0-9_.-])" + re.escape(match[1]) + r"(?![A-Za-z0-9_.-])",
                item["quote"]) for item in evidence):
                raise ValueError(f"{label}/url: exact Archive identifier is absent from quoted evidence")
        else:
            raise ValueError(f"{label}/url_basis: unsupported evidence basis")
    path = doc["repository_path"]
    if path is not None:
        _check_local_kind(path, label)
        if not _local_target_supported(path, evidence):
            raise ValueError(f"{label}/repository_path: exact local target is absent from quoted evidence")
    if doc["document_date"] is not None and not _date_supported(doc["document_date"], evidence):
        raise ValueError(f"{label}/document_date: complete calendar date is absent from quoted evidence; "
                         "add verified local evidence or retain an unknown date")
