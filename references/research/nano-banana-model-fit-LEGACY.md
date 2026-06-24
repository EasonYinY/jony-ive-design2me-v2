---
reference_id: REF-RESEARCH-001-LEGACY
title: Nano Banana Pro / 2 模型能力调研 (Lovart 路由)
category: research
used_when:
  - PROMPT-COMPILATION
  - SKILL-UPGRADE
  - MODEL-SELECTION
called_by:
  - prompt-engineering.md
  - product-level-prompt-revolution.md
  - end-to-end-workflow.md (STEP-15)
  - references/cases/pitfall-039
  - references/cases/pitfall-043
  - references/cases/pitfall-046
  - references/cases/pitfall-047
depends_on:
  - REF-CASE-019
  - REF-CASE-039
  - REF-CASE-043
outputs:
  - model_capability_baseline
  - prompt_follow_through_matrix
  - skill_md_change_recommendations
---

# Nano Banana Pro / 2 模型能力调研 (Lovart 路由)

> **状态**: 🚧 调研进行中(下一版升级目标 升级前置 deliverable,2026-06-23 启动)
> **触发**: User 反馈"生成的图片缺乏泛化性,容易生成雷同的东西"(金属拉丝 / 橙色按键 / 暖白灯) + 提示词结构错位
> **User 显式选项**: "先把 Nano Banana Pro/2 的能力调研写一份 reference 文档(单独 deliverable),等你看懂模型特性再决定 SKILL.md 怎么改"
> **保护**: 调研没完成前禁止 bump SKILL.md(见 pitfall-046 协议 C)

---

## 0. 阅读路径

| 你是… | 必读章节 |
|---|---|
| 想直接知道 SKILL.md 改什么 | § 7 actionable 结论 |
| 想理解 SKILL.md 为什么要这么改 | § 1-§ 6 + § 7 |
| 跑 STEP-15 编译 prompt 的 agent | § 2 提示词遵循度 + § 3 失败模式 |
| 负责 model routing 的 agent | § 1.3 alias 列表 + § 4 跟其他模型对比 |

---

## 1. 模型身份(Lovart 路由)

### 1.1 官方身份

- **模型家族**: Google Gemini 3 Pro Image(Nano Banana Pro)—— 注意:不是 Gemini 2.5 Flash Image(Nano Banana 基础款),Pro 跑在 Gemini 3 Pro Image 架构上,**渲染前有一个 reasoning step(Google 称 "Think Mode")**
- **Lovart catalog 名**: `generate_image_nano_banana_pro`
- **典型用途**: 工业产品渲染(stronger industrial-product rendering)、多参考图合成(最多 14 张)、高质量文字渲染(中/日/韩/西里尔/拉丁)、2K/4K 输出
- **输出**: 最高 4K(Lovart 当前默认 1K)
- **架构层级**: Pro = 推理优化(Think Mode) / Flash(Nano Banana 2) = 速度优化。**两个不是 "同款升级"**
- **catalog 状态**: 2026-05 catalog(2026-05)静态 catalog 列了此模型,但 2026-06-15 注释提到"曾 static catalog 缺失但 live 端点可用"

#### Nano Banana 三层模型对比(不要叫错)

| 别名 | 架构 | 定位 | Lovart 路由 | Free tier |
|------|------|------|-------------|-----------|
| Nano Banana(基础款) | Gemini 2.5 Flash Image | 速度优化,响应式 | (Lovart 默认走 Pro) | Gemini App / AI Studio |
| Nano Banana 2 | Gemini 3.1 Flash Image | 高效率、低延迟、高吞吐 | (Lovart 默认走 Pro) | 50-100 次/天(AI Studio)|
| Nano Banana Pro | Gemini 3 Pro Image + Think Mode | 推理优化、高精度、文字渲染、多图合成 | vertex/anon-bob(本环境实测)| 15-30 次/天(AI Studio)|

### 1.2 Lovart alias

```
nano_banana_pro 主要 alias:
- vertex/anon-bob         ← Lovart skill SKILL.md 当前默认路由(本环境实测)
- vertex/nano-banana-2    ← 同家族 fallback(Lovart SKILL.md 上一版 lovart 升级 注释)
```

### 1.3 调用命令(本环境实测可用,2026-06-23)

