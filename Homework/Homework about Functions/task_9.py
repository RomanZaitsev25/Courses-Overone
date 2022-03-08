# Если функция передаётся кортеж, то посчитать длинну всех слов.
# Если список, то посчитать кол-во бкув и чисел в нём
# Если число посчитать количество нечётных цифр в нём.
# Если строка посчитать количество букв.

def func(a):
    # Кортеж, tuple()
    t = 0
    # Список, lst[.....]
    c = 0
    # Числоб, int
    n = 0
    # Строка, str
    s = 0
    if type(a) is tuple:
        for i in a:
            g = len(i)
            t += g
        return f'Длинна всех его слов {t}'
    elif type(a) is list:
        for i in a:
            if type(i) is str:
                s += len(i)
            elif type(i) is int:
                n += 1
        return f'Количество букв {s}, Количество чисел {n}'
    elif type(a) is int:
        for i in str(a):
            i = int(i)
            if i % 2 != 0:
                n += 1
        return f'Количество нечётных цифр {n}'
    elif type(a) is str:
        q = len(a)
        return f'Количество букв {q}'


if __name__ == '__main__':
    print(func(('Hello', 'Word')))
    print(func(['Roman', 30, 5, 'Zaitsev']))
    print(func(30))
    print(func('Roman'))
