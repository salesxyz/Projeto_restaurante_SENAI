"""Schemas Pydantic da entidade "adicional_item" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class AdicionalItemBase(BaseModel):
    id_item: int
    id_adicional: int
    quantidade: int


class AdicionalItemCreate(AdicionalItemBase):
    pass


class AdicionalItemUpdate(BaseModel):
    id_item: Optional[int] = None
    id_adicional: Optional[int] = None
    quantidade: Optional[int] = None


class AdicionalItemRead(AdicionalItemBase):
    model_config = ConfigDict(from_attributes=True)

    id_adicional_item: int

