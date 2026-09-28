"""Modelo SQLAlchemy da entidade "ingrediente_fornecedor"."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.views.database import Base


class IngredienteFornecedor(Base):
    __tablename__ = "ingrediente_fornecedor"

    id_ingrediente_fornecedor = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_ingrediente = Column(Integer, ForeignKey("ingrediente.id_ingrediente"), nullable=False)
    id_fornecedor = Column(Integer, ForeignKey("fornecedor.id_fornecedor"), nullable=False)

