# Jony Ive Design2Me V2

证据驱动的十五步产品设计工作流。技能会逐步交付可审计判断、三个本质不同的完整方向、DesignIR、审美质量门，以及可追溯的中文绘画提示词。

## 安装

将本仓库克隆到 Codex 技能目录：

```bash
git clone https://github.com/EasonYinY/jony-ive-design2me-v2.git ~/.codex/skills/jony-ive-design2me-v2
```

重新启动 Codex，使技能被重新发现。

## 使用边界

- 默认在三个方向的提示词交付后停止，不自动生成图片。
- 只有用户明确要求出图、绘制、生成图片或渲染时，才允许调用图像生成工具。
- 每个方向都必须独立推导，并在关系、结构和操作上保持本质差异。
- 事实、推断、假设、未知项与禁止内容必须分区。
- 本技能不进行人物扮演或表面风格模仿。

完整入口见 [SKILL.md](SKILL.md)，引用总索引见 [references/README.md](references/README.md)。

## 验证

```bash
python3 scripts/validate_skill.py .
python3 scripts/validate_reference_graph.py .
```

两项命令均应以退出码 `0` 完成。
