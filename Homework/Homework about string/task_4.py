# Подсчитать количество маленьких букв

text = input('Enter new word:')
letter_count = 0
for i in text:
    if i.islower():
        letter_count += 1
print(letter_count)
