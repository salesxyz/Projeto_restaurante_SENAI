// Espelha app/schemas/adicional_schema.py do backend

export interface Adicional {
  id_adicional: number;
  nome: string;
  preco: number;
}

export interface AdicionalCreate {
  nome: string;
  preco: number;
}

export type AdicionalUpdate = Partial<AdicionalCreate>;
