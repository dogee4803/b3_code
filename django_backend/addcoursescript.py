import sqlite3
from datetime import datetime

# Подключение к базе данных (или создание, если она не существует)
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()


# Функция для добавления курса
def add_course(title, make_date, id_creator_id):
    cursor.execute('''
    INSERT INTO apiapp_course (title, make_date, id_creator_id)
    VALUES (?, ?, ?)
    ''', (title, make_date, id_creator_id))
    conn.commit()

# Пример добавления данных
courses = [
    ("Python Basics", '2023-10-05', 1),
    ("Advanced Python", '2023-10-12', 2),
    ("Data Science with Python", '2023-10-01', 1)
]

for course in courses:
    add_course(*course)

# Закрытие соединения с базой данных
conn.close()