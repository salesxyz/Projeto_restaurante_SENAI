// Espelha app/schemas/mesa_schema.py do backend

export interface Mesa {
  id_mesa: number;
  numero: number;
}

export interface MesaCreate {
  numero: number;
}

export type MesaUpdate = Partial<MesaCreate>;
