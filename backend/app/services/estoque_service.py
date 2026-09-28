"""Regras de negócio relacionadas à baixa de estoque de ingredientes."""
from sqlalchemy.orm import Session

from app.models.composicao_produto_model import ComposicaoProduto
from app.models.ingrediente_model import Ingrediente


def baixar_estoque_por_item(db: Session, id_produto: int, quantidade_vendida: int) -> None:
    """Para cada ingrediente da ficha técnica do produto, subtrai a quantidade usada."""
    composicoes = (
        db.query(ComposicaoProduto)
        .filter(ComposicaoProduto.id_produto == id_produto)
        .all()
    )
    for comp in composicoes:
        ingrediente = (
            db.query(Ingrediente)
            .filter(Ingrediente.id_ingrediente == comp.id_ingrediente)
            .first()
        )
        if ingrediente:
            ingrediente.quantidade_estoque -= comp.quantidade_utilizada * quantidade_vendida
    db.commit()


def ingredientes_abaixo_do_minimo(db: Session, minimo: float = 5.0) -> list[Ingrediente]:
    """Lista ingredientes com estoque abaixo de um limiar — útil para alertas de compra."""
    return db.query(Ingrediente).filter(Ingrediente.quantidade_estoque < minimo).all()
