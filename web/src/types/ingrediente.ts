// Espelha app/schemas/ingrediente_schema.py do backend

export interface Ingrediente {
  id_ingrediente: number;
  nome: string;
  quantidade_estoque: number;
  unidade_medida: string;
}

export interface IngredienteCreate {
  nome: string;
  quantidade_estoque: number;
  unidade_medida: string;
}

export type IngredienteUpdate = Partial<IngredienteCreate>;
