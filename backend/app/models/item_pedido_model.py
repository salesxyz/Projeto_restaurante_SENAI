"""Modelo SQLAlchemy da entidade "item_pedido"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class ItemPedido(Base):
    __tablename__ = "item_pedido"

    id_item = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_pedido = Column(Integer, ForeignKey("pedido.id_pedido"), nullable=False)
    id_produto = Column(Integer, ForeignKey("produto.id_produto"), nullable=False)
    id_variacao = Column(Integer, ForeignKey("variacao.id_variacao"), nullable=True)
    quantidade = Column(Integer, nullable=False)
    observacao = Column(String, nullable=True)

