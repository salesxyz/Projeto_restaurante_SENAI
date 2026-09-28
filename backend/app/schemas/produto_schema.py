"""Schemas Pydantic da entidade "produto" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class ProdutoBase(BaseModel):
    id_categoria: int
    nome: str
    preco_base: float


class ProdutoCreate(ProdutoBase):
    pass


class ProdutoUpdate(BaseModel):
    id_categoria: Optional[int] = None
    nome: Optional[str] = None
    preco_base: Optional[float] = None


class ProdutoRead(ProdutoBase):
    model_config = ConfigDict(from_attributes=True)

    id_produto: int

