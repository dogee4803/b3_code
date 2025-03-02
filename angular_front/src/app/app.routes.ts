import { Routes } from '@angular/router';
import { MyCoursesComponent } from './pages/my-courses/my-courses.component';
import { CourseDetailComponent } from './pages/course-detail/course-detail.component';
import { CourseCreatorComponent } from './pages/course-creator/course-creator.component';
import { AllCoursesComponent  } from './pages/all-courses/all-courses.component';
import { AllClientsComponent  } from './pages/all-clients/all-clients.component';
import { HomeComponent } from './pages/home/home.component';
import { NotFoundComponent } from './pages/not-found/not-found.component';
import { CourseEditorComponent } from './pages/course-editor/course-editor.component';

export const routes: Routes = [
  { path: 'home', component: HomeComponent }, // Страница "Домой"
  { path: 'my_courses', component: MyCoursesComponent }, // Страница "Мои курсы"
  { path: 'course/:id', component: CourseDetailComponent }, // Страница курса

  { path: 'course-creator', component: CourseCreatorComponent }, // Конструктор курсов
  { path: 'course/:id/edit', component: CourseEditorComponent }, // Редактор курса

  { path: 'all-courses', component: AllCoursesComponent  }, //Курсы у админа
  { path: 'all-clients', component: AllClientsComponent  }, //Пользователи у админа


  { path: '', redirectTo: '/home', pathMatch: 'full' }, // Перенаправление с пустого пути на /home
  { path: '404', component: NotFoundComponent }, // Страница "404 Not Found"
  { path: '**', redirectTo: '/404' }, // Перенаправление всех несуществующих маршрутов на /404
];