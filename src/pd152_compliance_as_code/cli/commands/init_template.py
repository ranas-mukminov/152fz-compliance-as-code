from __future__ import annotations

from pathlib import Path
from typing import Dict

import typer
import yaml

TEMPLATES: Dict[str, Dict] = {
    "online-shop": {
        "operator": {"name": "ООО «Пример-Маркет»", "inn": "1234567890"},
        "data_subjects": [{"id": "customers", "name": "Покупатели"}],
        "personal_data_categories": [
            {"id": "contact_data", "name": "Контактные данные", "fields": ["ФИО", "телефон", "email"]}
        ],
        "processing_activities": [
            {
                "id": "orders",
                "name": "Оформление заказов",
                "subjects": ["customers"],
                "data_categories": ["contact_data"],
                "purposes": ["исполнение договора"],
                "legal_basis": ["договор"],
                "operations": ["сбор", "запись", "хранение", "передача"],
                "retention": {"description": "5 лет"},
            }
        ],
    },
    "clinic": {
        "operator": {"name": "ООО «Пример-Клиника»"},
        "data_subjects": [{"id": "patients", "name": "Пациенты"}],
        "personal_data_categories": [
            {"id": "contact_data", "name": "Контактные данные", "fields": ["ФИО", "телефон", "email"]},
            {"id": "health_data", "name": "Данные о здоровье", "fields": ["анамнез", "диагноз"], "sensitivity": "special"},
        ],
        "processing_activities": [
            {
                "id": "medical_care",
                "name": "Медицинская помощь",
                "subjects": ["patients"],
                "data_categories": ["contact_data", "health_data"],
                "purposes": ["оказание медуслуг"],
                "legal_basis": ["закон", "договор"],
                "operations": ["сбор", "запись", "хранение", "передача"],
                "retention": {"description": "сроки по меддокументации"},
            }
        ],
    },
    "school": {
        "operator": {"name": "АНО «Пример-Школа»"},
        "data_subjects": [
            {"id": "students", "name": "Ученики"},
            {"id": "parents", "name": "Родители"},
        ],
        "personal_data_categories": [
            {"id": "contact_data", "name": "Контактные данные", "fields": ["ФИО", "телефон", "email"]},
            {"id": "progress", "name": "Успеваемость", "fields": ["оценки", "комментарии"]},
        ],
        "processing_activities": [
            {
                "id": "education",
                "name": "Организация обучения",
                "subjects": ["students", "parents"],
                "data_categories": ["contact_data", "progress"],
                "purposes": ["учебный процесс"],
                "legal_basis": ["договор", "согласие"],
                "operations": ["сбор", "запись", "хранение", "передача"],
                "retention": {"description": "период обучения + архив"},
            }
        ],
    },
    "saas": {
        "operator": {"name": "ООО «Пример-SaaS»"},
        "data_subjects": [
            {"id": "users", "name": "Пользователи"},
            {"id": "admins", "name": "Администраторы клиентов"},
        ],
        "personal_data_categories": [
            {"id": "contact_data", "name": "Контактные данные", "fields": ["ФИО", "email"]},
            {"id": "usage", "name": "Данные об активности", "fields": ["логи", "метрики"]},
        ],
        "processing_activities": [
            {
                "id": "service",
                "name": "Предоставление SaaS",
                "subjects": ["users", "admins"],
                "data_categories": ["contact_data", "usage"],
                "purposes": ["оказание услуг", "поддержка"],
                "legal_basis": ["договор"],
                "operations": ["сбор", "запись", "хранение", "передача"],
                "retention": {"description": "на период договора"},
            }
        ],
    },
}


def command(profile: str = typer.Option("online-shop", help="Template profile"), output: str = typer.Option("pd-config.yaml", help="Output YAML path")) -> None:
    if profile not in TEMPLATES:
        raise typer.BadParameter(f"Unknown profile {profile}")
    data = TEMPLATES[profile]
    path = Path(output)
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    typer.echo(f"Template saved to {path}")
