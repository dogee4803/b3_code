import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Router } from '@angular/router';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-all-courses',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './all-courses.component.html',
  styleUrls: ['./all-courses.component.css'],
})
export class AllCoursesComponent implements OnInit {
  courses: any[] = [];

  constructor(
    private apiService: ApiService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.loadCourses();
  }

  loadCourses(): void {
    this.apiService.getAllCourses().subscribe((data) => {
      this.courses = data;
    });
  }

  deleteCourse(courseId: number): void {
    this.apiService.deleteCourse(courseId).subscribe(() => {
      this.loadCourses();
    });
  }

  editCourse(courseId: number): void {
    this.router.navigate(['/course', courseId, 'edit']);
  }
}