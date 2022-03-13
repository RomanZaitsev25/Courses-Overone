# 4.Пользователь вводит число.
# Определить, содержит ли список данное число x.
# Если содержит, то вывести на экран
# True, если не содержит, то вывести на экран False;

number = int(input('Enter the number:'))
lst = [12, 34, 56, 67, 45, 56]
if number in lst:
    print(True)
else:
    print(False)
