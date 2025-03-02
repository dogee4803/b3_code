import { Injectable } from '@angular/core';
import { ApiService } from './api.service';
import { Course } from '../models/course.models';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class CourseService {
  constructor(private apiService: ApiService) {}

  getCourses(): Observable<Course[]> {
    return this.apiService.getCourses();
  }

  addCourse(course: Course): Observable<Course> {
    return this.apiService.createCourse(course.title, 1);
  }

  updateCourse(id: number, updatedCourse: Course): Observable<Course> {
    return this.apiService.updateCourse(id, updatedCourse);
  }

  deleteCourse(id: number): Observable<void> {
    return this.apiService.deleteCourse(id);
  }

  getCourseById(id: number): Observable<Course> {
    return this.apiService.getCourseById(id);
  }
}