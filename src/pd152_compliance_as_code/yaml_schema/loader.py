from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import yaml

from pd152_compliance_as_code.domain.models import (
    ComplianceConfig,
    DataSubjectCategory,
    Operator,
    OperatorContacts,
    PersonalDataCategory,
    ProcessingActivity,
    Processor,
    RetentionPolicy,
    SecurityMeasures,
)


def _build_operator(data: Dict[str, Any]) -> Operator:
    contacts = data.get("contacts", {}) or {}
    return Operator(
        name=data["name"],
        inn=data.get("inn"),
        ogrn=data.get("ogrn"),
        contacts=OperatorContacts(
            address=contacts.get("address"),
            email=contacts.get("email"),
            phone=contacts.get("phone"),
            website=contacts.get("website"),
        ),
    )


def _build_processors(items: list[Dict[str, Any]]) -> list[Processor]:
    processors: list[Processor] = []
    for item in items:
        contacts = item.get("contacts", {}) or {}
        processors.append(
            Processor(
                name=item["name"],
                role=item.get("role"),
                contacts=OperatorContacts(
                    address=contacts.get("address"),
                    email=contacts.get("email"),
                    phone=contacts.get("phone"),
                    website=contacts.get("website"),
                ),
            )
        )
    return processors


def _build_subjects(items: list[Dict[str, Any]]) -> list[DataSubjectCategory]:
    return [DataSubjectCategory(id=i["id"], name=i["name"], description=i.get("description")) for i in items]


def _build_data_categories(items: list[Dict[str, Any]]) -> list[PersonalDataCategory]:
    categories: list[PersonalDataCategory] = []
    for item in items:
        categories.append(
            PersonalDataCategory(
                id=item["id"],
                name=item["name"],
                fields=item.get("fields", []),
                sensitivity=item.get("sensitivity", "standard"),
            )
        )
    return categories


def _build_processing_activities(items: list[Dict[str, Any]]) -> list[ProcessingActivity]:
    activities: list[ProcessingActivity] = []
    for item in items:
        retention_raw = item.get("retention", {}) or {}
        security_raw = item.get("security_measures", {}) or {}
        activities.append(
            ProcessingActivity(
                id=item["id"],
                name=item["name"],
                subjects=item.get("subjects", []),
                data_categories=item.get("data_categories", []),
                purposes=item.get("purposes", []),
                legal_basis=item.get("legal_basis", []),
                operations=item.get("operations", []),
                storage_locations=item.get("storage_locations", []),
                recipients=item.get("recipients", []),
                retention=RetentionPolicy(
                    description=retention_raw.get("description", ""),
                    period=retention_raw.get("period"),
                ),
                security_measures=SecurityMeasures(
                    org=security_raw.get("org", []) or [],
                    tech=security_raw.get("tech", []) or [],
                    legal=security_raw.get("legal", []) or [],
                ),
                notes=item.get("notes"),
            )
        )
    return activities


def load_config_from_mapping(data: Dict[str, Any]) -> ComplianceConfig:
    operator = _build_operator(data["operator"])
    processors = _build_processors(data.get("processors", []) or [])
    subjects = _build_subjects(data.get("data_subjects", []) or [])
    data_categories = _build_data_categories(data.get("personal_data_categories", []) or [])
    activities = _build_processing_activities(data.get("processing_activities", []) or [])

    return ComplianceConfig(
        operator=operator,
        processors=processors,
        data_subjects=subjects,
        personal_data_categories=data_categories,
        processing_activities=activities,
    )


def load_config(path: str | Path) -> ComplianceConfig:
    path_obj = Path(path)
    with path_obj.open("r", encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}
    if not isinstance(raw, dict):
        raise ValueError("YAML root must be a mapping")
    return load_config_from_mapping(raw)