```bash
source ~/.lovart/credentials.sh && unset LOVART_BASE_URL && \
python3 ~/.hermes/skills/lovart/scripts/lovart-skill/skills/lovart-skill/agent_skill.py chat \
  --prompt "[提示词]" \
  --prefer-models '{"IMAGE":["vertex/anon-bob"]}' \
  --download --output-dir ~/lovart-out/<brief>-r<N>-d<N>
```

### 1.4 待调研

- [ ] Nano Banana Pro 训练数据截止日期
- [ ] 是否支持 image-to-image / ControlNet(本环境 Lovart 端点是否暴露)
- [ ] 1K vs 4K 输出质量差异(本环境只测过 1K)
- [ ] Nano Banana 2 是否同家族不同 checkpoint(还是独立模型?)

---

## 2. 提示词遵循度(待实测,先用现有 pitfall 数据)

### 2.1 已有实证(来自 pitfall-039 + pitfall-043,2026-06-23 brief-1 露营灯 9 张)

| 提示词维度 | 实际遵循度 | 证据 |
|---|---|---|
| **粗比例** (1:0.67:0.5 数量级) | ✅ 高(0% 丢失) | pitfall-043 C 方向三模块比例近似正确 |
| **粗数字** (≥ 1mm 数量级,如 92×64×38mm) | ⚠️ 中(粗比例对,具体数值偏离) | pitfall-043 A 方向"上尖下圆水滴"vs prompt "扁度 0.41 的鹅卵石" |
| **< 1mm 精度** (0.05mm / 0.1mm / Ra 1.6) | ❌ 100% 丢失 | pitfall-043 实测 4 个 < 1mm 数字全部 no-op |
| **工程材料牌号** (6061-T6 / SUS304) | ❌ 退到训练集先验 | pitfall-043 A "6061-T6 钛灰铝合金"被画成"沙黄硅胶水滴型" |
| **表面处理词汇** (hairline-brushed / anodized / polished) | ⚠️ 部分(只拉到训练集高频词) | 同 pitfall-043:即便 prompt 写 "拉丝",渲染也不一定保留拉丝 |
| **摄影锚词** (Studio photograph + 镜头) | ✅ 高(Lovart 训练集有稳定理解) | 方法 9「品牌语境锚定法」实测,英文摄影语法保留 |
| **品牌语境锚** (LoveFrom 2030 / post-Apple Jony Ive) | ⚠️ 中(风格倾向有效,具体元素不一定) | 现有 prompt-engineering 方法 9 验证 |
| **品类锚定 + 否定默认原型** (方法 14) | ✅ 高 | Round 3 无线充电器 D1=80, D3=82 |
| **文化杂交概念** (方法 6) | ⚠️ 低(AI 退到简单形态) | pitfall-028「纯自然形态天花板」+ pitfall-043 C 三模块 |

### 2.2 失败模式(已实证)

来自 pitfall-043,2026-06-23 实测:

| 失效模式 | 现象 | 触发条件 |
|---|---|---|
| **概念覆盖** | 渲染默认品类原型 | 提示词中出现品类词(mouse/phone/coffee maker) |
| **数字忽略** | 忽略所有 < 1mm 数字 | 提示词中包含 >2 个 < 1mm 数字 |
| **材料简化** | 复杂材料退到训练集高频原型 | 工程材料牌号 + 不常见材料组合 |
| **视觉互换** | 相似 prompt 之间互相借视觉特征 | 三个方向 prompt 越相似,互换率越高 |
| **背景污染** | 背景出现环境元素 | 背景描述不够强烈 |
| **细节抹除** | 精细细节被忽略 | 细节描述 >3 个 |

### 2.3 待调研

- [ ] **0.1mm vs 1mm vs 1cm**: 数字精度阈值具体在哪个量级开始丢?
- [ ] **< 1cm 粗数字** 是否安全(如 92mm / 64mm / 38mm 这种 mm 级整数)还是只有 ≥ 1cm 才稳?
- [ ] **摄影锚词位置**: 放第一句 vs 中间 vs 末尾,遵循度差异?
- [ ] **英文 vs 中文主体**: 哪个遵循度更高? 中文是否必须翻译成英文才能精确匹配?
- [ ] **词数上限**: 现有方法 13 说"30-50 words",实测临界值在哪里?
- [ ] **否定约束** (no logo, no text, no screws): 实测哪些否定有效哪些无效?

