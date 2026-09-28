// Chamadas HTTP para o recurso "categoria"
import { api } from './api';
import type { Categoria, CategoriaCreate, CategoriaUpdate } from '../types/categoria';

const BASE_PATH = '/categoria/';

export async function listarCategoria(): Promise<Categoria[]> {
  return api.get<Categoria[]>(BASE_PATH);
}

export async function obterCategoria(id: number): Promise<Categoria> {
  return api.get<Categoria>(`${BASE_PATH}${id}`);
}

export async function criarCategoria(payload: CategoriaCreate): Promise<Categoria> {
  return api.post<Categoria>(BASE_PATH, payload);
}

export async function atualizarCategoria(id: number, payload: CategoriaUpdate): Promise<Categoria> {
  return api.put<Categoria>(`${BASE_PATH}${id}`, payload);
}

export async function removerCategoria(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
