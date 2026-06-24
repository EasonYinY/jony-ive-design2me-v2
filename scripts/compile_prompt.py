"""把三个已验证的 Design IR 确定性编译为完整提示词包。"""

from dataclasses import fields
from typing import Tuple

import contracts


DEFAULT_PHOTOGRAPHY_CONTROLS = contracts.PhotographyControls(
    camera_view="three_quarter",
    composition="single_product",
    lighting="neutral_soft",
    background="pure_white",
    depth_of_field="deep",
    visibility_targets=("structure", "materials", "operation"),
)


PHOTOGRAPHY_LABELS = {
    "camera_view": {
        "overview": "整体视角",
        "three_quarter": "三分之四视角",
        "side": "侧视角",
        "detail": "细节视角",
        "use_state": "使用状态视角",
    },
    "composition": {
        "single_product": "单一产品构图",
        "orthographic": "正投影构图",
        "detail": "细节构图",
        "use_sequence": "使用序列构图",
    },
    "lighting": {
        "neutral_soft": "中性柔光",
        "directional_raking": "方向性掠射光",
        "diffuse_daylight": "漫射日光",
    },
    "background": {
        "pure_white": "纯白背景",
        "neutral_gray": "中性灰背景",
        "verified_context": "已确认情境",
    },
    "depth_of_field": {
        "deep": "深景深",
        "moderate": "中等景深",
        "shallow_detail": "细节浅景深",
    },
}


# V3.5.2 视觉等效编译矩阵（Visual Equivalent Wash Matrix）
# 审计报告发现：工程账本数据（寿命、制造方式、维护方式）直接注入提示词
# 对 Nano Banana Pro 造成语义噪音。必须转化为光学物理表征。
VISUAL_EQUIVALENT_MATRIX = {
    # 碳纤维
    "CFRP": "woven carbon fiber superstructure, ultra-matte micro-texture surface, capturing sharp crisp architectural highlights, zero surface oil reflectance",
    "碳纤维": "woven carbon fiber superstructure, ultra-matte micro-texture surface, capturing sharp crisp architectural highlights, zero surface oil reflectance",
    "碳纤维复合材料": "woven carbon fiber superstructure, ultra-matte micro-texture surface, capturing sharp crisp architectural highlights, zero surface oil reflectance",
    # 钛合金
    "titanium alloy": "bead-blasted grade 5 titanium structural rib, seamless solid metal integration, zero tool marks, monolithic precision",
    "钛合金": "bead-blasted grade 5 titanium structural rib, seamless solid metal integration, zero tool marks, monolithic precision",
    # 陶瓷基
    "ceramic matrix composite": "dense ceramic thermal shield, micro-crystalline surface, heat-resistant matte finish, zero oxidation discoloration",
    "陶瓷基复合材料": "dense ceramic thermal shield, micro-crystalline surface, heat-resistant matte finish, zero oxidation discoloration",
    # 超导磁体
    "YBCO": "cryogenic metallic surface, zero-resistance magnetic field containment, mirror-polished cryostat interface",
    "超导磁体": "cryogenic metallic surface, zero-resistance magnetic field containment, mirror-polished cryostat interface",
    # 铝合金
    "aluminum alloy": "precision-machined aluminum monocoque, anodized matte finish, zero visible machining marks",
    "铝合金": "precision-machined aluminum monocoque, anodized matte finish, zero visible machining marks",
    # 气凝胶
    "aerogel": "translucent nano-porous thermal barrier, zero-density visual weight, frosted crystal clarity",
    "气凝胶": "translucent nano-porous thermal barrier, zero-density visual weight, frosted crystal clarity",
    # 芳纶织物
    "aramid fabric": "high-tensile woven textile surface, matte directional grain, zero surface sheen",
    "芳纶织物": "high-tensile woven textile surface, matte directional grain, zero surface sheen",
    # 软木
    "cork": "natural porous cork surface, warm micro-texture, zero synthetic gloss",
    "软木": "natural porous cork surface, warm micro-texture, zero synthetic gloss",
    # 玻璃
    "glass": "chemically strengthened glass slab, zero optical distortion, pristine surface reflectance",
    "玻璃": "chemically strengthened glass slab, zero optical distortion, pristine surface reflectance",
    # 记忆泡沫
    "memory foam": "visco-elastic pressure-responsive surface, zero rebound visual texture, matte skin-contact finish",
    "记忆泡沫": "visco-elastic pressure-responsive surface, zero rebound visual texture, matte skin-contact finish",
}

