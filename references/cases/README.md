># Pitfall 与案例索引

> **用途**: 索引所有已记录的 pitfall 案例、失败模式和实证记录。
> **更新规则**: 发现新失败模式 → 添加新文件；修复完成 → 标记状态；不删除历史记录。

## 已记录 Pitfall

| Pitfall ID | 标题 | 触发条件 | 来源 | 状态 |
|-----------|------|---------|------|------|
| pitfall-001 | 输出合同违反 | 未严格展示 10 字段 | REF-QUALITY-003 | 已记录 |
| pitfall-002 | 形态优先于关系 | 未先定义使用者动作 | REF-IVE-001 MTH-002 | 已记录 |
| pitfall-003 | 中途停止执行 | STEP-05 后询问用户 | REF-PROCESS-003 | 已记录 |
| pitfall-011 | 形态先于关系 | 同 pitfall-002 但更严重 | REF-PROCESS-001 | 已记录 |
| pitfall-012 | 材料无职责 | 只写材料名未说明职责 | REF-QUALITY-003 | 已记录 |
| pitfall-013 | 纯审美比例 | 无来源的比例数字 | REF-PROCESS-001 | 已记录 |
| pitfall-014 | 颜色词替代高级感 | "深岩灰"等无职责颜色 | REF-QUALITY-003 | 已记录 |
| pitfall-015 | 功能未验证 | 形态无法完成核心功能 | REF-PROCESS-001 | 已记录 |
| pitfall-016 | 背景侵入 | 图片含手/人物/辅助物 | REF-QUALITY-002 | 已记录 |
| pitfall-017 | 提示词未用代码块 | 未按 codeblock 输出 | REF-PROCESS-001 | 已记录 |
| pitfall-018 | 工程材料替代感官材料 | "titanium alloy TC4" 等 | REF-PROMPT-002 | 已记录 |
| pitfall-019 | 输出经验主义验证 | 编造评分/跳过真出图 | REF-QUALITY-002 | 已记录 |
| pitfall-023 | 第三方模型提示词劣化 | 中文主体 prompt 喂英文模型 | REF-PROMPT-005 | 已记录 |
| pitfall-024 | Lovart 静默超时 | Status: timeout 但实际产出 | guides/lovart-execution | 已记录 |
| pitfall-025 | 咖啡机品类反模式 | Nano Banana Pro 品类默认联想 | REF-PROMPT-002 | 已记录 |
| pitfall-026 | 第三方 AI 反馈处理 | 盲吸/盲拒第三方建议 | REF-EVIDENCE-001 | 已记录 |
| pitfall-030 | 技能名称歧义 | BACKUP 副本 + 真实 skill 同名 | skill-router | 已记录 |
| pitfall-039 | 真实评审标准 | AI 天花板 4-5/10 不虚高 | guides/ai-ceiling | 已记录 |
| pitfall-040 | 内容镜像未接入 | 只完成 A 未完成 B | guides/external-knowledge-mirror | 已记录 |
| pitfall-041 | 审计脚本僵化 | REQUIRED_REFERENCES 固定 | audit_references.py | 已记录 |
| pitfall-042 | graph bypass via index | KB 不进 graph 但索引闭环 | guides/external-knowledge | 已记录 |
| pitfall-043 | SkillOpt 视觉黑盒 | 训练不能突破 Lovart 视觉权重 | guides/skillopt | 已记录 |
| pitfall-044 | Eagle 推送不自动 | 出图后未自动 publish | cases/pitfall-044 | 已记录 |
| pitfall-046 | 无调研就升级 | SKILL.md 改前必须 model-fit | cases/pitfall-046 | 已记录 |
| pitfall-047 | 提示词方法链内部矛盾 | 改前必须跑方法链审计 | cases/pitfall-047 | 已记录 |
| **pitfall-048** | **BACKUP 副本里"升级"是错觉** | **2026-06-23 飞行器任务实证** | **REF-CASE-030** | **已记录** |
