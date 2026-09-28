"""Rotas REST da entidade "forma_pagamento"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.forma_pagamento_model import FormaPagamento
from app.schemas.forma_pagamento_schema import FormaPagamentoCreate, FormaPagamentoUpdate, FormaPagamentoRead

router = APIRouter(prefix="/forma-pagamento", tags=["forma_pagamento"])


@router.get("/", response_model=List[FormaPagamentoRead])
def listar_forma_pagamento(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(FormaPagamento).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=FormaPagamentoRead)
def obter_forma_pagamento(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(FormaPagamento).filter(FormaPagamento.id_forma_pagamento == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="FormaPagamento não encontrado")
    return obj


@router.post("/", response_model=FormaPagamentoRead, status_code=status.HTTP_201_CREATED)
def criar_forma_pagamento(payload: FormaPagamentoCreate, db: Session = Depends(get_db)):
    obj = FormaPagamento(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=FormaPagamentoRead)
def atualizar_forma_pagamento(item_id: int, payload: FormaPagamentoUpdate, db: Session = Depends(get_db)):
    obj = db.query(FormaPagamento).filter(FormaPagamento.id_forma_pagamento == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="FormaPagamento não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_forma_pagamento(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(FormaPagamento).filter(FormaPagamento.id_forma_pagamento == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="FormaPagamento não encontrado")
    db.delete(obj)
    db.commit()
    return None

