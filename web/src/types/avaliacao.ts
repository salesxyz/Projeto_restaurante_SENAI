// Espelha app/schemas/avaliacao_schema.py do backend

export interface Avaliacao {
  id_avaliacao: number;
  id_pedido: number;
  nota: number;
  comentario?: string;
}

export interface AvaliacaoCreate {
  id_pedido: number;
  nota: number;
  comentario?: string;
}

export type AvaliacaoUpdate = Partial<AvaliacaoCreate>;