---

## 3. 工艺词典遵循度(对应 user 反馈"金属全是拉丝")

### 3.1 假设(待实测验证)

| 工艺词 | 训练集先验密度(假设) | 实际渲染倾向(假设) | 验证状态 |
|---|---|---|---|
| **hairline-brushed / 拉丝** | 🔴 极高(消费电子默认) | 金属件几乎都是拉丝 | ✅ user 反馈实证 |
| **sandblast / 喷砂** | 🟡 中(露营/户外常见) | 可能出现但不主导 | 🔄 待实测 |
| **anodized / 阳极氧化** | 🟡 中(消费电子常见但通常叠加拉丝) | 颜色变,但表面纹理仍是拉丝 | 🔄 待实测 |
| **polished / 镜面抛光** | 🟢 中(高端手表/首饰) | 可能出现,但要 prompt 强约束 | 🔄 待实测 |
| **PVD / Physical Vapor Deposition** | 🟢 低(高端手表/刀具) | 几乎不出现 | 🔄 待实测 |
| **ceramic coating / 陶瓷涂层** | 🟢 低 | 几乎不出现 | 🔄 待实测 |
| **micro-arc oxidation / 微弧氧化** | 🟢 极低(军工/航空) | 几乎不出现 | 🔄 待实测 |
| **electroplating / 电镀** | 🟡 中(首饰/汽车) | 容易跟抛光混淆 | 🔄 待实测 |
| **spray paint / 喷漆** | 🟢 低(汽车/家电) | 容易变成塑料感 | 🔄 待实测 |
| **wood-grain transfer / 木纹转印** | 🟢 低 | 几乎不出现 | 🔄 待实测 |
| **titanium carbonitride / 碳化钛** | 🟢 极低 | 几乎不出现 | 🔄 待实测 |

### 3.2 失败模式推测

- **"高频拉丝"现象**: 模型把 hairline-brushed 当默认高频词,其他工艺被覆盖
- **"塑料感"现象**: 不熟悉的工艺被模型简化成通用塑料材质
- **"组合失败"**: 多个工艺同时描述时,模型只渲染 1 个最强先验

### 3.3 待调研

- [ ] 哪些工艺词在 Nano Banana Pro 训练集里有强激活?
- [ ] 是否能用 `no brushed metal` 等负面约束强制走其他工艺?
- [ ] 3 方向工艺互斥规则,实测能否强制差异化?

---

## 4. 颜色词典遵循度(对应 user 反馈"按键全是橙色")

### 4.1 假设

| 颜色词 | 训练集先验(假设) | 实测状态 |
|---|---|---|
| **orange / 橙色** | 🔴 极高(消费电子 LED 默认) | ✅ user 反馈实证 |
| **warm white / 暖白** | 🔴 极高(家居/灯具默认) | ✅ user 反馈实证 |
| **warm yellow / 暖黄** | 🔴 极高(同暖白) | ✅ user 反馈实证 |
| **cool white / 冷白** | 🟡 中 | 🔄 待实测 |
| **RGB programmable / 可编程 RGB** | 🟢 低(电竞外设) | 🔄 待实测 |
| **monochrome single color / 单色** | 🟢 低(高端) | 🔄 待实测 |
| **dual-tone / 双色** | 🟡 中 | 🔄 待实测 |
| **muted earth tone / 莫兰迪** | 🟡 中(2025 室内设计趋势) | 🔄 待实测 |

### 4.2 失败模式推测

- **"橙色暖白"现象**: 提示词不指定颜色时,模型默认走"消费电子友好"配色
- **"渐变光"陷阱**: 提示词写"LED 灯",模型默认渐变暖白

### 4.3 待调研

- [ ] Nano Banana Pro 是否有 Pantone / RAL 颜色锚词训练数据?
- [ ] 是否支持 hex 颜色代码(如 `#FF6B35`)?
- [ ] 3 方向颜色互斥规则能否强制?

---

## 5. 光感词典遵循度(对应 user 反馈"灯光全是暖白/暖黄,缺长虹玻璃/点阵")

### 5.1 假设

