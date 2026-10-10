"""Copy the certificate data into a checkout of certificate-VIII and verify every file.

Usage (from this folder):  python restore.py /path/to/prolate-weil-bounds/certificate-VIII

* the 18 packet matrices are copied to notes/0803_gpt_A5_mu15_certificate/packet/ and checked
  against the SHA-256 sums in packet/manifest.json (shipped with the code);
* the six source matrices are rebuilt from their 48 MiB parts (GitHub limits files to 100 MB) and
  checked against SOURCE_PINS.json (shipped with the code).
Existing files are never overwritten unless they already have the correct hash.
"""
import hashlib, json, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = 'notes/0803_gpt_A5_mu15_certificate'

def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()

def place(target, digest, write):
    if target.exists():
        if sha(target) == digest:
            print('ok (already present)', target); return
        sys.exit(f'refusing to overwrite {target}: hash differs')
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_name(target.name + '.tmp')
    write(tmp)
    if sha(tmp) != digest:
        tmp.unlink(); sys.exit(f'hash mismatch for {target}')
    tmp.rename(target); print('ok', target)

def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    root = Path(sys.argv[1]).resolve()
    manifest = json.loads((root / CERT / 'packet/manifest.json').read_text())
    pins = json.loads((root / CERT / 'SOURCE_PINS.json').read_text())
    for block in manifest['blocks']:
        for ref in block['files'].values():
            src = HERE / CERT / 'packet' / ref['file']
            place(root / CERT / 'packet' / ref['file'], ref['sha256'], lambda t, s=src: shutil.copyfile(s, t))
    for p in (0, 1):
        for name in ('A', 'B', 'J'):
            ref = pins['files'][f'p{p}_{name}']
            parts = sorted((HERE / ref['path']).parent.glob(Path(ref['path']).name + '.part*'))
            if not parts:
                sys.exit('missing parts for ' + ref['path'])
            def join(t, parts=parts):
                with open(t, 'wb') as out:
                    for part in parts:
                        with open(part, 'rb') as f:
                            shutil.copyfileobj(f, out, 1 << 20)
            place(root / ref['path'], ref['sha256'], join)
    print('all 24 data files restored and verified')

if __name__ == '__main__':
    main()
