# Необходимо удалить пустые строки из списка строк

lst = ['Roman', '', 'Home', 23, '', 45]
i = list(filter(None, lst))
print(i)
