// services/module.service.ts
import { Injectable } from '@angular/core';
import { Module } from '../models/module.model';

@Injectable({
  providedIn: 'root',
})
export class ModuleService {
  private modules: Module[] = [];

  getModules(): Module[] {
    return this.modules;
  }

  getModuleById(id: number): Module | undefined {
    return this.modules.find((module) => module.id === id);
  }

  addModule(module: Module): void {
    module.id = this.modules.length + 1;
    this.modules.push(module);
  }

  updateModule(id: number, updatedModule: Module): void {
    const index = this.modules.findIndex((module) => module.id === id);
    if (index !== -1) {
      this.modules[index] = updatedModule;
    }
  }

  deleteModule(id: number): void {
    this.modules = this.modules.filter((module) => module.id !== id);
  }
}