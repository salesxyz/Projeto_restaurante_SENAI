// Espelha app/schemas/cargo_schema.py do backend

export interface Cargo {
  id_cargo: number;
  nome: string;
}

export interface CargoCreate {
  nome: string;
}

export type CargoUpdate = Partial<CargoCreate>;
