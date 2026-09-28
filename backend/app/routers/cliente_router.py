"""Rotas REST da entidade "cliente"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.cliente_model import Cliente
from app.schemas.cliente_schema import ClienteCreate, ClienteUpdate, ClienteRead

router = APIRouter(prefix="/cliente", tags=["cliente"])


@router.get("/", response_model=List[ClienteRead])
def listar_cliente(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Cliente).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=ClienteRead)
def obter_cliente(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Cliente).filter(Cliente.id_cliente == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado")
    return obj


@router.post("/", response_model=ClienteRead, status_code=status.HTTP_201_CREATED)
def criar_cliente(payload: ClienteCreate, db: Session = Depends(get_db)):
    obj = Cliente(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=ClienteRead)
def atualizar_cliente(item_id: int, payload: ClienteUpdate, db: Session = Depends(get_db)):
    obj = db.query(Cliente).filter(Cliente.id_cliente == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_cliente(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Cliente).filter(Cliente.id_cliente == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado")
    db.delete(obj)
    db.commit()
    return None

