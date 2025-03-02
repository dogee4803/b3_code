import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';
import { CardModule } from 'primeng/card';
import { ButtonModule } from 'primeng/button';

@Component({
  selector: 'app-course-detail',
  standalone: true,
  imports: [CommonModule, CardModule, ButtonModule],
  templateUrl: './course-detail.component.html',
  styleUrls: ['./course-detail.component.css']
})
export class CourseDetailComponent implements OnInit {
  course: any;
  courseId!: number;

  constructor(
    private route: ActivatedRoute,
    private apiService: ApiService
  ) {}

  ngOnInit(): void {
    this.courseId = +this.route.snapshot.paramMap.get('id')!;
    this.loadCourse();
  }

  loadCourse(): void {
    this.apiService.getCourseById(this.courseId).subscribe(
      (data) => {
        this.course = data;
      },
      (error) => {
        console.error('Ошибка при загрузке курса:', error);
      }
    );
  }
}