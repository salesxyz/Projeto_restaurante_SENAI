"""Rotas REST da entidade "composicao_produto"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.composicao_produto_model import ComposicaoProduto
from app.schemas.composicao_produto_schema import ComposicaoProdutoCreate, ComposicaoProdutoUpdate, ComposicaoProdutoRead

router = APIRouter(prefix="/composicao-produto", tags=["composicao_produto"])


@router.get("/", response_model=List[ComposicaoProdutoRead])
def listar_composicao_produto(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(ComposicaoProduto).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=ComposicaoProdutoRead)
def obter_composicao_produto(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(ComposicaoProduto).filter(ComposicaoProduto.id_composicao == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ComposicaoProduto não encontrado")
    return obj


@router.post("/", response_model=ComposicaoProdutoRead, status_code=status.HTTP_201_CREATED)
def criar_composicao_produto(payload: ComposicaoProdutoCreate, db: Session = Depends(get_db)):
    obj = ComposicaoProduto(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=ComposicaoProdutoRead)
def atualizar_composicao_produto(item_id: int, payload: ComposicaoProdutoUpdate, db: Session = Depends(get_db)):
    obj = db.query(ComposicaoProduto).filter(ComposicaoProduto.id_composicao == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ComposicaoProduto não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_composicao_produto(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(ComposicaoProduto).filter(ComposicaoProduto.id_composicao == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ComposicaoProduto não encontrado")
    db.delete(obj)
    db.commit()
    return None

