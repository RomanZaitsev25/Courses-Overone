# Три числа вводится c клавиатуры, вывидся наибольшее

num1 = int(input('Enter number_1:'))
num2 = int(input('Enter number_2:'))
num3 = int(input('Enter number_3:'))

if num1 > num2 or num1 > num3:
    print(num1)
elif num3 > num2 or num3 > num1:
    print(num3)
else:
    print(num2)
