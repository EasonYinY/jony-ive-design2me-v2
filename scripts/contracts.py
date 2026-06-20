"""五维决策卡与显性步骤记录的确定性合同。"""

from dataclasses import dataclass, fields, replace
from itertools import combinations
from typing import Tuple


EVIDENCE_LEVELS = frozenset({"S", "A", "B", "C", "D", "G", "U"})
CLAIM_CLASSES = frozenset(
    {"FACT", "INFERENCE", "HYPOTHESIS", "PROHIBITED", "GOVERNING"}
)


def _require_text(value: object, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} 必须是非空文本。")


def _require_text_tuple(value: object, field_name: str) -> None:
    if not isinstance(value, tuple) or not value:
        raise ValueError(f"{field_name} 必须是非空且不可变的文本元组。")
    for item in value:
        _require_text(item, field_name)


@dataclass(frozen=True)
class EvidenceClaim:
    """携带 N04 证据类型与来源指针的可追溯证据。"""

    claim_id: str
    claim: str
    claim_class: str
    evidence_level: str
    source_pointer: str
    source: str
    confidence: str
    applicability: str
    prohibited_inferences: Tuple[str, ...]

    def __post_init__(self) -> None:
        for field_name in (
            "claim_id",
            "claim",
            "source_pointer",
            "source",
            "confidence",
            "applicability",
        ):
            _require_text(getattr(self, field_name), field_name)
        if self.claim_class not in CLAIM_CLASSES:
            raise ValueError(f"claim_class 不合法：{self.claim_class}")
        if self.evidence_level not in EVIDENCE_LEVELS:
            raise ValueError(f"evidence_level 不合法：{self.evidence_level}")
        _require_text_tuple(self.prohibited_inferences, "prohibited_inferences")


@dataclass(frozen=True)
class DimensionAssessment:
    """单个维度的判断、证据、风险与状态。"""

    judgment: str
    evidence: Tuple[EvidenceClaim, ...]
    risks: Tuple[str, ...]
    status: str

    def __post_init__(self) -> None:
        _require_text(self.judgment, "judgment")
        _require_text(self.status, "status")
        if not isinstance(self.evidence, tuple) or not self.evidence:
            raise ValueError("evidence 必须是非空且不可变的证据元组。")
        if not all(isinstance(item, EvidenceClaim) for item in self.evidence):
            raise TypeError("evidence 中的每一项都必须是 EvidenceClaim。")
        _require_text_tuple(self.risks, "risks")


@dataclass(frozen=True)
class FiveDimensionCard:
    """每个正式步骤必须完整填写的五维决策卡。"""

    vision_value: DimensionAssessment
    strategy_system: DimensionAssessment
    tools_infrastructure: DimensionAssessment
    execution_tactics: DimensionAssessment
    environment_timing: DimensionAssessment

    def __post_init__(self) -> None:
        for contract_field in fields(self):
            if not isinstance(getattr(self, contract_field.name), DimensionAssessment):
                raise TypeError(
                    f"{contract_field.name} 必须是完整的 DimensionAssessment。"
                )


@dataclass(frozen=True)
class DesignDecisionRecord:
    """一个正式设计步骤的十字段可复核记录。"""

    input: Tuple[str, ...]
    core_question: str
    five_dimension_judgment: FiveDimensionCard
    evidence: Tuple[EvidenceClaim, ...]
    candidates: Tuple[str, ...]
    rejection_reasons: Tuple[str, ...]
    conclusion: str
    unconfirmed_items: Tuple[str, ...]
    status: str
    next_step: str

    def __post_init__(self) -> None:
        for field_name in (
            "input",
            "candidates",
            "rejection_reasons",
            "unconfirmed_items",
        ):
            _require_text_tuple(getattr(self, field_name), field_name)
        for field_name in ("core_question", "conclusion", "status", "next_step"):
            _require_text(getattr(self, field_name), field_name)
        if not isinstance(self.five_dimension_judgment, FiveDimensionCard):
            raise TypeError("five_dimension_judgment 必须是 FiveDimensionCard。")
        if not isinstance(self.evidence, tuple) or not self.evidence:
            raise ValueError("evidence 必须是非空且不可变的证据元组。")
        if not all(isinstance(item, EvidenceClaim) for item in self.evidence):
            raise TypeError("evidence 中的每一项都必须是 EvidenceClaim。")


