# Дан список.Выведите те его элементы, которые встречаются в списке 1 раз
lst = [1, 2, 3, 5, 6, 78, 5, 5]
new_lst = []
for i in lst:
    if lst.count(i) == 1:
        new_lst.append(i)
print('New list:', new_lst)
