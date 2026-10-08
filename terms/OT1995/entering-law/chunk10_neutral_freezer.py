from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]

def read(name):
    return (ROOT / 'entering-law' / name).read_text(encoding='utf-8-sig')

def freeze(key, text, supplements):
    target = ROOT / 'freeze' / f'OT_1995CHUNK10_{key}_NEUTRAL.md'
    if target.exists():
        raise RuntimeError(f'Refuse to replace frozen packet: {target}')
    parts = [text]
    for title, filename, start, end in supplements:
        source = read(filename)
        if start is not None:
            source = source.split(start, 1)[1]
            source = start + source
        if end is not None:
            source = source.split(end, 1)[0]
        parts += [f'\n\n# {title}\n\nSource: `../entering-law/{filename}`. Copied neutral reading material; stated source limits remain operative.\n\n', source]
    target.write_text(''.join(parts).rstrip() + '\n', encoding='utf-8')
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print(f'{key}: {target.name}; {target.stat().st_size} bytes; sha256 {digest}')

if __name__ == '__main__':
    import sys
    key = sys.argv[1]
    config = ROOT / 'entering-law' / f'OT_1995CHUNK10_{key}_VALIDATED_PREPARATION.json'
    import json
    data = json.loads(config.read_text(encoding='utf-8-sig'))
    freeze(key, data['text'], data['supplements'])
