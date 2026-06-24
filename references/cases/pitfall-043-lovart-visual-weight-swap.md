---
reference_id: PITFALL-043
title: Lovart 视觉权重互换 / 精度数字丢失
category: cases
used_when:
  - STEP-13 DesignIR 写出后
  - STEP-15 prompt 编译后
  - Lovart 出图后
  - 用户对比 prompt vs image 时
called_by:
  - image-critique.md
  - end-to-end-workflow.md
  - ai-ceiling-breaking.md
depends_on:
  - PITFALL-019
  - PITFALL-026
  - PITFALL-039
outputs:
  - failure_pattern
  - empirical_observation
---

# Pitfall 043: Lovart 视觉权重互换 / 精度数字丢失

> **版本**: 1.0
> **日期**: 2026-06-23
> **触发**: 跑 brief-1 户外露营灯 baseline 出图 (Lovart Nano Banana Pro 1K),发现 A/B 方向视觉互换,C 方向所有 0.05mm 精度数字全部视觉化不了
> **严重级别**: 🔴 高(直接影响出图质量,且与 pitfall-026/039 不重叠)

---

## 问题描述

**Lovart 视觉权重分配是黑盒**:即便 prompt 写得极其精确(STEP-13 DesignIR + STEP-15 6 组代码块 + 共享视觉语言 header),Lovart 也会:
1. **在不同方向之间互相"借"视觉特征**(鹅卵石的钛灰铝合金 + 5 道棱线跑到水滴那张图上)
2. **系统性丢失所有 < 1mm 的精度数字**(0.05mm 间隙、0.1mm 棱线过渡、Ra 1.6 粗糙度全部消失)
3. **退回到最简单原型**(鹅卵石扁度 0.41 的比例被 Lovart 自动改成更简单的"上尖下圆水滴")

**核心结论**:
- SKILL.md 写得再精确,**不能**保证 Lovart 按 prompt 来
- 改 SKILL.md 的边际收益 < 换模型的边际收益
- 这跟 pitfall-039 "AI 天花板 4-5/10"是**两个独立失败模式**:039 是"AI 表达不出",043 是"AI 表达得跟 prompt 不一样"

## 实证数据

### Brief-1 露营灯 9 张 baseline 出图(2026-06-23)

| 方向 | prompt 描述 | Lovart 实际渲染 | 关键丢失 |
|---|---|---|---|
| **A 鹅卵石-棱线** | 92×64×38mm 钛灰 6061-T6 铝合金,5 主棱线 + 12 次棱线,Ra 1.6 微磨砂,IPX7 | **沙黄硅胶水滴型,无棱线,USB-C 居中,挂绳孔 + 麻绳,底部柔光带** | CMF 错(硅胶非金属)、棱线 0/5 + 0/12、IPX7 不可见、Ra 1.6 不可见、磁吸不可见 |
| **B 水滴-嵌槽** | 78×58×58mm 食品级硅胶 RAL 1001 沙黄,2.5mm 壁厚,内胆 6063 铝,8° 自立 | **钛灰铝合金鹅卵石,5 道棱线清晰,顶面圆形触控,侧面嵌槽,底部柔光** | CMF 错(金属非硅胶)、B 拿到了 A 的视觉特征 —— 视觉互换 |
| **C 禅石-磁吸三模块** | 主 72×56×56 / 副 48×36×36 / 信标 36×24×24,钛灰铝 + 黄铜嵌件,3 处 NdFeB 磁吸,模块间隙 0.05mm 平齐 | **三块禅石,每块黑砂石 + 黄铜环,中间暖光带,比例 1:0.67:0.5** | 0.05mm 模块间隙不可见、Qi 无线充电不可见、磁感应唤醒不可见、信标 30 天待机不可见 |

### 三个数字的"非表达率"

| 精度维度 | prompt 中数字 | Lovart 表达 | 非表达率 |
|---|---|---|---|
| 长宽比 1.44 / 扁度 0.41 | A | 上尖下圆,接近正圆 | 100% 丢失 |
| 0.1mm 棱线倒角 | A | 无任何棱线 | 100% 丢失 |
| 0.05mm 模块间隙 | C | 模块拼合可见但间隙不可测量 | 100% 丢失 |
| Ra 1.6 微磨砂 | A | 看起来是"哑光"但无微纹理 | 100% 丢失 |
| 8° 倾斜自立 | B | 不确定是否 8° | 不可测 |
| 1:0.67:0.5 比例 | C | 比例近似正确 | 0% 丢失(粗比例) |

**规律**:**粗比例(数量级)能保,精数字(< 1mm)全丢**。这是 Lovart 视觉权重分配的下限。

### 视觉特征互换率

| 期望位置 | 实际位置 | 互换? |
|---|---|---|
| A 的钛灰铝合金 | B 的渲染结果 | ✓ 互换 |
| A 的 5 道棱线 | B 的渲染结果 | ✓ 互换 |
| A 的 IPX7 隐藏磁吸 | 全部丢失 | ✗ 不是互换,是丢 |
| B 的沙黄硅胶 | A 的渲染结果 | ✓ 互换 |
| B 的 8° 倾斜 | 不确定 | 不可测 |
| C 的三模块 | 保留(因为 C 比较"简单") | 0% 互换 |

**规律**:**两个 prompt 越相似,Lovart 越可能把它们的视觉特征互换**。差异化越强的方向(C 三模块)保留率越高。

## 根因分析

### 1. Lovart Nano Banana Pro 1K 的训练数据权重

