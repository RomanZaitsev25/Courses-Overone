# Создайте новую Базу данных.
# В нейсоздайте таблицу с тремя полями, два текстовых,
# одно – целое число.
# Число запрашивается с клавиатуры, а слова задаются
# статически.
# Выведите каждую запись в отдельную строку

import sqlite3

# Вводится число с клавиатуры
a = int(input('Enter a number:'))

# Импортируем библиотеку
conn = sqlite3.connect('name1.db')

# Создать объект, курсор,
# который позволяет взаимодействовать с БД
cursor = conn.cursor()

# Создадим таблицу, с тремя текстовыми полями(колонками)
cursor.execute('''
CREATE TABLE IF NOT EXISTS tab_1(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    col_1 TEXT,
    col_2 TEXT, 
    col_3 INTEGER
) ''')

# Вставляем слова в таблицу
cursor.execute(''' 
INSERT INTO tab_1(col_1, col_2, col_3)
VALUES ('hello', 'word', ?)
''', (a,))

# Сохраняем данные
conn.commit()

cursor.execute(''' 
SELECT * FROM tab_1
''')
# Вытягиваем все данные из таблицы 1
k = cursor.fetchall()
print(k)
for i in k:
    j = 0
    h = list(i)
    m = ' '.join(str(j) for j in h)
    print(m)
