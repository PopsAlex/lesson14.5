import sqlite3

connection = sqlite3.connect('database_for_bot.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')

    products = (('Волжанка', 'Вода питьевая', 100, 1), ('Бодрянка', 'Вода питьевая', 200, 2),
                ('Ульянка', 'Вода питьевая', 300, 3), ('Герольштайнер', 'Вода мегапитьевая', 400, 4))

    for i in products:
        check_product = cursor.execute('SELECT * FROM Products WHERE id=?', (i[3],))
        if check_product.fetchone() is None:
            cursor.execute('INSERT INTO Products (title, description, price) VALUES(?, ?, ?)', i[0:3])

    connection.commit()
    # connection.close()


def get_all_products():
    initiate_db()
    return cursor.execute('SELECT * FROM Products')


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()


def is_included(username):
    check_username = cursor.execute('SELECT username FROM Users WHERE username=?', (username,))
    if check_username.fetchone() is None:
        return False
    else:
        return True


connection.commit()