WORKFLOW_STEP_IDS = tuple(f"STEP-{index:02d}" for index in range(1, 16))


@dataclass(frozen=True)
class WorkflowStepRecord:
    """十五步主流程中一个带强制引用的完整决策记录。"""

    step_id: str
    required_references: Tuple[str, ...]
    decision_record: DesignDecisionRecord

    def __post_init__(self) -> None:
        if self.step_id not in WORKFLOW_STEP_IDS:
            raise ValueError(f"step_id 不合法：{self.step_id}")
        _require_text_tuple(self.required_references, "required_references")
        if len(set(self.required_references)) != len(self.required_references):
            raise ValueError("required_references 不得重复。")
        if not isinstance(self.decision_record, DesignDecisionRecord):
            raise TypeError("decision_record 必须是 DesignDecisionRecord。")


def validate_fifteen_step_reasoning(
    records: Tuple[WorkflowStepRecord, ...],
) -> Tuple[WorkflowStepRecord, ...]:
    """验证 STEP-01 至 STEP-15 顺序完整且每步包含 core 与专业引用。"""

    if not isinstance(records, tuple) or len(records) != len(WORKFLOW_STEP_IDS):
        raise ValueError("必须提交 STEP-01 至 STEP-15 的十五条不可变记录。")
    if not all(isinstance(item, WorkflowStepRecord) for item in records):
        raise TypeError("每一步都必须是 WorkflowStepRecord。")
    if tuple(item.step_id for item in records) != WORKFLOW_STEP_IDS:
        raise ValueError("十五步记录必须按 STEP-01 至 STEP-15 的顺序提交。")
    for record in records:
        if len(record.required_references) < 2:
            raise ValueError(f"{record.step_id} 缺少 core 或专业方法引用。")
    return records


@dataclass(frozen=True)
class DirectionCandidate:
    """STEP-06 至 STEP-09 使用的候选方向，不等同于已完成方向。"""

    candidate_id: str
    relationship: str
    structure: str
    operation: str
    material: str
    process: str
    color: str
    form: str
    constraint_failures: Tuple[str, ...]
    anti_cliche_failures: Tuple[str, ...]

    def __post_init__(self) -> None:
        for contract_field in fields(self):
            value = getattr(self, contract_field.name)
            if contract_field.name.endswith("_failures"):
                if not isinstance(value, tuple):
                    raise TypeError(f"{contract_field.name} 必须是不可变元组。")
                for item in value:
                    _require_text(item, contract_field.name)
            else:
                _require_text(value, contract_field.name)


@dataclass(frozen=True)
class DirectionScreeningResult:
    """方向筛选结果；不合格时显式要求重新生成候选。"""

    selected: Tuple[DirectionCandidate, ...]
    rejected_candidate_ids: Tuple[str, ...]
    regeneration_required: bool
    next_candidate_count: int
    distinct_visual_axes: int
    reasons: Tuple[str, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.selected, tuple) or not all(
            isinstance(item, DirectionCandidate) for item in self.selected
        ):
            raise TypeError("selected 必须是不可变的 DirectionCandidate 元组。")
        if len(self.selected) not in {0, 3}:
            raise ValueError("selected 只能为空或包含三个方向。")
        _require_text_tuple(self.rejected_candidate_ids, "rejected_candidate_ids")
        if not isinstance(self.regeneration_required, bool):
            raise TypeError("regeneration_required 必须是布尔值。")
        if self.next_candidate_count not in range(4, 7):
            raise ValueError("next_candidate_count 必须在 4 至 6 之间。")
        if self.distinct_visual_axes not in range(0, 5):
            raise ValueError("distinct_visual_axes 必须在 0 至 4 之间。")
        _require_text_tuple(self.reasons, "reasons")


def _axis_is_distinct(
    candidates: Tuple[DirectionCandidate, ...], field_name: str
) -> bool:
    return len({_semantic_key(getattr(item, field_name)) for item in candidates}) == 3


