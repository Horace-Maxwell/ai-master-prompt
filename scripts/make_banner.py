#!/usr/bin/env python3
"""Generate assets/banner.svg (animated README hero) from live data counts.

Design follows ui/prompts/style-recipes.md:
  #4 Terminal + #7 Editorial: serif headline, mono terminal demo, amber accent,
  dot-pattern background with fade mask, film grain, typewriter + marquee
  (names from ui/prompts/effect-vocabulary.md).
Pure SVG + SMIL so it animates inside GitHub's <img> sandbox (no external fonts/JS).

Called automatically by scripts/build.py.
"""
from __future__ import annotations

from html import escape
from pathlib import Path

from _data import countable, load_categories, load_meta, load_resources

ROOT = Path(__file__).resolve().parent.parent

W, H = 1200, 560
BG = "#0C0B0A"
INK = "#EDE6D6"
MUTED = "#8C857A"
AMBER = "#F5A524"
MOSS = "#9BC27D"
SERIF = "'Iowan Old Style','Palatino Linotype',Palatino,Georgia,'Songti SC','Noto Serif SC',serif"
MONO = "'SF Mono',Menlo,Consolas,'Liberation Mono','PingFang SC','Noto Sans Mono CJK SC',monospace"
SANS = "-apple-system,'Segoe UI',Helvetica,Arial,'PingFang SC','Noto Sans SC',sans-serif"

MARQUEE = [
    "shadcn/ui", "Magic UI", "Aceternity", "React Bits", "Looseleaf", "Sketchbook UI",
    "Rare UI", "goopUI", "ExpoKit", "beUI", "affectUI", "AI Elements", "motion-prompt",
    "GSAP", "Motion", "Lenis", "Three.js", "Paper Shaders", "Mobbin MCP", "Figma MCP",
    "find-skills", "frontend-design", "UI UX Pro Max", "awesome-design-md",
    "next-forge", "Expo", "FastMCP", "Mastra", "MediaCrawler", "System Design Primer",
]


def text(x, y, s, size, fill, family, weight=400, extra=""):
    return (
        f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" xml:space="preserve" {extra}>{escape(s)}</text>'
    )


def terminal(x0: int, y0: int) -> str:
    """Terminal window whose lines appear one by one (Typewriter)."""
    w, h = 520, 330
    out = [
        f'<g transform="translate({x0},{y0})">',
        f'<rect width="{w}" height="{h}" rx="14" fill="#151311" stroke="#2A2622"/>',
        f'<rect width="{w}" height="38" rx="14" fill="#1C1916"/>',
        f'<rect y="24" width="{w}" height="14" fill="#1C1916"/>',
    ]
    for i, c in enumerate(("#E5534B", "#D9A33B", "#57A55A")):
        out.append(f'<circle cx="{22 + i * 20}" cy="19" r="6" fill="{c}" opacity=".85"/>')
    out.append(text(w / 2, 24, "~/AI-Master-Prompt", 12, MUTED, MONO, extra='text-anchor="middle"'))

    lines = [
        # (kind, text, color, begin_seconds)
        ("cmd", "python3 scripts/find.py 手绘", INK, 0.6),
        ("out", "⭐ Looseleaf      shadcn/ui, drawn by hand", INK, 2.4),
        ("out", "⭐ Sketchbook UI  notebook-style React kit", INK, 2.6),
        ("out", "   Wired Elements Rough.js web components", MUTED, 2.8),
        ("cmd", "npm i sketchbook-ui", INK, 3.6),
        ("ok", "✓ added 1 package. Now it looks hand-drawn", MOSS, 5.0),
    ]
    y = 78
    for kind, s, color, t in lines:
        if kind == "cmd":
            # prompt sign, then typed text revealed by a growing clip rect
            cid = f"c{int(t * 10)}"
            chars = len(s) + sum(1 for ch in s if ord(ch) > 0x2E80)  # CJK = 2 cols
            tw = chars * 8.6 + 6
            dur = round(min(1.6, 0.05 * len(s)), 2)
            out.append(
                f'<clipPath id="{cid}"><rect x="40" y="{y - 16}" width="0" height="24">'
                f'<animate attributeName="width" from="0" to="{tw:.0f}" begin="{t}s" dur="{dur}s" '
                f'calcMode="discrete" values="{";".join(str(round(tw * k / len(s))) for k in range(len(s) + 1))}" '
                f'fill="freeze"/></rect></clipPath>'
            )
            out.append(
                f'<g opacity="0"><set attributeName="opacity" to="1" begin="{t - 0.3}s" fill="freeze"/>'
                + text(22, y, "$", 14.5, AMBER, MONO, 700)
                + "</g>"
            )
            out.append(f'<g clip-path="url(#{cid})">' + text(40, y, s, 14.5, color, MONO) + "</g>")
        else:
            out.append(
                f'<g opacity="0"><set attributeName="opacity" to="1" begin="{t}s" fill="freeze"/>'
                + text(22, y, s, 14.5, color, MONO)
                + "</g>"
            )
        y += 34 if kind != "ok" else 0
        if kind == "out" and s.startswith("   "):
            y += 10
    # blinking cursor after last line
    out.append(
        f'<rect x="22" y="{y + 22}" width="9" height="17" fill="{AMBER}" opacity="0">'
        f'<set attributeName="opacity" to="1" begin="6s" fill="freeze"/>'
        f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1s" begin="6s" repeatCount="indefinite"/>'
        f"</rect>"
    )
    out.append("</g>")
    return "\n".join(out)


