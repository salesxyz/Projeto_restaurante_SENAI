"""Schemas Pydantic da entidade "pedido" (Create / Update / Read)."""
from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel, ConfigDict


class PedidoBase(BaseModel):
    id_cliente: Optional[int] = None
    id_mesa: Optional[int] = None
    data_hora: datetime
    origem_pedido: str
    status_atual: str


class PedidoCreate(PedidoBase):
    pass


class PedidoUpdate(BaseModel):
    id_cliente: Optional[int] = None
    id_mesa: Optional[int] = None
    data_hora: Optional[datetime] = None
    origem_pedido: Optional[str] = None
    status_atual: Optional[str] = None


class PedidoRead(PedidoBase):
    model_config = ConfigDict(from_attributes=True)

    id_pedido: int

