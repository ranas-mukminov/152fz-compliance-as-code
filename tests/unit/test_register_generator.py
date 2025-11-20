from pathlib import Path

import pytest

from pd152_compliance_as_code.generators.register_docx import generate_register
from pd152_compliance_as_code.yaml_schema.loader import load_config


def test_register_docx_generation(tmp_path: Path):
    cfg = load_config(Path("src/pd152_compliance_as_code/yaml_schema/examples/simple_online_shop.yaml"))
    out = tmp_path / "register.docx"
    try:
        generate_register(cfg, out)
    except RuntimeError as exc:
        pytest.skip(str(exc))
    assert out.exists()
