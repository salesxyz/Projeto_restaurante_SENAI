// Chamadas HTTP para o recurso "variacao"
import { api } from './api';
import type { Variacao, VariacaoCreate, VariacaoUpdate } from '../types/variacao';

const BASE_PATH = '/variacao/';

export async function listarVariacao(): Promise<Variacao[]> {
  return api.get<Variacao[]>(BASE_PATH);
}

export async function obterVariacao(id: number): Promise<Variacao> {
  return api.get<Variacao>(`${BASE_PATH}${id}`);
}

export async function criarVariacao(payload: VariacaoCreate): Promise<Variacao> {
  return api.post<Variacao>(BASE_PATH, payload);
}

export async function atualizarVariacao(id: number, payload: VariacaoUpdate): Promise<Variacao> {
  return api.put<Variacao>(`${BASE_PATH}${id}`, payload);
}

export async function removerVariacao(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