| 光感词 | 训练集先验(假设) | 实测状态 |
|---|---|---|
| **dot matrix LED / 点阵** | 🟡 中(电子表/复古) | 🔄 待实测 |
| **linear light / 线光** | 🟡 中(建筑/汽车内饰) | 🔄 待实测 |
| **changi glass diffuser / 长虹玻璃** | 🟢 低(建筑/室内) | 🔄 待实测 |
| **volumetric light / 体光** | 🟢 低 | 🔄 待实测 |
| **hidden light / 隐藏光** | 🟡 中(高端) | 🔄 待实测 |
| **side-lit / 侧光** | 🟢 低 | 🔄 待实测 |

### 5.2 失败模式推测

- **"暖白暖黄"现象**: 提示词不指定光感时,模型默认走"家居友好"暖色温
- **"点状光"陷阱**: 提示词写 "LED",模型默认单点暖白光,而不是点阵/线性

### 5.3 待调研

- [ ] 哪些光感词在 Nano Banana Pro 训练集里激活?
- [ ] 长虹玻璃 / 点阵 / 线性 这些具体造型能否通过 prompt 强制?
- [ ] 是否需要附 reference image?

---

## 6. 跟其他模型对比(待实测)

| 维度 | Nano Banana Pro | Midjourney v6 | DALL-E 3 | Flux 1.0 Pro |
|---|---|---|---|---|
| 工业产品渲染 | 🟡 中(默认走消费电子) | 🟢 强 | 🟡 中 | 🟢 强 |
| 中文主体遵循度 | 🔴 待实测 | 🟡 中(英文优先) | 🟢 较好 | 🟡 中 |
| 数字精度遵循 | ❌ 100% 丢 < 1mm | 🟢 较好 | 🟡 中 | 🟡 中 |
| 工艺词典多样性 | 🔴 高频拉丝 | 🟢 多样 | 🟡 中 | 🟢 多样 |
| 颜色多样性 | 🔴 默认橙+暖白 | 🟢 多样 | 🟡 中 | 🟢 多样 |
| 摄影锚词遵循 | 🟢 强 | 🟢 强 | 🟢 强 | 🟢 强 |
| ControlNet 支持 | 🟡 Lovart 端点暴露度未知 | ❌ 无 | ❌ 无 | 🟡 部分 |

### 6.1 待调研

- [ ] 跑同一 brief × 4 模型 × 3 方向的 12 张对比图
- [ ] 评估各模型在 5 维度(数字/工艺/颜色/光感/摄影锚词)上的遵循度打分
- [ ] 给出"哪类 brief 适合哪个模型"的决策表

---

## 7. actionable 结论(SKILL.md 改动建议,待调研完成填实)

### 7.1 下一版升级目标 升级必须做的 SKILL.md 改动(已知)

1. **prompt-engineering.md 方法 1/2/7/9 的硬约束改为「默认 / 可覆盖」**
   - 方法 7「固定语法结构」: 摄影参数位置不再 hard-coded 在第一句
   - 方法 9「品牌语境锚定法」: Studio photograph 不再 hard-coded 在产品身份段
2. **product-level-prompt-revolution.md 改 0.1mm 精度为「≥ 1mm 粗数字 + 0 个 < 1mm」**
   - 删除 ≥3 个精确尺寸 0.1mm / Ra 1.6 / 0.05mm 强制要求
   - 改为「≤ 2 个 ≥ 1mm 粗数字(尺寸/比例),0 个 < 1mm」
3. **prompt-word-bank.md § 3 工艺词库从 10 工艺扩到 ≥ 30 工艺**
   - 覆盖喷砂 / 氧化 / 电镀 / 喷漆 / PVD / 微弧氧化 / 喷丸 / 陶瓷涂层 / 木纹转印 / 碳化钛 / 微孔阳极等
   - 加 3 方向工艺互斥硬约束(每方向 1 个独特工艺)
4. **新增 § 3.4 颜色词库 + § 3.5 光感词库**
   - 颜色词库显性 6 色 + 隐性配色
   - 光感词库: 点阵/长虹玻璃/线光/体光/侧光/隐藏光/扫光
   - 3 方向颜色 + 光感互斥硬约束

