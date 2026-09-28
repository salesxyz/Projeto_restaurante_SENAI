// Chamadas HTTP para o recurso "uso_cupom"
import { api } from './api';
import type { UsoCupom, UsoCupomCreate, UsoCupomUpdate } from '../types/uso_cupom';

const BASE_PATH = '/uso-cupom/';

export async function listarUsoCupom(): Promise<UsoCupom[]> {
  return api.get<UsoCupom[]>(BASE_PATH);
}

export async function obterUsoCupom(id: number): Promise<UsoCupom> {
  return api.get<UsoCupom>(`${BASE_PATH}${id}`);
}

export async function criarUsoCupom(payload: UsoCupomCreate): Promise<UsoCupom> {
  return api.post<UsoCupom>(BASE_PATH, payload);
}

export async function atualizarUsoCupom(id: number, payload: UsoCupomUpdate): Promise<UsoCupom> {
  return api.put<UsoCupom>(`${BASE_PATH}${id}`, payload);
}

export async function removerUsoCupom(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
