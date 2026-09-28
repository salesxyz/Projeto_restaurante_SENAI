"""Rotas REST da entidade "pagamento_forma"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.pagamento_forma_model import PagamentoForma
from app.schemas.pagamento_forma_schema import PagamentoFormaCreate, PagamentoFormaUpdate, PagamentoFormaRead

router = APIRouter(prefix="/pagamento-forma", tags=["pagamento_forma"])


@router.get("/", response_model=List[PagamentoFormaRead])
def listar_pagamento_forma(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(PagamentoForma).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=PagamentoFormaRead)
def obter_pagamento_forma(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(PagamentoForma).filter(PagamentoForma.id_pagamento_forma == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PagamentoForma não encontrado")
    return obj


@router.post("/", response_model=PagamentoFormaRead, status_code=status.HTTP_201_CREATED)
def criar_pagamento_forma(payload: PagamentoFormaCreate, db: Session = Depends(get_db)):
    obj = PagamentoForma(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=PagamentoFormaRead)
def atualizar_pagamento_forma(item_id: int, payload: PagamentoFormaUpdate, db: Session = Depends(get_db)):
    obj = db.query(PagamentoForma).filter(PagamentoForma.id_pagamento_forma == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PagamentoForma não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_pagamento_forma(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(PagamentoForma).filter(PagamentoForma.id_pagamento_forma == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PagamentoForma não encontrado")
    db.delete(obj)
    db.commit()
    return None

