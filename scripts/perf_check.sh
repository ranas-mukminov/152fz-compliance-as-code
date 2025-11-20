#!/usr/bin/env bash
set -euo pipefail

python - <<'PY'
import time
import yaml
from pathlib import Path
from pd152_compliance_as_code.yaml_schema.loader import load_config_from_mapping
from pd152_compliance_as_code.yaml_schema.validator import validate_mapping
from pd152_compliance_as_code.generators.register_docx import generate_register
from pd152_compliance_as_code.risk_engine.mapper import build_risk_profile
from pd152_compliance_as_code.generators.dpi_risk_report import generate_dpi_report

count = 100
activities = []
for i in range(count):
    activities.append({
        "id": f"proc_{i}",
        "name": f"Process {i}",
        "subjects": ["customers"],
        "data_categories": ["contact_data"],
        "purposes": ["testing"],
        "legal_basis": ["договор"],
        "operations": ["сбор", "хранение"],
        "retention": {"description": "1 год"}
    })

config = {
    "operator": {"name": "PerfTest LLC"},
    "data_subjects": [{"id": "customers", "name": "Покупатели"}],
    "personal_data_categories": [{"id": "contact_data", "name": "Контакты", "fields": ["ФИО"]}],
    "processing_activities": activities,
}

start = time.time()
errors = validate_mapping(config)
if errors:
    raise SystemExit(errors)
cfg = load_config_from_mapping(config)
profile = build_risk_profile(cfg)
out_dir = Path("out_perf")
out_dir.mkdir(exist_ok=True)
generate_register(cfg, out_dir / "register.docx")
generate_dpi_report(cfg, profile, out_dir / "dpi_report.md")
print(f"Done {count} processes in {time.time() - start:.2f}s")
PY