def screen_direction_candidates(
    candidates: Tuple[DirectionCandidate, ...],
) -> DirectionScreeningResult:
    """从四至六个候选中选择首个通过约束、反俗套和差异门的三元组。"""

    if not isinstance(candidates, tuple) or len(candidates) not in range(4, 7):
        raise ValueError("STEP-06 必须提交四至六个不可变候选。")
    if not all(isinstance(item, DirectionCandidate) for item in candidates):
        raise TypeError("每个候选都必须是 DirectionCandidate。")
    candidate_ids = tuple(item.candidate_id for item in candidates)
    if len(set(candidate_ids)) != len(candidate_ids):
        raise ValueError("候选必须使用不同的 candidate_id。")

    survivors = tuple(
        item
        for item in candidates
        if not item.constraint_failures and not item.anti_cliche_failures
    )
    rejected = tuple(
        item.candidate_id for item in candidates if item not in survivors
    )
    if len(survivors) < 3:
        return DirectionScreeningResult(
            selected=(),
            rejected_candidate_ids=rejected,
            regeneration_required=True,
            next_candidate_count=max(4, len(candidates)),
            distinct_visual_axes=0,
            reasons=("通过约束与反俗套检查的候选不足三个，必须重新生成。",),
        )

    visual_fields = ("material", "process", "color", "form")
    best_visual_axes = 0
    for group in combinations(survivors, 3):
        selected = tuple(group)
        if not all(
            _axis_is_distinct(selected, field_name)
            for field_name in ("relationship", "structure", "operation")
        ):
            continue
        visual_axes = sum(
            _axis_is_distinct(selected, field_name) for field_name in visual_fields
        )
        best_visual_axes = max(best_visual_axes, visual_axes)
        if visual_axes >= 3:
            selected_ids = {item.candidate_id for item in selected}
            return DirectionScreeningResult(
                selected=selected,
                rejected_candidate_ids=tuple(
                    item.candidate_id
                    for item in candidates
                    if item.candidate_id not in selected_ids
                ),
                regeneration_required=False,
                next_candidate_count=len(candidates),
                distinct_visual_axes=visual_axes,
                reasons=("三个方向通过核心差异门，且四个视觉轴中至少三个分别唯一。",),
            )
    return DirectionScreeningResult(
        selected=(),
        rejected_candidate_ids=candidate_ids,
        regeneration_required=True,
        next_candidate_count=max(4, len(candidates)),
        distinct_visual_axes=best_visual_axes,
        reasons=("没有三元组同时通过核心差异门与视觉差异门，必须重新生成。",),
    )


@dataclass(frozen=True)
class DesignIR:
    """单一方向在进入视觉表达前必须完成的产品设计中间表示。"""

    direction_id: str
    relationship: str
    structure: str
    operation: str
    form_proportion: str
    cmf_system: str
    resting_state: str
    ergonomics: str
    materials: str
    manufacturing: str
    interaction: str
    maintenance: str
    distinctive_features: Tuple[str, ...]

    def __post_init__(self) -> None:
        for contract_field in fields(self):
            if contract_field.name == "distinctive_features":
                _require_text_tuple(
                    self.distinctive_features, "distinctive_features"
                )
            else:
                _require_text(
                    getattr(self, contract_field.name), contract_field.name
                )


AESTHETIC_CRITERIA = frozenset(
    {
        "product_identity",
        "proportion_tension",
        "component_hierarchy",
        "material_honesty",
        "tactile_precision",
        "seam_order",
        "resting_state",
        "ten_year_durability",
    }
)


@dataclass(frozen=True)
class AestheticCriterionAssessment:
    """一项指向 DesignIR 或可见图像证据的审美判断。"""

    criterion: str
    judgment: str
    evidence_pointer: str
    passed: bool

    def __post_init__(self) -> None:
        if self.criterion not in AESTHETIC_CRITERIA:
            raise ValueError(f"criterion 不在审美质量门中：{self.criterion}")
        _require_text(self.judgment, "judgment")
        _require_text(self.evidence_pointer, "evidence_pointer")
        if not self.evidence_pointer.startswith(("design_ir.", "image.")):
            raise ValueError("evidence_pointer 必须指向 DesignIR 或可见图像证据。")
        if not isinstance(self.passed, bool):
            raise TypeError("passed 必须是布尔值。")


