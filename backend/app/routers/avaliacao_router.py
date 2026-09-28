"""Rotas REST da entidade "avaliacao"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.avaliacao_model import Avaliacao
from app.schemas.avaliacao_schema import AvaliacaoCreate, AvaliacaoUpdate, AvaliacaoRead

router = APIRouter(prefix="/avaliacao", tags=["avaliacao"])


@router.get("/", response_model=List[AvaliacaoRead])
def listar_avaliacao(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Avaliacao).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=AvaliacaoRead)
def obter_avaliacao(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Avaliacao).filter(Avaliacao.id_avaliacao == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Avaliacao não encontrado")
    return obj


@router.post("/", response_model=AvaliacaoRead, status_code=status.HTTP_201_CREATED)
def criar_avaliacao(payload: AvaliacaoCreate, db: Session = Depends(get_db)):
    obj = Avaliacao(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=AvaliacaoRead)
def atualizar_avaliacao(item_id: int, payload: AvaliacaoUpdate, db: Session = Depends(get_db)):
    obj = db.query(Avaliacao).filter(Avaliacao.id_avaliacao == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Avaliacao não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_avaliacao(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Avaliacao).filter(Avaliacao.id_avaliacao == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Avaliacao não encontrado")
    db.delete(obj)
    db.commit()
    return None

