---
reference_id: REF-PROCESS-004
title: 技能完整阅读指南与验证路径
category: process
used_when:
  - SKILL-READING
  - SKILL-REVIEW
  - STEP-01
called_by:
  - skill-router
  - step-reference-map
depends_on:
  - REF-INDEX-001
  - REF-PROCESS-001
  - REF-PROCESS-002
outputs:
  - reading_plan
---

# 技能完整阅读指南与验证路径

## 用途

当用户要求"完整阅读"本技能时，按此指南执行，确保不遗漏任何 reference 文件、脚本或验证步骤。

## 阅读顺序（不可跳过）

1. **SKILL.md** — 确认启动顺序、请求路由优先级、不可跨越边界。
2. **references/README.md** — 获取全部 29 个 reference 的 ID、路径和用途总览。
3. **references/process/end-to-end-workflow.md** — 理解四阶段十五步框架。
4. **references/process/step-reference-map.md** — 确认每步的强制引用映射。
5. **references/process/reasoning-output.md** — 理解用户可见推理输出合同。
6. **按类别批量读取剩余 reference**：
   - `core/` × 4：证据政策、五维引擎、方法快照、案例胶囊
   - `direction/` × 5：第一性锚点、约束级联、反俗套扫描、六轴差异门、三方向协议
   - `design/` × 4：DesignIR、形态比例、CMF、交互生命周期
   - `prompt/` × 4：PromptBundle 合同、压缩规则、逐句追溯、摄影控制
   - `quality/` × 4：审美质量门、图片评审、失败库、确定性质量门
   - `workflows/` × 9：全部专项工作流 + 索引
7. **运行验证脚本**：
   - `python3 scripts/validate_reference_graph.py .` — 确认引用闭环
   - 可选：`python3 scripts/validate_skill.py .`（需目录名匹配）
8. **统计完整性**：`find . -type f | sort` + `wc -l` 核对文件数和行数。

## 验证清单

- [ ] 29 个 reference 文件全部读取
- [ ] 6 个 Python 脚本存在且可运行
- [ ] `validate_reference_graph.py` 通过
- [ ] 15 步 × 每步 2+ 引用映射完整
- [ ] 9 个工作流全部覆盖
- [ ] 7 类质量门/评审/失败分类完整

## 输出格式

阅读完成后，向用户提交结构化报告：
1. 技能总览（目录、文件数、总行数、验证状态）
2. 四阶段十五步框架摘要
3. 核心方法文件要点（证据政策、五维引擎、方法快照、案例胶囊）
4. 方向筛选与 DesignIR 结构
5. 提示词编译与质量门机制
6. 专项工作流索引
7. Python 脚本与数据类覆盖范围
8. 与相关技能（jony-ive-perspective）的关键区别对比
