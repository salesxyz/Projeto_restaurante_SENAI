"""Modelo SQLAlchemy da entidade "promocao_produto"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class PromocaoProduto(Base):
    __tablename__ = "promocao_produto"

    id_promocao_produto = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_promocao = Column(Integer, ForeignKey("promocao.id_promocao"), nullable=False)
    id_produto = Column(Integer, ForeignKey("produto.id_produto"), nullable=False)
    id_cupom = Column(Integer, ForeignKey("cupom.id_cupom"), nullable=True)
    preco_promocional = Column(Float, nullable=False)
    data_inicio = Column(Date, nullable=True)
    data_fim = Column(Date, nullable=True)

