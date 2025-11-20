from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from pd152_compliance_as_code.domain.models import ComplianceConfig, ProcessingActivity
from pd152_compliance_as_code.risk_engine.controls_catalog import Control, baseline_controls
from pd152_compliance_as_code.risk_engine.scoring import RiskScore, evaluate_activity


@dataclass
class RiskAssessment:
    activity: ProcessingActivity
    score: RiskScore
    recommended_controls: List[Control] = field(default_factory=list)


@dataclass
class RiskProfile:
    assessments: List[RiskAssessment]

    def highest_level(self) -> str:
        levels = [a.score.level for a in self.assessments]
        if "high" in levels:
            return "high"
        if "medium" in levels:
            return "medium"
        return "low"


def build_risk_profile(config: ComplianceConfig) -> RiskProfile:
    assessments: List[RiskAssessment] = []
    for activity in config.processing_activities:
        score = evaluate_activity(activity, config)
        controls = _suggest_controls(score)
        assessments.append(RiskAssessment(activity=activity, score=score, recommended_controls=controls))
    return RiskProfile(assessments=assessments)


def _suggest_controls(score: RiskScore) -> List[Control]:
    controls = baseline_controls()
    if score.level == "high":
        return controls
    if score.level == "medium":
        return [c for c in controls if c.type in {"tech", "org"}]
    return [c for c in controls if c.type in {"org"}]
