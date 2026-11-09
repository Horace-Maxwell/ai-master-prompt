#!/usr/bin/env bash
# AI Master Prompt: one-step setup.
#   ./setup.sh                 check environment, fetch submodule, self-test
#   ./setup.sh --link-skills   also symlink bundled skills into ~/.claude/skills
set -euo pipefail

cd "$(dirname "$0")"
ROOT="$(pwd)"
AMBER=$'\033[33m'; GREEN=$'\033[32m'; DIM=$'\033[2m'; RED=$'\033[31m'; OFF=$'\033[0m'
ok()   { printf "%s✓%s %s\n" "$GREEN" "$OFF" "$1"; }
warn() { printf "%s!%s %s\n" "$AMBER" "$OFF" "$1"; }
die()  { printf "%s✗%s %s\n" "$RED" "$OFF" "$1"; exit 1; }

printf "\n%sAI Master Prompt%s %s· setup%s\n\n" "$AMBER" "$OFF" "$DIM" "$OFF"

# 1. Python 3.8+
PY="$(command -v python3 || command -v python || true)"
[ -n "$PY" ] || die "需要 Python 3.8+（https://www.python.org/downloads/）"
"$PY" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' \
  || die "Python 版本太低：$("$PY" --version 2>&1)，需要 3.8+"
ok "Python: $("$PY" --version 2>&1)"

# 2. Bundled skill submodule (works for git clones and ZIP downloads)
LIEFLAT_URL="https://github.com/larashero3-dotcom/lieflat-less-ai-tone.git"
if [ -f lieflat-less-ai-tone/SKILL.md ]; then
  ok "子模块 lieflat-less-ai-tone 已就绪"
elif [ -d .git ] && command -v git >/dev/null; then
  git submodule update --init --recursive && ok "已拉取子模块 lieflat-less-ai-tone"
elif command -v git >/dev/null; then
  rmdir lieflat-less-ai-tone 2>/dev/null || true
  git clone --depth 1 "$LIEFLAT_URL" lieflat-less-ai-tone && ok "已下载 lieflat-less-ai-tone"
else
  warn "没有 git，跳过 lieflat-less-ai-tone（其余功能不受影响）"
fi

# 3. Self-test: data validates, search works
"$PY" scripts/build.py --check >/dev/null && ok "数据校验通过：$("$PY" scripts/build.py --check | sed 's/^OK: //')"
"$PY" scripts/find.py 手绘 --limit 1 >/dev/null && ok "搜索正常（python3 scripts/find.py <关键词>）"

# 4. Optional: install bundled skills globally for Claude Code
if [ "${1:-}" = "--link-skills" ]; then
  DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
  mkdir -p "$DEST"
  link() {
    local src="$1" name="$2"
    [ -f "$src/SKILL.md" ] || { warn "跳过 $name（找不到 SKILL.md）"; return; }
    if [ -e "$DEST/$name" ] && [ ! -L "$DEST/$name" ]; then
      warn "$DEST/$name 已存在且不是链接，未覆盖"
    else
      ln -sfn "$src" "$DEST/$name" && ok "已安装 Skill：$name → $DEST/$name"
    fi
  }
  link "$ROOT/ui" "ui-master"
  link "$ROOT/lieflat-less-ai-tone" "lieflat-less-ai-tone"
  printf "  %s其他 Agent（Codex / Cursor …）：把 %s/ui 复制或链接到它的 skills 目录即可%s\n" "$DIM" "$ROOT" "$OFF"
fi

cat <<EOF

${GREEN}准备好了。${OFF}三种用法：

  ${AMBER}1.${OFF} 在这个文件夹里打开 Claude Code / Codex / Cursor，直接说需求
     ${DIM}它会先读 AGENTS.md，再按路由表找到该用的库${OFF}
  ${AMBER}2.${OFF} 复制 MASTER_PROMPT.md 到任何 AI 聊天框
  ${AMBER}3.${OFF} 自己搜：python3 scripts/find.py 液态玻璃

EOF
