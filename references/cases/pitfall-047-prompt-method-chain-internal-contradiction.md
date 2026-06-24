---
reference_id: REF-CASE-047
title: Pitfall 047 - prompt-engineering.md 内部方法链互相矛盾
category: cases
used_when:
  - PROMPT-COMPILATION
  - PROMPT-REVISION
  - SKILL-UPGRADE-DECISION
called_by:
  - prompt-engineering.md
  - product-level-prompt-revolution.md
  - end-to-end-workflow.md (STEP-15)
depends_on:
  - REF-CASE-019
  - REF-CASE-039
  - REF-CASE-043
  - REF-CASE-046
outputs:
  - method_chain_audit
  - contradiction_resolution_protocol
---

# Pitfall 047 - prompt-engineering.md 内部方法链互相矛盾

> **版本**: 1.0
> **日期**: 2026-06-23
> **触发**: 诊断 jony-ive-design2me-v2 本次升级时,发现 prompt-engineering.md 内部存在**两条互斥的方法链**,且都被 SKILL.md 默认加载
> **严重级别**: 🔴 高(让 agent 跑流程时陷入"听哪条都错"的决策瘫痪)

---

## 1. 触发条件

满足**任一**条件即触发本 pitfall:

| 触发场景 | 表现 |
|---|---|
| Agent 在 STEP-15 编译提示词时同时引用方法 1/2/7/9 和方法 13/14/15 | 不确定该塞精确数字还是删数字,默认走"产品级革命"链路 |
| User 反馈"提示词数字太多 Nano Banana 不读" | agent 想去方法 13 删数字,但又怕违反方法 1/2 的"≥2 个精确数字"硬约束 |
| User 反馈"摄影参数应该放最后" | 方法 7「固定语法结构」+ 方法 9「品牌语境锚定法」都把 Studio photograph 放第一句当锚定词 |
| 同时改 SKILL.md 和 prompt-engineering.md | 改动方向互相抵消 |

---

## 2. 矛盾矩阵(已确认事实诊断)

### 矛盾 1: 精确数字 vs 删数字

| 链路 A(塞数字) | 链路 B(删数字) |
|---|---|
| **方法 1「单材质主导 + 材料精确描述」**: 至少 2 个精确数字(尺寸+角度/曲率) | **方法 13「提示词简化法」**: 删除所有数字(mm/°/ratio/比例),30-50 words |
| **方法 2「基础形态锁定 + 几何精确注入」**: 至少 2 个精确数字 + G2/G1/fillet/chamfer/tangent | **方法 13**: 数字忽略是失效模式,触发条件 >2 个数字 |
| **方法 7「固定语法结构」模板**: 至少 2 个精确数字 | **方法 14「品类锚定法」**: 不得使用数字(mm/°/ratio) |
| **product-level-prompt-revolution.md(整篇"产品级革命"路线)**: 强制 ≥3 个精确尺寸 0.1mm/Ra 1.6/0.05mm | **方法 13**: 这些数字对 Lovart Nano Banana Pro 是"概念覆盖"失效模式的诱因 |

### 矛盾 2: 摄影参数位置

| 链路 A(摄影放第一句) | 链路 B(主体优先) |
|---|---|
| **方法 7「固定语法结构」**: `Studio photograph, [镜头],` 是第一句 | **User 2026-06-23 反馈**: "摄影参数应该放在比较靠后面的位置,一开始的主体应该先描述你要做一个什么东西" |
| **方法 9「品牌语境锚定法」**: "Studio photograph 摄影语法形成固定搭配",且放在产品身份段 | **User 立场**: "先描述整体是什么东西,产品的名称,然后通过风格提示说明风格,再分部件描述" |

### 矛盾 3: 中文 vs 英文主体

| 链路 A(中文主体) | 链路 B(英文精确) |
|---|---|
| **方法 10「中文提示词强制规则」**: 中文为主体,英文仅补充 | **prompt-compression.md 第三方轨道**: 英文主体(Dieter Rams/Bauhaus 锚) |
| **方法 9「品牌语境锚定法」**: LoveFrom 2030 / post-Apple Jony Ive 保留英文 | pitfall-023 实证:"中文版 prompt 直接喂给第三方模型会降级" |

**结论**: 较早期版本起 `PromptBundle` 已经承认这点,正式分了 `production_prompt_lovart`(中文) + `production_prompt_thirdparty`(英文)双轨 —— **矛盾 3 已部分解决**,但矛盾 1 + 2 仍未解决。

---

## 3. 失败表现

| 失败行为 | 真实成本 |
|---|---|
| Agent 默认走"产品级革命"链路(链路 A) | User 看到图全是 < 1mm 数字丢失但仍然塞了 30+ 数字 → "数字太多 Nano Banana 不读"反馈 |
| Agent 走"简化法"链路 B(30-50 words) | User 看到"细节不够 / 功能不明显" → 跟方法 15「功能暗示法」冲突 |
| Agent 同时尝试两边("我要兼容") | 提示词里既塞 0.1mm 又删数字,模型渲染混乱 |

---

## 4. 根因分析

- **方法 1/2/7/9 来源:早期版本 mouse nextgen / coffee maker 失败诊断 mouse nextgen / coffee maker 失败诊断 → 强调"产品级精度"
- **方法 13/14/15 来源:Round 1/2/3 用户评分 1/10 用户评分 1/10 教训 → 强调"删数字 + 品类锚定 + 功能暗示"
- **两条链各自在某个 brief 成功过**,但没合并成单一决策树
- **product-level-prompt-revolution.md 是"产品级革命"路线的独立尝试**,把链路 A 推到极端(< 1mm 精度),但没跟方法 13/14/15 协调
- **pitfall-039 (2026-06-23) 已经实证 Nano Banana Pro 100% 丢 < 1mm 数字** —— 这本该让链路 A 失效,但 SKILL.md 还在执行链路 A

