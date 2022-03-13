# Посчитать, сколько раз встречается определенная цифра в числах. Количество
# введенных чисел и искомая цифра задаются с клавиатуры. Числа выбираются
# рандомно.
import random

num = input('Цифра:')
num_count = int(input('Число:'))
c = 0
for i in range(num_count):
    a = str(random.randint(1, 10))
    c += a.count(num)
print(c)
