import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { API_BASE_URL } from '../api.config';
import { Course } from '../models/course.models';
import { Module } from '../models/module.model';
import { Block } from '../models/block.model';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  constructor(private http: HttpClient) {}

  getAllCourses(): Observable<any[]> {
    return this.http.get<any[]>(`${API_BASE_URL}/courses/`);
  }

  getCourses(): Observable<any[]> {
    return this.http.get<any[]>(`${API_BASE_URL}/client/1/course-progress/`);
  }

  getCourseById(courseId: number): Observable<any> {
    return this.http.get<any[]>(`${API_BASE_URL}/client/1/course-progress/`).pipe(
      map((courses) => courses.find((course) => course.id_course.id === courseId))
    );
  }

  deleteCourse(courseId: number): Observable<void> {
    return this.http.delete<void>(`${API_BASE_URL}/course/delete/${courseId}/`);
  }

  createCourse(title: string, idCreator: number): Observable<Course> {
    const body = { title, id_creator: idCreator };
    return this.http.post<Course>(`${API_BASE_URL}/course/create/`, body);
  }

  updateCourse(id: number, updatedCourse: Course): Observable<Course> {
    return this.http.put<Course>(`${API_BASE_URL}/course/update/${id}/`, updatedCourse);
  }

  getModulesForCourse(courseId: number): Observable<Module[]> {
    return this.http.get<Module[]>(`${API_BASE_URL}/api/course/${courseId}/modules/`);
  }

  createModule(courseId: number, numberOfDays: number): Observable<Module> {
    return this.http.post<Module>(`${API_BASE_URL}/api/module/create/`, {
      number_of_days: numberOfDays,
      id_course: courseId
    });
  }

  updateModule(moduleId: number, moduleData: Module): Observable<Module> {
    return this.http.put<Module>(`${API_BASE_URL}/api/module/update/${moduleId}/`, moduleData);
  }

  getBlocksForModule(moduleId: number): Observable<Block[]> {
    return this.http.get<Block[]>(`${API_BASE_URL}/api/module/${moduleId}/blocks/`);
  }

  createBlock(moduleId: number, blockData: {
    text_information: string, 
    images?: string[], 
    video?: string
  }): Observable<Block> {
    return this.http.post<Block>(`${API_BASE_URL}/api/block/create/`, {
      ...blockData,
      id_module: moduleId
    });
  }

  updateBlock(blockId: number, blockData: {
    text_information: string, 
    images?: string[], 
    video?: string
  }): Observable<Block> {
    return this.http.put<Block>(`${API_BASE_URL}/api/block/update/${blockId}/`, blockData);
  }

  deleteModule(moduleId: number): Observable<void> {
    return this.http.delete<void>(`${API_BASE_URL}/module/delete/${moduleId}/`);
  }

  deleteBlock(blockId: number): Observable<void> {
    return this.http.delete<void>(`${API_BASE_URL}/block/delete/${blockId}/`);
  }
}