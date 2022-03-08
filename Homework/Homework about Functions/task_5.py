# Простейший калькулятор, с ведёнными двумя числами.
# Вввод с клавиатуры операции: +, -, /, * и два числа. Являются функциями
# Обработать ошибку деление наноль.
# Ноль использовать как заверщение программы(операции)

# Ввод через клавиатуру, первого числа
a = int(input('Enter a number one:'))
# Ввод через клавиатуру, второго числа
b = int(input('Enter a number two:'))
print('Arithmetic operations:', '+', '-', '/', '*')


# Анотирующая инструкция
def devite(a, b: int) -> str:
    if b == 0:
        return 'Error'
    else:
        return a / b


def multiply(a, b: int) -> str:
    return a * b


def plus(a, b: int) -> str:
    return a + b


def minus(a, b: int) -> str:
    return a - b


while True:
    x = input('Add an arithmetic operation:')
    if x == 0:
        break
    else:
        if x == '+':
            print('Result:', plus(a, b))

        if x == '-':
            print('Result:', minus(a, b))

        if x == '*':
            print('Result:', multiply(a, b))

        if x == '/':
            print('Result:', (a, b))
