import { Component } from '@angular/core';
import { MenuItem } from 'primeng/api';
import { ToggleSwitchModule } from 'primeng/toggleswitch';
import { MenubarModule } from 'primeng/menubar';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [MenubarModule, ToggleSwitchModule, FormsModule, CommonModule],
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  items: MenuItem[] = [
    { label: 'Домой', icon: 'pi pi-home', routerLink: '/home' },
    { label: 'Мои курсы', icon: 'pi pi-list', routerLink: '/my_courses' },
    { label: 'Конструктор', icon: 'pi pi-wrench', routerLink: '/course-creator'},
    { label: 'Все курсы', icon: 'pi pi-list', routerLink: '/all-courses' },
    { label: 'Пользователи', icon: 'pi pi-users', routerLink: '/all-clients' },
  ];

  isDarkTheme = false;

  toggleTheme(): void {
    this.isDarkTheme = !this.isDarkTheme;
    this.applyTheme();
  }

  private applyTheme(): void {
    const element = document.querySelector('html');
    if (element) {
      if (this.isDarkTheme) {
        element.classList.add('my-app-dark');
      } else {
        element.classList.remove('my-app-dark');
      }
    }
  }
}