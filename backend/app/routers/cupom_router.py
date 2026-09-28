"""Rotas REST da entidade "cupom"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.cupom_model import Cupom
from app.schemas.cupom_schema import CupomCreate, CupomUpdate, CupomRead

router = APIRouter(prefix="/cupom", tags=["cupom"])


@router.get("/", response_model=List[CupomRead])
def listar_cupom(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Cupom).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=CupomRead)
def obter_cupom(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Cupom).filter(Cupom.id_cupom == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cupom não encontrado")
    return obj


@router.post("/", response_model=CupomRead, status_code=status.HTTP_201_CREATED)
def criar_cupom(payload: CupomCreate, db: Session = Depends(get_db)):
    obj = Cupom(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=CupomRead)
def atualizar_cupom(item_id: int, payload: CupomUpdate, db: Session = Depends(get_db)):
    obj = db.query(Cupom).filter(Cupom.id_cupom == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cupom não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_cupom(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Cupom).filter(Cupom.id_cupom == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cupom não encontrado")
    db.delete(obj)
    db.commit()
    return None

