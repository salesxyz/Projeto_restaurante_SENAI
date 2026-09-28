"""Modelo SQLAlchemy da entidade "fornecedor"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class Fornecedor(Base):
    __tablename__ = "fornecedor"

    id_fornecedor = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    contato = Column(String, nullable=True)

