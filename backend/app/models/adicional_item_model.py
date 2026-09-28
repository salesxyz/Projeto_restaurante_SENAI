"""Modelo SQLAlchemy da entidade "adicional_item"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class AdicionalItem(Base):
    __tablename__ = "adicional_item"

    id_adicional_item = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_item = Column(Integer, ForeignKey("item_pedido.id_item"), nullable=False)
    id_adicional = Column(Integer, ForeignKey("adicional.id_adicional"), nullable=False)
    quantidade = Column(Integer, nullable=False)

