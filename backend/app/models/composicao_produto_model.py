"""Modelo SQLAlchemy da entidade "composicao_produto"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class ComposicaoProduto(Base):
    __tablename__ = "composicao_produto"

    id_composicao = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_produto = Column(Integer, ForeignKey("produto.id_produto"), nullable=False)
    id_ingrediente = Column(Integer, ForeignKey("ingrediente.id_ingrediente"), nullable=False)
    quantidade_utilizada = Column(Float, nullable=False)

