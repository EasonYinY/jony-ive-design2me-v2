---
reference_id: REF-CASE-049-B
title: Pitfall 049-B — 批量版本号替换破坏跨技能引用和步骤描述里的版本号
category: cases
date: 2026-06-24
supersedes_id_was: REF-CASE-049
disambiguation_note: 原 REF-CASE-049 与 pitfall-049-skill-version-cleanup.md 冲突,本文件分配 -B 后缀。官方权威 REF-CASE-049 = 技能版本清理(由 README 登记)。
type: skill-repair-trap
supersedes_id_was: N/A (new pitfall)
used_when:
  - SKILL-UPGRADE
  - VERSION-POLLUTION-FIX
  - FILE-HYGIENE-BULK-EDIT
called_by:
  - skill-optimizer
  - file-hygiene-check
depends_on:
  - REF-HYGIENE-001
  - REF-CASE-048
outputs:
  - bulk_edit_safety_protocol
---

# Pitfall 049: 批量版本号替换破坏跨技能引用和步骤描述里的版本号

> **日期**: 2026-06-24
> **触发**: 2026-06-24 jony-ive-design2me-v2 自动诊断修复。check_version_pollution.py 报 45 处版本号污染,执行 `re.sub(r'v\d+\.\d+(\.\d+)?(-\w+)?', '本技能当前版本', line)` 批量替换,**破坏了 5 类合法上下文**。
> **严重级别**: 🟠 HIGH for any bulk-edit skill-upgrade 操作
> **触发关键词**: 看到 "check_version_pollution" 报 N 处污染时,本能反应是 sed/python 批量替换 — **先读完此 pitfall**

## 1. 现象(5 类被破坏的合法上下文)

| # | 上下文 | 示例 | 破坏后果 |
|---|---|---|---|
| 1 | **跨技能版本号引用** | `基于艾维大脑架构 {{skill_version}} 的方法` | 替换成 `本技能当前版本` 后,**跨技能引用失效**({{skill_version}} 是另一个技能的版本) |
| 2 | **步骤描述里的版本号** | `STEP-06.3 [NEW · 2026-06-24 {{skill_version}}]` | 替换后丢失步骤的版本标注 |
| 3 | **引用其他文件的版本后缀** | `pitfall-034-direction-homogenization.md {{skill_version}}` | 替换成 `pitfall-034-direction-homogenization.md 本技能当前版本`,读者不知道这个文件哪个版本 |
| 4 | **BACKUP 路径里的版本号** | `jony-ive-design2me-v2-BACKUP-{{skill_version}}-20260624-134945` | 替换后路径变成 `BACKUP-本技能当前版本-134945`,**教学价值归零** |
| 5 | **脚本自身白名单注释里的版本号** | `scripts/check_version_pollution.py` 第 35 行注释 `本脚本自身白名单注释含 {{skill_version}}` | 替换后白名单本身缺字面字符串,自指破坏 |

## 2. 根因

**批量替换无法区分"违规引用"和"合法引用"** — 两类都是 `v\d+\.\d+` 模式字面相同。

## 3. 修复协议(防下次重蹈)

### 3.1 **优先方案**: 加白名单(本技能已用)

```python
# check_version_pollution.py
ALLOWED_PATHS = {
    SKILL_ROOT / "SKILL.md",
    # 元 pitfall / 案例 / 指南 文件本身讲特定版本号的故事
    SKILL_ROOT / "references" / "cases" / "pitfall-048-backup-skill-illusion.md",
    SKILL_ROOT / "references" / "cases" / "pitfall-049-skill-version-cleanup.md",
    # ... 按需扩展
}
```

加白名单比批量替换更安全,因为白名单**只豁免文件级**,不破坏任何字面字符串。

### 3.2 **必须方案**(即使走批量替换): 替换前**先逐文件分类**

| 文件类型 | 处理 |
|---|---|
| 引用其他技能的版本号 | **跳过**,保留原样 |
| 引用具体文件版本的元 pitfall | **跳过**,保留原样 |
| 元 changelog / handoff 文件 | **跳过**,保留原样 |
| 业务规则文件里的版本号 | **替换** + 加白名单 |
| 脚本自指白名单注释 | **跳过**,保留原样 |

### 3.3 **替换后必跑** 三类验证

1. `grep -rn "本技能当前版本" references/ SKILL.md` → 必须为 0
2. `python3 scripts/check_version_pollution.py .` → 必须 0 处污染
3. **人工抽查 5 个引用,确认没破坏语义**

## 4. 决策矩阵

| 替换目标 | 用批量替换? | 替代方案 |
|---|---|---|
| `vX.Y.Z` → 移除 | ❌ | 加 ALLOWED_PATHS 白名单 |
| `vX.Y.Z` → 模糊引用("本技能当前版本") | ⚠️ 仅当配合白名单 + 替换后验证 | 直接保留,加白名单 |
| `vX.Y.Z` → 真实数字 | ✅ | 替换前先用 grep 列清单,逐文件审批 |

## 5. 实战案例(本次 session)

**修复**: 批量替换 45 处后,破坏 5 处合法上下文:
- `pitfall-034-direction-homogenization.md` 的 `艾维大脑架构 {{skill_version}}`(其他技能版本)
- `process/end-to-end-workflow.md` 的 `STEP-06.3 {{skill_version}}`(步骤描述)
- `process/step-reference-map.md` 的 `REF-CASE-034 {{skill_version}}`(引用文件版本)
- `pitfall-048-backup-skill-illusion.md` 的 `BACKUP-v1.1.0-...`(BACKUP 路径)
- `scripts/check_version_pollution.py` 自指注释

**回滚**: 逐文件 patch 恢复原字面 + 把这 5 个文件加进 ALLOWED_PATHS 白名单。

**最终**: 0 处污染,无任何破坏。

## 6. 引用

- 同批次: `pitfall-048-backup-skill-illusion.md`(BACKUP 路径里的版本号也是合法上下文)
- 协议铁律: `references/file-hygiene.md` 铁律 4(版本历史隔离 — 但**只禁止写回 SKILL.md**,允许 reference 内使用)
- 关联 pitfall: `pitfall-047-prompt-method-chain-internal-contradiction.md`(改文档前的内部矛盾审计精神同样适用 — 改 reference 前先看上下文)