// Espelha app/schemas/historico_status_schema.py do backend

export interface HistoricoStatus {
  id_historico: number;
  id_pedido: number;
  id_funcionario?: number;
  status: string;
  data_hora: string;
}

export interface HistoricoStatusCreate {
  id_pedido: number;
  id_funcionario?: number;
  status: string;
  data_hora: string;
}

export type HistoricoStatusUpdate = Partial<HistoricoStatusCreate>;
