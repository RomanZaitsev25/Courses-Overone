# Написать функцию и сделать так, что бы число секунд отображалось в виде
# дни:часы:мины:секунды
def convert(second):
    day = second // (24 * 3600)
    hour = second // 3600
    minute = second // 60
    second = 24 * 3600
    print('{}:Day\n{}:hour\n{}:minute\n{}:second'.format(day, hour,
                                                         minute, second))


if __name__ == '__main__':
    convert(int(input('Enter the seconds:')))
