// Espelha app/schemas/cupom_schema.py do backend

export interface Cupom {
  id_cupom: number;
  codigo: string;
  tipo_desconto: string;
  valor_desconto: number;
  data_inicio: string;
  data_fim?: string;
}

export interface CupomCreate {
  codigo: string;
  tipo_desconto: string;
  valor_desconto: number;
  data_inicio: string;
  data_fim?: string;
}

export type CupomUpdate = Partial<CupomCreate>;
