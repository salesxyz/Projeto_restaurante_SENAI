"""Modelo SQLAlchemy da entidade "produto"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class Produto(Base):
    __tablename__ = "produto"

    id_produto = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_categoria = Column(Integer, ForeignKey("categoria.id_categoria"), nullable=False)
    nome = Column(String, nullable=False)
    preco_base = Column(Float, nullable=False)

