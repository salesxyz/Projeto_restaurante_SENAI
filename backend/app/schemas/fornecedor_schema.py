"""Schemas Pydantic da entidade "fornecedor" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class FornecedorBase(BaseModel):
    nome: str
    contato: Optional[str] = None


class FornecedorCreate(FornecedorBase):
    pass


class FornecedorUpdate(BaseModel):
    nome: Optional[str] = None
    contato: Optional[str] = None


class FornecedorRead(FornecedorBase):
    model_config = ConfigDict(from_attributes=True)

    id_fornecedor: int

