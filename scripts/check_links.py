#!/usr/bin/env python3
"""Check that every URL in data/resources/*.json still responds.

Usage:
  python3 scripts/check_links.py            # check all, print failures
  python3 scripts/check_links.py --all      # also print OK results
Exit code 1 if any link is dead (404/410 and other hard errors, after retries).
Sites that block bots or rate-limit (401/403/429, redirect loops) are reported as WARN, not failures.
With a few thousand URLs this takes several minutes. A DEAD "URLError" can be a TLS quirk of
Python's urllib rather than a dead site; confirm those with `curl -IL <url>` before removing.
"""
from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from _data import load_resources

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"


def probe(url: str) -> tuple[str, str]:
    """OK / WARN (blocked, rate-limited, odd redirect: probably alive) / DEAD."""
    last = "?"
    for attempt in range(3):
        for method in ("HEAD", "GET"):
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
            try:
                with urllib.request.urlopen(req, timeout=20) as r:
                    return "OK", str(r.status)
            except urllib.error.HTTPError as e:
                last = str(e.code)
                if method == "HEAD":
                    continue  # many servers reject HEAD; retry with GET
            except Exception as e:  # noqa: BLE001
                last = type(e).__name__
                if method == "HEAD":
                    continue
        if last == "429" or not last.isdigit() or last.startswith("5"):
            time.sleep(4 * (attempt + 1))  # rate limit or transient error: back off and retry
            continue
        break
    if last in ("401", "402", "403", "429", "451", "454") or last.startswith("3"):
        return "WARN", last
    return "DEAD", last


def main() -> int:
    res = load_resources()
    urls = sorted({r["url"] for r in res if r["url"].startswith("http")})
    with ThreadPoolExecutor(max_workers=8) as ex:
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
