# Введите два числа с клавиатуры. Поделите одно на другое.
# Обрааботайде деление на ноль, преобразование и общее исключение
try:
    a = int(input('Enter first number:'))
    b = int(input('Enter second number:'))
    c = a / b
except ZeroDivisionError:
    print('На ноль делить нельзя')
except ValueError:
    print('Вводятся только целочислленные значения')
except Exception:
    print('Произошла ошибка')
else:
    print(с)
