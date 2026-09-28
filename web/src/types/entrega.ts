// Espelha app/schemas/entrega_schema.py do backend

export interface Entrega {
  id_entrega: number;
  id_pedido: number;
  id_funcionario?: number;
  endereco: string;
  taxa_entrega: number;
  data_hora?: string;
}

export interface EntregaCreate {
  id_pedido: number;
  id_funcionario?: number;
  endereco: string;
  taxa_entrega: number;
  data_hora?: string;
}

export type EntregaUpdate = Partial<EntregaCreate>;
