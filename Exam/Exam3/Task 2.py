# Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками
def credit_card(card):
    return '*' * len(card[:-4]) + card[-4:]


if __name__ == '__main__':
    print(credit_card((input('Enter your number of credit card:'))))
