"""Modelo SQLAlchemy da entidade "cargo"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class Cargo(Base):
    __tablename__ = "cargo"

    id_cargo = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)