### 7.2 下一版升级目标 升级可选的 SKILL.md 改动(调研后决定)

- 加「方法 16: 模型适配优先决策树」进 prompt-engineering.md
- 改方法 13/14「全部删数字」为「< 1mm 必删,≥ 1mm 粗数字可保留 1-2 个」
- 新增 pitfall-046 引用到 SKILL.md 升级规范段(本文件已写)

### 7.3 何时不升级(STOP 条件)

- 调研发现 Nano Banana Pro 已经能遵循差异化工艺/颜色/光感 → SKILL.md 现有词典扩充即可,不引入新方法
- 调研发现矛盾是 产品级革命路线(2026-06) 革命遗留问题,跟 Nano Banana Pro 无关 → 撤回 产品级革命路线(2026-06) 革命而不是改 SKILL.md
- 调研发现矛盾真实存在但工程层面无法解决(模型硬限制) → 在 pitfall-039/043 强化,不试图通过 prompt 修补

---

## 8. 调研方法论(自查清单)

每次跑实测前必跑:

```
[ ] 选定 1 个具体 brief(优先用现有 coffee-machine / camping-lantern / drone 之一)
[ ] 准备 prompt A(链路 A: 塞数字 / 摄影第一句) + prompt B(链路 B: 删数字 / 摄影末尾)
[ ] 同一模型(Nano Banana Pro)跑 2 张对比图
[ ] 复制到桌面,vision_analyze 跑事实级视觉评审(只描述差异,不打分,pitfall-019 纪律)
[ ] 记录: 哪些 prompt 维度 A 跟 B 一样,哪些维度 A 跟 B 不一样
[ ] 跨模型跑 Midjourney / DALL-E 对照(如有 API key)
[ ] 写实测结论进 § 2.3 / § 3.3 / § 4.3 / § 5.3 / § 6.1
[ ] 更新 § 7 actionable 结论
[ ] user 拍板后才动 SKILL.md
```

---

## 9. 来源(待补充)

- ✅ Lovart models.md(models catalog + 2026-06-15 nano_banana_pro 注释)
- ✅ Lovart SKILL.md 上一版 lovart 升级(vertex/anon-bob 路由 + vertex/nano-banana-2 fallback)
- ✅ pitfall-039 (Nano Banana Pro 4-5/10 AI 天花板)
- ✅ pitfall-043 (Lovart 视觉权重互换 + < 1mm 数字 100% 丢失)
- 🔄 待调研: Google Gemini 2.5 Flash Image 官方文档
- 🔄 待调研: Midjourney v6 / DALL-E 3 / Flux 1.0 Pro 对照
- 🔄 待调研: Nano Banana 2 是否同家族
- 🔄 待调研: PromptHero / Lexica 等社区 prompt 工程博客

---

## 10. 关联 pitfall 索引

| Pitfall | 跟本调研的关系 |
|---|---|
| **pitfall-019** | 视觉评审纪律:本调研的实测必须用真视觉评审,不文字评审 |
| **pitfall-039** | 上游:本调研必须验证 Nano Banana Pro 4-5/10 AI 天花板结论是否仍成立 |
| **pitfall-043** | 上游:本调研必须验证 < 1mm 数字丢失 / 视觉互换结论是否仍成立 |
| **pitfall-046** | 本调研本身:pitfall-046 要求"升级前必须先有模型调研",本文件就是该 pitfall 的实证 deliverable |
| **pitfall-047** | 本调研的发现会触发:SKILL.md 内部方法链矛盾诊断 + 解决方案 |

## 10.5 联网调研补强 · 来自 8 个权威源的"下一版升级目标 决策底座"

(本段由 2026-06-23 联网调研补强,在本地 pitfall 实证之上叠加官方文档共识。SKILL.md 改动建议必须能同时解释这两套证据。)

### 10.5.1 Google 官方提示词终极公式

> Google Cloud Ultimate Prompting Guide(2026-03-05,官方)**原文**:
>
> **Formula:** `[Subject] + [Action] + [Location/context] + [Composition] + [Style]`
>
> "When starting with a blank canvas, you are the director. **A simple list of keywords won't cut it; you need to describe the scene narratively.**"

### 10.5.2 Google Blog "7 Tips"(Nano Banana Pro 专项,2025-11-20)

