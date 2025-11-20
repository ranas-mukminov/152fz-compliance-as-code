from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates

from pd152_compliance_as_code.yaml_schema.loader import load_config_from_mapping
from pd152_compliance_as_code.yaml_schema.validator import validate_mapping

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=BASE_DIR / "templates")

app = FastAPI(title="152-FZ compliance as code")

# In-memory store only for demo purposes
STATE: Dict[str, Any] = {}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return TEMPLATES.TemplateResponse(
        "base.html", {"request": request, "title": "152-ФЗ как код", "message": "Опишите процессы и получите документы автоматически."}
    )


@app.get("/wizard", response_class=HTMLResponse)
async def wizard_form(request: Request) -> HTMLResponse:
    return TEMPLATES.TemplateResponse("wizard.html", {"request": request, "errors": [], "success": False})


@app.post("/wizard", response_class=HTMLResponse)
async def wizard_submit(
    request: Request,
    operator_name: str = Form(...),
    operator_email: str = Form(""),
    subjects: str = Form(..., description="Comma separated subject IDs"),
    categories: str = Form(..., description="Comma separated category IDs"),
    processes: str = Form(..., description="Comma separated process IDs"),
) -> HTMLResponse:
    config = {
        "operator": {"name": operator_name, "contacts": {"email": operator_email}},
        "data_subjects": [
            {"id": s.strip(), "name": s.strip()} for s in subjects.split(",") if s.strip()
        ],
        "personal_data_categories": [
            {"id": c.strip(), "name": c.strip(), "fields": ["описание"]} for c in categories.split(",") if c.strip()
        ],
        "processing_activities": [
            {
                "id": p.strip(),
                "name": p.strip(),
                "subjects": [s.strip() for s in subjects.split(",") if s.strip()],
                "data_categories": [c.strip() for c in categories.split(",") if c.strip()],
                "purposes": ["описание целей"],
                "legal_basis": ["согласие"],
                "operations": ["сбор", "хранение"],
                "retention": {"description": "указать срок"},
            }
            for p in processes.split(",")
            if p.strip()
        ],
    }
    errors = validate_mapping(config)
    success = len(errors) == 0
    if success:
        STATE["draft_config"] = config
    return TEMPLATES.TemplateResponse(
        "wizard.html", {"request": request, "errors": errors, "success": success}
    )


@app.get("/export", response_class=PlainTextResponse)
async def export_current() -> PlainTextResponse:
    if "draft_config" not in STATE:
        return PlainTextResponse("Нет сохранённой конфигурации. Заполните wizard." , status_code=404)
    cfg = load_config_from_mapping(STATE["draft_config"])
    summary = [f"Оператор: {cfg.operator.name}"]
    summary.append(f"Процессов: {len(cfg.processing_activities)}")
    return PlainTextResponse("\n".join(summary))
