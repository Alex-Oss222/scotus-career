"""Static, dependency-free navigation for an isolated catalogue snapshot.

This module renders metadata and pointers; it does not interpret law, fetch sources,
verify the snapshot's freshness, or turn internal records into stage-safe inputs.
"""

from __future__ import annotations

from collections import Counter
from html import escape
import json
import re
from urllib.parse import quote, unquote, urlsplit


def _text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def _e(value: object) -> str:
    return escape(_text(value), quote=True)


def _items(value: object) -> list:
    return value if isinstance(value, list) else []


def _external_href(target: object) -> str | None:
    """Reject schemes, credentials, controls and browser URL-parser ambiguities."""
    target = _text(target)
    if not target or any(c.isspace() or ord(c) < 32 or ord(c) == 127 for c in target):
        return None
    if "\\" in target or any(ord(c) < 32 or ord(c) == 127 for c in unquote(target)):
        return None
    try:
        parsed = urlsplit(target)
        if parsed.scheme.lower() not in {"https", "http"} or not parsed.hostname:
            return None
        if parsed.username is not None or parsed.password is not None:
            return None
        # Accessing port also rejects malformed ports rather than producing a bad link.
        parsed.port
    except ValueError:
        return None
    return target


def _repository_href(target: object, prefix: str) -> str | None:
    target = _text(target)
    path, separator, fragment = target.partition("#")
    if not path or "\\" in path or ":" in path or "?" in path:
        return None
    if any(ord(c) < 32 or ord(c) == 127 for c in target):
        return None
    # Canonical repository-relative paths only. The catalogue builder checks
    # existence and symlinks; rendering cannot establish either from metadata.
    if any(part in {"", ".", ".."} for part in path.split("/")):
        return None
    decoded = unquote(path)
    if "\\" in decoded or any(part in {"", ".", ".."} for part in decoded.split("/")):
        return None
    href = prefix + quote(path, safe="/-._~")
    if separator and fragment:
        href += "#" + quote(unquote(fragment), safe="-._~")
    return href


def _link(target: object, label: object, kind: str, prefix: str) -> str:
    href = _external_href(target) if kind == "external" else (
        _repository_href(target, prefix) if kind == "repository" else None
    )
    if href is None:
        return f'<span class="unavailable">{_e(label)}</span> <span class="muted">(no usable link)</span>'
    rel = ' rel="noreferrer noopener"' if kind == "external" else ""
    return f'<a href="{_e(href)}"{rel}>{_e(label)}</a>'


def _location(item: dict, prefix: str) -> str:
    path = item.get("source_path") or item.get("path")
    location = _link(path, path, "repository", prefix) if path else "Source location not recorded"
    if item.get("line") is not None:
        location += f' · line {_e(item["line"])}'
    if item.get("section"):
        location += f' · {_e(item["section"])}'
    return location


def _reference(item: dict, prefix: str) -> str:
    kind = item.get("kind", "missing")
    material = {
        "historical": "Historical pointer",
        "mixed": "Mixed / internal material",
        "unknown": "Material type not established",
    }.get(item.get("material_kind"), "Material type not established")
    target = item.get("target", "No target recorded")
    return (
        f'<li>{_link(target, target, kind, prefix)}'
        f'<p class="source-note">{_e(material)} · {_e(item.get("review_status", "unverified"))}'
        f'<br>Found in {_location(item, prefix)}</p></li>'
    )


