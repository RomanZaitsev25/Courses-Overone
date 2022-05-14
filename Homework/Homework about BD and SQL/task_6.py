# Создайте новую Базу данных.
# В ней создайте таблицу с четырьмя полями(имеющие название
# title,author,	price, amount), два текстовых,
# и два – целых чисел. Values(туда пишем название книги,
# автора, цен книги и количество) - должно быть состоять из 6 строк
# Все значения задаются динамически.
# Выбрать названия книг и авторов из таблицы book, для поля title задать
# имя(псевдоним) Название, для поля author –  Автор.
import sqlite3

conn = sqlite3.connect('name6.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS book(
    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    title TEXT,
    author TEXT, 
    price INTEGER,
    amount INTEGER
) ''')

cursor.execute(''' 
INSERT INTO book(title,	author,	price, amount)
VALUES ('Мастер и Маргарита', 'Булгаков М.А.', 670.99, 3),
    ('Белая гвардия', 'Булгаков М.А.', 540.50, 5),
    ('Идиот', 'Достоевский Ф.М.', 460.00, 10),
    ('Братья Карамазовы', 'Достоевский Ф.М.', 799.01, 3),
    ('Игрок', 'Достоевский Ф.М.', 480.50, 10),
    ('Стихотворения и поэмы', 'Есенин С.А.', 650.00, 15)
''')

conn.commit()

cursor.execute(''' 
Select title AS Название, author AS Автор FROM book
''')

k = cursor.fetchall()
print(k)

