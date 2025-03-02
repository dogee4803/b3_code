// services/block.service.ts
import { Injectable } from '@angular/core';
import { Block } from '../models/block.model';

@Injectable({
  providedIn: 'root',
})
export class BlockService {
  private blocks: Block[] = [];

  getBlocks(): Block[] {
    return this.blocks;
  }

  getBlockById(id: number): Block | undefined {
    return this.blocks.find((block) => block.id === id);
  }

  addBlock(block: Block): void {
    block.id = this.blocks.length + 1;
    this.blocks.push(block);
  }

  updateBlock(id: number, updatedBlock: Block): void {
    const index = this.blocks.findIndex((block) => block.id === id);
    if (index !== -1) {
      this.blocks[index] = updatedBlock;
    }
  }

  deleteBlock(id: number): void {
    this.blocks = this.blocks.filter((block) => block.id !== id);
  }
}