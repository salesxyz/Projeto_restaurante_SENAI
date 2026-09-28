"""Rotas REST da entidade "promocao"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.promocao_model import Promocao
from app.schemas.promocao_schema import PromocaoCreate, PromocaoUpdate, PromocaoRead

router = APIRouter(prefix="/promocao", tags=["promocao"])


@router.get("/", response_model=List[PromocaoRead])
def listar_promocao(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Promocao).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=PromocaoRead)
def obter_promocao(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Promocao).filter(Promocao.id_promocao == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promocao não encontrado")
    return obj


@router.post("/", response_model=PromocaoRead, status_code=status.HTTP_201_CREATED)
def criar_promocao(payload: PromocaoCreate, db: Session = Depends(get_db)):
    obj = Promocao(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=PromocaoRead)
def atualizar_promocao(item_id: int, payload: PromocaoUpdate, db: Session = Depends(get_db)):
    obj = db.query(Promocao).filter(Promocao.id_promocao == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promocao não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_promocao(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Promocao).filter(Promocao.id_promocao == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promocao não encontrado")
    db.delete(obj)
    db.commit()
    return None

