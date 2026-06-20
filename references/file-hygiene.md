---
reference_id: REF-HYGIENE-001
title: 文件卫生铁律与增量更新规范
category: meta
used_when:
  - SKILL-UPDATE
  - SKILL-REFACTOR
  - FILE-HYGIENECHECK
called_by:
  - skill-router
  - validate_skill.py
depends_on:
  - REF-INDEX-001
outputs:
  - hygiene_compliance_report
---

# 文件卫生铁律与增量更新规范

> **任何触碰 SKILL.md 或 references/ 文件前，必读此文档。**

## 铁律 1：信息分散原则（核心）

**未来运行任何项目后，用户给出的优化建议、更新要求、规则、流程、架构、思维等所有未来可能更新优化的内容，必须存放到对应的文档或文件夹内。不得把优化建议、规则、流程、架构、思维等内容全部记录在同一个文件夹或文档内。特别是除了关键内容外，不得污染 SKILL.md 等核心文件。**

### 具体执行标准

| 内容类型 | 存放位置 | 禁止存放位置 |
|---|---|---|
| 版本升级历史 | `references/changelogs/v{X.Y}-changelog.md` | SKILL.md |
| 详细方法论/反例/失败 | `references/cases/`, `references/rules/`, `references/guides/` | SKILL.md |
| 工作流专项说明 | `references/workflows/{name}.md` | SKILL.md |
| 质量门详细检查项 | `references/quality/*.md` | SKILL.md |
| 设计推导规则 | `references/direction/*.md` | SKILL.md |
| 提示词编译规则 | `references/prompt/*.md` | SKILL.md |
| 文件卫生规则本身 | `references/file-hygiene.md` | SKILL.md |
| 接力口令 | `references/handoff-quick-prompt.md` | SKILL.md |

## 铁律 2：不修改当前任务原则

**用户给出的任何更新要求，没有明确说明"修改当前设计任务""重做""重跑""重新执行""继续该设计"时，不得直接修改当前的设计任务。**

### 默认路由

| 用户指令 | 处理方式 | 禁止行为 |
|---|---|---|
| "优化技能""更新规则""改进流程" | 只修改技能文件，不碰当前项目 | 重跑原项目 |
| "这个设计有问题""方向不对" | 分析反馈，修改技能，不修改当前项目 | 自动修改当前设计 |
| "重做/重跑/重新执行/继续该设计" | 明确授权后，重新运行设计流程 | 在未授权时修改 |
| "出图/绘制/生成图片/渲染" | 明确授权后，进入图片生成 | 自动出图 |

### 歧义处理

当用户说"给出完整的计划""诊断报告""分析""建议"等，**没有**同时说"重做/修改/继续该设计"时：
- 默认进入 **技能优化模式**：分析 → 生成计划 → 修改技能文件 → 交付 handoff 口令
- **不**重新运行原项目的设计流程
- **不**生成新的项目方案或图片
- 只有在用户**追加**"好，现在按这个计划执行"时才切换为设计执行模式

## 铁律 3：SKILL.md 纯执行合同

SKILL.md 只允许以下 6 类内容：

1. **铁律声明**（文件卫生、边界规则）
2. **身份声明**（名称、描述、版本）
3. **Default 15 步启动顺序**（引用指针，不重复正文）
4. **Quality Gate 索引**（1-line 指针到详细检查项）
5. **Output Shapes**（交付格式说明）
6. **Session Prompt BRIEF**（当前会话快速启动）

### SKILL.md 严禁的 9 类内容

1. ❌ 版本历史或升级记录
2. ❌ 详细方法论解释
3. ❌ 失败案例或反例
4. ❌ 超 500 行（当前硬限制）
5. ❌ 重复 references/ 中的正文
6. ❌ 具体产品类型的特殊规则
7. ❌ 图片评审的详细检查清单
8. ❌ 提示词模板或示例
9. ❌ 任何"详细说明""完整解释"类内容

## 铁律 4：版本历史隔离

- **所有版本升级历史 → `references/changelogs/`**
- 0 删除 = MOVE，绝不写回 SKILL.md
- 命名：`v{X.Y}-changelog.md`，不要带 skill 名前缀
- 每个版本独立文件，不合并

## 铁律 5：详细内容下沉

- 详细方法论/反例/失败 → `references/` 各自文件 + 1-line 指针
- SKILL.md 只保留 stub（1-line 链接）
- 任何新发现的 pitfall → `references/cases/pitfall-{N}-{slug}.md`
- 任何新规则 → `references/rules/{name}.md`
- 任何长指南 → `references/guides/{name}.md`

## 铁律 6：双向路由

每个 reference 文件顶部必须有 "When to consult:" header：

```yaml
used_when:
  - TRIGGER-1
  - TRIGGER-2
called_by:
  - CALLER-1
  - CALLER-2
```

实现 Step ↔ Reference 双向路由。

## 增量更新检查清单

任何对 SKILL.md 的 patch / write 前必跑：

- [ ] 读 `references/file-hygiene.md` 6 条铁律
- [ ] 读 SKILL.md「铁律」段 + 「文档路由地图」段
- [ ] 改动属于 6 类允许内容之一？
- [ ] 改动是否在 SKILL.md 已存在某段重复？
- [ ] 改动是否包含版本号 / supersede 链？（→ 改写到 changelogs/）
- [ ] 改完后 SKILL.md 行数不大幅增长（< 10% 浮动）
- [ ] 用户是否明确授权修改当前设计任务？（如未授权，只改技能文件）

### 技能优化模式 vs 设计执行模式

| 模式 | 触发条件 | 行为 | 交付物 |
|---|---|---|---|
| **技能优化** | 用户说"分析""诊断""建议""优化""更新规则" | 只改技能文件，不碰项目 | 修改后的 skill + handoff 口令 |
| **设计执行** | 用户说"重做""重跑""继续该设计""按这个计划执行" | 运行十五步流程 | 3 方向 + DesignIR + 提示词 |
| **歧义** | 用户说"给出完整计划"（未明确执行） | 默认技能优化，等用户追加确认 | 计划 + 口令，不执行 |

## 违规处理

发现违反铁律的内容时：

1. 将违规内容 MOVE 到正确的 reference 文件
2. 在 SKILL.md 中替换为 1-line 指针
3. 在 `references/changelogs/` 中记录此次卫生清理
4. 不删除原始内容（0 删除原则）
