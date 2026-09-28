"""Schemas Pydantic da entidade "cargo" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class CargoBase(BaseModel):
    nome: str


class CargoCreate(CargoBase):
    pass


class CargoUpdate(BaseModel):
    nome: Optional[str] = None


class CargoRead(CargoBase):
    model_config = ConfigDict(from_attributes=True)

    id_cargo: int

