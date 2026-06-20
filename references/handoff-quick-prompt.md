---
reference_id: REF-HANDOFF-001
title: 新窗口快速接力口令
category: meta
used_when:
  - NEW-SESSION
  - TASK-HANDOFF
  - SKILL-RESUME
called_by:
  - user-command
  - skill-router
depends_on:
  - REF-INDEX-001
  - REF-PROCESS-001
  - REF-HYGIENE-001
outputs:
  - handoff_plan
---

# 新窗口快速接力口令

## 口令（复制粘贴到新窗口）

```
/handoff jony-ive-design2me-v2
```

或完整版：

```
加载 skill jony-ive-design2me-v2，读取 references/handoff-quick-prompt.md，按以下 5 步检查并恢复任务上下文：
```

## 5 步检查流程

### Step 1: 环境验证

- [ ] 确认 `~/.hermes/skills/creative/jony-ive-design2me-v2/` 存在
- [ ] 运行 `python3 scripts/validate_skill.py .` 通过
- [ ] 运行 `python3 scripts/validate_reference_graph.py .` 通过
- [ ] 运行 `python3 scripts/contracts.py` 15 项测试通过

### Step 2: 读取铁律

- [ ] 读取 `references/file-hygiene.md` — 确认 6 条铁律 + 2 条新增规则
- [ ] 确认当前任务是"技能优化"还是"设计任务执行"
- [ ] 确认用户是否明确授权修改当前设计任务

### Step 3: 读取 Reference 总索引

- [ ] 读取 `references/README.md` — 确认 29+ 个 reference 文件清单
- [ ] 确认新增文件已纳入索引（file-hygiene.md, handoff-quick-prompt.md, changelogs/）

### Step 4: 读取主流程

- [ ] 读取 `references/process/end-to-end-workflow.md` — 四阶段十五步
- [ ] 读取 `references/process/step-reference-map.md` — 步骤引用映射
- [ ] 读取 `references/process/reasoning-output.md` — 用户可见输出合同

### Step 5: 恢复任务上下文

- [ ] 询问用户当前任务状态（新设计 / 技能优化 / 继续之前）
- [ ] 如用户要求继续之前任务，询问具体断点（STEP-XX / 哪个方向）
- [ ] 如用户要求技能优化，读取 `references/file-hygiene.md` 确认不修改当前设计任务

## 快速验证命令

```bash
cd ~/.hermes/skills/creative/jony-ive-design2me-v2
python3 scripts/validate_skill.py /Users/easoneason/.hermes/skills/creative/jony-ive-design2me-v2
python3 scripts/validate_reference_graph.py .
python3 -c "import sys; sys.path.insert(0, 'scripts'); from contracts import *; print('contracts OK')"
```

## 文件变更速查（最近修改）

| 文件 | 变更类型 | 日期 |
|---|---|---|
| `references/changelogs/README.md` | 新增 | 2026-06-20 |
| `references/changelogs/v1.0.0-changelog.md` | 新增 | 2026-06-20 |
| `scripts/validate_skill.py` | 修改（+1 REQUIRED_REF） | 2026-06-20 |
| `references/process/step-reference-map.md` | 修改（+REF-PROCESS-004） | 2026-06-20 |
| `references/process/skill-reading-guide.md` | 修改（+STEP-01, +step-reference-map） | 2026-06-20 |
| `references/file-hygiene.md` | 新增 | 2026-06-20 |
| `references/handoff-quick-prompt.md` | 新增 | 2026-06-20 |
