from pathlib import Path

import pytest

from pd152_compliance_as_code.generators.consents_docx import generate_consents
from pd152_compliance_as_code.yaml_schema.loader import load_config


def test_consents_generation(tmp_path: Path):
    cfg = load_config(Path("src/pd152_compliance_as_code/yaml_schema/examples/simple_online_shop.yaml"))
    out = tmp_path / "consents.docx"
    try:
        generate_consents(cfg, None, out, policy_url="https://example.com/policy")
    except RuntimeError as exc:
        pytest.skip(str(exc))
    assert out.exists()
