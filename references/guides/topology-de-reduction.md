---
reference_id: REF-GUIDE-TDR
title: 几何降维归原协议
category: guides
status: stub
date: 2026-06-24
source: 资深设计流程审计师第二轮反馈(2026-06-24)
one_line: 强制从拓扑几何体出发(球/圆柱/双曲面/莫比乌斯),禁止已知产品形态直接代入
---

# 几何降维归原协议(Stub)

> **⚠️ 本文件为占位 stub,正式内容待补充。**

## 1. 协议意图

模型在 STEP-06 候选生成时,会**直接代入**已知产品形态(鼠标=MX Master 风格、咖啡机=Breville 风格、户外灯=Snow Peak 风格),导致 3 个方向都是同品类经典款的微调。

**降维归原**: 强制从**拓扑几何体**出发(Monolithic Slab / Monocoque Tension Shell / Volumetric Cluster / Lineage Tube),而非已知产品。

这与 `references/cases/pitfall-034-direction-homogenization.md`({{skill_version}} 物理叙事坐标拓扑去同质化断路器)直接对应。

## 2. 触发条件

- STEP-06.3 候选生成前
- brief 含强品类(户外灯/咖啡机/鼠标/无人机/机器人/...)
- 3 个候选方向已倾向同质化(相同材质 + 相同工艺 + 相同结构)

## 3. 最小运行骨架

```
1. 列出 4 个拓扑几何体备选(Monolithic Slab / Monocoque Tension Shell / Volumetric Cluster / Lineage Tube)
2. 每个候选必须从不同拓扑几何体出发
3. 拓扑几何体选定后,再叠加品类功能(用户场景/人体工学/CMF)
4. 禁止在 STEP-06 阶段调用已知产品形态库
```

## 4. 待补内容(占位 TODO)

- [ ] 4 个拓扑几何体的完整定义 + 适用场景
- [ ] 与 `pitfall-034-direction-homogenization.md` 的依赖关系
- [ ] 3 方向拓扑差异门硬约束
- [ ] 实证: 户外灯 / 咖啡机 / 鼠标 拓扑归原案例

## 5. 引用

- 触发案例: `references/cases/pitfall-034-direction-homogenization.md`
- 同批次: `category-metaphor-stripping.md` / `multi-level-composite-locking.md` / `context-sanitation-matrix.md` / `craft-spectrum-palette.md` / `audit-feedback-2026-06-24-prompt-architecture.md`

---

**Stub 生成**: 2026-06-24 by 自动诊断修复。