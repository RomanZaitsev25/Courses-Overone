# Определить является ли слово полидромом

word = input('Enter word:')
word = word.lower()
word = word.replace(' ', '')
if word == word[::-1]:
    print('Полидром')
else:
    print('Не полидром')