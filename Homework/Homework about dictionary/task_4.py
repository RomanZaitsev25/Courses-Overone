# Даны два списка одинаковой длины. Необходимо создать из
# них словарь таким образом, чтобы элементы первого списка были ключами,
# а элементы второго — соответственно значениями нашего словаря

key = ['Roman', 'Yana', 'Lena']
values = [30, 27, 59]
d = dict(zip(key, values))
print(d)
print(dict(zip(['Roman', 'Yana', 'Lena'], [30, 27, 59])))
