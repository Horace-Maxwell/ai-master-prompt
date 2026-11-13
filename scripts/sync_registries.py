#!/usr/bin/env python3
"""Snapshot the official shadcn registry index into data/registries.json.

Source: https://ui.shadcn.com/r/registries.json (every community registry the
shadcn CLI knows, with health and item counts). Any namespace listed there can
be installed with no configuration: `npx shadcn@latest add @namespace/item`.

Usage:
  python3 scripts/sync_registries.py     # refresh the snapshot, then run build.py
"""
from __future__ import annotations

import datetime
import json
import urllib.request

from _data import DATA

SOURCE = "https://ui.shadcn.com/r/registries.json"


def main() -> None:
    req = urllib.request.Request(SOURCE, headers={"User-Agent": "ai-master-prompt-sync"})
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = json.load(r)
    rows = []
    for x in raw:
        health = x.get("health") or {}
        rank = x.get("ranking") or {}
        row = {
            "name": x["name"],
            "homepage": x.get("homepage", ""),
            "desc": " ".join((x.get("description") or "").split()),
            "items": rank.get("itemCount") or 0,
            "status": health.get("status", "unknown"),
            "rank": round(rank.get("score") or 0, 1),
        }
        if health.get("hidden"):  # still resolvable by the CLI, but delisted from the directory page
            row["hidden"] = True
        rows.append(row)
    rows.sort(key=lambda r: (bool(r.get("hidden")), -r["rank"], r["name"]))
    out = {"source": SOURCE, "fetched": datetime.date.today().isoformat(), "registries": rows}
    path = DATA / "registries.json"
    body = ",\n".join("    " + json.dumps(r, ensure_ascii=False) for r in rows)
    path.write_text(
        '{\n  "source": %s,\n  "fetched": %s,\n  "registries": [\n%s\n  ]\n}\n'
        % (json.dumps(out["source"]), json.dumps(out["fetched"]), body),
        "utf-8",
    )
    print(f"wrote {path.name}: {len(rows)} registries (fetched {out['fetched']})")


if __name__ == "__main__":
    main()
