"""Rotas REST da entidade "entrega"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.entrega_model import Entrega
from app.schemas.entrega_schema import EntregaCreate, EntregaUpdate, EntregaRead

router = APIRouter(prefix="/entrega", tags=["entrega"])


@router.get("/", response_model=List[EntregaRead])
def listar_entrega(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Entrega).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=EntregaRead)
def obter_entrega(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Entrega).filter(Entrega.id_entrega == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entrega não encontrado")
    return obj


@router.post("/", response_model=EntregaRead, status_code=status.HTTP_201_CREATED)
def criar_entrega(payload: EntregaCreate, db: Session = Depends(get_db)):
    obj = Entrega(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=EntregaRead)
def atualizar_entrega(item_id: int, payload: EntregaUpdate, db: Session = Depends(get_db)):
    obj = db.query(Entrega).filter(Entrega.id_entrega == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entrega não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_entrega(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Entrega).filter(Entrega.id_entrega == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entrega não encontrado")
    db.delete(obj)
    db.commit()
    return None

