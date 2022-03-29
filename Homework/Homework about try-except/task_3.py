# Ввод с клавиатуры. Если строка введённая с клавиатуры – это числа,
# то поделить первое на второе. Обработать ошибку деления на ноль.
# Если второе число 0, то программа запрашивает ввод чисел заново.
# Также если были введены буквы, то обработать исключение.
while True:
    a = input('Enter the first number:')
    b = input('Enter the second number:')
    try:
        result = int(a) / int(b)
    except ValueError:
        print('Write only numbers')
    except ZeroDivisionError:
        print('Enter the number again')
    else:
        print(result)
        break
