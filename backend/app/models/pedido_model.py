"""Modelo SQLAlchemy da entidade "pedido"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class Pedido(Base):
    __tablename__ = "pedido"

    id_pedido = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey("cliente.id_cliente"), nullable=True)
    id_mesa = Column(Integer, ForeignKey("mesa.id_mesa"), nullable=True)
    data_hora = Column(DateTime, nullable=False)
    origem_pedido = Column(String, nullable=False)
    status_atual = Column(String, nullable=False)

