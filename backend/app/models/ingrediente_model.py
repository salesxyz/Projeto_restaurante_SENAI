"""Modelo SQLAlchemy da entidade "ingrediente"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class Ingrediente(Base):
    __tablename__ = "ingrediente"

    id_ingrediente = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    quantidade_estoque = Column(Float, nullable=False)
    unidade_medida = Column(String, nullable=False)

