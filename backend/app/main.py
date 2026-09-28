"""Ponto de entrada da aplicação FastAPI do SALES3DS."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.views.config import settings
from app.views.database import Base, engine

# importa todos os modelos para que Base.metadata os reconheça
import app.models  # noqa: F401

from app.routers.cliente_router import router as cliente_router
from app.routers.mesa_router import router as mesa_router
from app.routers.categoria_router import router as categoria_router
from app.routers.produto_router import router as produto_router
from app.routers.variacao_router import router as variacao_router
from app.routers.ingrediente_router import router as ingrediente_router
from app.routers.fornecedor_router import router as fornecedor_router
from app.routers.composicao_produto_router import router as composicao_produto_router
from app.routers.ingrediente_fornecedor_router import router as ingrediente_fornecedor_router
from app.routers.cargo_router import router as cargo_router
from app.routers.funcionario_router import router as funcionario_router
from app.routers.historico_cargo_router import router as historico_cargo_router
from app.routers.pedido_router import router as pedido_router
from app.routers.item_pedido_router import router as item_pedido_router
from app.routers.adicional_router import router as adicional_router
from app.routers.adicional_item_router import router as adicional_item_router
from app.routers.forma_pagamento_router import router as forma_pagamento_router
from app.routers.pagamento_router import router as pagamento_router
from app.routers.pagamento_forma_router import router as pagamento_forma_router
from app.routers.historico_status_router import router as historico_status_router
from app.routers.entrega_router import router as entrega_router
from app.routers.avaliacao_router import router as avaliacao_router
from app.routers.promocao_router import router as promocao_router
from app.routers.promocao_produto_router import router as promocao_produto_router
from app.routers.cupom_router import router as cupom_router
from app.routers.uso_cupom_router import router as uso_cupom_router

# cria as tabelas no banco (SQLite por padrão) se ainda não existirem
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_PREFIX}/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for r in (
    cliente_router, mesa_router, categoria_router, produto_router, variacao_router,
    ingrediente_router, fornecedor_router, composicao_produto_router,
    ingrediente_fornecedor_router, cargo_router, funcionario_router,
    historico_cargo_router, pedido_router, item_pedido_router, adicional_router,
    adicional_item_router, forma_pagamento_router, pagamento_router,
    pagamento_forma_router, historico_status_router, entrega_router,
    avaliacao_router, promocao_router, promocao_produto_router, cupom_router,
    uso_cupom_router,
):
    app.include_router(r, prefix=settings.API_V1_PREFIX)


@app.get("/", tags=["health"])
def health_check():
    return {"status": "ok", "projeto": settings.PROJECT_NAME}
