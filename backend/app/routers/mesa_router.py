"""Rotas REST da entidade "mesa"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.mesa_model import Mesa
from app.schemas.mesa_schema import MesaCreate, MesaUpdate, MesaRead

router = APIRouter(prefix="/mesa", tags=["mesa"])


@router.get("/", response_model=List[MesaRead])
def listar_mesa(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Mesa).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=MesaRead)
def obter_mesa(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Mesa).filter(Mesa.id_mesa == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mesa não encontrado")
    return obj


@router.post("/", response_model=MesaRead, status_code=status.HTTP_201_CREATED)
def criar_mesa(payload: MesaCreate, db: Session = Depends(get_db)):
    obj = Mesa(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=MesaRead)
def atualizar_mesa(item_id: int, payload: MesaUpdate, db: Session = Depends(get_db)):
    obj = db.query(Mesa).filter(Mesa.id_mesa == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mesa não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_mesa(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Mesa).filter(Mesa.id_mesa == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mesa não encontrado")
    db.delete(obj)
    db.commit()
    return None

