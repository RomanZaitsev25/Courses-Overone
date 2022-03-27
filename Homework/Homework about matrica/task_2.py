# Создать матрицу M x N, где M и N вводятся с клавиатуры. +
# Элементы матрицы заполнить случайными числами.
# Сделать читабельный вывод матрицы.
import random

M = int(input('M(row): '))
N = int(input('N(column): '))

A = []
for i in range(M):
    A.insert(i, [])
    for j in range(N):
        A[i].insert(j, random.randint(1, 100))
print(A)
for i in range(M):
    for j in range(N):
        print(A[i][j], end='')
    print()





# for i in range(M):
#     A.insert(i, [])
#     for j in range(N):
#         A[i].insert(j, random.randint(1, 100))
# print(A)
# for i in range(M):
#     for j in range(N):
#         print(A[i][j], end='')
#     print()