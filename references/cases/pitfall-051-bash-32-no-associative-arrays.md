---
reference_id: REF-CASE-051
title: Pitfall 051 — bash 3.2(macOS 默认)不支持 declare -A 关联数组,verify-all.sh 用普通数组 + 索引
category: cases
date: 2026-06-24
type: script-tooling-trap
used_when:
  - BASH-SCRIPT-WRITING
  - VERIFY-ALL-SCRIPT
  - MACOS-COMPATIBILITY
called_by:
  - skill-optimizer
  - any-agent-writing-bash-on-macos
depends_on:
  - REF-HYGIENE-001
outputs:
  - bash32_compatibility_protocol
---

# Pitfall 051: bash 3.2(macOS 默认)不支持 declare -A 关联数组

> **日期**: 2026-06-24
> **触发**: 2026-06-24 jony-ive-design2me-v2 自动诊断修复。`scripts/verify-all.sh` 第一次用 `declare -A RESULTS` 关联数组存 exit code,实测才发现 `RESULTS[foo]=1` 被当成 `RESULTS[0]=1`(bash 3.2 把字符串 key 算术求值),导致汇总段全部显示 exit=0。
> **严重级别**: 🟠 HIGH for any bash script on macOS
> **特征**: bash 3.2.57 是 macOS Big Sur+ 的默认 bash(Apple 不愿切换 GPLv3 bash),bash 4+ 特性(`declare -A`、`mapfile`、`${var,,}` 等)在 macOS 上**默默失败**

## 1. 现象

```bash
declare -A RESULTS  # bash 4+: OK  |  bash 3.2: 报"invalid option"或静默忽略
RESULTS[foo]=1      # bash 4+: 正常   |  bash 3.2: 等价于 RESULTS[0]=1
echo "${RESULTS[foo]:-MISS}"  # 输出 MISS(永远拿不到)
```

完整错误信息:
```
bash: line 1: declare: -A: invalid option
declare: usage: declare [-afFirtx] [-p] [name[=value] ...]
```

## 2. 受影响的 bash 4+ 特性

| 特性 | bash 4+ | bash 3.2 | 影响 |
|---|---|---|---|
| `declare -A` 关联数组 | ✅ | ❌ silent failure | 退出码收集、key-value 存储 |
| `declare -g` 全局变量声明 | ✅ | ❌ | |
| `mapfile` / `readarray` | ✅ | ❌ | 文件按行读数组 |
| `${var,,}` 全小写 | ✅ | ❌ | 大小写转换 |
| `**` globstar 递归匹配 | ✅ | ❌ | `shopt -s globstar` |
| `${var^}` 首字母大写 | ✅ | ❌ | |
| `printf -v` 赋值给变量 | ✅ | ❌ | |
| coproc 协进程 | ✅ | ❌ | |

## 3. 修复协议

### 3.1 关联数组 → 平行数组 + 索引查找

```bash
# ❌ bash 3.2 失败
declare -A RESULTS
RESULTS[foo]=1
echo "${RESULTS[foo]}"

# ✅ bash 3.2 兼容
SCRIPT_NAMES=("foo" "bar")
SCRIPT_CMDS=("cmd1" "cmd2")
declare -a EXIT_CODES
for i in "${!SCRIPT_NAMES[@]}"; do
    name="${SCRIPT_NAMES[$i]}"
    cmd="${SCRIPT_CMDS[$i]}"
    output=$(eval "$cmd" 2>&1)
    exit_code=$?
    EXIT_CODES[$i]="$exit_code"
done
# 读
echo "${EXIT_CODES[0]}"
```

### 3.2 `$?` 必须在 echo 前捕获

```bash
# ❌ $? 被 echo 覆盖
output=$(eval "$cmd" 2>&1)
echo "$output"
exit_code=$?  # 这是 echo 的 exit code (0)

# ✅ 先捕获
output=$(eval "$cmd" 2>&1)
exit_code=$?
echo "$output"
```

### 3.3 `set -u` + 数组兜底语法可能不稳

```bash
set -u
declare -A R
R[foo]=1
echo "${R[foo]:-MISS}"  # bash 4: OK  |  bash 3.2: 可能仍报错

# ✅ 不用 set -u,或先 unset 后取
echo "${R[foo]-MISS}"  # 没有冒号 = 不存在不报错
```

## 4. 检测 bash 版本的协议

写 bash 脚本时,文件头部加:

```bash
if [[ "${BASH_VERSINFO[0]}" -lt 4 ]]; then
    echo "⚠️ bash ${BASH_VERSION} (< 4) detected. macOS default. Avoiding bash 4+ features." >&2
fi
```

## 5. verify-all.sh 最终兼容写法(本 session 已落地)

```bash
#!/usr/bin/env bash
# verify-all.sh — macOS bash 3.2 兼容版
# 不启用 set -u(避免与 bash 3.2 数组兜底语法冲突)
# 不启用 set -e(让所有验证都跑完再汇总)

SCRIPT_NAMES=("validate_skill" "validate_reference_graph" "audit_references" "check_version_pollution")
SCRIPT_CMDS=("python3 scripts/validate_skill.py ." "...")

declare -a EXIT_CODES
OVERALL_EXIT=0

for i in "${!SCRIPT_NAMES[@]}"; do
    name="${SCRIPT_NAMES[$i]}"
    cmd="${SCRIPT_CMDS[$i]}"
    output=$(eval "$cmd" 2>&1)
    exit_code=$?  # 关键:在 echo 前捕获
    echo "$output"
    EXIT_CODES[$i]="$exit_code"
    [[ "$exit_code" -ne 0 ]] && OVERALL_EXIT=1
done

# 汇总段用索引读
for i in "${!SCRIPT_NAMES[@]}"; do
    code="${EXIT_CODES[$i]:-?}"
    echo "  ${SCRIPT_NAMES[$i]}: $code"
done
```

## 6. 实战案例(本次 session)

**第一版**: 用 `declare -A RESULTS`,汇总段全部 ✅,但实际脚本有失败。
**第二版**: 把 `$?` 移到 echo 之前,还是 ✅,因为 `RESULTS[foo]` 拿不到值。
**第三版**: 改用平行数组 + 索引,才正确显示 ❌。

**教训**: **写完 bash 脚本必须实测**,不能信 IDE 静态检查(bash 3.2 兼容性问题只能 runtime 发现)。

## 7. 引用

- 同类陷阱: `pitfall-002-image-view-failure-loop.md`(工具链限制也是同类家族 — 写之前先验证工具能力)
- Linux 兼容性: `pitfall-021-reference-graph-upgrade-friction.md`(同精神: 不要假设全平台兼容)
- Linux Foundation: [Bash 4.0 release notes](https://lists.gnu.org/archive/html/bug-bash/2009-02/msg00033.html) — bash 3.2 是 2006 年版本
- macOS bash 切换: `brew install bash`(但 Apple 不建议全局切换)