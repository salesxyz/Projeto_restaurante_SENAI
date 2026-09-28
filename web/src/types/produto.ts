// Espelha app/schemas/produto_schema.py do backend

export interface Produto {
  id_produto: number;
  id_categoria: number;
  nome: string;
  preco_base: number;
}

export interface ProdutoCreate {
  id_categoria: number;
  nome: string;
  preco_base: number;
}

export type ProdutoUpdate = Partial<ProdutoCreate>;
