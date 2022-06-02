# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены
# два динамических свойства: lang - язык и #2 letters - список букв.
# Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет
# вызываться родительский метод __init__().
# В качестве пар-рров ему будут передаваться обозначение языка(например, 'En')
# и строка, состоящая из всех букв алфавита
# (можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num,
# которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве
# параметра и определять, относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе классе
# он будет возвращать значение свойства __letters_num. -
# 6. Создайте статический метод example(), который будет возвращать пример
# текста на английском языке.
# Тесты:
# 1. Создайте объект класса EngAlphabet
# 2. Напечатайте буквы алфавита для этого объекта
# 3. Выведите количество букв в алфавите
# 4. Проверьте, относится ли буква F к английскому алфавиту
# 5. Проверьте, относится ли буква Щ к английскому алфавиту
# 6. Выведите пример текста на английском языке

import string


class Alphabet:

    def __init__(self, language, list_letters):
        self.lang = language
        self.letters = list(list_letters)

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self, ):
        super().__init__('En', string.ascii_uppercase)

    # Is_en_letter - определяем, относится ли данная буква к алфавиту
    def is_en_letter(self, letter):
        if letter in self.letters:
            return True
        else:
            False

    # Letters_num -  количество букв
    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        return 'I love my mother'


if __name__ == '__main__':
    engAlphabet_obj = EngAlphabet()
    print(engAlphabet_obj.letters)
    print(engAlphabet_obj.letters_num())
    print(engAlphabet_obj.is_en_letter('F'))
    print(engAlphabet_obj.is_en_letter('Ъ'))
    print(engAlphabet_obj.example())
