"""Schemas Pydantic da entidade "categoria" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class CategoriaBase(BaseModel):
    nome: str


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(BaseModel):
    nome: Optional[str] = None


class CategoriaRead(CategoriaBase):
    model_config = ConfigDict(from_attributes=True)

    id_categoria: int

