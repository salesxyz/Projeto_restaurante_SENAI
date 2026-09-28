"""Modelo SQLAlchemy da entidade "pagamento_forma"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class PagamentoForma(Base):
    __tablename__ = "pagamento_forma"

    id_pagamento_forma = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_pagamento = Column(Integer, ForeignKey("pagamento.id_pagamento"), nullable=False)
    id_forma_pagamento = Column(Integer, ForeignKey("forma_pagamento.id_forma_pagamento"), nullable=False)

