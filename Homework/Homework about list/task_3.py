# У меня есть список. Найти все числа 20 и заменить на 100

lst = [20, 34, 45, 20, 45, 55, 4, 5, 20]

for i, symbol in enumerate(lst):
    if symbol == 20:
        lst[i] = 100
print(lst)

