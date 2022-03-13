# С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько
# согласных. В случае равенства вывести на экран все гласные буквы.

text = input('Введите текст:').lower()
vowels = 'eyuioaёуеыаоэяию'
vowels_count = 0
consonants_count = 0
for symbol in text:
    if symbol in vowels:
        vowels_count += 1
    elif symbol.isalpha():
        consonants_count += 1
print('Consonants_count:{}\nVowels_count:{} '.format(consonants_count,
                                                     vowels_count))
if vowels_count == consonants_count:
    for symbol in text:
        if symbol in vowels:
            print(symbol, end=' ')