@dataclass(frozen=True)
class AestheticQualityResult:
    """八项审美检查的不可变质量门结果。"""

    direction_id: str
    outcome: str
    assessments: Tuple[AestheticCriterionAssessment, ...]
    failed_criteria: Tuple[str, ...]

    def __post_init__(self) -> None:
        _require_text(self.direction_id, "direction_id")
        if self.outcome not in {"PASS", "RETURN_TO_DIRECTION_DEVELOPMENT"}:
            raise ValueError(f"审美质量门 outcome 不合法：{self.outcome}")
        if not isinstance(self.assessments, tuple) or not all(
            isinstance(item, AestheticCriterionAssessment)
            for item in self.assessments
        ):
            raise TypeError("assessments 必须是不可变的审美判断元组。")
        if not isinstance(self.failed_criteria, tuple):
            raise TypeError("failed_criteria 必须是不可变元组。")


def evaluate_aesthetic_quality(
    design_ir: DesignIR,
    assessments: Tuple[AestheticCriterionAssessment, ...],
) -> AestheticQualityResult:
    """仅在八项检查完整且全部通过时放行方向。"""

    if not isinstance(design_ir, DesignIR):
        raise TypeError("design_ir 必须是 DesignIR。")
    if not isinstance(assessments, tuple) or not all(
        isinstance(item, AestheticCriterionAssessment) for item in assessments
    ):
        raise TypeError("assessments 必须是不可变的审美判断元组。")
    criteria = tuple(item.criterion for item in assessments)
    if len(criteria) != len(AESTHETIC_CRITERIA) or set(criteria) != AESTHETIC_CRITERIA:
        raise ValueError("必须完整且不重复地提交八项审美检查。")
    failed = tuple(item.criterion for item in assessments if not item.passed)
    return AestheticQualityResult(
        direction_id=design_ir.direction_id,
        outcome="PASS" if not failed else "RETURN_TO_DIRECTION_DEVELOPMENT",
        assessments=assessments,
        failed_criteria=failed,
    )


DIRECTION_STATES = frozenset({"DRAFT", "EXPLORING", "BLOCKED", "IR_READY"})
DIRECTION_TRANSITIONS = {
    "DRAFT": frozenset({"EXPLORING", "BLOCKED"}),
    "EXPLORING": frozenset({"IR_READY", "BLOCKED"}),
    "BLOCKED": frozenset({"EXPLORING"}),
    "IR_READY": frozenset(),
}

CAMERA_VIEWS = frozenset({"overview", "three_quarter", "side", "detail", "use_state"})
COMPOSITIONS = frozenset({"single_product", "orthographic", "detail", "use_sequence"})
LIGHTING_MODES = frozenset({"neutral_soft", "directional_raking", "diffuse_daylight"})
BACKGROUNDS = frozenset({"pure_white", "neutral_gray", "verified_context"})
DEPTH_OF_FIELD_MODES = frozenset({"deep", "moderate", "shallow_detail"})
VISIBILITY_TARGETS = frozenset(
    {
        "relationship",
        "structure",
        "operation",
        "form_proportion",
        "cmf_system",
        "resting_state",
        "ergonomics",
        "materials",
        "manufacturing",
        "interaction",
        "maintenance",
        "distinctive_features",
    }
)

PROMPT_TRACE_SOURCES = frozenset(
    {
        "relationship",
        "structure",
        "operation",
        "form_proportion",
        "cmf_system",
        "resting_state",
        "ergonomics",
        "materials",
        "manufacturing",
        "interaction",
        "maintenance",
        "distinctive_features",
        "photography_controls",
    }
)


@dataclass(frozen=True)
class PromptTraceEntry:
    """生产提示词中一个语义短句的不可变来源记录。"""

    sentence: str
    source_fields: Tuple[str, ...]
    source_values: Tuple[str, ...]

    def __post_init__(self) -> None:
        _require_text(self.sentence, "sentence")
        _require_text_tuple(self.source_fields, "source_fields")
        _require_text_tuple(self.source_values, "source_values")
        if len(self.source_fields) != len(self.source_values):
            raise ValueError("source_fields 与 source_values 必须一一对应。")
        if not set(self.source_fields).issubset(PROMPT_TRACE_SOURCES):
            raise ValueError("source_fields 只能引用 DesignIR 或封闭摄影控制。")


