# Функция, вычисляющая среднее арифметическое
# элеметов списка. Список Должен состоять
# из случайных чиссел, длинной 10 элементов
import random


def average(num_list):
    list_summa = 0
    for num in num_list:
        list_summa += num
    return list_summa / len(num_list)


if __name__ == '__main__':
    num_list = []
    for num in range(10):
        num_list.append(random.randint(1, 100))
    print(num_list)
    print(average((num_list)))
