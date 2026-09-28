"""Modelo SQLAlchemy da entidade "funcionario"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class Funcionario(Base):
    __tablename__ = "funcionario"

    id_funcionario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_cargo = Column(Integer, ForeignKey("cargo.id_cargo"), nullable=True)
    nome = Column(String, nullable=False)
    contato = Column(String, nullable=True)

