"""Modelo SQLAlchemy da entidade "pagamento"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class Pagamento(Base):
    __tablename__ = "pagamento"

    id_pagamento = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_pedido = Column(Integer, ForeignKey("pedido.id_pedido"), nullable=False)
    valor_pago = Column(Float, nullable=False)

