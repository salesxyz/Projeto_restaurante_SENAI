"""Modelo SQLAlchemy da entidade "historico_status"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class HistoricoStatus(Base):
    __tablename__ = "historico_status"

    id_historico = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_pedido = Column(Integer, ForeignKey("pedido.id_pedido"), nullable=False)
    id_funcionario = Column(Integer, ForeignKey("funcionario.id_funcionario"), nullable=True)
    status = Column(String, nullable=False)
    data_hora = Column(DateTime, nullable=False)