def _card(record: dict, prefix: str, ordinal: int) -> str:
    record_id = _text(record.get("record_id")) or f"entry-{ordinal}"
    term = _text(record.get("term"))
    chunks = _items(record.get("chunks"))
    kind = _text(record.get("kind"))
    kind_label = {"court_event": "Court event", "admitted_source": "Admitted source"}.get(kind, "Unclassified record")
    title = record.get("title") or record.get("path") or record_id
    # Search is explicitly metadata search. Including exact citations, references,
    # and inventory captions makes the navigation useful without copying records.
    search_fields = {k: record.get(k) for k in (
        "record_id", "term", "path", "title", "kind", "metadata", "chunks",
        "event_date", "effective_date", "inventory_refs", "references", "citations",
        "sections", "warnings",
    )}
    curation = record.get("curation")
    if isinstance(curation, dict):
        search_fields["curation"] = {key: curation.get(key) for key in ("aliases", "notes")}
    searchable = _text(search_fields)
    out = [
        f'<article class="record" id="{_e(record_id)}" data-term="{_e(term)}" '
        f'data-kind="{_e(kind)}" data-chunks="{_e("|" + "|".join(map(_text, chunks)) + "|")}" '
        f'data-search="{_e(searchable)}">',
        '<div class="record-heading">',
        f'<p class="eyebrow">{_e(term)} · {_e(kind_label)}</p>',
        f'<a class="permalink" href="#{_e(quote(record_id, safe="-._~"))}" aria-label="Link to {_e(title)}">Link to entry</a>',
        '</div>',
        f'<h3>{_e(title)}</h3>',
        '<p class="record-meta">',
        f'Event date: {_e(record.get("event_date") or "Not established")}',
    ]
    if record.get("effective_date"):
        out.append(f' · Effective date: {_e(record["effective_date"])}')
    out.append(f' · Chunks: {_e(", ".join(map(_text, chunks)) or "Not mapped")}')
    out.extend([
        '</p>',
        f'<p class="record-action">{_link(record.get("path"), "Open canonical record", "repository", prefix)}</p>',
        '<p class="source-note">Full record: mixed / internal material. A link does not authorize use in an isolated Run stage.</p>',
    ])
    warnings = _items(record.get("warnings"))
    if warnings:
        out.append('<details class="record-warnings"><summary>Review notes (' + str(len(warnings)) + ')</summary><ul>')
        out.extend(f'<li>{_e(warning)}</li>' for warning in warnings)
        out.append('</ul></details>')
    if isinstance(curation, dict):
        aliases = _items(curation.get("aliases"))
        notes = _items(curation.get("notes"))
        if aliases or notes:
            out.append('<details><summary>Operator annotations</summary><p class="source-note">Operator-supplied navigation aids, separate from the canonical record. These do not establish identity, legal authority, or precedent treatment.</p>')
            if aliases:
                out.append('<h4>Aliases</h4><ul>')
                out.extend(f'<li>{_e(alias)}</li>' for alias in aliases)
                out.append('</ul>')
            if notes:
                out.append('<h4>Notes</h4><ul>')
                out.extend(f'<li>{_e(note)}</li>' for note in notes)
                out.append('</ul>')
            out.append('</details>')
    metadata = record.get("metadata")
    if isinstance(metadata, dict) and metadata:
        out.append('<details><summary>Record metadata</summary><dl class="metadata">')
        for key, value in sorted(metadata.items()):
            out.append(f'<dt>{_e(key)}</dt><dd>{_e(value)}</dd>')
        out.append('</dl></details>')
    inventory = [x for x in _items(record.get("inventory_refs")) if isinstance(x, dict)]
    if inventory:
        out.append(f'<details><summary>Inventory matches ({len(inventory)})</summary><ul>')
        for item in inventory:
            out.append(f'<li>{_e(item.get("caption") or item.get("dockets") or "Inventory row")}')
            if item.get("area_of_law"):
                out.append(f' · {_e(item["area_of_law"])}')
            out.append(f'<p class="source-note">{_location(item, prefix)}</p></li>')
        out.append('</ul></details>')
    references = [x for x in _items(record.get("references")) if isinstance(x, dict)]
    out.append(f'<details><summary>Source pointers ({len(references)})</summary>')
    if references:
        out.append('<ul class="source-list">')
        out.extend(_reference(item, prefix) for item in references)
        out.append('</ul>')
    else:
        out.append('<p>No explicit source pointer was extracted. This does not establish that no source exists.</p>')
    out.append('</details>')
    citations = [x for x in _items(record.get("citations")) if isinstance(x, dict)]
    out.append(f'<details><summary>Citation mentions ({len(citations)})</summary>')
    if citations:
        out.append('<p class="source-note">Textual mentions only; no holding, treatment, or current force is inferred.</p><ul>')
        for item in citations:
            out.append(f'<li><span class="citation">{_e(item.get("text"))}</span><p class="source-note">{_location(item, prefix)}</p></li>')
        out.append('</ul>')
    else:
        out.append('<p>No supported citation pattern was extracted from this record.</p>')
    out.append('</details>')
    sections = [x for x in _items(record.get("sections")) if isinstance(x, dict)]
    if sections:
        out.append(f'<details><summary>Record sections ({len(sections)})</summary><ul>')
        for section in sections:
            out.append(f'<li>{_e(section.get("title"))} · line {_e(section.get("line"))}</li>')
        out.append('</ul></details>')
    if record.get("sha256"):
        out.append(f'<details><summary>Snapshot fingerprint</summary><p class="source-note">SHA-256 of the indexed record bytes. This page does not recheck the file.</p><code>{_e(record["sha256"])}</code></details>')
    out.append('</article>')
    return "\n".join(out)


