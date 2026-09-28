"""Rotas REST da entidade "historico_status"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.historico_status_model import HistoricoStatus
from app.schemas.historico_status_schema import HistoricoStatusCreate, HistoricoStatusUpdate, HistoricoStatusRead

router = APIRouter(prefix="/historico-status", tags=["historico_status"])


@router.get("/", response_model=List[HistoricoStatusRead])
def listar_historico_status(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(HistoricoStatus).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=HistoricoStatusRead)
def obter_historico_status(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(HistoricoStatus).filter(HistoricoStatus.id_historico == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HistoricoStatus não encontrado")
    return obj


@router.post("/", response_model=HistoricoStatusRead, status_code=status.HTTP_201_CREATED)
def criar_historico_status(payload: HistoricoStatusCreate, db: Session = Depends(get_db)):
    obj = HistoricoStatus(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=HistoricoStatusRead)
def atualizar_historico_status(item_id: int, payload: HistoricoStatusUpdate, db: Session = Depends(get_db)):
    obj = db.query(HistoricoStatus).filter(HistoricoStatus.id_historico == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HistoricoStatus não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_historico_status(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(HistoricoStatus).filter(HistoricoStatus.id_historico == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HistoricoStatus não encontrado")
    db.delete(obj)
    db.commit()
    return None

