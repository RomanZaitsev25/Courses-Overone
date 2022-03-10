# Задача. Вводится число, проверить является ли оно простым
# (делиться без остатка только на себя и на 1

a = int(input('Enter the number:'))
c = 0
for i in range(2, a + 1):
    if a % i == 0:
        c = i
        break
if c == a:
    print('Число простое')
else:
    print('Число не простое')
