"""Regras de negócio relacionadas a pagamentos de pedidos."""
from sqlalchemy.orm import Session

from app.models.pagamento_model import Pagamento
from app.services.pedido_service import calcular_total_pedido


def valor_pago_total(db: Session, id_pedido: int) -> float:
    pagamentos = db.query(Pagamento).filter(Pagamento.id_pedido == id_pedido).all()
    return round(sum(p.valor_pago for p in pagamentos), 2)


def pedido_esta_quitado(db: Session, id_pedido: int) -> bool:
    total_devido = calcular_total_pedido(db, id_pedido)
    total_pago = valor_pago_total(db, id_pedido)
    return total_pago >= total_devido
