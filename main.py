#!/usr/bin/env python3
"""Cutest Picture entry: copy entry.png to the make.fun output dir.

Stdlib only, no network. Verifies the output is byte-identical to the
source image (size + sha256) before exiting.
"""

import hashlib
import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isfile(SOURCE):
        print("error: entry.png not found next to main.py", file=sys.stderr)
        return 1
    dest = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    src_size = os.path.getsize(SOURCE)
    dst_size = os.path.getsize(dest)
    if src_size != dst_size:
        print(f"error: size mismatch {src_size} != {dst_size}", file=sys.stderr)
        return 1
    src_hash = sha256_of(SOURCE)
    dst_hash = sha256_of(dest)
    if src_hash != dst_hash:
        print("error: sha256 mismatch", file=sys.stderr)
        return 1
    with open(dest, "rb") as f:
        magic = f.read(2)
    if magic != b"\xff\xd8":
        print("error: output is not a JPEG (bad magic bytes)", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({dst_size} bytes, JPEG magic OK)")
    print(f"sha256 source={src_hash}")
    print(f"sha256 output={dst_hash} (match)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
