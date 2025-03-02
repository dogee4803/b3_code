import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CourseService } from '../../services/course.service';
import { Course } from '../../models/course.models';

@Component({
  selector: 'app-course-creator',
  templateUrl: './course-creator.component.html',
  styleUrls: ['./course-creator.component.css'],
  standalone: true,
  imports: [FormsModule]
})
export class CourseCreatorComponent {
  newCourse: Course = { id: 0, title: '', modules: []};

  constructor(
    private courseService: CourseService,
    private router: Router
  ) {}

  addCourse(): void {
    this.courseService.addCourse(this.newCourse).subscribe({
      next: (createdCourse) => {
        this.router.navigate(['/course', createdCourse.id, 'edit']);
      },
      error: (err) => {
        console.error('Ошибка при создании курса:', err);
      },
    });
  }
}