# 工程管理词汇 → 删除（Drop）
ENGINEERING_NOISE_WORDS = {
    "lifespan", "寿命", "manufacturing", "制造方式", "maintenance", "维护方式",
    "inspection", "检测", "detection", "refurbishment", "翻新", "years", "年",
    "aging", "老化", "degradation", "退化", "quality control", "质量控制",
    "certification", "认证", "standard", "标准", "hot press", "热压罐",
    "CVD", "chemical vapor deposition", "化学气相沉积", "3D print", "3D打印",
    "CNC", "vacuum infusion", "真空灌注", "ultrasonic", "超声波",
    "liquid nitrogen", "液氮", "magnetic field detection", "磁场检测",
}

# 微观尺寸泛化矩阵（Scale Zoom Filter）
# 宏观产品（>1m）自动抑制 <1mm 数字，泛化为视觉信号
MICRO_DIMENSION_MAP = {
    # 原始微观描述 → 泛化后视觉信号
    "0.5mm hairline seam": "hairline shadow line",
    "0.3mm hairline slit": "fine aerodynamic gap",
    "0.1mm LED slit": "subtle light line",
    "0.5mm fillet": "smooth tangent transition",
    "2mm levitation gap": "visual airgap",
    "0.1mm texture": "micro-texture surface",
    "0.3mm intake": "shadow-revealed junction",
    "0.5mm gap": "crisp alignment split",
    "0.1mm precision": "zero-tolerance sealed joint",
}

# 禁止词滤网（Semantic Sanitizer）
SEMANTIC_BANNED_WORDS = {
    # 意识形态/艺术流派
    "侘寂", "赛博朋克", "孟菲斯", "极简主义", "minimalism", "wabi-sabi",
    "cyberpunk", "memphis", "art deco", "bauhaus", "scandinavian",
    # 情感暗示词
    "手工感", "温暖感", "陌生感", "充满信任", "sense of",
    "feeling of", "emotional", "trust", "warmth", "handcrafted",
    "artisanal", "authentic", "premium feel", "luxury touch",
    # 风格抽象词
    "futuristic", "sleek", "high-tech", "sci-fi", "Apple-like",
    "minimalist design", "Jony Ive style", "LoveFrom aesthetic",
    # 动态情感词
    "spinning slowly", "gently hovering", "gracefully flying",
    "elegantly floating", "smoothly gliding",
}


def _without_terminal_punctuation(value: str) -> str:
    return value.strip().rstrip("。！？；;.!?")


def _compact_value(value: str, limit: int) -> str:
    """删除字段名式前缀，并为生产提示词保留固定长度的语义摘要。"""

    compact = "".join(_without_terminal_punctuation(value).split())
    if "：" in compact:
        compact = compact.split("：", 1)[1]
    if len(compact) <= limit:
        return compact
    return f"{compact[: limit - 1]}…"


def _apply_visual_equivalent_wash(text: str) -> str:
    """视觉等效洗涤：将工程账本数据转化为光学物理表征。"""
    # 1. 删除工程管理噪音词汇
    words = text.split()
    filtered = [w for w in words if w.lower() not in ENGINEERING_NOISE_WORDS]
    text = " ".join(filtered)
    
    # 2. 应用材料视觉等效矩阵
    for material, visual_equivalent in VISUAL_EQUIVALENT_MATRIX.items():
        text = text.replace(material, visual_equivalent)
    
    # 3. 应用微观尺寸泛化
    for micro, visual in MICRO_DIMENSION_MAP.items():
        text = text.replace(micro, visual)
    
    # 4. 语义洗涤：删除禁止词
    for banned in SEMANTIC_BANNED_WORDS:
        text = text.replace(banned, "")
    
    return text.strip()


