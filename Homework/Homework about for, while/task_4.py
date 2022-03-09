# Задача.Вводится число, вывести все числа от 0 до введенного числа,
# квадрат которых не превышает введенное число

number = int(input('Enter the number:'))
for i in range(0, number):
    if i * i < number:
        print(i)
