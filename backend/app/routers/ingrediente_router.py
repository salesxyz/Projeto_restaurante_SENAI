"""Rotas REST da entidade "ingrediente"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.ingrediente_model import Ingrediente
from app.schemas.ingrediente_schema import IngredienteCreate, IngredienteUpdate, IngredienteRead

router = APIRouter(prefix="/ingrediente", tags=["ingrediente"])


@router.get("/", response_model=List[IngredienteRead])
def listar_ingrediente(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Ingrediente).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=IngredienteRead)
def obter_ingrediente(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Ingrediente).filter(Ingrediente.id_ingrediente == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingrediente não encontrado")
    return obj


@router.post("/", response_model=IngredienteRead, status_code=status.HTTP_201_CREATED)
def criar_ingrediente(payload: IngredienteCreate, db: Session = Depends(get_db)):
    obj = Ingrediente(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=IngredienteRead)
def atualizar_ingrediente(item_id: int, payload: IngredienteUpdate, db: Session = Depends(get_db)):
    obj = db.query(Ingrediente).filter(Ingrediente.id_ingrediente == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingrediente não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_ingrediente(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Ingrediente).filter(Ingrediente.id_ingrediente == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingrediente não encontrado")
    db.delete(obj)
    db.commit()
    return None

