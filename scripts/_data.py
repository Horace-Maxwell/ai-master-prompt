"""Shared loader: merges data/resources/*.json into one list."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def load_categories() -> list[dict]:
    return json.loads((DATA / "categories.json").read_text("utf-8"))


def load_resources() -> list[dict]:
    out: list[dict] = []
    for f in sorted((DATA / "resources").glob("*.json")):
        items = json.loads(f.read_text("utf-8"))
        for it in items:
            it.setdefault("_file", f.name)
        out.extend(items)
    return out
