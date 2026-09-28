"""Schemas Pydantic da entidade "cupom" (Create / Update / Read)."""
from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel, ConfigDict


class CupomBase(BaseModel):
    codigo: str
    tipo_desconto: str
    valor_desconto: float
    data_inicio: date
    data_fim: Optional[date] = None


class CupomCreate(CupomBase):
    pass


class CupomUpdate(BaseModel):
    codigo: Optional[str] = None
    tipo_desconto: Optional[str] = None
    valor_desconto: Optional[float] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None


class CupomRead(CupomBase):
    model_config = ConfigDict(from_attributes=True)

    id_cupom: int

