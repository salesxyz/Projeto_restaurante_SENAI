"""Schemas Pydantic da entidade "promocao_produto" (Create / Update / Read)."""
from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel, ConfigDict


class PromocaoProdutoBase(BaseModel):
    id_promocao: int
    id_produto: int
    id_cupom: Optional[int] = None
    preco_promocional: float
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None


class PromocaoProdutoCreate(PromocaoProdutoBase):
    pass


class PromocaoProdutoUpdate(BaseModel):
    id_promocao: Optional[int] = None
    id_produto: Optional[int] = None
    id_cupom: Optional[int] = None
    preco_promocional: Optional[float] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None


class PromocaoProdutoRead(PromocaoProdutoBase):
    model_config = ConfigDict(from_attributes=True)

    id_promocao_produto: int

