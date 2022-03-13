# Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится
# в веденном с клавиатуры слове. (Пример HjkLM- 1 пара нижнего,
# 1 пара верхнего), а также сколько всего букв в слове,
# сколько гласных и согласных.

text = input('Enter the text:').lower()
# Количество пар верхнего и нижнего регистра
c = 0
# Итератор
i = 0
vowels = 'eyuioaуеыаоэяию'
vowels_count = 0
consonants_count = 0
while i < len(text) - 1:
    if text[i].isupper() and text[i + 1].isupper() or text[i].islower() and \
            text[i + 1].islower():
        c += 1
        i += 2
    else:
        i += 1
for i in text:
    if i in vowels:
        vowels_count += 1
    else:
        consonants_count += 1
print('Number_of_pairs: {}\nVowels_count: {}\n'
      'Consonants_count: {}'.format(c, vowels_count, consonants_count))



