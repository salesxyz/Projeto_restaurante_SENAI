// Chamadas HTTP para o recurso "fornecedor"
import { api } from './api';
import type { Fornecedor, FornecedorCreate, FornecedorUpdate } from '../types/fornecedor';

const BASE_PATH = '/fornecedor/';

export async function listarFornecedor(): Promise<Fornecedor[]> {
  return api.get<Fornecedor[]>(BASE_PATH);
}

export async function obterFornecedor(id: number): Promise<Fornecedor> {
  return api.get<Fornecedor>(`${BASE_PATH}${id}`);
}

export async function criarFornecedor(payload: FornecedorCreate): Promise<Fornecedor> {
  return api.post<Fornecedor>(BASE_PATH, payload);
}

export async function atualizarFornecedor(id: number, payload: FornecedorUpdate): Promise<Fornecedor> {
  return api.put<Fornecedor>(`${BASE_PATH}${id}`, payload);
}

export async function removerFornecedor(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