def _apply_scale_zoom_filter(text: str, product_scale: str = "macro") -> str:
    """尺度缩放滤网：宏观产品抑制微观尺寸。"""
    if product_scale not in ("macro", "meso", "micro"):
        product_scale = "macro"
    
    if product_scale == "macro":
        # 宏观产品：抑制 <1mm 数字，泛化为视觉信号
        import re
        # 匹配 0.xmm 模式
        text = re.sub(r'0\.\d+mm', lambda m: MICRO_DIMENSION_MAP.get(m.group(), "hairline shadow line"), text)
        # 匹配 <1mm 模式
        text = re.sub(r'<1mm', "hairline shadow line", text)
    
    return text


def _compile_production_prompt(
    design_ir: contracts.DesignIR,
    controls: contracts.PhotographyControls,
    product_scale: str = "macro",
) -> tuple[str, Tuple[contracts.PromptTraceEntry, ...]]:
    identity_sentence = (
        f"产品以{_compact_value(design_ir.relationship, 8)}为核心关系，"
        f"采用{_compact_value(design_ir.structure, 10)}，"
        f"形态依据{_compact_value(design_ir.form_proportion, 12)}。"
    )
    cmf_sentence = f"差异化 CMF 为{_compact_value(design_ir.cmf_system, 12)}。"
    use_sentence = (
        f"使用时{_compact_value(design_ir.operation, 8)}；静息时"
        f"{_compact_value(design_ir.resting_state, 10)}。"
    )
    photography_values = (
        PHOTOGRAPHY_LABELS["camera_view"][controls.camera_view],
        PHOTOGRAPHY_LABELS["composition"][controls.composition],
        PHOTOGRAPHY_LABELS["lighting"][controls.lighting],
        PHOTOGRAPHY_LABELS["background"][controls.background],
        PHOTOGRAPHY_LABELS["depth_of_field"][controls.depth_of_field],
    )
    photography_sentence = (
        f"以{'、'.join(photography_values)}清晰表达产品关系、结构形态、"
        "差异化 CMF、使用动作与静息状态。"
    )
    
    # 应用视觉等效洗涤和尺度缩放滤网
    raw_prompt = "".join(
        (identity_sentence, cmf_sentence, use_sentence, photography_sentence)
    )
    prompt = _apply_visual_equivalent_wash(raw_prompt)
    prompt = _apply_scale_zoom_filter(prompt, product_scale)
    
    trace = (
        contracts.PromptTraceEntry(
            sentence=identity_sentence,
            source_fields=("relationship", "structure", "form_proportion"),
            source_values=(
                design_ir.relationship,
                design_ir.structure,
                design_ir.form_proportion,
            ),
        ),
        contracts.PromptTraceEntry(
            sentence=cmf_sentence,
            source_fields=("cmf_system",),
            source_values=(design_ir.cmf_system,),
        ),
        contracts.PromptTraceEntry(
            sentence=use_sentence,
            source_fields=("operation", "resting_state"),
            source_values=(design_ir.operation, design_ir.resting_state),
        ),
        contracts.PromptTraceEntry(
            sentence=photography_sentence,
            source_fields=("photography_controls",),
            source_values=("|".join(photography_values),),
        ),
    )
    return prompt, trace


def _validate_complete_ir(design_ir: contracts.DesignIR) -> None:
    if not isinstance(design_ir, contracts.DesignIR):
        raise TypeError("design_ir 必须是 DesignIR。")
    for contract_field in fields(design_ir):
        value = getattr(design_ir, contract_field.name)
        if contract_field.name == "distinctive_features":
            contracts._require_text_tuple(value, contract_field.name)
        else:
            contracts._require_text(value, contract_field.name)


