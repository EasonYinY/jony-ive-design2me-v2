# Pitfall 024 补充: 复杂 prompt 长度阈值(mouse-r1 D2 v1→v2→v3 实证)

> **日期**: 2026-06-24
> **触发**: 科技感鼠标任务 R1 D2 提示词工程。原 prompt 1397 字节(含 N52 neodymium 钕铁硼磁吸 + 2mm levitation gap + 三阶层次链 + 镀金触点 + 多条工艺分界线)连续触发 3 次 `Status: timeout` 且 3 次均无 image URL 产出(连静默成功都不是),是 Lovart Nano Banana Pro 在 prompt 复杂度上"系统性静默失败"的新模式。
> **严重级别**: 🟠 HIGH for image-critique phase
> **关联**: 补充 `pitfall-024-lovart-quiet-success-timeout.md`(原 024 关注"timeout 但有 URL 兜底",本补充关注"timeout 且无 URL → 必须简化")

## 1. 现象

mouse-r1 D2 任务的 v1 → v2 → v3 三次重试,每次 Lovart 都报 `Status: timeout`,但 stdout 中**完全无 image URL 输出**(连"静默成功"都不是),与原 Pitfall 024 的"Status: timeout 但有 image URL"模式不同 — 这是 Nano Banana Pro 在 prompt 复杂度上**直接放弃生成**的新失败模式。

| 版本 | 字节数 | 主要内容 | 结果 |
|---|---|---|---|
| **v1** | 1397 | 完整三阶层次链 + 钕铁硼 N52 + 镀金触点 + 异质材质 + 3 条工艺分界线 | ❌ Status: timeout, 无 image URL, 无 assistant 输出 |
| **v2** | 1139 | 简化掉"三阶层次链"概念术语 + 删除"镀金微观精密端"细节 | ❌ Status: timeout, 无 image URL, assistant 出现但未生成图 |
| **v3** | 789 | 进一步简化: 删"内径/壁厚/环高"三组精确数字 + 用短语代替完整从句 | ✅ 成功生成 2.26MB PNG (2048×1536) |

## 2. 长度阈值经验

| 字节范围 | timeout 风险 | 推荐动作 |
|---|---|---|
| **< 800 字节** | 极低 | 1-2 次重试即可成功 |
| **800-1200 字节** | 偶发(1-2 次) | 重试有效 |
| **1200-1500 字节** | 高频(2-3 次) | 需要简化 |
| **> 1500 字节** | 系统性静默失败 | 重写 prompt 而非重试 |

## 3. v3 关键简化技术

| 简化技术 | v1 写法 | v3 写法 |
|---|---|---|
| 用短语代替完整从句 | "钕铁硼 N52 neodymium 钕铁硼磁吸 + 2mm levitation gap" | "磁吸 hairline 环(钕磁)" |
| 删去 ≤ 1 mm 量级精确尺寸 | "内径 18.0mm 壁厚 1.5mm 环高 6.0mm" | (整段删) |
| 保留 ≥ 2 mm 大尺度数字 | "slab 120mm × 65mm × 38mm" | (保留) |
| 保留 ≥ 1 个几何术语 | "G2 fillet articulation" | (保留) |
| 保留反偏见子句 | "NOT a gaming mouse..." | (必含,不能删) |

## 4. 重试决策树

```
第 1 次 timeout → 重试同一 prompt(成功率 50%)
第 2 次 timeout → 简化 prompt(删去 1 个非关键工艺细节 / 删去 1 个材料子句)
第 3 次 timeout → 大幅简化(删去三阶层次链概念 / 删去微观精密端 / 改用短语代替从句)
第 4 次 timeout → 触发 prompt 工程重写(不重试)
```

## 5. 新失败码(建议追加到 `failure-library.md`)

| 失败码 | 描述 | 严重性 |
|---|---|---|
| `complex_prompt_silent_timeout` | prompt > 1200 字节且连续 2 次 timeout 无 image URL 输出 | 🟠 HIGH |

## 6. 与既有 Pitfall / 协议的关系

- **Pitfall 024(Lovart 静默超时 + 模型回退)**: 原 024 关注"timeout 但有 URL 兜底"或"模型回退",本补充关注"timeout 且无 URL → 必须简化 prompt"
- **Pitfall 028(mouse archetype prior 塌陷)**: mouse-r1 D2 简化重试的副产品。028 关注"3 方向视觉同质化到 Apple Magic Mouse 家族",本补充关注"D2 方向本身出图失败" — 同一次任务的两个不同失败维度
- **REF-PROMPT-002 中文提示词压缩规则**: v3 简化技术 = REF-PROMPT-002 §"提示词工程方法 13.2 精确数字的双锁定原则"的具体应用 — 数字锁形态(≥ 2 mm + ≥ 1 几何术语)+ 形容词锁比例(短语代替完整从句)

## 7. 验证方式

每次 Lovart 任务后执行:
```bash
for d in d1 d2 d3; do
  echo "$d: $(ls ~/lovart-out/<task>-$d/*.png 2>/dev/null | wc -l) 张, 字节数: $(wc -c < ~/lovart-out/<task>-d*/prompts/$d*.txt 2>/dev/null | tail -1)"
done
```
期望:3 行都 ≥ 1 张图;若某方向 prompt 字节数 > 1200 且连续 timeout,触发 `complex_prompt_silent_timeout`。

## 8. 来源

- 2026-06-24 科技感鼠标任务 R1 D2 任务全过程
- 详细执行日志:`/Users/easoneason/lovart-out/mouse-r1-d2/run.log` 3 次记录
- prompt 演化:`/Users/easoneason/lovart-out/mouse-r1/prompts/d1.txt` (1397) → `d2-v2.txt` (1139) → `d2-v3.txt` (789)
- 经验:**复杂 prompt 优先简化而非重试**,与"3 方向并行在 Lovart 稳定性上有同源风险"
