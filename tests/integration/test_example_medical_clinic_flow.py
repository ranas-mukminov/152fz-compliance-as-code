from pathlib import Path

from pd152_compliance_as_code.yaml_schema.validator import validate_file
from pd152_compliance_as_code.generators.flows_diagram import generate_mermaid
from pd152_compliance_as_code.yaml_schema.loader import load_config


def test_medical_clinic_validation_and_flows(tmp_path: Path):
    example = Path("src/pd152_compliance_as_code/yaml_schema/examples/medical_clinic.yaml")
    errors = validate_file(example)
    assert errors == []
    cfg = load_config(example)
    out = tmp_path / "flows.mmd"
    generate_mermaid(cfg, out)
    assert out.exists()
