# Калькулятор.
# Создайте класс, где реализованы функции(методы)
# математических операций. А также функция, для ввод данных.

class Calculator:
    # Инициализируем класс, наполнение значением.
    def __init__(self):
        self.input()

    def input(self):
        self.num = int(input('Веедите первое число:'))
        self.num2 = int(input('Введите второе число:'))

    def sum(self):
        return self.num + self.num2

    def minus(self):
        return self.num - self.num2

    def multiply(self):
        return self.num * self.num2

    def div(self):
        if self.num2 == 0:
            return 'Error'
        else:
            return self.num / self.num2


if __name__ == '__main__':
    calc_obj = Calculator()
    operation = input('Введите операцию:')
    if operation == '+':
        print(calc_obj.sum())
    elif operation == '-':
        print(calc_obj.minus())
    elif operation == '*':
        print(calc_obj.multiply())
    elif operation == '/':
        print(calc_obj.div())
    else:
        print('Error')
