"""Приложение БИБЛИОТЕКА для автоматизированного контроля литературных
источников в библиотеке. БД должна содержать таблицу Каталог с информацией о
книгах и следующей структурой записи: Код книги, Жанр, Страна издания, Серия, Автор,
Название книги, Год выпуска, Аннотация."""


import sqlite3 as sq
import data_library

# Создание базы данных
def init_library():
    with sq.connect('library.db') as con:
        cur = con.cursor()
        cur.execute('DROP TABLE IF EXISTS catalog') # База данных пересоздается после каждого нового запуска программы
        cur.execute('''CREATE TABLE IF NOT EXISTS catalog (
        id_book INTEGER PRIMARY KEY AUTOINCREMENT,
        genre varchar(20) NOT NULL,
        country varchar(20) NOT NULL,
        series INT(11) NOT NULL,
        author varchar(20) NOT NULL,
        name_book varchar(20) NOT NULL,
        data_release varchar(20) NOT NULL,
        annotation varchar(255)
        )''')

        cur.executemany('''INSERT INTO catalog (genre, country, series, author, name_book, data_release, annotation)
        VALUES (?, ?, ?, ?, ?, ?, ?)''', data_library.books)    # Добавление массива данных из файла data_library.py

        con.commit()


def show_all(con):  # Показать все элементы и значения таблицы catalog
    cur = con.cursor()
    cur.execute('SELECT * FROM catalog')
    for result in cur:
        print(result)
        print()
    print()

def search(con):    # Поиск книг по значениям столбцов
    cur = con.cursor()

    print("Выберите поле для поиска:")
    print("1. Жанр")
    print("2. Страна издания")
    print("3. Серия")
    print("4. Автор")
    print("5. Название книги")
    print("6. Год выпуска")
    print("7. Аннотация")

    values = input("Ваш выбор (1-7): ")

    fields = {
        '1': 'genre',
        '2': 'country',
        '3': 'series',
        '4': 'author',
        '5': 'name_book',
        '6': 'data_release',
        '7': 'annotation'
    }

    field_names_ru = {
        'genre': 'Жанр',
        'country': 'Страна издания',
        'series': 'Серия',
        'author': 'Автор',
        'name_book': 'Название книги',
        'data_release': 'Год выпуска',
        'annotation': 'Аннотация'
    }

    if values in fields:
        search_value = input(f'Введите значение для поиска по полю "{field_names_ru[fields[values]]}": ')
        field_name = fields[values]
        cur.execute(f"SELECT * FROM catalog WHERE {field_name} LIKE ?", ('%' + search_value + '%',))
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("Ничего не найдено.")
    else:
        print("Некорректный выбор.")

def insert_data(con):   # Ручной ввод новых записей
    genre = input("Жанр: ")
    country = input("Страна издания: ")
    series = input("Серия (номер): ")
    author = input("Автор: ")
    name_book = input("Название книги: ")
    data_release = input("Год выпуска: ")
    annotation = input("Аннотация: ")

    cur = con.cursor()
    cur.execute('''
        INSERT INTO catalog (genre, country, series, author, name_book, data_release, annotation)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (genre, country, series, author, name_book, data_release, annotation))

    con.commit()
    print("Книга успешно добавлена.")

def delete(con):     # Удаление записей
    cur = con.cursor()
    id_del = input("Введите id книги для удаления: ")
    cur.execute("DELETE FROM catalog WHERE id_book = ?", (id_del,))
    con.commit()
    print(f"Книга с id {id_del} удалена.")

def update(con):    # Редактирование существующих записей
    cur = con.cursor()
    id_upd = input("Введите id книги для обновления: ")

    print("Выберите поле для обновления:")
    print("1. Жанр")
    print("2. Страна издания")
    print("3. Серия")
    print("4. Автор")
    print("5. Название книги")
    print("6. Год выпуска")
    print("7. Аннотация")

    values = input("Ваш выбор (1-7): ")

    fields = {
        '1': 'genre',
        '2': 'country',
        '3': 'series',
        '4': 'author',
        '5': 'name_book',
        '6': 'data_release',
        '7': 'annotation'
    }

    field_names_ru = {
        'genre': 'Жанр',
        'country': 'Страна издания',
        'series': 'Серия',
        'author': 'Автор',
        'name_book': 'Название книги',
        'data_release': 'Год выпуска',
        'annotation': 'Аннотация'
    }

    if values in fields:
        new_value = input(f"Введите новое значение для {field_names_ru[fields[values]]}: ")
        field_name = fields[values]
        cur.execute(f"UPDATE catalog SET {field_name} = ? WHERE id_book = ?", (new_value, id_upd))
        con.commit()
        print(f"{field_names_ru[field_name]} книги с id {id_upd} обновлено.")
    else:
        print("Некорректный выбор.")

def menu (): # Главный пункт выбора действий
    with sq.connect('library.db') as con:
        while True:
            print('1. Показать весь каталог\n2. Поиск\n3. Добавление новой записи\n4. Удаление\n5. Редактирование\n6. Выход')
            menu_value = input('Выберите действие: ')
            if menu_value == '1':
                show_all(con)
            elif menu_value == '2':
                search(con)
            elif menu_value == '3':
                insert_data(con)
            elif menu_value == '4':
                delete(con)
            elif menu_value == '5':
                update(con)
            elif menu_value == '6':
                break
            else:
                print('\nОшибка в выборе.\n')


init_library()
menu()



