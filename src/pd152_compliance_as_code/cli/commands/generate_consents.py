from __future__ import annotations

from pathlib import Path
from typing import List

import typer

from pd152_compliance_as_code.generators.consents_docx import generate_consents
from pd152_compliance_as_code.yaml_schema.loader import load_config
from pd152_compliance_as_code.yaml_schema.validator import validate_file


def command(
    config: str = typer.Option(..., "--config", help="Path to YAML config"),
    processes: List[str] = typer.Option(None, "--process", help="Process IDs to include", rich_help_panel="Filters"),
    policy_url: str | None = typer.Option(None, help="Link to privacy policy"),
    output: str = typer.Option("consents.docx", "--output", help="Path to DOCX"),
) -> None:
    errors = validate_file(config)
    if errors:
        for err in errors:
            typer.echo(f"ERROR: {err}")
        raise typer.Exit(code=1)
    cfg = load_config(config)
    generate_consents(cfg, processes, Path(output), policy_url=policy_url)
    typer.echo(f"Saved consents to {output}")
