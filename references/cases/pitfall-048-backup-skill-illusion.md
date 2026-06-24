---
reference_id: REF-CASE-048
title: Pitfall 048 - BACKUP 副本里的"升级"是错觉(2026-06-23 飞行器任务实证)
category: cases
date: 2026-06-23
type: operational-trap
used_when:
  - SKILL-UPGRADE
  - BACKUP-DETECTION
called_by:
  - skill-router
  - file-hygiene-check
depends_on:
  - REF-CASE-030
  - REF-RULE-VSN-001
outputs:
  - backup_skill_illusion_pattern
---

# Pitfall 048: BACKUP 副本里的"升级"是错觉

> **日期**: 2026-06-23
> **触发**: 飞行载人器具任务 + 第三方 AI 审计反馈后,用户要求"整体更新 skill"并 bump version 到 v3.0.0。我(agent)在 BACKUP 副本目录 `jony-ive-design2me-v2-BACKUP-v1.1.0-20260621-134945-BACKUP-v1.1.1-20260621-150429` 中完成了完整 v3.0.0 升级,但**真实 skill 路径 `creative/jony-ive-design2me-v2/` 仍处于 v2.9.0 状态**——BACKUP 副本不代表当前 skill。
> **严重级别**: 🔴 BLOCKER(任何 skill 升级的实际效果)
> **与既有 pitfall 的关系**: 扩展 `pitfall-030-skill-name-ambiguity.md`(只警告"路径歧义"),本 pitfall 进一步说明"路径歧义导致**升级错觉**"。

## 1. 现象

### 1.1 BACKUP 副本命名规则

用户在多次 skill 升级/试验时,常会保留历史快照作为 backup:

```
~/.hermes/skills/creative/
├── jony-ive-design2me-v2/                                    # 真实 skill
├── jony-ive-design2me-v2-BACKUP-v1.1.0-20260621-134945/        # 备份
└── jony-ive-design2me-v2-BACKUP-v1.1.0-20260621-134945-BACKUP-v1.1.1-20260621-150429/  # 嵌套备份
```

BACKUP 后缀模式: `BACKUP-<旧版本号>-<时间戳>[-BACKUP-<更旧版本号>-<时间戳>]`

### 1.2 agent 误判路径

**典型错误**: agent 接到"整体更新 skill"指令时,如果工作目录碰巧是 BACKUP 副本路径(或 terminal/cd 默认进入该目录),agent 会在 BACKUP 副本里**完整地做完所有升级动作**:
- 改 SKILL.md frontmatter version
- 改 references/ 下的多个文件
- 跑验证脚本(通过,因 BACKUP 副本自身一致)
- 输出"v3.0.0 升级完成"报告

**但**: 真实 skill 路径下,SKILL.md 仍是 `version: 2.9.0`,所有 `references/` 修改都落到了**历史快照**,不是当前 skill。

### 1.3 静默性

这是**最危险**的失败模式:
- agent 不报错
- 验证脚本不报错(BACKUP 副本自身是自洽的)
- 用户**直到下次重开 skill 才可能发现**"咦,v3.0.0 没生效?"
- 浪费 1+ 小时的实际工作

## 2. 失败根因

### 2.1 命名歧义(`pitfall-030` 已记录)
`skill_view(name="jony-ive-design2me-v2")` 报"Ambiguous skill name":3 skills match。

### 2.2 agent 选错路径
agent 通常**挑选**默认 name,但 BACKUP 副本和真实 skill 的 name 字段完全相同,无法区分。

### 2.3 验证脚本不跨目录检查
`validate_skill.py` / `check_version_consistency.py` 只检查**当前目录**内部一致性,不验证"我的修改是否落到了真实 skill 路径"。

## 3. 修复方法

### 3.1 升级前必跑路径确认(2026-06-23 新增硬约束)

```bash
# 强制 3 步检查
ls /Users/easoneason/.hermes/skills/creative/jony-ive-design2me-v2/SKILL.md
# 必须存在,且 frontmatter version 字段存在

# 用 skills_list 确认默认 skill 路径
skills_list
# 输出会有 <skill> 标记,**真实 skill 不带 BACKUP 后缀**

# 用 skill_view 时传完整路径
skill_view(name="creative/jony-ive-design2me-v2")
# 而不是 skill_view(name="jony-ive-design2me-v2")
```

### 3.2 升级动作前的"路径四问"

每次对 SKILL.md / references/ 写动作前,agent 必须确认 4 件事:

1. **我现在的工作目录是哪里?** `pwd` 或 `ls SKILL.md`
2. **真实 skill 路径是什么?** `/Users/easoneason/.hermes/skills/creative/jony-ive-design2me-v2/`
3. **当前目录是 BACKUP 副本吗?** 路径中是否含 `BACKUP`?
4. **如果含 BACKUP,我要不要切到真实路径?**

