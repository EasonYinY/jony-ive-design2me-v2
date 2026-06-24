---
reference_id: PITFALL-063
title: 复杂工业系统原型丢失（Complex System Archetype Loss）
category: cases
triggered_by:
  - 用户审计报告 2026-06-24（联影医疗MRI设计）
  - 重型设备/复杂系统/精密仪器/医疗设备的工业设计任务
  - 产品被误判为建筑/家具/雕塑/抽象几何体
used_when:
  - STEP-05（核心矛盾提炼后）
  - STEP-06（候选生成前）
  - STEP-15（提示词编译阶段）
  - 审美质量门 STEP-12（原型拓扑检查）
called_by:
  - end-to-end-workflow STEP-05.7
  - end-to-end-workflow STEP-15.6
  - aesthetic-gate 第十二项
  - archetype-verification.md
related_to:
  - PITFALL-060（去品牌化与功能可读性）
  - PITFALL-061（材料职责违反）
  - PITFALL-055（尺度事实名实分离）
  - PITFALL-024（形态优先失败）
  - PITFALL-011（关系先于形态）
  - REF-GUIDE-ARCHETYPE（行业原型锚定验证）
---

# 复杂工业系统原型丢失（PITFALL-063）

> **版本**: 1.0
> **日期**: 2026-06-24
> **触发**: 用户审计报告（联影医疗干磁体3T核磁共振设备设计）
> **严重级别**: 🔴 CRITICAL — 导致产品无法识别，完全丧失品类语义

---

## 现象（Symptoms）

当设计 Brief 属于**重型设备 / 复杂系统 / 精密仪器 / 医疗设备**时，工作流可能产生以下症状：

| 症状 | 示例（MRI 案例） | 后果 |
|------|----------------|------|
| **产品无法识别** | 生成图像被识别为"建筑微缩模型"或"高档家具" | 失去品类语义，设计失败 |
| **形态物神崇拜** | 将 MRI 筒状结构肢解为"石板"和"环" | 切断与品类原型的联系 |
| **功能虚无** | 表面无丝印、无 UI、无刻度、无警告标签 | 失去工业精密感与信任基础 |
| **材料错配** | 使用洞石(travertine)、胡桃木(walnut)描述超导磁体外壳 | 违背材料职责，引发尺度漂移 |
| **尺度崩塌** | "两个平行板"让模型迷惑是建筑外墙还是桌面硬盘 | 人体尺度参照丢失 |

---

## 根因分析（Root Causes）

### 根因 1：形态物神崇拜（Form Fetishism）

**错误思维**：将物体简化为方和圆就是 Jony Ive 风格。

**正确路径**："产品是关系，不是物体"。医疗设备的本质是"机器对恐惧身体的温柔包裹与精准探测"。外壳的几何必须为了支撑这种关系而存在，不可为了追求极简而切断与品类原型的联系。

> 艾维证据：Moncler 合作款（2024）保留了马灯的提手与光源拓扑；Linn LP12 保持了方形底座与圆盘。"熟悉但非怀旧"的前提是用户必须一眼认出这是一个什么。

### 根因 2：虚无主义极简（Nihilistic Minimalism）

**错误思维**：教条执行"无字、无螺丝、无标签"，切断一切细节。

**正确路径**："关怀不被看见的部分（Caring about the unseen）"。在 Christie's rostrum（2026）和 Linn LP12 中，细节（倒角、接缝、微型铭牌）被用作确立"制造精度"和"用户信任"的触觉/视觉节点。医疗器械的警告标签和丝印应当被视为**神圣的图形秩序规范**，而非视觉噪声。

> 艾维证据：Moncler 合作款 Button 内侧精细刻印了 LoveFrom logo；Apple Watch 表冠刻度；精细电子底部的全文本激光雕刻。信息并未被删除，而是通过极其严苛的字体排印和材料微雕，使其成为产品本体的一部分。

### 根因 3：质感贴图依赖（Texture Map Dependency）

**错误思维**：缺乏材料的工程职责认知，只追求视觉的高级感。

**正确路径**："[material] for [specific function]"。材料必须支撑功能的诚实。重型干磁体3T设备的外壳应该使用"微米级哑光喷涂的工程复合材料，用以提供绝对的屏蔽感与洁净度"，而非套用奢侈家具的木石词汇。

---

## 触发条件（Trigger Conditions）

以下任一条件触发时，必须运行原型锚定门：

- [ ] Brief 包含"医疗"、"工业"、"精密"、"重型"、"扫描"、"检测"等词汇
- [ ] 产品具有强物理限制（电磁屏蔽、结构刚性、热管理）
- [ ] 产品需要用户躺入/操作/围绕（人体尺度参照必需）
- [ ] 产品具有复杂内部结构（超导线圈、真空腔、光学路径）
- [ ] 产品需要法规合规标签（FDA、CE、ISO）

---

## 防御协议（Defense Protocol）

### 协议 A：行业原型锚定门（STEP-05.7）

在核心矛盾提炼后、候选生成前，强制注入：

1. **定义不可缩减三大形态特征**
   - 示例（MRI）：①扫描舱体(Bore Cavity) ②检查床与轨道(Patient Cradle Track) ③整体屏蔽外壳(Monolithic Enclosure)
   - 示例（无人机）：①动力臂拓扑 ②中央机身核心 ③光学传感器舱

