// Espelha app/schemas/ingrediente_fornecedor_schema.py do backend

export interface IngredienteFornecedor {
  id_ingrediente_fornecedor: number;
  id_ingrediente: number;
  id_fornecedor: number;
}

export interface IngredienteFornecedorCreate {
  id_ingrediente: number;
  id_fornecedor: number;
}

export type IngredienteFornecedorUpdate = Partial<IngredienteFornecedorCreate>;
