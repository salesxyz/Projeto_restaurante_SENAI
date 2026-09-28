"""Modelo SQLAlchemy da entidade "historico_cargo"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class HistoricoCargo(Base):
    __tablename__ = "historico_cargo"

    id_historico_cargo = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_funcionario = Column(Integer, ForeignKey("funcionario.id_funcionario"), nullable=False)
    id_cargo = Column(Integer, ForeignKey("cargo.id_cargo"), nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=True)

