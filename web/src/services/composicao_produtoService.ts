// Chamadas HTTP para o recurso "composicao_produto"
import { api } from './api';
import type { ComposicaoProduto, ComposicaoProdutoCreate, ComposicaoProdutoUpdate } from '../types/composicao_produto';

const BASE_PATH = '/composicao-produto/';

export async function listarComposicaoProduto(): Promise<ComposicaoProduto[]> {
  return api.get<ComposicaoProduto[]>(BASE_PATH);
}

export async function obterComposicaoProduto(id: number): Promise<ComposicaoProduto> {
  return api.get<ComposicaoProduto>(`${BASE_PATH}${id}`);
}

export async function criarComposicaoProduto(payload: ComposicaoProdutoCreate): Promise<ComposicaoProduto> {
  return api.post<ComposicaoProduto>(BASE_PATH, payload);
}

export async function atualizarComposicaoProduto(id: number, payload: ComposicaoProdutoUpdate): Promise<ComposicaoProduto> {
  return api.put<ComposicaoProduto>(`${BASE_PATH}${id}`, payload);
}

export async function removerComposicaoProduto(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
