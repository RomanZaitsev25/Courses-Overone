# Создайте новую Базу данных.
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Посчитайте среднее арифметическое всех элементов без учёта id
# Если среднее арифметическое больше количества
# записей в БД, то удалите четвёртую запись БД.


import sqlite3
import random

conn = sqlite3.connect('name2.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tab_1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    col_1 INTEGER, 
    col_2 INTEGER
) ''')

i = 0
x = random.randint(1, 10)
y = random.randint(1, 10)

cursor.execute('''
INSERT INTO tab_1(col_1,col_2) 
VALUES (?,?)
''', (x, y))

conn.commit()

cursor.execute('''SELECT col_1,col_2 FROM tab_1''')
k = cursor.fetchall()
print('List tuple:', k)
s = 0
for i in k:
    for j in i:
        s += j
print('SUM', s)

sr = (s / (len(k) * 2))
print(sr)
if sr > len(k):
    cursor.execute('''DELETE FROM tab_1 WHERE id=4''')
conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)
