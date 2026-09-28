"""Schemas Pydantic da entidade "forma_pagamento" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class FormaPagamentoBase(BaseModel):
    nome: str


class FormaPagamentoCreate(FormaPagamentoBase):
    pass


class FormaPagamentoUpdate(BaseModel):
    nome: Optional[str] = None


class FormaPagamentoRead(FormaPagamentoBase):
    model_config = ConfigDict(from_attributes=True)

    id_forma_pagamento: int

