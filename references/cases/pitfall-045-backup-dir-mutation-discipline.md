---
reference_id: REF-CASE-045
title: Pitfall 045 - 在 BACKUP 目录创建污染版本（未识别 active vs backup）
category: cases
used_when:
  - SKILL-UPGRADE
  - VERSION-BUMP
  - MULTIPLE-INSTALL-PATHS
called_by:
  - skill-execution
  - skill-architecture
  - skill-installation
depends_on:
  - NONE
outputs:
  - backup_pollution
  - version_drift
---

# Pitfall 045 - 在 BACKUP 目录创建污染版本

> **触发**: 用户 2026-06-23 咖啡机任务反馈
> **用户原话**: "jony-ive-design2me-v2 的版本不是都2.7 了吗为什么才1.3？版本没有完整同步"
> **严重级别**: BLOCKER（破坏版本一致性、污染历史备份、产生 phantom version）
> **触发日期**: 2026-06-23

## 现象

执行 jony-ive-design2me-v2 升级时，agent 收到 session 启动时注入的 `[Skill directory: .../jony-ive-design2me-v2-BACKUP-历史版本目录-双层嵌套]`，**未识别这是历史备份目录**，错误地：

1. 在 BACKUP 目录写入新的 SKILL.md（version 1.3.0）—— **污染了一个应该是只读的备份**
2. **凭空造版本号**:BACKUP 目录的旧版本 → 新跳号(phantom),但活跃 skill 实际在更高版本
3. **跳号严重**：活跃版本与写入版本相差 14 个 minor 版本（1.x vs 2.x）
4. **用户反馈后**才发现真实情况，被迫回滚 + 在活跃目录补做正确升级

## 根因

1. **没读路径名就假设**:`...-BACKUP-...-...` 路径里**两处**带 `BACKUP` + 旧版本字符串,是明显的备份标记,但 agent 跳过了
2. **没交叉验证**：没跑 `ls -la ~/.hermes/skills/creative/` 列出所有同名 skill，没用 `mtime` 判断哪个是活跃
3. **没读 SKILL.md frontmatter**：活跃 skill 的 `version: 2.7.0`，BACKUP 的 `version: 1.2.1` — 一行 `head -5 SKILL.md | grep version` 就能区分
4. **没问用户**：直接假设"session 启动时给的目录就是活跃的"——这是错的

## 修复（永久纪律）

### A. 升级前必跑 3 步验证

```bash
# 1) 列出所有同名 skill 目录
ls -la ~/.hermes/skills/creative/ | grep jony-ive-design2me-v2

# 2) 找 mtime 最新（=活跃）
ACTIVE=$(ls -td ~/.hermes/skills/creative/jony-ive-design2me-v2* | grep -v BACKUP | head -1)

# 3) 读 frontmatter 确认 version
head -5 "$ACTIVE/SKILL.md" | grep version
```

**任何升级操作只对 `$ACTIVE` 目录执行。BACKUP 目录只读。**

### B. 路径名识别规则

| 路径模式 | 含义 | 操作 |
|---|---|---|
| `~/.hermes/skills/creative/jony-ive-design2me-v2/`（无后缀） | 活跃 skill | ✅ 读 + 写 |
| `~/.hermes/skills/creative/jony-ive-design2me-v2-BACKUP-20260621-134945/` | 备份目录 | ❌ 禁止写（只读） |
| `~/.hermes/backups/jony-ive-design2me-v2-pre-升级-20260622-142821/` | 备份目录 | ❌ 禁止写（只读） |
| `~/.hermes/skills/creative/jony-ive-design2me-v2-BACKUP-双层嵌套-.../` | 嵌套备份 | ❌ 禁止写（只读） |

**规则**：
- 路径含 `BACKUP` 字符串 → 备份目录 → 禁止 write_file/patch/terminal 编辑
- 路径在 `~/.hermes/backups/` 下 → 备份目录 → 禁止编辑
- 路径 mtime 比活跃目录旧 > 24 小时 → 备份目录 → 禁止编辑
- **不确定时**：先 `head -5 SKILL.md | grep version` 看版本号，再用 `ls -lat` 看 mtime

### C. 版本号跳号检测

- 活跃版本 = 读 SKILL.md frontmatter 的 version 字段
- 计划升级号 = 活跃 + 1 个 minor(如上一版 → 下一版)）
- **如果计划号远低于活跃(>5 个 minor)**：**几乎一定是路径识别错误**，停止操作重新检查

## 验证

未来执行 skill 升级任务时，检查：
- [ ] 升级前已跑 A 节的 3 步验证
- [ ] 操作目录 = 活跃目录（无 BACKUP 后缀）
- [ ] 写出的版本号 = 活跃版本号 + 1 minor（不跳号）
- [ ] BACKUP 目录的 mtime 没被本次会话更新
- [ ] 没在路径含 `BACKUP` / 在 `~/.hermes/backups/` 下做任何编辑

## 与其他 Pitfall 关系

- **Pitfall 030 (skill-name-ambiguity)**：互补。030 描述 `skill_view` 因同名多 skill 报错时的处理；本 pitfall 045 描述 agent 主动避免污染 BACKUP 目录的纪律
- **Pitfall 021 (reference-graph-upgrade-friction)**：互补。021 是引用图层的版本号冲突；本 pitfall 045 是文件系统层的目录识别错误

## 一次性根因事件

- 2026-06-23 咖啡机任务:agent 在 BACKUP 目录写了 phantom 版本号(活跃是更高版本),被用户当场指出
- 修复:用户命令"现在应该升级" → agent 在活跃目录做下一版升级 + BACKUP 目录恢复早期版本
- **教训**：升级任何 skill 前**必须**先识别活跃 vs 备份，**不得**假设 session 注入的路径就是活跃

## 来源

- 用户 2026-06-23 反馈："jony-ive-design2me-v2 的版本不是都2.7 了吗为什么才1.3？版本没有完整同步"
- 活跃版本(2.x 阶段) vs BACKUP 目录(1.x 阶段),agent 写入 phantom 跳号（phantom 跳号）
- 用户命令"清除所有乱七八糟的版本号，统一一个版本" → 后续升级协议已确立(见上一版 file-hygiene 升级 changelog)）
