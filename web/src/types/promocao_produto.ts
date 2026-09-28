// Espelha app/schemas/promocao_produto_schema.py do backend

export interface PromocaoProduto {
  id_promocao_produto: number;
  id_promocao: number;
  id_produto: number;
  id_cupom?: number;
  preco_promocional: number;
  data_inicio?: string;
  data_fim?: string;
}

export interface PromocaoProdutoCreate {
  id_promocao: number;
  id_produto: number;
  id_cupom?: number;
  preco_promocional: number;
  data_inicio?: string;
  data_fim?: string;
}

export type PromocaoProdutoUpdate = Partial<PromocaoProdutoCreate>;
