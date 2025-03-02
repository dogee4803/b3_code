import { Module } from './module.model';

export interface Course {
  id: number;
  title: string;
  modules: Module[];
}