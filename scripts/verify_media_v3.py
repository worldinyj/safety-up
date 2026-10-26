#!/usr/bin/env python3
"""Verify safety-up V3 local Grokbot source assets; no external dependencies."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "production" / "assets_manifest_v3.json"
def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for piece in iter(lambda: f.read(1024 * 1024), b""):
            h.update(piece)
    return h.hexdigest()

def main():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures = 0
    for ref in data["source_assets"]:
        p = ROOT / ref["local_path"]
        if not p.is_file():
            print("MISSING", ref["id"], p)
            failures += 1
            continue
        actual = sha256(p)
        if actual == ref["sha256"]:
            print("PASS", ref["id"], str(p.relative_to(ROOT)), actual[:16])
        else:
            print("MISMATCH", ref["id"], actual, "expected", ref["sha256"])
            failures += 1
    previs = sorted((ROOT / "assets" / "previs").glob("S0[1-5]_*_PREVIS_V3.jpg"))
    print("PREVIS COUNT", len(previs), "expected 15")
    if len(previs) != 15:
        failures += 1
    checks = ROOT / "production" / "handoff_file_checksums_v3.json"
    if checks.exists():
        items = json.loads(checks.read_text(encoding="utf-8")).get("assets", [])
        for item in items:
            p = ROOT / item["path"]
            if not p.exists() or sha256(p) != item["sha256"]:
                print("MISSING_OR_MISMATCH", item["path"])
                failures += 1
        print("CHECKED INTEGRITY ITEMS", len(items))
    else:
        print("CHECKSUM FILE NOT PRESENT (ZIP may not have been unpacked)")
        failures += 1
    print("STATUS", "PASS" if failures == 0 else f"BLOCKED ({failures} item errors)")
    raise SystemExit(0 if failures == 0 else 1)

if __name__ == "__main__":
    main()
