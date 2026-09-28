"""Rotas REST da entidade "ingrediente_fornecedor"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.ingrediente_fornecedor_model import IngredienteFornecedor
from app.schemas.ingrediente_fornecedor_schema import IngredienteFornecedorCreate, IngredienteFornecedorUpdate, IngredienteFornecedorRead

router = APIRouter(prefix="/ingrediente-fornecedor", tags=["ingrediente_fornecedor"])


@router.get("/", response_model=List[IngredienteFornecedorRead])
def listar_ingrediente_fornecedor(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(IngredienteFornecedor).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=IngredienteFornecedorRead)
def obter_ingrediente_fornecedor(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(IngredienteFornecedor).filter(IngredienteFornecedor.id_ingrediente_fornecedor == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="IngredienteFornecedor não encontrado")
    return obj


@router.post("/", response_model=IngredienteFornecedorRead, status_code=status.HTTP_201_CREATED)
def criar_ingrediente_fornecedor(payload: IngredienteFornecedorCreate, db: Session = Depends(get_db)):
    obj = IngredienteFornecedor(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=IngredienteFornecedorRead)
def atualizar_ingrediente_fornecedor(item_id: int, payload: IngredienteFornecedorUpdate, db: Session = Depends(get_db)):
    obj = db.query(IngredienteFornecedor).filter(IngredienteFornecedor.id_ingrediente_fornecedor == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="IngredienteFornecedor não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_ingrediente_fornecedor(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(IngredienteFornecedor).filter(IngredienteFornecedor.id_ingrediente_fornecedor == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="IngredienteFornecedor não encontrado")
    db.delete(obj)
    db.commit()
    return None

