"""Schemas Pydantic da entidade "funcionario" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class FuncionarioBase(BaseModel):
    id_cargo: Optional[int] = None
    nome: str
    contato: Optional[str] = None


class FuncionarioCreate(FuncionarioBase):
    pass


class FuncionarioUpdate(BaseModel):
    id_cargo: Optional[int] = None
    nome: Optional[str] = None
    contato: Optional[str] = None


class FuncionarioRead(FuncionarioBase):
    model_config = ConfigDict(from_attributes=True)

    id_funcionario: int

