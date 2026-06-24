---
reference_id: REF-CASE-046
title: Pitfall 046 - 技能升级前未做模型能力调研,事实底座缺失
category: cases
used_when:
  - SKILL-UPGRADE
  - PROMPT-ENGINEERING-REVISION
  - MODEL-CAPABILITY-CHANGE
called_by:
  - SKILL.md (技能升级规范段)
  - prompt-engineering.md
  - end-to-end-workflow.md
depends_on:
  - REF-CASE-019
  - REF-CASE-039
  - REF-CASE-043
outputs:
  - model_research_protocol
  - upgrade_facts_first_rule
---

# Pitfall 046 - 技能升级前未做模型能力调研,事实底座缺失

> **版本**: 1.0
> **日期**: 2026-06-23
> **触发**: 用户反馈"生成的图片缺乏泛化性,容易生成雷同的东西"(金属全是拉丝/按键全是橙色/灯光全是暖白),后续 user 在本次升级选项中**显式选择**: "先把 Nano Banana Pro/2 的能力调研写一份 reference 文档(单独 deliverable),等你看懂模型特性再决定 SKILL.md 怎么改"
> **严重级别**: 🔴 高(直接违反用户"无视觉证据不升级"红线,且会让 SKILL.md 改错方向)

---

## 1. 触发条件

满足**任一**条件即触发本 pitfall:

| 触发场景 | 反例 |
|---|---|
| 改 SKILL.md 的 prompt-engineering 方法 / product-level-prompt-revolution 硬约束 / cmf-system 词典 | 没先确认目标模型(Nano Banana Pro / 2 / Midjourney / DALL-E / Flux)能读懂这些约束 |
| 改某品类的工艺词典/颜色词典/光感词典 | 没查模型训练集里这些工艺/颜色/光感的实际分布(可能"喷砂"在训练集里比"拉丝"还稀) |
| 改提示词结构(摄影参数位置 / 数字密度 / 描述顺序) | 没确认模型对结构重排的实际遵循度 |
| 改 pitfall-XX 触发的修复方法 | 没确认修复方法的 prompt 写法对模型实际生效 |

---

## 2. 失败表现

| 失败行为 | 真实成本 |
|---|---|
| 凭直觉改 prompt 约束(如"禁止 < 1mm 数字")但不验证模型实际是否读 | 改完无效,user 再反馈"还是一样",返工 |
| 改 SKILL.md 时反过来用上一轮"产品级革命"的"产品级革命"数字塞法回应 user 反馈"数字太多" | 走向 user 反对方向,bump 失败 |
| 工艺/颜色词典只基于 designer 主观词汇,不查模型训练先验 | 词典里的词在训练集里根本不存在,模型继续走默认原型 |
| 把"调研"挂在嘴上但不交付具体文档 | user 必须反复追问,信任度崩塌 |

---

## 3. 根因分析

- **SKILL.md 是"上层规范"**,模型能力是"下层事实"。上→下制定规范不验证下层 = 规范悬空
- **agent 倾向"立刻给出解决方案"** —— user 反馈"全是拉丝",agent 想立刻补词典,但词典本身有没有效要看模型
- **现有 skill 已有 pitfall-039 (AI 天花板 4-5/10) + pitfall-043 (Lovart 视觉权重互换)** 已实证"Nano Banana Pro 不读 < 1mm 数字 / 互换相似 prompt 视觉特征",但 prompt-engineering.md 同时仍保留方法 1/2「精确数字 ≥2 个」+ product-level-prompt-revolution 「强制 0.1mm 精度」—— **内部矛盾,根源就是没把模型调研结论回流到 prompt 约束**
- **pitfall-019 (无视觉证据不升级)** 是"出图侧"的纪律;**本 pitfall-046 是"调研侧"的对称纪律** —— 升级前必须先有事实底座(模型能力文档)

---

## 4. 修复方法(强制协议)

### 协议 A: 升级前置调研(必做)

**任何 SKILL.md / prompt-engineering / cmf-system / product-level-prompt-revolution 的实质性改动前,必须先有** `references/research/{model-name}-model-fit.md` **文档,包含**:
1. **模型身份**: 架构家族 / 训练截止日期 / 已知替代 alias(如 `vertex/anon-bob` = Nano Banana Pro)
2. **能力上限**: 最高分辨率 / 支持的尺寸 / 多模态能力
3. **提示词遵循度**: 实测哪些类型约束生效、哪些失效(数字精度 / 摄影锚词 / 工艺词典 / 颜色 / 光感 / 部件关系)
4. **失败模式**: 与现有 pitfall 对照(039/043 的 Nano Banana Pro 结论是否仍成立,有没有新发现)
5. **可操作结论**: SKILL.md 哪些规则应该保留/废弃/改造,带 1-2 行 actionable bullet

