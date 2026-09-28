"""Rotas REST da entidade "pedido"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.pedido_model import Pedido
from app.schemas.pedido_schema import PedidoCreate, PedidoUpdate, PedidoRead

router = APIRouter(prefix="/pedido", tags=["pedido"])


@router.get("/", response_model=List[PedidoRead])
def listar_pedido(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Pedido).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=PedidoRead)
def obter_pedido(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Pedido).filter(Pedido.id_pedido == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pedido não encontrado")
    return obj


@router.post("/", response_model=PedidoRead, status_code=status.HTTP_201_CREATED)
def criar_pedido(payload: PedidoCreate, db: Session = Depends(get_db)):
    obj = Pedido(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=PedidoRead)
def atualizar_pedido(item_id: int, payload: PedidoUpdate, db: Session = Depends(get_db)):
    obj = db.query(Pedido).filter(Pedido.id_pedido == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pedido não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_pedido(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Pedido).filter(Pedido.id_pedido == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pedido não encontrado")
    db.delete(obj)
    db.commit()
    return None

