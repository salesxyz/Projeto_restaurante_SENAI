// Espelha app/schemas/uso_cupom_schema.py do backend

export interface UsoCupom {
  id_uso: number;
  id_cupom: number;
  id_pedido: number;
  data_hora: string;
}

export interface UsoCupomCreate {
  id_cupom: number;
  id_pedido: number;
  data_hora: string;
}

export type UsoCupomUpdate = Partial<UsoCupomCreate>;
