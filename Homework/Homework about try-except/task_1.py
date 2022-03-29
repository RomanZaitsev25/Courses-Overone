# Введены 2 числа с клавиатуры. Поделить одно на другое.
# Обработать ошибку, деления на ноль, если нету ошибок то результат
# возвести в квадрат. Также используйте оператор Finally

try:
    a = int(input('Enter the first number:'))
    b = int(input('Enter the second number:'))
    c = a / b
except ZeroDivisionError:
    print('You can not divide by zero')
else:
    print(c ** 2)
finally:
    print('Have a nice day')
