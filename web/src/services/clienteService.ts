// Chamadas HTTP para o recurso "cliente"
import { api } from './api';
import type { Cliente, ClienteCreate, ClienteUpdate } from '../types/cliente';

const BASE_PATH = '/cliente/';

export async function listarCliente(): Promise<Cliente[]> {
  return api.get<Cliente[]>(BASE_PATH);
}

export async function obterCliente(id: number): Promise<Cliente> {
  return api.get<Cliente>(`${BASE_PATH}${id}`);
}

export async function criarCliente(payload: ClienteCreate): Promise<Cliente> {
  return api.post<Cliente>(BASE_PATH, payload);
}

export async function atualizarCliente(id: number, payload: ClienteUpdate): Promise<Cliente> {
  return api.put<Cliente>(`${BASE_PATH}${id}`, payload);
}

export async function removerCliente(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
