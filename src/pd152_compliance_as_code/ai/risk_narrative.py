from __future__ import annotations

from typing import List

from pd152_compliance_as_code.risk_engine.mapper import RiskAssessment, RiskProfile


def narrative_for_assessment(assessment: RiskAssessment) -> str:
    parts: List[str] = []
    parts.append(f"Процесс {assessment.activity.name} имеет риск {assessment.score.level}.")
    if assessment.score.reasons:
        parts.append("Причины: " + "; ".join(assessment.score.reasons))
    if assessment.recommended_controls:
        measures = ", ".join(c.description for c in assessment.recommended_controls)
        parts.append(f"Рекомендуемые меры: {measures}.")
    return " ".join(parts)


def summarize(profile: RiskProfile) -> List[str]:
    return [narrative_for_assessment(a) for a in profile.assessments]
