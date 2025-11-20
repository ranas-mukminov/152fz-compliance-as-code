from __future__ import annotations

import typer

from pd152_compliance_as_code.cli.commands import (
    generate_all,
    generate_consents,
    generate_dpi,
    generate_flows,
    generate_register,
    init_template,
    validate_config,
)

app = typer.Typer(help="152-FZ compliance as code CLI")

app.command(name="init-template")(init_template.command)
app.command(name="validate")(validate_config.command)
app.command(name="generate-all")(generate_all.command)
app.command(name="generate-register")(generate_register.command)
app.command(name="generate-consents")(generate_consents.command)
app.command(name="generate-flows")(generate_flows.command)
app.command(name="generate-dpi")(generate_dpi.command)


if __name__ == "__main__":
    app()
