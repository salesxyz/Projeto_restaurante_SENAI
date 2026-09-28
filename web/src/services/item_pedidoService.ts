// Chamadas HTTP para o recurso "item_pedido"
import { api } from './api';
import type { ItemPedido, ItemPedidoCreate, ItemPedidoUpdate } from '../types/item_pedido';

const BASE_PATH = '/item-pedido/';

export async function listarItemPedido(): Promise<ItemPedido[]> {
  return api.get<ItemPedido[]>(BASE_PATH);
}

export async function obterItemPedido(id: number): Promise<ItemPedido> {
  return api.get<ItemPedido>(`${BASE_PATH}${id}`);
}

export async function criarItemPedido(payload: ItemPedidoCreate): Promise<ItemPedido> {
  return api.post<ItemPedido>(BASE_PATH, payload);
}

export async function atualizarItemPedido(id: number, payload: ItemPedidoUpdate): Promise<ItemPedido> {
  return api.put<ItemPedido>(`${BASE_PATH}${id}`, payload);
}

export async function removerItemPedido(id: number): Promise<void> {
  return api.del(`${BASE_PATH}${id}`);
}