@dataclass(frozen=True)
class PhotographyControls:
    """只能提高 Design IR 可见度的封闭摄影控制。"""

    camera_view: str
    composition: str
    lighting: str
    background: str
    depth_of_field: str
    visibility_targets: Tuple[str, ...]

    def __post_init__(self) -> None:
        allowed_values = {
            "camera_view": CAMERA_VIEWS,
            "composition": COMPOSITIONS,
            "lighting": LIGHTING_MODES,
            "background": BACKGROUNDS,
            "depth_of_field": DEPTH_OF_FIELD_MODES,
        }
        for field_name, allowed in allowed_values.items():
            value = getattr(self, field_name)
            if value not in allowed:
                raise ValueError(f"{field_name} 不是允许的摄影控制值：{value}")
        _require_text_tuple(self.visibility_targets, "visibility_targets")
        if not set(self.visibility_targets).issubset(VISIBILITY_TARGETS):
            raise ValueError("visibility_targets 只能引用 Design IR 的既有字段。")


@dataclass(frozen=True)
class PromptBundle:
    """单一已验证方向的完整且不可变提示词包。"""

    direction_id: str
    design_prompt: str
    detail_prompt: str
    use_context_prompt: str
    negative_prompt: str
    photography_controls: PhotographyControls
    production_prompt: str
    prompt_trace: Tuple[PromptTraceEntry, ...]

    def __post_init__(self) -> None:
        for field_name in (
            "direction_id",
            "design_prompt",
            "detail_prompt",
            "use_context_prompt",
            "negative_prompt",
            "production_prompt",
        ):
            _require_text(getattr(self, field_name), field_name)
        if not isinstance(self.photography_controls, PhotographyControls):
            raise TypeError("photography_controls 必须是 PhotographyControls。")
        prompt_length = len("".join(self.production_prompt.split()))
        if not 90 <= prompt_length <= 160:
            raise ValueError("production_prompt 必须为 90 至 160 个非空白字符。")
        if not isinstance(self.prompt_trace, tuple) or not self.prompt_trace:
            raise ValueError("prompt_trace 必须是非空不可变元组。")
        if not all(isinstance(item, PromptTraceEntry) for item in self.prompt_trace):
            raise TypeError("prompt_trace 中每一项都必须是 PromptTraceEntry。")
        if not all(item.sentence in self.production_prompt for item in self.prompt_trace):
            raise ValueError("prompt_trace 短句必须完整出现在 production_prompt 中。")
        traced_fields = {
            field_name for item in self.prompt_trace for field_name in item.source_fields
        }
        required_fields = {
            "relationship",
            "structure",
            "form_proportion",
            "cmf_system",
            "operation",
            "resting_state",
            "photography_controls",
        }
        if not required_fields.issubset(traced_fields):
            raise ValueError("prompt_trace 未覆盖精简生产提示词的全部必需来源。")


IMAGE_FAILURE_CODES = frozenset(
    {
        "structural_misread",
        "material_fabrication",
        "operation_invisible",
        "direction_homogenization",
        "apple_shell",
        "unsupported_text_label",
        "resting_state_invisible",
    }
)
IMAGE_VISIBLE_CHECKS = frozenset(
    {
        "direction_identity",
        "design_ir_consistency",
        "prompt_consistency",
        "visible_expression",
    }
)
PRODUCT_CONFLICT_CODES = frozenset(
    {
        "structural_misread",
        "material_fabrication",
        "direction_homogenization",
        "apple_shell",
    }
)


@dataclass(frozen=True)
class ImageFailureFinding:
    """一项有可见证据的图片失败，不包含新的产品处方。"""

    failure_code: str
    observation: str
    evidence: str

    def __post_init__(self) -> None:
        if self.failure_code not in IMAGE_FAILURE_CODES:
            raise ValueError(f"failure_code 不在失败库中：{self.failure_code}")
        _require_text(self.observation, "observation")
        _require_text(self.evidence, "evidence")


