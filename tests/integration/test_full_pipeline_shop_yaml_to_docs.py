from pathlib import Path

import pytest

from pd152_compliance_as_code.generators.consents_docx import generate_consents
from pd152_compliance_as_code.generators.dpi_risk_report import generate_dpi_report
from pd152_compliance_as_code.generators.flows_diagram import generate_mermaid
from pd152_compliance_as_code.generators.register_docx import generate_register
from pd152_compliance_as_code.risk_engine.mapper import build_risk_profile
from pd152_compliance_as_code.yaml_schema.loader import load_config
from pd152_compliance_as_code.yaml_schema.validator import validate_file


def test_full_pipeline(tmp_path: Path):
    example = Path("src/pd152_compliance_as_code/yaml_schema/examples/simple_online_shop.yaml")
    errors = validate_file(example)
    assert errors == []
    cfg = load_config(example)
    profile = build_risk_profile(cfg)

    reg = tmp_path / "register.docx"
    cons = tmp_path / "consents.docx"
    flows = tmp_path / "flows.mmd"
    dpi = tmp_path / "dpi.md"

    try:
        generate_register(cfg, reg)
        generate_consents(cfg, None, cons)
    except RuntimeError:
        pytest.skip("Docx backend not available")

    generate_mermaid(cfg, flows)
    generate_dpi_report(cfg, profile, dpi)

    assert reg.exists()
    assert cons.exists()
    assert flows.exists()
    assert dpi.exists()
