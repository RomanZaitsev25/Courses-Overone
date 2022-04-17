# Написать функцию is_prime,  принимающей 1 аргумент - число 0 до 1000б и
# возвращаючая True, если простое, и False - иначе

def is_prime(number: int) -> bool:
    divider = 2
    while divider < number:
        if number % divider == 0:
            return False
        divider += 1
    return True


if __name__ == '__main__':
    print(is_prime(int(input('Enter the number:'))))