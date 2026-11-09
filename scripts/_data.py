"""Shared loader: merges data/resources/*.json into one list."""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Windows consoles and pipes are often not UTF-8; never crash on ⭐ or Chinese text.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# An `ai` value (or one segment of it) is a runnable command when it starts with one of these.
CMD_PREFIX = (
    "npx ", "npm ", "pnpm ", "bunx ", "pip ", "uvx ", "uv ", "git ", "claude ", "go ",
    "brew ", "wasp ", "cd ", "/plugin ", "python3 ", "curl ",
)


def is_command(text: str) -> bool:
    return text.strip().startswith(CMD_PREFIX)


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


def countable(res: list[dict]) -> list[dict]:
    """Entries minus cross-listed copies (alias_of), for honest totals."""
    return [r for r in res if not r.get("alias_of")]


def load_meta() -> dict:
    """Repo slug and last-verified date; edit data/meta.json to change them."""
    return json.loads((DATA / "meta.json").read_text("utf-8"))
