import sqlite3

# Подключение к базе данных (или создание, если она не существует)
conn = sqlite3.connect('db.sqlite3')  # Замените 'your_database.db' на имя вашей базы данных
cursor = conn.cursor()

# Данные для вставки в таблицу apiapp_course
courses_data = [
    ('2023-10-01', 1, 1, 0),
    ('2023-10-05', 1, 2, 0),
    ('2023-10-10', 1, 3, 0),
    ('2023-10-15', 2, 4, 0),
    # Добавьте другие записи по мере необходимости
]

# SQL-запрос для вставки данных
insert_query = '''
INSERT INTO apiapp_currentcourse (connect_date, id_client_id, id_course_id, progress)
VALUES (?, ?, ?, ?);
'''

# Вставка данных
cursor.executemany(insert_query, courses_data)

# Сохранение изменений
conn.commit()

# Закрытие соединения
conn.close()

print("Данные успешно добавлены в таблицу apiapp_course.")