"""Validation API for synthetic events only."""
from datetime import datetime
from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Synthetic Log Validation API", version="0.1.0")


class Event(BaseModel):
    device_id: str = Field(min_length=1, max_length=64)
    timestamp: datetime
    severity: Literal["DEBUG", "INFO", "WARN", "ERROR"]
    message: str = Field(min_length=1, max_length=2000)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/validate")
def validate_event(event: Event) -> dict[str, str | bool]:
    return {"valid": True, "device_id": event.device_id, "severity": event.severity}
