import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent {
  features = [
    {
      icon: 'pi pi-book',
      title: 'Широкий выбор курсов',
      description: 'Изучайте новые навыки с нашими экспертами.',
    },
    {
      icon: 'pi pi-users',
      title: 'Сообщество учащихся',
      description: 'Общайтесь с другими студентами и делитесь знаниями.',
    },
    {
      icon: 'pi pi-graduation-cap',
      title: 'Сертификаты',
      description: 'Получайте сертификаты по завершении курсов.',
    },
  ];
}