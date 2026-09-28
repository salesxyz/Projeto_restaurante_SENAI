// Chamadas HTTP para o recurso "cargo"
import { api } from './api';
import type { Cargo, CargoCreate, CargoUpdate } from '../types/cargo';

const BASE_PATH = '/cargo/';

export async function listarCargo(): Promise<Cargo[]> {
  return api.get<Cargo[]>(BASE_PATH);
}

export async function obterCargo(id: number): Promise<Cargo> {
  return api.get<Cargo>(`${BASE_PATH}${id}`);
}

export async function criarCargo(payload: CargoCreate): Promise<Cargo> {
  return api.post<Cargo>(BASE_PATH, payload);
}

export async function atualizarCargo(id: number, payload: CargoUpdate): Promise<Cargo> {
  return api.put<Cargo>(`${BASE_PATH}${id}`, payload);
}

export async function removerCargo(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
