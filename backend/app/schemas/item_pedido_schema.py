"""Schemas Pydantic da entidade "item_pedido" (Create / Update / Read)."""
from typing import Optional
from pydantic import BaseModel, ConfigDict


class ItemPedidoBase(BaseModel):
    id_pedido: int
    id_produto: int
    id_variacao: Optional[int] = None
    quantidade: int
    observacao: Optional[str] = None


class ItemPedidoCreate(ItemPedidoBase):
    pass


class ItemPedidoUpdate(BaseModel):
    id_pedido: Optional[int] = None
    id_produto: Optional[int] = None
    id_variacao: Optional[int] = None
    quantidade: Optional[int] = None
    observacao: Optional[str] = None


class ItemPedidoRead(ItemPedidoBase):
    model_config = ConfigDict(from_attributes=True)

    id_item: int

