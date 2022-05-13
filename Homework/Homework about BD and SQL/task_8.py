# Создайте новую Базу данных.
# В ней создайте таблицу с четырьмя полями(имеющие название
# title,author,	price, amount), два текстовых,
# и два – целых чисел. Values(туда пишем название книги,
# автора, цен книги и количество) - должно быть состоять из 6 строк
# Все значения задаются динамически.
# Указать в запросе столбцы: Автор, Название, Количество;
# Указать новую цену (столбец sale);
# Посчитать затраты по акции: снижение цены + кофе (столбец Затраты);
# Посчитать выручку по акции (столбец Выручка);
# Округлить цены до 2х знаков после запятой;
# Отсортировать авторов и названия книг в алфавитном порядке.
import sqlite3

conn = sqlite3.connect('name8.db')

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
SELECT author AS Автор,
title AS Название, 
amount AS Количество,
round((price*0.8),2) AS "sale",
round((price*0.2*amount + amount*70),2) AS Затраты,
round(((amount*(price*0.8))-amount*70),2) AS Выручка
FROM book
WHERE author = "Булгаков М.А." OR author = "Достоевский Ф.М."
ORDER by 1, 2;
''')

k = cursor.fetchall()
print(k)

