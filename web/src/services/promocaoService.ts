// Chamadas HTTP para o recurso "promocao"
import { api } from './api';
import type { Promocao, PromocaoCreate, PromocaoUpdate } from '../types/promocao';

const BASE_PATH = '/promocao/';

export async function listarPromocao(): Promise<Promocao[]> {
  return api.get<Promocao[]>(BASE_PATH);
}

export async function obterPromocao(id: number): Promise<Promocao> {
  return api.get<Promocao>(`${BASE_PATH}${id}`);
}

export async function criarPromocao(payload: PromocaoCreate): Promise<Promocao> {
  return api.post<Promocao>(BASE_PATH, payload);
}

export async function atualizarPromocao(id: number, payload: PromocaoUpdate): Promise<Promocao> {
  return api.put<Promocao>(`${BASE_PATH}${id}`, payload);
}

export async function removerPromocao(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
