"""Schemas Pydantic da entidade "adicional" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class AdicionalBase(BaseModel):
    nome: str
    preco: float


class AdicionalCreate(AdicionalBase):
    pass


class AdicionalUpdate(BaseModel):
    nome: Optional[str] = None
    preco: Optional[float] = None


class AdicionalRead(AdicionalBase):
    model_config = ConfigDict(from_attributes=True)

    id_adicional: int

