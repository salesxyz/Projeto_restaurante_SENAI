"""Schemas Pydantic da entidade "promocao" (Create / Update / Read)."""
from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel, ConfigDict


class PromocaoBase(BaseModel):
    descricao: str
    data_inicio: date
    data_fim: Optional[date] = None


class PromocaoCreate(PromocaoBase):
    pass


class PromocaoUpdate(BaseModel):
    descricao: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None


class PromocaoRead(PromocaoBase):
    model_config = ConfigDict(from_attributes=True)

    id_promocao: int

