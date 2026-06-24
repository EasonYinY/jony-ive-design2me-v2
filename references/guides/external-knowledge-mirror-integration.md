---
reference_id: REF-GUIDE-MIRROR
title: 外部知识库镜像与引用闭环集成指南
category: guide
used_when:
  - KB-MIRROR
  - EXTERNAL-KB-SYNC
  - UPSTREAM-DISTILL
called_by:
  - skill-router
  - upstream-knowledge-curator
depends_on:
  - REF-HYGIENE-001
outputs:
  - mirror_integration_protocol
---

# 外部知识库镜像与引用闭环集成指南

> **触发场景**:用户要求"同步/镜像/导入/复制"外部知识库(Obsidian / Notion / 内网 wiki / 任意 .md 仓库)到技能目录
> **强制三阶段**:镜像(A)→ 接入(B)→ 验证(C)
> **错误警示**:只完成 A 而声称"完成"是 当前版本 触发的核心失误(Pitfall 040)

## 三阶段流程

### 阶段 A · 字节级镜像(数据搬运)

**目的**:无损把外部 .md 复制到技能目录,保留 sha256 一致

**步骤**:

1. **建立 mirror 目录**: `references/knowledge-base/`(命名:`knowledge-base` / `external-mirror` / `upstream-kb`,按内容性质选)
2. **保留原目录结构**:用 `shutil.copytree` 或 `rsync -av`,不要合并不相关目录
3. **字节级校验**:读 src + dst 的 sha256,任何 mismatch 即重做
4. **生成元数据**:
   - `references/<mirror-dir>/README.md` — 28 篇元数据表(版本/日期/字节/用途定位)
   - `references/<mirror-dir>/SHA256SUMS.txt` — 全部 .md 的 sha256 + relpath
5. **写入校验命令**:在 README §5 写同步命令(rsync + sha256 diff),便于下次重同步

**完成定义**:28/28 sha256 一致 + 元数据完整

### 阶段 B · 接入引用闭环(知识接入)

**目的**:让运行工作流能找到 mirror 内容,不只是放在目录里

**B 阶段 6 个必做动作**(Pitfall 040 详细清单):

| # | 动作 | 位置 | 示例 |
|---|---|---|---|
| 1 | 启动顺序加 mirror 加载 step | SKILL.md `## 启动顺序` | `Step 6: 按 mirror README 加载 KB 原文` |
| 2 | 注册 mirror 顶层为 REF-XXX-ID | step-reference-map.md | `STEP-01 | ... REF-KB-INDEX` |
| 3 | 上游 STEP 加 mirror 反向链接 | end-to-end-workflow.md | `STEP-01 | **Mirror 反向链接**: \`.../不可生成项.md\`` |
| 4 | 运行 reference 加 mirror 反向链接段 | failure-library.md / ive-thinking-models.md / aesthetic-gate.md | `## 上游 Mirror 反向链接` 段 |
| 5 | 总索引加 REF-XXX-INDEX 行 | references/README.md | `\| REF-KB-INDEX \| [mirror README](README.md) \| ... \|` |
| 6 | 校验脚本加 mirror 白名单 | validate_skill.py / validate_reference_graph.py | `UPSTREAM_MIRROR_DIR = "knowledge-base"` |

**反向链接最少数量规则**(按 mirror 内容总量):

| mirror 文件数 | 最小反向链接数 |
|---|---|
| 1-5 篇 | 3 处 |
| 6-15 篇 | 8 处 |
| 16-30 篇 | 15 处 |
| 30+ 篇 | 25 处 |

**反向链接分布原则**:

- 启动顺序 / step-reference-map 各占 1 处
- end-to-end-workflow 各 STEP 至少覆盖:STEP-01(边界)、STEP-02(事实)、STEP-03(关系)、STEP-08(反例)、STEP-15(输出)5 个关键节点
- 运行 reference 至少 2 个反向链接文件(failure-library 必选)