### 协议 B: 调研来源要求

至少交叉 3 类来源:
1. **官方文档 / changelog**(权威但滞后)
2. **第三方 benchmark / prompt 工程博客**(实践侧)
3. **本 skill 历史 pitfall / 迭代记录**(本环境实证,最高优先级)

**禁止**: 只查官方文档就下结论(Lovart 模型 catalog 已经滞后过 —— `nano_banana_pro` 曾缺席 static catalog 但 live 端点可用,见 models.md 2026-06-15 注释)

### 协议 C: 调研 ↔ SKILL.md 隔离

**调研没完成前**:
- ✅ 允许:新增 pitfall 记录"内部矛盾"或"流程缺失"
- ✅ 允许:写调研文档骨架(标题/目录/已知事实/未知项)
- ❌ 禁止:bump SKILL.md frontmatter version
- ❌ 禁止:改 prompt-engineering / cmf-system / product-level-prompt-revolution 的硬约束
- ❌ 禁止:写 changelog 声称已升级

**调研完成后**:
- ✅ 一次性应用调研结论到 SKILL.md + references/(1 个 bump + 1 个 changelog,符合上一版 file-hygiene 协议)

---

## 5. 验证方式

| 验证项 | 标准 |
|---|---|
| 调研文档存在 | `references/research/{model}-model-fit.md` 文件存在且 ≥ 5 节 |
| 交叉来源 ≥ 3 类 | 文档里明确标注来源类别 |
| 对照现有 pitfall | 至少引用 039/043 之一 |
| actionable 结论 | 文档末尾有「SKILL.md 改动建议」段(即使该段写"暂无") |
| user 拍板 | 在改 SKILL.md 之前,user 必须明确回复调研文档已读 |

---

## 6. 实证记录(2026-06-23)

### 触发事件

User 反馈 3 类同质化失败:
1. 金属件**几乎清一色拉丝** —— 喷砂/氧化/电镀/喷漆等工艺几乎不出现
2. 按键/功能键**几乎清一色橙色**
3. LED 灯**几乎清一色暖白/暖黄** —— 缺长虹玻璃/点阵/线光等特征造型
4. 提示词结构问题 —— 摄影参数堆前面,部件不分,数字过多

Agent 提出 4 选项让 user 拍板:
- A 直接按计划升级下一版
- B 先做对照实验有视觉证据再改
- C **先做模型能力调研,等 user 看懂再改** ← user 选这个
- D 其他方向

User 原话(2026-06-23):"先把 Nano Banana Pro/2 的能力调研写一份 reference 文档(单独 deliverable),等你看懂模型特性再决定 SKILL.md 怎么改 —— 调研文档放 references/research/nano-banana-model-fit.md"

### 跟其他 pitfall 的关系

| Pitfall | 关系 |
|---|---|
| **pitfall-019 (无视觉证据不升级)** | 邻居:019 是"出图侧"纪律,046 是"调研侧"纪律,两者构成完整的"事实先行"协议 |
| **pitfall-039 (AI 真实水平 4-5/10)** | 上游:046 的调研必须引用 039 的 Nano Banana Pro 天花板结论 |
| **pitfall-043 (Lovart 视觉权重互换)** | 上游:046 的调研必须验证 043 的"< 1mm 数字丢失/相似 prompt 视觉互换"是否仍成立 |
| **pitfall-034/035 (方向/惊喜同质化)** | 平行:034/035 是"agent 选择方向"层面,046 是"模型能否渲染差异化"层面 |
| **pitfall-044 (eagle publish not automatic)** | 不冲突 |

---

## 7. 来源

- User 原话 2026-06-23 启动本次升级会话时的反馈
- User 显式选项 C 选择 2026-06-23
- 现有 pitfall-019 / 039 / 043 实证数据
- Lovart models.md 注释(nano_banana_pro 在 static catalog 滞后)

---

## 8. SKILL.md 升级规范段必跑清单(本 pitfall 衍生)

任何对 SKILL.md 的 prompt / cmf / prompt-engineering 实质性改动前:

```
[ ] 1. 读 references/research/nano-banana-model-fit.md(或对应目标模型的调研文档)
[ ] 2. 读 pitfall-019 / 039 / 043(确认约束仍生效)
[ ] 3. 调研文档 ≥ 5 节 + 交叉来源 ≥ 3 类
[ ] 4. user 已明确回复"调研看完了,按建议改"
[ ] 5. 改动属于 file-hygiene 铁律 5(详细内容下沉到 references/)
[ ] 6. 1 个 version bump + 1 个 changelog(不要散乱改多个文件)
```