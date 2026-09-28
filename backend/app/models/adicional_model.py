"""Modelo SQLAlchemy da entidade "adicional"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class Adicional(Base):
    __tablename__ = "adicional"

    id_adicional = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)

