"""Modelo SQLAlchemy da entidade "variacao"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class Variacao(Base):
    __tablename__ = "variacao"

    id_variacao = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_produto = Column(Integer, ForeignKey("produto.id_produto"), nullable=False)
    nome = Column(String, nullable=False)
    valor_adicional = Column(Float, nullable=False)

