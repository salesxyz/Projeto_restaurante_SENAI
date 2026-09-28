"""Rotas REST da entidade "adicional"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.adicional_model import Adicional
from app.schemas.adicional_schema import AdicionalCreate, AdicionalUpdate, AdicionalRead

router = APIRouter(prefix="/adicional", tags=["adicional"])


@router.get("/", response_model=List[AdicionalRead])
def listar_adicional(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Adicional).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=AdicionalRead)
def obter_adicional(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Adicional).filter(Adicional.id_adicional == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Adicional não encontrado")
    return obj


@router.post("/", response_model=AdicionalRead, status_code=status.HTTP_201_CREATED)
def criar_adicional(payload: AdicionalCreate, db: Session = Depends(get_db)):
    obj = Adicional(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=AdicionalRead)
def atualizar_adicional(item_id: int, payload: AdicionalUpdate, db: Session = Depends(get_db)):
    obj = db.query(Adicional).filter(Adicional.id_adicional == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Adicional não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_adicional(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Adicional).filter(Adicional.id_adicional == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Adicional não encontrado")
    db.delete(obj)
    db.commit()
    return None