def marquee(y: int) -> str:
    """Infinite horizontal scroll of library names (Marquee)."""
    size, cw, gap = 15, 9.0, 46
    xs, x = [], 0.0
    for name in MARQUEE:
        xs.append(x)
        x += len(name) * cw + gap
    total = x
    items = []
    for copy in (0, total):
        for name, px in zip(MARQUEE, xs):
            items.append(text(px + copy, 0, name, size, INK, MONO, extra='opacity=".72"'))
            items.append(
                text(px + copy + len(name) * cw + gap / 2 - 5, 0, "✦", 11, AMBER, MONO, extra='opacity=".8"')
            )
    return (
        f'<g transform="translate(0,{y})" mask="url(#edgeFade)">'
        f'<line x1="0" x2="{W}" y1="-28" y2="-28" stroke="#2A2622"/>'
        f'<g><animateTransform attributeName="transform" type="translate" from="0 0" to="{-total:.0f} 0" '
        f'dur="60s" repeatCount="indefinite"/>' + "".join(items) + "</g></g>"
    )


def build() -> str:
    res = countable(load_resources())
    cats = load_categories()
    n_res, n_cat = len(res), len(cats)
    n_star = sum(1 for r in res if r.get("star"))

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
        f'aria-label="AI Master Prompt: {n_res} verified resources for AI agents">',
        "<defs>",
        '<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">'
        '<circle cx="1.5" cy="1.5" r="1.1" fill="#3A342D"/></pattern>',
        '<radialGradient id="fade" cx="78%" cy="38%" r="70%"><stop offset="0" stop-color="#fff"/>'
        '<stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>',
        '<mask id="dotMask"><rect width="100%" height="100%" fill="url(#fade)"/></mask>',
        '<linearGradient id="edge" x1="0" x2="1"><stop offset="0" stop-color="#000"/>'
        '<stop offset=".08" stop-color="#fff"/><stop offset=".92" stop-color="#fff"/>'
        '<stop offset="1" stop-color="#000"/></linearGradient>',
        f'<mask id="edgeFade"><rect y="-40" width="{W}" height="60" fill="url(#edge)"/></mask>',
        '<radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#F5A524" stop-opacity=".16"/>'
        '<stop offset="1" stop-color="#F5A524" stop-opacity="0"/></radialGradient>',
        '<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/>'
        '<feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .05 0"/></filter>',
        "</defs>",
        f'<rect width="{W}" height="{H}" rx="18" fill="{BG}"/>',
        f'<rect width="{W}" height="{H}" fill="url(#dots)" mask="url(#dotMask)"/>',
        '<ellipse cx="930" cy="230" rx="380" ry="260" fill="url(#glow)"/>',
        # left column: editorial headline
        text(64, 92, f"{n_res} RESOURCES · {n_cat} CATEGORIES · VERIFIED {load_meta()['verified'][:7]}", 13, AMBER, MONO, 600,
             'letter-spacing="2.2"'),
        text(60, 178, "AI Master", 86, INK, SERIF, 400, 'letter-spacing="-2"'),
        text(60, 268, "Prompt", 86, INK, SERIF, 400, 'font-style="italic" letter-spacing="-2"'),
        f'<rect x="64" y="300" width="56" height="3" fill="{AMBER}"/>',
        text(64, 346, "把这个文件夹交给任何 AI，", 23, INK, SANS, 500),
        text(64, 380, "它立刻知道该用什么。", 23, INK, SANS, 500),
        text(64, 424, "UI 组件 · 动效词汇 · Skills · MCP · 脚手架 · 架构", 15, MUTED, SANS),
        text(64, 448, f"Give this folder to any AI agent. {n_star} ⭐ picks inside.", 15, MUTED, SANS,
             extra='font-style="italic"'),
        terminal(620, 84),
        marquee(522),
        f'<rect width="{W}" height="{H}" rx="18" filter="url(#grain)" opacity=".9" pointer-events="none"/>',
        "</svg>",
    ]
    return "\n".join(parts)


def main() -> None:
    out = ROOT / "assets" / "banner.svg"
    out.parent.mkdir(exist_ok=True)
    out.write_text(build(), "utf-8")
    print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
