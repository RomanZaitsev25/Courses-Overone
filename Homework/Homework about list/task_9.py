# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается,
# что любые два элемента, равные друг другу
# образуют одну пару, которую необходимо посчитать

lst = [1, 2, 3, 3, 5, 6]
n_count = 0
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] == lst[j]:
            n_count += 1
print(n_count)


