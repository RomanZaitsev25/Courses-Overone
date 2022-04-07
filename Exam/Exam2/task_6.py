# Напишите программу, демонстрирующую работу try\except\finally
try:
    a = int(input('Enter the number:'))
    b = int(input('Enter the number:'))
    c = int(input('Enter the number:'))
except ValueError:
    print('Write only numbers')
try:
    g = (a / b + c) * 2
except ZeroDivisionError:
    print('Division by Zero, will be mistake')
except NameError:
    print('Only number')
else:
    print(g)
finally:
    print('Happy New Year')
