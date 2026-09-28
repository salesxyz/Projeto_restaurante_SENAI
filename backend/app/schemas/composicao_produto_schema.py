"""Schemas Pydantic da entidade "composicao_produto" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class ComposicaoProdutoBase(BaseModel):
    id_produto: int
    id_ingrediente: int
    quantidade_utilizada: float


class ComposicaoProdutoCreate(ComposicaoProdutoBase):
    pass


class ComposicaoProdutoUpdate(BaseModel):
    id_produto: Optional[int] = None
    id_ingrediente: Optional[int] = None
    quantidade_utilizada: Optional[float] = None


class ComposicaoProdutoRead(ComposicaoProdutoBase):
    model_config = ConfigDict(from_attributes=True)

    id_composicao: int

