---
reference_id: REF-CASE-053
title: Pitfall 053 — Dynamic Version Variable Protocol 三大失败模式
category: cases
date: 2026-06-24
type: operational-trap
used_when:
  - SKILL-UPGRADE
  - VERSION-BUMP
  - DYNAMIC-VARIABLE-PROTOCOL
called_by:
  - skill-optimizer
  - file-hygiene-check
depends_on:
  - REF-HYGIENE-001
  - REF-RULES-VSN-001
outputs:
  - dynamic_var_pitfall_patterns
---

# Pitfall 053 — Dynamic Version Variable Protocol 三大失败模式

> **触发**(2026-06-24):user 显式声明"所有其他位置的版本号改为动态变量,永远不需要修改",实现此协议时连续踩 3 个坑。
>
> **严重级别**:🔴 BLOCKER(任何版本号动态化尝试)
>
> **关系**:v3.4.0 设计 bug + v3.5.1 修正版;与 `file-hygiene.md` 铁律 8.6 配套。

## 1. 失败 1 — 占位符渲染后被销毁(原始设计 bug)

### 1.1 现象

第一版 `render-version.sh` 把 `{{skill_version}}` 替换为字面版本号(`v3.4.0`)并**写回 references/ 源文件**。下一次 bump 时:

```
v3.4.0 references/(已被渲染为字面,占位符消失)
↓
bump 到 3.5.1
↓
references/ 里全是过期字面 v3.4.0,占位符为 0
↓
需要再次批量替换 v3.4.0 → v3.5.1
↓
违反 "永远不需要修改" 的用户约束
```

### 1.2 根因

混淆了**渲染输出**与**源文件**两个概念:

- ❌ 错误设计:把渲染结果写回源文件
- ✅ 正确设计:占位符永远保留在源文件,渲染只在 `--preview` / `--export` 时执行

### 1.3 修复

```bash
# render-version.sh 头部加铁律注释
# 铁律:占位符 {{skill_version}} 在 references/ 源文件中**永不**被替换为字面
# 渲染只在 --preview(stdout) / --export <dir>(新文件)时执行
```

## 2. 失败 2 — `v` 前缀丢失

### 2.1 现象

```bash
SKILL_VERSION=$(grep '^version:' SKILL.md | sed 's/version:\s*//' | tr -d '[:space:]')
echo "$SKILL_VERSION"
# 输出: 3.5.1  (无 v 前缀!)
```

下游渲染时:`sed s/{{skill_version}}/3.5.1/g` 把 `本技能 {{skill_version}}` 渲染为 `本技能 3.5.0`(或 `本技能 3.5.1`),**没有 v 前缀**,污染语义(读者以为是其他编号,如章节号)。

### 2.2 根因

`grep '^version:' SKILL.md` 匹配 `version: 3.5.1`,`sed 's/version:\s*//'` 删掉 `version: ` 前缀,得到裸 `3.5.1`。**不会**自动加回 `v` 前缀。

### 2.3 修复

```bash
# 显式 case 分支加 v 前缀
case "$SKILL_VERSION" in
    v*) FULL_VERSION="$SKILL_VERSION" ;;
    *)  FULL_VERSION="v$SKILL_VERSION" ;;
esac
```

**测试**:`bash scripts/render-version.sh . --preview | grep "本技能"` 应输出 `本技能 v3.5.1`。

## 3. 失败 3 — macOS bash 3.2 不支持 `declare -A`

### 3.1 现象

```bash
declare -A RESULTS=( ["foo"]=1 ["bar"]=2 )
echo "${RESULTS[foo]}"
# 输出: 2  (错误!应该是 1)
```

bash 3.2 把 `["foo"]` 当算术求值为 `0`,把 `RESULTS[0]=1` 覆盖成 `RESULTS[0]=2`(来自 `["bar"]`)。`RESULTS[foo]` 也索引到 `0`,所以输出 `2`。

### 3.2 根因

macOS 默认 bash 是 3.2.57(GPLv2,Apple 不愿切 GPLv3)。bash 4+ 才支持 `declare -A` 关联数组。

### 3.3 修复

用平行普通数组 + 索引查找:

```bash
SCRIPT_NAMES=( "validate_skill" "verify-all" )
SCRIPT_CMDS=( "python3 scripts/validate_skill.py ." "python3 scripts/verify-all.sh ." )
declare -a EXIT_CODES  # 普通数组

for i in "${!SCRIPT_NAMES[@]}"; do
    name="${SCRIPT_NAMES[$i]}"
    output=$(eval "${SCRIPT_CMDS[$i]}" 2>&1)
    exit_code=$?
    EXIT_CODES[$i]="$exit_code"  # 立即捕获 $!,避免 echo 覆盖
done

for i in "${!SCRIPT_NAMES[@]}"; do
    code="${EXIT_CODES[$i]:-?}"  # 兜底
    echo "$name: $code"
done
```

### 3.4 相关陷阱

- `grep -c` 在无匹配时返回 `0` 加 exit code 1,`$?` 在 pipe 中会被覆盖 — 用 `${var:-0}` 兜底
- `set -u` 在关联数组未定义时触发,即使有 `:-` 兜底也未必生效 — bash 3.2 推荐**不启用** set -u

## 4. 配套记录

| 文件 | 内容 |
|---|---|
| `references/file-hygiene.md` 铁律 8.6 | 动态变量协议正确做法 |
| `references/file-hygiene.md` 铁律 8.7 | bash 3.2 兼容约束 |
| `scripts/render-version.sh` 头部注释 | 占位符永不渲染原则 |
| `references/changelogs/v3.5.1-changelog.md` | 修正版发布记录 |
| `references/known-gaps.md` | 已知 bash 3.2 限制 |

## 5. 下次重蹈预防

任何下次实现"动态变量替换"类功能时,必读本 pitfall + file-hygiene 8.6/8.7。