def _compile_one(
    direction: contracts.DirectionBundle,
    controls: contracts.PhotographyControls,
    product_scale: str = "macro",
) -> contracts.PromptBundle:
    design_ir = direction.design_ir
    features = "；".join(design_ir.distinctive_features)
    visible_targets = "、".join(controls.visibility_targets)
    
    # 应用视觉等效洗涤到设计提示词
    design_prompt_raw = (
        f"方向 {design_ir.direction_id}。人与产品的关系：{design_ir.relationship}。"
        f"结构：{design_ir.structure}。操作方式：{design_ir.operation}。"
        f"人体工学：{design_ir.ergonomics}。材料职责：{design_ir.materials}。"
        f"识别特征：{features}。只呈现这些已确认的产品定义。"
    )
    design_prompt = _apply_visual_equivalent_wash(design_prompt_raw)
    design_prompt = _apply_scale_zoom_filter(design_prompt, product_scale)
    
    detail_prompt_raw = (
        f"方向 {design_ir.direction_id} 的结构与细节视图。结构：{design_ir.structure}。"
        f"材料：{design_ir.materials}。制造：{design_ir.manufacturing}。"
        f"维护：{design_ir.maintenance}。清晰显示 {visible_targets}，不添加新构件。"
    )
    detail_prompt = _apply_visual_equivalent_wash(detail_prompt_raw)
    detail_prompt = _apply_scale_zoom_filter(detail_prompt, product_scale)
    
    use_context_prompt = (
        f"方向 {design_ir.direction_id} 的真实使用状态。关系：{design_ir.relationship}。"
        f"操作：{design_ir.operation}。人体工学：{design_ir.ergonomics}。"
        f"交互与反馈：{design_ir.interaction}。环境只用于说明既有动作与状态。"
    )
    
    negative_prompt = (
        "不得新增、删除或改写 Design IR 的关系、结构、构件、操作、材料、工艺与维护路径；"
        "不得使用 Apple-like 外形、白色圆角金属套壳、无依据文字标签、装饰性接口、"
        "不真实连接、悬浮构件或用光效伪造材料品质；不得用机位隐藏产品冲突。"
    )
    
    production_prompt, prompt_trace = _compile_production_prompt(design_ir, controls, product_scale)
    return contracts.PromptBundle(
        direction_id=design_ir.direction_id,
        design_prompt=design_prompt,
        detail_prompt=detail_prompt,
        use_context_prompt=use_context_prompt,
        negative_prompt=negative_prompt,
        photography_controls=controls,
        production_prompt=production_prompt,
        prompt_trace=prompt_trace,
    )


def compile_prompts(
    directions: Tuple[contracts.DirectionBundle, ...],
    photography_controls: contracts.PhotographyControls | None = None,
    product_scale: str = "macro",
) -> Tuple[contracts.PromptBundle, ...]:
    """验证三个 IR_READY 方向后返回三个新 PromptBundle。"""

    if not isinstance(directions, tuple) or len(directions) != 3:
        raise ValueError("必须提交恰好三个不可变的方向。")
    for direction in directions:
        if not isinstance(direction, contracts.DirectionBundle):
            raise TypeError("每个方向都必须是 DirectionBundle。")
        if direction.status != "IR_READY":
            raise ValueError("只有 IR_READY 方向可以编译提示词。")
        _validate_complete_ir(direction.design_ir)
    validated = contracts.validate_direction_set(directions)
    controls = photography_controls or DEFAULT_PHOTOGRAPHY_CONTROLS
    if not isinstance(controls, contracts.PhotographyControls):
        raise TypeError("photography_controls 必须是 PhotographyControls。")
    return tuple(_compile_one(direction, controls, product_scale) for direction in validated)
