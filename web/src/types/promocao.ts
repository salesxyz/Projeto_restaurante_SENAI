// Espelha app/schemas/promocao_schema.py do backend

export interface Promocao {
  id_promocao: number;
  descricao: string;
  data_inicio: string;
  data_fim?: string;
}

export interface PromocaoCreate {
  descricao: string;
  data_inicio: string;
  data_fim?: string;
}

export type PromocaoUpdate = Partial<PromocaoCreate>;
