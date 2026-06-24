---
reference_id: REF-CASE-050
title: Pitfall 050 — 诊断时只看目录大小不看文件数会误判空目录,差点批量删除 15 个真实文件
category: cases
date: 2026-06-24
type: skill-repair-trap
used_when:
  - SKILL-UPGRADE
  - FILE-HYGIENE-CLEANUP
  - BULK-DELETE-OPERATION
called_by:
  - skill-optimizer
  - file-hygiene-check
depends_on:
  - REF-HYGIENE-001
outputs:
  - empty_dir_detection_protocol
---

# Pitfall 050: 诊断时只看目录大小不看文件数会误判空目录,差点批量删除 15 个真实文件

> **日期**: 2026-06-24
> **触发**: 2026-06-24 jony-ive-design2me-v2 自动诊断修复。`ls -la references/iterations/v2-round-1` 输出 `total 64`,被误判为"几乎为空(64 字节)",列入 P1-9 清理清单。
> **严重级别**: 🔴 BLOCKER for any bulk-delete operation
> **后果**: 若执行 `rm -rf references/iterations/v2-round-1..5` 会**永久丢失 15 个真实迭代文件 / 92 KB**(违反铁律 1 信息分散原则 + 铁律 7 0 删除原则)

## 1. 现象

`ls -la` 输出目录大小(`total 64` 等)是**目录 entry 自身占用的 inode 字节数**,**不是目录内容的总大小**。

```
$ ls -la references/iterations/v2-round-1
total 64
drwxr-xr-x@  7 easoneason  staff   224 Jun 21 23:01 .
drwxr-xr-x@ 27 easoneason  staff   864 Jun 23 22:43 ..
-rw-------@  1 easoneason  staff  6704 Jun 23 21:27 image-analysis-v2.md
-rw-------@  1 easoneason  staff  8069 Jun 23 21:27 image-analysis-v3.md
... (5 files, 32 KB)
```

误读 `total 64` → "目录几乎为空"。

实际 5 个文件 / 32 KB,每个有真实迭代历史。

## 2. 正确的空目录判定

### 2.1 按文件数判断

```bash
# 0 文件 = 真空
find references/iterations/v2-round-1 -type f | wc -l
# 输出: 5  ← 不空
```

### 2.2 按内容大小判断

```bash
du -sh references/iterations/v2-round-1
# 输出: 32K  ← 有内容
```

### 2.3 按 README 引用判断(本技能场景最强信号)

```bash
# 如果 v2-round-1 被 references/README.md 登记,它必有内容
grep "v2-round" references/README.md
```

## 3. 防御协议(批量删除前必跑)

### 3.1 三步检查(任一失败即停止删除)

```bash
# 步骤 1: 文件数检查(0 才考虑删)
N=$(find "$DIR" -type f | wc -l)
if [[ "$N" -gt 0 ]]; then
    echo "STOP: $DIR has $N files"
    exit 1
fi

# 步骤 2: 大小检查(0 才考虑删)
SIZE=$(du -sb "$DIR" | awk '{print $1}')
if [[ "$SIZE" -gt 0 ]]; then
    echo "STOP: $DIR has $SIZE bytes"
    exit 1
fi

# 步骤 3: README 引用检查(被登记的不删)
if grep -q "$DIR" references/README.md; then
    echo "STOP: $DIR is referenced in README"
    exit 1
fi
```

### 3.2 删除前必跑 git dry-run

```bash
# 显示将要删除什么,确认无误再真删
git rm -rn references/iterations/v2-round-* | head -50
```

### 3.3 删除前必备份

```bash
# 删除前 cp -r 留底
cp -r references/iterations/v2-round-1 /tmp/backup-before-delete/
```

## 4. 决策矩阵

| 信号 | 行动 |
|---|---|
| `ls -la` 显示 total < 100 bytes | **不要据此判断空**,跑 `find -type f \| wc -l` |
| `find -type f` 输出 0 | **可考虑删**,但仍跑 README 引用检查 |
| 被 README 引用 | **不删**(违反铁律 1 信息分散) |
| 没被 README 引用 + 0 文件 | **可删**,但仍 git dry-run |

## 5. 实战案例(本次 session)

**错误判断**: 看 `ls -la` 输出 `total 64`,列入"几乎为空 → 清理"清单。

**正确判断**: 跑 `find -type f | wc -l` 输出 `5`,跑 `du -sh` 输出 `32K`,跑 `grep v2-round references/README.md` 输出 6 行登记。

**撤销**: 撤回 P1-9 清理动作,目录保留。

## 6. 引用

- 铁律: `references/file-hygiene.md` 铁律 1(信息分散) + 铁律 7(0 删除原则)
- 同类陷阱: `pitfall-048-backup-skill-illusion.md`(BACKUP 副本陷阱也是误判家族)
- 修复历史: 本次 session 的 P1-9 撤销记录