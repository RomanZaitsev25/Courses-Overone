# Функция которая при заданном целом числе n считает n+ nn+ nnn
def summa(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)


if __name__ == '__main__':
    summa(int(input('Enter the number:')))
