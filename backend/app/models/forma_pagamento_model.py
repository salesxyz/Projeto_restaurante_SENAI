"""Modelo SQLAlchemy da entidade "forma_pagamento"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class FormaPagamento(Base):
    __tablename__ = "forma_pagamento"

    id_forma_pagamento = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)

