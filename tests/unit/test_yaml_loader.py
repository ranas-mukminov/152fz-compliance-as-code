from pathlib import Path

from pd152_compliance_as_code.yaml_schema.loader import load_config

def test_load_example_shop():
    cfg = load_config(Path("src/pd152_compliance_as_code/yaml_schema/examples/simple_online_shop.yaml"))
    assert cfg.operator.name.startswith("ООО")
    assert cfg.processing_activities[0].id == "order_processing"