2. **验证视觉权重**
   - 第一特征 > 40% 总体积
   - 第二特征 > 20% 总体积
   - 第三特征 > 30% 总体积

3. **定义功能暗示词**（至少 3 个）
   - MRI → patient cradle, scanning bore, superconducting magnet
   - 无人机 → propulsion arm, rotor hub, aerial sensor
   - 咖啡机 → brew group, steam wand, portafilter

4. **计算尺度校验公式**
   ```
   [净尺寸需求] + [结构厚度容差] + [安全防护边界] = [最终输出数值]
   ```

### 协议 B：高秩序工业细节加载（STEP-15.7）

针对复杂工业系统，禁止产品表面"绝对虚无"。引入三级细节加载：

**① 认知状态指示层（Cognitive State UI）**
```
措辞：Flush-integrated micro-typographic control zones embedded seamlessly 
into the surface. High-density micro-perforated dynamic display flush with 
the outer skin, exhibiting no decorative ornament when dormant.
```

**② 法律与工程信任标签（Regulatory & Engineering Veracity）**
```
措辞：Sub-millimeter laser-etched scale markings, warning typography, and 
functional indicators aligned to a strict engineering grid, maintaining 
absolute typographic restraint.
```

**③ 制造工艺接口（Manufacturing Interface Detail）**
```
措辞：0.3mm tight engineering gaps, flawless structural split-lines serving 
as functional division of materials, precise parting lines showing 
uncompromising manufacturing rigor.
```

### 协议 C：材料职责诚实性（STEP-15.8）

- ❌ 禁止：travertine, walnut, marble, bamboo, rattan 用于重型设备外壳
- ✅ 必须：工程复合材料、高刚性合金、医用级高分子
- ✅ 必须：指定具体工业精加工工艺（bead-blasted, anodized, passivated）
- ✅ 必须：材料承担功能职责（电磁屏蔽 / 结构刚性 / 热管理 / 生物相容性）

### 协议 D：提示词编译检查（STEP-15.6 子项）

1. **品类锚定词**：提示词第一段必须包含明确的品类锚定词（如 MRI scanner）
2. **禁止纯几何替代**：严禁用 slab/cube/cylinder/ring 完全替代行业原型词
3. **功能暗示词**：至少包含一个功能暗示词
4. **尺度锚定**：包含显性尺寸和人体参照

---

## 修复路径（Recovery Path）

当原型拓扑检查失败时：

1. **立即暂停**：不要继续生成图片或编译提示词
2. **退回 STEP-05.7**：重新运行行业原型锚定门
3. **检查 `archetype-verification.md`**：验证不可缩减三大特征
4. **重新编译提示词**：确保品类锚定词和功能暗示词
5. **替换材料**：将建筑/家具材料替换为工程材料
6. **添加细节层**：至少添加一个三级细节层
7. **重新运行审美质量门**：确认第十二项原型拓扑检查通过

---

## 历史案例

| 案例 | 日期 | 产品 | 失败模式 | 修复措施 |
|------|------|------|----------|----------|
| 联影医疗MRI | 2026-06-24 | 干磁体3T核磁共振 | 原型丢失为"石板/环/双板" | 新增 STEP-05.7 + STEP-15.7 + STEP-15.8 |
| 无人机设计 | 2026-06-XX | 四旋翼飞行器 | 动力臂被简化为"圆盘" | 新增原型锚定门（动力臂拓扑保护） |
| 咖啡机设计 | 2026-06-XX | 意式浓缩咖啡机 | 冲泡组被简化为"按钮" | 新增功能暗示词（brew group, steam wand） |

---

## 与其他 Pitfall 的关系

| Pitfall | 关系 | 区别 |
|---------|------|------|
| PITFALL-060 | 共同防御"去品牌化过度" | PITFALL-060 聚焦品牌词污染；PITFALL-063 聚焦品类原型丢失 |
| PITFALL-061 | 共同防御"材料错配" | PITFALL-061 聚焦材料职责；PITFALL-063 聚焦材料引发的原型漂移 |
| PITFALL-055 | 共同防御"尺度错误" | PITFALL-055 聚焦尺寸名实分离；PITFALL-063 聚焦尺度引发的品类误判 |
| PITFALL-024 | 共同防御"形态优先" | PITFALL-024 聚焦关系先于形态；PITFALL-063 聚焦形态不能切断原型 |
| PITFALL-011 | 共同防御"关系缺失" | PITFALL-011 聚焦关系命题；PITFALL-063 聚焦关系不能替代原型识别 |

---

## 来源

- 审计报告：2026-06-24 联影医疗MRI设计审计（用户提交）
- 核心病灶：产品无法识别为医疗设备，被误判为建筑/家具
- 根因分析：缺乏行业原型锚定，纯几何替代切断了品类语义联系
- 艾维案例：Moncler合作款（保留马灯提手）、Linn LP12（保留方形底座与圆盘）、Christie's rostrum（微型铭牌确立精度）
- 升级触发：用户反馈"完全看不出是何物"
- 技能文件升级：v3.5.3-changelog.md（2026-06-24）
