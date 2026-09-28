"""Rotas REST da entidade "promocao_produto"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.promocao_produto_model import PromocaoProduto
from app.schemas.promocao_produto_schema import PromocaoProdutoCreate, PromocaoProdutoUpdate, PromocaoProdutoRead

router = APIRouter(prefix="/promocao-produto", tags=["promocao_produto"])


@router.get("/", response_model=List[PromocaoProdutoRead])
def listar_promocao_produto(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(PromocaoProduto).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=PromocaoProdutoRead)
def obter_promocao_produto(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(PromocaoProduto).filter(PromocaoProduto.id_promocao_produto == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PromocaoProduto não encontrado")
    return obj


@router.post("/", response_model=PromocaoProdutoRead, status_code=status.HTTP_201_CREATED)
def criar_promocao_produto(payload: PromocaoProdutoCreate, db: Session = Depends(get_db)):
    obj = PromocaoProduto(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=PromocaoProdutoRead)
def atualizar_promocao_produto(item_id: int, payload: PromocaoProdutoUpdate, db: Session = Depends(get_db)):
    obj = db.query(PromocaoProduto).filter(PromocaoProduto.id_promocao_produto == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PromocaoProduto não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_promocao_produto(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(PromocaoProduto).filter(PromocaoProduto.id_promocao_produto == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PromocaoProduto não encontrado")
    db.delete(obj)
    db.commit()
    return None

