# С клавиатуры вводится 7 значное число. Если четных цифр в нем больше, чем
# нечетных, то найти сумму всех его цифр, если нечетных больше, то найти
# произведение 1 3 и 6 цифры.

num = input('Введите число:')
# Чётное
even = 0
# Нечётное
odd = 0
s = 0
for i in num:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
    s += int(i)
if even > odd:
    print('Summa:', s)
else:
    print('Composition:', int(num[1]) * int(num[3]) * int(num[6]))
