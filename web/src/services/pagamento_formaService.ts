// Chamadas HTTP para o recurso "pagamento_forma"
import { api } from './api';
import type { PagamentoForma, PagamentoFormaCreate, PagamentoFormaUpdate } from '../types/pagamento_forma';

const BASE_PATH = '/pagamento-forma/';

export async function listarPagamentoForma(): Promise<PagamentoForma[]> {
  return api.get<PagamentoForma[]>(BASE_PATH);
}

export async function obterPagamentoForma(id: number): Promise<PagamentoForma> {
  return api.get<PagamentoForma>(`${BASE_PATH}${id}`);
}

export async function criarPagamentoForma(payload: PagamentoFormaCreate): Promise<PagamentoForma> {
  return api.post<PagamentoForma>(BASE_PATH, payload);
}

export async function atualizarPagamentoForma(id: number, payload: PagamentoFormaUpdate): Promise<PagamentoForma> {
  return api.put<PagamentoForma>(`${BASE_PATH}${id}`, payload);
}

export async function removerPagamentoForma(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
