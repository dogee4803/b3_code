import { Answer } from './answer.model';

export interface Question {
  id: number;
  text: string;
  image?: string;
  answers: Answer[];
  isMultipleChoice: boolean;
}