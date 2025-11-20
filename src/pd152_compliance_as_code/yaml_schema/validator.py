from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

import jsonschema
import yaml

from pd152_compliance_as_code.domain.models import ComplianceConfig
from pd152_compliance_as_code.yaml_schema.loader import load_config_from_mapping

SCHEMA_PATH = Path(__file__).with_name("schema.yaml")


def _load_schema() -> Dict[str, Any]:
    with SCHEMA_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_mapping(data: Dict[str, Any]) -> List[str]:
    schema = _load_schema()
    errors: List[str] = []
    validator = jsonschema.Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(data), key=lambda e: e.path):
        location = ".".join(str(p) for p in err.path)
        errors.append(f"{location or '<root>'}: {err.message}")
    if errors:
        return errors

    config = load_config_from_mapping(data)
    errors.extend(_validate_references(config))
    return errors


def _validate_references(config: ComplianceConfig) -> List[str]:
    errors: List[str] = []
    subject_ids = {s.id for s in config.data_subjects}
    category_ids = {c.id for c in config.personal_data_categories}
    for activity in config.processing_activities:
        missing_subj = [sid for sid in activity.subjects if sid not in subject_ids]
        if missing_subj:
            errors.append(f"processing_activities.{activity.id}.subjects refers to unknown ids: {missing_subj}")
        missing_cat = [cid for cid in activity.data_categories if cid not in category_ids]
        if missing_cat:
            errors.append(f"processing_activities.{activity.id}.data_categories refers to unknown ids: {missing_cat}")
        if not activity.purposes:
            errors.append(f"processing_activities.{activity.id}.purposes must not be empty")
        if not activity.legal_basis:
            errors.append(f"processing_activities.{activity.id}.legal_basis must not be empty")
    return errors


def validate_file(path: str | Path) -> List[str]:
    with Path(path).open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        return ["YAML root must be a mapping"]
    return validate_mapping(data)
