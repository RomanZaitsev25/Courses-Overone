# Создайте метод класса для работы с БД
# В БД если передан 1 аргумент, вставить в таблицу запись с числом 3
# Если переданы 2 аргумента: проверить или второй
# аргумент является числом. Если условие верно, то
# удалить первую запись с БД
# Если переданы 2 аргумента, их значения не известны, а 3
# является числом, то обновить на число 77 запись 3

import sqlite3

conn = sqlite3.connect('name4.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tab_1(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    col_1 INTEGER
) ''')
conn.commit()
cursor.execute('''
SELECT * fROM tab_1
''')
k = cursor.fetchall()
print(k)


class A:
    def baz_d(self, a=None, b=None, c=None):
        if a is not None and b is None and c is None:
            cursor.execute('''
                INSERT INTO tab_1(col_1)
                Values(3)
                ''')
            conn.commit()

        elif a is not None and b is not None and c is None:
            if type(b) is int:
                cursor.execute('''
                    DELETE FROM tab_1 WHERE id=1
                ''')
                conn.commit()

        elif a is not None and b is not None and type(c) is int:
            cursor.execute('''
                UPDATE tab_1 SET col_1=77 WHERE id=3''')
            conn.commit()


if __name__ == '__main__':
    a_obj = A()
    a_obj.baz_d('1', '1', 1)
    cursor.execute('''
        SELECT * FROM TAB_1
    ''')
    k = cursor.fetchall()
    print(k)
