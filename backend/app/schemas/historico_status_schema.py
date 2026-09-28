"""Schemas Pydantic da entidade "historico_status" (Create / Update / Read)."""
from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel, ConfigDict


class HistoricoStatusBase(BaseModel):
    id_pedido: int
    id_funcionario: Optional[int] = None
    status: str
    data_hora: datetime


class HistoricoStatusCreate(HistoricoStatusBase):
    pass


class HistoricoStatusUpdate(BaseModel):
    id_pedido: Optional[int] = None
    id_funcionario: Optional[int] = None
    status: Optional[str] = None
    data_hora: Optional[datetime] = None


class HistoricoStatusRead(HistoricoStatusBase):
    model_config = ConfigDict(from_attributes=True)

    id_historico: int

