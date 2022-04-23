# Решение задачи фебоначи числа 7
def feb(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return feb(n - 1) + feb(n - 2)


if __name__ == '__main__':
    print(feb(16))
