from pathlib import Path

from typer.testing import CliRunner

from pd152_compliance_as_code.cli.main import app

runner = CliRunner()


def test_validate_command():
    result = runner.invoke(app, ["validate", "--config", "src/pd152_compliance_as_code/yaml_schema/examples/simple_online_shop.yaml"])
    assert result.exit_code == 0
    assert "valid" in result.stdout.lower()


def test_init_template_command(tmp_path: Path):
    out_path = tmp_path / "cfg.yaml"
    result = runner.invoke(app, ["init-template", "--profile", "online-shop", "--output", str(out_path)])
    assert result.exit_code == 0
    assert out_path.exists()
