#!/usr/bin/env python3
"""Check that the install commands in data/resources/*.json point at things that exist.

It never runs a command. It only asks the public registries:
  npx / npm i / npm create / pnpm dlx / bunx   -> package exists on npm
  pip install / uvx                            -> package exists on PyPI
  npx skills add owner/repo, git clone <url>   -> GitHub repo / URL responds
  npx shadcn@latest add <url>                  -> URL responds
  npx shadcn@latest add @namespace/item        -> namespace is in data/registries.json
                                                  (or listed in meta.json "extra_namespaces")

Usage:
  python3 scripts/check_commands.py            # print problems only
  python3 scripts/check_commands.py --all      # also print what was checked
Exit code 1 if anything is missing. Network errors are reported as WARN, not failures.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from _data import DATA, load_meta, load_resources

UA = "Mozilla/5.0 (ai-master-prompt command check)"
NPM_FLAG = re.compile(r"^-")
SKIP_NPX = {"shadcn", "skills"}  # handled separately / always present


def http_status(url: str, method: str = "GET") -> int | str:
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:  # noqa: BLE001
        return type(e).__name__


def strip_version(pkg: str) -> str:
    """@scope/name@1.2 -> @scope/name ; name@latest -> name"""
    if pkg.startswith("@"):
        head, _, _ = pkg[1:].partition("@")
        return "@" + head
    return pkg.partition("@")[0]


def first_pkg(tokens: list[str]) -> str | None:
    for t in tokens:
        if NPM_FLAG.match(t):
            continue
        return t
    return None


def extract(ai: str) -> set[tuple[str, str]]:
    """Returns {(kind, target)} found in one `ai` string."""
    found: set[tuple[str, str]] = set()
    text = re.sub(r"（[^（）]*）", " ", ai)
    for seg in re.split(r"[；;]|&&|\s→\s|\s/\s|\s--\s", text):
        tok = seg.replace("`", " ").replace('"', " ").replace("'", " ").split()
        if tok and tok[0] in ("或", "先", "再"):
            tok = tok[1:]
        if len(tok) < 2:
            continue
        cmd, rest = tok[0], tok[1:]
        if cmd in ("npx", "bunx") or (cmd == "pnpm" and rest[:1] == ["dlx"]):
            if cmd == "pnpm":
                rest = rest[1:]
            pkg = first_pkg(rest)
            if not pkg or "<" in pkg:
                continue
            name = strip_version(pkg)
            if name == "shadcn":
                args = rest[rest.index(pkg) + 1 :]
                if args[:1] == ["add"]:
                    for a in args[1:]:
                        if a.startswith("http"):
                            if "<" not in a:
                                found.add(("url", a))
                        elif a.startswith("@") and "/" in a:
                            found.add(("shadcn-ns", a.split("/")[0]))
                        elif re.fullmatch(r"[\w.-]+/[\w.-]+/[\w.<>-]+", a):
                            found.add(("github", "/".join(a.split("/")[:2])))
            elif name == "skills":
                args = rest[rest.index(pkg) + 1 :]
                if args[:1] == ["add"] and len(args) > 1:
                    src = args[1]
                    if src.startswith("http"):
                        found.add(("url", src))
                    elif re.fullmatch(r"[\w.-]+/[\w.-]+", src):
                        found.add(("github", src))
            elif name not in SKIP_NPX and re.fullmatch(r"(@[\w.-]+/)?[\w.-]+", name):
                found.add(("npm", name))
        elif cmd == "npm" and rest[0] in ("i", "install", "add"):
            for t in rest[1:]:
                if NPM_FLAG.match(t) or "<" in t:
                    continue
                name = strip_version(t)
                if re.fullmatch(r"(@[\w.-]+/)?[\w.-]+", name):
                    found.add(("npm", name))
        elif cmd in ("npm", "pnpm", "yarn", "bun") and rest[0] == "create":
            pkg = first_pkg(rest[1:])
            if pkg and "<" not in pkg:
                name = strip_version(pkg)
                if name.startswith("@"):
                    scope, _, n = name.partition("/")
                    name = f"{scope}/create-{n}" if n else f"{scope}/create"
                else:
                    name = "create-" + name
                found.add(("npm", name))
        elif cmd in ("pip", "pip3") and rest[0] == "install":
            for t in rest[1:]:
                if t.startswith("-") or "<" in t:
                    continue
                name = re.split(r"[\[=<>~!]", t)[0]
                if re.fullmatch(r"[\w.-]+", name):
                    found.add(("pypi", name))
        elif cmd == "uvx":
            src = next((t.split("=", 1)[1] for t in rest if t.startswith("--from=")), None)
            if src is None and "--from" in rest[:-1]:
                src = rest[rest.index("--from") + 1]
            pkg = src or first_pkg(rest)
            if pkg and re.fullmatch(r"[\w.-]+", pkg):
                found.add(("pypi", pkg))
        elif cmd == "git" and rest[0] == "clone":
            url = next((t for t in rest[1:] if t.startswith("http")), None)
            if url:
                found.add(("url", url))
    return found


def check(kind: str, target: str, namespaces: set[str]) -> tuple[str, str]:
    if kind == "shadcn-ns":
        return ("OK", "") if target in namespaces else ("MISSING", "not in data/registries.json")
    if kind == "npm":
        s = http_status("https://registry.npmjs.org/" + urllib.parse.quote(target, safe="@"))
    elif kind == "pypi":
        s = http_status(f"https://pypi.org/pypi/{target}/json")
    elif kind == "github":
        s = http_status(f"https://github.com/{target}", "HEAD")
    else:
        s = http_status(target)
        if s in (403, 405, 429):
            return "WARN", str(s)
    if s == 200:
        return "OK", ""
    if s == 404:
        return "MISSING", "404"
    return "WARN", str(s)


def main() -> int:
    reg_file = DATA / "registries.json"
    namespaces = {r["name"] for r in json.loads(reg_file.read_text("utf-8"))["registries"]} if reg_file.exists() else set()
    namespaces |= set(load_meta().get("extra_namespaces", []))

    wanted: dict[tuple[str, str], list[str]] = {}
    for r in load_resources():
        for item in extract(r.get("ai", "")):
            wanted.setdefault(item, []).append(r["id"])

    items = sorted(wanted)
    with ThreadPoolExecutor(max_workers=12) as ex:
        results = list(ex.map(lambda it: check(it[0], it[1], namespaces), items))

    missing = warn = 0
    for (kind, target), (status, why) in zip(items, results):
        if status == "MISSING":
            missing += 1
        elif status == "WARN":
            warn += 1
        if status != "OK" or "--all" in sys.argv:
            ids = ", ".join(wanted[(kind, target)][:3])
            print(f"{status:7} {kind:9} {target}  {why}  ← {ids}")
    print(f"\n{len(items)} targets checked, {missing} missing, {warn} could not be confirmed")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
