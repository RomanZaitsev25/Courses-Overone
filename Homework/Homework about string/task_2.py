# Выввести уникальный символ из строки

text = input('Enter new word:')
for i in text:
    if text.count(i) == 1:
        print(i)
