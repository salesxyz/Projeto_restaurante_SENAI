"""Rotas REST da entidade "historico_cargo"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.historico_cargo_model import HistoricoCargo
from app.schemas.historico_cargo_schema import HistoricoCargoCreate, HistoricoCargoUpdate, HistoricoCargoRead

router = APIRouter(prefix="/historico-cargo", tags=["historico_cargo"])


@router.get("/", response_model=List[HistoricoCargoRead])
def listar_historico_cargo(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(HistoricoCargo).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=HistoricoCargoRead)
def obter_historico_cargo(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(HistoricoCargo).filter(HistoricoCargo.id_historico_cargo == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HistoricoCargo não encontrado")
    return obj


@router.post("/", response_model=HistoricoCargoRead, status_code=status.HTTP_201_CREATED)
def criar_historico_cargo(payload: HistoricoCargoCreate, db: Session = Depends(get_db)):
    obj = HistoricoCargo(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=HistoricoCargoRead)
def atualizar_historico_cargo(item_id: int, payload: HistoricoCargoUpdate, db: Session = Depends(get_db)):
    obj = db.query(HistoricoCargo).filter(HistoricoCargo.id_historico_cargo == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HistoricoCargo não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_historico_cargo(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(HistoricoCargo).filter(HistoricoCargo.id_historico_cargo == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HistoricoCargo não encontrado")
    db.delete(obj)
    db.commit()
    return None

