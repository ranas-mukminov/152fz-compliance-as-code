"""Static vocabularies for the YAML DSL."""
from __future__ import annotations

from typing import Dict, List

DATA_SUBJECT_TEMPLATES: Dict[str, str] = {
    "customers": "Клиенты и пользователи сервисов",
    "employees": "Сотрудники",
    "candidates": "Кандидаты",
    "students": "Ученики/студенты",
    "patients": "Пациенты",
}

PERSONAL_DATA_CATEGORY_TEMPLATES: Dict[str, Dict[str, str | List[str]]] = {
    "contact_data": {"name": "Контактные данные", "fields": ["ФИО", "телефон", "email"]},
    "identity_docs": {"name": "Документы, удостоверяющие личность", "fields": ["паспорт", "СНИЛС"]},
    "health_data": {"name": "Данные о здоровье", "fields": ["диагноз", "анамнез"], "sensitivity": "special"},
    "biometric": {"name": "Биометрические данные", "fields": ["фото", "видео"], "sensitivity": "biometric"},
}

LEGAL_BASES: List[str] = ["согласие", "договор", "закон", "жизненно важные интересы"]

OPERATIONS: List[str] = [
    "сбор",
    "запись",
    "систематизация",
    "накопление",
    "хранение",
    "уточнение",
    "использование",
    "передача",
    "обезличивание",
    "блокирование",
    "удаление",
    "уничтожение",
]

SECURITY_MEASURES_ORG: List[str] = [
    "ограничение доступа по ролям",
    "обучение сотрудников",
    "назначение ответственных",
    "политика обработки ПДн",
]

SECURITY_MEASURES_TECH: List[str] = [
    "шифрование на диске",
    "резервное копирование",
    "журналирование доступа",
    "двухфакторная аутентификация",
    "сегментация сети",
]

SECURITY_MEASURES_LEGAL: List[str] = [
    "DPA с обработчиками",
    "NDA с сотрудниками",
    "условия передачи ПДн",
]
