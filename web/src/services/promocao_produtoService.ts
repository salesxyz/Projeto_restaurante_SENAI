// Chamadas HTTP para o recurso "promocao_produto"
import { api } from './api';
import type { PromocaoProduto, PromocaoProdutoCreate, PromocaoProdutoUpdate } from '../types/promocao_produto';

const BASE_PATH = '/promocao-produto/';

export async function listarPromocaoProduto(): Promise<PromocaoProduto[]> {
  return api.get<PromocaoProduto[]>(BASE_PATH);
}

export async function obterPromocaoProduto(id: number): Promise<PromocaoProduto> {
  return api.get<PromocaoProduto>(`${BASE_PATH}${id}`);
}

export async function criarPromocaoProduto(payload: PromocaoProdutoCreate): Promise<PromocaoProduto> {
  return api.post<PromocaoProduto>(BASE_PATH, payload);
}

export async function atualizarPromocaoProduto(id: number, payload: PromocaoProdutoUpdate): Promise<PromocaoProduto> {
  return api.put<PromocaoProduto>(`${BASE_PATH}${id}`, payload);
}

export async function removerPromocaoProduto(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
