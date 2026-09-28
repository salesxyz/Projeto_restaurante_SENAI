"""Rotas REST da entidade "item_pedido"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.item_pedido_model import ItemPedido
from app.schemas.item_pedido_schema import ItemPedidoCreate, ItemPedidoUpdate, ItemPedidoRead

router = APIRouter(prefix="/item-pedido", tags=["item_pedido"])


@router.get("/", response_model=List[ItemPedidoRead])
def listar_item_pedido(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(ItemPedido).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=ItemPedidoRead)
def obter_item_pedido(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(ItemPedido).filter(ItemPedido.id_item == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ItemPedido não encontrado")
    return obj


@router.post("/", response_model=ItemPedidoRead, status_code=status.HTTP_201_CREATED)
def criar_item_pedido(payload: ItemPedidoCreate, db: Session = Depends(get_db)):
    obj = ItemPedido(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=ItemPedidoRead)
def atualizar_item_pedido(item_id: int, payload: ItemPedidoUpdate, db: Session = Depends(get_db)):
    obj = db.query(ItemPedido).filter(ItemPedido.id_item == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ItemPedido não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_item_pedido(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(ItemPedido).filter(ItemPedido.id_item == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ItemPedido não encontrado")
    db.delete(obj)
    db.commit()
    return None

