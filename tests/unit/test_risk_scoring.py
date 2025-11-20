from pathlib import Path

from pd152_compliance_as_code.risk_engine.scoring import evaluate_activity
from pd152_compliance_as_code.yaml_schema.loader import load_config


def test_special_data_increases_risk():
    cfg = load_config(Path("src/pd152_compliance_as_code/yaml_schema/examples/medical_clinic.yaml"))
    activity = next(a for a in cfg.processing_activities if a.id == "medical_care")
    score = evaluate_activity(activity, cfg)
    assert score.level in {"high", "medium"}
    assert any("Категория" in r for r in score.reasons)
