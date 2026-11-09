#!/usr/bin/env python3
"""Check that every URL in data/resources/*.json still responds.

Usage:
  python3 scripts/check_links.py            # check all, print failures
  python3 scripts/check_links.py --all      # also print OK results
Exit code 1 if any link is dead (4xx except 403/429, 5xx, or network error).
Note: some sites block bots (403/429/Cloudflare); those are reported as WARN, not failures.
"""
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from _data import load_resources

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"


def probe(url: str) -> tuple[str, str]:
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=15) as r:
                return "OK", str(r.status)
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (400, 403, 404, 405, 429, 501):
                continue  # many servers reject HEAD; retry with GET
            if e.code in (401, 403, 429, 503):
                return "WARN", str(e.code)
            return "DEAD", str(e.code)
        except Exception as e:  # noqa: BLE001
            if method == "HEAD":
                continue
            return "DEAD", type(e).__name__
    return "DEAD", "?"


def main() -> int:
    res = load_resources()
    urls = sorted({r["url"] for r in res if r["url"].startswith("http")})
    with ThreadPoolExecutor(max_workers=16) as ex:
        results = list(ex.map(probe, urls))
    dead = 0
    for url, (status, code) in zip(urls, results):
        if status == "DEAD":
            dead += 1
        if status != "OK" or "--all" in sys.argv:
            print(f"{status:4} {code:>5}  {url}")
    print(f"\n{len(urls)} urls, {dead} dead, {sum(s == 'WARN' for s, _ in results)} warn")
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
