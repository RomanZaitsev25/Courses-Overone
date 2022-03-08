# Вводится два числа с клавы, вывести True,
# если расстояние между ними 135 иначе False

num1 = int(input('Enter number:'))
num2 = int(input('Enter number:'))
if num1 - num2 == 135 or num1 - num2 == -135:
    print(True)
else:
    print(False)
