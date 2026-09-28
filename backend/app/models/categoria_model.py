"""Modelo SQLAlchemy da entidade "categoria"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class Categoria(Base):
    __tablename__ = "categoria"

    id_categoria = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)

