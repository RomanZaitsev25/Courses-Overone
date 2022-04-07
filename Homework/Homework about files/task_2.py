# Создать текстовый файл, записать в него построчные данные,
# которые вводит пользователь. Окончание ввода, служит пустая строка.

# 1 Вариант решения
with open('file_2.txt', 'w') as f:
    while True:
        line = input('Enter string:')
        if line == '':
            break
        else:
            f.write(line + '\n')
