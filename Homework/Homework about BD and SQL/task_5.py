# Создать таблицу в Базе Данных с тремя колонками
# (id, 2 - text, 3 - text).
# Заполнить её с помощью INSERT данными (3 записи).
# Удалить с помощью DELETE 2 запись. Обновить значения
# 3-ей записи на: hello world с помощью UPDATE
# *Записать данные с таблицы в файл в три колонки.
# Первая – id, вторая и третья с данными.

import sqlite3

conn = sqlite3.connect('name8.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS tab_1(
    id Integer PRIMARY KEY AUTOINCREMENT,
    col_1 TEXT,
    col_2 Text
)''')

cursor.execute('''
INSERT INTO tab_1 (col_1, col_2)
VALUES('Roman', 'Zaitsev'),
('Roman', 'Zaitsev'),
('Roman', 'Zaitsev')
''')
conn.commit()

cursor.execute('''
SELECT * FROM tab_1
''')
k = cursor.fetchall()
print(k)

cursor.execute('''
DELETE FROM tab_1 WHERE id = 2
''')
conn.commit()

cursor.execute('''
SELECT * FROM tab_1
''')
k = cursor.fetchall()
print(k)

cursor.execute('''
UPDATE tab_1 SET col_2 = 'hello world' WHERE id=3
''')
conn.commit()

cursor.execute('''
SELECT * FROM tab_1
''')
k = cursor.fetchall()
print(k)
