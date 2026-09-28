"""Schemas Pydantic da entidade "avaliacao" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class AvaliacaoBase(BaseModel):
    id_pedido: int
    nota: int
    comentario: Optional[str] = None


class AvaliacaoCreate(AvaliacaoBase):
    pass


class AvaliacaoUpdate(BaseModel):
    id_pedido: Optional[int] = None
    nota: Optional[int] = None
    comentario: Optional[str] = None


class AvaliacaoRead(AvaliacaoBase):
    model_config = ConfigDict(from_attributes=True)

    id_avaliacao: int