@dataclass(frozen=True)
class ImageCritique:
    """追溯到同一方向 DesignIR 与 PromptBundle 的图片评审。"""

    direction_id: str
    design_ir: DesignIR
    prompt_bundle: PromptBundle
    visible_checks: Tuple[str, ...]
    findings: Tuple[ImageFailureFinding, ...]

    def __post_init__(self) -> None:
        _require_text(self.direction_id, "direction_id")
        if not isinstance(self.design_ir, DesignIR):
            raise TypeError("design_ir 必须是 DesignIR。")
        if not isinstance(self.prompt_bundle, PromptBundle):
            raise TypeError("prompt_bundle 必须是 PromptBundle。")
        if (
            self.design_ir.direction_id != self.direction_id
            or self.prompt_bundle.direction_id != self.direction_id
        ):
            raise ValueError("direction_id 必须与 DesignIR 和 PromptBundle 一致。")
        _require_text_tuple(self.visible_checks, "visible_checks")
        if not set(self.visible_checks).issubset(IMAGE_VISIBLE_CHECKS):
            raise ValueError("visible_checks 包含未定义的图片评审项。")
        if not isinstance(self.findings, tuple):
            raise TypeError("findings 必须是不可变元组。")
        if not all(isinstance(item, ImageFailureFinding) for item in self.findings):
            raise TypeError("findings 中每一项都必须是 ImageFailureFinding。")
        prompt_checks = (
            (self.design_ir.relationship, self.prompt_bundle.design_prompt),
            (self.design_ir.structure, self.prompt_bundle.detail_prompt),
            (self.design_ir.operation, self.prompt_bundle.use_context_prompt),
        )
        if not all(expected in prompt for expected, prompt in prompt_checks):
            raise ValueError("PromptBundle 与 DesignIR 的关键字段不一致。")
        trace_values = {
            field_name: source_value
            for item in self.prompt_bundle.prompt_trace
            for field_name, source_value in zip(
                item.source_fields, item.source_values, strict=True
            )
        }
        for field_name in ("form_proportion", "cmf_system", "resting_state"):
            if trace_values.get(field_name) != getattr(self.design_ir, field_name):
                raise ValueError(f"PromptBundle 追溯与 {field_name} 不一致。")


@dataclass(frozen=True)
class ImageQualityResult:
    """图片质量门的确定性结果与允许修复边界。"""

    direction_id: str
    design_ir: DesignIR
    prompt_bundle: PromptBundle
    outcome: str
    repair_level: str
    reasons: Tuple[str, ...]
    required_actions: Tuple[str, ...]
    prohibited_actions: Tuple[str, ...]

    def __post_init__(self) -> None:
        for field_name in ("direction_id", "outcome", "repair_level"):
            _require_text(getattr(self, field_name), field_name)
        if not isinstance(self.design_ir, DesignIR):
            raise TypeError("design_ir 必须是 DesignIR。")
        if not isinstance(self.prompt_bundle, PromptBundle):
            raise TypeError("prompt_bundle 必须是 PromptBundle。")
        for field_name in ("reasons", "required_actions", "prohibited_actions"):
            value = getattr(self, field_name)
            if not isinstance(value, tuple):
                raise TypeError(f"{field_name} 必须是不可变元组。")
            if value:
                for item in value:
                    _require_text(item, field_name)


def evaluate_image_quality(critique: ImageCritique) -> ImageQualityResult:
    """按失败库返回表达修复、产品重推导或通过，不修改输入。"""

    if not isinstance(critique, ImageCritique):
        raise TypeError("critique 必须是 ImageCritique。")
    failure_codes = frozenset(item.failure_code for item in critique.findings)
    common_prohibitions = (
        "不得修改 DesignIR",
        "不得用摄影表达改写产品定义",
    )
    if failure_codes & PRODUCT_CONFLICT_CODES:
        return ImageQualityResult(
            direction_id=critique.direction_id,
            design_ir=critique.design_ir,
            prompt_bundle=critique.prompt_bundle,
            outcome="RETURN_TO_PRODUCT_DERIVATION",
            repair_level="DESIGN_IR",
            reasons=("摄影参数不得覆盖产品冲突，必须回到产品推导定位根因。",),
            required_actions=("退回关系、结构、操作与约束推导并重新形成 DesignIR。",),
            prohibited_actions=common_prohibitions,
        )
    if failure_codes:
        return ImageQualityResult(
            direction_id=critique.direction_id,
            design_ir=critique.design_ir,
            prompt_bundle=critique.prompt_bundle,
            outcome="EXPRESSION_REPAIR",
            repair_level="PROMPT_OR_RENDER",
            reasons=("产品定义未发生冲突，但既有操作或标签未被正确表达。",),
            required_actions=("仅修订提示词约束或重新渲染，并复核可见表达。",),
            prohibited_actions=common_prohibitions,
        )
    return ImageQualityResult(
        direction_id=critique.direction_id,
        design_ir=critique.design_ir,
        prompt_bundle=critique.prompt_bundle,
        outcome="PASS",
        repair_level="NONE",
        reasons=("方向标识、DesignIR、PromptBundle 与可见表达未发现冲突。",),
        required_actions=(),
        prohibited_actions=common_prohibitions,
    )


