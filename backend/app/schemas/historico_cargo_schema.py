"""Schemas Pydantic da entidade "historico_cargo" (Create / Update / Read)."""
from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel, ConfigDict


class HistoricoCargoBase(BaseModel):
    id_funcionario: int
    id_cargo: int
    data_inicio: date
    data_fim: Optional[date] = None


class HistoricoCargoCreate(HistoricoCargoBase):
    pass


class HistoricoCargoUpdate(BaseModel):
    id_funcionario: Optional[int] = None
    id_cargo: Optional[int] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None


class HistoricoCargoRead(HistoricoCargoBase):
    model_config = ConfigDict(from_attributes=True)

    id_historico_cargo: int

