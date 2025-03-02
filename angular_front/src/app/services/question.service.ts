// services/question.service.ts
import { Injectable } from '@angular/core';
import { Question } from '../models/question.model';

@Injectable({
  providedIn: 'root',
})
export class QuestionService {
  private questions: Question[] = [];

  getQuestions(): Question[] {
    return this.questions;
  }

  getQuestionById(id: number): Question | undefined {
    return this.questions.find((question) => question.id === id);
  }

  addQuestion(question: Question): void {
    question.id = this.questions.length + 1;
    this.questions.push(question);
  }

  updateQuestion(id: number, updatedQuestion: Question): void {
    const index = this.questions.findIndex((question) => question.id === id);
    if (index !== -1) {
      this.questions[index] = updatedQuestion;
    }
  }

  deleteQuestion(id: number): void {
    this.questions = this.questions.filter((question) => question.id !== id);
  }
}