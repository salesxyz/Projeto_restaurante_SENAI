// Chamadas HTTP para o recurso "historico_status"
import { api } from './api';
import type { HistoricoStatus, HistoricoStatusCreate, HistoricoStatusUpdate } from '../types/historico_status';

const BASE_PATH = '/historico-status/';

export async function listarHistoricoStatus(): Promise<HistoricoStatus[]> {
  return api.get<HistoricoStatus[]>(BASE_PATH);
}

export async function obterHistoricoStatus(id: number): Promise<HistoricoStatus> {
  return api.get<HistoricoStatus>(`${BASE_PATH}${id}`);
}

export async function criarHistoricoStatus(payload: HistoricoStatusCreate): Promise<HistoricoStatus> {
  return api.post<HistoricoStatus>(BASE_PATH, payload);
}

export async function atualizarHistoricoStatus(id: number, payload: HistoricoStatusUpdate): Promise<HistoricoStatus> {
  return api.put<HistoricoStatus>(`${BASE_PATH}${id}`, payload);
}

export async function removerHistoricoStatus(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
