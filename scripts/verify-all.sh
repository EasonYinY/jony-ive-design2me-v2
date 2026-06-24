#!/usr/bin/env bash
# verify-all.sh — 一键跑全部 4 个验证脚本,输出 baseline 对比
#
# 用法:
#   bash scripts/verify-all.sh [SKILL_ROOT]
# 默认 SKILL_ROOT = 当前脚本所在目录的父目录
#
# 退出码:
#   0 = 全部通过
#   1 = 任一验证失败(打印汇总,仍输出所有结果)
#
# 添加日期: 2026-06-24 by 自动诊断修复
# 触发原因: 原 4 个脚本入口签名不一致,每次升级需要手动试错;现在一键跑全部

# 注意:不启用 set -u,因为 RESULTS[xxx] 兜底语法在不同 bash 版本下不稳
# 不启用 set -e,因为要让所有脚本都跑完再汇总

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="${1:-$(dirname "$SCRIPT_DIR")}"
LEDGER="${SKILL_ROOT}/SOURCE_LEDGER.csv"

if [[ ! -d "$SKILL_ROOT" ]]; then
    echo "❌ SKILL_ROOT 不存在: $SKILL_ROOT" >&2
    exit 2
fi
if [[ ! -f "$LEDGER" ]]; then
    echo "❌ SOURCE_LEDGER.csv 不存在: $LEDGER" >&2
    exit 2
fi

cd "$SKILL_ROOT" || exit 2

echo "═══════════════════════════════════════════════"
echo "  jony-ive-design2me-v2 全量验证"
echo "  SKILL_ROOT: $SKILL_ROOT"
echo "  时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo "═══════════════════════════════════════════════"

# 运行 4 个脚本,捕获退出码和输出
# 注意:macOS 默认 bash 3.2 不支持 declare -A,改用平行数组 + 索引查找
SCRIPT_NAMES=(
    "validate_skill"
    "validate_reference_graph"
    "audit_references"
    "check_version_pollution"
)
SCRIPT_CMDS=(
    "python3 scripts/validate_skill.py ."
    "python3 scripts/validate_reference_graph.py ."
    "python3 scripts/audit_references.py . SOURCE_LEDGER.csv"
    "python3 scripts/check_version_pollution.py ."
)

OVERALL_EXIT=0
TOTAL_FAILURES=0

# 用普通数组按索引存储 exit code
declare -a EXIT_CODES

for i in "${!SCRIPT_NAMES[@]}"; do
    name="${SCRIPT_NAMES[$i]}"
    cmd="${SCRIPT_CMDS[$i]}"
    echo ""
    echo "──── $name ─────────────────────────────────"
    output=$(eval "$cmd" 2>&1)
    exit_code=$?
    echo "$output"
    EXIT_CODES[$i]="$exit_code"
    if [[ "$exit_code" -ne 0 ]]; then
        OVERALL_EXIT=1
        count=$(echo "$output" | grep -c "^失败：" 2>/dev/null || true)
        TOTAL_FAILURES=$((TOTAL_FAILURES + ${count:-0}))
    fi
done

echo ""
echo "═══════════════════════════════════════════════"
echo "  汇总"
echo "═══════════════════════════════════════════════"
for i in "${!SCRIPT_NAMES[@]}"; do
    name="${SCRIPT_NAMES[$i]}"
    code="${EXIT_CODES[$i]:-?}"
    if [[ "$code" == "0" ]]; then
        status="✅ 通过"
    else
        status="❌ 失败 (exit $code)"
    fi
    printf "  %-30s %s\n" "$name" "$status"
done
echo ""
echo "  失败总数(粗略): $TOTAL_FAILURES"
echo ""

if [[ $OVERALL_EXIT -eq 0 ]]; then
    echo "  🎉 全部 4 个验证通过"
else
    echo "  ⚠️  至少 1 个验证失败,请查看上方详细输出"
fi
echo ""

exit $OVERALL_EXIT