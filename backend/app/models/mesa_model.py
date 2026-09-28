"""Modelo SQLAlchemy da entidade "mesa"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class Mesa(Base):
    __tablename__ = "mesa"

    id_mesa = Column(Integer, primary_key=True, index=True, autoincrement=True)
    numero = Column(Integer, nullable=False)

