"""Schemas Pydantic da entidade "ingrediente" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class IngredienteBase(BaseModel):
    nome: str
    quantidade_estoque: float
    unidade_medida: str


class IngredienteCreate(IngredienteBase):
    pass


class IngredienteUpdate(BaseModel):
    nome: Optional[str] = None
    quantidade_estoque: Optional[float] = None
    unidade_medida: Optional[str] = None


class IngredienteRead(IngredienteBase):
    model_config = ConfigDict(from_attributes=True)

    id_ingrediente: int