_STYLE = """
:root{color-scheme:light;--ink:#182c36;--muted:#52646a;--line:#d4dfdf;--paper:#fff;--accent:#155e66;--soft:#e7f1ef}
*{box-sizing:border-box}body{margin:0;background:#f4f6f3;color:var(--ink);font:16px/1.55 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
a{color:#075962;text-underline-offset:.18em;overflow-wrap:anywhere}a:hover{color:#092f34}a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,summary:focus-visible{outline:3px solid #b87520;outline-offset:3px}
.skip{position:absolute;top:-5rem;left:1rem;background:white;padding:.6rem;z-index:2}.skip:focus{top:1rem}.page{max-width:1100px;margin:auto;padding:2.5rem 1.5rem 4rem}
header{padding-bottom:1.4rem;border-bottom:1px solid var(--line)}h1,h2,h3,p{margin-top:0}h1{font:700 clamp(2rem,5vw,3.4rem)/1.1 Georgia,serif;letter-spacing:-.035em;margin-bottom:1rem}h2{font-size:1.45rem;margin-bottom:1rem}h3{font-size:1.3rem;line-height:1.35;margin-bottom:.6rem;overflow-wrap:anywhere}
.eyebrow{text-transform:uppercase;letter-spacing:.08em;font-size:.76rem;font-weight:750;color:var(--accent);margin-bottom:.7rem}.lede{max-width:760px;font-size:1.12rem}.notice{padding:1rem 1.15rem;border-left:4px solid #ae813b;background:#fff7e6;font-size:.94rem}.notice p:last-child{margin-bottom:0}
.coverage{display:flex;flex-wrap:wrap;gap:.75rem;margin:1.5rem 0}.term-tile{flex:1 1 155px;padding:1rem;background:var(--soft);border-radius:.5rem}.term-tile a{font-weight:750}.term-tile span{display:block;color:var(--muted);font-size:.9rem;margin-top:.35rem}
.filters{background:var(--paper);border:1px solid var(--line);padding:1.2rem;border-radius:.7rem;margin:1.5rem 0}.filter-grid{display:grid;grid-template-columns:minmax(180px,2fr) repeat(3,minmax(120px,1fr));gap:1rem}label{font-weight:650;font-size:.9rem;display:block}input,select,button{font:inherit}input,select{display:block;width:100%;margin-top:.4rem;padding:.65rem;border:1px solid #9aadaf;border-radius:.3rem;background:white;color:var(--ink)}button{padding:.45rem .8rem;border:1px solid #8ba6a7;border-radius:.3rem;background:var(--soft);color:var(--ink);cursor:pointer}button:disabled,input:disabled,select:disabled{opacity:.65;cursor:default}.filter-foot{display:flex;gap:1rem;justify-content:space-between;align-items:center;margin-top:1rem}.filter-foot p{margin:0}.help,.source-note,.record-meta,.muted{font-size:.87rem;color:var(--muted)}.help{margin:.7rem 0 0}
.record{background:var(--paper);border:1px solid var(--line);border-radius:.65rem;padding:1.4rem;margin-bottom:1rem;scroll-margin-top:1rem;overflow-wrap:anywhere}.record:target{border-color:#b87520;box-shadow:0 0 0 2px #e1c38f}.record-heading{display:flex;justify-content:space-between;gap:1rem;align-items:baseline}.permalink{font-size:.8rem;white-space:nowrap}.record-action{margin:.6rem 0 .35rem;font-weight:700}.record>.source-note{margin-bottom:1rem}.record-meta{margin-bottom:.6rem}.source-note{margin:.3rem 0 .6rem}.citation{font-weight:650}.unavailable{overflow-wrap:anywhere;color:#754623}
details{border-top:1px solid #e5eaea;padding:.55rem 0}details p{margin:.65rem 0}summary{cursor:pointer;font-size:.94rem;font-weight:600}ul{padding-left:1.3rem;margin:.7rem 0}li{padding:.15rem 0}.metadata{display:grid;grid-template-columns:minmax(130px,1fr) 3fr;gap:.55rem 1rem;font-size:.9rem}dt{font-weight:650}dd{margin:0;white-space:pre-wrap}code{font-size:.8rem;overflow-wrap:anywhere}.record-warnings{color:#754623}.empty{padding:2rem;text-align:center;border:1px dashed #9aadaf;border-radius:.5rem}.additional{margin-top:2rem}.additional>details{padding:.85rem 0}footer{margin-top:2rem;border-top:1px solid var(--line);padding-top:1rem;font-size:.85rem;color:var(--muted)}[hidden]{display:none!important}
@media(max-width:720px){.page{padding:1.5rem 1rem 3rem}.filter-grid{grid-template-columns:1fr 1fr}.filter-grid label:first-child{grid-column:1/-1}.record{padding:1rem}.record-heading{display:block}.permalink{display:inline-block;margin-bottom:.7rem}.metadata{grid-template-columns:1fr;gap:.25rem}.metadata dd{margin-bottom:.6rem}.term-tile{flex-basis:120px}}
@media(max-width:390px){.filter-grid{grid-template-columns:1fr}.filter-grid label:first-child{grid-column:auto}.filter-foot{align-items:flex-start;flex-direction:column}}
@media(prefers-reduced-motion:no-preference){a,button{transition:color .15s ease,background .15s ease}}
@media print{body{background:white}.page{max-width:none;padding:0}.filters,.skip,.permalink{display:none}.record{break-inside:avoid}.notice{background:white}}
"""


