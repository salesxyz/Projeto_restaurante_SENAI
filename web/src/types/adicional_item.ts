// Espelha app/schemas/adicional_item_schema.py do backend

export interface AdicionalItem {
  id_adicional_item: number;
  id_item: number;
  id_adicional: number;
  quantidade: number;
}

export interface AdicionalItemCreate {
  id_item: number;
  id_adicional: number;
  quantidade: number;
}

export type AdicionalItemUpdate = Partial<AdicionalItemCreate>;
