"""Regras de negócio relacionadas a pedidos."""
from datetime import datetime

from sqlalchemy.orm import Session

from app.models.item_pedido_model import ItemPedido
from app.models.produto_model import Produto
from app.models.variacao_model import Variacao
from app.models.historico_status_model import HistoricoStatus
from app.models.pedido_model import Pedido


def calcular_total_pedido(db: Session, id_pedido: int) -> float:
    """Soma produto (com variação) x quantidade de todos os itens do pedido."""
    itens = db.query(ItemPedido).filter(ItemPedido.id_pedido == id_pedido).all()
    total = 0.0
    for item in itens:
        produto = db.query(Produto).filter(Produto.id_produto == item.id_produto).first()
        preco = produto.preco_base if produto else 0.0
        if item.id_variacao:
            variacao = db.query(Variacao).filter(Variacao.id_variacao == item.id_variacao).first()
            if variacao:
                preco += variacao.valor_adicional
        total += preco * item.quantidade
    return round(total, 2)


def alterar_status(db: Session, id_pedido: int, novo_status: str, id_funcionario: int | None = None) -> Pedido:
    """Atualiza o status atual do pedido e registra a mudança no histórico."""
    pedido = db.query(Pedido).filter(Pedido.id_pedido == id_pedido).first()
    if not pedido:
        raise ValueError(f"Pedido {id_pedido} não encontrado")

    pedido.status_atual = novo_status
    db.add(HistoricoStatus(
        id_pedido=id_pedido,
        id_funcionario=id_funcionario,
        status=novo_status,
        data_hora=datetime.utcnow(),
    ))
    db.commit()
    db.refresh(pedido)
    return pedido
