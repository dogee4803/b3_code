import sqlite3

# Подключение к базе данных (если файла нет, он будет создан)
conn = sqlite3.connect('db.sqlite3')  # Укажите путь к вашей базе данных
cursor = conn.cursor()


# Данные для добавления клиентов
clients_data = [
    ('Иванов', 'Иван', 'Иванович', 'ivanov@example.com', 1),  # Администратор
    ('Петров', 'Петр', 'Петрович', 'petrov@example.com', 1),  # Администратор
    ('Сидорова', 'Мария', 'Ивановна', 'sidorova@example.com', 0),  # Обычный пользователь
    ('Козлов', 'Алексей', 'Сергеевич', 'kozlov@example.com', 0),  # Обычный пользователь
]

# Добавление клиентов в таблицу
cursor.executemany('''
INSERT INTO apiapp_client (surname, name, patronymic, email, is_admin)
VALUES (?, ?, ?, ?, ?);
''', clients_data)

# Сохранение изменений
conn.commit()

# Закрытие соединения с базой данных
conn.close()

print("Клиенты успешно добавлены в базу данных!")