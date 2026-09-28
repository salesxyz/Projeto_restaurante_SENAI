// Espelha app/schemas/historico_cargo_schema.py do backend

export interface HistoricoCargo {
  id_historico_cargo: number;
  id_funcionario: number;
  id_cargo: number;
  data_inicio: string;
  data_fim?: string;
}

export interface HistoricoCargoCreate {
  id_funcionario: number;
  id_cargo: number;
  data_inicio: string;
  data_fim?: string;
}

export type HistoricoCargoUpdate = Partial<HistoricoCargoCreate>;
