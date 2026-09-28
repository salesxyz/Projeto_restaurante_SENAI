// Chamadas HTTP para o recurso "adicional_item"
import { api } from './api';
import type { AdicionalItem, AdicionalItemCreate, AdicionalItemUpdate } from '../types/adicional_item';

const BASE_PATH = '/adicional-item/';

export async function listarAdicionalItem(): Promise<AdicionalItem[]> {
  return api.get<AdicionalItem[]>(BASE_PATH);
}

export async function obterAdicionalItem(id: number): Promise<AdicionalItem> {
  return api.get<AdicionalItem>(`${BASE_PATH}${id}`);
}

export async function criarAdicionalItem(payload: AdicionalItemCreate): Promise<AdicionalItem> {
  return api.post<AdicionalItem>(BASE_PATH, payload);
}

export async function atualizarAdicionalItem(id: number, payload: AdicionalItemUpdate): Promise<AdicionalItem> {
  return api.put<AdicionalItem>(`${BASE_PATH}${id}`, payload);
}

export async function removerAdicionalItem(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
