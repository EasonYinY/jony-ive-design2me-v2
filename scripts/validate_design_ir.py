#!/usr/bin/env python3
"""验证三个 DesignIR 与三个 PromptBundle 的完整性和一致性。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Mapping, Tuple

import contracts


def validate_design_ir_set(
    design_irs: Tuple[contracts.DesignIR, ...],
    prompt_bundles: Tuple[contracts.PromptBundle, ...],
) -> Tuple[contracts.DesignIR, ...]:
    """验证三个独立方向及提示词包，不修改任何输入对象。"""

    if not isinstance(design_irs, tuple) or len(design_irs) != 3:
        raise ValueError("必须提交恰好三个不可变的 DesignIR。")
    if not isinstance(prompt_bundles, tuple) or len(prompt_bundles) != 3:
        raise ValueError("必须提交恰好三个不可变的 PromptBundle。")
    if not all(isinstance(item, contracts.DesignIR) for item in design_irs):
        raise TypeError("每个方向都必须是 DesignIR。")
    if not all(isinstance(item, contracts.PromptBundle) for item in prompt_bundles):
        raise TypeError("每个提示词包都必须是 PromptBundle。")

    direction_ids = tuple(item.direction_id for item in design_irs)
    if len(set(direction_ids)) != 3:
        raise ValueError("三个 DesignIR 必须使用不同的 direction_id。")
    for field_name in ("relationship", "structure", "operation"):
        values = {"".join(getattr(item, field_name).split()).casefold() for item in design_irs}
        if len(values) != 3:
            raise ValueError("三个方向必须在关系、结构和操作方式上本质不同。")

    for design_ir, prompt in zip(design_irs, prompt_bundles, strict=True):
        if prompt.direction_id != design_ir.direction_id:
            raise ValueError("PromptBundle 与 DesignIR 的 direction_id 不一致。")
        required_pairs = (
            (design_ir.relationship, prompt.design_prompt),
            (design_ir.structure, prompt.detail_prompt),
            (design_ir.operation, prompt.use_context_prompt),
        )
        if not all(value in text for value, text in required_pairs):
            raise ValueError("PromptBundle 未完整保留 DesignIR 的关系、结构或操作。")
        trace_values = {
            field_name: source_value
            for item in prompt.prompt_trace
            for field_name, source_value in zip(
                item.source_fields, item.source_values, strict=True
            )
        }
        for field_name in ("form_proportion", "cmf_system", "resting_state"):
            if trace_values.get(field_name) != getattr(design_ir, field_name):
                raise ValueError(f"PromptBundle 追溯与 {field_name} 不一致。")
        if "不得新增" not in prompt.negative_prompt:
            raise ValueError("PromptBundle 缺少禁止新增产品定义的反向约束。")
    return design_irs


def _make_design_ir(data: Mapping[str, object]) -> contracts.DesignIR:
    return contracts.DesignIR(
        direction_id=data["direction_id"],
        relationship=data["relationship"],
        structure=data["structure"],
        operation=data["operation"],
        form_proportion=data["form_proportion"],
        cmf_system=data["cmf_system"],
        resting_state=data["resting_state"],
        ergonomics=data["ergonomics"],
        materials=data["materials"],
        manufacturing=data["manufacturing"],
        interaction=data["interaction"],
        maintenance=data["maintenance"],
        distinctive_features=tuple(data["distinctive_features"]),
    )


def _make_prompt_bundle(data: Mapping[str, object]) -> contracts.PromptBundle:
    controls_data = data["photography_controls"]
    controls = contracts.PhotographyControls(
        camera_view=controls_data["camera_view"],
        composition=controls_data["composition"],
        lighting=controls_data["lighting"],
        background=controls_data["background"],
        depth_of_field=controls_data["depth_of_field"],
        visibility_targets=tuple(controls_data["visibility_targets"]),
    )
    prompt_trace = tuple(
        contracts.PromptTraceEntry(
            sentence=item["sentence"],
            source_fields=tuple(item["source_fields"]),
            source_values=tuple(item["source_values"]),
        )
        for item in data["prompt_trace"]
    )
    return contracts.PromptBundle(
        direction_id=data["direction_id"],
        design_prompt=data["design_prompt"],
        detail_prompt=data["detail_prompt"],
        use_context_prompt=data["use_context_prompt"],
        negative_prompt=data["negative_prompt"],
        photography_controls=controls,
        production_prompt=data["production_prompt"],
        prompt_trace=prompt_trace,
    )


def validate_payload(payload: Mapping[str, object]) -> Tuple[contracts.DesignIR, ...]:
    """把 JSON 载荷转换为不可变合同后执行同一验证。"""

    directions = payload.get("directions")
    if not isinstance(directions, list):
        raise ValueError("载荷必须包含 directions 数组。")
    design_irs = tuple(_make_design_ir(item["design_ir"]) for item in directions)
    prompts = tuple(_make_prompt_bundle(item["prompt_bundle"]) for item in directions)
    return validate_design_ir_set(design_irs, prompts)


def main() -> int:
    parser = argparse.ArgumentParser(description="验证三个 DesignIR 与 PromptBundle。")
    parser.add_argument("payload", type=Path, help="待验证的 JSON 文件。")
    args = parser.parse_args()
    try:
        payload = json.loads(args.payload.read_text(encoding="utf-8"))
        validate_payload(payload)
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"验证失败：{error}")
        return 1
    print("DesignIR 与 PromptBundle 验证通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
