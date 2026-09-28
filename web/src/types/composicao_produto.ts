// Espelha app/schemas/composicao_produto_schema.py do backend

export interface ComposicaoProduto {
  id_composicao: number;
  id_produto: number;
  id_ingrediente: number;
  quantidade_utilizada: number;
}

export interface ComposicaoProdutoCreate {
  id_produto: number;
  id_ingrediente: number;
  quantidade_utilizada: number;
}

export type ComposicaoProdutoUpdate = Partial<ComposicaoProdutoCreate>;
