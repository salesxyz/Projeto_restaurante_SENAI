// Espelha app/schemas/funcionario_schema.py do backend

export interface Funcionario {
  id_funcionario: number;
  id_cargo?: number;
  nome: string;
  contato?: string;
}

export interface FuncionarioCreate {
  id_cargo?: number;
  nome: string;
  contato?: string;
}

export type FuncionarioUpdate = Partial<FuncionarioCreate>;
