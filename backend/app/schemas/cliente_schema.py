"""Schemas Pydantic da entidade "cliente" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class ClienteBase(BaseModel):
    nome: str
    contato: Optional[str] = None
    endereco: Optional[str] = None


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    contato: Optional[str] = None
    endereco: Optional[str] = None


class ClienteRead(ClienteBase):
    model_config = ConfigDict(from_attributes=True)

    id_cliente: int