@dataclass(frozen=True)
class DirectionBundle:
    """一个方向的隔离输入、推导证据、决策记录与 Design IR。"""

    direction_id: str
    inputs: Tuple[str, ...]
    evidence: Tuple[EvidenceClaim, ...]
    candidates: Tuple[str, ...]
    rejection_reasons: Tuple[str, ...]
    decision_record: DesignDecisionRecord
    design_ir: DesignIR
    status: str
    prompt_bundle: object | None = None

    def __post_init__(self) -> None:
        _require_text(self.direction_id, "direction_id")
        for field_name in ("inputs", "candidates", "rejection_reasons"):
            _require_text_tuple(getattr(self, field_name), field_name)
        if not isinstance(self.evidence, tuple) or not self.evidence:
            raise ValueError("evidence 必须是非空且不可变的证据元组。")
        if not all(isinstance(item, EvidenceClaim) for item in self.evidence):
            raise TypeError("evidence 中的每一项都必须是 EvidenceClaim。")
        if not isinstance(self.decision_record, DesignDecisionRecord):
            raise TypeError("decision_record 必须是 DesignDecisionRecord。")
        if not isinstance(self.design_ir, DesignIR):
            raise TypeError("design_ir 必须是 DesignIR。")
        if self.design_ir.direction_id != self.direction_id:
            raise ValueError("design_ir 与方向的 direction_id 必须一致。")
        if self.status not in DIRECTION_STATES:
            raise ValueError(f"方向状态不合法：{self.status}")
        if self.prompt_bundle is not None:
            raise ValueError(
                "DirectionBundle 不内嵌 PromptBundle；编译器必须单独返回新对象。"
            )


def transition_direction(bundle: DirectionBundle, next_status: str) -> DirectionBundle:
    """按显式状态机返回新方向对象，禁止原地修改或跨阶段跳转。"""

    if not isinstance(bundle, DirectionBundle):
        raise TypeError("bundle 必须是 DirectionBundle。")
    if next_status not in DIRECTION_STATES:
        raise ValueError(f"方向状态不合法：{next_status}")
    if next_status not in DIRECTION_TRANSITIONS[bundle.status]:
        raise ValueError(f"不允许从 {bundle.status} 跳转到 {next_status}。")
    return replace(bundle, status=next_status)


def _semantic_key(value: str) -> str:
    return "".join(value.split()).casefold()


def validate_direction_set(
    bundles: Tuple[DirectionBundle, ...],
) -> Tuple[DirectionBundle, ...]:
    """确认恰有三个独立方向，且关系、结构、操作方式均不重复。"""

    if not isinstance(bundles, tuple) or len(bundles) != 3:
        raise ValueError("必须提交恰好三个不可变的方向。")
    if not all(isinstance(item, DirectionBundle) for item in bundles):
        raise TypeError("每个方向都必须是 DirectionBundle。")
    direction_ids = tuple(item.direction_id for item in bundles)
    if len(set(direction_ids)) != 3:
        raise ValueError("三个方向必须使用不同的 direction_id。")
    for field_name in ("relationship", "structure", "operation"):
        values = {
            _semantic_key(getattr(item.design_ir, field_name)) for item in bundles
        }
        if len(values) != 3:
            raise ValueError("三个方向必须在关系、结构和操作方式上本质不同。")
    return bundles
