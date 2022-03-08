# Написать функцию season, принимающую 1 аргумент —
# номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или
# осень). Номер месяца вводить с клавиатуры.

def season(num_month: int) -> str:
    if num_month == 12 or 1 <= num_month <= 2:
        return 'Winter'
    elif 3 <= num_month <= 5:
        return 'Spring'
    elif 6 <= num_month <= 8:
        return 'Summer'
    elif 9 <= num_month <= 11:
        return 'Autumn'
    else:
        return 'add don not number'


if __name__ == '__main__':
    print(season(int(input('Add number of month:'))))
