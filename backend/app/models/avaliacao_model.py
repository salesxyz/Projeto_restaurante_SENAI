"""Modelo SQLAlchemy da entidade "avaliacao"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class Avaliacao(Base):
    __tablename__ = "avaliacao"

    id_avaliacao = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_pedido = Column(Integer, ForeignKey("pedido.id_pedido"), nullable=False)
    nota = Column(Integer, nullable=False)
    comentario = Column(String, nullable=True)

