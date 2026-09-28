// Chamadas HTTP para o recurso "historico_cargo"
import { api } from './api';
import type { HistoricoCargo, HistoricoCargoCreate, HistoricoCargoUpdate } from '../types/historico_cargo';

const BASE_PATH = '/historico-cargo/';

export async function listarHistoricoCargo(): Promise<HistoricoCargo[]> {
  return api.get<HistoricoCargo[]>(BASE_PATH);
}

export async function obterHistoricoCargo(id: number): Promise<HistoricoCargo> {
  return api.get<HistoricoCargo>(`${BASE_PATH}${id}`);
}

export async function criarHistoricoCargo(payload: HistoricoCargoCreate): Promise<HistoricoCargo> {
  return api.post<HistoricoCargo>(BASE_PATH, payload);
}

export async function atualizarHistoricoCargo(id: number, payload: HistoricoCargoUpdate): Promise<HistoricoCargo> {
  return api.put<HistoricoCargo>(`${BASE_PATH}${id}`, payload);
}

export async function removerHistoricoCargo(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