### 阶段 C · 验证(确认未引入新失败)

**目的**:跑校验脚本,确保 mirror 接入未破坏现有验证

**步骤**:

1. 跑 `python3 scripts/validate_skill.py .` — 记录 baseline 失败数
2. 跑 `python3 scripts/validate_reference_graph.py .` — 记录 baseline 失败数
3. **新增失败判定**:本次同步(阶段 A+B)引入的失败必须 = 0
4. 预先失败(cases/iterations/ 部分文件无 frontmatter 等)不算新失败,跨出本次同步范围

**完成定义**:`validate_*.py` 失败总数 ≤ baseline,KB 相关失败 = 0

## 反向铁律(0 改写外部原文)

mirror 文件**绝对不修改任何字节**,理由:

- 用户原资料库是真相源(single source of truth)
- 任何 frontmatter 注入 / humanizer 润色 / 简化 / 改写,都违反"同步"语义
- 万一 mirror 与上游不一致,以 src 为准 + 重做镜像

**元数据集中原则**:28 篇 mirror 文件的"使用触发 / 调用方 / 依赖 / 输出"全部写到 `references/<mirror-dir>/README.md` 一张表,**不要**在每篇 mirror 文件内加 frontmatter / 头部块。

## 失败模式清单

| 模式 | 症状 | 修正 |
|---|---|---|
| **镜像未接入** | 内容在但运行找不到 | 完成 B 阶段 6 个动作 |
| **改写原文字节** | sha256 与 src 不一致 | 用 `cp` 而非编辑;元数据集中到 README |
| **frontmatter 注入到 mirror** | 改了原文字节 | 不注入,元数据集中到 README |
| **mirror 路径破坏校验脚本** | validate_*.py 失败激增 | 加 `UPSTREAM_MIRROR_DIR` 白名单常量 |
| **只有 README 注册,无 STEP 引用** | 用户报告"新增内容未引用" | B 阶段必做 6 个动作全做 |
| **mirror 内容直接喂 STEP-15** | 破坏 prompt-contract 字符边界 | STEP-15 镜像用强约束:仅供写作参考,严禁直接复制 |

## 同步命令模板

```bash
SRC="$HOME/path/to/source/library"
DST="$HOME/.hermes/skills/<skill>/references/<mirror-dir>"

# 1. 镜像(覆盖,保留目录结构)
rsync -av --include='*/' --include='*.md' --exclude='*' "$SRC/" "$DST/"

# 2. 验证字节一致性
( cd "$SRC" && find . -name '*.md' -exec sha256sum {} + | sort ) > /tmp/src.sha
( cd "$DST" && find . -name '*.md' -exec sha256sum {} + | sort ) > /tmp/dst.sha
diff /tmp/src.sha /tmp/dst.sha   # 无输出 = 完全一致

# 3. 重新生成元数据表
python3 scripts/regen_mirror_readme.py "$SRC" "$DST"
```

## 决策表

| 用户说 | 阶段 A | 阶段 B | 阶段 C |
|---|---|---|---|
| "把这些信息同步跟新进技能对应的文旦当中" | ✅ | ✅ | ✅ |
| "不要过度优化,简化,和删除,要确保原始文字的表达完整,正确" | ✅(0 改写) | ✅ | ✅ |
| "导入参考材料" | ✅ | ✅(至少 6 个反向链接) | ✅ |
| "镜像 + 不需要接入运行" | ✅ | ⚠️ 必须做 B,但用户可豁免 1-2 个反向链接 | ✅ |
| "只复制过来我自己读" | ✅ | ❌ 不做 B | ⚠️ 不跑 validate |

## 关联

- 当前版本 →记录: `references/changelogs/当前版本-changelog.md`
- 失败模式: `references/cases/pitfall-040-content-added-not-integrated.md`
- 文件卫生铁律: `references/file-hygiene.md` 铁律 7
- 当前版本 changelog: `references/changelogs/当前版本-changelog.md`