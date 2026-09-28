// Espelha app/schemas/pagamento_schema.py do backend

export interface Pagamento {
  id_pagamento: number;
  id_pedido: number;
  valor_pago: number;
}

export interface PagamentoCreate {
  id_pedido: number;
  valor_pago: number;
}

export type PagamentoUpdate = Partial<PagamentoCreate>;
