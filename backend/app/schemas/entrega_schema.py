"""Schemas Pydantic da entidade "entrega" (Create / Update / Read)."""
from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel, ConfigDict


class EntregaBase(BaseModel):
    id_pedido: int
    id_funcionario: Optional[int] = None
    endereco: str
    taxa_entrega: float
    data_hora: Optional[datetime] = None


class EntregaCreate(EntregaBase):
    pass


class EntregaUpdate(BaseModel):
    id_pedido: Optional[int] = None
    id_funcionario: Optional[int] = None
    endereco: Optional[str] = None
    taxa_entrega: Optional[float] = None
    data_hora: Optional[datetime] = None


class EntregaRead(EntregaBase):
    model_config = ConfigDict(from_attributes=True)

    id_entrega: int

