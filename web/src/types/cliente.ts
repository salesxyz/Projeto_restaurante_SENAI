// Espelha app/schemas/cliente_schema.py do backend

export interface Cliente {
  id_cliente: number;
  nome: string;
  contato?: string;
  endereco?: string;
}

export interface ClienteCreate {
  nome: string;
  contato?: string;
  endereco?: string;
}

export type ClienteUpdate = Partial<ClienteCreate>;
