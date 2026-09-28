// Espelha app/schemas/forma_pagamento_schema.py do backend

export interface FormaPagamento {
  id_forma_pagamento: number;
  nome: string;
}

export interface FormaPagamentoCreate {
  nome: string;
}

export type FormaPagamentoUpdate = Partial<FormaPagamentoCreate>;
