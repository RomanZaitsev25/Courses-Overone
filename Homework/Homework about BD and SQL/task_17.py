# Создайте новую Базу данных.
# В ней создайте таблицу с пятью полями(имеющие название
# name, city, per_diem, date_first, date_last), шесть текстовых,
# и один – целых чисел. Values(туда пишем имена, городаб дата отправления
# и прибытия и стоимость) - должно быть состоять из 20 строк
# Все значения задаются динамически.

import sqlite3

conn = sqlite3.connect('name16.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS travel(
    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT,
    city TEXT, 
    per_diem INTEGER,
    date_first TEXT,
    date_last TEXT
) ''')

cursor.execute(''' 
INSERT INTO travel (name, city, per_diem, date_first, date_last)
VALUES ('Баранов П.Е.','Москва',700 , '2020-01-12', '2020-01-17'),
('Абрамова К.А.','Владивосток',450 , '2020-01-14', '2020-01-27'),
('Семенов И.В.','Москва',700 , '2020-01-23', '2020-01-31'),
('Ильиных Г.Р.','Владивосток', 450, '2020-01-12', '2020-02-02'),
('Колесов С.П.','Москва',700 , '2020-02-01', '2020-02-06'),
('Баранов П.Е.','Москва', 700, '2020-02-14', '2020-02-22'),
('Абрамова К.А.','Москва', 700, '2020-02-23', '2020-03-01'),
('Лебедев Т.К.','Москва', 700, '2020-03-03', '2020-03-06'),
('Колесов С.П.','Новосибирск',450 , '2020-02-27', '2020-03-12'),
('Семенов И.В.','Санкт-Петербург',700 , '2020-03-29', '2020-04-05'),
('Абрамова К.А.','Москва',700 , '2020-04-06', '2020-04-14'),
('Баранов П.Е.','Новосибирск',450 , '2020-04-18', '2020-05-04'),
('Лебедев Т.К.','Томск',450 , '2020-05-20', '2020-05-31'),
('Семенов И.В.','Санкт-Петербург',700 , '2020-06-01', '2020-06-03'),
('Абрамова К.А.','Санкт-Петербург', 700, '2020-05-28', '2020-06-04'),
('Федорова А.Ю.','Новосибирск',450 , '2020-05-25', '2020-06-04'),
('Колесов С.П.','Новосибирск', 450, '2020-06-03', '2020-06-12'),
('Федорова А.Ю.','Томск', 450, '2020-06-20', '2020-06-26'),
('Абрамова К.А.','Владивосток', 450, '2020-07-02', '2020-07-13'),
('Баранов П.Е.','Воронеж', 450, '2020-07-19', '2020-07-25');
''')

cursor.execute('''
SELECT * FROM travel;
''')

k = cursor.fetchall()
print(k)