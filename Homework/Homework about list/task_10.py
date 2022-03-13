# Дан список рандомных чисел, а так же с клавиатуры
# поступает число, необходимо сместить элементы списка вправа
# по индексам на это число пример: [1, 2, 3, 4, 5] число 2,
# результат: [4, 5, 1, 2, 3] (реальная задача с собеседования)

lst = [1, 2, 3, 4, 5, 6]
number = int(input('Enter the numbers:'))
if number < len(lst):
    lst = lst[-number:] + lst[:-number]
    print(lst)
else:
    number = number - len(lst)
    lst = lst[-number:] + lst[:-number]
print('New list:', lst)
