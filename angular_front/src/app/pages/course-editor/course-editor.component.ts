import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { BreadcrumbModule } from 'primeng/breadcrumb';
import { MenuItem } from 'primeng/api';

import { ApiService } from '../../services/api.service';
import { CourseService } from '../../services/course.service';
import { Course } from '../../models/course.models';
import { Module } from '../../models/module.model';
import { Block } from '../../models/block.model';

@Component({
  selector: 'app-course-editor',
  templateUrl: './course-editor.component.html',
  styleUrls: ['./course-editor.component.css'],
  standalone: true,
  imports: [
    FormsModule, 
    CommonModule, 
    BreadcrumbModule
  ]
})
export class CourseEditorComponent implements OnInit {
  course: Course = { id: 0, title: '', modules: [] };
  breadcrumbItems: MenuItem[] = [];
  homeBreadcrumb: MenuItem = { 
    label: 'Курсы', 
    routerLink: '/all-courses' 
  };
  originalTitle: string = '';
  isTitleEditMode: boolean = false;

  constructor(
    private apiService: ApiService,
    private courseService: CourseService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    const courseId = this.route.snapshot.paramMap.get('id');
    if (courseId) {
      const parsedCourseId = Number(courseId);
      this.loadCourse(parsedCourseId);
    }
  }

  loadCourse(courseId: number): void {
    this.courseService.getCourseById(courseId).subscribe({
      next: (course) => {
        this.course = course;
        this.originalTitle = course.title;
        this.initBreadcrumbs(course);
        this.loadModules(courseId);
      },
      error: () => this.router.navigate(['/courses'])
    });
  }

  initBreadcrumbs(course: Course): void {
    this.breadcrumbItems = [
      { 
        label: 'Курсы', 
        routerLink: '/all-courses' 
      },
      { 
        label: course.title, 
        routerLink: `/course/${course.id}` 
      },
      { 
        label: 'Редактирование' 
      }
    ];
  }

  loadModules(courseId: number): void {
    this.apiService.getModulesForCourse(courseId).subscribe({
      next: (modules) => {
        this.course.modules = modules.map(module => ({
          ...module,
          blocks: module.blocks || []
        }));
      }
    });
  }

  editCourseTitle(): void {
    this.isTitleEditMode = true;
  }

  cancelTitleEdit(): void {
    this.course.title = this.originalTitle;
    this.isTitleEditMode = false;
  }

  updateCourseTitle(): void {
    if (this.course.title && this.course.title.trim() !== '' && this.course.title !== this.originalTitle) {
      this.courseService.updateCourse(this.course.id, this.course).subscribe({
        next: (updatedCourse) => {
          this.course = updatedCourse;
          this.originalTitle = updatedCourse.title;
          this.initBreadcrumbs(updatedCourse);
          
          alert('Название курса успешно обновлено');
          this.isTitleEditMode = false;
        },
        error: (error) => {
          this.course.title = this.originalTitle;
          alert('Не удалось обновить название курса');
          console.error(error);
          this.isTitleEditMode = false;
        }
      });
    } else {
      this.course.title = this.originalTitle;
      this.isTitleEditMode = false;
    }
  }

  saveCourse(): void {
    if (this.course.id) {
      this.courseService.updateCourse(this.course.id, this.course).subscribe({
        next: () => {
          this.saveModules();
        },
        error: () => alert('Не удалось сохранить курс')
      });
    }
  }

  saveModules(): void {
    const modulePromises = this.course.modules.map(module => this.saveModule(module));

    Promise.all(modulePromises)
      .then(() => {
        alert('Курс успешно сохранен');
        this.router.navigate(['/courses']);
      })
      .catch(() => alert('Не удалось сохранить модули'));
  }

  saveModule(module: Module): Promise<void> {
    return new Promise((resolve, reject) => {
      const saveAction = module.id 
        ? this.apiService.updateModule(module.id, module)
        : this.apiService.createModule(this.course.id, module.number_of_days || 10);

      saveAction.subscribe({
        next: (savedModule) => {
          module.id = savedModule.id;
          this.saveBlocks(module)
            .then(resolve)
            .catch(reject);
        },
        error: reject
      });
    });
  }

  saveBlocks(module: Module): Promise<void> {
    if (!module.id || !module.blocks?.length) return Promise.resolve();

    const blockPromises = module.blocks.map(block => 
      this.saveBlock(module.id!, block)
    );

    return Promise.all(blockPromises).then(() => {});
  }

  saveBlock(moduleId: number, block: Block): Promise<void> {
    return new Promise((resolve, reject) => {

      const saveAction = block.id
        ? this.apiService.updateBlock(block.id, block)
        : this.apiService.createBlock(moduleId, block);

      saveAction.subscribe({
        next: () => resolve(),
        error: reject
      });
    });
  }

  addModule(): void {
    this.course.modules.push({
      id: 0,
      title: 'Новый модуль',
      blocks: [],
      number_of_days: 10
    });
  }

  removeModule(index: number): void {
    this.course.modules.splice(index, 1);
  }

  addBlock(module: Module): void {
    if (!module.blocks) {
      module.blocks = [];
    }
    module.blocks.push({
      id: 0,
      text_information: 'Новый блок',
    });
  }

  removeBlock(module: Module, blockIndex: number): void {
    module.blocks.splice(blockIndex, 1);
  }
}