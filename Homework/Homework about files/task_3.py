# В текстовом файле посчитать количество строк,
# а для каждой строки кол-во символов

f = open('file_3.txt', 'r')
lines = f.readlines()
print('Line_count:', len(lines))
for line_number, line in enumerate(lines, start=1):
    len_of_line = len(line.replace('\n', ' '))
# Выведем результат двумя методами
    print(f'Line № {line_number} has len:{len_of_line}')
    print('Line № {} has len:{}'.format(line_number, len_of_line))
f.close()