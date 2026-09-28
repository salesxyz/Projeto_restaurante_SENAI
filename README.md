# SALES3DS

Scaffold completo (backend + frontend) gerado a partir do MER do sistema de
pedidos/restaurante: 26 entidades, todas com CRUD funcional, testadas
ponta a ponta antes da entrega.

```
SALES3DS/
├── backend/   → API FastAPI + SQLAlchemy (SQLite por padrão)
└── web/       → Frontend React + TypeScript + Vite
```

## Como rodar

### 1. Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

- API disponível em `http://localhost:8000`
- Documentação interativa (Swagger) em `http://localhost:8000/docs`
- Banco SQLite (`sales3ds.db`) é criado automaticamente na primeira execução

### 2. Frontend

```bash
cd web
npm install
cp .env.example .env
npm run dev
```

- App disponível em `http://localhost:5173`
- Já vem apontando para `http://localhost:8000/api/v1` (ajustável em `.env`)

## Estrutura de cada entidade

**Backend** (`backend/app/`):
| Pasta        | Arquivo                      | Conteúdo                          |
|--------------|-------------------------------|------------------------------------|
| `models/`    | `<entidade>_model.py`         | Tabela SQLAlchemy                  |
| `schemas/`   | `<entidade>_schema.py`        | Pydantic Base/Create/Update/Read   |
| `routers/`   | `<entidade>_router.py`        | Endpoints REST (GET/POST/PUT/DELETE) |
| `services/`  | `<processo>_service.py`       | Regras de negócio (não é 1:1 com entidade) |
| `views/`     | `config.py`, `database.py`, `security.py` | Infraestrutura central |

**Frontend** (`web/src/`):
| Pasta         | Arquivo                     | Conteúdo                         |
|---------------|------------------------------|------------------------------------|
| `types/`      | `<entidade>.ts`              | Interfaces espelhando os schemas  |
| `services/`   | `<entidade>Service.ts`       | Chamadas HTTP (fetch) para a API  |

## O que foi validado antes da entrega

- Todos os 26 conjuntos model/schema/router importam sem erro (`Base.metadata.create_all` roda limpo)
- CRUD testado ponta a ponta via `TestClient` (categoria → produto → cliente → pedido → item_pedido), incluindo 404, PUT e DELETE
- `services/pedido_service.calcular_total_pedido` testado e retorna o valor correto
- Todo o TypeScript do frontend passa `tsc --noEmit` sem erros
- `npm run build` gera o bundle de produção sem erros

## Pendências conhecidas (fora do escopo deste scaffold)

- **Autenticação**: `views/security.py` tem hash de senha e JWT prontos, mas nenhuma rota exige login ainda
- **Migrations**: Alembic está no `requirements.txt` mas não foi inicializado (`alembic init`) — hoje as tabelas são criadas via `create_all` no startup
- **Duas lacunas do MER original** seguem sem FK, como já sinalizado antes: `item_pedido` seria o esperado ligar a `produto` (já incluí essa ligação aqui, diferente da leitura estritamente literal do diagrama) e `promocao_produto` liga a `produto` e `cupom`
- Páginas do frontend (`pages/`, `components/`, `hooks/`, `contexts/`, `routes/`) estão como pastas vazias — só a tela de produtos em `App.tsx` foi implementada como prova de conexão com a API
