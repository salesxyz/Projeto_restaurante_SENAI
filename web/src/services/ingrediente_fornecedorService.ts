// Chamadas HTTP para o recurso "ingrediente_fornecedor"
import { api } from './api';
import type { IngredienteFornecedor, IngredienteFornecedorCreate, IngredienteFornecedorUpdate } from '../types/ingrediente_fornecedor';

const BASE_PATH = '/ingrediente-fornecedor/';

export async function listarIngredienteFornecedor(): Promise<IngredienteFornecedor[]> {
  return api.get<IngredienteFornecedor[]>(BASE_PATH);
}

export async function obterIngredienteFornecedor(id: number): Promise<IngredienteFornecedor> {
  return api.get<IngredienteFornecedor>(`${BASE_PATH}${id}`);
}

export async function criarIngredienteFornecedor(payload: IngredienteFornecedorCreate): Promise<IngredienteFornecedor> {
  return api.post<IngredienteFornecedor>(BASE_PATH, payload);
}

export async function atualizarIngredienteFornecedor(id: number, payload: IngredienteFornecedorUpdate): Promise<IngredienteFornecedor> {
  return api.put<IngredienteFornecedor>(`${BASE_PATH}${id}`, payload);
}

export async function removerIngredienteFornecedor(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
