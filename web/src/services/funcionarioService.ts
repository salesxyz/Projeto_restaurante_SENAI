// Chamadas HTTP para o recurso "funcionario"
import { api } from './api';
import type { Funcionario, FuncionarioCreate, FuncionarioUpdate } from '../types/funcionario';

const BASE_PATH = '/funcionario/';

export async function listarFuncionario(): Promise<Funcionario[]> {
  return api.get<Funcionario[]>(BASE_PATH);
}

export async function obterFuncionario(id: number): Promise<Funcionario> {
  return api.get<Funcionario>(`${BASE_PATH}${id}`);
}

export async function criarFuncionario(payload: FuncionarioCreate): Promise<Funcionario> {
  return api.post<Funcionario>(BASE_PATH, payload);
}

export async function atualizarFuncionario(id: number, payload: FuncionarioUpdate): Promise<Funcionario> {
  return api.put<Funcionario>(`${BASE_PATH}${id}`, payload);
}

export async function removerFuncionario(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
