"""Modelo SQLAlchemy da entidade "entrega"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class Entrega(Base):
    __tablename__ = "entrega"

    id_entrega = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_pedido = Column(Integer, ForeignKey("pedido.id_pedido"), nullable=False)
    id_funcionario = Column(Integer, ForeignKey("funcionario.id_funcionario"), nullable=True)
    endereco = Column(String, nullable=False)
    taxa_entrega = Column(Float, nullable=False)
    data_hora = Column(DateTime, nullable=True)