- 训练集里"户外露营灯"原型以**水滴型硅胶**为主(Black Diamond Moji / Luci Solar / Snow Peak Hozuki 都是这型)
- "钛灰铝合金鹅卵石 + 5 道棱线"这种组合在训练集里**几乎不存在**
- Lovart 视觉权重分配 = 训练集原型先验,prompt 后验
- 当 prompt 后验跟先验冲突时,Lovart **混合两者的特征**,而不是二选一

### 2. 精度数字的训练数据稀缺

- 训练集图片基本没有"0.1mm 棱线"这种标签
- 视觉权重几乎不为精度数字分配任何激活
- 结果:无论 prompt 怎么强调,精度数字都是"no-op"

### 3. STEP-09 六轴差异门不防 Lovart 视觉混淆

- 六轴差异门是**逻辑差异**(材料 / 工艺 / 颜色 / 形态 / 关系 / 结构)
- Lovart 视觉权重分配基于**视觉特征差异**(轮廓 / 材质 / 比例)
- 逻辑差异 ≠ 视觉差异 → STEP-09 通过 ≠ Lovart 渲染差异化

## 修复方法

### A. Prompt 层面(不能完全解决,但能缓解)

1. **粗化精度数字**:把 0.1mm 棱线 → "fine chamfered edges",0.05mm 间隙 → "flush joinery",让 Lovart 的训练集先验能匹配
2. **强化视觉粗特征**:鹅卵石不要写"扁度 0.41",写"wide and flat, lower than tall",让轮廓权重最高
3. **加 anti-swap guard**(本次 当前版本 改不动,但应记入 当前版本 changelog):在 STEP-09 后加一行 "The three directions must differ on at least one of: silhouette (pebble/water-drop/mushroom), primary material (metal/silicone/composite), or module count (one/two/three+)"
4. **删掉装饰性精度**:Vi 等高线、Ra 粗糙度、0.4mm 壁厚 —— 这些对 Lovart 来说都是 noise

### B. SKILL.md 层面(待)

- 在 STEP-14 加 **AI-renderability 子维度**:对每个方向的"视觉粗特征差异化"打分,粗特征差异不足 = 该方向回 STEP-06 重做
- 在 STEP-15 输出合同里加: **每方向 prompt 必须包含"silhouette 描述句"**作为最优先 token(放 prompt 第一句而非最后)

### C. 工程层面(高于 SKILL.md)

- **换模型**:Midjourney v6 / DALL-E 3 / Flux 1.0 Pro 在粗特征保真度上显著优于 Lovart Nano Banana Pro 1K
- **加 ControlNet**:用轮廓图 / 深度图锁定形态,Lovart 视觉权重分配就被绕开
- **3D 渲染**:Blender + KeyShot,从 3D 模型直接出图,精度数字可在材质里直接控制 —— 这是 pitfall-039 "长期突破方案"中提到的路径

### D. 评审层面(本 pitfall 的硬约束)

- **每个 brief 出图后,必须做 prompt-vs-image 矩阵对比**:prompt 期望的 5 个关键视觉特征 × 实际图像的 5 个视觉特征 → 重合率打分
- **重合率 < 60% = 该方向重做**,不进入后续终结交付步
- 5 维重合率得分写进 STEP-14 评分表,作为第 9 维 "Lovart-renderability"

## 验证方式

### 静态验证(prompt 写作时)

```markdown
- [ ] prompt 第一句是 silhouette 描述
- [ ] 删掉所有 < 1mm 的精度数字
- [ ] 三个方向的 silhouette / material / module-count 至少一个不同
- [ ] 粗特征差异化打分 ≥ 6/10
```

### 动态验证(出图后)

```markdown
- [ ] prompt 5 关键视觉特征 vs 实际图像 5 视觉特征重合率 ≥ 60%
- [ ] 三个方向 silhouette 在人眼可分辨(不靠 vision 工具)
- [ ] 没有任何方向"互换"了另一个方向的特征
```

### 反向验证(对比 039)

```markdown
- 039: AI 表达不出 → 重在"换路径"(3D/ControlNet)
- 043: AI 表达得跟 prompt 不一样 → 重在"换 prompt 粗化"或"换模型"
- 同一图上 039+043 都可能触发,处理顺序:先检查 043(互换 / 丢失)→ 再检查 039(天花板)
```

## 与其他 pitfall 的关系

| Pitfall | 关系 |
|---|---|
| **pitfall-019** (提示词质量反馈必须用真实视觉对比验证) | 上游:043 的发现必须走 019 的"真视觉评审",不能文字评审 |
| **pitfall-026** (outdoor-light-form-cliche) | 邻居:026 是"避开俗套",043 是"避开视觉互换" |
| **pitfall-030** (AI 产品级精度天花板) | 邻居:030 是"精度数字天花板",043 是"精度数字丢失" |
| **pitfall-039** (评审标准虚高陷阱) | 上游:039 写"AI 真实水平 4-5/10",043 写"AI 表达得跟 prompt 不一样" —— 两个独立失败模式 |

## 来源

- **触发事件**: 2026-06-23 baseline brief-1 露营灯 9 张出图(Lovart Nano Banana Pro 1K)
- **触发 skill**: jony-ive-design2me-v2(本轮 baseline)+ skillopt 当前版本
- **沙盒路径**: `~/.hermes/sandboxes/jony-design2me-v2-baseline-2026-06-23/runs/v0-baseline/brief-1-camping-lantern/`
- **决策链 + 6 prompt 原文**: `decision-log/STEP-01-to-15.md` + `prompts/brief-1-three-directions.md`
- **9 张图 SHA + 视觉对比**: `images/`
- **关联 SKILL.md 升级建议**: 当前版本 changelog 待写(本文件)
