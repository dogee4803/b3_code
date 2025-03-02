import { Block } from './block.model';

export interface Module {
  id: number;
  title: string;
  blocks: Block[];
  deadline?: Date;
  number_of_days?: number;
  id_course?: number;
}