// Chamadas HTTP para o recurso "cupom"
import { api } from './api';
import type { Cupom, CupomCreate, CupomUpdate } from '../types/cupom';

const BASE_PATH = '/cupom/';

export async function listarCupom(): Promise<Cupom[]> {
  return api.get<Cupom[]>(BASE_PATH);
}

export async function obterCupom(id: number): Promise<Cupom> {
  return api.get<Cupom>(`${BASE_PATH}${id}`);
}

export async function criarCupom(payload: CupomCreate): Promise<Cupom> {
  return api.post<Cupom>(BASE_PATH, payload);
}

export async function atualizarCupom(id: number, payload: CupomUpdate): Promise<Cupom> {
  return api.put<Cupom>(`${BASE_PATH}${id}`, payload);
}

export async function removerCupom(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
