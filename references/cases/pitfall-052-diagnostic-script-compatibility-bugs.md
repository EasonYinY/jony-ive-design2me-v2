---
reference_id: REF-CASE-052
title: Pitfall 052 — 诊断脚本兼容性与字符串匹配 3 类隐性 bug
category: cases
date: 2026-06-24
type: diagnostic-trap
supersedes_id_was: N/A (new pitfall)
used_when:
  - SKILL-AUDIT
  - VALIDATION-SCRIPT-DEBUG
  - VERSION-POLLUTION-FIX
called_by:
  - skill-optimizer
  - file-hygiene-check
depends_on:
  - REF-HYGIENE-001
  - REF-CASE-049-B
outputs:
  - diagnostic_bug_checklist
---

# Pitfall 052: 诊断脚本兼容性与字符串匹配 3 类隐性 bug

> **日期**: 2026-06-24
> **触发**: jony-ive-design2me-v2 {{skill_version}} 升级 + 全量诊断修复时,跑了 4 个验证脚本,3 个暴露"看似脚本逻辑正确但实际 bug 严重"的隐性陷阱。
> **严重级别**: 🟡 MEDIUM for SKILL-AUDIT 流程
> **触发关键词**: 写新的 shell 脚本 / 改 frontmatter 解析 / 加白名单逻辑 / 改路径判断 — 每次都要跑这 3 类检查

## 1. 三类隐性 bug 总览

| # | bug 类型 | 触发条件 | 修复成本 | 实测脚本 |
|---|---|---|---|---|
| 1 | **bash 3.2 不支持 `declare -A` 关联数组** | macOS 默认 bash 是 3.2.57(2007 GPLv2) | 低(改用普通数组 + 索引) | `scripts/verify-all.sh` 第一次跑 exit code 全报 0 但显示 ✅ 全部通过(实际有失败) |
| 2 | **frontmatter category 单复数不匹配** | 文件写 `category: cases`,脚本判断 `file_category == "case"` | 低(改为 `in {"case", "cases"}`) | `validate_skill.py` 误报 pitfall-043/034 等含版本号 |
| 3 | **`_is_changelog_path` 不识别 `references/changelogs/` 前缀** | 路径以 `references/` 开头,但函数只检查裸 `changelogs/` | 低(加 2 行 `or` 判断) | `validate_skill.py` 误报 `v1.3.1-changelog.md` |

## 2. 详细 bug 复盘

### Bug 1: bash 3.2 `declare -A` 不可用

**症状**:
```bash
declare -A RESULTS
RESULTS[foo]=1
echo "${RESULTS[foo]:-MISS}"  # 输出 "2"(bar 的值,不是 foo)
```

**根因**:bash 3.2 把 `RESULTS[foo]=1` 解释为 `RESULTS[0]=1`(`foo` 被算术求值 = 0),所有 key 都映射到同一个 index。

**验证**:
```bash
bash -c 'declare -A RESULTS; RESULTS[foo]=1; RESULTS[bar]=2; echo "${!RESULTS[@]}"'
# bash 3.2: 输出 "0"
# bash 4+: 输出 "foo bar"
```

**修复**:用平行普通数组 + 索引:
```bash
NAMES=("validate_skill" "audit" ...)
CODES=()  # 按索引存
for i in "${!NAMES[@]}"; do
    CODES[$i]=$(...)
done
for i in "${!NAMES[@]}"; do
    echo "${NAMES[$i]}: ${CODES[$i]}"
done
```

**检测命令**:`bash --version | head -1` 看是否含 "version 3"。

### Bug 2: category 单复数

**症状**:`pitfall-043` 等文件 frontmatter 写 `category: cases`,但脚本判断 `file_category == "case"`(单数)→ 不匹配 → 没豁免 → 误报版本号。

**根因**:历史文件 category 命名不一致(有的 `case` 有的 `cases`),脚本硬编码单数。

**修复**:
```python
if file_category in {"case", "cases"}:  # 双形式都接受
    continue
```

**检测命令**:
```bash
grep -rh "^category:" references/ --include="*.md" | sort -u
```

### Bug 3: changelog 路径前缀缺失

**症状**:`validate_skill.py` 报 `v1.3.1-changelog.md 含版本口令`,但该文件在 `references/changelogs/` 下(白名单目录),应该豁免。

**根因**:`_is_changelog_path` 只检查 `changelogs/` 前缀(裸的),不检查 `references/changelogs/`(skill 标准化布局)。

**修复**:
```python
def _is_changelog_path(path, root):
    rel = path.relative_to(root).as_posix()
    return (
        rel.startswith("references/changelogs/")
        or rel.startswith("changelogs/")
        or rel.startswith("references/iterations/")
        or rel.startswith("iterations/")
    )
```

**检测命令**:
```bash
# 跑 validate_skill 看是否有 changelogs/ 下的误报
python3 scripts/validate_skill.py . 2>&1 | grep "changelog"
```

## 3. 检测三件套(下次写脚本前跑)

```bash
# 1. bash 版本
bash --version | head -1

# 2. frontmatter category 命名一致性
grep -rh "^category:" references/ --include="*.md" | sort -u

# 3. 路径白名单覆盖度
python3 -c "
from pathlib import Path
import re
files = list(Path('references').rglob('*.md'))
patterns = ['changelogs', 'iterations', 'knowledge-base', 'cases/README.md', 'latest-changelog.md']
uncovered = []
for f in files:
    rel = f.as_posix()
    if not any(p in rel for p in patterns):
        if re.search(r'v\d+\.\d', f.read_text()[:200]):  # frontmatter 含版本号
            uncovered.append(rel)
print('Files with version in frontmatter but no whitelist:', uncovered)
"
```

## 4. 防御原则

| 原则 | 说明 |
|---|---|
| **写完脚本先在老环境跑一次** | macOS 默认 bash 3.2 + Python 3.11 是最小公分母 |
| **grep category 别只看一个值** | 用 `sort -u` 看完整命名空间 |
| **白名单覆盖两个布局** | `references/X/` 和 `X/`(历史布局可能共存) |
| **路径判断用 `as_posix()`** | 避免 Windows 反斜杠差异 |
| **关联数组改普通数组** | bash 3.2 兼容 |

## 5. 引用

- 修复记录: `references/changelogs/{{skill_version}}-changelog.md` §2
- 上游 pitfall: `pitfall-049-B-bulk-version-replacement-destroys-context.md`(批量替换暴露了这些 bug)
- 铁律 4: `references/file-hygiene.md` 版本历史隔离(脚本白名单 = 这类 bug 的修复机制)