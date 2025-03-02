import { Question } from './question.model';

export interface Block {
  id: number;
  text_information: string;
  images?: string[];
  video?: string;
  id_module?: number;
}