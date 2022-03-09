# Задача. Вводится строка и символ, используя цикл,
# вывести все символы до указанного символа,
# если же такого символа там нет, вывести всю строку

# 1 вариант решения
text = input('Enter the string:')
symbol = input('Enter the symbol:')
for i in text:
    if i != symbol:
        print(i)
    else:
        break

# 2 вариант решения
text = input('Enter the string:')
symbol = input('Enter the symbol:')
for i in text:
    if i == symbol:
        break
    print(i)
