import csv
import sqlite3


def init():
    con = sqlite3.connect("phonebook.sqlite")
    cur = con.cursor()
    return [cur, con]


def create_table(cur, con):
    cur.execute('''
    CREATE TABLE IF NOT EXISTS phonebook(
        id INTEGER PRIMARY KEY,
        name  NOT NULL,
        phone TEXT UNIQUE NOT NULL,
        city TEXT DEFAULT NULL)
    ''')


def select_all(cur):
    return cur.execute('SELECT * FROM phonebook;')


def select_by_filter(cur, filter_p, value):
    return cur.execute(
        f'SELECT * FROM phonebook WHERE '
        f'{"name" if (value == "2") else "city"} LIKE "%{filter_p}%"')


def add_row(cur, row, con):
    cur.execute(f'INSERT INTO phonebook(name, phone, city) '
                f'VALUES ("{row["name"].lower()}","{row["phone"]}","{row["city"].lower()}");')
    con.commit()


def delete_row(cur, con, idx):
    cur.execute(f'DELETE FROM phonebook WHERE id = {idx}')
    con.commit()


def export_to_csv(db):
    with open('phonebook.csv', 'w', newline='', encoding='utf-8') as f:
        field_names = ['Имя', 'Номер телефона', 'Город']
        writer = csv.DictWriter(f, fieldnames=field_names)
        for row in db.fetchall():
            writer.writerow({'Имя': row[1], 'Номер телефона': row[2], 'Город': row[3]})