### 3.3 验证脚本增强建议(待落地)

`check_version_consistency.py` 加第 7 项检查:

```python
def check_no_backup_illusion(skill_root: Path) -> Tuple[List[str], List[str]]:
    """检测当前路径是否在 BACKUP 副本目录中(避免升级错觉)。"""
    errors: List[str] = []
    path_str = str(skill_root.resolve())
    if "BACKUP" in path_str:
        errors.append(
            f"当前 skill_root 包含 'BACKUP' 路径:{path_str}\n"
            f"BACKUP 副本是历史快照,在其中做的任何升级都**不会**生效到真实 skill。\n"
            f"请切换到真实 skill 路径(如 /Users/easoneason/.hermes/skills/creative/jony-ive-design2me-v2/)后重新执行。"
        )
    return errors, []
```

## 4. 触发条件

- 任何 SKILL.md frontmatter 修改
- 任何 references/ 目录新增/修改/删除
- 任何 scripts/ 目录新增/修改
- 任何 changelogs/ 新增 changelog
- 任何 `version:` 字段 bump

## 5. 验证方式

1. **路径确认**: 升级前 `pwd` 输出**不含** "BACKUP" 字样
2. **真实 skill 验证**: 升级后 `cat /Users/easoneason/.hermes/skills/creative/jony-ive-design2me-v2/SKILL.md | head -5` 显示新的 version 字段
3. **脚本增强**: `check_version_consistency.py` 第 7 项检查通过

## 6. 失败码(可被脚本拒绝)

| 失败码 | 描述 | 严重性 |
|--------|------|--------|
| `backup_skill_illusion.detected` | 当前 skill_root 在 BACKUP 副本中 | 🔴 BLOCKER |
| `backup_skill_illusion.path_mismatch` | 工作目录与真实 skill 路径不一致 | 🔴 BLOCKER |

## 7. 与既有 pitfall 的关系

- **Pitfall 030 (技能名称歧义)**: 上游。本 pitfall 是其**更严重后果**——歧义不仅导致 `skill_view` 失败,更导致**升级错觉**。
- **Pitfall 025 (升级前先改技能)**: 互补。本 pitfall 加一层"BACKUP 副本里改 = 没改"。
- **Rule VSN-001 (版本号单一来源)**: 一致。真实 skill 的 version 字段才是权威,BACKUP 副本里的 version 字段不算。

## 8. 实证(2026-06-23)

我(agent)在 `jony-ive-design2me-v2-BACKUP-v1.1.0-20260621-134945-BACKUP-v1.1.1-20260621-150429/` 完整执行了"v3.0.0 升级":
- SKILL.md `version: 2.9.0` → `3.0.0`
- 新增 3 个规则文件(rule-014/015/016)
- 新增 `references/changelogs/v3.0.0-changelog.md`
- 强化 `scripts/contracts.py` 占位符检测
- 新增 `scripts/check_step_compression.py`
- 全部 4 个验证脚本通过

但**真实 skill 路径** `~/.hermes/skills/creative/jony-ive-design2me-v2/` **完全没动**——仍处于 v2.9.0 状态。所有"v3.0.0 升级"工作等价于 0。

**用户实际看到的状态**: 真实 skill 仍是 v2.9.0,且 v2.9.0 已经包含大量升级(知识蒸馏库 / Pitfall 040-047 / 模型适配协议等),BACKUP 副本的"v3.0.0"反而**落后**于真实 skill 的实际状态。

## 9. 教训

### 9.1 给 agent
- **永远先 `pwd` 再升级**
- **永远用完整分类路径** `creative/jony-ive-design2me-v2`,不用 bare name
- **BACKUP 副本 = 历史快照,只读**,不在其中做写动作

### 9.2 给 skill 设计
- 任何 skill 升级工具都应**先验证路径不在 BACKUP 副本中**
- `check_version_consistency.py` 应加 backup_illusion 检测(见 §3.3)
- 用户应**清理** BACKUP 副本,避免歧义

### 9.3 给用户
- BACKUP 后缀命名策略**应**包含日期+序号(`BACKUP-2026-06-23-01` 而非 `BACKUP-v1.1.0`)
- 或用 `.snapshot/` 目录统一管理
- 或用 git/mercurial 做版本控制而非目录备份

## 10. 来源

- 2026-06-23 飞行载人器具任务 + 第三方 AI 审计
- 用户指令"整体更新 skill" + "整个技能只能有一个版本号"
- 我(agent)在 BACKUP 副本执行"v3.0.0 升级"的工作流
- `skill_view` 报"Ambiguous skill name"3 skills match
- 后续 `skill_view(name="creative/jony-ive-design2me-v2")` 显示真实 skill 仍 v2.9.0
