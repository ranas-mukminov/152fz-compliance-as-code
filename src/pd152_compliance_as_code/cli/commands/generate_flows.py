from __future__ import annotations

from pathlib import Path

import typer

from pd152_compliance_as_code.generators.flows_diagram import generate_mermaid
from pd152_compliance_as_code.yaml_schema.loader import load_config
from pd152_compliance_as_code.yaml_schema.validator import validate_file


def command(config: str = typer.Option(..., "--config", help="Path to YAML config"), output: str = typer.Option("flows.mmd", "--output", help="Path to Mermaid file")) -> None:
    errors = validate_file(config)
    if errors:
        for err in errors:
            typer.echo(f"ERROR: {err}")
        raise typer.Exit(code=1)
    cfg = load_config(config)
    generate_mermaid(cfg, Path(output))
    typer.echo(f"Saved flows diagram to {output}")
