# Вывести первые 13 чисел, которые кратные 13 и больше 100

c = 0
i = 100
while c < 13:
    if i % 13 == 0:
        print(i)
        c += 1
    i += 1