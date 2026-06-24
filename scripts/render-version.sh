#!/usr/bin/env bash
# render-version.sh — 预览/导出渲染结果(SKILL.md frontmatter version → {{skill_version}} 占位符)
#
# 设计原则(2026-06-24 修正版):
#   - references/ 字面永远保留 {{skill_version}},**不**在源文件中替换为版本号
#   - SKILL.md frontmatter version 是单一真实版本号源(SSOT)
#   - bump 版本 = 改 SKILL.md frontmatter → 完成(零修改其他文件)
#   - 本脚本的用途:
#       ① --preview:输出渲染预览(用于 Lovart 出图、文档展示)
#       ② --export <dir>:把渲染结果写到 export 目录(用于分发出图包)
#       ③ 无参数:仅显示 SKILL.md 当前版本号 + 渲染计数(不修改任何文件)
#
# 历史变更:
#   v3.4.0: 第一版 — 设计有 bug(渲染后占位符消失,bump 时需再次替换)
#   v3.5.1: 修正版 — references/ 字面永远保留 {{skill_version}},脚本只输出,不修改源
#
# 退出码:
#   0 = 成功
#   1 = SKILL.md 缺 version 字段
#   2 = SKILL.md 文件不存在

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="${1:-$(dirname "$SCRIPT_DIR")}"
SKILL_MD="$SKILL_ROOT/SKILL.md"

if [[ ! -f "$SKILL_MD" ]]; then
    echo "❌ SKILL.md 不存在: $SKILL_MD" >&2
    exit 2
fi

# 1. 提取版本号(保留 v 前缀)
SKILL_VERSION=$(grep '^version:' "$SKILL_MD" | head -1 | sed 's/version:\s*//' | tr -d '[:space:]')

if [[ -z "$SKILL_VERSION" ]]; then
    echo "❌ SKILL.md frontmatter 缺少 version: 字段" >&2
    exit 1
fi

# 加 v 前缀(如果原值没有)
case "$SKILL_VERSION" in
    v*) FULL_VERSION="$SKILL_VERSION" ;;
    *)  FULL_VERSION="v$SKILL_VERSION" ;;
esac

PLACEHOLDER='{{skill_version}}'

# 2. 统计占位符数量(无副作用,只读)
TOTAL_PLACEHOLDERS=0
COUNT_FILES=0
for md in $(find "$SKILL_ROOT/references" -name "*.md" -type f 2>/dev/null); do
    rel="${md#$SKILL_ROOT/}"
    [[ "$rel" == references/changelogs/* || "$rel" == references/knowledge-base/* ]] && continue
    n=$(grep -c "$PLACEHOLDER" "$md" 2>/dev/null | head -1)
    n="${n:-0}"
    if [[ "$n" -gt 0 ]]; then
        TOTAL_PLACEHOLDERS=$((TOTAL_PLACEHOLDERS + n))
        COUNT_FILES=$((COUNT_FILES + 1))
    fi
done

# 3. 处理参数
case "${2:-}" in
    --preview)
        # 输出所有含占位符文件的渲染预览
        echo "═══════════════════════════════════════════════"
        echo "  render-version --preview"
        echo "  SKILL_VERSION:   $FULL_VERSION (从 SKILL.md)"
        echo "  占位符总数:      $TOTAL_PLACEHOLDERS"
        echo "  文件数:          $COUNT_FILES"
        echo "═══════════════════════════════════════════════"
        echo ""
        for md in $(find "$SKILL_ROOT/references" -name "*.md" -type f 2>/dev/null); do
            rel="${md#$SKILL_ROOT/}"
            [[ "$rel" == references/changelogs/* || "$rel" == references/knowledge-base/* ]] && continue
            if grep -q "$PLACEHOLDER" "$md" 2>/dev/null; then
                echo "── $rel ──"
                perl -pe "s/\Q$PLACEHOLDER\E/$FULL_VERSION/g" "$md"
                echo ""
            fi
        done
        ;;

    --export)
        # 导出到目录
        OUT_DIR="${3:-$SKILL_ROOT/build/rendered}"
        mkdir -p "$OUT_DIR"
        # 镜像目录结构,只改含占位符的文件
        for md in $(find "$SKILL_ROOT/references" -name "*.md" -type f 2>/dev/null); do
            rel="${md#$SKILL_ROOT/}"
            [[ "$rel" == references/changelogs/* || "$rel" == references/knowledge-base/* ]] && continue
            out="$OUT_DIR/$rel"
            mkdir -p "$(dirname "$out")"
            if grep -q "$PLACEHOLDER" "$md" 2>/dev/null; then
                perl -pe "s/\Q$PLACEHOLDER\E/$FULL_VERSION/g" "$md" > "$out"
            else
                cp "$md" "$out"
            fi
        done
        echo "✅ 已导出到: $OUT_DIR (SKILL_VERSION=$FULL_VERSION)"
        ;;

    "")
        # 默认:只显示状态
        echo "═══════════════════════════════════════════════"
        echo "  render-version.sh (状态查询)"
        echo "  SKILL.md:        $SKILL_MD"
        echo "  当前版本号:      $FULL_VERSION (SSOT)"
        echo "  占位符总数:      $TOTAL_PLACEHOLDERS(分布在 $COUNT_FILES 个文件)"
        echo "═══════════════════════════════════════════════"
        echo ""
        echo "用法:"
        echo "  bash scripts/render-version.sh             # 状态查询"
        echo "  bash scripts/render-version.sh . --preview  # 输出渲染预览到 stdout"
        echo "  bash scripts/render-version.sh . --export <dir>  # 导出到目录"
        echo ""
        echo "bump 版本流程:"
        echo "  1. 改 SKILL.md frontmatter version: X.Y.Z"
        echo "  2. 完成(不需要改任何 references/ 字面)"
        echo "  3. 出图/分发前跑 --preview 或 --export"
        ;;

    *)
        echo "用法: bash scripts/render-version.sh [SKILL_ROOT] [--preview|--export <dir>]"
        exit 1
        ;;
esac

exit 0