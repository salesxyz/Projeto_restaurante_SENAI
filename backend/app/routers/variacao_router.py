"""Rotas REST da entidade "variacao"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.variacao_model import Variacao
from app.schemas.variacao_schema import VariacaoCreate, VariacaoUpdate, VariacaoRead

router = APIRouter(prefix="/variacao", tags=["variacao"])


@router.get("/", response_model=List[VariacaoRead])
def listar_variacao(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Variacao).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=VariacaoRead)
def obter_variacao(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Variacao).filter(Variacao.id_variacao == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Variacao não encontrado")
    return obj


@router.post("/", response_model=VariacaoRead, status_code=status.HTTP_201_CREATED)
def criar_variacao(payload: VariacaoCreate, db: Session = Depends(get_db)):
    obj = Variacao(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=VariacaoRead)
def atualizar_variacao(item_id: int, payload: VariacaoUpdate, db: Session = Depends(get_db)):
    obj = db.query(Variacao).filter(Variacao.id_variacao == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Variacao não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_variacao(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Variacao).filter(Variacao.id_variacao == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Variacao não encontrado")
    db.delete(obj)
    db.commit()
    return None

