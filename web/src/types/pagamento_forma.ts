// Espelha app/schemas/pagamento_forma_schema.py do backend

export interface PagamentoForma {
  id_pagamento_forma: number;
  id_pagamento: number;
  id_forma_pagamento: number;
}

export interface PagamentoFormaCreate {
  id_pagamento: number;
  id_forma_pagamento: number;
}

export type PagamentoFormaUpdate = Partial<PagamentoFormaCreate>;