---

## 5. 修复方法(强制协议)

### 协议 A: 模型适配优先决策树(待本次调研后正式定义)

**临时协议**(调研完成前):
1. **先确认目标模型** —— Lovart Nano Banana Pro / Midjourney / DALL-E / Flux 各有不同遵循度
2. **Nano Banana Pro 默认走链路 B**(方法 13/14/15: 30-50 words、删数字、品类锚定)
3. **Midjourney / DALL-E / Flux 可走链路 A**(方法 1/2/7/9 + 精确数字)
4. **product-level-prompt-revolution 的 < 1mm 精度数字** —— 对 Nano Banana Pro 必须**全部剥离**,改成感官描述
5. **摄影参数位置** —— Nano Banana Pro 默认放最后(`Floats. Neutral gradient. Studio photograph, three-quarter view.` 作视觉句号)

**正式协议**(本次调研完成后写进 prompt-engineering.md):
- 删除方法 7「固定语法结构」的硬约束
- 删除方法 9「品牌语境锚定法」的"Studio photograph 第一句"硬约束
- 把方法 1/2/7/9 的精确数字改为「≤2 个 ≥1mm 粗数字,禁 < 1mm」
- 把方法 13/14/15 的「全部删数字」放宽为「< 1mm 必删,≥ 1mm 粗数字可保留 1-2 个」
- 摄影参数位置由 user brief 决定(默认末尾)

### 协议 B: 升级前的内部矛盾审计(必做)

**任何改 prompt-engineering.md / product-level-prompt-revolution.md / cmf-system.md 之前**:

```
[ ] 列出所有方法(方法 1-15)
[ ] 画出方法间的"约束方向"(塞数字 vs 删数字 / 中文 vs 英文 / 摄影前 vs 后)
[ ] 标出冲突对(至少 2 对)
[ ] 给出冲突解决方案(选定一个链路 + 标记另一个为 deprecated)
[ ] 把解决方案写进 changelog,不静默保留矛盾
```

### 协议 C: 不静默保留矛盾(纪律)

**禁止**:
- ❌ 知道两条方法冲突但不解决,默认走一条,声称"兼容"
- ❌ 把矛盾推到 changelog 里说"未来解决" 但不解决
- ❌ 在 prompt-engineering.md 里同时保留两条链路,让 agent 自选

**必须**:
- ✅ 一旦发现矛盾,在 1 个 version 内解决(bump + changelog 必须含解决方案)
- ✅ 解决方案要写进 prompt-engineering.md 的「方法 X: 默认决策树」段
- ✅ 把"为什么废弃另一条"写进 changelog(0 删除原则下,旧方法移到 changelog 或 references/changelogs/)

---

## 6. 验证方式

| 验证项 | 标准 |
|---|---|
| prompt-engineering.md 内部无矛盾对 | grep `方法 1` `方法 13` 看是否指向同一决策方向 |
| 每个 brief 跑 STEP-15 时只用 1 条链路 | 跑 5 个 brief,记录每条 prompt 引用了哪些方法,不应混用 |
| 跟 pitfall-039 / 043 不冲突 | Nano Banana Pro 链路必须跟 039/043 实证一致(0 个 < 1mm 数字) |
| 跟 pitfall-046(调研前置)绑定 | 不解决矛盾 → 不允许 bump SKILL.md |

---

## 7. 实证记录(2026-06-23)

### 诊断过程

User 反馈 3 类同质化(金属拉丝 / 橙色按键 / 暖白灯) + 提示词结构错位 → agent 提出诊断表,发现:
- prompt-engineering.md 方法 1/2/7/9 + product-level-prompt-revolution 强制塞数字 + 摄影第一句
- prompt-engineering.md 方法 13/14/15 强制删数字 + 摄影任意 + 品类锚定
- 两条链路互斥但同时存在
- pitfall-039/043 已实证 Nano Banana Pro 100% 丢 < 1mm 数字 + 互换相似 prompt 视觉特征
- SKILL.md 没强制选哪条链路

**User 选 C: 先做调研,不改 SKILL.md**(2026-06-23 拍板)

### 未完成项(下一版待办)

- [ ] 跑 Nano Banana Pro / 2 实测,确认两条链路各自遵循度
- [ ] 跑 Midjourney / DALL-E 对照,确认矛盾 1 是否跟模型相关
- [ ] 写「模型适配优先决策树」正式方法 16 进 prompt-engineering.md
- [ ] 把方法 7「固定语法结构」+ 方法 9「品牌语境锚定法」中的硬约束改为「默认 / 可覆盖」
- [ ] 改 product-level-prompt-revolution.md 的 < 1mm 精度为「≥ 1mm 粗数字 + 0 个 < 1mm」
- [ ] bump 下一版 + 写 changelog(含本 pitfall + pitfall-046 + 调研结论)

---

## 8. 来源

- jony-ive-design2me-v2/references/guides/prompt-engineering.md (方法 1-15)
- jony-ive-design2me-v2/references/guides/product-level-prompt-revolution.md ("产品级革命"路线)
- jony-ive-design2me-v2/references/cases/pitfall-039 (AI 天花板)
- jony-ive-design2me-v2/references/cases/pitfall-043 (Lovart 视觉互换)
- User 2026-06-23 反馈(3 类同质化 + 提示词结构错位)