# Проект для Хакатона Б3
После клонирования репозитория необходимо запустить backend и frontend сервера.

## Backend на Django
1. Переход в директорию Django проекта 
```
cd django_backend
```
2. Создание виртуального окружения
```
python -m venv venv
```
3. Установка необходимых зависимостей
```
pip install -r requirements.txt
```
4. Запуск сервера
```
python manage.py runserver
```
**По умолчанию сервер запустится локально на адресе `http://127.0.0.1:8000/`**

## Frontend на Angular
1. Переход в директорию Angular проекта 
```
cd django_backend
```
2. Установка Angular
```
npm install -g @angular/cli
```
3. Установка зависимостей
```
npm install
```
4. В файле `api.config.ts` измените значение `BaseURL` согласно адресу Django сервера
5. После установки зависимостей запустите проект с помощью Angular CLI:
```
ng serve
```
**По умолчанию проект запустится локально на адресе `http://localhost:4200`**