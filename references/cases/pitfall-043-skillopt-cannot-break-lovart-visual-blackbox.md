---
pitfall_id: pitfall-043
reference_id: REF-CASE-043-skillopt
title: SkillOpt 训练不能突破 Lovart 视觉权重分配黑盒 — 2026-06-23 实测
category: cases
date: 2026-06-23
severity: critical
trigger: 用户要求"用 SkillOpt 训练提升出图质量" 或 "用 AI 训练 SKILL.md 改善 prompt"
status: empirical-confirmed
related:
  - pitfall-019-prompt-output-empirical-validation.md
  - pitfall-039-real-evaluation-standard.md
  - cases/README.md
model_under_test: Lovart vertex/anon-bob (Nano Banana Pro 1K)
image_budget: 9
---

# Pitfall 043 — SkillOpt 训练不能突破 Lovart 视觉权重分配黑盒

## 一句话

**改 SKILL.md 不能让 Lovart 出图变好。** SkillOpt 训练的 reward 信号是
文本,不是视觉 — 它让 prompt **写得更好**,但 prompt 写得好 ≠ Lovart 渲
染得对。

## 触发条件

用户说"用 SkillOpt 训练 jony-ive-design2me-v2" / "用 AI 训练我的设计
skill 改善出图" / 类似表达。

## 实测证据(2026-06-23)

**Brief**:户外露营灯,3 方向(鹅卵石-棱线 / 水滴-嵌槽 / 禅石-磁吸)

**Lovart 配置**:vertex/anon-bob (Nano Banana Pro),1K,3 方向并行,9 张图

**真实出图结果(诚实反查,不打分)**:

| 方向 | prompt 写了什么 | 实际渲染了什么 | 偏差 |
|---|---|---|---|
| A 鹅卵石-棱线 | 6061-T6 钛灰铝合金 + 5 主棱线 + 0.1mm 倒角 + IPX7 | 米色沙黄硅胶水滴型 + 5 棱线全失 + 挂绳孔 | **CMF 完全错配 + 形态退化为更简单的水滴** |
| B 水滴-嵌槽 | 食品级硅胶 RAL 1001 沙黄 + 2.5mm 壁厚 | 钛灰铝合金鹅卵石 + 5 棱线 + 嵌槽 | **A 的视觉跑到了 B 的图上 — A/B 视觉互换** |
| C 禅石-磁吸 | 三件套 1:0.67:0.5 比例 + 黄铜拉丝 + 0.05mm 间隙 | 三块黑砂石 + 黄铜环 + 中间暖光带,比例对,CMF 对 | **3 方向里最稳,但 0.05mm 精度 / Qi 无线 / 磁感应唤醒全部视觉不可达** |

**整体观察(9 张图统计)**:
- A/B 视觉互换 ≥ 4 张(沙黄硅胶水滴 vs 钛灰铝合金鹅卵石,prompt 区分不了)
- 0.1mm / 0.05mm 精度数字**全部视觉化不了**
- 功能细节(Qi 无线充电、磁感应唤醒、IPX7、IPX4 防水)全部**视觉不可达**
- surprise 时刻(0.5s micro-flash 暗示)全部**未表达**

**这印证了 V2.3.0 自己的 pitfall-039**:`AI(Lovart Nano Banana Pro)真实
水平 4-5/10,材料质感/制造精度/功能细节/边缘清晰度 全部上不去` —— 但
是**这是 Lovart 系统性局限,不是 SKILL.md 写得烂**。

## 根因(3 段断链)

```
SkillOpt 训练 → 改 SKILL.md → 改 prompt → Lovart 黑盒出图 → 真视觉评审
       ↑                                                      ↑
   judge LLM 文本打分(看不到图)                  真实改进无法被 SkillOpt 测量
```

SkillOpt 只能优化**左半链**(SKILL.md → prompt)。**右半链**(Lovart 视觉
权重分配)是它自己的黑盒,改 SKILL.md 不能触及。

## 该走的路(替代方案,已验证可行)

**对照实验 + 真人评审**(V4.16 终结交付步),不要 SkillOpt:

1. 选 3 个有代表性 brief(简易 / 难 / 手持长时长 8h+)
2. **当前 SKILL.md** 跑一轮 baseline(3 方向 × 3 张 = 9 张)
3. 选**1 个原子改动**(加 1 个维度 / 强制 1 个 prompt 字段)
4. **改动后 SKILL.md** 再跑同样 3 brief(再 9 张)
5. 你真人评 9 维 × 2 轮 = 18 次评分
6. diff 两份 SKILL.md → 归因分数差距到具体改动

**成本**:18 张图 + 18 次真人评分,1-2 小时,**原子级归因**
**vs SkillOpt**:数百次 API 调用,**reward 是文本不是视觉**,0 归因

## 错误做法(2026-06-23 我差点犯的 2 个)

1. **列 4 个 choice 问用户"你说的 8 分是什么意思"** —— 反而绕弯。直接
   问"是这一轮就要 8/10,还是更新后下一轮的目标?" 一句话
2. **看到 9 张图都失败就自动否决 SkillOpt 训练** —— 用户的"全部不行 +
   8 分 = 下一轮目标"是合理诉求,不要长 lecture,直接进 1 段说明 + 接
   意图声明 + 安全闸

## 给后续 session 的硬规则

- 用户说"用 SkillOpt 训练提升出图质量" → **先读
  `references/when-to-use-for-image-skills.md`(skillopt)**,5 秒内能回
- 不要自动否决,但**必须**让用户先写意图声明(Q1-Q5),再跑
- 如果 baseline 4-5/10,**对 SkillOpt 训练后达 8/10 的期望必须有保留**:
  SkillOpt 不能突破 Lovart 黑盒
- 真要突破 4-5/10,换模型(Midjourney v6 / DALL-E 3 / Flux Pro 1.1)或
  换路径(3D 渲染 / ControlNet)

## 数据存档

本次 9 张图 + 完整 STEP-01~15 决策链 + 6 个 prompt + 评分卡 template 全部
留在 sandbox:

```
~/.hermes/sandboxes/jony-design2me-v2-baseline-2026-06-23/
├── PHASE-0-baseline.md
├── PHASE-1-scorecard-template.md
├── PHASE-0-INTENT-DECLARATION.md
├── runs/v0-baseline/brief-1-camping-lantern/
│   ├── decision-log/STEP-01-to-15.md
│   ├── prompts/brief-1-three-directions.md
│   ├── prompts/commands.md
│   ├── images/  (9 张 PNG)
│   └── scoring/brief-1-baseline-scores.md
└── skillopt-runs/v1-skillopt/
    ├── config.yaml (minimax_chat, edit_budget 2%, max_steps 10)
    ├── trajectories/trajectories.jsonl (30 条: baseline+失败+红线)
    ├── run-skillopt.sh (一键启动)
    └── README.sh (启动说明)
```

## 关联 pitfalls

- `pitfall-019-prompt-output-empirical-validation.md` — 禁止编造评分、文字
  评审替代真图对比
- `pitfall-039-real-evaluation-standard.md` — 诚实报告 AI 真实水平 4-5/10
- `pitfall-002-image-view-failure-loop.md` — 出图后用桌面查看器,不要
  browser file://
