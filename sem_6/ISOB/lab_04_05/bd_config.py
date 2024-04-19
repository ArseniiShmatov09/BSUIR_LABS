import sqlite3
def config():
    
    con = sqlite3.connect("users.db")

    c = con.cursor()

    # Сохранение изменений
    con.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS roles
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL)''')

    # Сохранение изменений
    con.commit()


    roles_data = [
        ('Admin',),
        ('User',),
    ]
    c.execute('SELECT * FROM roles')
    roles = c.fetchall()
    if not roles:
        c.executemany('INSERT INTO roles (name) VALUES (?)', roles_data)

    # Добавляем некоторых пользователей в таблицу users
    users_data = [
        ('admin', '111', 'Admin'),
        ('arsen', '09120912', 'User'),
        ('arsenii', '09120912', 'User')
    ]

    c.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role_id INTEGER,
                FOREIGN KEY(role_id) REFERENCES roles(id))''')

    # Сохраняем изменения
    con.commit()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    if not users:
        c.executemany('INSERT INTO users (username, password, role_id) VALUES (?, ?, ?)', users_data)

    # Сохраняем изменения
    con.commit()

    # Закрытие соединения
    con.close()

