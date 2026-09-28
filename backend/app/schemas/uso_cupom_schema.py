"""Schemas Pydantic da entidade "uso_cupom" (Create / Update / Read)."""
from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel, ConfigDict


class UsoCupomBase(BaseModel):
    id_cupom: int
    id_pedido: int
    data_hora: datetime


class UsoCupomCreate(UsoCupomBase):
    pass


class UsoCupomUpdate(BaseModel):
    id_cupom: Optional[int] = None
    id_pedido: Optional[int] = None
    data_hora: Optional[datetime] = None


class UsoCupomRead(UsoCupomBase):
    model_config = ConfigDict(from_attributes=True)

    id_uso: int

