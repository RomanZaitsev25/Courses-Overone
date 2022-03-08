# Создайте новую Базу данных
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Выберите случайную запись из БД
# Если каждое число данной записи чётное, то удалите эту
# запись, если нечётное, то обновите данные в ней на(2,2)

import sqlite3
import random

# Импортируем библиотеку
conn = sqlite3.connect('name3.db')

# Создать объект, курсор,
# который позволяет взаимодействовать с БД
cursor = conn.cursor()

# Создадим таблицу, с двумя числовыми полями(колонками)
cursor.execute('''
CREATE TABLE if NOT EXISTS tab_1(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col_1 INTEGER,
    col_2 INTEGER
) ''')
i = 0
x = random.randint(1, 9)
y = random.randint(1, 9)

# Вставляем числа в таблицу
cursor.execute(''' 
INSERT INTO tab_1(col_1, col_2)
VALUES (?, ?)
''', (x, y))
conn.commit()

cursor.execute('''
Select id FROM tab_1
''')
k = cursor.fetchall()
print('List id in Tuple:', k)

r = random.choice(k)
print('Random id:', *r)

cursor.execute('''
    Select col_1, col_2 From tab_1 WHERE id=?
''', (r))
oo = cursor.fetchall()
print('Values:', oo)
new = []
for i in oo:
    print(i)
    for j in i:
        print(j)
        new.append(j)
if new[0] % 2 == 0 and new[1] % 2 == 0:
    cursor.execute('''Delete From tab_1 Where id=?''', (r))
    conn.commit()
else:
    cursor.execute('''Update tab_1 Set col_1 = 2, col_2 = 2 Where id=?''', (r))
    conn.commit()
cursor.execute('''Select id, col_1, col_2 FROM tab_1''')
oo = cursor.fetchall()
print(oo)
