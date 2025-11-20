from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

import yaml

from pd152_compliance_as_code.ai.base import AIProvider


@dataclass
class DraftConfig:
    subjects: List[str] = field(default_factory=list)
    categories: List[str] = field(default_factory=list)
    purposes: List[str] = field(default_factory=list)
    measures: List[str] = field(default_factory=list)


KEYWORDS = {
    "patients": "пациент",
    "customers": "покупател",
    "employees": "сотрудник",
    "marketing": "маркетинг",
    "backup": "резерв"
}


def extract_structure_from_policy(text: str) -> DraftConfig:
    lower = text.lower()
    draft = DraftConfig()
    if "пациент" in lower:
        draft.subjects.append("patients")
        draft.categories.append("health_data")
        draft.purposes.append("оказание медицинских услуг")
    if "покупател" in lower or "заказ" in lower:
        draft.subjects.append("customers")
        draft.categories.append("contact_data")
        draft.purposes.append("исполнение договора")
    if "маркетинг" in lower or "рассыл" in lower:
        draft.purposes.append("маркетинг и рассылки")
    if "резерв" in lower:
        draft.measures.append("резервное копирование")
    if "шифр" in lower:
        draft.measures.append("шифрование")
    return draft


def draft_yaml_from_policy(text: str, provider: AIProvider | None = None) -> str:
    draft = extract_structure_from_policy(text)
    config = {
        "operator": {"name": "Заполните название"},
        "data_subjects": [{"id": s, "name": s} for s in draft.subjects] or [{"id": "subject", "name": "Субъект"}],
        "personal_data_categories": [{"id": c, "name": c, "fields": ["уточнить"]} for c in draft.categories] or [
            {"id": "contact_data", "name": "Контактные данные", "fields": ["ФИО", "email"]}
        ],
        "processing_activities": [
            {
                "id": "process_1",
                "name": "Определите название процесса",
                "subjects": [s for s in draft.subjects] or ["subject"],
                "data_categories": [c for c in draft.categories] or ["contact_data"],
                "purposes": draft.purposes or ["уточните цели"],
                "legal_basis": ["согласие"],
                "operations": ["сбор", "запись", "хранение"],
                "retention": {"description": "уточнить сроки"},
                "security_measures": {"org": [], "tech": draft.measures},
            }
        ],
    }
    return yaml.safe_dump(config, allow_unicode=True, sort_keys=False)
