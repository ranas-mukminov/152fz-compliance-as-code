from __future__ import annotations

from pathlib import Path

import typer

from pd152_compliance_as_code.generators.register_docx import generate_register
from pd152_compliance_as_code.yaml_schema.loader import load_config
from pd152_compliance_as_code.yaml_schema.validator import validate_file


def command(config: str = typer.Option(..., "--config", help="Path to YAML config"), output: str = typer.Option("register.docx", "--output", help="Path to DOCX register")) -> None:
    errors = validate_file(config)
    if errors:
        for err in errors:
            typer.echo(f"ERROR: {err}")
        raise typer.Exit(code=1)
    cfg = load_config(config)
    generate_register(cfg, Path(output))
    typer.echo(f"Saved register to {output}")
