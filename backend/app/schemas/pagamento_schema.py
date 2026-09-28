"""Schemas Pydantic da entidade "pagamento" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class PagamentoBase(BaseModel):
    id_pedido: int
    valor_pago: float


class PagamentoCreate(PagamentoBase):
    pass


class PagamentoUpdate(BaseModel):
    id_pedido: Optional[int] = None
    valor_pago: Optional[float] = None


class PagamentoRead(PagamentoBase):
    model_config = ConfigDict(from_attributes=True)

    id_pagamento: int

