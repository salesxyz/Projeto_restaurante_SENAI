// Chamadas HTTP para o recurso "forma_pagamento"
import { api } from './api';
import type { FormaPagamento, FormaPagamentoCreate, FormaPagamentoUpdate } from '../types/forma_pagamento';

const BASE_PATH = '/forma-pagamento/';

export async function listarFormaPagamento(): Promise<FormaPagamento[]> {
  return api.get<FormaPagamento[]>(BASE_PATH);
}

export async function obterFormaPagamento(id: number): Promise<FormaPagamento> {
  return api.get<FormaPagamento>(`${BASE_PATH}${id}`);
}

export async function criarFormaPagamento(payload: FormaPagamentoCreate): Promise<FormaPagamento> {
  return api.post<FormaPagamento>(BASE_PATH, payload);
}

export async function atualizarFormaPagamento(id: number, payload: FormaPagamentoUpdate): Promise<FormaPagamento> {
  return api.put<FormaPagamento>(`${BASE_PATH}${id}`, payload);
}

export async function removerFormaPagamento(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