_SCRIPT = r"""
(() => {
  'use strict';
  const cards = Array.from(document.querySelectorAll('.record'));
  const search = document.getElementById('search');
  const term = document.getElementById('term-filter');
  const chunk = document.getElementById('chunk-filter');
  const kind = document.getElementById('kind-filter');
  const clear = document.getElementById('clear-filters');
  const status = document.getElementById('results-summary');
  const empty = document.getElementById('empty-state');
  const normalize = value => value.normalize('NFKC').toLowerCase();
  const entries = cards.map(card => ({
    card, term: card.dataset.term, kind: card.dataset.kind,
    chunks: card.dataset.chunks.split('|').filter(Boolean),
    search: normalize(card.dataset.search)
  }));
  function filter() {
    const words = normalize(search.value).trim().split(/\s+/u).filter(Boolean);
    let visible = 0;
    for (const entry of entries) {
      const show = (!term.value || entry.term === term.value) &&
        (!kind.value || entry.kind === kind.value) &&
        (!chunk.value || entry.chunks.includes(chunk.value)) &&
        words.every(word => entry.search.includes(word));
      entry.card.hidden = !show;
      if (show) visible += 1;
    }
    status.textContent = `${visible} of ${cards.length} records shown`;
    empty.hidden = visible !== 0;
  }
  function reset() {
    search.value = ''; term.value = ''; chunk.value = ''; kind.value = '';
    filter();
  }
  function revealHash() {
    let id;
    try { id = decodeURIComponent(window.location.hash.slice(1)); }
    catch (_) { return; }
    const target = document.getElementById(id);
    if (target && target.classList.contains('record') && target.hidden) {
      reset(); target.scrollIntoView();
    }
  }
  for (const input of [search, term, chunk, kind, clear]) input.disabled = false;
  search.addEventListener('input', filter);
  for (const select of [term, chunk, kind]) select.addEventListener('change', filter);
  clear.addEventListener('click', () => { reset(); search.focus(); });
  for (const shortcut of document.querySelectorAll('[data-term-shortcut]')) {
    shortcut.addEventListener('click', () => {
      reset(); term.value = shortcut.dataset.termShortcut; filter();
    });
  }
  window.addEventListener('hashchange', revealHash);
  filter(); revealHash();
})();
"""


