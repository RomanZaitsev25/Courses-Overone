# Создайте новую Базу данных.
# В ней создайте таблицу с четырьмя полями(имеющие название
# title,author,	price, amount), два текстовых,
# и два – целых чисел. Values(туда пишем название книги,
# автора, цен книги и количество) - должно быть состоять из 6 строк
# Все значения задаются динамически
# Вывести  автора и название  книг, количество которых принадлежит интервалу
# от 2 до 14 (включая границы). Информацию  отсортировать сначала по авторам
# (в обратном алфавитном порядке), а затем по названиям книг (по алфавиту).

import sqlite3

conn = sqlite3.connect('name9.db')

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
SELECT title, author FROM book
WHERE amount BETWEEN 2 and 14
ORDER by author DESC, title DESC;''')

r = cursor.fetchall()
print(r)