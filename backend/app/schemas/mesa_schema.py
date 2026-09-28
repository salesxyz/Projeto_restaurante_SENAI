"""Schemas Pydantic da entidade "mesa" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class MesaBase(BaseModel):
    numero: int


class MesaCreate(MesaBase):
    pass


class MesaUpdate(BaseModel):
    numero: Optional[int] = None


class MesaRead(MesaBase):
    model_config = ConfigDict(from_attributes=True)

    id_mesa: int

