# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова,
# выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.

class Example:
    def __init__(self):
        # Список пустых глассных
        self.vowels = []

        # Список пустых соглассных
        self.consonants = []

        # Счётчик для гласснх
        self.v = 0
        # Счётчик для соглассных
        self.c = 0

        # Счётчик для чисел
        self.n = 0

    def func1(self, a):
        if type(a) is str:
            for i in a:
                if i in 'eyuioaёуеыаоэяию':
                    self.v += 1
                    self.vowels.append(i)
                else:
                    self.c += 1
                    self.consonants.append(i)
            print('Number of vowels:', self.v)
            print('Number of consonants:', self.c)
            print('Long a word:', self.func2(a))
            if (self.c * self.v) <= self.func2(a):
                print('All vowels:', self.v)
            else:
                print('All consonants:', self.c)
        if type(a) is int:
            for i in str(a):
                i = int(i)
                if i % 2 == 0:
                    self.n += 1
            print('Composition:', self.n * self.func2(a))

    def func2(self, a):
        return len(str(a))


if __name__ == '__main__':
    obj_example = Example()
    f = input('Write string or number:')
    if f.isalpha():
        obj_example.func1(f)
    elif f.isdigit():
        obj_example.func1(int(f))
