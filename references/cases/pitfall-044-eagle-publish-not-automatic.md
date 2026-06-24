---
reference_id: REF-CASE-044
title: Pitfall 044 - Lovart 出图后未自动 publish 到 Eagle
category: cases
used_when:
  - LOVART-POST-GENERATION
  - ITERATION-MODE
  - USER-IMAGE-GENERATION
called_by:
  - skill-execution
  - quality-gates
depends_on:
  - REF-EAGLE-001
  - REF-PROCESS-001
outputs:
  - eagle_publish_chain_failure
---

# Pitfall 044 - Lovart 出图后未自动 publish 到 Eagle

> **触发**: 用户 2026-06-23 咖啡机任务反馈
> **用户原话**: "在Lovart Skill里面没有添加上次说的，把图片添加到ego里面的这个功能，没有流畅地运行，要我问了以后才运行"
|> **严重级别**: BLOCKER(破坏 Lovart → Eagle 自动归档的永久协议)
> **触发日期**: 2026-06-23

## 现象

执行 jony-ive-design2me-v2 技能时，agent 走了完整 15 步流程并生成 6 张图到 `~/lovart-out/coffee-machine-r1-{d1,d2,d3}/`，但：

1. **未加载** `lovart` skill 的 Eagle 归档协议(虽然 SKILL.md 在"图片生成与评审"段提到了 Lovart)
2. **未运行** `bash ~/.hermes/skills/lovart/scripts/eagle_publish.sh publish-images` 6 次（每图一次）
3. **未运行** `bash ... publish-doc` 生成项目证据文档
4. **结果**: 用户打开 Eagle 时找不到项目，必须手动反馈"为什么没有按照要求导入 eagle"才补做

## 根因

1. **跨技能协议裂缝**：`jony-ive-design2me-v2` SKILL.md 在"图片生成与评审"段提到 Lovart，但**没把 Lovart 描述为强制依赖**。`lovart` SKILL.md 的"Default Post-Generation Behavior"段写得很清楚，但 agent 没有跨技能加载机制
2. **单向引用**：`lovart` SKILL.md 的 `related_skills` 写了 `jony-ive-design2me-v2`，但 `jony-ive-design2me-v2` 的 SKILL.md frontmatter `related_skills` 只有 `jony-ive-perspective`，**漏列 `lovart`**
3. **3 步链 vs 1 步执行**:Lovart 当前协议是"出图 → publish-images → publish-doc"3 步,但 SKILL.md 的"图片生成与评审"段只展示了步骤 1(出图),未强制 2 和 3

## 修复(已写入 jony-ive-design2me-v2 SKILL.md · 上一版 file-hygiene 升级)

1. **强制三步链段**:"## 图片生成与评审(迭代模式)" 段头部新增 🚨 强制三步链声明
2. **完整命令示例**:3 步命令全部展开(出图 + publish-images + publish-doc)
3. **跨技能钩子段**:明确"任何 Lovart 出图任务前必须先 `skill_view(name="lovart")` 加载 Eagle 归档协议"
4. **本 pitfall 文件**：作为 SKILL.md 中"详见 ..."的引用目标
5. **Lovart 侧反向引用**：`lovart` SKILL.md 在 `related_skills` 已经列了 jony-ive-design2me-v2（在 Related Skills 段）

## 验证

未来执行 Lovart 出图任务时，检查：
- [ ] 出图前 `skill_view(name="lovart")` 加载了 Eagle 归档协议(含 `eagle-integration.md` 引用)
- [ ] 出图后立即跑 `eagle_publish.sh publish-images`（每图一次）
- [ ] 项目结束跑 `eagle_publish.sh publish-doc`（生成项目 md 文档）
- [ ] Eagle library `lovart-generations/{date}_{brief}_{version}/` folder 存在
- [ ] 6 张图 + 1 个 doc.md 全部在 folder 内
- [ ] 用户不需要追问"为什么没导入 eagle"——流程就该自动完成

## 与其他 Pitfall 关系

- **Pitfall 017 (desktop-pollution)**：是 Lovart 侧的反向版本，描述"不准 cp 到桌面"
- **Pitfall 018 (mcp-folder-add-bug)**：是 Eagle MCP server 的实现 bug，由 `eagle_publish.sh` 自动 `item_update` 兜底
- **Pitfall 044 (本文件)**：是 jony-ive-design2me-v2 侧的执行流程缺陷，强调"必须跑 3 步链"

## 来源

- 用户 2026-06-23 反馈："在Lovart Skill里面没有添加上次说的..."
- Lovart skill changelog:2026-06-22 升级"图片发布 Eagle 永久协议"
- jony-ive-design2me-v2 上一版 file-hygiene 升级(本次):跨技能钩子修复
