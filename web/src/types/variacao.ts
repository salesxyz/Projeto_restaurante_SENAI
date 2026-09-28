// Espelha app/schemas/variacao_schema.py do backend

export interface Variacao {
  id_variacao: number;
  id_produto: number;
  nome: string;
  valor_adicional: number;
}

export interface VariacaoCreate {
  id_produto: number;
  nome: string;
  valor_adicional: number;
}

export type VariacaoUpdate = Partial<VariacaoCreate>;
