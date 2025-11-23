# 152-FZ Compliance as Code

![CI](https://github.com/ranas-mukminov/152fz-compliance-as-code/actions/workflows/ci.yml/badge.svg)
![Security](https://github.com/ranas-mukminov/152fz-compliance-as-code/actions/workflows/security.yml/badge.svg)
![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

🇬🇧 English | 🇷🇺 [Русская версия](README.ru.md)

**Author & Website:** [Ranas Mukminov](https://github.com/ranas-mukminov) | [run-as-daemon.ru](https://run-as-daemon.ru)

## Overview

**152-FZ Compliance as Code** is an open-source Python toolkit that enables organizations to manage Russian Federal Law 152-FZ (Personal Data Law) compliance through a declarative YAML configuration. Instead of manually maintaining spreadsheets and Word documents, you describe your data processing activities once in a structured format and automatically generate registers, consent forms, data processor agreements, data flow diagrams, and DPIA-style risk reports. This project is designed for small-to-medium businesses, integrators, auditors, and DevSecOps teams who want to implement "Compliance as Code" workflows.

## Key Features

- **Declarative YAML DSL**: Define operators, data subjects, personal data categories, and processing activities in a version-controlled configuration file.
- **Automated Document Generation**: Generate the Register of Processing Activities, consent forms, and data processor agreements (DPA) in DOCX format.
- **Data Flow Diagrams**: Automatically create visual representations of data flows using Mermaid or PlantUML.
- **Risk Assessment Engine**: Built-in DPIA-lite risk scoring to identify high-risk processing activities.
- **CLI and Web UI**: Command-line tool (`pd152`) for CI/CD integration and a FastAPI-based web wizard for interactive configuration.
- **CI/CD Ready**: Validate configurations and generate artifacts as part of your automated pipelines.
- **Extensible Templates**: Jinja2-based templating for easy customization of generated documents.
- **Privacy-First**: No real personal data is required—use anonymized examples and placeholders.

## Architecture / Components

The toolkit consists of several modular components:

```
┌─────────────────────────────────────────────────────────────┐
│                      User Input                             │
│  ┌──────────────────┐         ┌─────────────────────────┐  │
│  │  YAML Config     │         │  Web Wizard (FastAPI)   │  │
│  │  (pd-config.yaml)│         │  http://localhost:8000  │  │
│  └─────────┬────────┘         └───────────┬─────────────┘  │
└────────────┼───────────────────────────────┼────────────────┘
             │                               │
             ▼                               ▼
┌─────────────────────────────────────────────────────────────┐
│             YAML Loader & Validator                         │
│  - JSON Schema validation                                   │
│  - Domain model mapping (models.py)                         │
└─────────────────────┬───────────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┬─────────────────┐
        │             │             │                 │
        ▼             ▼             ▼                 ▼
┌──────────────┐ ┌──────────┐ ┌──────────────┐ ┌──────────┐
│ Register     │ │ Consents │ │ Data Flow    │ │ Risk     │
│ Generator    │ │ Generator│ │ Diagrams     │ │ Engine   │
│ (DOCX)       │ │ (DOCX)   │ │ (Mermaid)    │ │ (DPIA)   │
└──────┬───────┘ └────┬─────┘ └──────┬───────┘ └────┬─────┘
       │              │              │              │
       └──────────────┴──────────┬───┴──────────────┘
                                 │
                                 ▼
                      ┌──────────────────────┐
                      │  Output Artifacts    │
                      │  - register.docx     │
                      │  - consents.docx     │
                      │  - flows.mmd         │
                      │  - risks.txt         │
                      └──────────────────────┘
```

**Key Components:**
- **Domain Models**: Python dataclasses defining operators, data subjects, processing activities, etc.
- **YAML Schema**: JSON Schema-based validation for the configuration DSL.
- **Generators**: Modular generators for different document types (DOCX, diagrams, reports).
- **Risk Engine**: Risk scoring based on data sensitivity, cross-border transfers, and security measures.
- **CLI (`pd152`)**: Typer-based command-line interface for all operations.
- **Web App**: FastAPI web wizard for guided configuration creation.

## Requirements

### Operating System
- **Linux**: Ubuntu 20.04+, Debian 11+, RHEL 8+, Rocky Linux, Alma Linux
- **macOS**: 11+ (Big Sur and later)
- **Windows**: 10/11 with Python installed

### Software
- **Python**: 3.10 or higher (3.11 recommended)
- **pip**: Latest version
- **Git**: For cloning the repository

### System Resources
- **CPU**: 1 core (2+ recommended)
- **RAM**: 512 MB minimum (1 GB recommended)
- **Disk**: 100 MB for the application + space for generated documents

### Network
- Internet access for installing Python dependencies from PyPI

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ranas-mukminov/152fz-compliance-as-code.git
   cd 152fz-compliance-as-code
   ```

2. **Install the package:**
   ```bash
   pip install .
   ```

3. **Validate an example configuration:**
   ```bash
   pd152 validate --config src/pd152_compliance_as_code/yaml_schema/examples/simple_online_shop.yaml
   ```

4. **Generate all documents:**
   ```bash
   pd152 generate-all --config src/pd152_compliance_as_code/yaml_schema/examples/simple_online_shop.yaml --output ./artifacts
   ```

5. **View generated files:**
   ```bash
   ls -lh artifacts/
   ```

## Installation

### Standard Installation (Production Use)

For most users who want to use the toolkit as-is:

```bash
# Install from source
git clone https://github.com/ranas-mukminov/152fz-compliance-as-code.git
cd 152fz-compliance-as-code
pip install .

# Verify installation
pd152 --help
```

### Development Installation

For contributors or those who want to modify the code:

```bash
# Clone and install in editable mode with dev dependencies
git clone https://github.com/ranas-mukminov/152fz-compliance-as-code.git
cd 152fz-compliance-as-code
pip install -e ".[dev]"

# Run tests to verify
pytest

# Run linters
scripts/lint.sh
```

### System-Wide Installation (Ubuntu/Debian)

```bash
# Install Python 3.10+ if not available
sudo apt update
sudo apt install python3.11 python3-pip git -y

# Clone and install
git clone https://github.com/ranas-mukminov/152fz-compliance-as-code.git
cd 152fz-compliance-as-code
pip install .
```

### System-Wide Installation (RHEL/Rocky/Alma)

```bash
# Install Python 3.10+ if not available
sudo dnf install python3.11 python3-pip git -y

# Clone and install
git clone https://github.com/ranas-mukminov/152fz-compliance-as-code.git
cd 152fz-compliance-as-code
pip install .
```

## Configuration

The heart of the toolkit is the YAML configuration file. Below is a complete example:

```yaml
operator:
  name: "LLC Romashka Online"
  inn: "1234567890"
  ogrn: "1234567890123"
  contacts:
    address: "Moscow, Flower Street, 1"
    email: "dpo@romashka.ru"
    phone: "+7 (495) 123-45-67"
    website: "https://romashka.ru"

processors:
  - name: "CloudProvider LLC"
    role: "Cloud hosting provider"
    contacts:
      email: "support@cloudprovider.ru"

data_subjects:
  - id: customers
    name: "Online store customers"
    description: "Individuals purchasing goods"
  
  - id: employees
    name: "Company employees"

personal_data_categories:
  - id: contact_data
    name: "Contact information"
    fields: ["Full name", "Email", "Phone", "Delivery address"]
    sensitivity: "standard"
  
  - id: payment_data
    name: "Payment information"
    fields: ["Card number (masked)", "Payment history"]
    sensitivity: "standard"

processing_activities:
  - id: order_processing
    name: "Order processing and fulfillment"
    subjects: ["customers"]
    data_categories: ["contact_data", "payment_data"]
    purposes:
      - "Contract execution (sale of goods)"
      - "Delivery coordination"
    legal_basis:
      - "Contract"
    operations:
      - "collection"
      - "recording"
      - "storage"
      - "transfer"
    storage_locations:
      - "Server in Russia (DataCenter Moscow)"
    recipients:
      - "Delivery service (courier)"
      - "Payment processor"
    retention:
      description: "5 years for accounting and dispute resolution"
      period: "5 years"
    security_measures:
      org:
        - "Role-based access control"
        - "Employee training on data protection"
      tech:
        - "Disk encryption (AES-256)"
        - "Daily backups"
        - "Access logging and monitoring"
      legal:
        - "DPA with processors"
        - "Internal data protection policy"
    notes: "Payment card data is processed by certified payment gateway, not stored in our systems"
```

### Environment Variables

The toolkit currently does not require environment variables for basic operation. All configuration is done via the YAML file.

## Usage & Common Tasks

### Command Line Interface

The `pd152` CLI is the primary interface for all operations:

```bash
# Show all available commands
pd152 --help

# Validate a configuration file
pd152 validate --config pd-config.yaml

# Generate all artifacts (register, consents, diagrams, risk report)
pd152 generate-all --config pd-config.yaml --output ./out

# Generate only the Register of Processing Activities
pd152 generate-register --config pd-config.yaml --output ./out/register.docx

# Generate only consent forms
pd152 generate-consents --config pd-config.yaml --output ./out/consents.docx

# Generate data flow diagrams
pd152 generate-flows --config pd-config.yaml --output ./out/flows.mmd

# Generate DPA (Data Processing Agreement) drafts
pd152 generate-dpi --config pd-config.yaml --output ./out/dpa.docx

# Initialize a template configuration
pd152 init-template --output my-config.yaml
```

### Web Wizard

To use the interactive web interface:

```bash
# Start the web server
uvicorn pd152_compliance_as_code.webapp.app:app --reload --host 0.0.0.0 --port 8000
```

Then open your browser at `http://localhost:8000` and use the wizard to:
- Create a new configuration interactively
- Validate your inputs in real-time
- Export the configuration as YAML

### Using in CI/CD Pipelines

Example GitHub Actions workflow:

```yaml
name: Compliance Docs

on:
  push:
    paths:
      - 'compliance/pd-config.yaml'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install pd152
        run: pip install git+https://github.com/ranas-mukminov/152fz-compliance-as-code.git
      - name: Validate
        run: pd152 validate --config compliance/pd-config.yaml
      - name: Generate
        run: pd152 generate-all --config compliance/pd-config.yaml --output compliance/artifacts
      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: compliance-docs
          path: compliance/artifacts/
```

## Update / Upgrade

To update to the latest version:

```bash
# Navigate to your local clone
cd 152fz-compliance-as-code

# Pull latest changes
git pull origin main

# Reinstall
pip install --upgrade .

# Verify version (check CHANGELOG.md for version info)
pd152 --help
```

**Breaking Changes**: Always review `CHANGELOG.md` before upgrading. Major changes to the YAML schema will be documented there.

## Logs, Monitoring, Troubleshooting

### Validation Errors

If `pd152 validate` fails:
- Read the error message carefully—it will indicate which field is missing or incorrect.
- Check the YAML syntax (indentation, colons, quotes).
- Compare your configuration with the examples in `src/pd152_compliance_as_code/yaml_schema/examples/`.

**Common errors:**
```bash
# Invalid YAML syntax
Error: mapping values are not allowed here
  ▶ Fix: Check for missing colons or incorrect indentation

# Missing required field
Error: 'operator.name' is a required property
  ▶ Fix: Add the operator name in your YAML

# Invalid reference
Error: Subject ID 'customer' not found in data_subjects
  ▶ Fix: Ensure all IDs referenced in processing_activities exist
```

### Generation Issues

If document generation fails:
- Ensure the output directory exists or is writable.
- Check that `python-docx` is installed: `pip install python-docx`
- Run with verbose output (if implemented) or check stderr.

### Web Interface Issues

If the web wizard doesn't start:
```bash
# Check if port 8000 is already in use
lsof -i :8000

# Use a different port
uvicorn pd152_compliance_as_code.webapp.app:app --port 8080

# Check uvicorn installation
pip install uvicorn[standard]
```

### Performance Issues

For large configurations (100+ processing activities):
- Generation may take 10-30 seconds.
- Use `scripts/perf_check.sh` to benchmark (if available).

## Security Notes

### Legal Disclaimer

> **This tool does NOT replace professional legal advice.** Generated documents are templates and drafts that MUST be reviewed by a qualified lawyer or Data Protection Officer (DPO) before use in production.

### Data Privacy

- **Do NOT commit real personal data** (names, phone numbers, emails of actual individuals) to your YAML configuration files.
- Use anonymized examples: "Ivan Ivanov", "example@example.com", "+7 (XXX) XXX-XX-XX".
- If storing configurations with sensitive information, use private repositories with access controls.

### Secrets Management

- This tool does not currently require API keys or passwords.
- If you extend it with external integrations (e.g., cloud storage), use environment variables or secret management tools, never hardcode credentials.

### External AI/LLM Services

If you use external AI services to help generate YAML configurations:
- Always anonymize or pseudonymize data before sending it to third-party services.
- Do not send real personal data to LLMs without proper legal basis and data subject consent.
- Review the AI-generated output—it may contain errors or non-compliant suggestions.

### Access Control

- Restrict access to the web UI (`http://localhost:8000`) to internal networks or use authentication (not included by default).
- Do not expose the web interface directly to the Internet without a reverse proxy with TLS and authentication.

## Project Structure

```
152fz-compliance-as-code/
├── src/
│   └── pd152_compliance_as_code/
│       ├── cli/                    # CLI commands (Typer)
│       ├── domain/                 # Data models (dataclasses)
│       ├── generators/             # Document generators (DOCX, diagrams)
│       ├── risk_engine/            # Risk assessment logic
│       ├── webapp/                 # FastAPI web application
│       └── yaml_schema/            # YAML schema and examples
├── tests/                          # Unit and integration tests
│   ├── unit/                       # Unit tests
│   └── integration/                # Integration tests
├── scripts/                        # Development and CI scripts
│   ├── lint.sh                     # Run linters (ruff, mypy)
│   ├── security_scan.sh            # Run bandit and pip-audit
│   └── perf_check.sh               # Performance benchmarks
├── .github/
│   └── workflows/                  # GitHub Actions CI/CD
│       ├── ci.yml                  # Lint, test, generate examples
│       └── security.yml            # Security scanning
├── examples/                       # Sample input policies (markdown)
├── pyproject.toml                  # Python project configuration
├── LICENSE                         # Apache 2.0 license
├── LEGAL.md                        # Legal disclaimers
├── CONTRIBUTING.md                 # Contribution guidelines
└── README.md                       # This file
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Open an issue** before starting work on major changes.
2. **Fork the repository** and create a feature branch.
3. **Keep changes focused**: One feature or bugfix per PR.
4. **Add tests**: Cover new functionality with unit tests.
5. **Run linters**: Ensure `scripts/lint.sh` passes before submitting.
6. **No real personal data**: Use anonymized examples only.

**Development setup:**
```bash
pip install -e ".[dev]"
scripts/lint.sh
pytest
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## License

This project is licensed under the **Apache License 2.0**. See [LICENSE](LICENSE) for the full text.

You are free to use, modify, and distribute this software, including for commercial purposes, provided you include the license notice and attribution.

## Author and Commercial Support

**Author:** [Ranas Mukminov](https://github.com/ranas-mukminov)  
**Website:** [run-as-daemon.ru](https://run-as-daemon.ru)

For production-grade implementation, customized templates, audits, and ongoing support, commercial services are available:

- 152-FZ compliance audits and gap analysis
- Custom YAML configuration development for your organization
- Integration with existing systems (CMDB, ticketing, HR)
- Training for your team on "Compliance as Code" practices
- Ongoing support and updates

Visit [run-as-daemon.ru](https://run-as-daemon.ru) or contact via the GitHub profile for inquiries.
