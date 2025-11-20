from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Control:
    id: str
    description: str
    type: str  # org | tech | legal
    lowers: List[str]


CONTROLS: List[Control] = [
    Control(id="rbac", description="Разграничение прав доступа и ролей", type="org", lowers=["probability"]),
    Control(id="encryption", description="Шифрование в хранении и передаче", type="tech", lowers=["impact", "probability"]),
    Control(id="backup", description="Резервное копирование и проверка восстановления", type="tech", lowers=["impact"]),
    Control(id="logging", description="Журналирование доступа и действий", type="tech", lowers=["probability"]),
    Control(id="dpa", description="Договор с обработчиками (DPA) и проверка мер", type="legal", lowers=["probability"]),
]


def baseline_controls() -> List[Control]:
    return list(CONTROLS)
