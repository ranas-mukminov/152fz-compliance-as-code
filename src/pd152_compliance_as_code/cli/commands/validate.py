from __future__ import annotations

import typer

from pd152_compliance_as_code.yaml_schema.validator import validate_file


def command(config: str = typer.Option(..., "--config", help="Path to YAML config")) -> None:
    errors = validate_file(config)
    if errors:
        for err in errors:
            typer.echo(f"ERROR: {err}")
        raise typer.Exit(code=1)
    typer.echo("Config is valid")
