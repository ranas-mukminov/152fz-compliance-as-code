from __future__ import annotations

from pathlib import Path

import typer

from pd152_compliance_as_code.generators.consents_docx import generate_consents
from pd152_compliance_as_code.generators.dpa_docx import generate_dpa
from pd152_compliance_as_code.generators.dpi_risk_report import generate_dpi_report
from pd152_compliance_as_code.generators.flows_diagram import generate_mermaid
from pd152_compliance_as_code.generators.register_docx import generate_register
from pd152_compliance_as_code.risk_engine.mapper import build_risk_profile
from pd152_compliance_as_code.yaml_schema.loader import load_config
from pd152_compliance_as_code.yaml_schema.validator import validate_file


def command(
    config: str = typer.Option(..., "--config", help="Path to YAML config"),
    output: str = typer.Option("out", "--output", help="Output directory"),
    policy_url: str | None = typer.Option(None, help="Link to privacy policy for consents"),
) -> None:
    errors = validate_file(config)
    if errors:
        for err in errors:
            typer.echo(f"ERROR: {err}")
        raise typer.Exit(code=1)

    cfg = load_config(config)
    output_dir = Path(output)
    output_dir.mkdir(parents=True, exist_ok=True)

    register_path = output_dir / "register.docx"
    consents_path = output_dir / "consents.docx"
    dpa_path = output_dir / "dpa.docx"
    flows_path = output_dir / "flows.mmd"
    dpi_path = output_dir / "dpi_report.md"

    profile = build_risk_profile(cfg)

    generate_register(cfg, register_path)
    generate_consents(cfg, None, consents_path, policy_url=policy_url)
    generate_dpa(cfg, None, dpa_path)
    generate_mermaid(cfg, flows_path)
    generate_dpi_report(cfg, profile, dpi_path)

    typer.echo(f"Generated artifacts in {output_dir}")
