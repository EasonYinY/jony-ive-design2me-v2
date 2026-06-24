---
reference_id: REF-GUIDE-CSP
title: 工艺色谱协议
category: guides
status: stub
date: 2026-06-24
source: 资深设计流程审计师第二轮反馈(2026-06-24)
one_line: 颜色的 4 元素分解(基础色+表面工艺+反射+触觉),禁止单色词替代完整色彩意图
---

# 工艺色谱协议(Stub)

> **⚠️ 本文件为占位 stub,正式内容待补充。**

## 1. 协议意图

传统提示词只用"基础色"(深空灰 / 哑光黑 / 香槟金),丢失工艺感。

**4 元素分解**:
1. **基础色**: hex / Pantone / NCS
2. **表面工艺**: 阳极氧化 / PVD / 喷砂 / 拉丝 / 镜面抛光 / 微弧氧化
3. **反射**: 漫反射 / 镜面反射 / 弱反射 / 哑光吸光
4. **触觉**: 磨砂 / 顺滑 / 颗粒 / 织物纹理 / 木材纹理

每个候选必须 4 元素**显式全填**,而不是只给基础色。

## 2. 触发条件

- STEP-09 CMF 系统(`REF-DESIGN-003`)
- STEP-15 提示词编译的 CMF 段
- 任何"想要高级感"的 brief

## 3. 最小运行骨架

```
1. 基础色: 选 hex 值 + Pantone 编号
2. 表面工艺: 选 1 种主工艺 + 1 种次工艺(如 阳极氧化主 + 喷砂次)
3. 反射: 漫反射率 5-90% 区间,显式给值
4. 触觉: 1 个形容词(磨砂/顺滑/...),允许工艺反推
```

## 4. 待补内容(占位 TODO)

- [ ] 4 元素的工程参数映射(漫反射率/光泽度单位/粗糙度 Ra)
- [ ] 5 类材料的工艺色谱参考(铝/钛/钢/陶瓷/木材)
- [ ] 3 方向工艺色谱差异化门
- [ ] 实证: 户外灯 / 鼠标 / 咖啡机 工艺色谱对比

## 5. 引用

- 同批次: `category-metaphor-stripping.md` / `multi-level-composite-locking.md` / `context-sanitation-matrix.md` / `topology-de-reduction.md` / `audit-feedback-2026-06-24-prompt-architecture.md`

---

**Stub 生成**: 2026-06-24 by 自动诊断修复。