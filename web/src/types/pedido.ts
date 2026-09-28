// Espelha app/schemas/pedido_schema.py do backend

export interface Pedido {
  id_pedido: number;
  id_cliente?: number;
  id_mesa?: number;
  data_hora: string;
  origem_pedido: string;
  status_atual: string;
}

export interface PedidoCreate {
  id_cliente?: number;
  id_mesa?: number;
  data_hora: string;
  origem_pedido: string;
  status_atual: string;
}

export type PedidoUpdate = Partial<PedidoCreate>;