官方提示词结构(顺序固定):
1. Subject —— 主体(具体:"a stoic robot barista with glowing blue optics")
2. Composition —— 构图
3. Action —— 动作
4. Location —— 场景
5. Style —— 风格

**Camera/Lighting 在 Subject 之后,不在第一句**。

### 10.5.3 ppl.studio 5-Part Framework(1000+ 张产品摄影实测)

> "Every high-performing product photo prompt has five parts in this order: **subject, action, environment, camera, style**. Mixing the order confuses the model. Skipping a part gives you generic results."
>
> "Always name a lens — **'50mm at f/1.8'** is the single most effective modifier for making AI photos look like photos."
>
> "In practice, **40–80 words is the sweet spot**. Below 40 you are under-specifying. Above 100 you are usually contradicting yourself."

### 10.5.4 官方已知限制 + 社区实测

| 限制 | 来源 |
|------|------|
| Small text / fine details / accurate spellings may not work perfectly | Google Blog 官方 |
| 10-20% 概率完全忽略 prompt 和 reference images | Google AI Developers Forum(2025-12 至今未修)|
| "Too many constraints can backfire",写得像 creative director 而非 tag-soup | QuestStudio 评测 |
| Photorealism 在 complex real-world systems / messy wiring / small mechanical details 有 artifact | QuestStudio |

### 10.5.5 关键决策结论(供 user 拍板 下一版升级目标 用)

| 维度 | 联网调研共识 | 本地 pitfall 实证 | SKILL.md 必须改 |
|------|-------------|----------------|---------------|
| 提示词结构 | Subject 在第一句,Camera 在末尾 | 方法 7 把摄影参数放第一句,违反官方 | § 7.1.1 必须改 |
| 提示词长度 | 40-80 words sweet spot | 方法 13 强制 30 words,过短 | § 7.2 必须改 |
| 数字精度 | Pro 100% 丢 < 1mm 是官方明示下限 | pitfall-039/043 实测验证 | § 7.1.2 必须改 |
| 摄影锚词 | 放末尾而非第一句 | 方法 9 把 LoveFrom 锚放第一句 | § 7.1.1 必须改 |
| 工艺词典 | 训练集决定先验,词库需 ≥ 30 + 互斥 | user 反馈"金属全是拉丝" | § 7.1.3 必须改 |
| 颜色词典 | 同上,3 方向互斥 | user 反馈"按键全是橙色" | § 7.1.4 必须改 |
| 光感词典 | 同上,3 方向互斥 | user 反馈"灯光全是暖白" | § 7.1.4 必须改 |

### 10.5.6 来源清单(8 个权威源,跨平台交叉)

1. Google Cloud Ultimate Prompting Guide(2026-03-05)— 官方 https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana
2. Google Blog 7 Tips for Nano Banana Pro(2025-11-20)— 官方 https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/
3. Google AI for Developers image generation overview — 官方 https://ai.google.dev/gemini-api/docs/image-generation
4. Google Developers Blog Introducing Gemini 2.5 Flash Image — 官方 https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/
5. Lovart Nano Banana 2 vs Pro(2026-01-26)— 平台官方 https://www.lovart.ai/blog/nano-banana-2-vs-pro
6. ppl.studio Product Photo Prompts Guide — 第三方实战 https://ppl.studio/blog/gemini-nano-banana-product-photo-prompts-guide
7. QuestStudio Nano Banana Pro Review(2026-01-07)— 第三方评测 https://queststudio.io/blog/nano-banana-pro-review
8. Google AI Developers Forum — 官方论坛 https://discuss.ai.google.dev/t/nano-banan-pro-ignoring-prompt-and-reference-images/112781

---

| 阶段 | 完成定义 | 当前状态 |
|---|---|---|
| **A · 调研骨架** | 5 节 + 调研方法论 + actionable 段 | ✅ 2026-06-23 完成(本文件) |
| **B · 实测数据** | § 2.3 / § 3.3 / § 4.3 / § 5.3 / § 6.1 全部填实 | 🔄 进行中 |
| **C · user 拍板** | user 看完调研,明确回复"按建议改" | ⏳ 等待 |
| **D · 应用升级** | bump 下一版升级目标 + 1 个 changelog | ⏳ 等待 C |