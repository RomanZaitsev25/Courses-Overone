# Задача. В зависимости от выбора пользователя вычислить площадь круга,
# прямоугольника или треугольника. Для вычисоения площади каждой фигуры
# долна быть написана функция

from math import pi, sqrt


def square_circle():
    radius = float(input("Введите радиус: "))
    print(pi * (radius ** 2))


def square_rectangle():
    a = float(input("Введите длину: "))
    b = float(input("Введите ширину: "))
    print(a * b)


def square_triangle():
    a = float(input("Введите сторону a: "))
    b = float(input("Введите сторону b: "))
    c = float(input("Введите сторону c: "))
    p = (a + b + c) / 2
    print(sqrt(p * (p - a) * (p - b) * (p - c)))


if __name__ == '__main__':
    choice = input("Введите к, п или т чтобы вычислить площадь: ")
    if choice == "к":
        square_circle()
    elif choice == "п":
        square_rectangle()
    elif choice == "т":
        square_triangle()
    else:
        print("Недопустимый ввод")
