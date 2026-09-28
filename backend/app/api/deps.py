"""Dependências compartilhadas entre as rotas."""
from typing import Generator

from app.views.database import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
