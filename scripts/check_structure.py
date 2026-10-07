"""Verify preserved teaching files against their original Git blob hashes."""

import hashlib
import json
from pathlib import Path
import sys


def git_blob_sha(path):
    data = path.read_bytes()
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()


def check_structure(root):
    manifest = json.loads((root / "docs/reorganization.json").read_text(encoding="utf-8"))
    errors = []
    for item in manifest["moved_files"]:
        path = root / item["to"]
        if not path.is_file():
            errors.append(f"Missing: {item['to']}")
        elif git_blob_sha(path) != item["sha"]:
            errors.append(f"Content changed: {item['to']}")
        if (root / item["from"]).exists():
            errors.append(f"Old path remains: {item['from']}")
    for path in (root / "tutorials").rglob("*"):
        if any(part in (".vs", "bin", "obj") for part in path.relative_to(root).parts):
            errors.append(f"Generated artifact remains: {path.relative_to(root)}")
    return errors


def main():
    root = Path(__file__).resolve().parents[1]
    errors = check_structure(root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        raise SystemExit(1)
    print("PASS: preserved tutorial hashes, relocated paths and generated-file cleanup")


if __name__ == "__main__":
    main()
