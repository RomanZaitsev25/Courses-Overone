# Вывести символы строки, которые находятся на чётных индексах

text = input('Enter new word:')
for i in range(len(text)):
    if i % 2 == 0:
        print(text[i])
