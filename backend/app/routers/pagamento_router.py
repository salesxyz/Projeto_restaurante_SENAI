"""Rotas REST da entidade "pagamento"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.pagamento_model import Pagamento
from app.schemas.pagamento_schema import PagamentoCreate, PagamentoUpdate, PagamentoRead

router = APIRouter(prefix="/pagamento", tags=["pagamento"])


@router.get("/", response_model=List[PagamentoRead])
def listar_pagamento(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Pagamento).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=PagamentoRead)
def obter_pagamento(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Pagamento).filter(Pagamento.id_pagamento == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pagamento não encontrado")
    return obj


@router.post("/", response_model=PagamentoRead, status_code=status.HTTP_201_CREATED)
def criar_pagamento(payload: PagamentoCreate, db: Session = Depends(get_db)):
    obj = Pagamento(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=PagamentoRead)
def atualizar_pagamento(item_id: int, payload: PagamentoUpdate, db: Session = Depends(get_db)):
    obj = db.query(Pagamento).filter(Pagamento.id_pagamento == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pagamento não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_pagamento(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Pagamento).filter(Pagamento.id_pagamento == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pagamento não encontrado")
    db.delete(obj)
    db.commit()
    return None

