"""Schemas Pydantic da entidade "ingrediente_fornecedor" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class IngredienteFornecedorBase(BaseModel):
    id_ingrediente: int
    id_fornecedor: int


class IngredienteFornecedorCreate(IngredienteFornecedorBase):
    pass


class IngredienteFornecedorUpdate(BaseModel):
    id_ingrediente: Optional[int] = None
    id_fornecedor: Optional[int] = None


class IngredienteFornecedorRead(IngredienteFornecedorBase):
    model_config = ConfigDict(from_attributes=True)

    id_ingrediente_fornecedor: int

