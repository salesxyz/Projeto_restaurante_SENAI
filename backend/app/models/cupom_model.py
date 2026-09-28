"""Modelo SQLAlchemy da entidade "cupom"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class Cupom(Base):
    __tablename__ = "cupom"

    id_cupom = Column(Integer, primary_key=True, index=True, autoincrement=True)
    codigo = Column(String, nullable=False)
    tipo_desconto = Column(String, nullable=False)
    valor_desconto = Column(Float, nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=True)

