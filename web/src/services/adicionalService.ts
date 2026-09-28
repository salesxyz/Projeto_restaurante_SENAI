// Chamadas HTTP para o recurso "adicional"
import { api } from './api';
import type { Adicional, AdicionalCreate, AdicionalUpdate } from '../types/adicional';

const BASE_PATH = '/adicional/';

export async function listarAdicional(): Promise<Adicional[]> {
  return api.get<Adicional[]>(BASE_PATH);
}

export async function obterAdicional(id: number): Promise<Adicional> {
  return api.get<Adicional>(`${BASE_PATH}${id}`);
}

export async function criarAdicional(payload: AdicionalCreate): Promise<Adicional> {
  return api.post<Adicional>(BASE_PATH, payload);
}

export async function atualizarAdicional(id: number, payload: AdicionalUpdate): Promise<Adicional> {
  return api.put<Adicional>(`${BASE_PATH}${id}`, payload);
}

export async function removerAdicional(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
