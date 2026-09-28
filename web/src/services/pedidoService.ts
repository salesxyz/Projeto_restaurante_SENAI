// Chamadas HTTP para o recurso "pedido"
import { api } from './api';
import type { Pedido, PedidoCreate, PedidoUpdate } from '../types/pedido';

const BASE_PATH = '/pedido/';

export async function listarPedido(): Promise<Pedido[]> {
  return api.get<Pedido[]>(BASE_PATH);
}

export async function obterPedido(id: number): Promise<Pedido> {
  return api.get<Pedido>(`${BASE_PATH}${id}`);
}

export async function criarPedido(payload: PedidoCreate): Promise<Pedido> {
  return api.post<Pedido>(BASE_PATH, payload);
}

export async function atualizarPedido(id: number, payload: PedidoUpdate): Promise<Pedido> {
  return api.put<Pedido>(`${BASE_PATH}${id}`, payload);
}

export async function removerPedido(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
