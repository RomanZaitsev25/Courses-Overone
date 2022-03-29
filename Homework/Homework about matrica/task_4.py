# Матрица M x N, можно задать статически.
# Элементы заполняются случайными числами.
# Вводить с клавиатуры число и если оно есть в матрице,
# то вывести индекс строки и колонки в которой оно находится
import random

M = 3
N = 3
A = []
for i in range(M):
    A.insert(i, [])
    for j in range(N):
        A[i].insert(j, random.randint(1, 9))
print(A)
num = int(input('Enter tne number:'))
for i in range(M):
    for j in range(N):
        if j == num:
            print(num)
