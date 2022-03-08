# Создайте функции, которая будет считать суммму чисел в списке.

def sum_number():
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    s = 0
    for i in a:
        s += i
    print(s)


if __name__ == '__main__':
    sum_number()
