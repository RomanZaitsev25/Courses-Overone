# Матрица 5 х 5. Найти строку с максимальной
# суммой элементов и вывести её номер.
import random

M = 5
N = 5
A = []
for i in range(M):
    A.insert(i, [])
    for j in range(N):
        A[i].insert(j, random.randint(1, 9))
print('{}'.format(A))

for i in range(M):
    print('-----', end='')
print()
max_sum = 0
row = 0
for i in range(M):
    s = 0
    for j in range(N):
        s += A[i][j]
    print(' {}'.format(s), end='')
    if s > max_sum:
        max_sum = s
        row = i
print()
print('Row number:', row + 1)
