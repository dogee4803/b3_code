// services/answer.service.ts
import { Injectable } from '@angular/core';
import { Answer } from '../models/answer.model';

@Injectable({
  providedIn: 'root',
})
export class AnswerService {
  private answers: Answer[] = [];

  getAnswers(): Answer[] {
    return this.answers;
  }

  getAnswerById(id: number): Answer | undefined {
    return this.answers.find((answer) => answer.id === id);
  }

  addAnswer(answer: Answer): void {
    answer.id = this.answers.length + 1;
    this.answers.push(answer);
  }

  updateAnswer(id: number, updatedAnswer: Answer): void {
    const index = this.answers.findIndex((answer) => answer.id === id);
    if (index !== -1) {
      this.answers[index] = updatedAnswer;
    }
  }

  deleteAnswer(id: number): void {
    this.answers = this.answers.filter((answer) => answer.id !== id);
  }
}