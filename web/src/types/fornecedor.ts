// Espelha app/schemas/fornecedor_schema.py do backend

export interface Fornecedor {
  id_fornecedor: number;
  nome: string;
  contato?: string;
}

export interface FornecedorCreate {
  nome: string;
  contato?: string;
}

export type FornecedorUpdate = Partial<FornecedorCreate>;
