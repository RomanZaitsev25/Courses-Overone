# Введите два числа с клавиатуры. Поделите одно на другое.
# Обрааботайде деление на ноль, преобразование и общее исключение
try:
    a = int(input('Enter the first number:'))
    b = int(input('Enter the second number:'))
    c = a / b
except ZeroDivisionError:
    print('You can not divide by zero')
except ValueError:
    print('Вводятся только целочислленные значения')
except Exception:
    print('Произошла ошибка')
else:
    print(c)
