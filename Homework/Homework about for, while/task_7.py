# Задача. Посчитать в строке количество цифр,
# если их количество окажется больше половины всех символов,
# то вывести сумму этих цифр

# 1 Вариант решения
text = input('Enter the text:')
c = 0
s = 0
for i in text:
    if i.isdigit():
        c += 1
        s += int(i)
print('Count numbers:', c)
if c > len(text) // 2:
    print('Summa:', s)

# 2 Вариант решения
text = input('Введите текст:')
c = 0
for i in text:
    if i.isdigit():
        c += 1
print('Count numbers:', c)
s = 0
if c > len(text)//2:
    for i in text:
        if i.isdigit():
            s += int(i)
print('Summa:', s)

