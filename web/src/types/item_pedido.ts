// Espelha app/schemas/item_pedido_schema.py do backend

export interface ItemPedido {
  id_item: number;
  id_pedido: number;
  id_produto: number;
  id_variacao?: number;
  quantidade: number;
  observacao?: string;
}

export interface ItemPedidoCreate {
  id_pedido: number;
  id_produto: number;
  id_variacao?: number;
  quantidade: number;
  observacao?: string;
}

export type ItemPedidoUpdate = Partial<ItemPedidoCreate>;
