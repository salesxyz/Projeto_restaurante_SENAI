"""Rotas REST da entidade "produto"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.produto_model import Produto
from app.schemas.produto_schema import ProdutoCreate, ProdutoUpdate, ProdutoRead

router = APIRouter(prefix="/produto", tags=["produto"])


@router.get("/", response_model=List[ProdutoRead])
def listar_produto(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Produto).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=ProdutoRead)
def obter_produto(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Produto).filter(Produto.id_produto == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    return obj


@router.post("/", response_model=ProdutoRead, status_code=status.HTTP_201_CREATED)
def criar_produto(payload: ProdutoCreate, db: Session = Depends(get_db)):
    obj = Produto(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=ProdutoRead)
def atualizar_produto(item_id: int, payload: ProdutoUpdate, db: Session = Depends(get_db)):
    obj = db.query(Produto).filter(Produto.id_produto == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_produto(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Produto).filter(Produto.id_produto == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    db.delete(obj)
    db.commit()
    return None

