// Chamadas HTTP para o recurso "avaliacao"
import { api } from './api';
import type { Avaliacao, AvaliacaoCreate, AvaliacaoUpdate } from '../types/avaliacao';

const BASE_PATH = '/avaliacao/';

export async function listarAvaliacao(): Promise<Avaliacao[]> {
  return api.get<Avaliacao[]>(BASE_PATH);
}

export async function obterAvaliacao(id: number): Promise<Avaliacao> {
  return api.get<Avaliacao>(`${BASE_PATH}${id}`);
}

export async function criarAvaliacao(payload: AvaliacaoCreate): Promise<Avaliacao> {
  return api.post<Avaliacao>(BASE_PATH, payload);
}

export async function atualizarAvaliacao(id: number, payload: AvaliacaoUpdate): Promise<Avaliacao> {
  return api.put<Avaliacao>(`${BASE_PATH}${id}`, payload);
}

export async function removerAvaliacao(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
