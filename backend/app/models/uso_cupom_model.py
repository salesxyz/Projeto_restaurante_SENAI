"""Modelo SQLAlchemy da entidade "uso_cupom"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class UsoCupom(Base):
    __tablename__ = "uso_cupom"

    id_uso = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_cupom = Column(Integer, ForeignKey("cupom.id_cupom"), nullable=False)
    id_pedido = Column(Integer, ForeignKey("pedido.id_pedido"), nullable=False)
    data_hora = Column(DateTime, nullable=False)

