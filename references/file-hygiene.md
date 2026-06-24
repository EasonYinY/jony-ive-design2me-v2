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

## 铁律 7：用户原文 0 简化原则（当前版本+）+ 镜像必须含接入（当前版本+）

**当用户要求同步 / 镜像 / 搬运 / 同步更新 任何外部资料库(尤其是用户的 Obsidian 笔记、个人 wiki、v4.x 知识蒸馏等)到技能 references/ 时,必须遵守:**

### 7.1 绝对禁止

| 禁止行为 | 用户原话出处 |
|---|---|
| ❌ "为了精简合并"删字、合段、改写 | 2026-06-22 "不可以有任何 token 焦虑" |
| ❌ "为了控制字符数"简化表达 | 2026-06-22 "不会因为 token 导致的文字描述优化,减少,删减,简化的描述" |
| ❌ "为了文档整洁"调整原文结构 | 2026-06-22 "不要过度优化,简化,和删除" |
| ❌ 注入 frontmatter / 重写 H1 / 改版本号 | "确保原始文字的表达完整,正确" |
| ❌ 喂给 humanizer / AI 润色 | "不要过度优化" |
| ❌ 字节级不一致的"语义化改写" | 用户原话优先于任何内部优化标准 |

### 7.2 必须执行

| 必须行为 | 实施细节 |
|---|---|
| ✅ **字节级精确镜像**(sha256 校验通过) | 用 `shasum -a 256` 双向比对,完全一致才算同步成功 |
| ✅ **保留原文件名 / 子目录结构 / 章节编号** | 原 `00-` / `01-` / `02-` ... `附录U-` 命名**完整保留** |
| ✅ **保留原 frontmatter / 注释块 / ASCII 架构图** | 不删任何注释行、不改 ASCII 图 |
| ✅ **加 KB 内部元数据(README + SHA256SUMS)** | 在镜像目录根加 `README.md`(登记每篇元数据) + `SHA256SUMS.txt`(字节校验) |
| ✅ **KB 内部元数据集中登记,不注入原文** | 28 篇原文 0 改动;元数据写在 KB 根 README |

### 7.3 上游 KB vs 运行 reference 的隔离

当用户外部资料库要落到 `references/` 下时,**禁止**直接合并到现有 `core/` / `design/` / `direction/` 等运行 reference。处理方式:

```
references/
├── core/, design/, direction/, ...  ← 运行知识(自包含,稳定快照)
└── knowledge-base/                  ← 用户原文 KB 镜像(上游参考,字节级镜像)
    ├── README.md                    ← KB 内部总索引(登记每篇元数据)
    ├── SHA256SUMS.txt               ← 每篇 sha256
    └── {原资料库的 28 篇原文镜像}
```

**判定标准**:

| 问题 | 答案 → 处理 |
|---|---|
| 这是技能运行需要的知识吗? | 是 → 落到 `references/core/` 等运行 reference(精简+有 frontmatter) |
| 还是用户的外部参考/输入? | 是 → 落到 `references/knowledge-base/`(字节级镜像) |

### 7.4 验证脚本白名单(必做)

因为用户原文 KB 镜像会包含被运行 reference 规则禁止的字符串(case-study 真实引用如 "LoveFrom 2030"、"V4.x" 版本号、"Mobile Documents" 路径等),必须:

1. **在 `validate_skill.py` 加常量** `UPSTREAM_KB_DIR = "knowledge-base"`
2. **在 markdown_paths 循环里加 skip**:`if rel_posix.startswith(f"references/{UPSTREAM_KB_DIR}/"): continue`
3. **在 `validate_reference_graph.py` 加同样 skip**(在 `_metadata` 调用前过滤)
4. **同步命令必须留底**:在 KB README 写明 `rsync` 命令 + `diff SHA256SUMS` 校验命令

详见 `references/changelogs/当前版本-changelog.md` 的实际案例(28 篇 + 737.2 KB + 0 改动)。

### 7.5 反模式(常见错误)

| 反模式 | 后果 | 正确做法 |
|---|---|---|
| 把 28 篇合并为 3 篇"摘要" | 丢失用户原文,违背 0 简化原则 | 28 篇完整镜像 + 在 KB README 登记元数据 |
| 在原文里加 frontmatter | 改动了原文,不再字节级一致 | frontmatter 写在 KB README 表格里 |
| 把 KB 喂给 STEP-15 提示词编译 | 破坏 prompt-contract 字符边界(90-160 字) | KB 只用于深度背景/教学/写作,不喂给 STEP |
| 镜像后不写 sha256 校验 | 无法验证同步是否完整,下次同步无 baseline | 写 SHA256SUMS.txt,下次 `diff` 校验 |
| 把 KB 内容复制到 `references/core/` 等运行 reference | 污染运行知识(自包含承诺破裂) | KB 与运行 reference 严格分离 |
| **只完成镜像字节搬运,未接入到工作流** | **用户在 Pitfall 040 触发:"新增的内容是否完全被成功引用?"** | **完整三阶段:A 镜像 + B 接入 + C 验证** |

### 7.6 完成定义:三阶段必须全做

**用户说"同步/镜像"≠ 只搬运字节文件。完整任务必须含三阶段:**

