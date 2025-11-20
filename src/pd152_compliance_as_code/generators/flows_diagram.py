from __future__ import annotations

from pathlib import Path
from typing import List, Set

from pd152_compliance_as_code.domain.models import ComplianceConfig


MERMAID_HEADER = "graph LR"


def generate_mermaid(config: ComplianceConfig, output_path: str | Path) -> Path:
    lines: List[str] = [MERMAID_HEADER]
    declared_nodes: Set[str] = set()

    def ensure_node(node_id: str, label: str) -> None:
        if node_id not in declared_nodes:
            lines.append(f"{node_id}[{label}]")
            declared_nodes.add(node_id)

    for activity in config.processing_activities:
        act_id = activity.id.replace(" ", "_")
        ensure_node(act_id, activity.name)
        for subject in activity.subjects:
            subj_id = subject.replace(" ", "_")
            ensure_node(subj_id, f"Субъект: {subject}")
            lines.append(f"{subj_id} -->|{activity.name}| {act_id}")
        for recipient in activity.recipients or ["operator"]:
            rec_id = recipient.replace(" ", "_")
            ensure_node(rec_id, recipient)
            lines.append(f"{act_id} -->|передача| {rec_id}")
        for storage in activity.storage_locations:
            storage_id = storage.replace(\" \", \"_\")
            ensure_node(storage_id, f\"Хранение: {storage}\")
            lines.append(f\"{act_id} -->|хранение| {storage_id}\")
        for category in activity.data_categories:
            cat_id = category.replace(\" \", \"_\")
            ensure_node(cat_id, f\"Категория: {category}\")
            lines.append(f\"{act_id} -->|данные| {cat_id}\")

    out = Path(output_path)
    out.write_text(\"\\n\".join(lines), encoding=\"utf-8\")
    return out
