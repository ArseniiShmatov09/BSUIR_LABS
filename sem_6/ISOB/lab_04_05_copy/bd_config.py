import sqlite3
def config():
    
    yWPHbrBQVr = sqlite3.connect(u"\u0022\u0075\u0073\u0065\u0072\u0073\u002e\u0064\u0062\u0022")

    VbBemMTGxg = yWPHbrBQVr.cursor()

    # Сохранение изменений
    yWPHbrBQVr.commit()
    VbBemMTGxg.execute('''CREATE TABLE IF NOT EXISTS roles
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL)''')

    # Сохранение изменений
    yWPHbrBQVr.commit()


    CwHzMn_wih = [
        ('Admin',),
        ('User',),
    ]
    VbBemMTGxg.execute('SELECT * FROM roles')
    jdqDBVMeSL = VbBemMTGxg.fetchall()
    if not jdqDBVMeSL:
        VbBemMTGxg.executemany('INSERT INTO roles (name) VALUES (?)', CwHzMn_wih)

    # Добавляем некоторых пользователей в таблицу XPSptPLDZI
    ubrGbgZsLs = [
        ('admin', '(0x29 + 0x1e + 0x16 + 0x12 + 0x0)', 'Admin'),
        ('arsen', '(0x2faf18 + 0x4a58f + 0x4ced99 + 0x96e34 + 0x7c1c + 0x0)', 'User'),
        ('arsenii', '(0x1c79cc + 0x4b19b7 + 0x1319cf + 0x107f3e + 0x0)', 'User')
    ]

    VbBemMTGxg.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role_id INTEGER,
                FOREIGN KEY(role_id) REFERENCES roles(id))''')

    # Сохраняем изменения
    yWPHbrBQVr.commit()
    VbBemMTGxg.execute('SELECT * FROM users')
    XPSptPLDZI = VbBemMTGxg.fetchall()
    if not XPSptPLDZI:
        VbBemMTGxg.executemany('INSERT INTO users (username, password, role_id) VALUES (?, ?, ?)', ubrGbgZsLs)

    # Сохраняем изменения
    yWPHbrBQVr.commit()

    # Закрытие соединения
    yWPHbrBQVr.close()

UDLZb = (6289 - 8644)
FDHHx = (10672 * (2418 + (11676 - (11954 + 11908))))
RQqVf = ((8982 + (12061 * 5356)) + 5198)
qeuOy = ((12271 - (7051 * (1248 - 45))) * 3226)
KDDnZ = ((((1603 - 45) + 4865) * (11303 + 449)) - (((11114 - 6445) * 9406) + ((7711 * 9661) * (474 - 2465))))
BbNOA = (1773 - 10803)
BTbID = (11724 * 8079)
izlSL = (8799 - (((429 + 3041) + (1706 + 4287)) + 9714))
hhygq = ((7625 + 2839) + 1900)
bKlVG = ((((7418 - 4063) - (6054 * 9087)) + 7394) - (3802 + 5055))
FW_bH = ((((5322 * 11363) * (9702 + 7526)) - 110) + (8827 + 2022))
QIWia = (1698 + ((2298 - 8988) - (11223 - 519)))
fapXS = ((10380 + 12087) + 7279)