| 阶段 | 动作 | 完成定义 |
|---|---|---|
| **A · 镜像** | 字节级复制 + sha256 + 元数据 README | 28/28 sha256 一致 |
| **B · 接入** | 在 SKILL.md 启动顺序 + step-reference-map + end-to-end-workflow + 运行 reference 中加反向链接 | grep `references/<mirror-dir>/` 在 ≥ 5 处出现 |
| **C · 验证** | 跑 validate_*.py,新增失败 = 0 | 失败计数 ≤ baseline |

**只完成 A 而声称"完成"是 Pitfall 040 触发的核心失误**(当前版本 → 当前版本 教训)。

### 7.7 B 阶段 6 个必做动作

1. **SKILL.md 启动顺序**:加 `<mirror 加载 step>`,链接到 mirror README
2. **step-reference-map.md**:mirror 顶层 README 注册为 REF-XXX-ID,加入 3-5 个相关 STEP 行
3. **end-to-end-workflow.md**:每个用到 mirror 内容的上游 STEP 加 `**Mirror 反向链接**:` 块
4. **运行 reference**:每个会查 mirror 内容的 reference(failure-library / ive-thinking-models / aesthetic-gate 等)加 mirror 反向链接段
5. **references/README.md 总索引**:mirror 顶层 README 注册为 `REF-XXX-INDEX` 行
6. **scripts/validate_*.py**:mirror 目录加白名单常量

**反向链接最少数量规则**:mirror N 篇文件至少 N÷3 处反向链接;16-30 篇 ≥ 15 处;30+ 篇 ≥ 25 处。

详见 `references/guides/external-knowledge-mirror-integration.md` 与 `references/cases/pitfall-040-content-added-not-integrated.md`。

## 增量更新检查清单

任何对 SKILL.md 的 patch / write 前必跑：

- [ ] 读 `references/file-hygiene.md` 7 条铁律
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

---

## 铁律 8：User 显式偏好优先级 + 升级后清理协议（2026-06-24 新增）

> **触发**:user 2026-06-24 显式声明 "{{skill_version}} 以上,绝不可能低于这个版本,所有的都是统一一个版本号" + "所有备份都删除"。

### 8.1 升级后版本号统一协议

当 user 显式说"全部统一一个版本号"或类似指令时:

| 步骤 | 动作 |
|---|---|
| 1 | **确认最新版本号**(user 显式指定 ≥ 某数字,如 "{{skill_version}} 以上") |
| 2 | **SKILL.md frontmatter** `version:` 改到最新 |
| 3 | **批量替换 references 里所有版本号引用**(包括白名单元文件 — user 显式指令 > 教学价值保留) |
| 4 | **跳过 `changelogs/` 目录**(每个 changelog 是独立版本叙事,跨版本串会破坏历史) |
| 5 | **跳过 `knowledge-base/` 目录**(用户原文字节级镜像,不可改) |
| 6 | **新建 `references/changelogs/v{new}-changelog.md`** 记录本次升级 |
| 7 | **加白名单**:批量替换会破坏自指文件(如 `scripts/check_version_pollution.py` 第 35 行白名单注释),加到 `ALLOWED_PATHS` |

### 8.2 备份清理协议

当 user 显式说"所有备份都删除"或类似指令时:

| 项 | 处理 |
|---|---|
| `*.bak-{timestamp}` 文件 | **全删**(`find . -name "*.bak-*" -type f -delete`) |
| `*-BACKUP-v*` 副本目录 | **全删**(`rm -rf ../{skill}-BACKUP-*`) |
| BACKUP 路径示例在元 pitfall 文档里 | **保留**(讲历史的文档,但版本号按 8.1 统一改) |
| `.git` 里的版本历史 | **保留**(git 历史 ≠ 文件系统备份) |

### 8.3 User 显式偏好 > 内部一致性最优解

**核心原则**:`user 显式声明 > 铁律 1-7 > skill 内部逻辑最优解`。

当 user 指令与 file-hygiene 铁律冲突时(如批量替换破坏元文件教学价值),**执行 user 指令 + 记录 pitfall**(本协议执行后已在 `references/cases/pitfall-049-bulk-version-replacement-destroys-context.md` 记录)。

### 8.4 与 jony-ive-perspective 无关声明

**user 2026-06-24 显式声明**:"该升级和 jony-ive-perspective 没有任何关系"。

- 本技能的升级、版本号、内容变更**不得**影响 jony-ive-perspective
- jony-ive-perspective 是独立技能(V4.x 系列),本技能是 V3.x 系列
- 跨技能版本号引用(如 `艾维大脑架构 v4.1`)在本技能里**禁止保留**(会被批量替换为当前版本号,但实际破坏语义 — 已在 pitfall-049-B 记录)

### 8.5 检测命令(下次升级前跑)

```bash
# 1. 当前版本号
grep "^version:" SKILL.md

# 2. 备份文件
find . -name "*.bak-*" 2>/dev/null
ls -d ../{skill-name}-BACKUP* 2>/dev/null

# 3. references 里版本号引用数量
grep -rE "v[0-9]+\.[0-9]+(\.[0-9]+)?" references/ --include="*.md" | grep -v "references/changelogs/" | wc -l
```

## 违规处理（保留原段）

发现违反铁律的内容时：

1. 将违规内容 MOVE 到正确的 reference 文件
2. 在 SKILL.md 中替换为 1-line 指针
3. 在 `references/changelogs/` 中记录此次卫生清理
4. 不删除原始内容（0 删除原则）