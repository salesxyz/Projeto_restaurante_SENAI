"""Rotas REST da entidade "adicional_item"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.adicional_item_model import AdicionalItem
from app.schemas.adicional_item_schema import AdicionalItemCreate, AdicionalItemUpdate, AdicionalItemRead

router = APIRouter(prefix="/adicional-item", tags=["adicional_item"])


@router.get("/", response_model=List[AdicionalItemRead])
def listar_adicional_item(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(AdicionalItem).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=AdicionalItemRead)
def obter_adicional_item(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(AdicionalItem).filter(AdicionalItem.id_adicional_item == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AdicionalItem não encontrado")
    return obj


@router.post("/", response_model=AdicionalItemRead, status_code=status.HTTP_201_CREATED)
def criar_adicional_item(payload: AdicionalItemCreate, db: Session = Depends(get_db)):
    obj = AdicionalItem(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=AdicionalItemRead)
def atualizar_adicional_item(item_id: int, payload: AdicionalItemUpdate, db: Session = Depends(get_db)):
    obj = db.query(AdicionalItem).filter(AdicionalItem.id_adicional_item == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AdicionalItem não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_adicional_item(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(AdicionalItem).filter(AdicionalItem.id_adicional_item == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AdicionalItem não encontrado")
    db.delete(obj)
    db.commit()
    return None

