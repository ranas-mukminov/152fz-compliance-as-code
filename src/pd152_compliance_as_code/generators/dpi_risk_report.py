from __future__ import annotations

from pathlib import Path
from typing import List

from pd152_compliance_as_code.domain.models import ComplianceConfig
from pd152_compliance_as_code.risk_engine.mapper import RiskProfile


def generate_dpi_report(config: ComplianceConfig, profile: RiskProfile, output_path: str | Path) -> Path:
    lines: List[str] = []
    lines.append("# DPIA-лайт отчёт")
    lines.append("")
    lines.append(f"Оператор: {config.operator.name}")
    if config.operator.contacts.email:
        lines.append(f"Контакт: {config.operator.contacts.email}")
    lines.append("")
    lines.append("## Итоги по процессам")
    for assessment in profile.assessments:
        lines.append(f"### {assessment.activity.name} ({assessment.activity.id})")
        lines.append(f"Уровень риска: {assessment.score.level}")
        lines.append("Причины:")
        for reason in assessment.score.reasons or ["не указаны"]:
            lines.append(f"- {reason}")
        lines.append("Рекомендуемые меры:")
        for control in assessment.recommended_controls:
            lines.append(f"- {control.description} ({control.type})")
        lines.append("")

    lines.append("## Общие рекомендации")
    lines.append(
        "- Регулярно пересматривать сроки хранения и минимизировать перечень собираемых данных."
    )
    lines.append("- Усилить контроль доступа и журналирование для процессов с повышенным риском.")
    lines.append("- Согласовать тексты документов с юристом.")

    out = Path(output_path)
    out.write_text("\n".join(lines), encoding="utf-8")
    return out
