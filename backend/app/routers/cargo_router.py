"""Rotas REST da entidade "cargo"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.cargo_model import Cargo
from app.schemas.cargo_schema import CargoCreate, CargoUpdate, CargoRead

router = APIRouter(prefix="/cargo", tags=["cargo"])


@router.get("/", response_model=List[CargoRead])
def listar_cargo(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Cargo).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=CargoRead)
def obter_cargo(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Cargo).filter(Cargo.id_cargo == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cargo não encontrado")
    return obj


@router.post("/", response_model=CargoRead, status_code=status.HTTP_201_CREATED)
def criar_cargo(payload: CargoCreate, db: Session = Depends(get_db)):
    obj = Cargo(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=CargoRead)
def atualizar_cargo(item_id: int, payload: CargoUpdate, db: Session = Depends(get_db)):
    obj = db.query(Cargo).filter(Cargo.id_cargo == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cargo não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_cargo(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Cargo).filter(Cargo.id_cargo == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cargo não encontrado")
    db.delete(obj)
    db.commit()
    return None

