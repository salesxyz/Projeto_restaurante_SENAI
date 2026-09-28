"""Modelo SQLAlchemy da entidade "promocao"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class Promocao(Base):
    __tablename__ = "promocao"

    id_promocao = Column(Integer, primary_key=True, index=True, autoincrement=True)
    descricao = Column(String, nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=True)

