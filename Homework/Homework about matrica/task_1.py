# Дана матрица. вывести на экран 3 столбец матрицы
A = [[1, 4, 5, 12],
     [-5, 8, 9, 0],
     [-6, 7, 11, 19]]
column = []
for row in A:
    column.append(row[2])

print('3rd column=', column)
