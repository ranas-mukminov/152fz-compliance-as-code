# Contributing

Thank you for considering a contribution! This project targets small businesses that want "152-FZ as code" workflows. Please keep changes lightweight, documented, and privacy-aware.

## Ground rules
- Do not paste verbatim text from laws or third-party policies.
- Avoid committing secrets or real personal data. Use anonymized examples only.
- Keep code typed (Python 3.10+), add tests, and ensure `scripts/lint.sh` passes.
- Prefer small, focused pull requests with clear rationale.

## Development
1. Create a branch and install dev dependencies: `pip install -e .[dev]`.
2. Run `scripts/lint.sh` and `pytest` before opening a PR.
3. Add or update examples under `src/pd152_compliance_as_code/yaml_schema/examples/` when changing the DSL.

## Code of conduct
Be kind, constructive, and mindful of privacy. When in doubt about including specific legal text, keep it high-level and reference generally accepted practices instead of quoting laws.
