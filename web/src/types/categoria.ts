// Espelha app/schemas/categoria_schema.py do backend

export interface Categoria {
  id_categoria: number;
  nome: string;
}

export interface CategoriaCreate {
  nome: string;
}

export type CategoriaUpdate = Partial<CategoriaCreate>;
