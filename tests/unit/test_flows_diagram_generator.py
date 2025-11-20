from pathlib import Path

from pd152_compliance_as_code.generators.flows_diagram import generate_mermaid
from pd152_compliance_as_code.yaml_schema.loader import load_config


def test_mermaid_output(tmp_path: Path):
    cfg = load_config(Path("src/pd152_compliance_as_code/yaml_schema/examples/simple_online_shop.yaml"))
    out = tmp_path / "flows.mmd"
    generate_mermaid(cfg, out)
    content = out.read_text(encoding="utf-8")
    assert "graph LR" in content
