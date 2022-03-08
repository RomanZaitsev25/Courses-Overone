# Посчитать количество пробелов, без count

text = input('Enter new word:')
count_space = 0
for i in text:
    if i == ' ':
        count_space += 1
print(count_space)
