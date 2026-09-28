"""Rotas REST da entidade "fornecedor"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.fornecedor_model import Fornecedor
from app.schemas.fornecedor_schema import FornecedorCreate, FornecedorUpdate, FornecedorRead

router = APIRouter(prefix="/fornecedor", tags=["fornecedor"])


@router.get("/", response_model=List[FornecedorRead])
def listar_fornecedor(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Fornecedor).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=FornecedorRead)
def obter_fornecedor(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Fornecedor).filter(Fornecedor.id_fornecedor == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fornecedor não encontrado")
    return obj


@router.post("/", response_model=FornecedorRead, status_code=status.HTTP_201_CREATED)
def criar_fornecedor(payload: FornecedorCreate, db: Session = Depends(get_db)):
    obj = Fornecedor(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=FornecedorRead)
def atualizar_fornecedor(item_id: int, payload: FornecedorUpdate, db: Session = Depends(get_db)):
    obj = db.query(Fornecedor).filter(Fornecedor.id_fornecedor == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fornecedor não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_fornecedor(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Fornecedor).filter(Fornecedor.id_fornecedor == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fornecedor não encontrado")
    db.delete(obj)
    db.commit()
    return None

