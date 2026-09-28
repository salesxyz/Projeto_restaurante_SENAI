"""Regras de negócio relacionadas a cupons de desconto."""
from datetime import date, datetime

from sqlalchemy.orm import Session

from app.models.cupom_model import Cupom
from app.models.uso_cupom_model import UsoCupom


def validar_cupom(db: Session, codigo: str) -> Cupom:
    """Verifica se o cupom existe e está dentro da vigência. Lança ValueError se inválido."""
    cupom = db.query(Cupom).filter(Cupom.codigo == codigo).first()
    if not cupom:
        raise ValueError("Cupom não encontrado")

    hoje = date.today()
    if cupom.data_inicio and hoje < cupom.data_inicio:
        raise ValueError("Cupom ainda não está vigente")
    if cupom.data_fim and hoje > cupom.data_fim:
        raise ValueError("Cupom expirado")

    return cupom


def aplicar_desconto(valor_total: float, cupom: Cupom) -> float:
    """Aplica o desconto do cupom (percentual ou valor fixo) sobre o valor total."""
    if cupom.tipo_desconto == "percentual":
        desconto = valor_total * (cupom.valor_desconto / 100)
    else:
        desconto = cupom.valor_desconto
    return round(max(valor_total - desconto, 0), 2)


def registrar_uso(db: Session, id_cupom: int, id_pedido: int) -> UsoCupom:
    uso = UsoCupom(id_cupom=id_cupom, id_pedido=id_pedido, data_hora=datetime.utcnow())
    db.add(uso)
    db.commit()
    db.refresh(uso)
    return uso
