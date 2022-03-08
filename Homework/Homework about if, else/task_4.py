# Три числа вводится, вывидся наименьшее

num1 = int(input('Enter number:'))
num2 = int(input('Enter number:'))
num3 = int(input('Enter number:'))

if num1 < num2 or num1 < num3:
    print(num1)
elif num2 < num1 or num2 < num3:
    print(num2)
else:
    print(num3)
