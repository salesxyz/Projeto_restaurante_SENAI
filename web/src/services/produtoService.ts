// Chamadas HTTP para o recurso "produto"
import { api } from './api';
import type { Produto, ProdutoCreate, ProdutoUpdate } from '../types/produto';

const BASE_PATH = '/produto/';

export async function listarProduto(): Promise<Produto[]> {
  return api.get<Produto[]>(BASE_PATH);
}

export async function obterProduto(id: number): Promise<Produto> {
  return api.get<Produto>(`${BASE_PATH}${id}`);
}

export async function criarProduto(payload: ProdutoCreate): Promise<Produto> {
  return api.post<Produto>(BASE_PATH, payload);
}

export async function atualizarProduto(id: number, payload: ProdutoUpdate): Promise<Produto> {
  return api.put<Produto>(`${BASE_PATH}${id}`, payload);
}

export async function removerProduto(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
