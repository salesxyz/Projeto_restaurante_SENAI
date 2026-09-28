// Chamadas HTTP para o recurso "ingrediente"
import { api } from './api';
import type { Ingrediente, IngredienteCreate, IngredienteUpdate } from '../types/ingrediente';

const BASE_PATH = '/ingrediente/';

export async function listarIngrediente(): Promise<Ingrediente[]> {
  return api.get<Ingrediente[]>(BASE_PATH);
}

export async function obterIngrediente(id: number): Promise<Ingrediente> {
  return api.get<Ingrediente>(`${BASE_PATH}${id}`);
}

export async function criarIngrediente(payload: IngredienteCreate): Promise<Ingrediente> {
  return api.post<Ingrediente>(BASE_PATH, payload);
}

export async function atualizarIngrediente(id: number, payload: IngredienteUpdate): Promise<Ingrediente> {
  return api.put<Ingrediente>(`${BASE_PATH}${id}`, payload);
}

export async function removerIngrediente(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
