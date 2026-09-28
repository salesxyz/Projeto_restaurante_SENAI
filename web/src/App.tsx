import { useEffect, useState } from 'react';
import type { Produto } from './types/produto';
import { listarProduto } from './services/produtoService';
import './styles/global.css';

function App() {
  const [produtos, setProdutos] = useState<Produto[]>([]);
  const [erro, setErro] = useState<string | null>(null);
  const [carregando, setCarregando] = useState(true);

  useEffect(() => {
    listarProduto()
      .then(setProdutos)
      .catch((e: Error) => setErro(e.message))
      .finally(() => setCarregando(false));
  }, []);

  return (
    <div className="app">
      <header>
        <h1>SALES3DS</h1>
        <p>Frontend conectado à API FastAPI em {import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api/v1'}</p>
      </header>

      <main>
        <h2>Produtos</h2>
        {carregando && <p>Carregando...</p>}
        {erro && (
          <p className="erro">
            Não foi possível conectar ao backend ({erro}). Confirme que o servidor FastAPI está
            rodando em <code>localhost:8000</code>.
          </p>
        )}
        {!carregando && !erro && produtos.length === 0 && <p>Nenhum produto cadastrado ainda.</p>}
        <ul>
          {produtos.map((p) => (
            <li key={p.id_produto}>
              {p.nome} — R$ {p.preco_base.toFixed(2)}
            </li>
          ))}
        </ul>
      </main>
    </div>
  );
}

export default App;
