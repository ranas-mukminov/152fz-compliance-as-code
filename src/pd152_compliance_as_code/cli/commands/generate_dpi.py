from __future__ import annotations

from pathlib import Path

import typer

from pd152_compliance_as_code.generators.dpi_risk_report import generate_dpi_report
from pd152_compliance_as_code.risk_engine.mapper import build_risk_profile
from pd152_compliance_as_code.yaml_schema.loader import load_config
from pd152_compliance_as_code.yaml_schema.validator import validate_file


def command(config: str = typer.Option(..., "--config", help="Path to YAML config"), output: str = typer.Option("dpi_report.md", "--output", help="Path to Markdown report")) -> None:
    errors = validate_file(config)
    if errors:
        for err in errors:
            typer.echo(f"ERROR: {err}")
        raise typer.Exit(code=1)
    cfg = load_config(config)
    profile = build_risk_profile(cfg)
    generate_dpi_report(cfg, profile, Path(output))
    typer.echo(f"Saved DPIA-lite report to {output}")
