import sqlite3
def config():
    
    tpCLxEhGAu = sqlite3.connect("users.db")

    ewauuNHBky = tpCLxEhGAu.cursor()

    # Сохранение изменений
    tpCLxEhGAu.commit()
    ewauuNHBky.execute('''CREATE TABLE IF NOT EXISTS roles
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL)''')

    # Сохранение изменений
    tpCLxEhGAu.commit()


    ruCSNnaTTj = [
        ('Admin',),
        ('User',),
    ]
    ewauuNHBky.execute('SELECT * FROM roles')
    sbqvSiCyGS = ewauuNHBky.fetchall()
    if not sbqvSiCyGS:
        ewauuNHBky.executemany('INSERT INTO roles (name) VALUES (?)', ruCSNnaTTj)

    # Добавляем некоторых пользователей в таблицу jnbcnwNAAc
    gxSaOusbGn = [
        ('admin', '(0x52 + 0x1d + 0x0)', 'Admin'),
        ('arsen', '(0x557eaf + 0x2ef4b5 + 0x5a02f + 0x118fd + 0x0)', 'User'),
        ('arsenii', '(0x6885b6 + 0x1ee901 + 0x2b811 + 0x105c8 + 0x0)', 'User')
    ]

    ewauuNHBky.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role_id INTEGER,
                FOREIGN KEY(role_id) REFERENCES roles(id))''')

    # Сохраняем изменения
    tpCLxEhGAu.commit()
    ewauuNHBky.execute('SELECT * FROM users')
    jnbcnwNAAc = ewauuNHBky.fetchall()
    if not jnbcnwNAAc:
        ewauuNHBky.executemany('INSERT INTO users (username, password, role_id) VALUES (?, ?, ?)', gxSaOusbGn)

    # Сохраняем изменения
    tpCLxEhGAu.commit()

    # Закрытие соединения
    tpCLxEhGAu.close()

CIGXh = (3027 * 2718)
PLSDQ = (12007 + 970)
BKMji = ((10919 + 1283) + ((1298 + (4458 * 9469)) * 3118))
IreRJ = (4085 * (((510 - 5680) * 4684) * 2749))
VTKZf = (5604 * (9956 - 8189))
yvCLy = (2038 * (((4220 - 153) + 176) + ((5404 * 10500) + 7726)))
JHMJp = (4977 - 4242)
NVWHk = ((((8099 + 9851) - (1517 - 10159)) * 8673) * ((5250 * (1391 + 6100)) - 8922))
v_ARa = (9772 - ((8333 * (11719 + 11790)) + ((4603 + 493) * (11323 + 4072))))
CviEl = (10578 * (((5798 + 2700) - 11186) + ((2549 * 451) - (4326 * 4524))))
MDAUR = (((50 - 6546) - 3616) - (((8763 - 7295) + 5498) - 11615))
wOEYS = (4084 * 2169)
VwZTL = (11721 + 1396)
