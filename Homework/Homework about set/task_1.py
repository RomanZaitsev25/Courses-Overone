# Проверить если ли дубликаты в списки. Список вывести через клавиатуру.
a = [1, 4, 6, 7, 8, 4]
b = set(a)
if len(a) != len(b):
    print('В списке есть дубликаты')
else:
    print('В списке нет дубликатов')