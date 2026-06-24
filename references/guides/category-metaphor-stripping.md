---
reference_id: REF-GUIDE-CMS
title: 品类隐喻剥离与纯粹动作解耦协议
category: guides
status: stub
date: 2026-06-24
source: 资深设计流程审计师第二轮反馈(2026-06-24)
one_line: 强品类 brief 强制剥离"手柄/扳机"等部件名词,先推导纯粹动作再映射回造型
---

# 品类隐喻剥离与纯粹动作解耦协议(Stub)

> **⚠️ 本文件为占位 stub,正式内容待补充。**
> **触发**: 2026-06-24 资深设计流程审计师第二轮反馈中提出。
> **指针完整**: README 中已登记 `REF-GUIDE-CMS`,运行引用不会断链。
> **下一步**: 用户后续任务触发该协议时,按下方"最小骨架"运行,再回头补完本文件。

## 1. 协议意图(审计师原话摘要)

强品类 brief(户外灯、咖啡机、手电筒、鼠标、无人机等)在 STEP-06 候选生成时,模型会**自动代入**该品类的"部件名词库"(手柄/扳机/灯罩/杯托),导致 3 个方向都收敛于同一组部件。

**解耦动作**: 先剥离品类隐喻,把 brief 还原为**纯粹动作**(握持/旋转/插入/倾倒/对焦),再让动作自由派生出造型;造型确立后才映射回品类的功能部件名。

## 2. 触发条件

满足以下任一即触发本协议:

- brief 含强品类名词(户外灯/咖啡机/鼠标/无人机/机器人/...)
- STEP-06 候选生成阶段
- 3 个候选中出现 ≥ 2 个相同品类部件名(如 2 个都有"杯托")

## 3. 最小运行骨架(占位)

```
1. 从 brief 提取所有"品类部件名词",写入 BRIEF-NOUN-LIST
2. 对每个名词,问:这个部件承担的纯粹动作是什么?  (握持? 旋转? 倾倒? ...)
3. 派生命题: 能否用非该品类部件名,完成同样的动作?  (例: "倾倒"不一定要"杯托",可以是斜面、凹槽、引流槽)
4. 在 STEP-06 候选生成前,只用动作命题,而非部件命题
5. 候选确立后,再映射回具体部件命名
```

## 4. 待补内容(占位 TODO)

- [ ] 完整协议正文(铁律、禁止词清单、3 方向差异化矩阵)
- [ ] 实证案例(咖啡机 / 鼠标 / 户外灯 各自剥离前后对比)
- [ ] 与 `REF-DIRECTION-001 ~ 005` 的 depends_on 关系图
- [ ] QG 检查项(STEP-08 怎么验证"动作已剥离")
- [ ] 同类协议互引(`REF-GUIDE-CSM` 语境清洗 / `REF-GUIDE-TDR` 几何降维)

## 5. 引用

- 触发案例: `references/cases/pitfall-027-auditor-gray-background-conflict.md`(同批次审计师反馈)
- 同批次协议: `multi-level-composite-locking.md` / `context-sanitation-matrix.md` / `topology-de-reduction.md` / `craft-spectrum-palette.md` / `audit-feedback-2026-06-24-prompt-architecture.md`

---

**Stub 生成**: 2026-06-24 by 自动诊断修复 — `references/cases/case-*.md` 类的"诊断即修复"模式见 `references/cases/pitfall-025-upgrade-before-rerun.md`。