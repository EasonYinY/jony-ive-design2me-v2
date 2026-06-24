---
reference_id: REF-CASE-027
title: Pitfall 027 — 复杂提示词超时
category: cases
used_when:
  - IMAGE-GENERATION
called_by:
  - prompt-engineering-guide
  - iteration-workflow
depends_on:
  - REF-GUIDE-001
  - REF-CASE-026
outputs:
  - timeout_warning
---

# Pitfall 027 — 复杂提示词超时 (Complex Prompt Timeout)

> **版本**: 1.0
> **日期**: 2026-06-21
> **触发**: Round 2 便携式咖啡机迭代 — 方向B旋转压提示词超时
> **严重程度**: 🔴 高

---

## 现象

提示词长度 > 500 英文词时，Lovart vertex/anon-bob 返回 `final_status: timeout`。

Round 2 方向B（旋转压）提示词约 520 词，生成超时。

---

## 根因分析

### 根因1: 模型Routing层超时

vertex/anon-bob (Nano Banana Pro) 的 routing 层对长提示词处理时间增加，超过默认超时阈值。

### 根因2: 提示词信息过载后要求提示词 ≥ 400 词，但部分产品（如咖啡机）复杂度高，提示词自然膨胀至 500+ 词。

### 根因3: 无Fallback机制

超时后未自动 fallback 到更稳定的模型（如 vertex/nano-banana-2）。

---

## 解决方案

### 策略1: 提示词长度控制

| 产品复杂度 | 建议长度 | 控制方法 |
|-----------|---------|---------|
| 简单（充电器、灯具） | 350-400词 | 标准描述 |
| 中等（音箱、手表） | 400-450词 | 精简交互细节 |
| 复杂（咖啡机、相机） | 300-400词 | 分两次生成 |

### 策略2: 复杂产品分两次生成

**第一次**: 主体形态 + 核心材料 + 摄影语法
**第二次**: 细节补充（交互、接缝、文化杂交）

```bash
# 第一次: 主体
python3 agent_skill.py chat --prompt "[主体描述，200词]" ...

# 第二次: 细节（使用同一thread-id）
python3 agent_skill.py chat --thread-id "$TID" --prompt "[细节补充，150词]" ...
```

### 策略3: 优先级排序

提示词中按优先级排序信息，确保核心信息在前 300 词内：

```
Priority 1 (必须): 形态 + 核心材料 + 尺寸
Priority 2 (重要): 接缝 + 摄影语法
Priority 3 (可选): 文化杂交 + 交互细节
```

### 策略4: 自动Fallback

超时后立即 fallback 到 vertex/nano-banana-2：

```bash
# 第一次尝试
python3 agent_skill.py chat --prefer-models '{"IMAGE":["vertex/anon-bob"]}' ...

# 如果timeout，第二次尝试
python3 agent_skill.py chat --prefer-models '{"IMAGE":["vertex/nano-banana-2"]}' ...
```

---

## 验证方法

在 STEP-15 后，运行以下自检：

```
[ ] 提示词长度 ≤ 450 英文词
[ ] 核心形态描述在前 200 词内
[ ] 如果 > 450 词，已准备分两次生成
[ ] 超时 fallback 方案已准备
```

---

## 关联

- 相关 Pitfall: 026（提示词→图片衰减）
- 相关指南: prompt-engineering.md, dynamic-form-expression.md
- 相关案例: Round 2 便携式咖啡机方向B timeout

---

## 来源

- Round 2 实证: references/iterations/round-2/image-analysis.md
- 日期: 2026-06-21
