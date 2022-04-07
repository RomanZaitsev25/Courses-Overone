# Создайте словарь из строки ' An apple a day keeps the doctor away' следующим
# образом: в качестве ключей возьмите символы строки, а значениями пусть будут
# числа, соответствующие количеству вхождений данной буквы в строку.

a = 'An apple a day keeps the doctor away'
a = a.replace(' ', '')
b = {}
for i in a:
    b[i] = a.count(i)
print('New_dictionary:', b)
