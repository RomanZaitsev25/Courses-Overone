# Написать функцию, которая считает сколько глассных а сколько
# согласнных. Строку вводить с клавиатуры

def letters_vowels_and_consonants(lst):
    vowels = 'eyuioaёуеыаоэяию'
    vowels_count = 0
    consonants_count = 0
    for letters in lst:
        if letters in vowels:
            vowels_count += 1
        elif letters.isalpha():
            consonants_count += 1
    print('Vowels:', vowels_count)
    print('Consonants:', consonants_count)


if __name__ == '__main__':
    letters_vowels_and_consonants(str(input('Ввести с клавиатуры:')))
