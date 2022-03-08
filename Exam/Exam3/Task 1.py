# 1. Напишите функцию, которая проверяет: является ли слово палиндромом
def polidrom(word):
    word = word.replace(' ', '').lower()
    return 'Polidrom' if word == word[::-1] else 'No polidrom'


if __name__ == '__main__':
    print(polidrom(input('Add word:')))
