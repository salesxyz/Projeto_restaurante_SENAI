// Chamadas HTTP para o recurso "entrega"
import { api } from './api';
import type { Entrega, EntregaCreate, EntregaUpdate } from '../types/entrega';

const BASE_PATH = '/entrega/';

export async function listarEntrega(): Promise<Entrega[]> {
  return api.get<Entrega[]>(BASE_PATH);
}

export async function obterEntrega(id: number): Promise<Entrega> {
  return api.get<Entrega>(`${BASE_PATH}${id}`);
}

export async function criarEntrega(payload: EntregaCreate): Promise<Entrega> {
  return api.post<Entrega>(BASE_PATH, payload);
}

export async function atualizarEntrega(id: number, payload: EntregaUpdate): Promise<Entrega> {
  return api.put<Entrega>(`${BASE_PATH}${id}`, payload);
}

export async function removerEntrega(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
