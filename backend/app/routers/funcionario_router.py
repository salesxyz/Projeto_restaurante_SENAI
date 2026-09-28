"""Rotas REST da entidade "funcionario"."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.funcionario_model import Funcionario
from app.schemas.funcionario_schema import FuncionarioCreate, FuncionarioUpdate, FuncionarioRead

router = APIRouter(prefix="/funcionario", tags=["funcionario"])


@router.get("/", response_model=List[FuncionarioRead])
def listar_funcionario(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Funcionario).offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=FuncionarioRead)
def obter_funcionario(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Funcionario).filter(Funcionario.id_funcionario == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Funcionario não encontrado")
    return obj


@router.post("/", response_model=FuncionarioRead, status_code=status.HTTP_201_CREATED)
def criar_funcionario(payload: FuncionarioCreate, db: Session = Depends(get_db)):
    obj = Funcionario(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.put("/{item_id}", response_model=FuncionarioRead)
def atualizar_funcionario(item_id: int, payload: FuncionarioUpdate, db: Session = Depends(get_db)):
    obj = db.query(Funcionario).filter(Funcionario.id_funcionario == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Funcionario não encontrado")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_funcionario(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(Funcionario).filter(Funcionario.id_funcionario == item_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Funcionario não encontrado")
    db.delete(obj)
    db.commit()
    return None

