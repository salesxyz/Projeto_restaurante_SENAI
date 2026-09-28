"""Schemas Pydantic da entidade "variacao" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class VariacaoBase(BaseModel):
    id_produto: int
    nome: str
    valor_adicional: float


class VariacaoCreate(VariacaoBase):
    pass


class VariacaoUpdate(BaseModel):
    id_produto: Optional[int] = None
    nome: Optional[str] = None
    valor_adicional: Optional[float] = None


class VariacaoRead(VariacaoBase):
    model_config = ConfigDict(from_attributes=True)

    id_variacao: int

