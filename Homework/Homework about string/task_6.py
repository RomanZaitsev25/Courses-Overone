# Вводится строка, если там чётное количество слов,
# то сделайте буквы большимии, иначе сделать буквы маленькими,
# за исключением первой буквы каждого слова

# При вводе слова, удаляем лишние пробелы в начале и в конце
text = input('Enter new word:').strip()

# Определяем количество пробелов между слов
count_space = text.count(' ')

# Определяем количество слов, зная кол-во  пробелов
count_word = count_space + 1

if count_word % 2 == 0:
    text = text.upper()
else:
    text = text.title()
print(text)