def render(catalogue: dict, repo_prefix: str = "../../../../") -> str:
    """Return a self-contained browser; perform no I/O or network operations.

    The prefix is the relative distance from a published snapshot to the repository
    root. Only parent-directory components are accepted, never a URL or arbitrary
    markup. Catalogue validation and safe source resolution belong to the builder.
    """
    if not isinstance(repo_prefix, str) or not re.fullmatch(r"(?:\.\./)*", repo_prefix):
        raise ValueError("repo_prefix must contain only ../ components")
    records = [x for x in _items(catalogue.get("records")) if isinstance(x, dict)]
    counts = Counter(_text(record.get("term")) for record in records)
    terms = sorted(set(counts) | {
        _text(item.get("term")) for item in _items(catalogue.get("terms")) if isinstance(item, dict)
    })
    chunks = sorted({_text(chunk) for record in records for chunk in _items(record.get("chunks"))},
                    key=lambda value: (0, int(value)) if value.isdigit() else (1, value))
    court_count = sum(record.get("kind") == "court_event" for record in records)
    admitted_count = sum(record.get("kind") == "admitted_source" for record in records)
    out = [
        '<!doctype html><html lang="en"><head><meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<meta name="referrer" content="no-referrer">',
        '<title>Development library · Case and source catalogue</title>',
        f'<style>{_STYLE}</style></head><body>',
        '<a class="skip" href="#record-list">Skip to records</a><div class="page">',
        '<header><p class="eyebrow">Stone-Zsela · Isolated development</p>',
        '<h1>Development library</h1>',
        '<p class="lede">Find the simulated record, its citation mentions, and the source pointers recorded with it.</p>',
        f'<p>{len(records)} records · {court_count} court events · {admitted_count} admitted sources</p>',
        '<div class="notice"><p><strong>Development only. Production integration is disabled.</strong> '
        'This catalogue is a navigation aid, not authority or a stage-safe research packet.</p>',
        '<p>Historical pointers are unverified. Historical law may differ from simulated law; '
        'follow the canonical simulated record for the Court’s action. Full records can contain mixed and internal material. '
        'This static view cannot check freshness; validate the snapshot before relying on its pointers.</p></div></header>',
        '<nav class="coverage" aria-label="Browse by term">',
    ]
    for term in terms:
        out.append(f'<div class="term-tile"><a href="#record-list" data-term-shortcut="{_e(term)}">{_e(term)}</a><span>{counts[term]} records</span></div>')
    out.extend([
        '</nav><main><section class="filters" aria-labelledby="filter-heading">',
        '<h2 id="filter-heading">Find a record</h2><div class="filter-grid">',
        '<label for="search">Search metadata and citations<input id="search" type="search" placeholder="Case, docket, citation, or source…" aria-describedby="search-help" disabled></label>',
        '<label for="term-filter">Term<select id="term-filter" disabled><option value="">All terms</option>',
    ])
    out.extend(f'<option value="{_e(term)}">{_e(term)}</option>' for term in terms)
    out.append('</select></label><label for="chunk-filter">Chunk<select id="chunk-filter" disabled><option value="">All chunks</option>')
    out.extend(f'<option value="{_e(chunk)}">Chunk {_e(chunk)}</option>' for chunk in chunks)
    out.extend([
        '</select></label><label for="kind-filter">Record type<select id="kind-filter" disabled>',
        '<option value="">All types</option><option value="court_event">Court event</option>',
        '<option value="admitted_source">Admitted source</option></select></label></div>',
        '<p class="help" id="search-help">Searches catalogue metadata, operator annotations, and extracted mentions, not the full text of records. All search words must match. Filters combine.</p>',
        f'<div class="filter-foot"><p id="results-summary" role="status" aria-live="polite" aria-atomic="true">{len(records)} of {len(records)} records shown</p>',
        '<button type="button" id="clear-filters" disabled>Clear filters</button></div>',
        '<noscript><p>JavaScript is disabled. Every record, citation, and source pointer remains below; use your browser’s Find command.</p></noscript>',
        '</section><section aria-labelledby="records-heading"><h2 id="records-heading">Records</h2>',
        '<p id="empty-state" class="empty" hidden>No matching records. Try fewer search words or clear the filters.</p>',
        '<div id="record-list">',
    ])
    out.extend(_card(record, repo_prefix, index) for index, record in enumerate(records, 1))
    if not records:
        out.append('<p class="empty">This snapshot contains no records.</p>')
    out.append('</div></section><section class="additional" aria-label="Coverage and review notes">')
    carryovers = _items(catalogue.get("carryovers"))
    if carryovers:
        out.append(f'<details><summary>Recorded carryovers ({len(carryovers)})</summary><p class="source-note">These are source entries, not completed adjudications or a new interpretation of their status.</p><ul>')
        for item in carryovers:
            if isinstance(item, dict):
                label = item.get("raw") or item.get("text") or item.get("caption") or item.get("cells") or item
                out.append(f'<li>{_e(label)}')
                if item.get("path") or item.get("source_path"):
                    out.append(f'<p class="source-note">{_location(item, repo_prefix)}</p>')
                out.append('</li>')
            else:
                out.append(f'<li>{_e(item)}</li>')
        out.append('</ul></details>')
    warnings = _items(catalogue.get("warnings"))
    if warnings:
        out.append(f'<details><summary>Catalogue review notes ({len(warnings)})</summary><ul>')
        out.extend(f'<li>{_e(warning)}</li>' for warning in warnings)
        out.append('</ul></details>')
    out.extend([
        '</section></main><footer><p>Records remain authoritative over this derived index. '
        'A citation mention does not establish a holding, a relationship between cases, or a precedent’s current force. '
        'Line numbers identify where a pointer was extracted; links open the file without assuming unsupported line anchors.</p>',
        f'<p>Catalogue schema: {_e(catalogue.get("schema_version", "not specified"))}. '
        'No external scripts, fonts, or network requests are needed to browse this page.</p></footer></div>',
        f'<script>{_SCRIPT}</script></body></html>',
    ])
    return "\n".join(out)
