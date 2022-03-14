# Вводится 2 числа с клавиатуры (от 1 до 20).
# Так же генерируется 2 числа рандомно.
# Посчитать, сколько раз пара введенных чисел с клавиатуры окажется больше
# рандомной пары. Проверку выполнить 7 раз.
# В случае равенства (количества, когда пара больше и всех остальных случаем)
# вывести случайные числа, полученные в 4 итерации.

import random

c = 0
for i in range(7):
    num1 = int(input('Enter number one:'))
    num2 = int(input('Enter number two:'))
    rand_num1 = random.randint(1, 21)
    rand_num2 = random.randint(1, 21)
    if num1 > rand_num1:
        c += 1
    if num2 > rand_num2:
        c += 1
    if i == 3:
        a = rand_num1
        b = rand_num2
if c == 7:
    print(a, b)