// Chamadas HTTP para o recurso "mesa"
import { api } from './api';
import type { Mesa, MesaCreate, MesaUpdate } from '../types/mesa';

const BASE_PATH = '/mesa/';

export async function listarMesa(): Promise<Mesa[]> {
  return api.get<Mesa[]>(BASE_PATH);
}

export async function obterMesa(id: number): Promise<Mesa> {
  return api.get<Mesa>(`${BASE_PATH}${id}`);
}

export async function criarMesa(payload: MesaCreate): Promise<Mesa> {
  return api.post<Mesa>(BASE_PATH, payload);
}

export async function atualizarMesa(id: number, payload: MesaUpdate): Promise<Mesa> {
  return api.put<Mesa>(`${BASE_PATH}${id}`, payload);
}

export async function removerMesa(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
