"""Apply four exact source-derived editorial omissions to Agostini's packet.

All retained wording is sliced from the source. The hashes constrain the
operation to the four inspected lines; any source drift stops the operation.
"""
from __future__ import annotations

import hashlib
import re


EDITS = {
    "bd3210b52be5717aac30976d2e125f2bfc10a27b09449154fb4c3f00b9dbc8a7": (),
    "6b0b9fa995b1a79f03292ea68a736270319ea4bf96a604af6f22acd0f3aa8bcc": ((327, 370),),
    "dbfea2945ffcc185b8956229dd30c175952ed9846c662ee1541a968aedf29ec8": ((0, 2), (124, 474)),
    "f36972aaad9a92a38eac6b132f8821b5d3a5da067bcd637bf4c2c96e7ed89ce1": ((0, 69), (129, 320)),
}


def sanitize_agostini_text(text: str) -> str:
    """Copy the packet with exactly four source-line operations applied."""
    headings = list(re.finditer(r"^# 127\. Agostini v\. Felton\s*$", text, re.M))
    if len(headings) != 1:
        raise ValueError("Expected one Agostini packet heading")
    start = headings[0].start()
    later = re.search(r"^# \d+\. ", text[headings[0].end():], re.M)
    end = headings[0].end() + later.start() if later else len(text)
    section = text[start:end]
    seen = {key: 0 for key in EDITS}
    output = []
    for line in section.splitlines(keepends=True):
        body = line.rstrip("\r\n")
        ending = line[len(body):]
        key = hashlib.sha256(body.encode("utf-8")).hexdigest()
        if key not in EDITS:
            output.append(line)
            continue
        seen[key] += 1
        ranges = EDITS[key]
        if ranges:
            output.append("".join(body[a:b] for a, b in ranges) + ending)
    if any(count != 1 for count in seen.values()):
        raise ValueError("The four exact Agostini editorial source lines were not found once each")
    return text[:start] + "".join(output) + text[end:]


def sanitize_agostini_neutral_text(text: str) -> str:
    """Omit one exact private-position clause from the neutral reading copy."""
    key = "ab63d44c88d6adc515d87312af5a83b6598128a88c3199bfbbaaaabd9ed6d72b"
    count = 0
    output = []
    for line in text.splitlines(keepends=True):
        body = line.rstrip("\r\n")
        if hashlib.sha256(body.encode("utf-8")).hexdigest() == key:
            count += 1
            output.append(body[:315] + "." + line[len(body):])
        else:
            output.append(line)
    if count != 1:
        raise ValueError("Expected one exact neutral editorial source line")
    return "".join(output)
