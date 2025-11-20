from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from pd152_compliance_as_code.domain.models import ComplianceConfig, ProcessingActivity


RISK_MATRIX = {
    ("low", "low"): "low",
    ("low", "medium"): "medium",
    ("low", "high"): "medium",
    ("medium", "low"): "medium",
    ("medium", "medium"): "medium",
    ("medium", "high"): "high",
    ("high", "low"): "medium",
    ("high", "medium"): "high",
    ("high", "high"): "high",
}


@dataclass
class RiskScore:
    activity_id: str
    probability: str
    impact: str
    level: str
    reasons: List[str] = field(default_factory=list)


SPECIAL_KEYWORDS = {"special", "biometric"}


def _impact(activity: ProcessingActivity, config: ComplianceConfig) -> tuple[str, List[str]]:
    reasons: List[str] = []
    impact = "medium"
    for cat_id in activity.data_categories:
        category = config.find_data_category(cat_id)
        if category and category.sensitivity in SPECIAL_KEYWORDS:
            impact = "high"
            reasons.append(f"Категория {cat_id} имеет повышенную чувствительность")
    if len(activity.data_categories) > 3:
        if impact == "medium":
            impact = "high"
            reasons.append("Большой перечень категорий повышает потенциальный ущерб")
    return impact, reasons


def _probability(activity: ProcessingActivity) -> tuple[str, List[str]]:
    probability = "medium"
    reasons: List[str] = []
    if len(activity.recipients) > 2:
        probability = "high"
        reasons.append("Много получателей/третьих лиц")
    if any("за руб" in loc.lower() or "не rf" in loc.lower() for loc in activity.storage_locations):
        probability = "high"
        reasons.append("Есть хранение или передача вне РФ")
    if "передача" in activity.operations and probability != "high":
        probability = "medium"
        reasons.append("Есть внешняя передача")
    if not activity.security_measures.tech:
        probability = "high"
        reasons.append("Не указаны технические меры")
    return probability, reasons


def evaluate_activity(activity: ProcessingActivity, config: ComplianceConfig) -> RiskScore:
    impact, impact_reasons = _impact(activity, config)
    probability, prob_reasons = _probability(activity)
    level = RISK_MATRIX.get((probability, impact), "medium")
    return RiskScore(
        activity_id=activity.id,
        probability=probability,
        impact=impact,
        level=level,
        reasons=impact_reasons + prob_reasons,
    )
