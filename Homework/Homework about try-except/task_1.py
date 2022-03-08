# Введены 2 числа с клавиатуры. Поделить одно на другое.
# Обработать ошибку, деления на ноль, если нету ошибок то результат
# возвести в квадрат. Также используйте оператор Finally

try:
    a = int(input('Enter first number:'))
    b = int(input('Enter second number:'))
    c = a / b
except ZeroDivisionError:
    print('На ноль делить нельзя')
else:
    print(c ** 2)
finally:
    print('Have a nice day')
