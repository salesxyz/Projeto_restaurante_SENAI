// Chamadas HTTP para o recurso "pagamento"
import { api } from './api';
import type { Pagamento, PagamentoCreate, PagamentoUpdate } from '../types/pagamento';

const BASE_PATH = '/pagamento/';

export async function listarPagamento(): Promise<Pagamento[]> {
  return api.get<Pagamento[]>(BASE_PATH);
}

export async function obterPagamento(id: number): Promise<Pagamento> {
  return api.get<Pagamento>(`${BASE_PATH}${id}`);
}

export async function criarPagamento(payload: PagamentoCreate): Promise<Pagamento> {
  return api.post<Pagamento>(BASE_PATH, payload);
}

export async function atualizarPagamento(id: number, payload: PagamentoUpdate): Promise<Pagamento> {
  return api.put<Pagamento>(`${BASE_PATH}${id}`, payload);
}

export async function removerPagamento(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
