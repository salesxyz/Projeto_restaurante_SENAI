"""Rotas REST da entidade "categoria"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.categoria_model import Categoria
from app.schemas.categoria_schema import CategoriaCreate, CategoriaUpdate, CategoriaRead

router = APIRouter(prefix="/categoria", tags=["categoria"])


@router.get("/", response_model=List[CategoriaRead])
def listar_categoria(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Categoria).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=CategoriaRead)
def obter_categoria(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Categoria).filter(Categoria.id_categoria == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrado")
    return obj


@router.post("/", response_model=CategoriaRead, status_code=status.HTTP_201_CREATED)
def criar_categoria(payload: CategoriaCreate, db: Session = Depends(get_db)):
    obj = Categoria(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=CategoriaRead)
def atualizar_categoria(item_id: int, payload: CategoriaUpdate, db: Session = Depends(get_db)):
    obj = db.query(Categoria).filter(Categoria.id_categoria == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_categoria(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Categoria).filter(Categoria.id_categoria == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrado")
    db.delete(obj)
    db.commit()
    return None

